#!/usr/bin/env python3
"""
gsw_lookup.py — CLI for querying the GSW anchor graph by topic.

Usage:
  python3 scripts/gsw_lookup.py "phase transitions and critical phenomena"
  python3 scripts/gsw_lookup.py "entropy in living systems" --top-k 15
  python3 scripts/gsw_lookup.py "AdS/CFT" --json

Output: ranked canonical sources connected to the topic via the wiki's anchor
graph. Surfaces co-citation hubs, cross-domain bridges, and IC/unanchored gaps.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Make src/ importable
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "src"))

from analysis.anchor_query import find_anchors_for_topic, expand_via_co_citation  # noqa: E402


def _domain_str(domains: list[str]) -> str:
    if not domains:
        return "—"
    if len(domains) == 1:
        return domains[0]
    return f"{len(domains)}-domain bridge: " + " + ".join(domains)


def render_text(result: dict, query: str, expand: bool = False) -> None:
    print()
    print("=" * 78)
    print(f"GSW lookup: {query}")
    print("=" * 78)

    seed = result["seed_entries"]
    print(f"\n{len(seed)} wiki entries semantically related to this topic:\n")
    for e in seed:
        ic = "  [IC]" if e["internal_construction"] else ""
        anchor_tag = f"  ({e['n_anchors']} anchors)" if e["n_anchors"] else "  (UNANCHORED)"
        domain = e["primary_domain"] or "—"
        print(f"  {e['entry_id']:<8} score={e['score']}  {domain:<22}  {e['title'][:55]}{anchor_tag}{ic}")

    sources = result["canonical_sources"]
    if not sources:
        print("\n(No canonical sources anchored to these entries.)")
        return

    print(f"\n--- Canonical sources connected to this topic ({len(sources)}) ---\n")
    print(f"{'#ent':>4} {'src':<10} {'identifier':<35} {'role':<22} {'tier':<5} {'conf':<6} title")
    for s in sources:
        title = (s["title"] or "")[:50]
        role = s["canonical_role"] or "(no role)"
        print(f"  {s['n_entries_in_topic']:>3} "
              f"{s['source']:<10} {s['identifier']:<35} {role:<22} "
              f"t{s['tier']}    {s['confidence']:<6} {title}")

    hubs = result["co_citation_hubs"]
    if hubs:
        print(f"\n--- Co-citation hubs (sources spanning 2+ topic entries): {len(hubs)} ---")
        for s in hubs:
            print(f"  {s['n_entries_in_topic']} entries via {s['source']}:{s['identifier'][:50]}")
            print(f"    -> {', '.join(s['entries_in_topic'])}")
            if expand:
                # Show all OTHER entries that share this anchor
                others = expand_via_co_citation(s["source"], s["identifier"],
                                                exclude_entries=s["entries_in_topic"])
                if others:
                    other_ids = [o["entry_id"] for o in others[:8]]
                    extra = f" (+{len(others)-8})" if len(others) > 8 else ""
                    print(f"    also anchors: {', '.join(other_ids)}{extra}")

    bridges = result["cross_domain_bridges"]
    if bridges:
        print(f"\n--- Cross-domain bridges (sources spanning 2+ primary domains): {len(bridges)} ---")
        for s in bridges:
            print(f"  {_domain_str(s['domains_spanned'])}")
            print(f"    {s['source']}:{s['identifier'][:50]}")
            print(f"    -> {', '.join(s['entries_in_topic'])}")

    if result["internal_constructions"]:
        ic = result["internal_constructions"]
        print(f"\n--- Internal constructions in topic: {len(ic)} ---")
        print(f"  {', '.join(ic)}")
        print("  (wiki-internal vocabulary, no GSW equivalent)")

    if result["unanchored"]:
        un = result["unanchored"]
        print(f"\n--- Unanchored topic entries (gap targets): {len(un)} ---")
        print(f"  {', '.join(un)}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Query the GSW anchor graph by topic.",
    )
    parser.add_argument("query", help="Natural-language topic or question")
    parser.add_argument("--top-k", type=int, default=10,
                        help="Max wiki entries to surface (default 10)")
    parser.add_argument("--chunks", type=int, default=30,
                        help="Chunks to retrieve from ChromaDB (default 30)")
    parser.add_argument("--expand", action="store_true",
                        help="For each co-citation hub, also list other entries that share the anchor")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON instead of human-readable output")
    args = parser.parse_args()

    result = find_anchors_for_topic(
        args.query, top_k_entries=args.top_k, chunks_per_query=args.chunks,
    )

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        render_text(result, args.query, expand=args.expand)


if __name__ == "__main__":
    main()

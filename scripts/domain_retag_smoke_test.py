"""
Domain Retagging — Smoke Test — 2026-04-17

Dry-run over 20 entries to:
- Validate the ID-prefix-to-domain mapping
- Validate the domain-string-to-canonical-tag mapping
- Exercise the primacy rule (ID prefix first, hierarchy fallback)
- Sort multi-domain lists in foundation-first hierarchy order
- Measure time commitment so we can plan the full 278-entry pass

NO INSERTS. Produces a markdown report listing proposed tags per entry,
confidence, and flags for manual review.

Output: docs/prior_art_reviews/DOMAIN_RETAG_SMOKE_TEST.md
"""

from __future__ import annotations
import sqlite3
import re
import time
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
REPORT_PATH = Path("docs/prior_art_reviews/DOMAIN_RETAG_SMOKE_TEST.md")


# ====================================================================
# GSW Hierarchy — foundation-first ordering of the 10 top-level domains
# Lower rank = more foundational
# ====================================================================
HIERARCHY_RANK = {
    "formal_logic":          1,
    "mathematics":           2,
    "information_theory":    3,
    "statistics_probability":4,
    "computer_science":      5,
    "physics":               6,
    "chemistry":             7,
    "biology":               8,
    "earth_sciences":        9,
    "networks_systems":     10,
}


# ====================================================================
# ID Prefix -> canonical tag_path mapping
# When the ID prefix unambiguously identifies a domain (sub-tag preferred)
# ====================================================================
ID_PREFIX_TO_TAG = {
    # Biology
    "BIO":  "biology",
    "NE":   "biology.neuroscience",
    "BR":   "biology.neuroscience",

    # Chemistry
    "CHEM": "chemistry",
    "CR":   "chemistry",          # crystallography
    "MS":   "chemistry.materials",
    "KC":   "chemistry.physical",

    # Mathematics
    "MATH": "mathematics",

    # Information theory
    "INFO": "information_theory",
    "IT":   "information_theory",  # distinct IT-prefix cluster in the wiki

    # Statistics
    "STAT": "statistics_probability",

    # Computer science
    "CS":   "computer_science",

    # Formal logic
    "FL":   "formal_logic",

    # Physics - cosmology / gravity
    "GV":   "physics.cosmology",
    "GT":   "physics.cosmology",   # G-prefix for gravity
    "HB":   "physics.cosmology",   # HB = black holes / horizons

    # Physics - classical
    "CM":   "physics.classical",
    "AM":   "physics.classical",   # analytical mechanics
    "EM":   "physics.classical",
    "FM":   "physics.classical",   # fluid mechanics
    "OP":   "physics.classical",   # optics
    "RD":   "physics.classical",   # radiation / thermo
    "TD":   "physics.classical",   # thermodynamics

    # Physics - modern
    "QM":   "physics.modern",
    "RG":   "physics.modern",      # renormalization group
    "DM":   "physics.cosmology",   # dark matter
    "GL":   "physics.classical",   # assumed gas laws; confirm during review

    # Earth sciences
    "ES":   "earth_sciences",

    # P / Q / Ax / Om — no deterministic prefix; rely on domain string
    "P":    None,
    "Q":    None,
    "Ax":   None,
    "Om":   None,
}


# ====================================================================
# Domain-string -> canonical tag(s) mapping
# Maps the 44 existing free-text domain strings to a list of canonical
# tags (ordered as originally written; re-sorted by hierarchy later)
# ====================================================================
DOMAIN_STRING_TO_TAGS = {
    # single-domain
    "physics":                               ["physics"],
    "biology":                               ["biology"],
    "information":                           ["information_theory"],
    "chemistry":                             ["chemistry"],
    "mathematics":                           ["mathematics"],
    "computer science":                      ["computer_science"],
    "networks":                              ["networks_systems"],
    "earth sciences":                        ["earth_sciences"],
    "geometry":                              ["mathematics.geometry_topology"],
    "cosmology":                             ["physics.cosmology"],
    "astronomy":                             ["physics.cosmology"],

    # two-domain
    "formal logic · mathematics":            ["formal_logic", "mathematics"],
    "physics · information":                 ["physics", "information_theory"],
    "chemistry · physics":                   ["chemistry", "physics"],
    "physics · cosmology":                   ["physics.cosmology"],
    "physics · chemistry":                   ["physics", "chemistry"],
    "information · mathematics":             ["information_theory", "mathematics"],
    "computer science · mathematics":        ["computer_science", "mathematics"],
    "physics · mathematics":                 ["physics", "mathematics"],
    "mathematics · physics":                 ["mathematics", "physics"],
    "information · physics":                 ["information_theory", "physics"],
    "mathematics · information":             ["mathematics", "information_theory"],
    "physics · biology":                     ["physics", "biology"],
    "mathematics · computer science":        ["mathematics", "computer_science"],
    "geometry · physics":                    ["mathematics.geometry_topology", "physics"],
    "geometry · biology":                    ["mathematics.geometry_topology", "biology"],
    "geometry · networks":                   ["mathematics.geometry_topology", "networks_systems"],
    "chemistry · biology":                   ["chemistry", "biology"],
    "biology · information":                 ["biology", "information_theory"],
    "earth sciences · biology":              ["earth_sciences", "biology"],
    "earth sciences · networks":             ["earth_sciences", "networks_systems"],

    # three-domain and more
    "physics · mathematics · information":   ["physics", "mathematics", "information_theory"],
    "information · mathematics · physics":   ["information_theory", "mathematics", "physics"],
    "physics · information · networks":      ["physics", "information_theory", "networks_systems"],
    "physics · information · mathematics":   ["physics", "information_theory", "mathematics"],
    "physics · chemistry · biology":         ["physics", "chemistry", "biology"],
    "physics · biology · networks":          ["physics", "biology", "networks_systems"],
    "biology · physics · networks · information": [
        "biology", "physics", "networks_systems", "information_theory"
    ],
    "biology · physics · information":       ["biology", "physics", "information_theory"],
    "geometry · biology · networks":         ["mathematics.geometry_topology", "biology", "networks_systems"],

    # comma-separated / long-form — confidence should be MEDIUM or LOW
    "biology, scaling laws":                 ["biology", "networks_systems"],
    "scaling laws, fractals, networks":      ["networks_systems", "mathematics.geometry_topology"],
    "information geometry, statistical physics, networks": [
        "information_theory", "physics.modern.statistical_mechanics", "networks_systems"
    ],
    "information geometry, finance, non-equilibrium thermodynamics": [
        "information_theory", "statistics_probability", "physics.modern.statistical_mechanics"
    ],
}


# ====================================================================
# Helpers
# ====================================================================
def top_level_of(tag_path: str) -> str:
    return tag_path.split(".")[0]


def id_prefix(entry_id: str) -> str:
    """Split leading alpha chars from id (e.g., 'CHEM5' -> 'CHEM')."""
    m = re.match(r"^([A-Za-z]+)", entry_id)
    return m.group(1) if m else ""


def sort_tags_by_hierarchy(tags: list[str]) -> list[str]:
    """Sort a list of tag paths by the top-level hierarchy rank."""
    return sorted(
        tags,
        key=lambda t: (HIERARCHY_RANK.get(top_level_of(t), 99), t),
    )


def derive_tagging(entry_id: str, domain_string: str) -> dict:
    """Apply primacy rule + hierarchy sort. Returns dict with proposed tagging."""
    prefix = id_prefix(entry_id)
    prefix_tag = ID_PREFIX_TO_TAG.get(prefix)

    tags_from_string = DOMAIN_STRING_TO_TAGS.get(domain_string, None)
    if tags_from_string is None:
        return {
            "primary":   None,
            "secondary": [],
            "auxiliary": [],
            "confidence":"low",
            "flags":     ["unrecognized-domain-string", f"prefix={prefix}"],
            "rationale": f"Domain string '{domain_string}' not in mapping table",
            "tags_from_string": [],
            "prefix_tag": prefix_tag,
        }

    # Primary selection
    if prefix_tag is not None:
        primary = prefix_tag
        # If prefix_tag's top-level does not appear in the string, add low-confidence flag
        prefix_top = top_level_of(prefix_tag)
        string_tops = {top_level_of(t) for t in tags_from_string}
        primary_matches_string = prefix_top in string_tops
        confidence = "high" if primary_matches_string else "medium"
        flags = [] if primary_matches_string else [
            f"prefix-tag-top ({prefix_top}) not in domain string"
        ]
        rationale = f"Primary via ID prefix '{prefix}' -> {prefix_tag}."
        if not primary_matches_string:
            rationale += (
                f" Domain string top-level(s) {sorted(string_tops)} differ from "
                f"prefix-derived top-level '{prefix_top}'."
            )
    else:
        # No prefix tag: use most foundational tag in the string as primary
        sorted_by_rank = sort_tags_by_hierarchy(tags_from_string)
        primary = sorted_by_rank[0]
        confidence = "medium"
        flags = ["primary-via-hierarchy-fallback (ID prefix non-deterministic)"]
        rationale = (
            f"ID prefix '{prefix}' is non-deterministic. Primary = most "
            f"foundational tag in string per hierarchy: {primary}."
        )

    # Secondary/auxiliary from the string, excluding primary top-level, sorted
    secondary_pool = [
        t for t in tags_from_string if top_level_of(t) != top_level_of(primary)
    ]
    secondary_pool = sort_tags_by_hierarchy(secondary_pool)

    # Split secondary vs auxiliary: first 1-2 as secondary, rest as auxiliary
    secondary = secondary_pool[:2]
    auxiliary = secondary_pool[2:]

    return {
        "primary":   primary,
        "secondary": secondary,
        "auxiliary": auxiliary,
        "confidence":confidence,
        "flags":     flags,
        "rationale": rationale,
        "tags_from_string": tags_from_string,
        "prefix_tag": prefix_tag,
    }


# ====================================================================
# Smoke-test entry pick — 20 entries covering diverse prefixes + tricky cases
# ====================================================================
SMOKE_TEST_IDS = [
    # clean tier-1 reference_laws
    "INFO1",    # Shannon Entropy (information, clean)
    "MATH1",    # pure math
    "BIO1",     # biology
    "CHEM1",    # chemistry
    "CS1",      # Church-Turing
    "GV1",      # GR Einstein Field Equations
    "CM1",      # Newton's Laws
    "QM1",      # Schrödinger
    "TD6",      # Onsager
    "STAT1",    # MaxEnt principle
    # multi-domain reference_laws
    "MATH5",    # tests MATH prefix
    "NE01",     # neuroscience — confirms 2-digit NE IDs, 3-domain 'physics · chemistry · biology'
    "FL1",      # formal logic
    "ES1",      # earth sciences
    # axioms (non-deterministic prefix)
    "Ax1",      # Information Primacy
    # tricky prefix / less-standard
    "M1",       # "M"-prefix check
    # meta-entries
    "P2_STATUS", # status-tracker entry
    "Q1",       # open question
    # additional coverage
    "GT01",     # GT-prefix gravity (Jacobson's thermodynamic derivation)
    "IT02",     # Von Neumann entropy (IT-prefix)
]


def fetch_entries(conn: sqlite3.Connection, ids: list[str]) -> list[dict]:
    placeholders = ",".join("?" * len(ids))
    rows = conn.execute(
        f"SELECT id, title, entry_type, domain FROM entries WHERE id IN ({placeholders})",
        ids,
    ).fetchall()
    return [dict(id=r[0], title=r[1], entry_type=r[2], domain=r[3]) for r in rows]


def main() -> None:
    t_start = time.time()

    conn = sqlite3.connect(DS_WIKI_DB)
    try:
        entries = fetch_entries(conn, SMOKE_TEST_IDS)
    finally:
        conn.close()

    found_ids = {e["id"] for e in entries}
    missing = [i for i in SMOKE_TEST_IDS if i not in found_ids]

    # Process each entry
    results = []
    per_entry_times = []
    for e in entries:
        t0 = time.time()
        tagging = derive_tagging(e["id"], e["domain"])
        dt = time.time() - t0
        per_entry_times.append(dt)
        results.append({**e, **tagging, "ms": int(dt * 1000)})

    # Aggregate stats
    confs = {"high": 0, "medium": 0, "low": 0}
    for r in results:
        confs[r["confidence"]] += 1
    total_time = time.time() - t_start

    # Render report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w") as f:
        f.write("# Domain Retagging — Smoke Test Report\n\n")
        f.write(f"**Date:** {date.today().isoformat()}\n")
        f.write(f"**Scope:** {len(results)} entries (target 20; missing {missing})\n")
        f.write(f"**Total wall time (script only):** {total_time:.2f}s\n\n")
        f.write("## Summary\n\n")
        f.write(f"- high confidence: {confs['high']}\n")
        f.write(f"- medium confidence: {confs['medium']}\n")
        f.write(f"- low confidence: {confs['low']}\n")
        f.write(f"- missing entries: {len(missing)}\n\n")

        if missing:
            f.write(f"**Missing from ds_wiki.db:** {', '.join(missing)}\n\n")

        f.write("## Hierarchy (foundation-first)\n\n")
        for tag, rank in sorted(HIERARCHY_RANK.items(), key=lambda x: x[1]):
            f.write(f"{rank}. `{tag}`\n")

        f.write("\n## Per-entry proposals\n\n")
        f.write("| ID | Type | Current `domain` | Primary | Secondary | Auxiliary | Conf | Flags |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for r in results:
            flags = ", ".join(r["flags"]) if r["flags"] else "—"
            sec = ", ".join(r["secondary"]) if r["secondary"] else "—"
            aux = ", ".join(r["auxiliary"]) if r["auxiliary"] else "—"
            f.write(
                f"| `{r['id']}` | {r['entry_type']} | {r['domain']} | "
                f"`{r['primary']}` | {sec} | {aux} | {r['confidence']} | {flags} |\n"
            )

        f.write("\n## Per-entry rationale\n\n")
        for r in results:
            f.write(f"### `{r['id']}` — {r['title']}\n")
            f.write(f"- Current `domain`: `{r['domain']}`\n")
            f.write(f"- ID prefix: `{id_prefix(r['id'])}` -> "
                    f"`{r['prefix_tag']}`\n")
            f.write(f"- Tags from string: {r['tags_from_string']}\n")
            f.write(f"- Proposed primary: `{r['primary']}`\n")
            if r['secondary']:
                f.write(f"- Proposed secondary: {r['secondary']}\n")
            if r['auxiliary']:
                f.write(f"- Proposed auxiliary: {r['auxiliary']}\n")
            f.write(f"- Confidence: {r['confidence']}\n")
            f.write(f"- Rationale: {r['rationale']}\n")
            if r['flags']:
                f.write(f"- Flags: {r['flags']}\n")
            f.write("\n")

        # Timing projection
        avg_ms = (sum(per_entry_times) / len(per_entry_times) * 1000) if per_entry_times else 0
        projected_278 = avg_ms * 278 / 1000
        f.write("## Timing projection for full 278-entry pass\n\n")
        f.write(f"- Average script time per entry: {avg_ms:.1f} ms\n")
        f.write(f"- Projected script time for 278 entries: {projected_278:.2f} seconds\n")
        f.write(f"- **Script time is negligible.** Bottleneck is owner review of "
                f"medium/low-confidence cases.\n")
        f.write(f"- Smoke test produced {confs['medium']+confs['low']} medium+low "
                f"confidence cases out of {len(results)} ({(confs['medium']+confs['low'])/max(len(results),1)*100:.0f}%).\n")
        f.write(f"- Extrapolated review burden for 278 entries: "
                f"~{int((confs['medium']+confs['low'])/max(len(results),1) * 278)} cases "
                f"needing manual review.\n")

    print(f"Smoke test complete. Report: {REPORT_PATH}")
    print(f"  {len(results)} entries processed in {total_time:.2f}s")
    print(f"  confidence — high: {confs['high']}, medium: {confs['medium']}, low: {confs['low']}")
    if missing:
        print(f"  missing: {missing}")


if __name__ == "__main__":
    main()

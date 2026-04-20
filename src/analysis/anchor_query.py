"""
anchor_query.py — Query the GSW anchor graph by topic.

The pipeline:
  1. Semantic search: BGE-encode the topic query, retrieve top-k chunks via ChromaDB
  2. Map chunks -> entries
  3. JOIN entries to external_anchors in wiki_history.db
  4. Surface co-citation hubs (sources anchoring multiple entries)
  5. Detect cross-domain bridges (sources anchoring entries from different primary domains)

Returns canonical sources connected to the topic via the wiki's anchor graph,
not just the wiki text itself.
"""
from __future__ import annotations

import sqlite3
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import chromadb
from sentence_transformers import SentenceTransformer

# Make src/ importable
_SRC = Path(__file__).resolve().parent.parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from config import CHROMA_COLLECTION, CHROMA_DIR, EMBED_MODEL, HISTORY_DB, SOURCE_DB

# ── Singletons ────────────────────────────────────────────────────────────────

_model: SentenceTransformer | None = None
_collection: chromadb.Collection | None = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def _get_collection() -> chromadb.Collection:
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        _collection = client.get_collection(CHROMA_COLLECTION)
    return _collection


def _open_history() -> sqlite3.Connection:
    conn = sqlite3.connect(HISTORY_DB)
    conn.row_factory = sqlite3.Row
    conn.execute(f"ATTACH DATABASE '{SOURCE_DB}' AS ds")
    return conn


# ── Core query ────────────────────────────────────────────────────────────────

def find_anchors_for_topic(
    query: str,
    top_k_entries: int = 10,
    chunks_per_query: int = 30,
) -> dict[str, Any]:
    """Find canonical sources connected to a topic via the wiki's anchor graph.

    Args:
        query: natural-language topic ("phase transitions", "what does the wiki
               say about entropy in living systems", etc.)
        top_k_entries: max distinct entries to surface from semantic search.
        chunks_per_query: chunks to retrieve before deduplicating to entries.

    Returns dict with:
        seed_entries:   wiki entries semantically related to the query
        canonical_sources: external sources anchored to those entries, ranked by
                           co-citation count
        co_citation_hubs:  sources anchoring 2+ entries (the connective tissue)
        cross_domain_bridges: sources anchoring entries from different primary
                              domains (most semantically valuable)
        internal_constructions: entries flagged IC (no GSW equivalent)
        unanchored: entries with no anchors and no IC flag (gaps)
    """
    # 1. Semantic search via ChromaDB
    qvec = _get_model().encode([query], normalize_embeddings=True)[0].tolist()
    res = _get_collection().query(
        query_embeddings=[qvec],
        n_results=min(chunks_per_query, 50),
        include=["metadatas", "distances", "documents"],
    )

    # 2. Map chunks -> entries (dedupe; keep best score per entry)
    entry_scores: dict[str, float] = {}
    entry_snippets: dict[str, str] = {}
    for cid, meta, dist, doc in zip(
        res["ids"][0], res["metadatas"][0],
        res["distances"][0], res["documents"][0],
    ):
        eid = meta.get("entry_id", "")
        if not eid:
            continue
        score = 1.0 - float(dist)
        if eid not in entry_scores or score > entry_scores[eid]:
            entry_scores[eid] = score
            entry_snippets[eid] = doc[:200].strip()

    # Top-k entries by best chunk score
    sorted_entries = sorted(entry_scores.items(), key=lambda x: -x[1])[:top_k_entries]
    entry_ids = [eid for eid, _ in sorted_entries]
    if not entry_ids:
        return {"seed_entries": [], "canonical_sources": [], "co_citation_hubs": [],
                "cross_domain_bridges": [], "internal_constructions": [], "unanchored": []}

    # 3. Open history DB and pull entry metadata + anchors
    conn = _open_history()
    placeholders = ",".join("?" for _ in entry_ids)

    # Entry metadata (title, type, primary domain)
    entry_meta: dict[str, dict] = {}
    for r in conn.execute(f"""
        SELECT e.id, e.title, e.entry_type
        FROM ds.entries e
        WHERE e.id IN ({placeholders})
    """, entry_ids):
        entry_meta[r["id"]] = {
            "title": r["title"], "entry_type": r["entry_type"], "primary_domain": None,
        }
    # Conjectures may also appear (chunks for conj_*)
    for r in conn.execute(f"""
        SELECT c.id, c.title, c.claim
        FROM ds.conjectures c
        WHERE c.id IN ({placeholders})
    """, entry_ids):
        entry_meta[r["id"]] = {
            "title": r["title"] or (r["claim"] or "")[:80],
            "entry_type": "conjecture",
            "primary_domain": None,
        }

    # Primary domain per entry
    for r in conn.execute(f"""
        SELECT e.entry_id,
               CASE WHEN INSTR(t.tag_path,'.')=0 THEN t.tag_path
                    ELSE SUBSTR(t.tag_path,1,INSTR(t.tag_path,'.')-1) END AS top
        FROM entry_source_domains e
        JOIN source_domain_taxonomy t ON t.id = e.tag_id
        WHERE e.entry_id IN ({placeholders})
          AND e.primacy='primary' AND e.review_status='current'
    """, entry_ids):
        if r["entry_id"] in entry_meta:
            entry_meta[r["entry_id"]]["primary_domain"] = r["top"]

    # Pull all anchors for these entries
    anchors_by_entry: dict[str, list[dict]] = defaultdict(list)
    sources_to_entries: dict[tuple[str, str], list[str]] = defaultdict(list)
    for r in conn.execute(f"""
        SELECT entry_id, source, identifier, title, canonical_role,
               relationship, tier, confidence, notes
        FROM external_anchors
        WHERE entry_id IN ({placeholders})
        ORDER BY entry_id, canonical_role, tier
    """, entry_ids):
        anchor = dict(r)
        anchors_by_entry[r["entry_id"]].append(anchor)
        sources_to_entries[(r["source"], r["identifier"])].append(r["entry_id"])

    # Internal constructions
    ic_set = set()
    for r in conn.execute(f"""
        SELECT entry_id, reason FROM internal_constructions
        WHERE entry_id IN ({placeholders})
    """, entry_ids):
        ic_set.add(r["entry_id"])

    conn.close()

    # 4. Build seed_entries output
    seed_entries = []
    for eid, score in sorted_entries:
        meta = entry_meta.get(eid, {})
        seed_entries.append({
            "entry_id": eid,
            "title": meta.get("title", "(unknown)"),
            "entry_type": meta.get("entry_type", "unknown"),
            "primary_domain": meta.get("primary_domain"),
            "score": round(score, 3),
            "snippet": entry_snippets.get(eid, ""),
            "n_anchors": len(anchors_by_entry.get(eid, [])),
            "internal_construction": eid in ic_set,
            "anchors": anchors_by_entry.get(eid, []),
        })

    # 5. Build canonical_sources ranked by co-citation count
    sources_ranked = []
    for (src, ident), eids in sources_to_entries.items():
        # Get title from first anchor row
        first = next((a for a in anchors_by_entry[eids[0]]
                      if a["source"] == src and a["identifier"] == ident), None)
        if first is None:
            continue
        domains = {entry_meta[e].get("primary_domain") for e in eids if e in entry_meta}
        domains.discard(None)
        sources_ranked.append({
            "source": src,
            "identifier": ident,
            "title": first.get("title", ""),
            "canonical_role": first.get("canonical_role"),
            "tier": first.get("tier"),
            "confidence": first.get("confidence"),
            "n_entries_in_topic": len(eids),
            "entries_in_topic": eids,
            "domains_spanned": sorted(domains),
        })
    sources_ranked.sort(key=lambda x: (-x["n_entries_in_topic"], x["source"]))

    # 6. Co-citation hubs: sources anchoring 2+ topic entries
    co_citation_hubs = [s for s in sources_ranked if s["n_entries_in_topic"] >= 2]

    # 7. Cross-domain bridges: sources spanning 2+ primary domains
    cross_domain_bridges = [s for s in sources_ranked if len(s["domains_spanned"]) >= 2]

    # 8. Unanchored topic entries
    unanchored = [
        eid for eid, _ in sorted_entries
        if not anchors_by_entry.get(eid) and eid not in ic_set
    ]

    return {
        "seed_entries":          seed_entries,
        "canonical_sources":     sources_ranked,
        "co_citation_hubs":      co_citation_hubs,
        "cross_domain_bridges":  cross_domain_bridges,
        "internal_constructions": [e for e in entry_ids if e in ic_set],
        "unanchored":            unanchored,
    }


def expand_via_co_citation(
    source: str,
    identifier: str,
    exclude_entries: list[str] | None = None,
) -> list[dict]:
    """Given a canonical source, find ALL wiki entries that anchor to it.

    Useful for cross-referencing: 'who else cites this source?' surfaces the
    full cluster around a canonical reference.
    """
    exclude = set(exclude_entries or [])
    conn = _open_history()
    rows = conn.execute("""
        SELECT a.entry_id, e.title, e.entry_type, a.canonical_role, a.relationship
        FROM external_anchors a
        JOIN ds.entries e ON e.id = a.entry_id
        WHERE a.source = ? AND a.identifier = ?
        ORDER BY a.entry_id
    """, (source, identifier)).fetchall()
    conn.close()
    return [
        {"entry_id": r["entry_id"], "title": r["title"],
         "entry_type": r["entry_type"], "canonical_role": r["canonical_role"],
         "relationship": r["relationship"]}
        for r in rows if r["entry_id"] not in exclude
    ]

"""
Apply Domain Retag — Clean Backlog (Chunks 1-5) — 2026-04-17

Applies the owner-approved retagging for 217 entries across the 5 "clean"
chunks (physics, bio_chem, math_formal, info_stat_cs, earth_conj_misc).

Logic:
- For each entry, use the script's derived proposal (from domain_retag_chunk.py
  logic) UNLESS an owner amendment exists in AMENDMENTS dict below.
- Amendments come from docs/prior_art_reviews/DOMAIN_RETAG_AMENDMENTS.md
- All rows inserted with:
  - review_status='current'
  - confidence='high' (after ratification/amendment, all are owner-approved)
  - assigned_date=today, assigned_by_session=this migration's id
  - last_reviewed_date=today, last_reviewed_by_session=same
- Multi-row per entry: primary + secondaries + auxiliaries (one row each,
  distinguished by `primacy` column).

Conjectures (Chunk 7) + misc_entries (Chunk 6) NOT handled here — those are
the judgment-heavy cases that come next.

Run: python3 scripts/migrations/apply_domain_retag_clean_2026_04_17.py
"""

from __future__ import annotations
import sqlite3
import sys
from datetime import date
from pathlib import Path

# Ensure scripts/ is importable so we can reuse domain_retag_chunk logic
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from domain_retag_chunk import (  # type: ignore
    CHUNK_PREFIXES, derive_proposal, fetch_entries_with_claims,
)

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-retag-clean-2026-04-17"

CLEAN_CHUNKS = ["physics", "bio_chem", "math_formal", "info_stat_cs", "earth_conj_misc"]


# ====================================================================
# Owner-approved amendments from DOMAIN_RETAG_AMENDMENTS.md
# Format: entry_id -> {primary, secondary, auxiliary}
# Any entry NOT in this dict uses the script's derived proposal as-is.
# ====================================================================
AMENDMENTS: dict[str, dict] = {
    # ---- bio_chem ----
    "CR1":   {"primary": "physics.classical",
              "secondary": ["chemistry"],
              "auxiliary": []},
    "DM3":   {"primary": "chemistry.physical",
              "secondary": [],
              "auxiliary": []},
    "DM4":   {"primary": "chemistry.physical",
              "secondary": ["physics.classical"],
              "auxiliary": []},
    "BIO6":  {"primary": "biology",
              "secondary": [],
              "auxiliary": ["chemistry.biochemistry"]},
    "MS1":   {"primary": "physics.classical",
              "secondary": [],
              "auxiliary": ["chemistry.materials"]},

    # ---- math_formal ----
    "MATH1": {"primary": "mathematics.probability_measure",
              "secondary": ["statistics_probability"],
              "auxiliary": ["information_theory"]},
    "MATH3": {"primary": "mathematics.probability_measure",
              "secondary": [],
              "auxiliary": []},
    "MATH4": {"primary": "formal_logic.proof_theory",
              "secondary": ["mathematics"],
              "auxiliary": []},

    # ---- info_stat_cs ----
    "IT05":  {"primary": "information_theory.shannon",
              "secondary": ["mathematics.probability_measure"],
              "auxiliary": []},
    "IT06":  {"primary": "physics.modern.statistical_mechanics",
              "secondary": ["information_theory"],
              "auxiliary": []},
    "IT08":  {"primary": "information_theory",
              "secondary": ["mathematics.geometry_topology"],
              "auxiliary": []},
    "STAT1": {"primary": "statistics_probability.inference",
              "secondary": ["information_theory", "mathematics"],
              "auxiliary": ["physics.modern.statistical_mechanics"]},
    "STAT3": {"primary": "physics.modern.statistical_mechanics",
              "secondary": ["information_theory"],
              "auxiliary": []},
    "CS6":   {"primary": "information_theory.shannon",
              "secondary": ["computer_science", "physics.classical"],
              "auxiliary": []},
    "STAT2": {"primary": "mathematics.probability_measure",
              "secondary": ["physics.modern.statistical_mechanics"],
              "auxiliary": []},

    # ---- earth_conj_misc ----
    "ES7":   {"primary": "earth_sciences.planetary",
              "secondary": ["physics.cosmology"],
              "auxiliary": []},
}


def resolve_tag_id(conn: sqlite3.Connection, tag_path: str) -> int:
    row = conn.execute(
        "SELECT id FROM source_domain_taxonomy WHERE tag_path = ?",
        (tag_path,),
    ).fetchone()
    if row is None:
        raise KeyError(f"tag_path not found in taxonomy: {tag_path}")
    return row[0]


def final_tagging_for_entry(entry: dict) -> dict:
    """Return the final {primary, secondary, auxiliary} lists for an entry.

    If the entry has an amendment, use it; otherwise derive via the script.
    """
    if entry["id"] in AMENDMENTS:
        amendment = AMENDMENTS[entry["id"]]
        return {
            "primary":   amendment["primary"],
            "secondary": amendment["secondary"],
            "auxiliary": amendment["auxiliary"],
        }

    prop = derive_proposal(
        entry["id"], entry["title"], entry["entry_type"],
        entry["domain"], entry["claim"],
    )
    if prop.primary is None:
        # low/no-signal cases — shouldn't appear in clean chunks after amendments
        return {"primary": None, "secondary": [], "auxiliary": []}
    return {
        "primary":   prop.primary,
        "secondary": prop.secondary,
        "auxiliary": prop.auxiliary,
    }


def insert_entry_tags(
    hconn: sqlite3.Connection, entry_id: str, tagging: dict,
) -> int:
    """Insert rows into entry_source_domains for this entry.

    Returns number of rows inserted. Skips duplicates via the UNIQUE index.
    """
    n = 0
    if tagging["primary"] is not None:
        tag_id = resolve_tag_id(hconn, tagging["primary"])
        res = hconn.execute(
            "INSERT OR IGNORE INTO entry_source_domains "
            "(entry_id, tag_id, primacy, assigned_date, assigned_by_session, "
            " last_reviewed_date, last_reviewed_by_session, confidence, "
            " review_status, rationale) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (entry_id, tag_id, "primary", TODAY, SESSION, TODAY, SESSION,
             "high", "current",
             "Clean-backlog retag pass; owner-approved via DOMAIN_RETAG_AMENDMENTS.md"),
        )
        n += res.rowcount

    for tag_path in tagging.get("secondary", []):
        tag_id = resolve_tag_id(hconn, tag_path)
        res = hconn.execute(
            "INSERT OR IGNORE INTO entry_source_domains "
            "(entry_id, tag_id, primacy, assigned_date, assigned_by_session, "
            " last_reviewed_date, last_reviewed_by_session, confidence, "
            " review_status, rationale) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (entry_id, tag_id, "secondary", TODAY, SESSION, TODAY, SESSION,
             "high", "current",
             "Clean-backlog retag pass; hierarchy-ordered secondary"),
        )
        n += res.rowcount

    for tag_path in tagging.get("auxiliary", []):
        tag_id = resolve_tag_id(hconn, tag_path)
        res = hconn.execute(
            "INSERT OR IGNORE INTO entry_source_domains "
            "(entry_id, tag_id, primacy, assigned_date, assigned_by_session, "
            " last_reviewed_date, last_reviewed_by_session, confidence, "
            " review_status, rationale) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (entry_id, tag_id, "auxiliary", TODAY, SESSION, TODAY, SESSION,
             "high", "current",
             "Clean-backlog retag pass; auxiliary"),
        )
        n += res.rowcount

    return n


def main() -> None:
    # Gather all entries across the 5 clean chunks
    dconn = sqlite3.connect(DS_WIKI_DB)
    try:
        all_entries = []
        for chunk in CLEAN_CHUNKS:
            prefixes = CHUNK_PREFIXES[chunk]
            chunk_entries = fetch_entries_with_claims(dconn, prefixes)
            for e in chunk_entries:
                e["_chunk"] = chunk
            all_entries.extend(chunk_entries)
    finally:
        dconn.close()

    print(f"Loaded {len(all_entries)} entries across {len(CLEAN_CHUNKS)} clean chunks.")

    # Apply tagging to wiki_history.db
    hconn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        rows_inserted = 0
        entries_with_tags = 0
        entries_skipped = []
        amendments_applied = 0
        per_chunk_counts = {c: 0 for c in CLEAN_CHUNKS}

        for e in all_entries:
            tagging = final_tagging_for_entry(e)
            if tagging["primary"] is None:
                entries_skipped.append(e["id"])
                continue
            n = insert_entry_tags(hconn, e["id"], tagging)
            rows_inserted += n
            entries_with_tags += 1
            per_chunk_counts[e["_chunk"]] += 1
            if e["id"] in AMENDMENTS:
                amendments_applied += 1

        hconn.commit()

        print(f"\nApplied:")
        print(f"  {entries_with_tags} entries tagged")
        print(f"  {rows_inserted} rows inserted into entry_source_domains")
        print(f"  {amendments_applied}/{len(AMENDMENTS)} amendments applied")
        if entries_skipped:
            print(f"  {len(entries_skipped)} entries skipped (no proposal): {entries_skipped}")

        print(f"\nPer chunk:")
        for chunk, n in per_chunk_counts.items():
            print(f"  {chunk:18}: {n} entries tagged")

        # Verification: distinct entry count + primacy distribution
        cur = hconn.cursor()
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM entry_source_domains "
                    "WHERE review_status='current'")
        print(f"\nTotal distinct entries with current tags: {cur.fetchone()[0]}")

        cur.execute(
            "SELECT primacy, COUNT(*) FROM entry_source_domains "
            "WHERE review_status='current' GROUP BY primacy"
        )
        print("Primacy distribution:")
        for row in cur.fetchall():
            print(f"  {row[0]:10} {row[1]}")

        # Top-level domain distribution
        cur.execute("""
            SELECT
                CASE
                    WHEN INSTR(t.tag_path, '.') = 0 THEN t.tag_path
                    ELSE SUBSTR(t.tag_path, 1, INSTR(t.tag_path, '.')-1)
                END AS top_level,
                COUNT(DISTINCT e.entry_id)
            FROM entry_source_domains e
            JOIN source_domain_taxonomy t ON t.id = e.tag_id
            WHERE e.review_status='current' AND e.primacy='primary'
            GROUP BY top_level
            ORDER BY COUNT(DISTINCT e.entry_id) DESC
        """)
        print("\nPrimary-tag top-level distribution:")
        for row in cur.fetchall():
            print(f"  {row[0]:25} {row[1]} entries")

    finally:
        hconn.close()


if __name__ == "__main__":
    main()

"""
Apply Domain Retag — Chunk 6 (misc_entries) — 2026-04-18

Applies owner-approved tagging for 60 misc entries from
DOMAIN_RETAG_MISC_PROPOSALS.md.

Special case: X8 "Financial Market Entropy Production" is the owner's side
AlphaEntropy finance project — NOT canonical science-wiki content. It is
excluded from domain tagging and added to `internal_constructions` with a
clear rationale flagging it for relocation or explicit non-wiki labelling.

Run: python3 scripts/migrations/apply_domain_retag_misc_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-retag-misc-2026-04-18"

# X8 is owner's side finance project; excluded from tag graph
X8_ID = "X8"
X8_REASON = (
    "Side finance/algorithmic-trading project (AlphaEntropy). Not canonical "
    "science-wiki content. Flagged by owner 2026-04-18 during misc-chunk "
    "retagging. Options: (a) relocate to a separate repo/wiki, (b) clearly "
    "label as side-project in-place and exclude from cross-domain bridging. "
    "Pending owner decision."
)
X8_SEARCHED = '["flagged-by-owner-as-side-project"]'


# ====================================================================
# Tagging proposals from DOMAIN_RETAG_MISC_PROPOSALS.md (owner-approved)
# ====================================================================
PROPOSALS: dict[str, dict] = {
    # A-series
    "A1":  {"primary": "mathematics.geometry_topology",
            "secondary": ["physics.classical"],
            "auxiliary": ["biology.physiology"]},
    "A2":  {"primary": "mathematics.geometry_topology",
            "secondary": ["networks_systems"],
            "auxiliary": []},

    # Ax + OmD
    "Ax1": {"primary": "information_theory",
            "secondary": ["physics.modern"],
            "auxiliary": []},
    "Ax2": {"primary": "information_theory",
            "secondary": ["physics"],
            "auxiliary": ["mathematics.probability_measure"]},
    "OmD": {"primary": "physics.cosmology",
            "secondary": ["information_theory"],
            "auxiliary": []},

    # B-series
    "B1":  {"primary": "physics.modern",
            "secondary": ["chemistry"],
            "auxiliary": []},
    "B2":  {"primary": "chemistry.physical",
            "secondary": ["physics.classical"],
            "auxiliary": []},
    "B3":  {"primary": "physics.classical",
            "secondary": [],
            "auxiliary": []},
    "B4":  {"primary": "physics.classical",
            "secondary": [],
            "auxiliary": []},
    "B5":  {"primary": "information_theory",
            "secondary": ["physics.classical"],
            "auxiliary": []},

    # C-series
    "C1":  {"primary": "biology.physiology",
            "secondary": ["networks_systems"],
            "auxiliary": []},
    "C2":  {"primary": "networks_systems",
            "secondary": ["computer_science"],
            "auxiliary": ["biology.physiology"]},
    "C3":  {"primary": "statistics_probability.stochastic_processes",
            "secondary": ["networks_systems"],
            "auxiliary": ["mathematics.probability_measure"]},

    # D-series
    "D1":  {"primary": "biology.neuroscience",
            "secondary": ["statistics_probability"],
            "auxiliary": []},
    "D2":  {"primary": "networks_systems.dynamical_systems",
            "secondary": ["mathematics"],
            "auxiliary": ["physics.modern"]},

    # E-series
    "E1":  {"primary": "networks_systems",
            "secondary": ["computer_science"],
            "auxiliary": []},
    "E2":  {"primary": "networks_systems",
            "secondary": ["computer_science"],
            "auxiliary": []},

    # F-series
    "F1":  {"primary": "information_theory",
            "secondary": ["networks_systems"],
            "auxiliary": []},
    "F2":  {"primary": "biology.ecology",
            "secondary": [],
            "auxiliary": []},
    "F3":  {"primary": "biology.ecology",
            "secondary": [],
            "auxiliary": []},
    "F4":  {"primary": "biology",
            "secondary": ["physics.modern"],
            "auxiliary": ["networks_systems"]},
    "F5":  {"primary": "biology.physiology",
            "secondary": ["earth_sciences"],
            "auxiliary": []},

    # G-series
    "G1":  {"primary": "physics.cosmology",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "G3":  {"primary": "physics.cosmology",
            "secondary": ["computer_science.complexity"],
            "auxiliary": ["information_theory"]},

    # H-series
    "H1":  {"primary": "information_theory",
            "secondary": ["networks_systems"],
            "auxiliary": ["physics.modern", "biology"]},
    "H2":  {"primary": "mathematics.geometry_topology",
            "secondary": ["networks_systems"],
            "auxiliary": ["biology.physiology"]},
    "H3":  {"primary": "information_theory",
            "secondary": ["biology.physiology"],
            "auxiliary": ["physics.modern"]},
    "H4":  {"primary": "mathematics.geometry_topology",
            "secondary": ["physics"],
            "auxiliary": []},
    "H5":  {"primary": "networks_systems",
            "secondary": ["biology.physiology", "information_theory"],
            "auxiliary": ["physics.modern"]},

    # M-series
    "M1":  {"primary": "mathematics",
            "secondary": ["statistics_probability.inference"],
            "auxiliary": ["computer_science"]},
    "M2":  {"primary": "statistics_probability.inference",
            "secondary": ["computer_science"],
            "auxiliary": []},
    "M3":  {"primary": "physics.classical",
            "secondary": ["networks_systems"],
            "auxiliary": []},
    "M4":  {"primary": "physics.modern.statistical_mechanics",
            "secondary": ["mathematics"],
            "auxiliary": []},
    "M5":  {"primary": "statistics_probability.inference",
            "secondary": ["mathematics"],
            "auxiliary": ["computer_science"]},
    "M6":  {"primary": "information_theory",
            "secondary": ["mathematics.probability_measure"],
            "auxiliary": ["statistics_probability"]},

    # P_STATUS
    "P2_STATUS":  {"primary": "biology.physiology",
                   "secondary": ["networks_systems", "information_theory"],
                   "auxiliary": []},
    "P12_STATUS": {"primary": "networks_systems",
                   "secondary": ["biology.physiology", "information_theory"],
                   "auxiliary": []},

    # Q-series
    "Q1":  {"primary": "mathematics.geometry_topology",
            "secondary": ["networks_systems"],
            "auxiliary": ["statistics_probability"]},
    "Q2":  {"primary": "mathematics.geometry_topology",
            "secondary": ["physics.modern"],
            "auxiliary": []},
    "Q3":  {"primary": "biology.physiology",
            "secondary": ["mathematics", "information_theory"],
            "auxiliary": []},
    "Q4":  {"primary": "computer_science.ml",
            "secondary": ["biology.physiology"],
            "auxiliary": ["information_theory"]},
    "Q5":  {"primary": "information_theory",
            "secondary": ["physics.modern"],
            "auxiliary": ["networks_systems"]},

    # T-series
    "T1":  {"primary": "information_theory",
            "secondary": ["mathematics"],
            "auxiliary": []},
    "T2":  {"primary": "biology.physiology",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "T3":  {"primary": "physics",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "T4":  {"primary": "physics.cosmology",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "T5":  {"primary": "physics.modern.statistical_mechanics",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "T6":  {"primary": "physics.cosmology",
            "secondary": ["computer_science.complexity"],
            "auxiliary": []},
    "T7":  {"primary": "physics.modern",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "T8":  {"primary": "networks_systems",
            "secondary": ["biology.physiology", "physics.modern"],
            "auxiliary": ["information_theory"]},
    "T9":  {"primary": "biology.physiology",
            "secondary": ["mathematics"],
            "auxiliary": []},
    "T10": {"primary": "computer_science.ml",
            "secondary": ["biology.physiology"],
            "auxiliary": []},

    # X-series
    "X0_FIM_Regimes": {"primary": "information_theory",
                       "secondary": ["physics.modern.statistical_mechanics",
                                     "networks_systems"],
                       "auxiliary": []},
    "X1": {"primary": "biology.physiology",
           "secondary": ["networks_systems"],
           "auxiliary": ["information_theory"]},
    "X2": {"primary": "information_theory",
           "secondary": ["mathematics.geometry_topology"],
           "auxiliary": []},
    "X3": {"primary": "physics.modern.statistical_mechanics",
           "secondary": ["information_theory"],
           "auxiliary": []},
    "X4": {"primary": "physics.modern",
           "secondary": ["information_theory"],
           "auxiliary": []},
    "X5": {"primary": "biology.ecology",
           "secondary": ["networks_systems"],
           "auxiliary": []},
    "X6": {"primary": "biology.neuroscience",
           "secondary": ["networks_systems", "computer_science.ml"],
           "auxiliary": []},
    "X7": {"primary": "biology",
           "secondary": ["networks_systems"],
           "auxiliary": []},

    # X8 is handled separately (side project, excluded from tag graph)
}


def resolve_tag_id(conn: sqlite3.Connection, tag_path: str) -> int:
    row = conn.execute(
        "SELECT id FROM source_domain_taxonomy WHERE tag_path = ?",
        (tag_path,),
    ).fetchone()
    if row is None:
        raise KeyError(f"tag_path not found in taxonomy: {tag_path}")
    return row[0]


def insert_entry_tags(
    conn: sqlite3.Connection, entry_id: str, tagging: dict, rationale: str,
) -> int:
    n = 0
    if tagging["primary"]:
        tag_id = resolve_tag_id(conn, tagging["primary"])
        res = conn.execute(
            "INSERT OR IGNORE INTO entry_source_domains "
            "(entry_id, tag_id, primacy, assigned_date, assigned_by_session, "
            " last_reviewed_date, last_reviewed_by_session, confidence, "
            " review_status, rationale) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (entry_id, tag_id, "primary", TODAY, SESSION, TODAY, SESSION,
             "high", "current", rationale),
        )
        n += res.rowcount
    for tag_path in tagging.get("secondary", []):
        tag_id = resolve_tag_id(conn, tag_path)
        res = conn.execute(
            "INSERT OR IGNORE INTO entry_source_domains "
            "(entry_id, tag_id, primacy, assigned_date, assigned_by_session, "
            " last_reviewed_date, last_reviewed_by_session, confidence, "
            " review_status, rationale) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (entry_id, tag_id, "secondary", TODAY, SESSION, TODAY, SESSION,
             "high", "current", rationale),
        )
        n += res.rowcount
    for tag_path in tagging.get("auxiliary", []):
        tag_id = resolve_tag_id(conn, tag_path)
        res = conn.execute(
            "INSERT OR IGNORE INTO entry_source_domains "
            "(entry_id, tag_id, primacy, assigned_date, assigned_by_session, "
            " last_reviewed_date, last_reviewed_by_session, confidence, "
            " review_status, rationale) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (entry_id, tag_id, "auxiliary", TODAY, SESSION, TODAY, SESSION,
             "high", "current", rationale),
        )
        n += res.rowcount
    return n


def insert_x8_internal_construction(conn: sqlite3.Connection) -> int:
    """Mark X8 as a non-wiki side project in internal_constructions."""
    res = conn.execute(
        "INSERT OR IGNORE INTO internal_constructions "
        "(entry_id, reason, searched_sources, flagged_date, "
        " flagged_by_session, scrutiny_level, notes) "
        "VALUES (?,?,?,?,?,?,?)",
        (X8_ID, X8_REASON, X8_SEARCHED, TODAY, SESSION,
         "owner-aware",
         "Owner flagged X8 during misc-chunk retagging 2026-04-18: "
         "side finance/AlphaEntropy project, not science-wiki content. "
         "Excluded from entry_source_domains; pending relocation decision."),
    )
    return res.rowcount


def main() -> None:
    rationale_base = (
        "Misc-chunk retag pass; owner-approved via "
        "DOMAIN_RETAG_MISC_PROPOSALS.md"
    )

    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        rows_inserted = 0
        entries_tagged = 0

        for entry_id, tagging in PROPOSALS.items():
            n = insert_entry_tags(conn, entry_id, tagging, rationale_base)
            if n > 0:
                entries_tagged += 1
            rows_inserted += n

        # X8 handled separately
        x8_rc = insert_x8_internal_construction(conn)

        conn.commit()

        print("Applied misc-chunk retagging:")
        print(f"  {entries_tagged}/60 entries tagged "
              f"(expected 60; X8 excluded as side project)")
        print(f"  {rows_inserted} rows inserted into entry_source_domains")
        print(f"  X8 flagged: {x8_rc} row inserted into internal_constructions")

        # Verification
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM entry_source_domains "
            "WHERE review_status='current'"
        )
        print(f"\nTotal entries tagged so far (chunks 1-6): {cur.fetchone()[0]}")

        cur.execute(
            "SELECT primacy, COUNT(*) FROM entry_source_domains "
            "WHERE review_status='current' GROUP BY primacy"
        )
        print("Primacy distribution (all chunks):")
        for row in cur.fetchall():
            print(f"  {row[0]:10} {row[1]}")

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
        print("\nPrimary-tag top-level distribution (all chunks):")
        for row in cur.fetchall():
            print(f"  {row[0]:25} {row[1]} entries")

        cur.execute("SELECT COUNT(*) FROM internal_constructions")
        print(f"\ninternal_constructions rows: {cur.fetchone()[0]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

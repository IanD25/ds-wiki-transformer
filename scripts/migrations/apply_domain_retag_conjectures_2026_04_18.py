"""
Apply Domain Retag — Chunk 7 (23 P-series conjectures) — 2026-04-18

Applies owner-approved tagging from DOMAIN_RETAG_CONJECTURES_PROPOSALS.md.

Special handling:
- P18, P19, P20: tag + flag `internal_constructions` as AlphaEntropy-derived
  (owner choice option-b 2026-04-18)
- P13, P15: tag + flag `internal_constructions` as owner-acknowledged ansatz
  (per epistemic contract + preserve-falsifications feedback rule)

Run: python3 scripts/migrations/apply_domain_retag_conjectures_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-retag-conjectures-2026-04-18"


# Conjecture tagging per DOMAIN_RETAG_CONJECTURES_PROPOSALS.md
PROPOSALS: dict[str, dict] = {
    "P1":  {"primary": "physics.cosmology",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P2":  {"primary": "biology.physiology",
            "secondary": ["networks_systems", "information_theory"],
            "auxiliary": []},
    "P3":  {"primary": "physics.cosmology",
            "secondary": ["information_theory"],
            "auxiliary": ["physics.modern"]},
    "P4":  {"primary": "chemistry.biochemistry",
            "secondary": ["biology.physiology"],
            "auxiliary": ["physics.classical"]},
    "P5":  {"primary": "information_theory",
            "secondary": ["mathematics.probability_measure",
                          "statistics_probability"],
            "auxiliary": []},
    "P6":  {"primary": "mathematics.geometry_topology",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P7":  {"primary": "information_theory",
            "secondary": ["mathematics.probability_measure"],
            "auxiliary": ["physics.modern.statistical_mechanics"]},
    "P8":  {"primary": "physics.modern.statistical_mechanics",
            "secondary": ["mathematics.geometry_topology"],
            "auxiliary": ["information_theory"]},
    "P9":  {"primary": "physics.cosmology",
            "secondary": ["computer_science.complexity"],
            "auxiliary": ["information_theory"]},
    "P10": {"primary": "physics.modern",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P11": {"primary": "networks_systems",
            "secondary": ["computer_science", "biology.physiology"],
            "auxiliary": []},
    "P12": {"primary": "networks_systems",
            "secondary": ["biology.physiology", "information_theory"],
            "auxiliary": []},
    "P13": {"primary": "information_theory",
            "secondary": ["biology.physiology",
                          "mathematics.geometry_topology"],
            "auxiliary": []},
    "P14": {"primary": "biology.physiology",
            "secondary": ["networks_systems", "statistics_probability"],
            "auxiliary": []},
    "P15": {"primary": "biology.physiology",
            "secondary": ["information_theory",
                          "mathematics.geometry_topology"],
            "auxiliary": []},
    "P16": {"primary": "computer_science.ml",
            "secondary": ["biology.physiology",
                          "mathematics.geometry_topology"],
            "auxiliary": []},
    "P17": {"primary": "physics.cosmology",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P18": {"primary": "statistics_probability",
            "secondary": ["information_theory", "networks_systems"],
            "auxiliary": []},
    "P19": {"primary": "statistics_probability.stochastic_processes",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P20": {"primary": "statistics_probability.inference",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P21": {"primary": "mathematics.probability_measure",
            "secondary": ["information_theory",
                          "mathematics.geometry_topology"],
            "auxiliary": []},
    "P22": {"primary": "physics.modern.statistical_mechanics",
            "secondary": ["information_theory"],
            "auxiliary": []},
    "P23": {"primary": "physics.cosmology",
            "secondary": ["information_theory",
                          "physics.modern.statistical_mechanics"],
            "auxiliary": []},
}


# Internal-construction flags
INTERNAL_CONSTRUCTIONS: dict[str, dict] = {
    "P18": {
        "reason": "AlphaEntropy-derived single-domain observation: US equity "
                  "markets 2003-2025. Empirically Supported within this one "
                  "dataset (per M0 audit), but owner flagged 2026-04-18 as "
                  "part of the same side-project ecosystem as X8. Treat as "
                  "side-project-adjacent: tagged in the science wiki graph "
                  "with an honest 'not general scientific claim' label.",
        "scrutiny_level": "needs-review",
        "notes": "Option-b treatment per owner 2026-04-18. Kept in tag graph "
                 "for connectivity; flagged here so searches can filter.",
    },
    "P19": {
        "reason": "AlphaEntropy-derived: non-ergodicity of D_eff regime "
                  "signals tested only on US equities. Same side-project "
                  "context as X8/P18.",
        "scrutiny_level": "needs-review",
        "notes": "Option-b treatment per owner 2026-04-18.",
    },
    "P20": {
        "reason": "AlphaEntropy-derived: subadditive error propagation "
                  "formula fit to 19 A/B variants in AlphaEntropy testing. "
                  "Empirical fit, single-domain. Side-project ecosystem.",
        "scrutiny_level": "needs-review",
        "notes": "Option-b treatment per owner 2026-04-18.",
    },
    "P13": {
        "reason": "Owner-acknowledged ansatz: 'The (d_f-1)/(d_f+1) functional "
                  "form is an ansatz — not derived from first principles.' "
                  "No literature analog found. Falsified by absence-of-"
                  "derivation (not by contradicting data). Preserved as a "
                  "learning artifact per preserve-falsifications rule.",
        "scrutiny_level": "needs-review",
        "notes": "M0 audit labelled Speculative (Falsified bucket in the "
                 "subsequent conjecture audit). Kept in wiki as owner asked: "
                 "'keep the wrong and label as falsified, we need to learn "
                 "from our mistakes' (2026-04-17).",
    },
    "P15": {
        "reason": "Owner-acknowledged ansatz: 'The formula is an ansatz.' "
                  "No first-principles derivation; financial-market evidence "
                  "is owner-labelled analogy, not independent test. Same "
                  "class as P13.",
        "scrutiny_level": "needs-review",
        "notes": "See P13 notes. Preserved per feedback rule.",
    },
}

INTERNAL_CONSTRUCTION_SEARCHED = '["owner-assertion-no-derivation-found"]'


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


def insert_internal_construction(
    conn: sqlite3.Connection, entry_id: str, ic: dict,
) -> int:
    res = conn.execute(
        "INSERT OR IGNORE INTO internal_constructions "
        "(entry_id, reason, searched_sources, flagged_date, "
        " flagged_by_session, scrutiny_level, notes) "
        "VALUES (?,?,?,?,?,?,?)",
        (entry_id, ic["reason"], INTERNAL_CONSTRUCTION_SEARCHED, TODAY,
         SESSION, ic["scrutiny_level"], ic["notes"]),
    )
    return res.rowcount


def main() -> None:
    rationale_base = (
        "Conjecture-chunk retag pass; owner-approved via "
        "DOMAIN_RETAG_CONJECTURES_PROPOSALS.md (option-b for "
        "AlphaEntropy-adjacent P18/19/20)"
    )

    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        rows_inserted = 0
        entries_tagged = 0
        ic_inserted = 0

        for entry_id, tagging in PROPOSALS.items():
            n = insert_entry_tags(conn, entry_id, tagging, rationale_base)
            if n > 0:
                entries_tagged += 1
            rows_inserted += n

        for entry_id, ic in INTERNAL_CONSTRUCTIONS.items():
            ic_inserted += insert_internal_construction(conn, entry_id, ic)

        conn.commit()

        print("Applied conjecture-chunk retagging:")
        print(f"  {entries_tagged}/23 conjectures tagged")
        print(f"  {rows_inserted} rows inserted into entry_source_domains")
        print(f"  {ic_inserted} rows inserted into internal_constructions")

        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM entry_source_domains "
            "WHERE review_status='current'"
        )
        print(f"\nTotal items tagged (chunks 1-7): {cur.fetchone()[0]}")

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
        print("\nFinal primary-tag top-level distribution (all chunks):")
        for row in cur.fetchall():
            print(f"  {row[0]:25} {row[1]} entries")

        cur.execute(
            "SELECT entry_id, scrutiny_level FROM internal_constructions "
            "ORDER BY entry_id"
        )
        print("\ninternal_constructions contents:")
        for row in cur.fetchall():
            print(f"  {row[0]:15} [{row[1]}]")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

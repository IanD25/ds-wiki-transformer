"""
Insert Tier-1 anchor batch 5 — C2 / E1 / STAT1 — 2026-04-18

Sixth live anchor insertion. Closes domain coverage by adding anchors to
the two previously-untouched domains:
  C2    Urban Scaling (Bettencourt-West) (networks_systems)
  E1    Moore's Law                      (networks_systems)
  STAT1 Maximum Entropy Principle        (statistics_probability.inference)

After this batch, all 10 top-level domains have at least one anchored
Tier-1 reference_law. Also reuses Jaynes 2003 book (already anchored on
MATH1) and West "Scale" book (already anchored on C1) — first cross-entry
source reuse pattern, demonstrating the co-citation graph filling in.

Run: python3 scripts/migrations/insert_tier1_batch5_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-tier1-batch5-2026-04-18"


ANCHORS = [
    # ==========================================================
    # C2 — Urban Scaling (Bettencourt-West)
    # ==========================================================
    ("C2", "doi", "10.1073/pnas.0610172104", None,
     "Bettencourt, Lobo, Helbing, Kühnert, West 2007 - Growth, innovation, scaling, pace of life in cities",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Bettencourt et al. 2007, PNAS 104(17), pp. 7301-7306. Empirical "
     "discovery of urban scaling laws: superlinear (beta~1.2) for wealth "
     "and innovation; sublinear (beta~0.85) for infrastructure. "
     "Verified via CrossRef 2026-04-18. ~4,000+ citations."),

    ("C2", "isbn", "978-0691202969", None,
     "Bettencourt - Introduction to Urban Science (MIT Press 2021)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Bettencourt 2021 MIT Press. First systematic textbook on urban "
     "science / urban scaling. By one of the 2007 PNAS authors."),

    ("C2", "isbn", "978-0143110903", None,
     "West - Scale: The Universal Laws of Life, Growth, and Death",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "West 2018 (paperback). Same anchor as C1 (Kleiber's Law). West "
     "Scale synthesizes metabolic + urban + company scaling. Fills "
     "comprehensive_survey for C2. **First cross-entry source reuse** "
     "in the anchor graph — Scale book anchors both C1 and C2 via "
     "comprehensive_survey."),

    # ==========================================================
    # E1 — Moore's Law
    # ==========================================================
    ("E1", "doi", "10.1109/JPROC.1998.658762", None,
     "Moore 1965/1998 - Cramming more components onto integrated circuits",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Original: Moore 1965, Electronics Magazine 38(8), pp. 114-117 "
     "(19 April 1965). Pre-DOI era. Republished: Moore 1998 in Proc. "
     "IEEE 86(1), pp. 82-85, DOI 10.1109/JPROC.1998.658762. Anchored "
     "via the 1998 IEEE reprint DOI."),

    ("E1", "doi", "10.1109/TSM.2010.2096437", None,
     "Mack 2011 - Fifty Years of Moore's Law",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Mack 2011, IEEE Trans. Semiconductor Manufacturing 24(2), pp. "
     "202-207. Comprehensive survey of Moore's Law over its first 50 "
     "years: original formulation, revisions, scaling relationships, "
     "physical limits. Fills comprehensive_survey for E1."),

    ("E1", "wikipedia",
     "https://en.wikipedia.org/wiki/Moore%27s_law",
     "1348480582",
     "Moore's law",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Moore 1965 "
     "citation present."),

    # ==========================================================
    # STAT1 — Maximum Entropy Principle
    # ==========================================================
    ("STAT1", "doi", "10.1103/PhysRev.106.620", None,
     "Jaynes 1957 - Information Theory and Statistical Mechanics (I)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Jaynes 1957 Part I, Physical Review 106(4), pp. 620-630. "
     "Introduces the MaxEnt principle as a foundation for statistical "
     "mechanics: least-biased distribution subject to constraints. "
     "~9,000+ citations. Verified via CrossRef."),

    ("STAT1", "doi", "10.1103/PhysRev.108.171", None,
     "Jaynes 1957 - Information Theory and Statistical Mechanics (II)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Jaynes 1957 Part II, Physical Review 108(2), pp. 171-190. "
     "Continuation; applications to thermodynamics. Second progenitor "
     "paper, same author, same year — analogous to Shannon 1948 Pt I "
     "and Pt II."),

    ("STAT1", "isbn", "978-0521592710", None,
     "Jaynes - Probability Theory: The Logic of Science",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Jaynes 2003 (posthumous). Same anchor as MATH1 Bayes' Theorem. "
     "Cox-axiom-based foundation for probability-as-logic + MaxEnt. "
     "**Cross-entry source reuse** — this book serves as "
     "axiomatic_foundation for both MATH1 (Bayes) and STAT1 (MaxEnt)."),

    ("STAT1", "isbn", "978-1439840955", None,
     "Gelman et al. - Bayesian Data Analysis (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Gelman et al. 2013. Same anchor as MATH1. Standard textbook "
     "treating MaxEnt alongside Bayesian inference. Cross-entry reuse."),

    ("STAT1", "wikipedia",
     "https://en.wikipedia.org/wiki/Principle_of_maximum_entropy",
     "1339189568",
     "Principle of maximum entropy",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Both Jaynes "
     "1957 papers cited with DOIs."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("C2", "E1", "STAT1"):
            cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            )
            n = cur.fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
            print(f"{eid} has {n} domain-tag rows.")

        print()
        print(f"Inserting {len(ANCHORS)} anchor rows...")
        inserted = 0
        for a in ANCHORS:
            (entry_id, source, identifier, revision_id, title, tier,
             stability, relationship, canonical_role, confidence, notes) = a
            res = conn.execute(
                "INSERT OR IGNORE INTO external_anchors "
                "(entry_id, source, identifier, revision_id, title, tier, "
                " source_stability_class, relationship, canonical_role, "
                " verified_date, verified_by_session, confidence, notes) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (entry_id, source, identifier, revision_id, title, tier,
                 stability, relationship, canonical_role,
                 TODAY, SESSION, confidence, notes),
            )
            inserted += res.rowcount
        conn.commit()
        print(f"  Inserted: {inserted}")

        print("\nPer-entry slot coverage:")
        for eid in ("C2", "E1", "STAT1"):
            cur.execute("""
                SELECT canonical_role, COUNT(*)
                FROM external_anchors
                WHERE entry_id=? AND canonical_role IS NOT NULL
                GROUP BY canonical_role
            """, (eid,))
            rows = {r[0]: r[1] for r in cur.fetchall()}
            filled = [r for r in
                      ("progenitor", "axiomatic_foundation",
                       "standard_textbook", "living_reference",
                       "comprehensive_survey") if r in rows]
            print(f"  {eid}: {len(filled)}/5 — "
                  f"{', '.join(f'{r}({rows[r]})' for r in filled)}")

        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries_anchored = cur.fetchone()[0]
        print(f"\nGlobal totals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries_anchored} / 300")

        # Co-citation graph analysis (expanded)
        print("\n=== Co-cited sources (appear on >=2 entries) ===")
        for r in cur.execute("""
            SELECT source, identifier,
                   COUNT(DISTINCT entry_id) as n,
                   GROUP_CONCAT(DISTINCT entry_id) as entries,
                   MAX(title) as title
            FROM external_anchors
            GROUP BY source, identifier
            HAVING n > 1
            ORDER BY n DESC, source, identifier
        """):
            print(f"  {r[2]}× — {r[4][:55]}")
            print(f"      entries: {r[3]}")

        # Domain coverage
        cur.execute("""
            SELECT
                CASE WHEN INSTR(t.tag_path, '.') = 0 THEN t.tag_path
                     ELSE SUBSTR(t.tag_path, 1, INSTR(t.tag_path, '.')-1)
                END AS top_level,
                COUNT(DISTINCT e.entry_id)
            FROM external_anchors a
            JOIN entry_source_domains e ON e.entry_id = a.entry_id
            JOIN source_domain_taxonomy t ON t.id = e.tag_id
            WHERE e.primacy='primary' AND e.review_status='current'
            GROUP BY top_level
            ORDER BY COUNT(DISTINCT e.entry_id) DESC
        """)
        print("\n=== Anchored entries by primary domain ===")
        for row in cur.fetchall():
            print(f"  {row[0]:25} {row[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

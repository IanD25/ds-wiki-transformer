"""
Insert Tier-1 anchor batch 3 — MATH1 / FL1 / CHEM1 — 2026-04-18

Fourth live anchor insertion. Adds three more domains never anchored before:
  MATH1 Bayes' Theorem    (mathematics.probability_measure)
  FL1  Deductive Validity (formal_logic)
  CHEM1 Periodic Law      (chemistry)

New source-type debuts (via SEP for formal_logic / Bayesian epistemology).
CHEM1 is the first chemistry anchor — basket audit noted this domain
has thin encyclopedia coverage (no Scholarpedia for most topics).

Run: python3 scripts/migrations/insert_tier1_batch3_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-tier1-batch3-2026-04-18"


ANCHORS = [
    # ==========================================================
    # MATH1 — Bayes' Theorem
    # ==========================================================
    ("MATH1", "doi", "10.1098/rstl.1763.0053", None,
     "Bayes 1763 - An Essay towards solving a Problem in the Doctrine of Chances",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Bayes 1763 (posthumous, communicated by Richard Price), "
     "Philosophical Transactions of the Royal Society 53, pp. 370-418. "
     "Verified via CrossRef API 2026-04-18. Laplace 1812 'Theorie "
     "analytique des probabilites' independently rediscovered and "
     "systematized but is not separately anchored here."),

    ("MATH1", "isbn", "978-0521592710", None,
     "Jaynes - Probability Theory: The Logic of Science",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Jaynes 2003 (posthumous, ed. G. L. Bretthorst). Cox-axiom-based "
     "axiomatization of Bayesian probability as extended logic. Fills "
     "the axiomatic_foundation slot for Bayes-as-inference."),

    ("MATH1", "isbn", "978-1439840955", None,
     "Gelman et al. - Bayesian Data Analysis (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Gelman et al. 2013, standard graduate Bayesian statistics "
     "textbook."),

    ("MATH1", "isbn", "978-0471494645", None,
     "Bernardo & Smith - Bayesian Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Bernardo & Smith 2000, rigorous decision-theoretic Bayesian "
     "treatment."),

    ("MATH1", "wikipedia",
     "https://en.wikipedia.org/wiki/Bayes%27_theorem",
     "1349118319",
     "Bayes' theorem",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch. P(A|B) = P(B|A)P(A)/P(B); "
     "Bayes 1763 citation present with DOI."),

    ("MATH1", "sep", "https://plato.stanford.edu/entries/bayes-theorem/",
     None,
     "Bayes' Theorem (Stanford Encyclopedia of Philosophy)",
     1, "canonical", "canonical_authority", "living_reference", "high",
     "SEP entry by James Joyce (2003, rev. 2021). Peer-reviewed "
     "authoritative treatment including conditional probability "
     "foundations, Bayesian inference, and probabilistic coherence. "
     "SEP is a canonical living_reference for mathematics-"
     "philosophy-adjacent topics."),

    ("MATH1", "scholarpedia",
     "http://www.scholarpedia.org/article/Bayesian_statistics", None,
     "Bayesian statistics (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Scholarpedia article expected; not fetched this session. "
     "Confidence medium pending retry."),

    # ==========================================================
    # FL1 — Deductive Validity
    # ==========================================================
    ("FL1", "isbn", "978-0691252322", None,
     "Aristotle - The Complete Works (Princeton, Barnes ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Aristotle's Organon (Prior Analytics, Posterior Analytics) is the "
     "historical ancestor of the concept of deductive validity. The "
     "MODERN formal definition (truth preservation under every "
     "interpretation) is Tarski's — see axiomatic_foundation anchor. "
     "Confidence medium because Aristotle captures the concept's "
     "origin but not its modern formal characterization."),

    ("FL1", "isbn", "978-0915144761", None,
     "Tarski - Logic, Semantics, Metamathematics",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Tarski 1956 (2nd ed. 1983 Hackett, ed. Corcoran). Contains the "
     "1936 paper 'On the Concept of Logical Consequence' which gives "
     "the modern semantic definition of validity: an argument is valid "
     "iff the conclusion is true in every interpretation where the "
     "premises are true."),

    ("FL1", "isbn", "978-0122384523", None,
     "Enderton - A Mathematical Introduction to Logic (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Enderton 2001, standard graduate-level mathematical logic "
     "textbook. Rigorous treatment of validity, soundness, "
     "completeness."),

    ("FL1", "isbn", "978-1447145578", None,
     "van Dalen - Logic and Structure (5th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "van Dalen 2013, standard introductory-to-intermediate logic "
     "textbook, strong on semantic vs syntactic consequence."),

    ("FL1", "wikipedia",
     "https://en.wikipedia.org/wiki/Validity_(logic)",
     "1335834261",
     "Validity (logic)",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Defines "
     "validity as 'takes a form that makes it impossible for the "
     "premises to be true and the conclusion false.'"),

    ("FL1", "sep",
     "https://plato.stanford.edu/entries/logical-consequence/", None,
     "Logical Consequence (Stanford Encyclopedia of Philosophy)",
     1, "canonical", "canonical_authority", "living_reference", "high",
     "SEP entry by JC Beall, Greg Restall, Gil Sagi (2005, rev. 2019). "
     "Authoritative peer-reviewed treatment of the concept of logical "
     "consequence / deductive validity — including model-theoretic and "
     "proof-theoretic accounts. SEP is the primary living_reference "
     "for formal_logic per basket audit §4.3."),

    # ==========================================================
    # CHEM1 — Periodic Law
    # ==========================================================
    ("CHEM1", "isbn", "978-0486445717", None,
     "Mendeleev - Periodic Law (Jensen, ed., Dover)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "'Mendeleev on the Periodic Law: Selected Writings, 1869-1905', "
     "ed. W.B. Jensen, Dover 2005. Contains Mendeleev's 1869 Russian "
     "Chemical Society paper in English. The 1869 paper predates DOI "
     "system. Moseley 1913/1914 Phil. Mag. papers established atomic-"
     "number ordering (also predate DOIs; not separately anchored this "
     "session but referenced in notes)."),

    ("CHEM1", "isbn", "978-0801403330", None,
     "Pauling - The Nature of the Chemical Bond (3rd ed.)",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "medium",
     "Pauling 1960, Cornell UP. Quantum-mechanical foundation for "
     "periodic trends via electron configuration and bonding. Not a "
     "strict axiomatization but the canonical link between QM and the "
     "periodic law. Confidence medium because this is interpretive "
     "rather than formal axiomatization."),

    ("CHEM1", "isbn", "978-0198769866", None,
     "Atkins - Physical Chemistry (11th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Atkins 2017, standard graduate physical chemistry textbook. "
     "Treats periodic trends in atomic-structure chapters."),

    ("CHEM1", "isbn", "978-0190914363", None,
     "Scerri - The Periodic Table: Its Story and Its Significance",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Scerri 2019 (2nd ed. Oxford UP). Definitive scholarly survey of "
     "the periodic table's history, philosophy, and current status. "
     "Fills comprehensive_survey for CHEM1."),

    ("CHEM1", "wikipedia",
     "https://en.wikipedia.org/wiki/Periodic_table",
     "1344168732",
     "Periodic table",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch. Notes Mendeleev 1869 "
     "and the atomic-number-based modern formulation via Moseley."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("MATH1", "FL1", "CHEM1"):
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
        for eid in ("MATH1", "FL1", "CHEM1"):
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

        cur.execute("""
            SELECT canonical_role, COUNT(*)
            FROM external_anchors
            WHERE canonical_role IS NOT NULL
            GROUP BY canonical_role
            ORDER BY CASE canonical_role
                WHEN 'progenitor' THEN 1 WHEN 'axiomatic_foundation' THEN 2
                WHEN 'standard_textbook' THEN 3 WHEN 'living_reference' THEN 4
                WHEN 'comprehensive_survey' THEN 5 END
        """)
        print(f"\nCanonical-role totals across all entries:")
        for row in cur.fetchall():
            print(f"  {row[0]:22} {row[1]}")

        cur.execute("""
            SELECT source, COUNT(*) FROM external_anchors
            GROUP BY source ORDER BY COUNT(*) DESC
        """)
        print(f"\nSource-type distribution:")
        for row in cur.fetchall():
            print(f"  {row[0]:15} {row[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

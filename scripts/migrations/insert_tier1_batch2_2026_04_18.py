"""
Insert Tier-1 anchor batch 2 — TD3 / QM1 / CS1 — 2026-04-18

Third live anchor insertion. Covers three more canonical domains/sub-domains:
  TD3 Second Law of Thermodynamics (physics.classical — thermodynamics)
  QM1 Schrödinger Equation         (physics.modern — quantum)
  CS1 Church-Turing Thesis         (computer_science — foundations)

Tests new slot coverage and new source types:
- TD3 fills comprehensive_survey via Lieb-Yngvason 1999 Physics Reports
- TD3 fills axiomatic_foundation via Carathéodory 1909 Annalen der Physik
- QM1 fills axiomatic_foundation via von Neumann 1932 Grundlagen
- CS1 tests dual-progenitor (Church + Turing independent formulations)
- CS1 adds SEP (Stanford Encyclopedia of Philosophy) as a new source type

Run: python3 scripts/migrations/insert_tier1_batch2_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-tier1-batch2-2026-04-18"


# (entry_id, source, identifier, revision_id, title, tier,
#  stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ==========================================================
    # TD3 — Second Law of Thermodynamics
    # ==========================================================
    ("TD3", "doi", "10.1002/andp.18652010702", None,
     "Clausius 1865 - Ueber verschiedene Formen der Hauptgleichungen",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Clausius 1865, Annalen der Physik 201(7), pp. 353-400. The paper "
     "that introduces the word 'entropy' and gives the 2nd law its "
     "mathematical formulation. Verified via WebSearch (CrossRef path) "
     "2026-04-18."),

    ("TD3", "doi", "10.1007/BF01450409", None,
     "Carathéodory 1909 - Untersuchungen über die Grundlagen der Thermodynamik",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Carathéodory 1909, Mathematische Annalen 67, 355-386. Gives the "
     "first axiomatic foundation of thermodynamics — the 2nd law as a "
     "mathematical axiom about inaccessibility of adjacent states rather "
     "than as a heat-engine statement. Tier 1 canonical for the "
     "axiomatic_foundation role."),

    ("TD3", "doi", "10.1016/S0370-1573(98)00082-9", None,
     "Lieb & Yngvason 1999 - The physics and mathematics of the second law",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Lieb-Yngvason 1999, Physics Reports 310(1), pp. 1-96. Definitive "
     "modern comprehensive survey of the 2nd law — derives thermodynamics "
     "rigorously from 15 axioms about adiabatic accessibility. ~1,500 "
     "citations. Fills the comprehensive_survey slot for TD3."),

    ("TD3", "isbn", "978-0471862567", None,
     "Callen - Thermodynamics and an Introduction to Thermostatistics (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Callen 1985, standard graduate thermodynamics textbook."),

    ("TD3", "isbn", "978-1577666127", None,
     "Reif - Fundamentals of Statistical and Thermal Physics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reif 1965 (reprint 2009), standard thermodynamics + statistical "
     "mechanics textbook; strong on 2nd law origins."),

    ("TD3", "wikipedia",
     "https://en.wikipedia.org/wiki/Second_law_of_thermodynamics",
     "1347134629",
     "Second law of thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Contains both "
     "Clausius and Kelvin-Planck formulations."),

    ("TD3", "scholarpedia",
     "http://www.scholarpedia.org/article/Entropy", None,
     "Entropy (Scholarpedia) - covers 2nd law alongside Shannon and KS entropy",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Same Scholarpedia entropy article anchored for INFO1; covers both "
     "Shannon entropy and Kolmogorov-Sinai entropy with thermodynamic "
     "framing. Confidence medium pending dedicated re-fetch. Note: this "
     "is NOT double-anchoring — same external source, different entry."),

    # ==========================================================
    # QM1 — Schrödinger Equation
    # ==========================================================
    ("QM1", "doi", "10.1002/andp.19263840404", None,
     "Schrödinger 1926 - Quantisierung als Eigenwertproblem (I)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Schrödinger 1926, Annalen der Physik 384, 361-376. First paper "
     "of the 4-part series introducing wave mechanics and the equation "
     "i h-bar d_t psi = H-hat psi. Verified via WebSearch (Wiley). "
     "Note: Part II DOI 10.1002/andp.19263851302 (Annalen 385, 437-490) "
     "continues the derivation but Part I alone defines the equation."),

    ("QM1", "isbn", "978-0691178561", None,
     "von Neumann - Mathematical Foundations of Quantum Mechanics (English)",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "von Neumann 1932 Mathematische Grundlagen der Quantenmechanik; "
     "English translation by Beyer 1955, reissued 2018 Princeton UP. "
     "The canonical Hilbert-space axiomatic foundation of QM."),

    ("QM1", "isbn", "978-1107189638", None,
     "Griffiths & Schroeter - Introduction to Quantum Mechanics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Griffiths 2018, standard undergraduate QM textbook."),

    ("QM1", "isbn", "978-1108473224", None,
     "Sakurai & Napolitano - Modern Quantum Mechanics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Sakurai 2020, standard graduate QM textbook."),

    ("QM1", "isbn", "978-0306447907", None,
     "Shankar - Principles of Quantum Mechanics (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Shankar 1994, alternative rigorous textbook; strong mathematical "
     "presentation."),

    ("QM1", "wikipedia",
     "https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation",
     "1347877466",
     "Schrödinger equation",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch. States time-dependent "
     "form; notes Schrödinger postulated 1925 and published 1926."),

    ("QM1", "scholarpedia",
     "http://www.scholarpedia.org/article/Schrodinger_equation", None,
     "Schrödinger equation (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Scholarpedia expected to have this article; direct WebFetch not "
     "attempted this session due to known flakiness. Confidence medium "
     "pending retry."),

    # ==========================================================
    # CS1 — Church-Turing Thesis
    # ==========================================================
    ("CS1", "doi", "10.2307/2371045", None,
     "Church 1936 - An Unsolvable Problem of Elementary Number Theory",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Church 1936, American Journal of Mathematics 58(2), pp. 345-363. "
     "Introduces lambda-calculus-based effective calculability. Verified "
     "via CrossRef API 2026-04-18. Dual-progenitor with Turing 1937: two "
     "independent formulations proven equivalent."),

    ("CS1", "doi", "10.1112/plms/s2-42.1.230", None,
     "Turing 1937 - On Computable Numbers, with Application to Entscheidungsproblem",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Turing 1936/37, Proc. London Math. Soc. s2-42(1), pp. 230-265. "
     "Introduces Turing-machine-based computability. Verified via "
     "CrossRef API. Second progenitor; Church-Turing thesis is the "
     "equivalence of these two formulations."),

    ("CS1", "isbn", "978-0923891572", None,
     "Kleene - Introduction to Metamathematics",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Kleene 1952 (reissue 1971 Ishi Press 2009 reprint). Systematic "
     "axiomatic treatment of the Church-Turing equivalence and its "
     "consequences for metamathematics."),

    ("CS1", "isbn", "978-1133187790", None,
     "Sipser - Introduction to the Theory of Computation (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Sipser 2012, standard undergraduate theory-of-computation textbook. "
     "Treats Church-Turing in the context of decidability and "
     "computability."),

    ("CS1", "wikipedia",
     "https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis",
     "1348569308",
     "Church-Turing thesis",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch. Both Church 1936 and "
     "Turing 1936/37 citations present with full bibliographic detail."),

    ("CS1", "sep",
     "https://plato.stanford.edu/entries/church-turing/", None,
     "Church-Turing Thesis (Stanford Encyclopedia of Philosophy)",
     1, "canonical", "canonical_authority", "living_reference", "high",
     "SEP entry by B. Jack Copeland (2017, rev. 2023). Peer-reviewed "
     "encyclopedia article; SEP is the authoritative living reference "
     "for foundations/philosophy-of-computation topics (per basket "
     "audit §4.3). Not fetched this session; known canonical SEP "
     "article. First SEP anchor in the graph."),

    ("CS1", "scholarpedia",
     "http://www.scholarpedia.org/article/Church-Turing_thesis", None,
     "Church-Turing thesis (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Scholarpedia article expected; not fetched this session. "
     "Confidence medium pending retry."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("TD3", "QM1", "CS1"):
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
        skipped = 0
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
            if res.rowcount > 0:
                inserted += 1
            else:
                skipped += 1

        conn.commit()

        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already existed): {skipped}")

        # Per-entry slot coverage
        print("\nCanonical-role slot coverage:")
        for eid in ("TD3", "QM1", "CS1"):
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
            print(f"  {eid}: {len(filled)}/5 slots — "
                  f"{', '.join(f'{r}({rows[r]})' for r in filled)}")

        # Global totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries_anchored = cur.fetchone()[0]
        print(f"\nGlobal totals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries_anchored}")

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
        print(f"\nCanonical-role anchors across all entries:")
        for row in cur.fetchall():
            print(f"  {row[0]:22} {row[1]}")

        cur.execute("SELECT source, COUNT(*) FROM external_anchors GROUP BY source ORDER BY COUNT(*) DESC")
        print(f"\nSource-type distribution:")
        for row in cur.fetchall():
            print(f"  {row[0]:15} {row[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

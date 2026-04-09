"""
M0 Primary-Source-Verified Calibration Addendum — 2026-04-08

Adds a second tranche of calibration records to confidence_calibration
in wiki_history.db, recording which M0 findings have been verified by
direct primary-source reading (as opposed to agent summaries of abstracts).

Uses a new audit_ref 'M0_2026-04-08_primary_sources' so the original M0
audit records are preserved unchanged. This preserves the audit trail
across multiple verification rounds.

Papers read in full (or to end of technical content):
  1. Machta-Chachra-Transtrum-Sethna, Science 342, 604 (2013)
     arXiv:1303.6738 (read in prior session)
  2. Transtrum-Machta-Brown-Daniels-Myers-Sethna, J. Chem. Phys.
     143, 010901 (2015); arXiv:1501.07668
  3. Mattingly-Transtrum-Abbott-Machta, PNAS 115, 1760 (2018)
     arXiv:1705.01166 (bonus; introduces d_eff terminology with
     different formula — mandatory citation)
  4. Brown-Bossomaier-Barnett, Sci. Rep. 12, 15145 (2022)
     arXiv:1810.09607 (prior art for broader research program)
  5. Quinn-Abbott-Transtrum-Machta-Sethna, Rep. Prog. Phys. 86,
     035901 (2023) (modern synthesis)

Run with:
  python3 scripts/migrations/m0_primary_source_verified_2026_04_08.py
"""

import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "M0_2026-04-08_primary_sources"
AUDIT_DATE = "2026-04-08"


# (entity_id, entity_type, confidence, short_status, rationale)
VERIFICATIONS = [
    # CCA entries — status unchanged, rationale updated with primary-source evidence
    ("CCA-1c", "cca_conjecture", "Supported",
     "Primary-source verified no prior art; Brown 2022 is prior art for broader research program",
     "Primary-source reading of 4 papers (Machta 2013, Transtrum 2015, "
     "Mattingly 2018, Brown-Bossomaier-Barnett 2022, Quinn 2023) confirmed "
     "NO prior art for CCA's specific curve-shape discriminator via FIM "
     "eigenvalue spectrum. HOWEVER: Brown et al. 2022 Sci. Rep. is prior "
     "art for the broader research program (information-theoretic "
     "discrimination of Potts transition order) using Global Transfer "
     "Entropy. They study q=2,5,7,10 and find curve-shape differences "
     "qualitatively similar to CCA-1c's claims, with a simple physical "
     "mechanism (cluster interfacial length, their Eqs. 5-6). CCA "
     "currently lacks a comparable physical mechanism. The highest-"
     "leverage scientific question: can CCA's d_eff/η be explained by "
     "interfacial geometry, or does it measure something structurally "
     "different from transfer entropy? Single-test status unchanged; "
     "promotion blocked on second test + mechanism question."),

    ("CCA-1b-magnitude", "cca_conjecture", "Supported",
     "Primary-source verified; Brown 2022 shows GTE peak convergence toward Tc as q increases",
     "Primary-source reading confirmed 20× dη/dT magnitude separation "
     "between q=10 (first-order) and q=2 (continuous) has no direct "
     "prior-art match. However, Brown et al. 2022 shows a related "
     "phenomenon in GTE: peak location converges toward Tc as q and "
     "L increase for first-order transitions, while staying stable "
     "above Tc for continuous (q=2). This is not the same observation "
     "(magnitude of derivative vs peak location), but it is in the same "
     "family. The q=3 vs q=5 test should be extended to q=2,5,7,10 to "
     "enable direct comparison with Brown et al.'s GTE results."),

    ("cca_d_eff_naming", "terminology", "Speculative",
     "MANDATORY CITATION: Mattingly 2018 uses 'd_eff' with a different formula",
     "Mattingly-Transtrum-Abbott-Machta 2018 PNAS defines d_eff = Σ_r "
     "r·Ω_r where Ω_r is the weight of the maximally informative "
     "discrete prior on edges of dimension r of the parameter manifold. "
     "This is a DIFFERENT formula from CCA's d_eff = (Σλ)²/Σλ² "
     "(participation ratio of FIM eigenvalue spectrum). Both are called "
     "d_eff and both measure 'effective dimensionality' in a sloppy-"
     "models sense. CCA MUST cite Mattingly 2018 and explicitly "
     "distinguish the two formulas. This is basic scholarly hygiene, "
     "not a novelty challenge — the formulas are different — but "
     "citing prior usage of the terminology is mandatory. Status: "
     "Speculative (pending the citation being actually added to "
     "CCA docs main body, not just the header note)."),

    # P5 — rationale refined per primary-source finding (Quinn 2023 admits Ising isn't sloppy microscopically)
    ("P5", "conjecture", "Supported",
     "Sloppy-models application; caveat from Quinn 2023 'Ising is not sloppy'",
     "Primary-source reading confirms: the Sethna lineage's own view "
     "is that Ising at its microscopic parameterization (2 params: h, "
     "J) is NOT a sloppy model (Quinn 2023 Section 8.2 explicitly "
     "states: 'The Ising model is not sloppy, and has no beautiful "
     "emergent theory, unless one only cares about long length and "
     "time scales'). Sloppiness in Ising emerges only under coarse-"
     "graining (Machta 2013). P5's validation on tori, random graphs, "
     "random geometric graphs is best framed not as 'applying sloppy "
     "models to Ising' but as 'applying the sloppy-models framework "
     "to a different class of geometric models'. Supported-as-"
     "application stays, but the 'application of what, to what' needs "
     "careful phrasing. Still not a novel discovery; Machta 2013 + "
     "Quinn 2023 are the canonical references."),

    # Fisher-gravity chain — primary-source reading confirmed nothing new (no sloppy-gravity bridge work exists)
    ("fisher_gravity_chain", "chain", "Speculative",
     "Primary-source reading confirmed: no sloppy-models-to-gravity bridge in the Sethna lineage",
     "Primary-source reading of 4 papers in the Sethna lineage "
     "(Machta 2013, Transtrum 2015, Mattingly 2018, Quinn 2023) found "
     "no connection to gravity, entanglement entropy, or information-"
     "theoretic derivations of Einstein equations. The Sethna program "
     "stays within dynamical systems, biology, and statistical "
     "mechanics. The M6→IT05→IT03→GT10→GT01 chain remains a "
     "conceptual analogy, not a theorem composition. No new "
     "information from primary-source reading that would rehabilitate "
     "the chain. Jacobson 2016 was not independently re-verified in "
     "this round."),
]


def populate(conn):
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for entity_id, entity_type, confidence, short_status, rationale in VERIFICATIONS:
        try:
            cur.execute("""
                INSERT INTO confidence_calibration
                    (entity_id, entity_type, confidence, calibration_date,
                     audit_ref, short_status, rationale)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (entity_id, entity_type, confidence, AUDIT_DATE,
                  AUDIT_REF, short_status, rationale))
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1
    conn.commit()
    return inserted, skipped


def summarize(conn):
    cur = conn.cursor()
    print("\n=== Primary-source-verified entries (M0 Fourth Addendum) ===")
    for row in cur.execute("""
        SELECT entity_id, confidence, short_status FROM confidence_calibration
        WHERE audit_ref = ?
        ORDER BY entity_id
    """, (AUDIT_REF,)):
        print(f"  [{row[1]:11s}] {row[0]:25s} {row[2][:55]}")

    print("\n=== All audit refs in confidence_calibration ===")
    for row in cur.execute("""
        SELECT audit_ref, COUNT(*) FROM confidence_calibration
        GROUP BY audit_ref
        ORDER BY audit_ref
    """):
        print(f"  {row[0]:40s} {row[1]:3d}")


def main():
    if not WIKI_HISTORY_DB.exists():
        raise SystemExit(f"wiki_history.db not found at {WIKI_HISTORY_DB}")
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        inserted, skipped = populate(conn)
        print(f"M0 primary-source-verified migration complete.")
        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already present): {skipped}")
        summarize(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

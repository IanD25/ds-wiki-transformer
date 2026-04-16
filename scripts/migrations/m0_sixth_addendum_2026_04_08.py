"""
M0 Sixth Addendum — 2026-04-08

Adds calibration corrections from primary-source reading of Saberi 2024
PRB and refined re-reading of Brown 2022.

Critical correction: the Fifth Addendum's characterization of Saberi 2024
was wrong. Their matrix M_ij = spin value at site (i,j) symmetrized — NOT
the connected correlation matrix. Different mathematical object from CCA.
Saberi 2024 is therefore NOT direct prior art for CCA's specific
construction. CCA's narrow novelty surface is slightly broader than the
Fifth Addendum claimed.

Brown 2022 mechanism analysis refined: Brown's GTE is a hybrid 2-point +
multi-point observable, not purely multi-point as Fifth Addendum stated.
Sharpened mechanism question: at first-order Potts, can a pure 2-point
observable (CCA) reproduce hybrid 2-point + multi-point discrimination
(Brown's GTE) or capture only partial signal?

Audit ref: M0_2026-04-08_sixth_addendum.

Run with:
  python3 scripts/migrations/m0_sixth_addendum_2026_04_08.py
"""

import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "M0_2026-04-08_sixth_addendum"
AUDIT_DATE = "2026-04-08"


CORRECTIONS = [
    # CCA-1c rationale refined: Saberi NOT direct prior art (correction)
    ("CCA-1c", "cca_conjecture", "Speculative",
     "Saberi 2024 is NOT direct prior art (different matrix); novelty surface slightly broader",
     "PRIMARY-SOURCE CORRECTION (Sixth Addendum): The Fifth Addendum "
     "characterized Saberi-Saber-Moessner 2024 PRB as the most direct "
     "prior art for CCA. Re-reading the primary source reveals this was "
     "WRONG. Saberi's matrix M_ij = spin value at site (i,j), "
     "symmetrized — this is the spin configuration ITSELF arranged as an "
     "L×L matrix with entries in {-1, 0, +1}. It is NOT the connected "
     "correlation matrix χ_ij = <s_i s_j>_c (which is L²×L² and has "
     "thermal-expectation-value entries). Different mathematical object. "
     "CCA's narrow novelty surface is slightly BROADER than Fifth "
     "Addendum claimed. Saberi DOES recover Onsager magnetization from "
     "rescaled max eigenvalue with exact β/ν=1/8, but uses a different "
     "matrix construction. The 'use connected correlation matrix "
     "spectrum + PR + isotropy as transition-order discriminator on "
     "Potts' approach remains specific to CCA among the papers searched. "
     "Status unchanged (Speculative single-test); the narrow-novelty "
     "surface is now: (1) per-site fields parameterization (still no "
     "lattice-physics prior art identified); (2) PR + isotropy as paired "
     "scalar observables (specific choice not in Vinayak/Saberi/Borgs-"
     "Chayes); (3) first-order Potts discrimination via these specific "
     "observables. The pattern 'matrix observables on 2D Ising at "
     "criticality reduce to standard critical exponents' is now confirmed "
     "by THREE independent constructions (Vinayak 2014, Saberi 2024, "
     "Borgs-Chayes 1996), strongly supporting the prediction that CCA "
     "continuous-transition observables also reduce to η_critical."),

    # Brown 2022 mechanism question sharpened (correction)
    ("CCA_brown_mechanism_question", "scientific_question", "Speculative",
     "Refined: Brown's GTE is hybrid 2-point + multi-point; CCA is pure 2-point",
     "PRIMARY-SOURCE REFINEMENT (Sixth Addendum): The Fifth Addendum "
     "characterized Brown's GTE as 'purely multi-point.' Re-reading the "
     "primary source: Brown's G ∝ Σ_c p(c)·L_c is HYBRID. L_c "
     "(interfacial length per cluster) is a sum of 2-point measurements "
     "(count nearest-neighbor pairs with different spin states). p(c) "
     "(cluster size distribution) is multi-point (cluster identity "
     "requires connectivity). CCA's d_eff and η are pure 2-point "
     "observables. At continuous transitions, both Brown's GTE and CCA's "
     "d_eff/η are functions of the same 2D Ising critical exponents (η, "
     "β/ν, d_f, τ via hyperscaling) and should track each other up to "
     "scaling factors. At first-order transitions, the multi-point part "
     "of Brown's observable may capture latent-heat / cluster-statistics "
     "information that CCA's pure 2-point observable cannot. SHARPENED "
     "MECHANISM QUESTION: at first-order Potts (q≥5), can a pure 2-point "
     "observable (CCA) reproduce the same transition-order discrimination "
     "that a hybrid 2-point + multi-point observable (Brown's GTE) "
     "achieves? Two outcomes: (1) CCA tracks Brown's GTE quantitatively "
     "at all q → CCA captures multi-point cluster info via 2-point "
     "observables (surprising, defensible novelty); (2) CCA captures only "
     "partial signal while Brown captures full → CCA is methodologically "
     "simpler but strictly less informative than Brown's. Test directly "
     "via q=2,5,7,10 sweep with both observables computed on same data."),

    # Saberi as external reviewer recommendation
    ("saberi_external_reviewer", "literature_priority", "Speculative",
     "Saberi is the obvious external reviewer for any CCA writeup",
     "Abbas Ali Saberi (University of Tehran / Max Planck Dresden) is "
     "uniquely positioned as external reviewer for CCA: he works on both "
     "(a) cluster geometry of 2D Ising — Saberi 2009 J. Stat. Mech. on "
     "interface walks in 2D Ising, cited by Brown-Bossomaier-Barnett "
     "2022 as the geometric backbone for their interfacial-length "
     "mechanism; AND (b) eigenvalue spectra of 2D-Ising-derived matrices "
     "— Saberi-Saber-Moessner 2024 PRB. He spans both literatures "
     "relevant to CCA without (apparently) connecting them in the way "
     "CCA does. If CCA is ever written up externally, direct "
     "correspondence with Saberi (ab.saberi@ut.ac.ir or "
     "saberi@pks.mpg.de) would resolve the novelty question definitively. "
     "He would either immediately recognize CCA as a known construction "
     "and point to where, or confirm its novelty within his expertise "
     "area. The fact that Saberi has worked on both literatures without "
     "(apparently) connecting them is mild evidence the connection has "
     "not been made — but only mild, since there could be a Saberi-"
     "coauthored paper outside the audit's search range."),

    # Pattern observation: 3 independent constructions show same reduction
    ("matrix_spectrum_reduces_to_critical_exponents",
     "pattern_observation", "Established",
     "Confirmed by 3 independent matrix constructions on 2D Ising",
     "ESTABLISHED PATTERN (Sixth Addendum): Three independent "
     "constructions of matrices derived from 2D Ising at criticality, "
     "all studied via eigenvalue spectrum analysis, all reduce to "
     "standard 2D Ising critical exponents: (1) Vinayak-Prosen-Buča-"
     "Seligman 2014 EPL — connected correlation matrix → power-law "
     "spectrum from η_critical=1/4; (2) Saberi-Saber-Moessner 2024 PRB "
     "— spin configuration matrix → Fréchet extremes from β/ν=1/8; "
     "(3) Borgs-Chayes 1996 J. Stat. Phys. — Potts covariance matrix → "
     "cluster connectivity from FK percolation exponents. This pattern "
     "is robust across different mathematical constructions on the same "
     "physical system. Implication for CCA: continuous-transition "
     "observables (Potts q≤4) on the connected correlation matrix are "
     "highly likely to reduce analytically to standard critical "
     "exponents. The Saberi 2024 derivation is a concrete model for how "
     "this reduction works. The analytical-comparison-at-T_c "
     "experimental check (Fifth Addendum recommendation, repeated here "
     "with stronger justification) should derive CCA's d_eff and η_CCA "
     "at T_c for q=2 from η_critical=1/4 and β/ν=1/8 via finite-size "
     "scaling, then compare to Phase B/C numerical results. If they "
     "agree, CCA continuous-transition observables are reading out known "
     "exponents and have no novel content there. If they disagree, "
     "something is being captured beyond standard exponents."),
]


def populate(conn):
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for entity_id, entity_type, confidence, short_status, rationale in CORRECTIONS:
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
    print("\n=== Sixth Addendum entries ===")
    for row in cur.execute("""
        SELECT entity_id, confidence, short_status FROM confidence_calibration
        WHERE audit_ref = ?
        ORDER BY entity_id
    """, (AUDIT_REF,)):
        print(f"  [{row[1]:11s}] {row[0]:50s} {row[2][:55]}")

    print("\n=== All audit refs in confidence_calibration ===")
    for row in cur.execute("""
        SELECT audit_ref, COUNT(*) FROM confidence_calibration
        GROUP BY audit_ref
        ORDER BY audit_ref
    """):
        print(f"  {row[0]:42s} {row[1]:3d}")


def main():
    if not WIKI_HISTORY_DB.exists():
        raise SystemExit(f"wiki_history.db not found at {WIKI_HISTORY_DB}")
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        inserted, skipped = populate(conn)
        print(f"M0 Sixth Addendum migration complete.")
        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already present): {skipped}")
        summarize(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

"""
M0 Deep-Research Pass — 2026-04-08

Adds a third tranche of calibration records to confidence_calibration in
wiki_history.db, recording the deep-research findings from the Fifth
Addendum:

1. Amendola 2024 verified — but "5σ" was a forecast, not current data.
   Current GWTC-3 data: 2σ upper limit k<2.1, ~3σ tension with k=3.
2. Cadoni 2023 verified — but is 7-author, says "universal" not
   "generic," and their own KS analysis prefers k=3 over k=1.
3. New prior art identified: Vinayak 2014 EPL (correlation matrix
   spectrum on 2D Ising at criticality, power-law from η_critical),
   Borgs-Chayes 1996 J. Stat. Phys. (Potts covariance matrix vs FK
   clusters, rigorous), Saberi-Saber-Moessner 2024 PRB (interaction-
   correlated RMT on 2D Ising).
4. Two terminology collisions: CCA's d_eff vs Mattingly 2018's d_eff
   (different formulas), CCA's η vs standard stat-mech η_critical
   (anomalous dimension of correlation function).
5. Brown 2022 mechanism question: at continuous transitions CCA
   observables likely reduce to standard η_critical; at first-order
   transitions they diverge from cluster interfacial length and may
   capture latent-heat / discontinuity structure that's CCA's
   candidate novel territory.

Audit ref: M0_2026-04-08_deep_research.

Run with:
  python3 scripts/migrations/m0_deep_research_2026_04_08.py
"""

import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "M0_2026-04-08_deep_research"
AUDIT_DATE = "2026-04-08"


VERIFICATIONS = [
    # P17 and P23: citations VERIFIED but statistical figures need correction
    ("P17", "conjecture", "Speculative",
     "VERIFIED: Amendola 2024 cite real but '5σ' was forecast not current data; ~3σ tension actual",
     "Amendola, Rodrigues, Kumar, Quartin 2024 (MNRAS 528, 2377; "
     "arXiv:2307.02474) verified via direct primary-source check. "
     "However: the '5σ rejection of k=3' wiki claim is INCORRECT — "
     "this figure refers to the paper's FORECAST for ~250 additional "
     "future GW events, not its current-data result. Current GWTC-3 "
     "data give 2σ upper limit k<2.1 (PLPP) or k<2.5 (direct method). "
     "Tension with k=3 from current data is ~2.6-3.7σ depending on "
     "methodology. Authors' own conclusion: 'strong tension... but "
     "there still is an open parameter space where it can survive the "
     "present test.' P17 status unchanged (still Speculative high-risk) "
     "but the quantitative wording must be corrected. Also: Cadoni "
     "2023 verified (JCAP 11, 007; arXiv:2306.11588) — 7-author paper, "
     "uses 'universal' not 'generic,' k=1 holds for regular BHs only "
     "(horizonless compact objects have additional model-dependent "
     "term). Crucially, Cadoni's own KS analysis on the Farrah "
     "elliptical-galaxy sample prefers k=3 over k=1 — they interpret "
     "this as evidence BHs may be non-GR, not as confirming their k=1 "
     "prediction. P17 wording should reflect this nuance. Both "
     "citations VERIFIED, both wordings need tightening."),

    ("P23", "conjecture", "Speculative",
     "VERIFIED: inherits Amendola+Cadoni citation corrections from P17",
     "P23 inherits all P17 GT11 tensions. Same citation corrections "
     "apply: Amendola 2024 is 2σ upper limit not 5σ; Cadoni 2023 is "
     "'universal' not 'generic' k=1 for regular BHs, with their own "
     "elliptical-sample analysis preferring k=3. Status unchanged "
     "(Speculative high-risk). Underlying tension between Cadoni k=1 "
     "theoretical prediction and Farrah-Croker k=3 observation is real, "
     "but neither side is empirically settled. P23's 'horizon formation "
     "as Bekenstein-saturation phase transition' framing is its own "
     "speculative claim distinct from k value."),

    # MAJOR new finding: CCA prior art is broader than the Fourth Addendum claimed
    ("CCA-1c", "cca_conjecture", "Speculative",
     "Prior art surface broadened: Vinayak 2014, Borgs-Chayes 1996, Saberi 2024 PRB join the map",
     "DEEP-RESEARCH PRIOR-ART UPDATE (Fifth Addendum): The CCA general "
     "approach 'FIM = connected correlation matrix spectrum on 2D "
     "lattice as transition probe' is broader prior art than the "
     "Fourth Addendum identified. Specifically: (1) Vinayak, Prosen, "
     "Buča, Seligman 2014 EPL 108, 20006 (arXiv:1403.7218) proves "
     "analytically that correlation-matrix eigenvalue density at 2D "
     "Ising criticality is power-law with exponent fixed by η_critical "
     "(=1/4 for 2D Ising). (2) Borgs-Chayes 1996 J. Stat. Phys. 82, "
     "1235 (arXiv:adap-org/9411001) rigorously connects Potts "
     "connected covariance matrix eigenvalues to Fortuin-Kasteleyn "
     "cluster representations and cluster diameter. (3) Saberi-Saber-"
     "Moessner 2024 PRB 110, L180102 (arXiv:2503.03472) is active 2024 "
     "work on interaction-correlated RMT on 2D Ising using top "
     "eigenvalue as order parameter. None of these compute "
     "participation ratio + isotropy as paired observables, none do "
     "Potts q>2, none discriminate first-order vs continuous via the "
     "specific CCA observables. So CCA's specific construction "
     "(PR + η_isotropy + first-order Potts discriminator) may still "
     "be narrow-novel, but the surface has shrunk substantially. The "
     "remaining candidate territory is the FIRST-ORDER regime (Potts "
     "q≥5), where scale invariance fails and the CCA observables "
     "cannot be derived from η_critical. At continuous transitions "
     "(Potts q≤4), CCA observables are LIKELY REDUCIBLE to η_critical "
     "via finite-size scaling — this can be tested directly via "
     "analytical comparison at T_c. Status unchanged (still "
     "Speculative single-test); blocked on Saberi 2024 read + "
     "analytical η_critical check."),

    # Mechanism question gets a tentative mathematical answer
    ("CCA_brown_mechanism_question", "scientific_question", "Speculative",
     "Tentative answer: at criticality both reduce to η_critical; at first-order they diverge",
     "MECHANISM QUESTION (Fifth Addendum): Can CCA's d_eff/η be "
     "explained via cluster interfacial geometry (Brown et al. 2022)? "
     "Tentative answer based on FIM=χ identification: at CONTINUOUS "
     "transitions in 2D (Potts q≤4), both CCA's spectrum observables "
     "and Brown's interfacial length are governed by the same "
     "underlying critical exponents (η_critical and cluster fractal "
     "dimension d_f). They should track each other up to scaling "
     "factors — neither is novel content; both reduce to standard "
     "critical exponents. At FIRST-ORDER transitions (Potts q≥5), "
     "scale invariance fails: 2-point function has exponential decay; "
     "cluster interfacial length is determined by latent heat / "
     "discontinuity structure. CCA observables (functions of 2-point "
     "correlation matrix) and Brown's interfacial length (multi-point "
     "geometric observable) DECOUPLE in this regime. Therefore both "
     "could distinguish transition order but via different mathematical "
     "mechanisms. The CCA observables in the first-order regime may "
     "capture the latent-heat / discontinuity structure of the FIM "
     "spectrum — this is the candidate territory for genuine narrow "
     "novelty. Concrete experimental check: at T=T_c for Potts q=2 "
     "(continuous in 2D), CCA's d_eff and η_CCA should be derivable "
     "from η_critical=1/4 via finite-size scaling. Compare to Phase "
     "B/C numerical results: if they agree, no novel content at "
     "continuous; if they disagree, something is captured beyond "
     "η_critical."),

    # NEW: terminology collision — CCA η vs standard stat-mech η
    ("cca_eta_naming", "terminology", "Speculative",
     "MANDATORY RENAME: CCA's η collides with standard stat-mech η_critical (anomalous dimension)",
     "Standard stat-mech η (anomalous dimension of two-point function): "
     "C(r) ~ r^(-(d-2+η)). For 2D Ising universality class, η=1/4. "
     "CCA's η (isotropy indicator of FIM eigenvalue spectrum) is a "
     "completely different object that shares the symbol. WORSE: "
     "since the FIM IS the connected correlation matrix and the "
     "standard η governs the spectrum of the correlation matrix at "
     "criticality, the two η's are mathematically RELATED (CCA's η at "
     "criticality is a function of the standard η_critical). This "
     "compounds the confusion. CCA must rename its η to avoid "
     "collision. Suggested: ι_CCA (iota for isotropy) or η_spec with "
     "explicit subscript or non-Greek symbol entirely. Status: "
     "Speculative pending the rename being done in CCA docs."),

    # Saberi 2024 PRB elevated to highest-priority single read
    ("saberi_2024_prb_priority_read", "literature_priority", "Speculative",
     "Highest-priority single paper: most direct prior art in CCA mathematical framework",
     "Saberi-Saber-Moessner 2024 PRB 110, L180102 (arXiv:2503.03472) "
     "constructs random-matrix ensemble from 2D Ising Boltzmann factors, "
     "finds bell-shaped bulk with universal heavy tail at criticality "
     "vs semicircle off-critical, uses rescaled max eigenvalues as "
     "order parameter, Fréchet extreme value statistics at criticality. "
     "Same general framework as CCA (correlation-matrix spectrum on "
     "2D Ising as transition probe), same target system, same "
     "publication timing (active research community 2024). "
     "Differences: top eigenvalue vs PR/isotropy as scalar observable; "
     "Ising only vs CCA's Potts q=2,10. Notably co-authored by Saberi, "
     "the SLE/cluster-perimeter expert cited by Brown-Bossomaier-"
     "Barnett 2022 — the same researcher works in both the cluster-"
     "geometry and correlation-matrix-RMT literatures. NOW THE "
     "HIGHEST-PRIORITY SINGLE PAPER for assessing CCA's novelty "
     "surface. Higher priority than Brown 2022 because it's more "
     "directly in CCA's specific mathematical framework. Owner must "
     "read this before any further CCA novelty claim."),
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
    print("\n=== Deep-research entries (M0 Fifth Addendum) ===")
    for row in cur.execute("""
        SELECT entity_id, confidence, short_status FROM confidence_calibration
        WHERE audit_ref = ?
        ORDER BY entity_id
    """, (AUDIT_REF,)):
        print(f"  [{row[1]:11s}] {row[0]:35s} {row[2][:60]}")

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
        print(f"M0 deep-research migration complete.")
        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already present): {skipped}")
        summarize(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

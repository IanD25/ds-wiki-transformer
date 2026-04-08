"""
M0 Audit Calibration Migration — 2026-04-08

Creates a confidence_calibration table in wiki_history.db and populates it
with the M0 audit findings for all 23 conjectures plus the CCA sub-conjectures
(which live only in docs) and the Fisher-gravity chain "discovery."

CRITICAL CONSTRAINTS (per charter + CLAUDE.md):
- Never schema-alter ds_wiki.db (read-only source of truth)
- All new tables go in wiki_history.db
- INSERT OR IGNORE / UPSERT throughout — safe to re-run
- Confidence levels: Established / Supported / Speculative / Falsified
- Every calibration entry references M0 as the audit reference

Run with: python3 scripts/migrations/m0_calibration_2026_04_08.py
"""

import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
M0_REF = "M0_2026-04-08"
AUDIT_DATE = "2026-04-08"


def create_schema(conn):
    """Create confidence_calibration table (idempotent)."""
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS confidence_calibration (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id       TEXT NOT NULL,
        entity_type     TEXT NOT NULL,
        confidence      TEXT NOT NULL CHECK(confidence IN (
                            'Established', 'Supported', 'Speculative',
                            'Falsified', 'Retired'
                        )),
        calibration_date TEXT NOT NULL,
        audit_ref       TEXT NOT NULL,
        short_status    TEXT,
        rationale       TEXT,
        UNIQUE(entity_id, calibration_date, audit_ref)
    );

    CREATE INDEX IF NOT EXISTS idx_cal_entity
        ON confidence_calibration(entity_id);
    CREATE INDEX IF NOT EXISTS idx_cal_confidence
        ON confidence_calibration(confidence);
    """)
    conn.commit()


# (entity_id, entity_type, confidence, short_status, rationale)
CALIBRATIONS = [
    # ===== ESTABLISHED =====
    ("P21", "conjecture", "Established",
     "Fisher-Rao universality — classical case only",
     "Chentsov 1982 + Amari 1985 uniqueness theorem. Classical case is "
     "Established. Quantum extension via Petz 1996 monotone metric family "
     "is Speculative (Bianconi GT04 bridge to gravity is analogy, not "
     "theorem). P21 main claim stays Established; quantum extension separate."),

    # ===== SUPPORTED (application of established work or single-domain empirical) =====
    ("P5", "conjecture", "Supported",
     "Re-parameterization of sloppy models (Machta 2013), not novel discovery",
     "The central claim 'Fisher Rank = effective dimensionality' restates "
     "the Sethna-group sloppy-models result. Machta-Chachra-Transtrum-Sethna "
     "Science 2013 (arXiv:1303.6738) computes FIM eigenvalue spectra on 2D "
     "Ising at criticality with stiff/sloppy hierarchy. P5's validation on "
     "tori, random graphs, random geometric graphs is Supported as "
     "application to new model classes. NOT Established as discovery. "
     "Owner's own notes: 'rank returns mixed integers on fractals' — "
     "complication already in the gap notes."),

    ("P18", "conjecture", "Supported",
     "Single-domain empirical observation (US equities 2003-2025)",
     "Empirical: participation ratio on US equities never reached FRAGMENTED "
     "regime under normal crisis conditions. Supported as single-domain "
     "observation. NOT supported as general structural claim. Needs "
     "replication on non-US markets, power grids, telecom before any "
     "generalization."),

    ("P19", "conjecture", "Supported",
     "Single-domain empirical (US equities only)",
     "Non-ergodicity of D_eff regime signals in Tier 3 domains. Only US "
     "equities tested. Only participation-ratio proxy tested. 4:1 "
     "recovery-to-crisis threshold from one dataset. Supported as "
     "observation, NOT as cross-domain claim."),

    ("P20", "conjecture", "Supported",
     "Empirical fit, single-domain (AlphaEntropy 19-variant testing)",
     "Subadditive error propagation formula fit to 19 A/B variants in "
     "financial domain. Supported as empirical fit. NOT supported as "
     "theoretical principle. ρ estimated qualitatively, not measured."),

    ("CCA-1b-magnitude", "cca_conjecture", "Supported",
     "Single-test qualitative support, cautiously narrow-novel",
     "dη/dT ~20× magnitude separation between Potts q=10 (first-order) and "
     "q=2 (continuous). Phase C+D 2026-04-07 experiments. Single comparison "
     "only. Charter rule: cannot promote beyond Speculative-Supported "
     "without second test (q=3 vs q=5). No confirmed prior art across 3 "
     "targeted searches, but residual risks remain (Tkačik 2015 supp, "
     "expert correspondence)."),

    ("CCA-1c", "cca_conjecture", "Supported",
     "Single-test qualitative, candidate narrow-novel, blocked on 2nd test",
     "Curve shape discriminator: continuous = smooth sigmoid; first-order = "
     "flat-jump-plateau. Phase D 2026-04-07. Single comparison. No prior "
     "art found across 3 targeted searches (Machta 2013 doesn't do it; "
     "Brown-Bossomaier-Barnett 2022 uses transfer entropy not FIM; "
     "inverse-Ising community uses FIM for inference not phase-transition "
     "spectroscopy). POSSIBLY narrow-novel pending: (i) second test, "
     "(ii) direct expert correspondence, (iii) Tkačik 2015 supp check."),

    ("CCA-2", "cca_conjecture", "Supported",
     "d_eff = d_lattice + 1 confirmed for 2D and 3D tori only",
     "Confirmed for 2D and 3D tori in Phase A. Regular-lattice topology "
     "family only. Needs test on irregular lattices, random graphs, other "
     "topology classes."),

    # ===== SPECULATIVE =====
    ("P1", "conjecture", "Speculative",
     "Heterodox cosmology, no independent support",
     "Cosmological redshift as dimensional gradient attenuation rather than "
     "metric expansion. Alternative to ΛCDM. Depends on Ω_D scaling operator "
     "(itself speculative). Own gap notes: 'null result constrains but does "
     "not decisively falsify.'"),

    ("P2", "conjecture", "Speculative",
     "DFIG-framed reparameterization of WBE metabolic scaling",
     "α = D_eff/(D_eff+1) functional form is West-Brown-Enquist 1997 and "
     "extensions. The 'tracks D_eff' framing is owner-constructed. "
     "Underlying WBE is Established in the metabolic scaling literature. "
     "The specific D_eff identification is Speculative. Needs micro-CT "
     "vascular data that does not exist at required resolution."),

    ("P3", "conjecture", "Speculative",
     "Three λ exponents, formal audit not performed",
     "Single Ω_D governs G, h, m. Over/under-constraint status unresolved. "
     "Owner's own gap: 'formal audit (Test 3) has not yet been performed.'"),

    ("P4", "conjecture", "Speculative",
     "No experimental discrimination from speed-limit interpretation",
     "CcO 1.5 ms as thermodynamic refresh rate vs kinetic speed limit. "
     "Own gap: 'no direct measurement has distinguished refresh rate from "
     "speed limit in vivo.' Acoustic Quantum Code hypothesis lacks "
     "independent experimental confirmation."),

    ("P6", "conjecture", "Speculative",
     "PARTIALLY CONTRADICTED by own Phase 1 results",
     "Fisher rank ↔ Hausdorff dimension convergence. Owner's own Phase 1 "
     "notes say 'gap-based rank returns mixed integers on fractals' — "
     "direct convergence does NOT hold. Claim survives only through "
     "participation ratio (a different observable from rank). Should "
     "arguably be reformulated as a PR claim or retired."),

    ("P7", "conjecture", "Speculative",
     "PARTIALLY FALSIFIED — PR fails monotonicity under all tested configs",
     "D_eff monotonically decreasing under coarse-graining. Owner's Phase 1 "
     "notes: 'Participation ratio does NOT satisfy monotonicity under any "
     "tested configuration.' Only gap-based rank on lattices under "
     "block-spin satisfies it. The claim as stated is too strong; needs "
     "reformulation or retirement."),

    ("P8", "conjecture", "Speculative",
     "Rediscovery of Janke-Johnston-Kenna-style FIM-distinguishes-order",
     "Continuous critical exponent interpolation on fractional-D substrates. "
     "Gefen et al. 1980 precedes the fractal-substrate work. Phase 2 "
     "results (SV degeneracy swap at continuous transitions, absent at "
     "first-order) are consistent with the broader FIM-discriminates-order "
     "literature (Janke-Johnston-Kenna 2004 for scalar curvature; "
     "Machta 2013 for spectrum). Supported as rediscovery within the "
     "lineage, Speculative as novel claim."),

    ("P9", "conjecture", "Speculative",
     "Monitoring gate, not an active conjecture",
     "Holographic dictionary LWE complexity. Owner's own notes: 'This is a "
     "monitoring gate tracking developments in quantum complexity theory, "
     "not an active experimental programme.' Should be reclassified as an "
     "Open Question (Q-series) rather than a conjecture (P-series)."),

    ("P10", "conjecture", "Speculative",
     "One of several consistent interpretations; no unique predictions",
     "Hadron charge radii via running ℏ. Own gap: 'The GUP interpretation "
     "is one of several consistent with existing hadron data. No unique "
     "predictions have been generated.'"),

    ("P11", "conjecture", "Speculative",
     "Reframing of Bettencourt-West urban scaling literature",
     "Urban scaling = network spectral dimension. Uses same D/(D+1) form "
     "as P2 metabolic scaling. Spectral dimension of urban infrastructure "
     "networks not routinely measured. Cross-city datasets sparse."),

    ("P12", "conjecture", "Speculative",
     "Untested — no published cross-domain measurement exists",
     "β(λ) formula predicts scaling exponents cross-domain. Own gap: 'No "
     "published study has measured d_f, λ, and β simultaneously in two "
     "different domains.' Untestable without owner-generated data."),

    ("P13", "conjecture", "Speculative",
     "Owner-acknowledged ansatz, not derived from first principles",
     "λ_min = (d_f-1)/(d_f+1) capacity bound. Owner's own gap: 'The "
     "(d_f-1)/(d_f+1) functional form is an ansatz — not derived from "
     "first principles.' λ_min proxy from BMR/MMR ratios needs validation."),

    ("P14", "conjecture", "Speculative",
     "Requires data that does not exist at required resolution",
     "Branching variance predicts exponent gap. Needs high-resolution "
     "micro-CT across diverse taxa. Depends on Q1 resolution."),

    ("P15", "conjecture", "Speculative",
     "Owner-acknowledged ansatz; financial-market 'evidence' is analogy",
     "Metabolic cost ∝ (1-λ)² d_f. Own gap: 'The formula is an ansatz — "
     "see Q5 for the derivation challenge. No controlled experiment has "
     "varied λ independently of other physiological parameters.' "
     "AlphaEntropy financial results are analogy-level, not a test of "
     "the specific formula."),

    ("P16", "conjecture", "Speculative",
     "Blocked by Q4; no test performed",
     "RLCT = d_f at regime transitions. 'The mapping of metabolism to a "
     "statistical learning problem (Q4) has not been done. P16 is currently "
     "blocked by Q4 progress.'"),

    ("P17", "conjecture", "Speculative",
     "HIGH RISK: unstable foundation, unverified citations, owner-constructed bridge",
     "Cosmological coupling = D_eff. Rests on contested Farrah-Croker 2023 "
     "observational claim. Critical citations NOT verifiable by audit: "
     "Amendola 2024 '5σ GW rejection of k=3' and Cadoni 2023 JCAP "
     "'k=1 generic' — both PENDING OWNER PRIMARY-SOURCE VERIFICATION. "
     "The D_eff = k identification is owner-constructed, not standard in "
     "cosmology literature. Multiple 2024-2025 tensions documented (GW, "
     "Gaia BH, JWST AGN). Highest-risk speculative claim in the wiki."),

    ("P22", "conjecture", "Speculative",
     "Trichotomy unproven as exhaustive; MBL status open in CM theory",
     "Irreversible lockout trichotomy for SSB. Recent (2026-03-30) stress "
     "test absorbed topological lockout. Whether MBL survives the "
     "thermodynamic limit is open (Roeck-Huveneers avalanche instability). "
     "Individual mechanisms are established; the trichotomy as exhaustive "
     "classification is unproven."),

    ("P23", "conjecture", "Speculative",
     "HIGH RISK: inherits all GT11 tensions; no first-principles derivation",
     "Horizon formation as Bekenstein-saturation phase transition. Inherits "
     "all P17/GT11 tensions (GW 5σ pending verification, Gaia BH, JWST "
     "AGN, Cadoni k=1 pending verification). No first-principles derivation "
     "of coupling mechanism. Novel framing not independently supported."),

    # ===== FALSIFIED =====
    ("CCA-1", "cca_conjecture", "Falsified",
     "Phase C 2026-04-07: Potts q=10 and q=2 show identical η signatures",
     "Original claim: (d_eff>1, η>0.35) only at continuous transitions. "
     "Phase C Monte Carlo: Potts q=10 (first-order) and q=2 (continuous) "
     "both show η ≈ 0.42, d_eff = 3.0, PR = 3.66 at T_c. Clean falsification. "
     "Kept in DB for historical record only."),

    ("CCA-1b-scaling", "cca_conjecture", "Falsified",
     "Phase D 2026-04-07: L^d scaling does not materialize",
     "Claim: S_max ~ L^d for first-order transitions. Phase D numba-JIT MC "
     "on L=16, 32, 48 showed q=10 scales as L^0.12 (weak growth), not L^d. "
     "dη/dT is grid-resolution-limited, not physics-limited — saturates "
     "at L=16 already. The 20× absolute separation survived (CCA-1b-magnitude "
     "Supported) but the scaling prediction is FALSIFIED."),

    # ===== DOWNGRADED DISCOVERIES (not conjectures but claimed structural findings) =====
    ("fisher_gravity_chain", "chain", "Speculative",
     "DOWNGRADED from 'structural coherence result' to conceptual analogy",
     "M6→IT05→IT03→GT10→GT01 chain. M0 audit found: stacking vocabulary, "
     "not composing theorems. Jacobson 2016 uses von Neumann entanglement "
     "entropy on quantum subalgebra via modular Hamiltonian, NOT classical "
     "Fisher information or classical KL divergence on a parameter "
     "manifold. The chain conflates three distinct mathematical objects "
     "sharing the word 'relative entropy.' Jacobson 2016 is also only "
     "linearized — full nonlinear Einstein not derived. No prior art "
     "found bridging sloppy models / classical FIM to emergent gravity. "
     "The chain is conceptual, not structural."),

    ("GT10_as_CCA_instance", "claim", "Speculative",
     "Post-hoc feature fit to 5-feature checklist",
     "Claim that Jacobson's entanglement equilibrium is a CCA instance "
     "because it satisfies the 5 descriptive features (F1-F5 in STAT3). "
     "M0 audit: satisfying a post-hoc descriptive checklist is not "
     "predictive support. Unless CCA makes a sharp mathematical "
     "discriminator that GT10 satisfies non-trivially, this is pattern "
     "matching. Downgrade from 'Supported' to 'Speculative post-hoc fit.'"),
]


def populate(conn):
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for entity_id, entity_type, confidence, short_status, rationale in CALIBRATIONS:
        try:
            cur.execute("""
                INSERT INTO confidence_calibration
                    (entity_id, entity_type, confidence, calibration_date,
                     audit_ref, short_status, rationale)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (entity_id, entity_type, confidence, AUDIT_DATE,
                  M0_REF, short_status, rationale))
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1
    conn.commit()
    return inserted, skipped


def summarize(conn):
    cur = conn.cursor()
    print("\n=== Confidence distribution (M0 audit) ===")
    for row in cur.execute("""
        SELECT confidence, COUNT(*) FROM confidence_calibration
        WHERE audit_ref = ?
        GROUP BY confidence
        ORDER BY CASE confidence
            WHEN 'Established' THEN 1
            WHEN 'Supported' THEN 2
            WHEN 'Speculative' THEN 3
            WHEN 'Falsified' THEN 4
            WHEN 'Retired' THEN 5
        END
    """, (M0_REF,)):
        print(f"  {row[0]:15s} {row[1]:3d}")

    print("\n=== By entity type ===")
    for row in cur.execute("""
        SELECT entity_type, COUNT(*) FROM confidence_calibration
        WHERE audit_ref = ?
        GROUP BY entity_type
    """, (M0_REF,)):
        print(f"  {row[0]:20s} {row[1]:3d}")


def main():
    if not WIKI_HISTORY_DB.exists():
        raise SystemExit(f"wiki_history.db not found at {WIKI_HISTORY_DB}")
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        create_schema(conn)
        inserted, skipped = populate(conn)
        print(f"M0 calibration migration complete.")
        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already present): {skipped}")
        summarize(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

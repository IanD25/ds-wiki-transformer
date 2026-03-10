"""
add_tier2_links.py  — Tier 2 Semantic Links

Adds semantic links between DS-native entries and reference_law entries
(and between DS-native entries) based on structural derivational relationships.

Link types:
  derives from   — mathematically or logically derived (B5 from TD3, B3 from RD1)
  implements     — concrete instantiation of abstract law (X4 implements QM1)
  generalizes    — DS-native extends reference_law to D dimensions or broader scope
  analogous to   — parallel mathematical structure across domains

Confidence tiers:
  1.5  — strong structural connection, direct derivation or instantiation
  2    — indirect derivation, analogical connection, or weaker evidence

Run: .venv/bin/python scripts/add_tier2_links.py [--dry-run]
"""

import sqlite3, sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import SOURCE_DB

# ===========================================================================
# TIER 2 LINK DATA
# (source_id, target_id, link_type, confidence_tier, description)
# ===========================================================================

TIER2_LINKS = [

    # -------------------------------------------------------------------------
    # Dimensional Scaling Operator (OmD) generalizes fundamental reference laws
    # OmD modifies G, ℏ, and m when D_eff ≠ 4 — extending each to D dimensions
    # -------------------------------------------------------------------------
    ("OmD", "GV1", "generalizes", "1.5",
     "Ω_D modifies Newton's G and the metric in the Einstein field equations when D_eff ≠ 4, "
     "extending general relativity to effective D-dimensional spacetime."),
    ("OmD", "CM2", "generalizes", "1.5",
     "Ω_D modifies Newton's gravitational constant G, making the inverse-square law D-dependent: "
     "F ∝ r^(−(D−1)) in D spatial dimensions."),
    ("OmD", "QM1", "generalizes", "1.5",
     "Ω_D modifies the effective Planck constant ℏ_eff = Ω_D^λ_h·ℏ, altering Schrödinger "
     "dynamics when effective dimensionality departs from 4."),
    ("OmD", "EM1", "generalizes", "2",
     "Ω_D modifies electric permittivity in D-dimensional space, altering Gauss's law "
     "and the force law from inverse-square to inverse-(D−1)-power."),
    ("OmD", "EM6", "generalizes", "2",
     "Coulomb's law F ∝ r^−2 becomes F ∝ r^−(D−1) under Ω_D dimensional scaling, "
     "with k_eff depending on the effective spatial dimension."),

    # -------------------------------------------------------------------------
    # G1 (Dimensional Redshift Law) derives from and generalizes GR and Newtonian gravity
    # -------------------------------------------------------------------------
    ("G1", "GV1", "derives from", "1.5",
     "The dimensional redshift formula z(r) = exp(∫(1/D_eff)(dD_eff/dr)dr) − 1 is derived "
     "from the Einstein field equations by allowing the metric's effective dimensionality "
     "to vary with position."),
    ("G1", "CM2", "generalizes", "1.5",
     "The effective Hubble parameter H_eff = (c/D_eff)(dD_eff/dr) generalizes Newton's "
     "gravitational framework to regions of varying effective dimensionality, recovering "
     "Newtonian gravity when D_eff is uniform."),
    ("G1", "GV3", "generalizes", "2",
     "Gravitational Gauss's law in D-varying space must account for dimensional gradients; "
     "G1's redshift formula encodes the cumulative effect of dimensional structure on "
     "light propagation."),

    # -------------------------------------------------------------------------
    # G3 (Holographic Complexity Bound) derives from GR and quantum mechanics
    # -------------------------------------------------------------------------
    ("G3", "GV1", "derives from", "1.5",
     "The Bekenstein entropy bound S ≤ A/(4ℓ_P²) underlying holographic complexity "
     "derives from the Einstein field equations applied to black hole thermodynamics."),
    ("G3", "QM1", "derives from", "2",
     "Holographic bulk reconstruction is a quantum mechanical problem; the exponential "
     "complexity bound C ≥ 2^Ω(n) follows from quantum information-theoretic arguments "
     "about reconstructing quantum states from boundary data."),

    # -------------------------------------------------------------------------
    # B5 (Landauer's Principle) derives from second law of thermodynamics
    # -------------------------------------------------------------------------
    ("B5", "TD3", "derives from", "1.5",
     "Landauer's minimum erasure energy E_min = k_B T ln 2 is derived directly from the "
     "second law: erasing one bit irreversibly reduces distinguishable states by half, "
     "requiring at least k_B T ln 2 of entropy to be produced."),
    ("B5", "TD2", "derives from", "2",
     "Landauer's principle also follows from the first law: the work done in erasing "
     "one bit must equal the heat dissipated, with both bounded below by k_B T ln 2."),

    # -------------------------------------------------------------------------
    # B3 (Wien's Displacement Law) derives from Planck's Law and Planck-Einstein relation
    # -------------------------------------------------------------------------
    ("B3", "RD1", "derives from", "1.5",
     "Wien's displacement law λ_max = b/T is derived by differentiating Planck's "
     "spectral distribution u(ν,T) with respect to ν and setting it to zero, giving "
     "x·e^x/(e^x − 1) = 5 where x = hν/k_BT."),
    ("B3", "RD3", "derives from", "1.5",
     "Wien's displacement law depends on the Planck-Einstein relation E = hν to convert "
     "between wavelength and frequency peak, with b = hc/(x·k_B) where x ≈ 4.965."),

    # -------------------------------------------------------------------------
    # B2 (Arrhenius) derives from thermodynamic/statistical mechanics principles
    # -------------------------------------------------------------------------
    ("B2", "TD3", "derives from", "1.5",
     "The Arrhenius exponential k = A·exp(−E_a/k_BT) follows from Boltzmann statistics: "
     "the fraction of molecules with energy ≥ E_a at temperature T is exp(−E_a/k_BT) "
     "per the second law's Boltzmann factor."),
    ("B2", "TD7", "derives from", "2",
     "The Arrhenius equation is a direct application of the Boltzmann transport equation's "
     "equilibrium distribution: the Maxwell-Boltzmann speed distribution gives the fraction "
     "of collisions with energy above the activation barrier."),

    # -------------------------------------------------------------------------
    # C1 (Metabolic Scaling) derives from and implements geometric/physical laws
    # -------------------------------------------------------------------------
    ("C1", "A1", "derives from", "1.5",
     "Metabolic scaling B ∝ M^(D_eff/(D_eff+1)) derives from the Square-Cube Law: "
     "surface area scales as L^(D_eff−1) and volume as L^D_eff, so the "
     "surface-to-volume ratio (constraining nutrient/oxygen delivery) "
     "gives the metabolic exponent as D_eff/(D_eff+1)."),
    ("C1", "FM4", "implements", "2",
     "Metabolic scaling in vascular organisms implements Poiseuille's r^4 flow law: "
     "the fractal vascular network optimizes over hierarchical branching such that "
     "the aggregate transport capacity scales as M^(D_eff/(D_eff+1))."),

    # -------------------------------------------------------------------------
    # H5 (β(λ)) derives from C1 and implements the D_eff/D_eff+1 formula
    # -------------------------------------------------------------------------
    ("H5", "C1", "derives from", "1.5",
     "The scaling exponent β(λ) = λ·d_f/(d_f+1) + (1−λ) generalizes Kleiber's "
     "metabolic exponent D_eff/(D_eff+1) to systems with partial fractal coherence λ, "
     "recovering C1 exactly when λ=1 (full fractal regime)."),

    # -------------------------------------------------------------------------
    # T1 (Fisher Rank Monotonicity) derives from information-theoretic laws
    # -------------------------------------------------------------------------
    ("T1", "AM5", "derives from", "2",
     "Fisher Rank Monotonicity (D_eff decreases under coarse-graining) is a consequence "
     "of the Data Processing Inequality — a theorem in information theory that follows "
     "from the same symmetry reasoning as Noether's theorem applied to statistical models."),

    # -------------------------------------------------------------------------
    # T2 (Metabolic Exponent Test) implements C1 and validates A1
    # -------------------------------------------------------------------------
    ("T2", "C1", "implements", "1.5",
     "The Metabolic Exponent–Dimensionality Correlation test directly implements Kleiber's "
     "Law by predicting α = D_eff/(D_eff+1) and testing this against paired metabolic and "
     "micro-CT measurements in the same organism."),

    # -------------------------------------------------------------------------
    # Instantiations (X-entries) implement reference_laws
    # -------------------------------------------------------------------------
    ("X4", "QM1", "implements", "1.5",
     "X4 (Quantum Systems) applies the Schrödinger equation framework to regime-first "
     "analysis: quantum phase regimes are defined by the eigenstates and evolution of Ĥ."),
    ("X4", "QM2", "implements", "1.5",
     "X4 (Quantum Systems) implements the Heisenberg uncertainty principle as a regime "
     "boundary: the ΔxΔp ≥ ℏ/2 bound defines the minimum resolution of quantum regimes."),
    ("X3", "TD3", "implements", "1.5",
     "X3 (Statistical Physics) applies the Second Law of Thermodynamics as the governing "
     "constraint: entropy maximization defines the statistical physics regime's equilibrium."),
    ("X3", "TD5", "implements", "1.5",
     "X3 (Statistical Physics) implements the Fundamental Thermodynamic Relation: "
     "dU = TdS − PdV + Σμ_i dN_i governs energy flows in the statistical physics regime."),
    ("X5", "BIO3", "implements", "1.5",
     "X5 (Ecological Networks) implements Fisher's Fundamental Theorem: mean fitness "
     "maximization drives ecological regime dynamics via additive genetic variance selection."),
    ("X5", "F3", "implements", "1.5",
     "X5 (Ecological Networks) implements Gause's Competitive Exclusion Principle: "
     "the ecological regime's species coexistence structure is bounded by this law."),
    ("X1", "FM4", "implements", "1.5",
     "X1 (Vascular/Metabolic) directly implements Poiseuille's Law: the r^4 flow resistance "
     "in branching vessel networks determines the metabolic scaling exponent via fractal "
     "vascular geometry."),
    ("X1", "C1", "implements", "1.5",
     "X1 (Vascular/Metabolic) is the primary biological instantiation of Kleiber's "
     "Metabolic Scaling Law, operationalizing B = B_0 M^α in mammalian vascular systems."),
    ("X2", "M6", "implements", "1.5",
     "X2 (Information Geometry) directly implements Fisher Information Rank as its "
     "dimensionality measure: D_eff = rank(ℱ(ℓ)) is the core equation governing the "
     "information geometry regime's observable complexity."),
    ("X2", "AM3", "implements", "2",
     "X2 (Information Geometry) implements Hamilton's equations: the Fisher metric defines "
     "a Riemannian structure on statistical manifolds with Hamiltonian geodesic flow."),
    ("X6", "M6", "implements", "1.5",
     "X6 (Neural Networks) implements Fisher Information Rank to measure effective "
     "dimensionality of neural representations: D_eff = rank(ℱ) counts distinguishable "
     "neural coding dimensions at a given observation scale."),
    ("X7", "BIO1", "implements", "2",
     "X7 (Developmental Biology) implements Mendelian inheritance laws as the genetic "
     "substrate: developmental trajectories are constrained by Mendelian allele "
     "segregation at each cell division."),

    # -------------------------------------------------------------------------
    # M6 (Fisher Information Rank) derives from quantum/statistical mechanics
    # -------------------------------------------------------------------------
    ("M6", "QM2", "analogous to", "2",
     "Fisher Information Rank is the classical information-geometric analog of the "
     "Heisenberg Uncertainty Principle: both bound the simultaneous precision of "
     "parameter estimation, with ΔθΔp ≥ ℏ/2 and ΔΘ ≥ 1/√(F) as parallel limits."),

    # -------------------------------------------------------------------------
    # Ax1 (Information Primacy) connects to quantum and thermodynamic foundations
    # -------------------------------------------------------------------------
    ("Ax1", "QM2", "analogous to", "2",
     "The Information Primacy axiom (information bounds observables) is analogous to "
     "the Heisenberg Uncertainty Principle: both assert that the precision of knowledge "
     "about a system is fundamentally bounded, not by technology but by information limits."),
    ("Ax1", "TD3", "derives from", "2",
     "Information Primacy is grounded in the second law: entropy = missing information, "
     "so the irreversibility of information loss (erasure) is thermodynamically bounded "
     "by k_B T ln 2 per bit (Landauer's Principle)."),

    # -------------------------------------------------------------------------
    # B4 (Rayleigh Scattering) derives from classical electromagnetism
    # -------------------------------------------------------------------------
    ("B4", "EM4", "derives from", "2",
     "Rayleigh scattering σ ∝ d^6/λ^4 is derived from Maxwell's equations (Ampere-Maxwell "
     "law): a small sphere in an oscillating electric field re-radiates at the same "
     "frequency, with cross-section proportional to (ω/c)^4 from the radiation reaction."),
    ("B4", "EM6", "derives from", "2",
     "Rayleigh scattering involves oscillating dipoles induced by the electromagnetic "
     "wave; the induced dipole moment follows from Coulomb's law (EM6) applied to "
     "the polarizable sphere, giving the d^6/λ^4 dependence."),

    # -------------------------------------------------------------------------
    # F2 (Liebig's Law) analogous to thermodynamic constraint
    # -------------------------------------------------------------------------
    ("F2", "TD5", "analogous to", "2",
     "Liebig's Law of the Minimum is structurally analogous to the Fundamental "
     "Thermodynamic Relation's binding term: the minimum operator selects the binding "
     "chemical potential (scarcest resource), just as μ_i dN_i selects the binding "
     "component in multi-component thermodynamics."),

    # -------------------------------------------------------------------------
    # A2 (Richardson Effect) connects to fractal geometry laws
    # -------------------------------------------------------------------------
    ("A2", "ES14", "analogous to", "2",
     "Richardson's fractal coastline effect is analogous to Walther's Law in geology: "
     "both reveal how apparent structure depends on the scale of observation — the "
     "'length' of a coastline and the 'facies' seen in a stratigraphic section both "
     "depend on measurement resolution."),

]


# ===========================================================================
# INSERT LOGIC
# ===========================================================================

def run(db_path: str, dry_run: bool = False):
    print(f"DB: {db_path}")
    conn = sqlite3.connect(db_path)

    # Get existing links to avoid duplicates
    existing = set()
    for row in conn.execute("SELECT source_id, target_id, link_type FROM links"):
        existing.add((row[0], row[1], row[2]))

    # Get max link_order
    max_order_cur = conn.execute("SELECT MAX(link_order) FROM links").fetchone()
    next_order = (max_order_cur[0] or 0) + 1

    # Validate entry ids
    all_ids = set(r[0] for r in conn.execute("SELECT id FROM entries"))
    # Also add conjecture and gate ids
    all_ids.update(r[0] for r in conn.execute("SELECT id FROM conjectures"))
    all_ids.update(r[0] for r in conn.execute("SELECT id FROM gates"))

    rows_to_insert = []
    skipped_existing = 0
    skipped_invalid = 0

    for src, tgt, ltype, tier, desc in TIER2_LINKS:
        if (src, tgt, ltype) in existing or (tgt, src, ltype) in existing:
            skipped_existing += 1
            continue
        if src not in all_ids:
            print(f"  WARNING: source '{src}' not found in DB — skipping")
            skipped_invalid += 1
            continue
        if tgt not in all_ids:
            print(f"  WARNING: target '{tgt}' not found in DB — skipping")
            skipped_invalid += 1
            continue
        # Get labels
        src_label = conn.execute(
            "SELECT COALESCE(title, id) FROM entries WHERE id=?", (src,)
        ).fetchone()
        tgt_label = conn.execute(
            "SELECT COALESCE(title, id) FROM entries WHERE id=?", (tgt,)
        ).fetchone()
        if not src_label:
            src_label = conn.execute(
                "SELECT COALESCE(title, id) FROM conjectures WHERE id=?", (src,)
            ).fetchone()
        if not tgt_label:
            tgt_label = conn.execute(
                "SELECT COALESCE(title, id) FROM conjectures WHERE id=?", (tgt,)
            ).fetchone()
        src_label = src_label[0] if src_label else src
        tgt_label = tgt_label[0] if tgt_label else tgt
        rows_to_insert.append((ltype, src, src_label, tgt, tgt_label, desc, next_order, tier))
        next_order += 1

    print(f"Links defined       : {len(TIER2_LINKS)}")
    print(f"Skipped (existing)  : {skipped_existing}")
    print(f"Skipped (invalid id): {skipped_invalid}")
    print(f"Will insert         : {len(rows_to_insert)}")

    if dry_run:
        print("\nDRY RUN — Tier 2 links to insert:")
        for row in rows_to_insert:
            ltype, src, sl, tgt, tl, desc, order, tier = row
            print(f"  [{tier}] {src} --[{ltype}]--> {tgt}")
            print(f"       {desc[:80]}...")
        return

    # Live insert
    cur = conn.cursor()
    inserted = 0
    for row in rows_to_insert:
        try:
            cur.execute("""
                INSERT INTO links
                    (link_type, source_id, source_label, target_id, target_label,
                     description, link_order, confidence_tier)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
            inserted += 1
        except Exception as e:
            print(f"ERROR: {e}")

    conn.commit()
    conn.close()
    print(f"\nTier 2 links inserted: {inserted}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add Tier 2 semantic links")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(SOURCE_DB, dry_run=args.dry_run)

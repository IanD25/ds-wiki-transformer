"""
Insert two new entries to bridge the NE pillar isolation:

  GT07: Non-Equilibrium Spacetime Thermodynamics (Eling-Guedens-Jacobson 2006 / Chirco-Liberati 2010)
        Bridges NE ↔ GT: gravitational entropy production σ is the spacetime analog of
        Jarzynski dissipated work W_diss and Seifert trajectory entropy production s_tot.

  IT06: Seifert Stochastic Thermodynamics (Seifert 2012)
        Bridges NE ↔ IT: ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0 is the information-theoretic
        proof of the second law; all fluctuation theorems follow from this single identity.
        Also bridges NE ↔ IT08 (Fisher-Rao): minimum-dissipation paths are geodesics.

Current NE cross-pillar density:
  NE ↔ IT: 0 pairs ≥ 0.80  →  target: IT06 provides the direct bridge
  NE ↔ GT: 0 pairs ≥ 0.80  →  target: GT07 provides the direct bridge
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

# ---------------------------------------------------------------------------
# Entry definitions
# ---------------------------------------------------------------------------

ENTRIES = [
    {
        "id": "GT07",
        "title": "GT07: Non-Equilibrium Spacetime Thermodynamics",
        "filename": "GT07_nonequilibrium_spacetime_thermodynamics.md",
        "entry_type": "reference_law",
        "scale": "cross-scale",
        "domain": "physics · information",
        "status": "established",
        "confidence": "Tier 1",
        "type_group": "GT",
        "authoring_status": "",
        "formality_tier": 1,
    },
    {
        "id": "IT06",
        "title": "IT06: Seifert Stochastic Thermodynamics",
        "filename": "IT06_seifert_stochastic_thermodynamics.md",
        "entry_type": "reference_law",
        "scale": "cross-scale",
        "domain": "information · physics",
        "status": "established",
        "confidence": "Tier 1",
        "type_group": "IT",
        "authoring_status": "",
        "formality_tier": 1,
    },
]

# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------

SECTIONS = {
    "GT07": [
        (0, "What It Claims",
         "Jacobson's 1995 derivation of Einstein's equations from the Clausius relation "
         "δQ = TdS assumes equilibrium: the horizon entropy changes reversibly, with zero "
         "internal entropy production. Eling, Guedens, and Jacobson (2006) showed this "
         "assumption fails for modified gravity theories (f(R) gravity): the derivation "
         "requires a non-equilibrium correction term — an entropy production rate σ ≥ 0 "
         "on the horizon. The full non-equilibrium spacetime thermodynamic relation is "
         "δQ = T(dS − σ), where σ is produced by the shear of null congruences generating "
         "the horizon, governed by the Raychaudhuri equation. Chirco and Liberati (2010) "
         "extended this: gravitational dissipation — the viscous damping of spacetime "
         "curvature fluctuations — plays the role of entropy production in the "
         "non-equilibrium extension, giving spacetime an effective bulk viscosity. "
         "This connects the Jacobson programme directly to non-equilibrium thermodynamics: "
         "the Clausius relation δQ = TdS is the equilibrium limit (σ = 0), and the "
         "non-equilibrium generalisation requires the same conceptual framework as the "
         "Jarzynski equality and Crooks fluctuation theorem — a thermodynamic identity "
         "valid for irreversible processes that reduces to the equilibrium relation in "
         "the quasi-static limit. The gravitational entropy production rate σ is the "
         "spacetime analog of the dissipated work W_diss = ⟨W⟩ − ΔF in the Jarzynski "
         "equality and the trajectory entropy production s_tot = log[P_F/P_R] in "
         "Seifert's stochastic thermodynamics."),

        (1, "Mathematical Form",
         "Non-equilibrium spacetime thermodynamics:\n"
         "  δQ = T(dS − σ)\n\n"
         "where:\n"
         "  δQ = heat flux through the local Rindler horizon\n"
         "  T  = Unruh temperature = ℏa/2πck_B\n"
         "  dS = horizon entropy change\n"
         "  σ  ≥ 0  = internal entropy production rate (from horizon shear)\n\n"
         "Raychaudhuri equation (governs σ):\n"
         "  dθ/dλ = −(1/2)θ² − σ_μν σ^μν + ω_μν ω^μν − R_μν k^μ k^ν\n"
         "  (shear tensor σ_μν terms are entropy-producing)\n\n"
         "Equilibrium limit (σ = 0) → Jacobson 1995:\n"
         "  δQ = TdS → G_μν + Λg_μν = 8πG T_μν  (Einstein equations)\n\n"
         "Non-equilibrium analog structure:\n"
         "  σ ≥ 0  ↔  W_diss = ⟨W⟩ − ΔF ≥ 0  (Jarzynski)\n"
         "  σ ≥ 0  ↔  s_tot = log[P_F/P_R] ≥ 0 on average (Seifert)\n"
         "  σ = 0  ↔  reversible quasi-static process (Clausius)"),

        (2, "Constraint Category",
         "Thermodynamic (Th): The non-equilibrium spacetime thermodynamic relation "
         "δQ = T(dS − σ) is an irreversibility constraint on gravitational dynamics. "
         "The entropy production term σ ≥ 0 is the gravitational counterpart of the "
         "dissipated work bound ⟨W_diss⟩ ≥ 0 in the Jarzynski equality and the "
         "trajectory-level entropy production ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0 in Seifert's "
         "stochastic thermodynamics. All three — gravitational σ, thermodynamic W_diss, "
         "and stochastic s_tot — quantify the irreversibility of a process that reduces "
         "to an equilibrium identity (Clausius / Jarzynski / fluctuation theorem) in the "
         "reversible limit. The non-equilibrium extension of Jacobson's derivation "
         "therefore bridges the gravity-thermodynamics programme (GT pillar) to "
         "non-equilibrium thermodynamics (NE pillar) at the level of their shared "
         "entropy-production structure."),

        (3, "DS Cross-References",
         "GT01 (Jacobson Thermodynamic Derivation — the non-equilibrium extension directly "
         "generalises Jacobson's equilibrium δQ = TdS; setting entropy production σ = 0 "
         "recovers exactly Jacobson's derivation and the Einstein equations). "
         "NE03 (Jarzynski Equality — the Jarzynski dissipated-work bound ⟨W_diss⟩ ≥ 0 is "
         "the non-equilibrium thermodynamic analog of the gravitational entropy production "
         "σ ≥ 0; both reduce to the equilibrium second law in the reversible limit). "
         "NE04 (Crooks Fluctuation Theorem — the full probability distribution of "
         "gravitational entropy production would obey a Crooks-type fluctuation symmetry; "
         "a quantum gravitational fluctuation theorem extending Crooks to horizon processes "
         "is the outstanding open question bridging GT07 and NE04). "
         "IT06 (Seifert Stochastic Thermodynamics — the gravitational entropy production "
         "rate σ is the continuous-spacetime analog of Seifert's trajectory-level entropy "
         "production s_tot = log[P_F/P_R]; both provide the non-equilibrium correction to "
         "the equilibrium Clausius/Jarzynski identity). "
         "HB06 (Black Hole Area Theorem — the Raychaudhuri equation governs the horizon "
         "shear that produces σ; the non-negativity σ ≥ 0 is equivalent to the area "
         "theorem dA/dt ≥ 0 in the classical vacuum limit). "
         "HB09 (Generalised Second Law — the GSL dS_total/dt ≥ 0 is the integrated "
         "form of the non-equilibrium condition σ ≥ 0; the GSL is the global statement, "
         "GT07 provides the local non-equilibrium dynamics)."),

        (4, "Mathematical Archetype",
         "Mathematical archetype: conservation-law\n\n"
         "The non-equilibrium spacetime thermodynamic relation is a monotonicity law: "
         "total entropy (horizon entropy dS plus bulk entropy production σ) is "
         "non-decreasing. The entropy production term σ ≥ 0 is structurally identical "
         "to the Jarzynski dissipated-work bound W_diss ≥ 0 and Seifert's stochastic "
         "entropy production ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0. All three are instances of "
         "the same monotonicity structure: a total entropy budget is non-decreasing under "
         "time evolution, with the production term measuring the degree of irreversibility. "
         "The equilibrium case (σ = 0, W_diss = 0, s_tot = 0) corresponds to a reversible "
         "process; the non-equilibrium case produces entropy proportional to the "
         "irreversibility of the process."),

        (5, "What The Math Says",
         "Jacobson (1995) assigned heat δQ = T dS to each patch of spacetime horizon and "
         "derived Einstein's equations. Eling et al. (2006) showed that for f(R) gravity, "
         "the entropy of the horizon changes not just due to heat flux but also due to "
         "internal entropy production σ from the shear of the null congruences generating "
         "the horizon. The Raychaudhuri equation controls this shear: the shear tensor "
         "σ_μν contributes a term −σ_μν σ^μν ≤ 0 that focusses the horizon, producing "
         "entropy. Setting σ = 0 (no shear, reversible horizon) recovers Jacobson's "
         "Einstein equations. Non-zero σ leads to modified gravity equations. "
         "Chirco and Liberati (2010) showed this entropy production is a gravitational "
         "viscosity: spacetime has an effective bulk viscosity coefficient ζ that damps "
         "non-equilibrium perturbations, analogous to the viscosity of a fluid. "
         "The non-equilibrium relation δQ = T(dS − σ) parallels the Jarzynski equality "
         "exactly: the equilibrium free energy identity ΔF = W (reversible work) becomes "
         "W = ΔF + W_diss (non-equilibrium), where W_diss ≥ 0 measures irreversibility. "
         "In gravitational thermodynamics, the reversible Clausius relation δQ = TdS "
         "becomes δQ = T(dS − σ), where σ ≥ 0 measures gravitational irreversibility. "
         "The outstanding open question is whether a full gravitational fluctuation theorem "
         "exists — extending Crooks' P_F(a)/P_R(−a) = e^a to the distribution of σ over "
         "horizon fluctuations."),

        (6, "Concept Tags",
         "• non-equilibrium spacetime thermodynamics\n"
         "• Jacobson derivation extension\n"
         "• gravitational entropy production\n"
         "• Clausius relation\n"
         "• horizon shear viscosity\n"
         "• Raychaudhuri equation\n"
         "• f(R) gravity\n"
         "• gravitational dissipation\n"
         "• non-equilibrium Clausius\n"
         "• bulk viscosity of spacetime\n"
         "• entropy production rate\n"
         "• dissipated work analog\n"
         "• irreversible horizon dynamics\n"
         "• gravitational fluctuation theorem"),
    ],

    "IT06": [
        (0, "What It Claims",
         "Seifert's stochastic thermodynamics (Seifert, Rep. Prog. Phys. 75, 126001, 2012) "
         "provides the microscopic framework unifying all non-equilibrium fluctuation theorems "
         "under a single information-theoretic identity. For any stochastic process described "
         "by a trajectory x(t), the trajectory-level entropy production is "
         "s_tot[x(t)] = log[P_F[x(t)] / P_R[x̃(t)]], where P_F is the probability of the "
         "forward trajectory and P_R is the probability of the time-reversed trajectory under "
         "the reverse protocol. The integral fluctuation theorem ⟨e^{−s_tot}⟩ = 1 holds "
         "exactly for any stochastic process, and the Jarzynski equality and Crooks "
         "fluctuation theorem follow as special cases by setting "
         "s_tot = β(W − ΔF). The average entropy production equals the KL divergence "
         "between forward and reverse path distributions: "
         "⟨s_tot⟩ = D_KL(P_F || P_R) ≥ 0. This is the information-theoretic proof of the "
         "second law: entropy production is non-negative because KL divergence is "
         "non-negative — irreversibility is distinguishability of forward from reverse. "
         "Stochastic thermodynamics further reveals that the Fisher-Rao metric governs the "
         "geometry of optimal non-equilibrium processes: minimum-dissipation paths between "
         "thermodynamic states are geodesics on the Fisher-Rao manifold of probability "
         "distributions, connecting non-equilibrium thermodynamics directly to information "
         "geometry."),

        (1, "Mathematical Form",
         "Trajectory entropy production:\n"
         "  s_tot[x(t)] = log[ P_F[x(t)] / P_R[x̃(t)] ]\n\n"
         "Integral fluctuation theorem (master identity):\n"
         "  ⟨e^{−s_tot}⟩ = 1   (exact, any protocol, any initial condition)\n\n"
         "Second law from Jensen's inequality:\n"
         "  ⟨s_tot⟩ = D_KL(P_F || P_R) ≥ 0\n\n"
         "Special cases:\n"
         "  Jarzynski:  s_tot = β(W − ΔF)\n"
         "              → ⟨e^{−β(W−ΔF)}⟩ = 1\n"
         "              → ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0\n\n"
         "  Crooks:     P_F(s_tot = a) / P_R(s_tot = −a) = e^a\n"
         "              (detailed fluctuation theorem / time-reversal symmetry)\n\n"
         "Minimum dissipation (thermodynamic geometry):\n"
         "  ⟨W_diss⟩ ≥ (1/τ) ∫ g_ij λ̇^i λ̇^j dt\n"
         "  where g_ij = Fisher-Rao metric on parameter space\n"
         "  Equality: minimum-dissipation path is a geodesic on Fisher-Rao manifold"),

        (2, "Constraint Category",
         "Informatic-Thermodynamic (In-Th): Stochastic thermodynamics reveals that "
         "irreversibility is fundamentally a statement about distinguishability of "
         "probability distributions. The entropy production s_tot = log(P_F/P_R) is the "
         "log-likelihood ratio — the fundamental quantity in statistical hypothesis testing "
         "— applied to the question: is this trajectory consistent with forward or reverse "
         "dynamics? The second law ⟨s_tot⟩ ≥ 0 follows from D_KL(P_F||P_R) ≥ 0, "
         "connecting thermodynamic irreversibility to information-theoretic "
         "distinguishability. The non-negativity of KL divergence (IT03) is therefore the "
         "information-theoretic foundation of the second law, the Jarzynski equality "
         "(NE03), and the Crooks fluctuation theorem (NE04) — all are consequences of "
         "D_KL ≥ 0 instantiated in different physical settings. The Fisher-Rao metric "
         "(IT08) connection shows that information geometry governs not just the statistics "
         "of thermodynamic states but the optimal dynamics between them: dissipation is "
         "minimised by following geodesics on the Fisher-Rao manifold."),

        (3, "DS Cross-References",
         "IT03 (KL Divergence — ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0 is the fundamental identity "
         "connecting stochastic entropy production to KL divergence; the second law IS "
         "KL non-negativity at the trajectory level; all fluctuation theorems follow from "
         "this single information-theoretic fact). "
         "NE03 (Jarzynski Equality — Jarzynski follows from the integral fluctuation theorem "
         "⟨e^{−s_tot}⟩ = 1 by setting s_tot = β(W − ΔF); stochastic thermodynamics "
         "provides its microscopic derivation, trajectory-level interpretation, and the "
         "proof that ⟨W_diss⟩ = D_KL(P_F||P_R) × k_BT). "
         "NE04 (Crooks Fluctuation Theorem — Crooks follows from the detailed fluctuation "
         "symmetry P_F(a)/P_R(−a) = e^a of the entropy production distribution; "
         "stochastic thermodynamics is the general framework from which Crooks is derived). "
         "IT08 (Fisher-Rao Metric — minimum-dissipation non-equilibrium processes are "
         "geodesics on the Fisher-Rao manifold; the Fisher metric governs the thermodynamic "
         "cost of non-equilibrium driving at rate 1/τ, connecting information geometry "
         "to entropy production). "
         "GT07 (Non-Equilibrium Spacetime Thermodynamics — the gravitational entropy "
         "production rate σ in Chirco-Liberati is the continuous spacetime analog of "
         "Seifert's trajectory entropy production s_tot; both provide the non-equilibrium "
         "correction to the equilibrium Clausius/Jarzynski identity)."),

        (4, "Mathematical Archetype",
         "Mathematical archetype: conservation-law\n\n"
         "Stochastic thermodynamics is a monotonicity framework: "
         "⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0. The trajectory entropy production s_tot is a "
         "stochastic variable that can be negative on individual trajectories (rare events "
         "that look like they violate the second law) but has non-negative mean. "
         "The integral fluctuation theorem ⟨e^{−s_tot}⟩ = 1 is the exact master identity; "
         "Jensen's inequality e^{⟨−x⟩} ≤ ⟨e^{−x}⟩ gives ⟨s_tot⟩ ≥ 0 immediately. "
         "The framework unifies all non-equilibrium fluctuation theorems — Jarzynski, "
         "Crooks, the fluctuation-dissipation theorem — as consequences of this single "
         "exact statement about stochastic trajectories. The information-geometric "
         "interpretation (minimum dissipation = geodesic on Fisher-Rao manifold) adds a "
         "geometric layer: entropy production measures deviation from the geodesic path "
         "through the space of probability distributions."),

        (5, "What The Math Says",
         "For any physical process described by a stochastic trajectory x(t) — the "
         "position of a colloidal particle in a trap, the conformation of a protein being "
         "pulled, the chemical state of a molecular motor — assign to the trajectory a "
         "number s_tot equal to the log ratio of the probability of observing this forward "
         "trajectory under the forward protocol to the probability of observing the "
         "time-reversed trajectory under the reversed protocol. This number fluctuates from "
         "trajectory to trajectory and can in principle be negative (corresponding to "
         "trajectories that look, briefly, like they violate the second law). "
         "The integral fluctuation theorem states that the exponential average of −s_tot "
         "equals exactly 1, for any driving protocol, any duration, and any initial "
         "condition. Jensen's inequality then gives the second law: the mean entropy "
         "production ⟨s_tot⟩ is non-negative. Setting s_tot = β(W − ΔF) recovers the "
         "Jarzynski equality ⟨e^{−β(W−ΔF)}⟩ = 1 and the bound ⟨W_diss⟩ ≥ 0. "
         "Taking the ratio of the probability of observing entropy production a to the "
         "probability of observing −a gives the Crooks relation P_F(a)/P_R(−a) = e^a. "
         "The information-theoretic content: ⟨s_tot⟩ = D_KL(P_forward || P_reverse), "
         "the KL divergence between forward and reverse path distributions. Entropy "
         "production measures how distinguishable the forward process is from its time "
         "reverse — precisely the log-likelihood ratio that a statistician would compute "
         "to test time-reversal symmetry. The minimum-dissipation result follows from the "
         "Cramér-Rao bound applied to the Fisher-Rao metric on the space of thermodynamic "
         "states: the fastest path between states with minimum entropy production is a "
         "geodesic, with dissipation proportional to the geodesic distance squared divided "
         "by the protocol duration."),

        (6, "Concept Tags",
         "• stochastic thermodynamics\n"
         "• trajectory entropy production\n"
         "• integral fluctuation theorem\n"
         "• detailed fluctuation theorem\n"
         "• KL divergence and entropy production\n"
         "• time-reversal symmetry\n"
         "• non-equilibrium work\n"
         "• Jarzynski from stochastic thermodynamics\n"
         "• Crooks from stochastic thermodynamics\n"
         "• Fisher-Rao metric and minimum dissipation\n"
         "• information geometry of non-equilibrium\n"
         "• log-likelihood ratio\n"
         "• thermodynamic irreversibility\n"
         "• forward and reverse path distributions\n"
         "• Jensen's inequality"),
    ],
}

# ---------------------------------------------------------------------------
# Links
# ---------------------------------------------------------------------------

LINKS = [
    # GT07 links
    ("GT07", "GT01", "derives from", "1.5",
     "Non-equilibrium extension directly generalises Jacobson's equilibrium δQ = TdS; "
     "σ = 0 recovers Jacobson's derivation exactly"),
    ("GT07", "NE03", "analogous to", "1.5",
     "Gravitational entropy production σ ≥ 0 is the spacetime analog of Jarzynski "
     "dissipated work W_diss ≥ 0; both reduce to equilibrium identity at σ = W_diss = 0"),
    ("GT07", "NE04", "analogous to", "1.5",
     "A quantum gravitational Crooks-type fluctuation theorem for σ would be the "
     "gravitational counterpart of Crooks' P_F/P_R = e^{β(W-ΔF)}"),
    ("GT07", "IT06", "analogous to", "1.5",
     "Gravitational entropy production σ is the spacetime analog of Seifert's trajectory "
     "entropy production s_tot = log[P_F/P_R]"),
    ("GT07", "HB06", "derives from", "1.5",
     "Raychaudhuri equation governing horizon shear (entropy production) is equivalent "
     "to the area theorem dA/dt ≥ 0 in the classical vacuum limit"),
    ("GT07", "HB09", "derives from", "1.5",
     "GSL dS_total ≥ 0 is the integrated global statement of the local non-equilibrium "
     "condition σ ≥ 0 that GT07 provides the dynamics for"),

    # IT06 links
    ("IT06", "IT03", "derives from", "1.5",
     "⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0 — the second law IS KL non-negativity at trajectory "
     "level; stochastic thermodynamics gives this identity its physical grounding"),
    ("IT06", "NE03", "generalizes", "1.5",
     "Jarzynski equality follows from the integral fluctuation theorem ⟨e^{-s_tot}⟩ = 1 "
     "by setting s_tot = β(W - ΔF); IT06 is the general framework"),
    ("IT06", "NE04", "generalizes", "1.5",
     "Crooks fluctuation theorem follows from the detailed fluctuation symmetry "
     "P_F(a)/P_R(-a) = e^a of the entropy production distribution"),
    ("IT06", "IT08", "couples to", "1.5",
     "Minimum-dissipation non-equilibrium processes are geodesics on the Fisher-Rao "
     "manifold; IT08 provides the geometric structure that governs optimal IT06 paths"),
    ("IT06", "GT07", "analogous to", "1.5",
     "Seifert's s_tot = log[P_F/P_R] is the stochastic analog of Chirco's gravitational "
     "entropy production σ; both are non-equilibrium corrections to equilibrium identities"),
]


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    labels = {r[0]: r[1] for r in cur.execute("SELECT id, title FROM entries")}

    for entry in ENTRIES:
        existing = cur.execute("SELECT id FROM entries WHERE id = ?", (entry["id"],)).fetchone()
        if existing:
            print(f"  SKIP (exists): {entry['id']}")
            continue

        cur.execute(
            """INSERT INTO entries
               (id, title, filename, entry_type, scale, domain, status, confidence,
                type_group, authoring_status, formality_tier)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (entry["id"], entry["title"], entry["filename"], entry["entry_type"],
             entry["scale"], entry["domain"], entry["status"], entry["confidence"],
             entry["type_group"], entry["authoring_status"], entry["formality_tier"])
        )
        print(f"  Inserted entry: {entry['id']} — {entry['title']}")

        for order, name, content in SECTIONS[entry["id"]]:
            cur.execute(
                "INSERT INTO sections (entry_id, section_name, section_order, content) "
                "VALUES (?, ?, ?, ?)",
                (entry["id"], name, order, content)
            )
            print(f"    Section [{order}]: {name} ({len(content)} chars)")

    # Update labels to include new entries
    labels.update({e["id"]: e["title"] for e in ENTRIES})

    print()
    for src, tgt, lt, tier, desc in LINKS:
        src_label = labels.get(src, src)
        tgt_label = labels.get(tgt, tgt)
        cur.execute(
            "INSERT OR IGNORE INTO links "
            "(link_type, source_id, source_label, target_id, target_label, description, link_order, confidence_tier) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (lt, src, src_label, tgt, tgt_label, desc, 0, tier)
        )
        print(f"  Link: {src} → {tgt} ({lt})")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Inserting GT07 + IT06 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)

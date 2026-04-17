"""
Insert X8: Financial Market Entropy Production Proxy

New entry defining σ(t) = v(t)²/D_eff(t) as the instantaneous dissipation
rate of a market regime transition, where v(t) = dD_eff/dt is the velocity
of the participation ratio.

This entry:
  1. Defines the proxy formula and its physical motivation
  2. Documents the three empirical crisis archetypes (k-means clusters)
  3. Connects to GT07 (Chirco), IT06 (Seifert), HB09 (GSL) as thermodynamic
     analogs — without overclaiming equivalence
  4. Defines the geodesic test (P21 connection) as a falsifiable prediction

Honest framing throughout: this is a proxy measure motivated by analogy
with non-equilibrium thermodynamics, not a formally derived entropy production
from a statistical model of returns.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRY = {
    "id": "X8",
    "title": "X8: Financial Market Entropy Production Proxy",
    "filename": "X8_financial_entropy_production.md",
    "entry_type": "instantiation",
    "scale": "cross-scale",
    "domain": "information geometry, finance, non-equilibrium thermodynamics",
    "status": "established",
    "confidence": "Tier 2†",
    "type_group": "X",
    "authoring_status": "Fully authored",
    "formality_tier": 3,
}

SECTIONS = [
    (0, "Overview",
     "The financial market entropy production proxy σ(t) measures how far a market "
     "regime transition is from a quasi-static (reversible) path. It is computed from "
     "the velocity of the effective dimensionality D_eff — the rate at which the "
     "participation ratio of the EWMA correlation matrix is changing:\n\n"
     "  σ(t) = v(t)² / D_eff(t)    where v(t) = dD_eff/dt\n\n"
     "High σ(t) means a fast collapse of market degrees of freedom occurring when few "
     "dimensions remain — the most dissipative possible transition. Low σ(t) means a "
     "slow, near-reversible evolution. The total dissipation Σ = ∫σ dt over a crisis "
     "episode is the market analog of total entropy produced in a non-equilibrium "
     "thermodynamic process.\n\n"
     "This entry documents the empirical proxy, its three crisis archetypes, and its "
     "connections to formal non-equilibrium thermodynamics (GT07, IT06). "
     "IMPORTANT: σ(t) is a proxy motivated by dimensional analogy with thermodynamic "
     "entropy production — it is NOT a formally derived entropy production rate from "
     "a statistical model of the return-generating process. The formal connection "
     "requires computing the true Fisher Information on the return distribution and "
     "deriving the Onsager-type dissipation from it. This has not been done."),

    (1, "Mathematical Definition",
     "Instantaneous dissipation rate:\n"
     "  σ(t) = v(t)² / D_eff(t)\n\n"
     "where:\n"
     "  v(t) = dD_eff/dt  — velocity of participation ratio (numerical derivative)\n"
     "  D_eff(t) = N² / Σᵢ λᵢ(t)²  — participation ratio of EWMA correlation matrix\n"
     "  λᵢ(t) = eigenvalues of the EWMA correlation matrix (λ_decay = 0.984)\n"
     "  N = number of assets in the universe\n\n"
     "Total dissipation per crisis episode:\n"
     "  Σ = ∫_{t_onset}^{t_trough} σ(t) dt\n\n"
     "Properties of the proxy:\n"
     "  σ(t) ≥ 0  always  (v² ≥ 0, D_eff > 0)\n"
     "  σ(t) → 0  when v → 0  (quasi-static / near-trough)\n"
     "  σ large  when v large and D_eff small  (fast collapse at the floor)\n"
     "  σ large  when v large and D_eff large  (fast collapse from high diversity)\n\n"
     "Physical motivation (by analogy with Onsager irreversible thermodynamics):\n"
     "  In a fluid: σ = η |∇v|² / T  (viscosity × velocity gradient² / temperature)\n"
     "  Financial analog: D_eff plays the role of T (diversity = market temperature),\n"
     "  |v| = |dD_eff/dt| plays the role of |∇v| (gradient driving dissipation).\n"
     "  When D_eff is low (crisis floor), small velocity still produces high σ — the\n"
     "  system is fighting against the structural coherence floor.\n\n"
     "PROXY LIMITATION: v(t) is a numerical derivative of a noisy proxy (D_eff).\n"
     "Smoothing window and derivative method affect σ(t) values. Results are\n"
     "qualitatively robust to smoothing choices but quantitative values are\n"
     "proxy-dependent."),

    (2, "Three Crisis Archetypes",
     "k-means clustering (k=3) on normalized phase-space trajectories in the\n"
     "(D_eff, velocity) plane identifies three empirically distinct crisis shapes:\n\n"
     "CLUSTER 0 — Shallow Grind\n"
     "  Profile: Low |v|, long duration, shallow D_eff trough\n"
     "  σ(t) profile: Low peak σ, sustained non-zero σ over extended episode\n"
     "  Total Σ: Moderate-to-high (long duration compensates low rate)\n"
     "  Thermodynamic analog: Near quasi-static — slow, partially reversible process\n"
     "  Example: Minor corrections, sector rotations without full crisis\n\n"
     "CLUSTER 1 — Deep V-Shape\n"
     "  Profile: High |v|, short duration, deep D_eff trough\n"
     "  σ(t) profile: High peak σ (spike at maximum velocity), brief episode\n"
     "  Total Σ: Moderate (high rate, short duration)\n"
     "  Thermodynamic analog: Abrupt/irreversible — maximum instantaneous dissipation\n"
     "  Example: COVID March 2020 (fast crash, fast recovery)\n\n"
     "CLUSTER 2 — Deep Slow Grind\n"
     "  Profile: Moderate |v|, long duration, deep D_eff trough\n"
     "  σ(t) profile: Moderate peak σ, sustained over extended episode\n"
     "  Total Σ: High (deepest total irreversibility)\n"
     "  Thermodynamic analog: Sustained non-equilibrium — maximum total entropy produced\n"
     "  Example: GFC 2008–2009 (slow dimensional collapse over months)\n\n"
     "The three archetypes partition the (peak σ, total Σ) space:\n"
     "  Cluster 0: low peak σ, moderate Σ  (quasi-static)\n"
     "  Cluster 1: high peak σ, moderate Σ  (abrupt)\n"
     "  Cluster 2: moderate peak σ, high Σ  (sustained)\n\n"
     "STATUS: Archetypes identified from normalized phase-space chart.\n"
     "Formal k-means clustering with statistical validation is pending."),

    (3, "Thermodynamic Connections",
     "The financial σ(t) proxy is motivated by analogy with three formal entropy\n"
     "production frameworks in the DS Wiki:\n\n"
     "GT07 (Chirco Non-Equilibrium Spacetime Thermodynamics):\n"
     "  The gravitational entropy production rate σ (Chirco-Liberati) is the\n"
     "  non-equilibrium correction to Jacobson's Clausius relation δQ = TdS.\n"
     "  Financial analog: σ(t) is the non-equilibrium correction to the\n"
     "  'equilibrium' state (D_eff constant, quasi-static market). Both σ_grav\n"
     "  and σ_fin are zero at equilibrium and positive for irreversible processes.\n"
     "  ANALOGY ONLY — the gravitational σ derives from the Raychaudhuri equation\n"
     "  and null congruence shear; the financial σ is a dimensional proxy.\n\n"
     "IT06 (Seifert Stochastic Thermodynamics):\n"
     "  ⟨s_tot⟩ = D_KL(P_forward || P_reverse) is Seifert's trajectory entropy\n"
     "  production — the KL divergence between forward and reverse processes.\n"
     "  Financial analog: Σ = ∫σ dt approximates the total entropy produced in\n"
     "  the market regime transition. If the return-generating process were fully\n"
     "  specified, the true analog of ⟨s_tot⟩ would be\n"
     "  D_KL(P_crisis_path || P_reverse_path). The proxy σ(t) = v²/D_eff is an\n"
     "  approximation that captures the qualitative behavior without requiring\n"
     "  the full distributional specification.\n\n"
     "HB09 (Generalised Second Law):\n"
     "  dS_total/dt ≥ 0 integrated over a black hole process gives the total\n"
     "  entropy increase. Σ = ∫σ dt ≥ 0 integrated over a crisis episode is the\n"
     "  financial analog — total irreversibility is always non-negative.\n\n"
     "RECOVERY ASYMMETRY (empirical):\n"
     "  Crisis onset (normal→crisis): σ(t) rises rapidly, peaks, falls at trough.\n"
     "  Recovery (crisis→normal): σ(t) remains low throughout — recoveries are\n"
     "  near-quasi-static in this measure. This asymmetry between collapse and\n"
     "  recovery is the financial market signature of thermodynamic irreversibility:\n"
     "  the forward path (crisis) differs from the reverse path (recovery), consistent\n"
     "  with IT06's P_forward ≠ P_reverse and GT07's σ > 0 for irreversible processes."),

    (4, "Geodesic Test",
     "The geodesic test is the primary falsifiable prediction connecting X8 to P21\n"
     "(Fisher-Rao Metric Universality).\n\n"
     "HYPOTHESIS: If crisis trajectories in the (D_eff, velocity) phase space follow\n"
     "minimum-dissipation paths, they should trace Fisher-Rao geodesics on the\n"
     "statistical manifold of market states. This would be the financial market\n"
     "instance of Seifert's minimum-dissipation result (IT06): optimal non-equilibrium\n"
     "processes are geodesics on the Fisher-Rao manifold.\n\n"
     "TEST DESIGN:\n"
     "  1. For each historical crisis episode, compute:\n"
     "     - Σ_actual = ∫σ(t) dt  (observed total dissipation)\n"
     "     - d_geodesic(start, end)  (Fisher-Rao geodesic distance between start\n"
     "       and end states, using the correlation matrix as a proxy for the\n"
     "       statistical manifold)\n"
     "  2. Compare Σ_actual to the minimum possible dissipation d_geodesic²/τ\n"
     "     (Seifert's bound: ⟨W_diss⟩ ≥ d_geodesic²/τ)\n"
     "  3. If Σ_actual ≈ d_geodesic²/τ across crisis types: evidence for\n"
     "     minimum-dissipation (near-geodesic) trajectories\n"
     "     If Σ_actual >> d_geodesic²/τ: transitions are 'wasteful' — they take\n"
     "     longer paths through state space than necessary\n\n"
     "PROXY LIMITATION: The Fisher-Rao geodesic distance here would be computed\n"
     "using the correlation matrix as a proxy for the true statistical manifold —\n"
     "not the formal Fisher-Rao metric on the return-generating distribution.\n"
     "The test therefore provides evidence about the proxy manifold, not the\n"
     "true manifold.\n\n"
     "STATUS: Trajectory data exists in AlphaEntropy (normalized phase-space\n"
     "chart, crisis overlays). Path integral computation has not been done.\n"
     "This is the highest-priority quantitative test connecting X8 to P21."),

    (5, "DS Connections",
     "| Link | Target | Relationship |\n"
     "|------|--------|--------------|\n"
     "| Primary analog | GT07 (Chirco Non-Equilibrium Spacetime Thermodynamics) | "
     "σ(t) is the financial proxy for gravitational entropy production σ |\n"
     "| Primary analog | IT06 (Seifert Stochastic Thermodynamics) | "
     "Σ = ∫σ dt approximates D_KL(P_forward||P_reverse) trajectory entropy production |\n"
     "| Foundation | X0 (Three FIM Regime States) | "
     "σ(t) is computed from phase-space trajectories in the X0 state space |\n"
     "| Foundation | P5 (Fisher Information Rank = D_eff) | "
     "D_eff in σ(t) is the participation ratio proxy for FIM rank |\n"
     "| Monotonicity | HB09 (Generalised Second Law) | "
     "Σ ≥ 0 always — financial analog of dS_total/dt ≥ 0 |\n"
     "| Geodesic test | P21 (Fisher-Rao Universality) | "
     "If crisis paths minimize Σ, they are Fisher-Rao geodesics — key test for P21 |\n"
     "| Non-ergodicity | P19 (Non-Ergodicity of Regime Detection) | "
     "σ(t) measures why non-ergodic transitions look different in different eras |\n"
     "| Coherence floor | P18 (Structural Coherence Floor) | "
     "σ → ∞ as D_eff → 0 — the floor prevents catastrophic dissipation |\n"),

    (6, "Mathematical Archetype",
     "Mathematical archetype: conservation-law\n\n"
     "σ(t) = v(t)²/D_eff(t) ≥ 0 is a non-negative dissipation rate by construction. "
     "Its integral Σ = ∫σ dt is monotonically increasing throughout any crisis episode "
     "— a total irreversibility measure that can only accumulate, never decrease. "
     "This monotonicity is the financial market instance of the entropy production "
     "monotonicity in GT07 (σ_grav ≥ 0) and IT06 (⟨s_tot⟩ = D_KL ≥ 0). "
     "All three are instances of the same mathematical structure: a non-negative "
     "scalar that measures deviation from a reversible (quasi-static) path, "
     "integrates to give total irreversibility, and is zero only for perfectly "
     "reversible processes (which do not occur in finite time in any of the three domains)."),

    (7, "Concept Tags",
     "• financial entropy production\n"
     "• market dissipation rate\n"
     "• phase-space trajectories\n"
     "• crisis archetypes\n"
     "• D_eff velocity\n"
     "• quasi-static market transition\n"
     "• irreversible collapse\n"
     "• non-equilibrium finance\n"
     "• regime transition dynamics\n"
     "• Chirco analog in finance\n"
     "• thermodynamic cost of crisis\n"
     "• geodesic test\n"
     "• Onsager dissipation\n"
     "• participation ratio velocity\n"
     "• total dissipation per episode"),
]

LINKS = [
    ("X8", "GT07", "analogous to", "2",
     "σ(t)=v²/D_eff is the financial proxy for Chirco's gravitational entropy "
     "production rate; both are non-negative dissipation measures for irreversible "
     "non-equilibrium processes"),
    ("X8", "IT06", "analogous to", "2",
     "Σ=∫σ dt approximates Seifert's D_KL(P_forward||P_reverse) trajectory entropy "
     "production; both measure the total irreversibility of a stochastic transition"),
    ("X8", "X0_FIM_Regimes", "derives from", "1.5",
     "σ(t) is computed from the D_eff time series that defines the X0 phase space; "
     "the three crisis archetypes correspond to different X0 state trajectories"),
    ("X8", "HB09", "analogous to", "2",
     "Σ=∫σ dt ≥ 0 is the financial analog of the GSL dS_total/dt ≥ 0 integrated "
     "over an episode; both are total irreversibility bounds"),
    ("X8", "P21_conjecture", "tests", "1.5",
     "The geodesic test (Σ_actual vs d_geodesic²/τ) is the primary falsifiable "
     "prediction connecting X8 financial trajectories to P21 Fisher-Rao universality"),
]


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if cur.execute("SELECT id FROM entries WHERE id = 'X8'").fetchone():
        print("X8 already exists — skipping.")
        conn.close()
        return

    cur.execute(
        """INSERT INTO entries
           (id, title, filename, entry_type, scale, domain, status, confidence,
            type_group, authoring_status, formality_tier)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (ENTRY["id"], ENTRY["title"], ENTRY["filename"], ENTRY["entry_type"],
         ENTRY["scale"], ENTRY["domain"], ENTRY["status"], ENTRY["confidence"],
         ENTRY["type_group"], ENTRY["authoring_status"], ENTRY["formality_tier"])
    )
    print(f"  Inserted entry: X8 — {ENTRY['title']}")

    for order, name, content in SECTIONS:
        cur.execute(
            "INSERT INTO sections (entry_id, section_name, section_order, content) "
            "VALUES (?, ?, ?, ?)",
            ("X8", name, order, content)
        )
        print(f"    Section [{order}]: {name} ({len(content)} chars)")

    labels = {r[0]: r[1] for r in cur.execute("SELECT id, title FROM entries")}

    print()
    for src, tgt, lt, tier, desc in LINKS:
        tgt_label = labels.get(tgt, tgt)
        try:
            cur.execute(
                "INSERT OR IGNORE INTO links "
                "(link_type, source_id, source_label, target_id, target_label, "
                "description, link_order, confidence_tier) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (lt, src, ENTRY["title"], tgt, tgt_label, desc, 0, tier)
            )
            print(f"  Link: X8 → {tgt} ({lt}, tier {tier})")
        except Exception as e:
            print(f"  WARN: {e}")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Inserting X8 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)

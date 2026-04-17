"""
Update P21 and X8 with Test 2 results (Archetype Validation → τ_relax Scaling Law).

Key findings:
  1. k=3 archetype model FALSIFIED. k=2 wins (silhouette 0.575) but is just
     "normal" vs "extreme outliers" (n=2) — not a useful taxonomy.
  2. The real structure is CONTINUOUS: η_down = f(log(duration/τ_relax)), r = -0.896
  3. τ_relax = 43 trading days (EWMA halflife) naturally separates:
     - Adiabatic regime (dur/τ < 0.5, η = 0.429)
     - Transition zone (dur/τ = 0.5–1.5, η = 0.175)
     - Isothermal regime (dur/τ > 1.5, η = 0.132)
  4. CRITICAL INSIGHT: The geodesic/non-geodesic distinction is a property of
     the observation timescale relative to the crisis timescale, not a property
     of the market itself. The same crisis with different EWMA λ would give
     different η. This is an observer-dependent coarse-graining effect.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB


def run(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ------------------------------------------------------------------
    # P21 — Replace the crude "fast-shock limit" with the scaling law
    # ------------------------------------------------------------------
    print("=== P21 ===")

    # Append to phase1_results
    p21_phase1 = cur.execute(
        "SELECT phase1_results FROM conjectures WHERE id='P21'"
    ).fetchone()[0]

    p21_phase1_addendum = (
        "\n\n"
        "τ_RELAX SCALING LAW (AlphaEntropy Test 2, 2026-03-30):\n"
        "The three-archetype model (Shallow Grind / Deep V-Shape / Deep Slow Grind) "
        "was FALSIFIED by k-means clustering. k=2 wins (silhouette 0.575) but the "
        "two clusters are just 'normal episodes' (n=19) vs 'extreme dissipation "
        "outliers' (n=2) — not a useful taxonomy.\n\n"
        "The real structure is continuous:\n"
        "  η_down = f(log(duration / τ_relax))    r = −0.896\n\n"
        "where τ_relax = 43 trading days (EWMA halflife at λ = 0.984).\n\n"
        "Three regimes emerge from the continuous curve:\n"
        "  Adiabatic  (dur/τ < 0.5):   mean η = 0.429, n=10\n"
        "  Transition  (dur/τ 0.5–1.5): mean η = 0.175, n=5\n"
        "  Isothermal  (dur/τ > 1.5):   mean η = 0.132, n=6\n\n"
        "CRITICAL INSIGHT: The geodesic/non-geodesic distinction is NOT a property "
        "of the market. It is a property of the observation timescale relative to "
        "the crisis timescale. The same crisis observed with different EWMA λ values "
        "would give different η. When the crisis unfolds faster than the correlation "
        "estimator's memory (dur < τ), the trajectory appears near-geodesic because "
        "the estimator cannot partially relax between moves. When the crisis unfolds "
        "slower (dur > τ), the estimator relaxes between moves and the trajectory "
        "meanders. This is an observer-dependent coarse-graining effect — the "
        "thermodynamic analog is exact: the adiabatic/isothermal distinction depends "
        "on the ratio of process timescale to thermal relaxation time.\n\n"
        "The 43-day timescale was chosen for signal processing quality, not "
        "thermodynamic reasons. The fact that it naturally separates geodesic from "
        "non-geodesic behavior is suggestive: the optimal signal processing timescale "
        "may coincide with the information-geometric relaxation time of the "
        "correlation manifold. This connection is unexplored."
    )

    cur.execute("UPDATE conjectures SET phase1_results = ? WHERE id = 'P21'",
                (p21_phase1 + p21_phase1_addendum,))
    print(f"  Updated P21.phase1_results (+{len(p21_phase1_addendum)} chars)")

    # Update claim — refine the conditional from "fast-shock limit" to "τ_crisis < τ_observation"
    p21_claim = cur.execute(
        "SELECT claim FROM conjectures WHERE id='P21'"
    ).fetchone()[0]

    # Replace the crude "fast-shock limit" framing
    old_refined = (
        "REFINED SCOPE: P21 universality holds across the four formal domains "
        "(thermodynamics, RG flow, gravity, information theory) where the "
        "Fisher-Rao metric appears by Chentsov uniqueness. In financial "
        "markets — where D_eff is a participation ratio proxy, not a true "
        "FIM — the geodesic prediction holds only for acute shock events. "
        "This is not an ad hoc rescue: the fast-shock condition is independently "
        "testable and physically motivated."
    )

    new_refined = (
        "REFINED SCOPE: P21 universality holds across the four formal domains "
        "(thermodynamics, RG flow, gravity, information theory) where the "
        "Fisher-Rao metric appears by Chentsov uniqueness. In financial "
        "markets — where D_eff is a participation ratio proxy, not a true "
        "FIM — geodesic efficiency η scales continuously with "
        "log(duration / τ_relax), where τ_relax = 43 days is the EWMA halflife "
        "(r = −0.896). The condition for P21 to hold is τ_crisis < τ_observation, "
        "not a categorical 'fast shock.' This is physically exact: the "
        "adiabatic/isothermal distinction in thermodynamics depends on the same "
        "ratio of process timescale to thermal relaxation time. The observer's "
        "coarse-graining timescale determines what appears geodesic — the same "
        "crisis observed with different EWMA λ would give different η. This is "
        "not an artifact to be corrected; it is the correct information-geometric "
        "statement: geodesic efficiency is relative to the measurement resolution, "
        "just as effective dimensionality is relative to the coarse-graining scale "
        "(P7)."
    )

    if old_refined in p21_claim:
        p21_claim_new = p21_claim.replace(old_refined, new_refined)
        cur.execute("UPDATE conjectures SET claim = ? WHERE id = 'P21'",
                    (p21_claim_new,))
        print(f"  Updated P21.claim — replaced fast-shock framing with τ scaling law")
    else:
        print("  SKIP P21.claim — old fragment not found")

    # Update critical_gaps — the τ_relax prediction from gap 4 is now CONFIRMED
    p21_gaps = cur.execute(
        "SELECT critical_gaps FROM conjectures WHERE id='P21'"
    ).fetchone()[0]

    p21_gaps_addendum = (
        "\n5. τ_RELAX PREDICTION CONFIRMED (2026-03-30): The prediction from gap 4 "
        "that η should transition at τ/τ_relax ≈ 1 is confirmed: the continuous "
        "scaling law η = f(log(dur/τ)) has its inflection in the transition zone "
        "dur/τ = 0.5–1.5. The 43-day EWMA halflife was estimated a priori and "
        "matches the empirical boundary. REMAINING GAP: Why does the optimal signal "
        "processing timescale (chosen for Sharpe ratio maximization) coincide with "
        "the information-geometric relaxation time? Is this a coincidence, or does "
        "optimal filtering inherently select the Fisher-Rao relaxation scale? This "
        "is a testable question: vary λ systematically and check whether the λ that "
        "maximizes trading performance also maximizes the r² of the η(dur/τ) "
        "scaling law."
    )

    cur.execute("UPDATE conjectures SET critical_gaps = ? WHERE id = 'P21'",
                (p21_gaps + p21_gaps_addendum,))
    print(f"  Updated P21.critical_gaps — τ_relax confirmed, new gap defined")

    # ------------------------------------------------------------------
    # X8 — Kill the three-archetype model, replace with scaling law
    # ------------------------------------------------------------------
    print("\n=== X8 ===")

    # Replace "Three Crisis Archetypes" section content
    row = cur.execute(
        "SELECT content FROM sections WHERE entry_id='X8' "
        "AND section_name='Three Crisis Archetypes'"
    ).fetchone()

    new_archetypes_content = (
        "ARCHETYPE MODEL FALSIFIED (Test 2, 2026-03-30):\n\n"
        "The three-archetype model (Shallow Grind / Deep V-Shape / Deep Slow Grind) "
        "was tested via k-means clustering on per-episode feature vectors "
        "[peak σ, total Σ, duration, trough D_eff, peak |v|, mean σ, η_down].\n\n"
        "Results:\n"
        "  k=2: silhouette 0.575 (winner)\n"
        "  k=3: silhouette < k=2\n"
        "  k=4, k=5: worse\n\n"
        "The k=2 clusters are 'normal episodes' (n=19) vs 'extreme dissipation "
        "outliers' (n=2: 2007-03 and 2025 Stress). This is not a useful taxonomy — "
        "it's an outlier detection, not a structural classification.\n\n"
        "The real structure is CONTINUOUS, not categorical.\n\n"
        "---\n\n"
        "## τ_relax Scaling Law (replaces archetype model)\n\n"
        "Geodesic efficiency η scales continuously with the ratio of crisis "
        "duration to the EWMA correlation estimator's halflife:\n\n"
        "  η_down = f(log(duration / τ_relax))    r = −0.896\n"
        "  τ_relax = 43 trading days (EWMA halflife at λ = 0.984)\n\n"
        "Three regimes emerge as ranges on the continuous curve, not as "
        "discrete clusters:\n\n"
        "  Regime       | dur/τ    | Mean η  | n  | Physical analog\n"
        "  -------------+----------+---------+----+-----------------------------\n"
        "  Adiabatic    | < 0.5    | 0.429   | 10 | Fast shock, near-geodesic\n"
        "  Transition   | 0.5–1.5  | 0.175   |  5 | Inflection zone\n"
        "  Isothermal   | > 1.5    | 0.132   |  6 | Slow grind, far from geodesic\n\n"
        "INTERPRETATION: When a crisis unfolds faster than the correlation "
        "estimator's memory (dur < τ_relax), the estimator cannot partially "
        "relax between moves. The trajectory on the correlation manifold appears "
        "near-geodesic because there is no time for intermediate equilibration — "
        "correlations snap directly from one structure to another. When the crisis "
        "unfolds slower (dur > τ_relax), the estimator has time to partially relax "
        "between moves, producing a meandering trajectory with partial reversals "
        "and excess path length.\n\n"
        "OBSERVER DEPENDENCE: The geodesic/non-geodesic distinction is NOT a "
        "property of the market. It is a property of the observation timescale "
        "relative to the crisis timescale. The same crisis observed with different "
        "EWMA λ values (different τ_relax) would give different η. Increasing λ "
        "(longer memory → larger τ_relax) would make more crises appear adiabatic. "
        "Decreasing λ (shorter memory → smaller τ_relax) would make more crises "
        "appear isothermal.\n\n"
        "This is the correct information-geometric statement: geodesic efficiency "
        "is relative to the measurement resolution, just as effective dimensionality "
        "is relative to the coarse-graining scale (P7). The thermodynamic analog "
        "is exact: whether a process appears adiabatic or isothermal depends on "
        "the ratio of the process timescale to the thermal relaxation time of "
        "the measuring apparatus.\n\n"
        "OPEN QUESTION: Why does the EWMA halflife (chosen for signal processing "
        "quality — Sharpe ratio optimization) coincide with the information-geometric "
        "relaxation time that naturally separates adiabatic from isothermal regimes? "
        "Is optimal filtering inherently selecting the Fisher-Rao relaxation scale?"
    )

    cur.execute(
        "UPDATE sections SET content = ? WHERE entry_id='X8' "
        "AND section_name='Three Crisis Archetypes'",
        (new_archetypes_content,)
    )
    print("  Updated X8/'Three Crisis Archetypes' — replaced with τ_relax scaling law")

    # Also update Concept Tags to reflect the new framing
    row = cur.execute(
        "SELECT content FROM sections WHERE entry_id='X8' AND section_name='Concept Tags'"
    ).fetchone()

    new_tags = (
        "• financial entropy production\n"
        "• market dissipation rate\n"
        "• phase-space trajectories\n"
        "• τ_relax scaling law\n"
        "• adiabatic vs isothermal regimes\n"
        "• observer-dependent coarse-graining\n"
        "• D_eff velocity\n"
        "• quasi-static market transition\n"
        "• irreversible collapse\n"
        "• non-equilibrium finance\n"
        "• regime transition dynamics\n"
        "• geodesic efficiency η\n"
        "• EWMA halflife as relaxation time\n"
        "• thermodynamic cost of crisis\n"
        "• geodesic test\n"
        "• measurement timescale dependence\n"
        "• total dissipation per episode"
    )

    cur.execute(
        "UPDATE sections SET content = ? WHERE entry_id='X8' AND section_name='Concept Tags'",
        (new_tags,)
    )
    print("  Updated X8/Concept Tags — replaced archetype tags with scaling law tags")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Updating P21 + X8 with Test 2 results in:\n  {SOURCE_DB}\n")
    run(SOURCE_DB)

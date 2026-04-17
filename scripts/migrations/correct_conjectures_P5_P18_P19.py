"""
Corrections to P5, P18, P19 based on AlphaEntropy LLM session (2026-03-29).

P5 — Fisher Information Rank Equals D_eff
  CORRECTION: The financial market D_eff is the participation ratio of EWMA
  correlation matrix eigenvalues (N²/Σλᵢ²), NOT a true Fisher Information
  Matrix. The FIM conjecture (formal) and the participation ratio proxy
  (operational) are related but distinct. Must not conflate them.

P18 — Structural Coherence Floor in Regulated Systems
  CORRECTION 1: "FIM score ≥ 0.59" refers to the PCI-engine coherence proxy
  (2017–2025 window). The participation ratio D_eff has troughs of ~0.22
  (GFC), ~0.22 (COVID), ~0.20 (Rate Shock), ~0.185 (2025 current) — a
  different metric, not the same floor.
  CORRECTION 2: The trough tranche is drifting lower (0.22 → 0.185). The
  hard floor claim needs softening.
  CORRECTION 3: Approach to floor is smooth asymptotic, not discontinuous.
  Trough signature = acceleration crosses zero.

P19 — Non-Ergodicity of Regime Detection in Tier 3 Domains
  CORRECTION: The mechanism is now identified — secular drift in the D_eff
  distribution (r=+0.32 with SPY price level, r=−0.40 with VIX), not just
  sampling non-ergodicity. Fixed thresholds classified 86% of 2007–2009 as
  CRISIS vs 4% of 2017–2019 at the same absolute D_eff levels.
  NEW: Fix validated — adaptive 3yr rolling percentile thresholds improved
  Calmar 0.532 → 0.538. The rolling 1-yr correlation between D_eff and SPY
  swings −0.2 to +0.84, confirming the relationship is non-stationary.
  UPDATE: three_state upgraded from "All States" to "State 2" (mechanism
  found, partial fix validated).
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB


def update_field(cur, pid, field, new_value):
    cur.execute(f"UPDATE conjectures SET {field} = ? WHERE id = ?", (new_value, pid))
    print(f"  Updated {pid}.{field} ({len(new_value)} chars)")


def run(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ------------------------------------------------------------------
    # P5 — add proxy-distinction note to claim and update phase1_results
    # ------------------------------------------------------------------
    print("=== P5 ===")

    p5_claim_new = (
        r"The effective dimensionality of a physical system is operationally defined as the "
        r"rank of its Fisher Information Matrix at a given resolution scale: "
        r"$D_{\text{eff}}(\ell) = \text{rank}(\mathcal{F}_\ell)$. "
        r"\n\n"
        r"**OPERATIONAL PROXY DISTINCTION (added 2026-03-29):** In financial market "
        r"applications, $D_{\text{eff}}$ is approximated by the *participation ratio* of "
        r"EWMA correlation matrix eigenvalues: "
        r"$D_{\text{eff}} = N^2 / \sum_i \lambda_i^2$, where $\lambda_i$ are the "
        r"eigenvalues of the rolling correlation matrix. "
        r"This is **not** a true Fisher Information Matrix — it requires no parametric "
        r"statistical model of the return-generating process and is not computed on the "
        r"manifold of probability distributions. "
        r"The participation ratio measures how many eigenvalues are active (how many "
        r"independent return dimensions are live), which is conceptually related to "
        r"$D_{\text{eff}}$ but operationally distinct: (1) the participation ratio is "
        r"not DPI-compatible (it can increase under coarse-graining, unlike FIM rank); "
        r"(2) it does not require a likelihood function or statistical model; "
        r"(3) it has not been formally derived as a limiting case of the FIM rank. "
        r"A proper FIM for financial returns would require a parameterised model of the "
        r"joint return-generating distribution, with the metric computed as the Hessian "
        r"of the log-likelihood. This has not been computed. "
        r"The conjecture (FIM rank = $D_{\text{eff}}$) remains formally valid for "
        r"systems with explicit statistical models (Ising, geometric graphs); its "
        r"extension to financial markets via the participation ratio proxy is an "
        r"approximation whose formal justification is an open gap."
    )

    p5_phase1_new = (
        "Gap-based Fisher rank returns exact integer dimension on flat tori in d = 2, 3, 4 "
        "with zero variance across all sample vertices. On Erdős–Rényi graphs (no geometry), "
        "rank = 1 everywhere. On random geometric graphs, rank = d + 1, detecting d spatial "
        "directions plus one local-disorder direction. Threshold sensitivity resolved via "
        "gap-based detection (Gavish & Donoho, 2014). The operational definition converges "
        "with known dimensionality on all tested geometric benchmarks. "
        "CRITICAL DISTINCTION: Rank is DPI-compatible (non-increasing under coarse-graining); "
        "participation ratio is not. For fractal systems: rank returns mixed integers (not d_H), "
        "but participation ratio converges to d_H within 0.6–4.7%.\n\n"
        "FINANCIAL MARKET PROXY (AlphaEntropy, 2003–2025): The financial D_eff is the "
        "participation ratio of the EWMA correlation matrix (λ=0.984): "
        "D_eff = N²/Σλᵢ² where λᵢ are correlation matrix eigenvalues. "
        "This is NOT a true FIM — no parametric return-generating model is used. "
        "Crisis troughs (participation ratio): GFC ~0.22, COVID ~0.22, Rate Shock ~0.20, "
        "2025 current ~0.185. These values are distinct from the PCI-engine coherence scores "
        "(0.594–0.974) which are a separate proxy. "
        "Regime classification using adaptive 3yr rolling percentile thresholds (V28.3) "
        "outperforms fixed thresholds — the underlying D_eff distribution has secular drift "
        "(r=+0.32 with SPY price level, r=−0.40 with VIX), consistent with P19.\n\n"
        "FORMAL GAP: A proof that participation ratio → FIM rank in the limit of large N "
        "and i.i.d. returns, or a construction of the full FIM for the return-generating "
        "process, remains outstanding. Until this is closed, the financial market results "
        "support P5 as an analogy, not a formal instantiation."
    )

    p5_gaps_current = cur.execute(
        "SELECT critical_gaps FROM conjectures WHERE id='P5'"
    ).fetchone()[0]
    p5_gaps_new = p5_gaps_current.rstrip() + (
        "\n4. PROXY FORMALIZATION GAP (added 2026-03-29): The financial market D_eff "
        "(participation ratio of EWMA correlation matrix eigenvalues) has not been formally "
        "derived as a limiting case of FIM rank. The participation ratio is not DPI-compatible, "
        "lacks a parametric statistical model, and is computed on a correlation matrix rather "
        "than the statistical manifold of probability distributions. Closing this gap requires "
        "either (a) deriving the participation ratio as an FIM rank approximation under "
        "specific return-generating assumptions, or (b) computing the full FIM on a "
        "parametric model and verifying convergence with the participation ratio proxy."
    )

    update_field(cur, "P5", "claim", p5_claim_new)
    update_field(cur, "P5", "phase1_results", p5_phase1_new)
    update_field(cur, "P5", "critical_gaps", p5_gaps_new)

    # ------------------------------------------------------------------
    # P18 — soften floor claim, add trough sequence, smooth approach
    # ------------------------------------------------------------------
    print("\n=== P18 ===")

    p18_claim_new = (
        "Regulated market systems have not empirically reached the FRAGMENTED regime "
        "(coherence < 0.40) under normal crisis conditions (markets open, no exchange "
        "closure). This holds across all tested crises in US equities 2003–2025. "
        "The structural interpretation is that circuit breakers, regulatory oversight, "
        "and distributed participation impose a lower bound on information-geometric "
        "coherence independent of stress level.\n\n"
        "METRIC DISTINCTION (revised 2026-03-29): Two proxies are tracked, with "
        "different observed floors:\n"
        "— PCI-engine coherence score (2017–2025 backtest window): minimum observed "
        "0.594 (2022 bear), maximum 0.974. Floor claim: ≥ 0.59 within this window.\n"
        "— Participation ratio D_eff (EWMA correlation matrix, 2003–2025): troughs at "
        "GFC ~0.22, COVID ~0.22, Rate Shock ~0.20, 2025 ~0.185. These are well below "
        "the PCI floor — the two metrics have different scales and different floor levels.\n\n"
        "The strong form of the claim ('FIM score ≥ 0.59') applies only to the PCI "
        "coherence proxy on the 2017–2025 window. The weak form ('FRAGMENTED regime "
        "never reached') has held across the full 2003–2025 history in both proxies. "
        "The participation ratio D_eff trough sequence is drifting lower (0.22 → 0.185) "
        "— if this trend continues, the hard FRAGMENTED boundary (<0.40) remains "
        "unbreached, but the floor is not static."
    )

    p18_phase1_new = (
        "AlphaEntropy backtests (2003–2025, US equities):\n\n"
        "PCI-engine coherence scores (2017–2025 only): range 0.594–0.974. "
        "COVID March 2020: 0.615. 2022 H2 bear: 0.594. Normal range: 0.70–0.90. "
        "Never reached FRAGMENTED (<0.40) in this window.\n\n"
        "Participation ratio D_eff (2003–2025, EWMA λ=0.984 correlation matrix):\n"
        "  GFC trough: ~0.22\n"
        "  COVID trough: ~0.22\n"
        "  Rate Shock trough: ~0.20\n"
        "  2025 current trough: ~0.185 (ongoing as of session date)\n"
        "Trough sequence is drifting lower across episodes.\n\n"
        "TROUGH STRUCTURE (smooth asymptotic, not discontinuous): "
        "The approach to each trough follows a consistent 5-phase pattern: "
        "(1) velocity goes negative (D_eff falling); "
        "(2) velocity accelerates — descent gets faster; "
        "(3) acceleration flips positive (velocity still negative but decelerating); "
        "(4) velocity approaches zero at the floor; "
        "(5) slow asymmetric recovery begins. "
        "Trough signature = acceleration crosses zero (smooth inflection). "
        "In the 2025 episode, acceleration flipped positive 6 days after trough. "
        "COVID was similar. This is asymptotic approach, not a sudden stop.\n\n"
        "RECOVERY ASYMMETRY: Crisis→recovery paths are systematically longer and "
        "slower than normal→crisis paths. Recovery often has false starts. "
        "This asymmetry is consistent with irreversible entropy production (GT07): "
        "the path from normal→crisis differs from crisis→normal."
    )

    p18_gaps_current = cur.execute(
        "SELECT critical_gaps FROM conjectures WHERE id='P18'"
    ).fetchone()[0]
    p18_gaps_new = (
        "1. Only validated on US equities (S&P 500 proxy) 2003–2025. "
        "Needs replication on other regulated systems (non-US markets, power grids, "
        "telecommunications). This remains the single most critical gap.\n"
        "2. METRIC DISAMBIGUATION GAP (added 2026-03-29): Two proxies (PCI coherence "
        "score and participation ratio D_eff) have different scales and different "
        "observed floors. The claim needs to specify which metric and window it applies "
        "to. The PCI floor (≥ 0.59) is a 2017–2025 window artifact; the participation "
        "ratio floor is lower (~0.18) and trending lower across successive crises.\n"
        "3. The formal FIM on the full pricing surface has not been computed — both "
        "metrics are proxies.\n"
        "4. Exchange closure events (market halts) not tested.\n"
        "5. DRIFT GAP: The participation ratio D_eff trough sequence is declining "
        "(0.22 → 0.185). If this represents a structural drift rather than noise, "
        "the floor itself is not static — it may be a slowly eroding bound rather "
        "than a hard regulatory constraint."
    )

    update_field(cur, "P18", "claim", p18_claim_new)
    update_field(cur, "P18", "phase1_results", p18_phase1_new)
    update_field(cur, "P18", "critical_gaps", p18_gaps_new)

    # ------------------------------------------------------------------
    # P19 — update mechanism, add fix, update three_state
    # ------------------------------------------------------------------
    print("\n=== P19 ===")

    p19_claim_new = (
        "In Tier 3 domains (economics, ecology, social systems), D_eff-based regime "
        "signals are non-ergodic: time-averages over short windows do not converge to "
        "stable ensemble averages because the underlying D_eff distribution has "
        "secular drift. The non-ergodicity is not purely a sampling artifact — the "
        "relationship between D_eff and market conditions is itself non-stationary.\n\n"
        "MECHANISM (identified 2026-03-29): D_eff (participation ratio) drifts "
        "secularly with market structure: r = +0.32 with SPY price level, r = −0.40 "
        "with VIX. Fixed thresholds (e.g. 0.29 = CRISIS, 0.40 = NORMAL) classified "
        "86% of 2007–2009 observations as CRISIS but only 4% of 2017–2019 at the same "
        "absolute D_eff levels — the same number meant different things in different "
        "structural regimes. The rolling 1-year correlation between D_eff and SPY "
        "swings from −0.20 to +0.84 across different years, confirming that the "
        "relationship is non-stationary, not merely noisy.\n\n"
        "FIX (validated 2026-03-29): Adaptive 3yr rolling percentile thresholds — "
        "asking 'is D_eff low relative to recent history?' rather than 'is D_eff "
        "below 0.29?' — is a scale-conditional normalization that corrects for the "
        "secular drift. Calmar improved from 0.532 to 0.538 under adaptive thresholds. "
        "This is a practical resolution of the non-ergodicity problem for the regime "
        "signal, though it does not resolve the deeper theoretical question of why "
        "Tier 3 systems exhibit this drift.\n\n"
        "NOTE: The original conjecture described 'sign inversion' where D_eff predicts "
        "positive returns on short windows but negative on long windows. This formal "
        "sign inversion in forward returns has NOT been found as of 2026-03-29 — the "
        "non-ergodicity manifests as threshold drift and performance degradation over "
        "longer windows, not as a literal sign change in the signal-return relationship."
    )

    p19_phase1_new = (
        "AlphaEntropy D_eff signal (participation ratio on EWMA correlation matrix):\n\n"
        "ORIGINAL FINDING: +0.013 Calmar on 5-year window (2020–2025, 2 crises, "
        "3 years recovery) vs -0.009 Calmar on 22-year window (2003–2025, 5 crises, "
        "17 years recovery). Performance degraded on the longer window.\n\n"
        "MECHANISM (session 2026-03-29): Secular drift in D_eff distribution. "
        "r(D_eff, SPY price level) = +0.32; r(D_eff, VIX) = −0.40. "
        "Fixed thresholds (0.29/0.40) classified 86% of 2007–2009 as CRISIS vs "
        "4% of 2017–2019 at the same absolute values. Rolling 1-year correlation "
        "between D_eff and SPY: range −0.20 to +0.84 (highly non-stationary).\n\n"
        "FIX VALIDATED: Adaptive 3yr rolling percentile thresholds. "
        "Calmar improvement: 0.532 → 0.538 (V28.3 live architecture). "
        "The fix is a scale-conditional normalization — equivalent to asking "
        "'is D_eff in the bottom decile of its recent distribution?' rather than "
        "'is D_eff below a fixed absolute value?'\n\n"
        "OPEN: Formal sign inversion (D_eff signal switching from positive to "
        "negative predictive relationship at different time scales) has not been "
        "explicitly tested. Ablation data exists to test this: compute Q1-Q5 D_eff "
        "quintile spread at weekly/monthly/quarterly rebalance frequencies and check "
        "for sign or magnitude changes."
    )

    update_field(cur, "P19", "claim", p19_claim_new)
    update_field(cur, "P19", "phase1_results", p19_phase1_new)
    cur.execute("UPDATE conjectures SET three_state = ? WHERE id = 'P19'",
                ("State 2",))
    print("  Updated P19.three_state → 'State 2' (mechanism found, partial fix validated)")

    conn.commit()
    conn.close()
    print("\nDone. P5, P18, P19 corrected.")


if __name__ == "__main__":
    print(f"Correcting P5, P18, P19 in:\n  {SOURCE_DB}\n")
    run(SOURCE_DB)

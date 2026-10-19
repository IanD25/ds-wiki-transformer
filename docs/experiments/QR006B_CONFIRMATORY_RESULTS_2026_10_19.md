# QR-006b Benchmark — Confirmatory Results (primary analysis)

**Date:** 2026-10-19. **Mode:** B. **Protocol:** [`QR006B_BENCHMARK_PREREGISTRATION.md`](QR006B_BENCHMARK_PREREGISTRATION.md), frozen at tag `qr006b-prereg-frozen`, with deviations D1–D2 (§11), made before any confirmatory data existed. **Predictions recorded beforehand:** [`QR006B_PREDICTIONS_2026_10_18.md`](QR006B_PREDICTIONS_2026_10_18.md) (commit `9a8ca84`). **Post-hoc audit:** [`QR006B_LEADTIME_AUDIT_2026_10_19.md`](QR006B_LEADTIME_AUDIT_2026_10_19.md).
**Numbers:** `data/reports/qr006b/controls.json` (commit `d061776`, opened first) and `results.json` (commit `89d40e0`).
**Not yet run:** the §5.7 sensitivity analyses (window 0.5, detrending, buffer 50, observation noise, Null-B) and stratum E. **Nothing promoted; no DB writes.**

---

## 0. Plain-language summary

We asked whether "information" warning signs (how predictable or complex a signal is) ever warn of a tipping point better than the standard signs: slowing down, growing wobbles, and the newer shape-of-the-distribution and fitted-model signs. We simulated 21,600 series across nine situations, half heading for a tip and half not, and scored every sign the same way.

**Answer: no, in every situation where the test could decide.** Where noise grows with the system, comes in sudden jumps, or produces flickering, and in networks of interacting species, the best information sign always fell short of the best standard sign. The best ones came close only because they are near-copies of standard signs (the Fisher index tracks variance; mutual information tracks autocorrelation).

- Where tipping is caused by a random kick, nothing could predict it, as physics says.
- Where conditions change too fast, every sign was barely better than a coin flip, and the test could not separate them: inconclusive.
- A first look at warning lead times seemed to favour some information signs. Our own audit traced most of that to a flaw in how the live version removes trends. One small lead remains (the Fisher index under flickering) and is filed as Speculative.

This is one benchmark by one group, so the result is **Supported**, not Established.

## 1. What ran

| Item | Value |
|---|---|
| Code | commit `d236f56` (`qr006b-prereg-frozen` + D1–D2 + raw-path option); manifest in `~/qr006b_runs/` |
| Seeds | `SeedSequence(20261018)`; none shared with the pilot |
| Size | 600 transition + 600 null series per model family; 18 families (C0's family (a) holds Bury's three models). 21,600 series, plus C0g's 2,400 transformed copies. Split: 200 + 200 calibration, 400 + 400 confirmation |
| Run | 2026-10-18 20:57 → 2026-10-19 01:53 (4 h 56 min, M4, 9 workers); `--variants primary,C0g` |
| Order | controls opened and committed first (`d061776`), then the test strata (`89d40e0`) |

**Decisive score (D1):** Kendall-τ trend over the first 80% of the way to the tip in the slow-ramp strata (C0, CM, S1, S2, S3, SM); the full segment in S4 and S5. AUC 0.5 is a coin flip, 1.0 is perfect.

## 2. Controls (§6.4): all pass

| Check | Result |
|---|---|
| C0, C0g, CM: no information indicator meets the YES rule | **Pass.** Best baseline: variance (C0 0.988, C0g 0.933, CM 0.986). Information indicators' Δ vs best: −0.007 (FI, C0) to −0.46 (TE, CM); all clean negatives |
| C0g exact invariances: permutation entropy and rank AC1 per-series τ | **Identical** in all four models (2,400 series) |
| C0g KSG MI drift (D2, ±0.05) | **−0.031**, within tolerance (pilot: −0.038) |
| C0g Pearson AC1 AUC ≤ C0's | **Pass** |
| CM: transfer entropy does not beat the covariance baselines | **Pass** (AUC 0.52 vs variance 0.99) |
| S4 leakage: no prediction AUC > 0.6 with CI excluding 0.5 | **Pass**; every AUC within 0.027 of 0.5 |

## 3. Test strata (§6.1–6.2)

ΔAUC is against the **best baseline**, chosen on the calibration split before the confirmation split was scored. Brackets give the pooled 95% bootstrap CI. Holm-adjusted p for every Δ test (31 tests) = 1.0.

| Stratum | Best baseline (AUC) | Best information indicator (AUC) | Every information indicator | **Label** |
|---|---|---|---|---|
| **S1** multiplicative noise | lag-1 AC (0.901) | Fisher index (0.803), Δ −0.098 [−0.119, −0.077] | clean negatives | **NO** |
| **S2** α-stable noise | robust spread, MAD (0.890) | lagged MI (0.865), Δ −0.025 [−0.044, −0.007] | clean negatives | **NO** |
| **S3** flickering / strong nonlinearity | variance (0.845) | Fisher index (0.842), Δ −0.003 [−0.018, 0.012] | clean negatives | **NO** |
| **S4** noise-induced tipping | variance (0.479) | RPDE (0.510) | four clean negatives; RPDE inconclusive (CI to 0.067) | **UNDETECTABLE** (every AUC CI includes 0.5) |
| **S5** rate-induced tipping | restoring rate (0.542) | permutation entropy (0.570), Δ +0.028 [−0.009, 0.064] | PE inconclusive; the rest clean negatives | **INCONCLUSIVE** |
| **SM** multivariate, multiplicative noise | lag-1 AC (0.975) | lagged MI (0.967), Δ −0.008 [−0.014, −0.003] | clean negatives (TE 0.53) | **NO** |

**No ceiling in the decisive strata.** S1–S3's best baselines sit at 0.85–0.90, which leaves room for a +0.05 win. The NOs are therefore not an artefact of a perfect baseline (the pilot's concern, §6 of the pilot report). SM's baseline (0.975) is near the ceiling, but there the information indicators also trail on the 60% cut, where it is lower (0.917).

**The answer under §6.5.** The protocol defines NO as "every test stratum is NO or UNDETECTABLE". **That category does not cover this outcome:** four NO, one UNDETECTABLE, one INCONCLUSIVE. The script's "NOT ANSWERED" is a fall-through in `report.py`, not a protocol category. Stated without forcing a category: **NO in every decidable regime (S1, S2, S3, SM); S4 undetectable, as physics predicts; S5 inconclusive.**

On S5:
- Against the baseline that scored best on confirmation (kurtosis, 0.561), PE's Δ is +0.009 [−0.031, 0.048], which would be a clean negative. It is inconclusive only against the calibration-chosen baseline.
- At the observed SE (≈ 0.019), settling Δ ≈ 0.03 against the 0.05 margin needs ≈ 2.8× the series (≈ 1,100 + 1,100 scored per family).
- Every indicator, information or baseline, is at most 0.57.

## 4. Reported alongside (not decisive)

- **60% cut:** baselines 0.72–0.92. No information indicator reaches Δ ≥ 0.05. Closest: S2 MI +0.023 (CI upper 0.041); S2 and S3 FI ≈ 0.
- **Full segment (to t_tip − B):** baselines 0.90–1.00 (near the ceiling, as in the pilot controls). No information indicator is ahead by the margin. So the NO is **not** a data-length effect of the 80% cut.
- **Learned directions for every indicator:** no information indicator exceeds the best baseline anywhere except S5 (PE 0.570 vs kurtosis 0.561).
- **Lead time, actionable lead time:** **unreliable in the ramped strata.** The post-hoc audit found that the pre-registered causal detrending leaves a drift of 1–3 window SDs in transition windows (≈ 0.2 in nulls). This inflates online alarms for any indicator sensitive to drift. With the artefact removed, the apparent information advantages in SM, CM and S2(a) disappear. **One lead survives:** the Fisher index's online detection in S3 (0.56–0.84 vs the best baseline's 0.27–0.56). It is "lead time only" under §6.1, unexplained, and **Speculative**.
- **Detection (§5.4)** is computed in `results.json` but not interpreted here. It uses the same causal residuals and inherits the same caveat.
- **Fixed-direction note:** in SM the Fisher index (pre-registered ↓) and variance (↑) score below 0.5 (0.11 and 0.08). Under multiplicative noise the fluctuations shrink as abundances fall, so both move the "wrong" way. With learned directions they are still below the best baseline.

## 5. Predictions scored (from `QR006B_PREDICTIONS_2026_10_18.md`)

| Prediction | Outcome |
|---|---|
| Controls: no win; PE and rank AC1 invariant; KSG within D2 | **Held** |
| S1, S2, S3, S4, S5, SM: no win (P(win) 5–30%, highest in S3) | **Held** in all. No win anywhere, so the 20–30% overall P(win) was not contradicted. |
| S2 detail: "most likely a tie between PE and rank AC1" | **Wrong.** PE 0.68 vs rank AC1 0.85; the best information indicator was MI, the best baseline MAD |
| S3 mechanism: lagged MI sees nonlinear lag-1 dependence | **Not borne out.** MI 0.76; the near-tie came from the Fisher index, which tracks variance |
| Secondary: against Pearson AC1 and variance *alone*, information indicators often look better in S1–S3, and the advantage vanishes against the widened set | **Partly.** Held in S2 (MI 0.865 > AC1 0.832 and variance 0.674, but < MAD 0.890). Failed in S1 (MI 0.77, FI 0.80 < AC1 0.90) and S3 (FI ties variance) |
| 60% cut: information indicators relatively worse | **Not held.** Relatively better in S2 (MI −0.025 → +0.023), still under the margin |
| Full segment: baselines near the ceiling | **Held** (0.90–1.00) |
| Lead time: no material information advantage outside S3 | **Held after the audit.** The raw numbers contradicted it through an artefact; the only surviving lead is in S3, the one place predicted |
| Surprises: wins in C0/C0g/CM, S4 above chance, an S2/SM win larger than S3's, wins in several strata | **None occurred** |
| Surprise: information indicators failing even against Pearson AC1 and variance in S2 and S3 | **Half occurred:** in S3 (FI ties variance, the others below); not in S2 |

## 6. What this result is and is not

- **Is:** a pre-registered, controlled benchmark in which six information indicators, as implemented, failed to beat the best non-information indicator by ΔAUC ≥ 0.05 in any decidable regime. It covers multiplicative, α-stable and flickering noise and multivariate networks, at matched false-alarm control and with replication across two model families.
- **Is not:**
  - a proof that information measures never help (threat 1: estimator and parameter choices);
  - evidence about real data (stratum E not built; threat 3);
  - a comparison against deep-learning classifiers (threat 8);
  - a decision on rate-induced tipping (S5 inconclusive).
- **Confidence:** **Supported** (single benchmark, one implementation, simulation only). It agrees with the prior literature leaning NO: Harris et al. 2024, where distribution-shape features won; the seizure-prediction literature (Mormann 2005, abstract level); and Weinans 2021.
- **Novelty check:** the gate verdict (PROCEED with named gaps) stands. Dakos & Soler-Toscano 2017 and Mormann 2005 remain unread. If either holds a matched-false-alarm comparison, the overlapping strata are replications.

## 7. Pending

1. §5.7 sensitivity analyses: `run_confirmatory --variants window0.5,detrend_gaussian,detrend_none,buffer50,obsnoise,nullB`, ≈ 19 h. Their lead-time parts inherit the causal-detrending artefact. The window-0.5 run matters most: it is the test of the data-hunger threat.
2. S5: accept as inconclusive, or extend to ≈ 1,100 + 1,100 scored series per family (owner).
3. The S3 Fisher-index lead-time lead: Speculative. Parked unless the owner wants a prior-art check and a pre-registered follow-up on fresh seeds.
4. §6.5 gap: the owner decides how the "NO + UNDETECTABLE + one INCONCLUSIVE" outcome is labelled. Recommended: "NO in all decidable regimes (S5 inconclusive)".
5. QR-008 stage 2 receives the type-by-indicator table: for every regime tested, the best warning indicator is a non-information one.

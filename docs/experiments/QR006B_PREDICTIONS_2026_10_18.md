# QR-006b — predictions recorded before the confirmatory results

**Written:** 2026-10-18, evening, while the confirmatory run (`run_confirmatory --variants primary,C0g`, started 20:57 from commit `d236f56`, tag `qr006b-prereg-frozen` plus deviations D1–D2) was still computing indicators.
**Author:** the main research session, at the owner's request.
**State of knowledge when written:** no confirmatory result had been computed or opened. Eight raw indicator files existed in `~/qr006b_runs/indicators/`; no AUC, lead time or decision had been calculated from them, and none was looked at. The only results seen were the pilot's control and leakage checks (`QR006B_PILOT_REPORT_2026_10_18.md`), which by design compare no information measure with a baseline in a test stratum.

**What this is.** A dated record of what we expected, so that afterwards we can check whether our judgement was calibrated and whether any interpretation is being fitted after the fact. **It changes no rule.** The decision rules are those of the frozen pre-registration (§6) with deviations D1–D2; these predictions carry no weight in the verdict.

Probabilities are subjective judgements, not calculations. "Win" means an information indicator meets the pre-registered rule in that stratum: it beats the **best** baseline by ΔAUC ≥ 0.05 on the decisive score (the 80% cut, D1), survives the §6.3 multiple-comparison control, and does so in **both** model families.

---

## 1. Per-stratum predictions

| Stratum | Regime | Prediction | P(an information indicator wins) | Reasoning |
|---|---|---|---|---|
| C0 | Additive Gaussian (textbook CSD) | No win | ≈ 0 (a win means a bug) | In this regime lagged MI, permutation entropy and transfer entropy are functions of the autocovariance (−½ log(1 − ρ²); Granger equivalence; Gaussian ordinal-pattern probabilities). They can at best match AC1 and variance. |
| C0g | Gaussian copula (monotone transform of C0) | No win; PE and rank AC1 unchanged from C0; KSG MI within the D2 tolerance | ≈ 0 | Rank statistics are exactly invariant; KSG is invariant only asymptotically (pilot: −0.038). |
| CM | Multivariate additive Gaussian | No win, including transfer entropy | ≈ 0 | Transfer entropy reduces to Granger causality in the linear-Gaussian case. |
| S1 | Multiplicative noise | No win | ≈ 10% | Skews the marginal, but rank AC1 and the skewness and kurtosis baselines are aimed at exactly this. |
| S2 | α-stable noise | No win; most likely a tie between permutation entropy and rank AC1 | ≈ 15% | Pearson AC1 and variance break under heavy tails, but permutation entropy is rank-based and behaves much like rank autocorrelation, and the α-stable scale factor is in the baselines. |
| **S3** | **Strong nonlinearity / flickering near the fold** | **The stratum most likely to produce a win; still more likely no** | **≈ 20–30%** | Flickering makes the lag-1 dependence nonlinear, which lagged MI (and perhaps RPDE) can detect and autocorrelation cannot. Against: bimodality and kurtosis baselines see flickering directly, and the 80% cut (D1) may remove much of it, since flickering intensifies close to the tip. Leading candidate: **lagged MI (I1)**, then RPDE (I6). |
| S4 | Noise-induced tipping, parameter fixed | Every indicator at chance, information and baseline alike | ≈ 5% (would suggest leakage) | No precursor in the physics; the pilot's leakage check passed at 200 + 200 per family. |
| S5 | Rate-induced tipping | No win; most indicators near chance | ≈ 10% | No slowing down to detect; any signal comes from the moving equilibrium, which the baselines see as well. |
| SM | Multivariate, multiplicative noise | No win, including transfer entropy | ≈ 15% | The only test stratum for transfer entropy; near-linear coupling makes it close to Granger again, and it is data-hungry. |

**Overall:** P(at least one stratum gives a pre-registered win for an information indicator) ≈ **20–30%**, concentrated in S3. Central expectation: **NO overall**, with at most one narrow, regime-specific YES.

## 2. Secondary prediction (likely whatever the main verdict)

Against **Pearson AC1 and variance alone**, information indicators will often look better in S1, S2 and S3. That advantage will **shrink or vanish against the widened baseline set** (rank AC1, higher moments, bimodality, RAD, the α-stable scale factor, drift–diffusion–jump estimates). If this holds, it explains why the literature reports information measures as superior: they are usually tested against weak baselines.

## 3. Cross-check predictions on the reported, non-decisive scores

- **60% cut:** information indicators do relatively worse than at 80% (less data, weaker signal), so any S3 win at 80% weakens or disappears at 60%.
- **Full segment (to t_tip − B):** baselines near the ceiling again in the slow-ramp strata (as in the pilot controls), so few or no wins are possible there, by construction.
- **Lead time at a 5% false-alarm rate:** same ordering as the AUCs; no information indicator gives a materially longer lead time than the best baseline outside S3.
- **Data-hunger check:** if information indicators lose at 80% but win on the full segment, the "no" is partly a data-length effect, as D1's threat note anticipates. We would report that rather than a clean negative.

## 4. What would surprise us

- Any win in C0, C0g or CM. This would mean a pipeline fault, not a finding.
- Any indicator clearly above chance in S4.
- A win in S2 or SM larger than one in S3.
- Wins in several test strata at once.
- Information indicators failing even against Pearson AC1 and variance in S2 and S3. That would contradict the secondary prediction and suggest the estimators are underpowered at these window lengths.

## 5. Basis

- The linear-Gaussian and Gaussian-copula equivalences, folded in the gate reports (`prior_art_reviews/QR-006_BENCHMARK_GATES_2026_10_18.md`; `QR-006b_SECOND_SEARCH_2026_10_18.md` §4).
- Harris, Gollo & Fulcher 2024, Table S1: under unknown noise amplitude no information feature reached the top 100, and distribution-shape features won (second-search report §7).
- Seizure-prediction ROC comparisons, which found no advantage of nonlinear over linear measures (Mormann et al. 2005, abstract only; McSharry et al. 2003, abstract).
- Weinans et al. 2021: mutual information among the least robust of 13 indicators; information measures are data-hungry.
- D1's early cut handicaps data-hungry estimators.

## 6. After the results

Score this note honestly in the results report: which predictions held, which failed, and whether the probabilities were too high or too low. Do not edit this file after the results are opened. Corrections go in the results report.

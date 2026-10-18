# QR-006b Benchmark — Pre-registration

**Mode:** B (design only). **Nothing has been simulated, downloaded or computed for this benchmark.** Every choice below is fixed before any data is touched.
**Date:** 2026-10-18
**Question:** QR-006b, `docs/QUESTIONS_RAISED_LOG.md` (widened-baseline wording, owner-approved 2026-10-18).
**Gate status:** **PROCEED with named gaps**: `docs/prior_art_reviews/QR-006b_SECOND_SEARCH_2026_10_18.md` §8. Eason 2014 was read in full and is clean. Dakos & Soler-Toscano 2017 and Mormann et al. 2005 could not be obtained; both are carried into §10, gap 1.
**Not touched:** `ds_wiki.db`, `wiki_history.db`, the Chroma index, `docs/demo/`, the podcast folder.
**Freeze rule:** this file is the protocol. After the pilot (§7) one *freeze commit* may fill in the values that §7 says the pilot sets, and nothing else. Any later change is a numbered entry in §11 (Deviations), with its date and reason, made before the confirmatory results are opened where possible. Results that depend on a deviation are reported both ways.

---

## 0. Plain-language summary

We want to know whether "information" warning signs (measures of how predictable or how complex a signal is) ever warn of a tipping point better than the standard ones (a signal becoming slower and more variable, plus the newer shape-of-the-distribution and fitted-model measures). Theory already says they can't win when the noise is ordinary bell-curve noise, so the test is aimed at the cases where that theory breaks: unusual noise, strong nonlinearity, and tipping caused by noise or by changing conditions too fast. We simulate many systems that tip and many matched systems that don't, compute every warning sign the same way on all of them, and score each sign by how well it separates the two groups at a fixed false-alarm rate. Before looking at the hard cases, we check that the easy cases come out the way theory says; if they don't, the pipeline is wrong and we stop.

## 1. Hypotheses

For each **test stratum** s (§2.1) and each **information indicator** I (§4.1):

- **H₁(I, s):** I separates transition series from matched null series better than the **best** baseline indicator in s (§4.2) by at least ΔAUC = 0.05.
- **H₀(I, s):** it does not.

Every indicator, information or baseline, is also tested against chance (AUC = 0.5).

**What each overall answer would rule out** (Gate 2, test 5):
- **YES in stratum s** rules out "the classical, distributional and model-based indicators are sufficient in regime s". It would justify adding I to the toolbox for s.
- **NO in every test stratum** rules out recommending information indicators for warning, outside data-rich settings, in any regime tested. That is a clean negative the field lacks.
- **Regime-dependent** gives the type-by-indicator table QR-008 stage 2 needs.

**Out of scope:** deep-learning classifiers (Bury 2021) are not baselines here (§10, threat 8). Spatial indicators, observation-noise degradation (except §5.7), and real-time deployment are also out of scope. The benchmark does not test CCA observables (QR-007 folded; the participation ratio is a second-order statistic with no special standing).

## 2. Data

### 2.1 Strata

**Controls** have outcomes that theory fixes in advance (§6.4). **Test strata** are where the linear-Gaussian picture fails. Each test stratum has **two model families**, (a) and (b), so a result must replicate across models.

| ID | Regime | (a) | (b) | Role |
|---|---|---|---|---|
| **C0** | Additive Gaussian, small noise (textbook CSD) | Bury 2021 test models, unmodified: May harvesting (fold), consumer–resource (Hopf), consumer–resource (transcritical) | Cubic fold, ẋ = x − x³ + c(t) + σ ξ, low noise | Control |
| **C0g** | Gaussian copula: C0 residuals passed through a strictly increasing map | C0(a) residuals → exp(r / s_ref) | C0(b) residuals → same map | Control |
| **CM** | Multivariate, additive Gaussian | Lever plant–pollinator 4D (Weinans 2021) | Lever 20D, full collapse (Weinans 2021) | Control (for transfer entropy) |
| **S1** | Multiplicative noise | May fold with noise σ_m x dW | Cubic fold with noise σ_m (1 + x²)^{1/2} dW | Test |
| **S2** | α-stable (Lévy) noise | Layritz 2025 fold, ẋ = k − x², α ∈ {1.5, 1.8} | May fold driven by α-stable increments, α ∈ {1.5, 1.8} | Test |
| **S3** | Strong nonlinearity near the fold (flickering, skew, bimodality) | May fold, high noise | Cubic fold, high noise | Test |
| **S4** | Noise-induced tipping (parameter fixed) | May model at fixed b = 0.24 < b_crit | Cubic double well at fixed c = 0.1 | Test |
| **S5** | Rate-induced tipping | ẋ = (x + λ(t))² − 1 + σ ξ | Moving double well, ẋ = (x − λ(t)) − (x − λ(t))³ + σ ξ | Test |
| **SM** | Multivariate, multiplicative noise | Lever 4D, multiplicative | Lever 20D, multiplicative | Test (the only test stratum for transfer entropy) |
| **E** | Empirical | Bury 2021 records: anoxia sediment cores, thermoacoustic, paleoclimate | — | Descriptive only; not in the decision rules |

### 2.2 Model specifications

Each simulation uses Euler–Maruyama (Gaussian) or the Chambers–Mallows–Stuck increment (α-stable, via `scipy.stats.levy_stable.rvs`). Each run has a burn-in at the starting parameter. Series are sampled at a fixed interval before any analysis.

- **May harvesting fold** (C0a, S1a, S2b, S3a, S4a). These are the parameters in Bury's `test_models/may_fold_1500/sim_may_fold.py` (read 2026-10-18):
  - dynamics: ẋ = r x (1 − x/k) − b x²/(s² + x²), with r = 1, k = 1, s = 0.1;
  - forcing: b ramps linearly from 0.15 to 0.27, with b_crit = 0.260437;
  - integration: dt = 0.01, t_max = 1500, burn-in 100, sampled every 1 time unit, x reflected at 0;
  - noise: C0a uses σ = 0.01, as in the script.
  - **S1a:** noise σ_m x dW, with σ_m set so that the stationary residual SD at b = 0.15 equals C0a's (σ_m = 0.01 / x*, x* = 0.8197).
  - **S2b:** increments σ · L_α · dt^{1/α} with σ = 0.01, symmetric (β = 0).
  - **S3a:** σ from the grid {0.02, 0.03, 0.04, 0.05, 0.06}, set by the pilot rule in §7.
  - **S4a:** b fixed at 0.24, σ set by the escape-time rule in §7.
- **Consumer–resource Hopf and transcritical** (C0a). Bury's `cr_hopf_1500` and `cr_trans_1500` scripts, unmodified.
- **Cubic fold / double well** (C0b, S1b, S3b, S4b).
  - Dynamics: ẋ = x − x³ + c. The left well vanishes at c* = 2/(3√3) ≈ 0.3849.
  - Ramped cases: c ramps linearly from −0.2 to 0.45 over t ∈ [0, 1500], starting in the left well. dt = 0.01, sampled every 1 time unit.
  - C0b: σ = 0.05. S1b: σ_m matched to C0b's starting residual SD. S3b: σ from the grid {0.15, 0.2, 0.25, 0.3, 0.35} (pilot rule). S4b: c fixed at 0.1, σ by the escape-time rule.
- **Layritz fold** (S2a), from `lucialayr/stableEWS_paper/code/StableFold.py`, `gamma_neq` (read 2026-10-18):
  - dynamics ẋ = k − x², with k ramping from 5 to 0 in steps of 10⁻⁴ per step, dt = 0.005, after a spin-up of 10⁴ steps;
  - increments 0.1 · L_α · dt^{1/α};
  - escape when x < −√k − 0.1 k;
  - sampled every 40 steps (≈ 1,250 points over the ramp).
- **Rate-induced tipping** (S5).
  - (a) ẋ = (x + λ(t))² − 1 + σ ξ, with λ(t) = (λ_max/2)(1 + tanh(r t)) and λ_max = 3. This is the form commonly used as the canonical R-tipping example; it has not been checked against Ashwin et al. 2012, which was read only at abstract and front-matter level.
  - (b) ẋ = (x − λ) − (x − λ)³ + σ ξ, with λ(t) = −(λ_max/2)(1 + tanh(r t)) and λ_max = 3. λ moves downwards, so the lag pushes the state from the left well towards the barrier.
  - Both: σ = 0.05, dt = 0.01, sampled every 1 time unit, t ∈ [−750, 750].
  - The critical rate r_c for each model comes from deterministic runs (σ = 0) in the pilot. Transition runs draw r uniformly from [1.1 r_c, 2 r_c]; null runs from [0.5 r_c, 0.9 r_c].
- **Lever plant–pollinator** (CM, SM). Equations 1–2 of Weinans et al. 2021 (Methods; read in full text). Parameter values, the driver and its ramp are taken from Weinans 2021's Methods and Supplementary Information. **They have not been transcribed yet** (§10, gap 4). Multiplicative variant: the noise term σ A_k dW (and σ P_i dW), with σ matched as in S1. In 20D, observed variables are all 20.

### 2.3 Transition time and the analysed segment

- **t_tip** is the first time the state crosses the separating threshold:
  - May model: the midpoint between the upper and lower stable branches at b_crit;
  - cubic models: x = 0;
  - Layritz fold: Layritz's escape threshold;
  - S5(a): x + λ > 1, past the unstable root;
  - S5(b): x − λ > 0;
  - Lever: total pollinator abundance falls below 10% of its starting value.
- For Hopf and transcritical (no jump), t_tip is t_crit, the time the parameter crosses the bifurcation, as in Bury.
- The **pre-transition segment** is [t_start, t_tip − B], with buffer B = 20 sampled points (sensitivity: B = 50). It never contains the escape itself.
- Runs that tip before 40% of the ramp are discarded and counted. The count is reported per stratum.

### 2.4 Matched nulls

- **Null-A (primary).** The same model, noise and seed scheme, with the control parameter held at its starting value, or for S5 a sub-critical rate (§2.2).
- **Null-B (secondary).** The parameter ramps over the first 50% of the distance to the bifurcation only. This tests whether detrending removes non-critical trends.
- **S4 nulls.** Runs that do not escape within the record, plus fresh runs, both at the same fixed parameter.
- **Length matching.** Each null series is paired, by a fixed seed, with one transition series and truncated to that series' pre-transition length. Record length therefore cannot separate the classes.
- **Observed variables.** One-dimensional models give x. Lever gives all species.

### 2.5 Sample sizes, splits and seeds

- **Per stratum and model family:** 600 transition and 600 null series. Within a family, noise levels (S2 α, S3 σ) are split evenly.
- **Split:** 200 + 200 **calibration** (directions, thresholds, best-baseline choice) and 400 + 400 **confirmation** (all reported tests). Assignment is by seed, before simulation.
- **C0a:** each of Bury's three models gets 600 + 600.
- **Seeds:** `numpy.random.SeedSequence(20261018)` is spawned per (stratum, family, class, run). The pilot uses `SeedSequence(1)`, so no pilot series reappears in the confirmatory run.
- **Power, rough:** with 400 + 400 per family (800 + 800 pooled), the bootstrap SE of a paired ΔAUC is about 0.01 for AUCs in 0.6–0.9. The 0.05 minimum effect is then ≈ 5 SE, enough to survive the Holm correction (§6.3) with high power.

### 2.6 Bury et al. 2021 materials and licence

- **Repository:** `github.com/ThomasMBury/deep-early-warnings-pnas`. Its README declares **CC BY-NC-SA 4.0** (GitHub's licence field reads NOASSERTION; the README text governs).
- **Non-commercial:** this personal, non-commercial research use is compatible.
- **ShareAlike:** any *adapted* Bury script must carry the same licence and attribution. The repo is therefore cloned at a pinned commit into `external/bury2021/` (git-ignored) and called from wrappers, never copied into this repo. Our own code and our results tables are not adaptations.
- **Empirical data:** these have their own terms: PANGAEA dataset 923197 (anoxia), NOAA World Data Center (paleoclimate), and the repository itself (thermoacoustic). Each is recorded in `external/README` at download.
- **Stratum E nulls** follow Bury's own `test_empirical` scripts. These scripts have not been read (§10, gap 5).

## 3. Preprocessing (identical for every indicator)

Following Dablander & Bury 2022 (*PNAS*; read in full: a short letter showing that the detrending choice alone changes a classifier's verdict):

1. **Resample** to the fixed interval (§2.2). No interpolation is needed for simulated series. Empirical series are handled per Bury's scripts.
2. **Offline residuals** (prediction ROC, §5.1): Lowess detrending with span 0.20 of the segment length, Bury's setting (`ewstools` `detrend(method="Lowess", span=0.2)`). **Sensitivity:** Gaussian kernel, bandwidth 0.20; and no detrending.
3. **Causal residuals** (online lead time, §5.2; detection, §5.4): at each time t, subtract a one-sided Gaussian-kernel mean of past values with bandwidth 0.20 × segment length. A non-causal detrend would leak future data into an "early" alarm.
4. **Rolling window** w = 0.25 × segment length, trailing, evaluated every 5 points. Bury used 0.25. **Sensitivity:** w = 0.5, which favours the data-hungry information measures.
5. **The same residual series and the same windows** go to every indicator, information and baseline alike. No indicator gets its own preprocessing in the primary analysis.
   - **Declared secondary:** the Fisher Information index on raw, undetrended data, as its developers use it (Karunanithi 2008).
6. **Multivariate strata:**
   - Each variable is detrended separately.
   - Univariate indicators are averaged over variables.
   - Transfer entropy and the multivariate Fisher index use the full residual vector.

## 4. Indicators

**Direction rule.**
- Where the literature gives a direction (column "Dir."), it is fixed here.
- Where it does not ("learned"), the sign is set on the calibration split: the sign of the median Kendall-τ difference, transition minus null. It is then frozen for the confirmation split.
- **Secondary analysis:** every indicator is also scored with its learned direction.

### 4.1 Information-theoretic set (I)

| # | Indicator | Estimator and parameters | Implementation | Dir. |
|---|---|---|---|---|
| I1 | Lagged mutual information, lag 1 | KSG estimator, algorithm 1 (Kraskov, Stögbauer & Grassberger 2004), k = 4 neighbours, max-norm, nats; ties broken by adding jitter of 10⁻¹⁰ × window SD (fixed seed) | own code on `scipy.spatial.cKDTree`, unit-tested (§7) | ↑ |
| I2 | Transfer entropy (CM, SM only) | KSG conditional-MI form, target and source history 1, lag 1, k = 4. Score = mean over ordered pairs: all 12 pairs in 4D; a fixed set of 20 ordered pairs in 20D, drawn once with seed 0 | own code | learned |
| I3 | Permutation entropy | Bandt–Pompe, order d = 4, delay 1, normalised by log d!; ties broken by order of occurrence. Sensitivity: d = 3, 5 | `ordpy` 1.2.3 (MIT) | ↓ |
| I4 | Sample entropy | m = 2, r = 0.2 × window SD, Chebyshev distance (Richman & Moorman 2000) | `EntropyHub` 2.0 (Apache-2.0) via `ewstools.compute_entropy(method="sample")` | ↓ |
| I5 | Fisher Information index | Karunanithi et al. 2008 (Ecol. Soc. 13(1):22; method read in full text 2026-10-18), univariate and multivariate. Size of states ±2 SD of each variable over a reference period (the first 20% of the segment). Tightening level 100% (1D), 80% (multivariate). Discrete FI from binned state probabilities via the amplitude form I = 4∫(dq/ds)² (their Eq. 5), states ordered by phase-space closeness. The exact discrete expression is transcribed from the paper in the freeze commit | own code; unit test: I → 1/σ² for Gaussian input as bins shrink | ↓ |
| I6 | Recurrence period density entropy (RPDE) | Little et al. 2007, as in hctsa `EN_rpde` defaults: embedding m = 2, delay 1, ε = 0.12 on the z-scored window, no T_max; normalised entropy. Sensitivity: m = 3 | own port of `EN_rpde.m` (hctsa, read 2026-10-18), checked against hctsa on test series | learned |

*Why these six:* together they cover the families named in QR-006b: mutual information, transfer entropy, ordinal-pattern entropy, sample entropy, the ecological Fisher index, and RPDE. RPDE was the best information feature under variable noise in Harris 2024 Table S1 (second-search report §7).

### 4.2 Baseline set (B), as widened by the owner

| # | Indicator | Estimator and parameters | Implementation | Dir. |
|---|---|---|---|---|
| B1 | Lag-1 autocorrelation (Pearson) | lag-1 sample autocorrelation of residuals | `ewstools.compute_auto(lag=1)` | ↑ |
| B2 | Rank AC1 | Spearman correlation of (r_t, r_{t+1}) | own | ↑ |
| B3 | Variance | sample variance | `ewstools.compute_var` | ↑ |
| B4 | Robust spread | MAD × 1.4826 | own | ↑ |
| B5 | Skewness | adjusted Fisher–Pearson (pandas rolling) | `ewstools.compute_skew` | learned |
| B6 | Kurtosis | excess kurtosis (pandas rolling) | `ewstools.compute_kurt` | learned |
| B7 | Bimodality coefficient | BC = (g² + 1) / (κ + 3(n − 1)² / ((n − 2)(n − 3))), with g = skewness and κ = excess kurtosis | own | ↑ |
| B8 | cRAD | Harris et al. 2024 Eqs. 11–12 (read): f_RAD = σ(Δx)·[1/σ(U) − 1/σ(L)], with U, L the halves above and below the median. cRAD = f_RAD applied to y = \|x − median(x)\|. RAD (uncentred) reported as secondary | own; checked against the authors' code if their repository (`brendanjohnharris/criticality`, MATLAB, MIT) contains it, otherwise against a hand-computed example | ↑ (towards 0) |
| B9 | α-stable scale factor γ_X | Joint fit of (α, β, γ, δ) per window by McCulloch's 1986 quantile estimator. Layritz et al. fitted by `scipy.stats.levy_stable.fit` on 300-point windows (their code, read). That is too slow at this scale, so the ML fit is run on a fixed 2% subsample as a cross-check; disagreement is reported | own McCulloch; `scipy` cross-check | ↑ |
| B10 | Langevin restoring rate | Kramers–Moyal drift D₁(x): mean increment / Δt, in 20 equal-count bins of x within the window. Score = −slope of a linear fit of D₁ on x over the central 16 bins. → 0 at a fold | own (cross-check: `kramersmoyal` 0.4.1, MIT) | ↓ |
| B11 | Diffusion D₂ at the window median | second KM moment / (2Δt), same bins, median bin | own | ↑ |
| B12 | Jump intensity λ_J | jump–diffusion moment method (KM moments 4 and 6; Rydin Gorjão & Meirinhos 2019), central bins | `jumpdiff` 0.4.2 (MIT) | learned |

**Multivariate additions (CM, SM):**
- mean AC1 and mean variance over variables;
- largest covariance eigenvalue;
- PC1 explained-variance share (EWS7 family);
- AC1 of the PC1 projection. The projection is fitted on the reference period (first 20%) and then held fixed.

## 5. Scoring

### 5.1 Prediction ROC (primary)

1. For each series and indicator, compute Kendall's τ between the windowed indicator values and time, over the pre-transition segment (Bury 2021's statistic). Use the offline residuals.
2. AUC = Mann–Whitney probability that τ(transition) > τ(null), after applying the indicator's direction.
3. Compute AUC per stratum and model family, and pooled across the two families with equal weight.

### 5.2 Lead time at a fixed false-alarm rate (key secondary)

**Online rule.**
- Inputs: causal residuals and trailing windows.
- At each evaluation point t, compute the expanding-window Kendall τ of the indicator from its first window up to t.
- Raise an alarm when τ_t ≥ θ_I for 5 consecutive evaluation points.

**Threshold.** θ_I is set on calibration nulls so that 5% of null series alarm at any time over their full length: a per-series false-alarm rate of 5%. Sensitivity: 10%.

**Lead time.** t_tip − t_alarm, on confirmation transition series. An alarm after t_tip − B, or no alarm, counts as a miss.

**Report:**
- detection probability at 5% FAR;
- median lead time over detected series;
- the lead-time distribution, with misses counted as zero lead.

Units are sampled points and τ_rec,0 = −1/λ₀, the linear recovery time at the starting parameter, computed analytically per model.

### 5.3 Actionable lead time (QR-008, requirement 1)

- AL = lead time − T_resp, for T_resp ∈ {0, 1, 5, 20} × τ_rec,0.
- Report the fraction of confirmation transition series with AL > 0 at 5% FAR, per indicator and stratum.
- Stratum E reports T_resp in the record's own time units, descriptively.

### 5.4 In-progress detection (QR-008, requirement 2), reported separately

- **Windows:** short windows of w_d = 50 points, ending at t_tip − j for j ∈ {0, 5, 10, 20}, from causal residuals. Nulls: 50-point windows at random positions in null series, one per series.
- **Score:** the indicator's *level* (not its trend). AUC per j; direction learned on calibration.
- **Defined only** for strata with an abrupt jump: fold, N-tipping, R-tipping and Lever collapse. Not for Hopf or transcritical.
- **Not part of the YES/NO rule** (§6). QR-006b asks about warning, not detection. The result feeds QR-008.

### 5.5 Against chance and against baselines

- **Chance:** every indicator, information and baseline, is tested for AUC > 0.5 in every stratum (one-sided; two-sided where the direction is learned).
- **Pairwise:** every information indicator is compared with **each** baseline, and with the **best baseline** in that stratum. The best baseline is the one with the highest calibration-split AUC in that stratum, frozen before the confirmation split is scored.

### 5.6 Uncertainty

- Paired, stratified bootstrap over series: transition and null series are resampled separately, with the same resample used for all indicators. 10,000 resamples.
- Percentile 95% intervals.
- One-sided bootstrap p-values for H₀: ΔAUC ≤ 0.

### 5.7 Sensitivity analyses (reported, not decisive)

- Window 0.5.
- Gaussian-kernel detrending and no detrending.
- Buffer B = 50.
- Null-B.
- Permutation-entropy order 3 and 5; RPDE m = 3.
- Learned directions for every indicator.
- Gaussian observation noise at 10% of the residual SD, added to C0 and S2 only.

### 5.8 Results table (filled in after the run)

One row per (stratum, indicator) with:
- AUC [95% CI] for family (a), family (b) and pooled;
- p versus chance (Holm-adjusted);
- the best baseline, and ΔAUC [95% CI] against it (Holm-adjusted p);
- detection probability and median lead time at 5% FAR;
- the AL > 0 fraction at each T_resp;
- detection AUC at j = 0.

Plus one stratum-level row with the outcome label from §6.2.

## 6. Decision rules

### 6.1 Per information indicator I, per test stratum s (S1–S5, SM)

**"I beats the baselines in s"** requires all of these on the confirmation split:
1. AUC_I > 0.5, Holm-adjusted p < 0.05 (chance family, §6.3).
2. ΔAUC_I = AUC_I − AUC_best-baseline: pooled point estimate ≥ **0.05**, and Holm-adjusted one-sided p < 0.05 (primary family, §6.3).
3. **Replication:** the ΔAUC point estimate is > 0 in *each* model family, (a) and (b), separately.

**"I does not beat the baselines in s" (clean negative):** the upper bound of the pooled two-sided 95% CI of ΔAUC_I is < 0.05. Any advantage is then smaller than the minimum effect worth having.

**Otherwise: inconclusive** for (I, s).

**Lead time** is reported alongside. If I meets the ROC rule but its median lead time at 5% FAR is worse than the best baseline's (bootstrap 95% CI excludes 0), the result is labelled **"YES, mixed (ROC only)"**. A lead-time advantage with no ROC advantage is labelled **"lead time only"** and does not count as YES.

### 6.2 Per stratum

- **YES:** at least one I beats the baselines.
- **NO:** every I is a clean negative.
- **UNDETECTABLE:** every indicator, information and baseline, has AUC 95% CI including 0.5. This is expected for prediction in S4 (§6.4).
- **INCONCLUSIVE:** anything else. The report must state the n that would be needed, from the observed SE.

### 6.3 Multiple comparisons

- **Primary family:** the ΔAUC tests, information indicators × test strata.
  - Five univariate indicators (I1, I3–I6) × five univariate strata (S1–S5) = 25.
  - Six indicators (I1–I6) × SM = 6.
  - Total **31 tests**, Holm–Bonferroni at α = 0.05.
- **Chance family:** all indicators × all strata, Holm at α = 0.05.
- Sensitivity and secondary analyses are not corrected and are labelled exploratory.

### 6.4 Controls and blinding

The controls are computed and opened **first**. The test strata's confirmation results stay unopened until the controls pass. Expected control outcomes, from the folded linear-Gaussian and Gaussian-copula results (QR-006b gate reports):

| Control | Expected | Fails if |
|---|---|---|
| C0 | No I beats the baselines. Every I is a clean negative or has ΔAUC CI including 0 | Any I meets §6.1's YES rule in C0 |
| C0g | Permutation entropy's per-series τ is identical to C0's (exact invariance). Rank AC1's AUC equals C0's. KSG MI's AUC is within ±0.02 of C0's. Pearson AC1's AUC is ≤ C0's | Any of these breaks |
| CM | Transfer entropy does not beat the covariance baselines (TE = ½ Granger causality for Gaussian processes) | TE meets the YES rule in CM |
| S4, prediction | All indicators at chance (Kramers escape is memoryless at a fixed parameter) | Any indicator's prediction AUC > 0.6 with CI excluding 0.5: indicates leakage of the escape into the segment |

**If a control fails:** stop, audit the pipeline, and fix it as a numbered deviation (§11). Re-run the controls on fresh seeds. Only then open the test strata. If the cause cannot be found, the benchmark reports the failed control and does not answer QR-006b.

### 6.5 The answer to QR-006b

- **YES (regime-specific)**, naming the strata and indicators, if any test stratum is YES.
- **NO** if every test stratum is NO or UNDETECTABLE.
- **REGIME-DEPENDENT** if YES in some strata and NO in others. The table is then the result.
- **NOT ANSWERED** if the controls fail (§6.4), or if inconclusive strata outnumber decided ones.

**Promotion:** none follows automatically. Any YES is a single benchmark from one group's implementation, so at most **Supported** (charter), with a prior-art re-check before any wiki entry.

## 7. Pilot (pipeline validation; results discarded)

**Scale:** 50 transition and 50 null series per model family in every stratum, plus C0a's three models. Seeds come from `SeedSequence(1)`. About 1,400 series.

**Pass criteria.** All must hold before the freeze commit.
1. **Wrapper fidelity.** On the same series, our AC1 and variance Kendall τ match Bury's unmodified scripts' output to 10⁻⁶.
2. **Estimators.**
   - KSG MI on bivariate Gaussian samples (n = 375, ρ ∈ {0.3, 0.6, 0.9}, 200 replicates): mean within 5% of −½ log(1 − ρ²).
   - Permutation entropy exactly invariant under exp(·).
   - Sample entropy equals EntropyHub's.
   - RPDE matches hctsa `EN_rpde` within 10⁻³ on 10 test series.
   - cRAD matches the authors' code (or the hand-computed example, §4.2) within 10⁻⁶.
   - McCulloch γ is within 10% of the scipy ML fit on α-stable samples (α ∈ {1.5, 1.8}, n = 300).
   - The Fisher index tends to 1/σ² on Gaussian input.
3. **Leakage check:** S4 prediction AUCs lie in 0.5 ± 0.1 for all indicators.
4. **Runtime** per series within 2× of the §8 estimate; otherwise §8 is re-estimated in the freeze commit.

**Values the pilot sets.** Only these, each by its stated rule:
- **S3 σ:** the smallest grid value at which ≥ 50% of transition runs flicker before t_crit. Flickering means at least one excursion past t_tip's threshold and back, lasting ≥ 5 sampled points.
- **S4 σ:** the grid value (geometric grid, 8 points) whose median first-passage time is closest to the record length.
- **S5 r_c:** from deterministic runs, by bisection to 1% relative precision.
- **S5 null noise:** σ is halved until ≤ 2% of null runs tip.
- **Lever parameters:** transcribed from Weinans 2021 (§10, gap 4).
- **Fisher index:** the discrete formula, transcribed.

## 8. Compute estimate

| Item | Estimate |
|---|---|
| Series | C0a 3 × 1,200; C0b, S1–S5 2 × 1,200 each (≈ 13,200); CM, SM 2 × 1,200 each (4,800 multivariate); C0g reuses C0 residuals. ≈ **21,600 series** |
| Simulation | Vectorised across runs. ≈ 150k Euler steps per 1D series; ≈ 3–5 CPU-hours in total |
| Indicators, 1D | ≈ 165 windows of ≈ 275 points per series; ≈ 20 ms per window for all 18 indicators (KSG, sample entropy and RPDE dominate); offline + online + detection ≈ 7 s per series → ≈ 30 CPU-hours |
| Indicators, multivariate | Univariate indicators on 4 or 20 variables, plus transfer entropy (20 pairs) → ≈ 50–60 CPU-hours |
| Bootstrap | 10,000 resamples × ~40 (stratum, indicator) cells, vectorised: < 1 CPU-hour |
| **Total** | ≈ **90–100 CPU-hours**: about 12–15 hours wall-clock on the M4 at 8 workers; ≈ 2 days including the pilot and one re-run |
| Disk | Raw series < 1 GB (Parquet); indicator tables ≈ 2–3 GB; git-ignored. Summary tables committed |

## 9. Code plan

**Environment.** A separate virtual environment, `.venv-qr006b`, from a pinned `scripts/qr006b/requirements.txt`:
- `numpy`, `scipy`, `pandas`, `statsmodels` (Lowess), `pyarrow`;
- `ewstools==2.1.3` (MIT; it pulls in EntropyHub (Apache-2.0), `arch`, `lmfit`, `plotly`);
- `ordpy==1.2.3` (MIT), `jumpdiff==0.4.2` (MIT), `kramersmoyal==0.4.1` (MIT).

The project's numpy-only rule applies to ingestion passes, not to experiment scripts. A separate environment keeps the main `.venv`, which has no scipy, unchanged. Bury's code needs AUTO-07P only to regenerate *training* data, which is not needed here; the test-model scripts use `ewstools` alone.

```
scripts/qr006b/
  README.md            how to run; licence notes for external/
  requirements.txt     pinned versions
  config.py            every parameter in this file, one place; frozen at the freeze commit
  models.py            simulators (§2.2); wrappers that import Bury's test models from external/
  segments.py          t_tip, buffers, null matching, splits (§2.3–2.5)
  preprocess.py        offline and causal detrending, windows (§3)
  indicators/
    info.py            I1–I6
    baselines.py       B1–B12 + multivariate additions
  score.py             Kendall τ, AUC, bootstrap, Holm, lead time, AL, detection (§5–6)
  run_pilot.py         §7, writes data/experiments/qr006b/pilot/
  run_confirmatory.py  refuses to run unless config.FROZEN is True and the git tree is clean
  report.py            writes the §5.8 table to data/reports/qr006b/
  tests/               estimator unit tests (§7, item 2); pytest.importorskip on the extra
                       dependencies, so the main suite (tests/) is unaffected
external/bury2021/     git-ignored clone at a pinned commit (CC BY-NC-SA 4.0)
data/experiments/qr006b/   git-ignored raw outputs
data/reports/qr006b/       committed summary tables + run manifest (commit hash, seeds, versions)
```

**Order:**
1. Unit tests.
2. Pilot.
3. Freeze commit.
4. Confirmatory run on controls.
5. Open the controls.
6. If they pass, open the test strata.
7. Write the report.

The confirmatory scripts log the commit hash, package versions and seeds into the manifest.

## 10. Known gaps and threats to validity

**Gaps:**
1. **Reading gaps from the gate** (second-search report §8; verdict **PROCEED with named gaps**). Eason et al. 2014 was read in full and is clean. Two items could not be obtained:
   - **Dakos & Soler-Toscano 2017** (search summary only) could already hold a complexity-vs-CSD comparison for the bifurcation strata (C0, S1, S3), and for S4/S5 if its transition types include noise- or rate-induced tipping. Its measure, BDM Kolmogorov complexity, is not in §4.1. Adding it would be an owner decision, logged as a deviation.
   - **Mormann et al. 2005** (abstract only) is one empirical system with no regime labels. It cannot pre-empt a simulated stratum, but its negative result for univariate non-linear measures is a prior in favour of NO.

   If either is read later and contains a matched-false-alarm comparison, the overlapping strata's results are reported as replications, not new answers.
2. **The Fisher index's discrete estimator** is not yet transcribed. Our implementation may differ from the EPA group's code, which was not found.
3. **No primary source for the R-tipping model forms (S5).** They are standard constructions. Ashwin 2012 was not read in full.
4. **Lever / Weinans parameters** are not yet transcribed. No code release was found in a keyword scan of the full text (models were run in MATLAB Grind; MI via NPEET). If the SI values cannot be recovered, the model is parameterised from Lever et al. 2014 and logged as a deviation.
5. **Bury's empirical null construction** (`test_empirical`) has not been read. Stratum E is descriptive only.

**Threats to validity:**
1. **Estimator choice.** Information measures are sensitive to their estimator (k, bins, embedding). One fixed choice per measure could understate them. Partial mitigation: the window-0.5 sensitivity and the parameter sensitivities. A NO is "for these estimators".
2. **Window length.** w = 0.25 favours the cheaper baselines (Weinans 2021). The w = 0.5 sensitivity is reported, but the decision uses w = 0.25 for comparability with Bury.
3. **Simulation-only decisions.** All decisive strata are simulated. Real systems mix regimes. Stratum E cannot be stratified.
4. **Model choice inside a stratum.** Two families per stratum limit, but do not remove, model-specific results.
5. **Kendall-τ trend scoring** follows Bury but discards level information. Lead time and detection partly cover this.
6. **Best-baseline selection** on the calibration split is conservative for the information indicators. That is intended: QR-006b asks whether they beat *all* baselines.
7. **N- and R-tipping labels.** In S4, prediction is expected to be impossible, and S4's "transition" labels are chance outcomes. S4 is a leakage and false-alarm check as much as a test.
8. **No deep-learning comparator.** A YES against the non-ML baselines may not survive against Bury-type classifiers. That comparison belongs to QR-008.
9. **Same group implementing all indicators.** Errors could favour either side. Mitigation: package cross-checks (§7) and the controls (§6.4).
10. **The direction rule.** Learned directions use the calibration split only, but skewness and kurtosis can change sign within a stratum. If so, this is reported, and the AUC understates them.
11. **Licence.** ShareAlike obligations attach to any adapted Bury code. Handled by not vendoring it (§2.6).

## 11. Deviations

*None yet.* Each entry: number, date, what changed, why, whether made before or after opening any confirmatory result, and which results it affects.

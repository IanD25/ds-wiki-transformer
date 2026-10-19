# QR-006b Benchmark — Pilot Report

**Date:** 2026-10-18. **Mode:** B. **Protocol:** [`QR006B_BENCHMARK_PREREGISTRATION.md`](QR006B_BENCHMARK_PREREGISTRATION.md) §7 (pilot), with amendments in its §12 and the freeze values in §13.
**Verdict:** **the pilot passes.** The pipeline is validated and the protocol is frozen. **The confirmatory run has not been started**; the owner starts it.
**Results:** pilot results are discarded (§7). This report gives only what §7 allows: pipeline diagnostics, the values the pilot sets, the control-stratum safety check and the S4 leakage check. **No information-versus-baseline comparison was computed for any test stratum (S1, S2, S3, S5, SM)**, and none is reported.
**Not touched:** `ds_wiki.db`, `wiki_history.db`, the Chroma index, `docs/demo/`, the podcast folder. Nothing promoted.

---

## 0. Plain-language summary

We built the machine that will run the benchmark, and tested it on a small batch: about 2,200 simulated series (50 that tip and 50 that don't, per model), plus a larger check of 400 more series in one stratum.

- **The machine works.** Our code reproduces Bury et al.'s own published scripts to 13 decimal places. Every warning-sign calculator matches a reference package or a worked example from its original paper. The simulators reproduce known numbers: for example, the published critical rate for rate-induced tipping (2.0; we get 2.006).
- **The safety check passes.** In the "easy" control cases, where theory says the information measures cannot win, none of them did.
- **The leak check passes.** In the case where tipping is pure chance (noise-induced tipping at a fixed setting), no warning sign could predict it: the scores sat between 0.44 and 0.57, where 0.5 is a coin flip. At the first, smaller size, a few signs drifted outside the allowed band. We had written down in advance that this would trigger a re-check at four times the size, and at that size they fell back inside.
- **It is cheaper than we thought.** The part of the run that decides the answer takes about 3.5 hours on the Mac. Every optional robustness check together takes about 18 hours.
- **Two things for you to decide before the full run** (§6). In the easy control cases the best standard sign is already near-perfect (a score of 0.98–1.0 out of 1). So "the information measures did not beat it" was close to guaranteed there. If the hard cases are also that easy, the benchmark can only answer "no" there. And one control expectation (mutual information unchanged by a reshaping of the data, to within 0.02) looks too strict for the estimator we use.

## 1. What ran

| Item | Value |
|---|---|
| Code | `scripts/qr006b/` at commit `e42b6c5` (pipeline and pre-pilot amendments A1–A18 committed **before** the pilot ran) |
| Environment | `.venv-qr006b`, Python 3.13.12, numpy 2.5.4, scipy 1.18.1, numba 0.68.0, ewstools 2.1.3 (`requirements.txt`) |
| Machine | Apple M4, 9 worker processes |
| Seeds | `SeedSequence(1)` (pilot); pilot-setting runs use their own class code. No pilot series can reappear in the confirmatory run (`SeedSequence(20261018)`) |
| Pilot size | 50 transition + 50 null series per model family, every simulated stratum: 18 model families, 900 pairs, plus C0g on C0's 200 pairs: **2,200 series** |
| S4 extension (A15) | 200 + 200 per family, 800 series |
| Wall-clock | settings 10 s; simulation 12 s; indicators 17.6 min (9,476 CPU-s); S4 extension ≈ 6 min |
| Outputs | summary `data/reports/qr006b_pilot/` (`pilot_summary.json`, `pilot_settings.json`, `pilot_s4_extension.json`, `fidelity_bury.json`); raw per-series tables `data/experiments/qr006b/pilot/` (git-ignored) |

**Simulation counts** (runs needed to obtain 50 valid pairs; discards are replaced by the next seed, A14):

| Stratum / family | Discards | Note |
|---|---|---|
| C0 (May, Hopf, transcritical, cubic), CM, S1, S5(b), SM | 0 | |
| S2(a) Layritz | 3 nulls escaped | α-stable jumps |
| S2(b) May, α-stable | 15 transitions tipped before 40% of the ramp | |
| S3(b) cubic, high noise | 22 transitions tipped before 40% | |
| S4(a) May, fixed b | 298 runs for 50 + 50; 53 early escapes | ≈ 17% of runs give a usable transition |
| S4(b) cubic, fixed c | 298 runs; 43 early escapes | |
| S5(a) | 1 transition run did not tip | noise near r_c |

Segment lengths (pre-transition, samples): 1,270–1,440 for most ramped models; S2 down to ≈ 600 (early jumps); S3(b) median 716 (high noise tips well before the fold); S4 600–1,480; S5 730–850. The rolling window is 25% of each segment (≈ 180–350 points), with 110–210 windows per series.

## 2. Pass criteria (§7)

| # | Criterion | Result |
|---|---|---|
| 1 | Wrapper fidelity: our AC1 and variance Kendall τ = Bury's unmodified scripts' output to 10⁻⁶ | **Pass.** Max abs difference 8.9 × 10⁻¹⁴ over residuals, rolling variance, rolling AC1 and both τ series, on all three of Bury's models (`fidelity_bury.json`; A17) |
| 2a | KSG MI on bivariate Gaussians (n = 375, ρ = 0.3/0.6/0.9, 200 reps) within 5% of −½ log(1 − ρ²) | **Pass** (≈ 2–3% off; the AR(1) lagged-MI identity also passes) |
| 2b | Permutation entropy exactly invariant under exp(·) | **Pass**, and equal to `ordpy` to 10⁻¹² with ties |
| 2c | Sample entropy = EntropyHub's | **Pass** (exactly, including the undefined case; A20) |
| 2d | RPDE vs hctsa (replaced by A5) | **Pass**: equal to an independent transcription of the published algorithm to 10⁻¹² on 10 series × m ∈ {2, 3}; periodic signal → H_norm < 0.1 |
| 2e | cRAD vs the authors' code / hand example | **Pass**: −1.2903 / −1.6959 on the A6 example |
| 2f | McCulloch γ within 10% of scipy's ML fit (α ∈ {1.5, 1.8}, n = 300) | **Pass** (median relative difference over 10 samples; A7) |
| 2g | Fisher index (replaced by A5) | **Pass**: Ahmad 2016's worked example FI = 2.136; falls monotonically with σ |
| — | Also tested: Kramers–Moyal restoring rate and diffusion on an OU process (within 5%), jump rate on a simulated jump–diffusion (within 25%), Kendall τ_b and the expanding τ vs scipy (10⁻¹²), transfer entropy (0 when independent; Gaussian value when coupled) | Pass. 17 tests in `scripts/qr006b/tests/` |
| 3 | Leakage: S4 prediction AUCs in 0.5 ± 0.1 for all indicators | **Pass after the A15 extension.** At 50 + 50, 11 of 44 (indicator × family) AUCs fell outside, 0.34–0.69. A15, written before the pilot, says the SE at that size is ≈ 0.058 and requires re-judging at 200 + 200. There, every AUC (confirmation split, 133 + 133) lies in **0.44–0.57** |
| 4 | Runtime within 2× of §8 | **Pass** (faster): 0.3–3.7 s per univariate series, 8 s (Lever 4D), 24 s (Lever 20D), against §8's ≈ 7 s and ≈ 40 s |

## 3. The safety check (control strata, allowed by §7)

Rule applied at pilot size: does any information indicator meet §6.1's YES rule (ΔAUC ≥ 0.05 over the best baseline, Holm-adjusted p < 0.05, positive in both families)? Directions were fixed or learned per family on the calibration third; AUCs are on the confirmation two-thirds (≈ 33 + 33 per model).

| Control | Best baseline (pooled AUC) | Information indicators: pooled AUC; Δ vs best [95% CI] | Any YES? |
|---|---|---|---|
| **C0** additive Gaussian | variance (1.00) | MI 0.84, Δ −0.16 [−0.20, −0.13]; PE 0.85, −0.15; SampEn 0.83, −0.17; FI 1.00, 0.00 [−0.001, 0.001]; RPDE 0.52, −0.48 | **No** (all clean negatives) |
| **C0g** Gaussian copula | variance (0.98) | MI 0.80, −0.18; PE 0.85, −0.13; SampEn 0.97, −0.01; FI 0.97, −0.00; RPDE 0.93, −0.05 | **No** |
| **CM** multivariate Gaussian | AC1 (0.99) | MI 0.995, +0.008 [−0.008, 0.03]; PE 0.89, −0.10; SampEn 0.97, −0.02; FI 0.99, +0.006; RPDE 0.72, −0.27; **TE 0.65, −0.34** | **No** |

**C0g exact invariances** (§6.4): permutation entropy's and rank AC1's per-series τ are **identical** to C0's in all four models (max difference 0). Pearson AC1's AUC falls under the transform in May, transcritical and cubic, as expected.

**The safety check passes.** Two caveats belong with it:
1. **Ceiling.** The best baseline sits at AUC 0.98–1.00 in every control. With the baseline already near-perfect, no indicator could have beaten it by 0.05, so this check had little power to fail. It still exercises the whole scoring chain, and the exact invariances above are a sharp test.
2. **The Fisher index tracks variance.** Its AUC equals variance's in C0 (1.00, Δ = 0.000). That is the 1/σ² identity (Eason 2014) showing up in the data, and a useful sanity signal.

**Online rule (lead time), control strata only.** Thresholds set on the calibration nulls give a false-alarm rate of 3.6–6.9% (mean per family) on the confirmation nulls, against the 5% target. With only 17 calibration nulls per family, single indicators range up to 24%; at 200 calibration nulls this noise shrinks. Every threshold is finite in every stratum (structural check only for the test strata).

## 4. Values the pilot set (§7)

| Item | Value | Note |
|---|---|---|
| S3 σ | May **0.06**, cubic **0.35** | Both are the **top** of their pre-registered grids, just reaching the 50% flicker rule (54%, 50%). Lower grid values flickered in ≤ 10% of runs |
| S4 σ | May **0.0399**, cubic **0.2166** | The A9 grid is coarse where it matters: neighbouring values give median escape times of 2,433 vs 901 (May) and 3,160 vs 686 (cubic). The rule picks the closer in log ratio. About 17% of runs then give a usable transition, so S4 needs ≈ 3,600 runs per family in the full run (cheap) |
| S5 r_c | (a) **2.006**, (b) **0.378** | (a) agrees with Ritchie & Sieber 2016's ε_c = 4/3 (r_c = 2 here) to 0.3% |
| S5 σ | **0.05** both | 0/100 nulls tipped; no halving needed |
| Lever δ_c | 4D **0.3657**, 20D **1.4945** | Consistent with Weinans 2021's SI figures |

## 5. Problems found, and amendments

**Before the pilot** (protocol §12.1, A1–A18, committed in `e42b6c5` before the pilot ran). The substantive ones:
- **A11, S5 was uninformative as written.** With t ∈ [−750, 750] and unit sampling, the whole rate ramp sits within about one time unit of t = 0. A segment ending 20 samples before tipping would contain no ramp at all, so the stratum could not have detected anything. Fixed by re-scaling the record window to the critical rate.
- **A10, S3's first-crossing rule** would have cut every series before its first flicker. Now the final crossing.
- **A4, the online rule.** τ over the first few overlapping windows is ±1, so the 5% threshold would have been degenerate. Online τ now starts after one window length.
- **A5, two checks that could not be run as written.** The Fisher-index check (an estimator that is not an estimator of 1/σ²) and the RPDE check (hctsa needs MATLAB; its code is GPL) were replaced.
- **A12, the Lever ramp.** Weinans' ramps never tip, so the ramp was extended past the collapse.

**After the pilot ran** (protocol §12.2; prompted by diagnostics, not comparisons):
- **A20, undefined values.** Sample entropy on the 50-point detection windows was undefined in up to 58 of 100 series per family, and RPDE (m = 3) often. Sample entropy now follows EntropyHub's +∞ convention, and NaN pairs count as ties in every AUC. The offline prediction τ had no undefined values anywhere.
- **A19.** Learned directions are set once per stratum, not per family.
- **A21.** Null-B was undefined for the Layritz fold. Found by an end-to-end smoke test of the confirmatory code on throwaway seeds.
- **A22.** Analysis families spelled out.

**Bugs fixed during the build** (no protocol change): the Layritz null record was shorter than its paired transition; the transcritical model's recovery time used a non-existent interior equilibrium (now the stable boundary state, τ_rec = 1.14); the pilot's online check ignored learned directions.

## 6. For the owner: decide before starting the full run

Each of these can be handled by a numbered deviation in §11 **before** the confirmatory run, or left as is. I have not changed any of them.

1. **Ceiling risk (design).** In every control the best standard indicator scored 0.98–1.00. The test strata share these models' ramp length and sampling, so some may sit at the ceiling too. **I have not looked at the test strata.** Where a baseline is near AUC = 1, an information indicator cannot beat it by 0.05, and the stratum returns a "NO" that only means "the baseline is already perfect". Options:
   - accept it: the question is "do they beat the best baseline", and a perfect baseline is a legitimate NO;
   - make prediction harder for every stratum alike: score only the earlier part of each segment (Bury's "early" interval, 60–80% of the way to the transition), or use shorter records;
   - rely on lead time, which has no ceiling at fixed false-alarm rate, as the tie-breaker. It is reported already but is not decisive.
2. **One C0g expectation is probably too strict.** §6.4 expects KSG MI's AUC within ±0.02 of C0's. The pilot shows −0.038 pooled (−0.06 in the cubic model). KSG is invariant under monotone maps only asymptotically, so this looks like estimator behaviour, not a pipeline fault. At confirmatory size this control may "fail" and halt the run under §6.4. Options: relax it to "within the bootstrap CI of a paired difference", or keep it and accept the halt-and-audit.
3. **AC1 in the Hopf model goes the "wrong" way.** Its AUC with the pre-registered ↑ direction is ≈ 0.005; the paired invariance "Pearson AC1's AUC ≤ C0's" then fails trivially in that one model. The decision rules are unaffected (the best baseline is chosen per stratum, and variance wins), but the §6.4 check should be read as pooled, or per model excluding Hopf. Lag-1 autocorrelation falling before a Hopf bifurcation at this sampling interval is known behaviour, not a bug.
4. **S3 σ at the top of the grid; S4 grid coarse.** Both follow the rules. S3 runs at the noisiest pre-registered setting. S4's expected escape time (≈ 2,400) is longer than the record, which makes transitions rarer but does not bias the comparison.
5. **Stratum E** (empirical) is deferred (A16). It is descriptive and not in the decision rules.
6. **Gap 1** (Dakos & Soler-Toscano 2017; Mormann 2005) is still unread.
7. **Compute.** The decisive part is ≈ 32 CPU-hours (≈ 3.5 h wall-clock); with all sensitivity analyses ≈ 160 CPU-hours (≈ 18 h). Suggested order: `--variants primary,C0g`; `report --stage controls`; then the sensitivities; then `report --stage tests`.

## 7. What was deliberately not done

- No AUC, ΔAUC, lead time or detection value was computed or opened for S1, S2, S3, S5 or SM. The pilot code computes only structural diagnostics there (NaN counts, finite thresholds, timings).
- No confirmatory seed was simulated.
- No package beyond the owner-approved list was installed. Bury's repository is a git-ignored sparse clone, run unmodified and not copied.

## 8. Files

- Code: `scripts/qr006b/` (README there). Tests: `scripts/qr006b/tests/test_estimators.py`.
- Pilot outputs: `data/reports/qr006b_pilot/`.
- Readings behind A5–A12: primary sources named in the protocol's §12, with reading levels. Transcribed Weinans 2021 matrices: `scripts/qr006b/data/`.
- Confirmatory entry points, not run: `run_confirmatory.py` (refuses unless `config.FROZEN` is True and the code and protocol are committed) and `report.py` (opens the controls first).

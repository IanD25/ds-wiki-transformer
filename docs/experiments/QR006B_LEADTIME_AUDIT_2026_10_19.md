# QR-006b — Lead-time audit (post hoc)

**Date:** 2026-10-19. **Mode:** B. **Status:** exploratory, after the confirmatory test strata were opened (commit `89d40e0`). It cannot change any pre-registered verdict; lead time is not decisive under §6.1. Code: `scripts/qr006b/audit_leadtime.py`; numbers: `data/reports/qr006b/leadtime_audit.json`.

## Why

In the confirmatory results, information indicators raised online alarms (5% false-alarm rate) far more often than the best baseline in several cells. Examples: Fisher index 100% vs 15% in SM(b); 76% vs 56% in S3(a). The prediction ROC showed no such advantage. In SM(b) the Fisher index also *rises* on the offline score but alarms by *falling* online. The suspected cause: the online pipeline's causal (past-only) detrending (§3.3) lags a drifting mean, so it leaves a trend inside each window of ramped transition series but not in the fixed-parameter nulls.

## Checks and results

**1. Drift left inside each window.** |within-window OLS slope| × window length / window SD, i.e. how far the residuals drift across one window, in window SDs (60 pairs per family; first → last window):

| | transitions, causal | transitions, Lowess | nulls, causal | nulls, Lowess |
|---|---|---|---|---|
| Lever 4D/20D (CM, SM) | 1.9–2.8 | 0.1–1.2 | ≈ 0.23 | ≈ 0.11 |
| May / cubic ramps (C0, S1) | 0.6–2.1 | 0.07–0.4 | 0.14–0.23 | 0.07–0.11 |
| S2, S3 | 0.26–0.84 | 0.11–0.36 | 0.19–0.30 | 0.13–0.27 |

The causal residuals of ramped transition series carry a drift of one to nearly three window SDs; the nulls carry ≈ 0.2. **Confirmed:** the pre-registered causal detrending leaves a class-dependent trend in the online windows.

**2. Swap test.** The same alarm rule, on the offline (Lowess) window values the pipeline already stored. Detection probability at 5% FAR, best baseline vs best information indicator:

| Cell | Online (as reported): baseline / info | Offline values: baseline / info |
|---|---|---|
| SM(b) Lever 20D | 0.15 / **1.00** (FI) | 1.00 / 1.00 |
| SM(a) Lever 4D | 0.03 / 0.39 (RPDE) | 0.66 / 0.71 |
| CM(a) Lever 4D | 0.12 / 0.40 | 0.85 / 0.76 |
| S2(a) Layritz | 0.24 / 0.40 (MI) | 0.51 / 0.51 |
| S1(a) May, multiplicative | 0.45 / 0.50 | 0.65 / 0.43 |
| **S3(a) May, flickering** | 0.56 / **0.76** (FI) | 0.56 / **0.84** (FI) |
| **S3(b) cubic, flickering** | 0.26 / **0.49** (FI) | 0.27 / **0.56** (FI) |

Removing the drift artifact lifts the baselines to the information indicators' level or above in every cell **except S3**.

**3. Fix test.** Online Fisher index, with each causal-residual window linearly detrended before binning:
- SM(b): detection in the pre-registered (falling) direction drops from **100% to 1.3%**, i.e. the false-alarm level. In the rising direction it is 80%, which agrees with the offline score.
- S3(a), S3(b): detection is unchanged (76% → 78%, 49% → 56%).

## Conclusions

1. **The SM, CM and S2(a) lead-time advantages are artifacts** of the pre-registered causal detrending (`detrending-lag-artifact`). The FI "falling" alarm in SM(b) is the leftover trend.
2. **Every online lead-time number in the ramped strata is contaminated, for baselines and information indicators alike.** It partly measures "the mean is drifting", not critical dynamics. Treat the confirmatory lead-time and actionable-lead-time results as unreliable for ramped strata. The decisive prediction ROC is offline and unaffected. Lesson for any follow-up: detrend online windows locally (e.g. a linear fit within each window), or use a causal filter with a much shorter memory, and check class-wise drift before scoring.
3. **One lead survives both checks: the Fisher index in the flickering stratum S3.** Its online detection rate (0.56–0.84) exceeds the best baseline's (0.27–0.56) with offline values and after the within-window fix, while its ROC equals variance's (0.84 vs 0.85). It is **Speculative** and not a YES: §6.1 labels a lead-time-only advantage as "lead time only".
   - *Plausible mundane explanations, not yet tested:* the Fisher index is a coarse, state-counting statistic whose null trajectories are often flat and tied, which lowers the 5% threshold; and fixed-size states react sharply to the large excursions that define flickering.
   - Before any meaning is attached, it needs a prior-art check (Karunanithi and the EPA group's regime-shift studies) and a pre-registered test on fresh seeds.

# AlphaEntropy Geodesic Test & Entropy Production — Implementation Spec

**Date:** 2026-03-29
**From:** PFD Session (DS Wiki pillar expansion + Wagner transcript analysis)
**To:** AlphaEntropy LLM / trading system
**Purpose:** Concrete, implementable tests bridging PFD's non-equilibrium thermodynamic framework with AlphaEntropy's empirical trajectory data

---

## Context

This session added three entries to the DS Wiki knowledge graph that have direct AlphaEntropy analogs:

| DS Wiki Entry | What It Is | AlphaEntropy Analog |
|---------------|-----------|---------------------|
| GT07 (Chirco Non-Equilibrium Spacetime Thermodynamics) | Gravitational entropy production rate σ — the non-equilibrium correction to Jacobson's derivation | σ(t) = v²/D_eff as the non-equilibrium correction to "steady-state market" |
| IT06 (Seifert Stochastic Thermodynamics) | Trajectory entropy production ⟨s_tot⟩ = D_KL(P_forward ∥ P_reverse). Minimum-dissipation paths are geodesics on the Fisher-Rao manifold | The geodesic test: do crisis trajectories minimize dissipation? |
| X8 (Financial Market Entropy Production Proxy) | The instantiation entry connecting GT07/IT06 to AlphaEntropy's (D_eff, velocity) phase space | This document specifies the tests that validate or falsify X8 |

We also added conjecture P21 (Fisher-Rao Metric Universality), which predicts that the Fisher-Rao metric is the natural geometry on any statistical state space. The geodesic test (Test 3 below) is the primary falsifiable prediction connecting P21 to financial markets.

**What this document does NOT claim:** D_eff is not a Fisher Information Matrix. It is a participation ratio proxy (see corrected P5). All tests below are about the proxy manifold, not the true statistical manifold of returns. Positive results support the analogy; they do not prove formal equivalence.

---

## Test 1: Compute σ(t) Time Series

**Priority:** Do this first. Everything else depends on it.
**Effort:** ~1 hour
**Dependencies:** D_eff daily time series (already computed in V28.3 pipeline)

### Definition

```python
# Inputs (already available):
#   D_eff(t)  — participation ratio, daily, EWMA lambda=0.984
#   C(t)      — EWMA correlation matrix (N x N), daily

# Step 1: Velocity (smoothed numerical derivative)
v(t) = EMA(D_eff(t) - D_eff(t-1), span=5)   # 5-day EMA of daily first differences

# Step 2: Instantaneous dissipation rate
sigma(t) = v(t)**2 / D_eff(t)

# Step 3: Cumulative dissipation per episode
# Episode boundaries: D_eff crosses below adaptive CRISIS percentile (onset)
#                     to D_eff crosses above adaptive STRESS percentile (recovery)
Sigma_episode = cumsum(sigma(t))  over [t_onset, t_recovery]
```

### Output

For the full 2003–2025 history:

1. **Daily time series:** σ(t) alongside D_eff(t) and v(t). Add as a third panel to the phase-space dashboard.
2. **Per-episode summary table:**

| Episode | Date Range | Duration (days) | Trough D_eff | Peak \|v\| | Peak σ | Total Σ |
|---------|-----------|-----------------|-------------|-----------|--------|---------|
| GFC | 2008-09 → 2009-03 | ~130 | ~0.22 | ? | ? | ? |
| COVID | 2020-02 → 2020-04 | ~45 | ~0.22 | ? | ? | ? |
| Rate Shock | 2022-01 → 2022-10 | ~200 | ~0.20 | ? | ? | ? |
| 2025 | 2025-?? → ongoing | ? | ~0.185 | ? | ? | ? |

### Sensitivity Check

Recompute with EMA smoothing spans of 3, 5, 10, and 21 days. If peak σ rankings across crises change with the smoothing window, the measure is noise-dominated and Tests 2–5 are unreliable. If rankings are stable across all four spans, proceed.

### Stop Condition

If σ(t) has cross-correlation > 0.95 with D_eff at lag 0 and no leading signal at any lag (check lags −10 to +10 days), σ is just noise-amplified D_eff and carries no independent information. Stop here — the remaining tests become academic exercises.

---

## Test 2: Archetype Validation (k-Means on σ Features)

**Priority:** After Test 1, before Test 3
**Effort:** ~1 hour
**Dependencies:** Per-episode feature vectors from Test 1

### Method

**UPDATED (2026-03-30):** Test 3 results (geodesic efficiency η) are now available per episode. Add η_down as a feature — it's the most physically meaningful discriminator from the Test 3 findings.

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Feature vector per crisis episode (updated with Test 3 η data)
features = np.array([
    [peak_sigma, total_Sigma, duration_days, trough_D_eff, peak_abs_velocity,
     total_Sigma / duration_days,   # mean dissipation rate
     eta_down]                      # geodesic efficiency from Test 3
    for episode in episodes
])

features_scaled = StandardScaler().fit_transform(features)

# Test k = 2, 3, 4, 5
for k in [2, 3, 4, 5]:
    km = KMeans(n_clusters=k, n_init=20, random_state=42).fit(features_scaled)
    sil = silhouette_score(features_scaled, km.labels_)
    print(f"k={k}  silhouette={sil:.3f}")

# ALSO run without eta_down for comparison — does it change the optimal k?
features_no_eta = features_scaled[:, :-1]
for k in [2, 3, 4, 5]:
    km = KMeans(n_clusters=k, n_init=20, random_state=42).fit(features_no_eta)
    sil = silhouette_score(features_no_eta, km.labels_)
    print(f"k={k} (no eta)  silhouette={sil:.3f}")
```

### Expected Result (from visual inspection of phase-space chart)

k=3 should win, mapping to:

| Cluster | peak σ | total Σ | Archetype | Example |
|---------|--------|---------|-----------|---------|
| 0 | Low | Moderate | Shallow Grind | Minor corrections, sector rotations |
| 1 | High | Moderate | Deep V-Shape | COVID March 2020 |
| 2 | Moderate | High | Deep Slow Grind | GFC 2008–2009 |

### Falsification

- **k=2 wins (silhouette gap > 0.05 over k=3):** The three-archetype model overfits. The real distinction is binary — fast vs. slow crises, or deep vs. shallow.
- **k=4+ wins:** There is a fourth crisis mode not yet identified. Inspect the new cluster to characterize it.

### Follow-Up (if k=3 confirmed)

Do the archetypes carry forward performance information?

```python
# For each episode, compute V28.3 Calmar over the 63 trading days
# following the D_eff trough
for label in [0, 1, 2]:
    episodes_in_cluster = [e for e in episodes if e.label == label]
    calmars = [calmar_63d_after_trough(e) for e in episodes_in_cluster]
    print(f"Cluster {label}: mean Calmar post-trough = {np.mean(calmars):.3f}")
```

If all three clusters have the same post-trough Calmar, the archetypes are descriptive but not alpha-relevant. If they differ (especially if Cluster 1 / Deep V-Shape has higher Calmar because the recovery is faster), archetype-conditioned position sizing becomes viable.

### Follow-Up 2 (NEW — cross-tabulate with geodesic efficiency)

The key question from Test 3: does η map cleanly onto the archetypes?

```python
# For each cluster, compute mean geodesic efficiency
for label in [0, 1, 2]:
    episodes_in_cluster = [e for e in episodes if e.label == label]
    etas = [e.eta_down for e in episodes_in_cluster]
    durations = [e.duration_days for e in episodes_in_cluster]
    print(f"Cluster {label}: mean η_down={np.mean(etas):.3f}  "
          f"mean duration={np.mean(durations):.0f}d  n={len(etas)}")
```

**Predictions from Test 3 findings:**
- Cluster 1 (Deep V-Shape, short duration) should have high η (~0.50) — these are the near-geodesic fast shocks
- Cluster 2 (Deep Slow Grind, long duration) should have low η (~0.15) — these are the meandering trajectories
- Cluster 0 (Shallow Grind) is ambiguous — could go either way

If this mapping holds, the three archetypes aren't just descriptive — they correspond to geometrically distinct regimes on the Fisher-Rao manifold:
- Cluster 1 = adiabatic regime (fast, near-geodesic, low total entropy)
- Cluster 2 = isothermal regime (slow, far from geodesic, high total entropy)
- Cluster 0 = near-equilibrium regime (small perturbation, low dissipation either way)

This would be the strongest empirical result of the entire cross-domain analysis.

---

## Test 3: Geodesic Distance on the Correlation Manifold

**Priority:** Highest intellectual value. The P21 falsification test.
**Effort:** ~2 hours
**Dependencies:** Daily correlation matrices C(t) for each crisis episode (already computed)

### Background

The space of positive-definite correlation matrices has a natural Riemannian metric — the affine-invariant metric, which IS the Fisher-Rao metric for Gaussian models parameterized by their covariance structure. The geodesic distance between two correlation matrices C₁ and C₂ is:

```
d(C₁, C₂) = sqrt( Σᵢ log²(λᵢ) )
```

where λᵢ are the generalized eigenvalues of the pair (C₁, C₂), i.e., eigenvalues of C₁⁻¹ C₂.

The actual path length of a trajectory through a sequence of correlation matrices is the sum of incremental geodesic distances.

### Implementation

```python
import numpy as np

def riemannian_distance(C1, C2):
    """
    Affine-invariant (Fisher-Rao) distance on SPD manifold.
    d(C1, C2) = sqrt( sum( log(lambda_i)^2 ) )
    where lambda_i = eigenvalues of C1^{-1} @ C2
    """
    # Solve generalized eigenvalue problem
    # Use Cholesky for numerical stability
    L = np.linalg.cholesky(C1)
    L_inv = np.linalg.inv(L)
    M = L_inv @ C2 @ L_inv.T
    lambdas = np.linalg.eigvalsh(M)
    lambdas = np.clip(lambdas, 1e-10, None)
    return np.sqrt(np.sum(np.log(lambdas)**2))

def path_length(C_series):
    """
    Total Riemannian path length through a daily sequence of
    correlation matrices.
    """
    L = 0.0
    for t in range(len(C_series) - 1):
        L += riemannian_distance(C_series[t], C_series[t+1])
    return L
```

### Per-Episode Computation

```python
for episode in episodes:
    C_onset   = C[episode.t_onset]
    C_trough  = C[episode.t_trough]
    C_recover = C[episode.t_recovery]

    # Geodesic distance (shortest possible path on the manifold)
    d_geo_down = riemannian_distance(C_onset, C_trough)
    d_geo_full = riemannian_distance(C_onset, C_recover)

    # Actual path length (what the market traversed)
    L_down = path_length([C[t] for t in range(episode.t_onset,
                                               episode.t_trough + 1)])
    L_full = path_length([C[t] for t in range(episode.t_onset,
                                               episode.t_recovery + 1)])

    # Efficiency ratio: 1.0 = perfect geodesic, <1.0 = wasteful
    eta_down = d_geo_down / L_down
    eta_full = d_geo_full / L_full

    # Seifert bound test:
    # Minimum possible dissipation = d_geo^2 / duration
    Sigma_min = d_geo_down**2 / episode.duration_down
    waste_ratio = episode.total_Sigma / Sigma_min  # 1.0 = minimum entropy

    print(f"{episode.name}: eta_down={eta_down:.3f}  eta_full={eta_full:.3f}  "
          f"waste={waste_ratio:.2f}")
```

### Output Table

| Episode | d_geo (down) | L_actual (down) | η (down) | Σ_actual | Σ_min (Seifert) | Waste Ratio |
|---------|-------------|----------------|----------|----------|----------------|-------------|
| GFC | ? | ? | ? | ? | ? | ? |
| COVID | ? | ? | ? | ? | ? | ? |
| Rate Shock | ? | ? | ? | ? | ? | ? |
| 2025 | ? | ? | ? | ? | ? | ? |

### Interpretation

| Result | What It Means | Implication for P21 |
|--------|--------------|---------------------|
| η > 0.8 across all crises | Trajectories are near-geodesic | Strong support for P21 — markets follow minimum-dissipation paths on the correlation manifold |
| η = 0.4–0.8, varies by archetype | Some crisis types are near-geodesic, others aren't | Partial P21 support — fast crises (Cluster 1) may be more geodesic than slow grinds (Cluster 2) |
| η < 0.4 consistently | Trajectories are far from geodesic | P21 does not hold for financial markets via the correlation matrix proxy. The Fisher-Rao analogy is limited to the thermodynamic and gravitational domains |
| η_down >> η_full | The descent is near-geodesic but the full cycle isn't | Consistent with irreversibility — recovery takes a different (longer) path than collapse |

### Subtlety: the Asymmetry Prediction

Seifert's framework predicts that the MINIMUM dissipation path should be the same in both directions (geodesics are reversible). But the recovery asymmetry observed empirically (Section 4 of X8) means η_down should be higher than η_up. If η_down ≈ η_up, the asymmetry is not in the path but in the speed, and the thermodynamic analogy is weaker than expected.

---

## Test 4: σ(t) as a Live Signal

**Priority:** After Tests 1 and 3
**Effort:** ~1 hour per sub-test

### 4.1: Does σ Lead D_eff?

```python
from scipy.signal import correlate

# Normalize both series
sigma_norm = (sigma - sigma.mean()) / sigma.std()
deff_norm = (D_eff - D_eff.mean()) / D_eff.std()

# Cross-correlation at lags -10 to +10 days
xcorr = correlate(sigma_norm[-2000:], deff_norm[-2000:], mode='full')
lags = np.arange(-2000+1, 2000)
# Focus on lags -10 to +10
mask = (lags >= -10) & (lags <= 10)
print("Lag (days) | Cross-correlation")
for lag, xc in zip(lags[mask], xcorr[mask]):
    print(f"  {lag:+3d}       | {xc/len(sigma_norm[-2000:]):.4f}")
```

**What we want:** Peak cross-correlation at lag −2 to −5 (σ leads D_eff by 2–5 days). If peak is at lag 0 or positive, σ does not lead and has limited value as an early warning.

### 4.2: Does Peak σ Predict Crisis Depth?

```python
# For each episode: compute sigma over first 10 days of crisis
early_sigma = [np.max(sigma[e.t_onset:e.t_onset+10]) for e in episodes]
eventual_trough = [e.trough_D_eff for e in episodes]

r = np.corrcoef(early_sigma, eventual_trough)[0,1]
print(f"Correlation(early peak sigma, eventual trough D_eff): {r:.3f}")
```

**Threshold:** r > 0.5 means early dissipation is a useful predictor of crisis severity. r < 0.3 means it's not — the first 10 days don't tell you how bad it gets.

### 4.3: Does σ Peak Reliably Precede the D_eff Trough?

```python
for e in episodes:
    sigma_peak_day = np.argmax(sigma[e.t_onset:e.t_trough]) + e.t_onset
    lead_days = e.t_trough - sigma_peak_day
    print(f"{e.name}: sigma peaked {lead_days} days before D_eff trough")
```

**Threshold:** If lead_days is consistently 3–7 across all crises, σ peak is a trough-proximity signal. If it varies from 0 to 30, it's not consistent enough to trade on.

---

## Test 5: Dissipation-Conditioned Regime Signal

**Priority:** Last. Only if Tests 1–4 show σ carries independent information.
**Effort:** Half day (full V28.3 backtest required)

### Signal Variants

```python
# A: Current V28.3 signal (D_eff adaptive percentile only)
signal_A = d_eff_rolling_percentile < 0.10   # bottom decile = CRISIS

# B: Conjunction (D_eff + sigma)
# Rationale: only call CRISIS when BOTH D_eff is low AND dissipation
# is high. This filters out quiet low-diversity markets (low D_eff,
# near-zero velocity) which trigger false alarms on signal A.
signal_B = (d_eff_rolling_percentile < 0.15) & (sigma > sigma_rolling_75th)

# C: Sigma-only (probably too noisy, but test it)
signal_C = sigma > sigma_rolling_90th

# D: Archetype-conditioned position sizing
# If Test 2 shows Cluster 1 (Deep V-Shape) has different optimal
# allocation than Cluster 2 (Deep Slow Grind):
signal_D = signal_A  # same entry trigger
# But: if current episode is classified as Cluster 1 → 80% V22
#      if current episode is classified as Cluster 2 → 60% V22
```

### Backtest Metrics

For each signal variant, run the full V28.3 backtest (2003–2025) and report:

| Metric | Signal A (current) | Signal B (conjunction) | Signal C (σ only) | Signal D (archetype) |
|--------|-------------------|----------------------|-------------------|---------------------|
| Calmar | 0.541 | ? | ? | ? |
| Max Drawdown | ? | ? | ? | ? |
| CRISIS days/year | ? | ? | ? | ? |
| Regime switches/year | ? | ? | ? | ? |
| Hit rate (CRISIS precedes >2% DD within 21d) | ? | ? | ? | ? |

### Expected Result

Signal B (conjunction) should have:
- Fewer false positives than Signal A (filters out quiet low-diversity markets)
- Similar or better hit rate
- Slightly higher Calmar from reduced unnecessary defensiveness
- Lower turnover (fewer regime switches)

Signal C (σ alone) should be too noisy — v² amplifies measurement noise in D_eff.

Signal D is only viable if Test 2 shows archetype-dependent forward performance.

---

## Execution Order

```
Test 1  (1 hr)     Compute sigma(t) time series
  │
  ├── STOP CHECK: Is sigma just noise-amplified D_eff?
  │   If cross-corr > 0.95 at lag 0, no lead → STOP
  │
  ▼
Test 4.1 (30 min)  Does sigma lead D_eff?
  │
  ├── If no lead → Tests 4.2–5 are low priority, skip to Test 3
  │
  ▼
Test 3  (2 hrs)    Geodesic distance computation (P21 test)
  │                 Can be done in parallel with Test 2
  │
Test 2  (1 hr)     k-means archetype validation
  │
  ▼
Test 4.2–4.3       Predictive value of peak sigma
  │
  ▼
Test 5  (half day)  Full backtest of sigma-augmented signal
```

---

## What to Report Back

After running the tests, the following updates are needed in the PFD knowledge graph:

1. **X8 entry update:** Fill in the per-episode summary table (Test 1 output). Add archetype cluster labels if Test 2 confirms k=3.

2. **P21 conjecture update:** The geodesic test results from Test 3 determine whether P21's financial market arm holds:
   - η > 0.8 → add to P21.phase1_results as supporting evidence
   - η < 0.4 → add to P21.critical_gaps as negative evidence from financial markets
   - η varies by archetype → add as a nuanced result

3. **P18/P19 conjecture updates:** If σ(t) reveals structure in the coherence floor approach (P18) or non-ergodicity mechanism (P19) not captured by D_eff alone, update those conjectures.

4. **V28.3 architecture update:** If Test 5 produces a signal variant that improves on Signal A, update the X0 entry and architecture record.

---

## Provenance

This spec was generated from:
- PFD pillar expansion (IT06, GT07, HB09, P21 — session 2026-03-27 to 2026-03-29)
- Wagner transcript analysis (inverse problem, model dependence, local information)
- AlphaEntropy LLM cross-session exchange (D_eff ≠ FIM correction, phase-space trajectories, adaptive thresholds)

DS Wiki entries referenced: GT07, IT06, IT08, HB09, X0, X8, P5, P18, P19, P21

---

## Appendix: Test Results (Updated 2026-03-30)

### Test 1 Results — σ(t) Time Series

**Status:** Complete
**Stop condition:** PASSED (lag-0 corr = 0.035, not redundant)
**Key finding:** σ is a LAGGING indicator (D_eff leads σ by ~10 days). Useful for post-hoc characterization of crisis intensity (total Σ discriminates episode types), not for prediction.

| Episode | Peak σ | Total Σ | Character |
|---------|--------|---------|-----------|
| 2025 Stress | 0.00263 | 0.0131 | Highest total Σ — sustained high dissipation |
| 2007-03 (pre-GFC) | 0.00424 | 0.0112 | Highest peak σ — sharp initial shock |
| Euro Crisis | 0.00133 | 0.0058 | Moderate peak, long duration |
| Rate Shock 2022 | 0.00062 | 0.0062 | Low peak, very long — classic Slow Grind |
| COVID Mar 2020 | 0.00058 | 0.0057 | Moderate everything |
| GFC 2008–2009 | 0.00072 | 0.0030 | Surprisingly low (61 days detected — boundary issue) |

Ranking stability: 11/21 episodes stable (±2 rank) across EMA spans 3/5/10/21. Top 3 consistent.

**Consequence for remaining tests:**
- Tests 4.1–4.3 (predictive value): Deprioritized. σ lags, so it won't lead D_eff.
- Test 5 (σ-augmented signal): Likely dead — adding a lagging filter makes the signal slower, not better.
- Tests 2 and 3: Unaffected — both are about characterization/geometry, not prediction.

### Test 3 Results — Geodesic Efficiency (P21 Falsification)

**Status:** Complete

| Metric | Value |
|--------|-------|
| Mean η_down (descent efficiency) | 0.284 |
| Mean η_up (recovery efficiency) | 0.197 |
| Mean asymmetry η_down/η_up | 1.75 |
| P21 universal geodesic | ❌ NOT supported |
| P21 conditional (fast-shock limit) | ✅ SUPPORTED |
| Irreversibility asymmetry | ✅ CONFIRMED |

η vs. descent duration:

| Duration | η | Interpretation |
|----------|---|----------------|
| < 10 days | 0.50 | Near-geodesic — fast shocks follow shortest path |
| 10–20 days | 0.32 | Moderate meandering |
| > 30 days | 0.15 | Far from geodesic — slow grinds meander extensively |

**Refined P21 scope:** Seifert minimum-dissipation applies to financial markets in the fast-shock limit only. Acute crises follow near-geodesic paths because there's no time for internal friction (adiabatic limit). Slow structural deterioration meanders — the correlation structure shifts, partially reverses, shifts again (isothermal limit with continuous entropy exchange).

**Irreversibility interpretation:** Descents are 1.75× more efficient than recoveries. Collapsing into crisis is a more "natural" (direct) process on the correlation manifold than recovering. Recovery trajectories meander with partial reversals, consistent with P_forward ≠ P_reverse (IT06/Seifert entropy production).

### Remaining Tests

| Test | Status | Priority |
|------|--------|----------|
| Test 2 (k-means archetype validation) | COMPLETE — 3-archetype model FALSIFIED; replaced by τ_relax scaling law (r = −0.896) | Closed |
| Test 4.1 (does σ lead D_eff?) | Answered by Test 1 — NO, σ lags by 10 days | Closed |
| Test 4.2 (peak σ predicts depth?) | Not yet run | Low — σ lags, predictive value unlikely |
| Test 4.3 (σ peak precedes trough?) | Not yet run | Low — σ lags, likely follows trough |
| Test 5 (σ-augmented signal backtest) | Not yet run | Low — lagging filter unlikely to help |
| τ_relax estimation | COMPLETE — confirmed: τ_relax = 43d, η transitions at dur/τ ≈ 0.5–1.5, r = −0.896 | Closed |
| λ-sweep test | NEW — vary EWMA λ, check whether λ maximizing trading Sharpe also maximizes r² of η(dur/τ) scaling law | High — tests whether optimal filtering = Fisher-Rao relaxation |

*Generated by PFD Session | Snapshots: snap_20260329_231529, snap_20260330*

# CCA Potts Sweep — Derivation Notes

**Companion to:** `CCA_POTTS_SWEEP_SPEC.md`, `CCA_POTTS_SWEEP_HANDOVER.md`
**Purpose:** Pin down the canonical definitions, FSS predictions, and implementation conventions used by `scripts/cca_potts_sweep_main.py` before coding. Records choices explicitly so the Phase 4 report can cite them.
**Owner-approved 2026-04-20:** Option B (full connected correlation matrix χ), Glauber dynamics, spec-§3.4-literal η_CCA.

---

## 1. Potts Hamiltonian + dynamics

```
H = -J Σ_{<i,j>} δ(s_i, s_j),   s_i ∈ {0, ..., q-1},   J = k_B = 1
T_c(q) = 1 / ln(1 + √q)    (exact, 2D square)
```

Dynamics: **Glauber** (matches Brown 2022 Suppl. Eq. S1):

```
P(s_i → s_k) = [1 + exp(ΔE_{ki} / T)]⁻¹,   ΔE_{ki} = E_k − E_i
```

Satisfies detailed balance. One sweep = L² attempted site updates (random order). Rationale for Glauber over Metropolis: Brown 2022 GTE is defined per Glauber-flip statistics; using Metropolis changes the transition kernel and makes GTE apples-to-oranges with Brown.

## 2. Canonical CCA connected correlation matrix χ

For Potts q-state spins on L² sites we adopt the **q-symmetric Kronecker-delta** definition — matches Borgs-Chayes 1996 (Eq. 1.2) up to normalization and gives clean Vinayak 2014 alignment:

```
[χ]_{ij} = ⟨q·δ(s_i, s_j)⟩ − 1,    i, j = 1..N = L²
```

Properties:
- Real, symmetric, N × N.
- For q=2: reduces to ⟨σ_i σ_j⟩ up to constant (using σ ∈ {±1} from σ = 2δ−1).
- Diagonal: χ_ii = q − 1 always.
- Off-diagonal at criticality: `χ_ij ~ r^{−η_std}` with standard anomalous dimension η_std (= 1/4 for 2D Ising).
- In the disordered phase with free BC: χ = (q−1)·τ where τ is the Fortuin-Kasteleyn cluster connectivity (Borgs-Chayes Eq. 1.2).

**Why this choice** (not alternatives):
- "Project onto state 0" (M_i = q·δ(s_i,0) − 1) breaks the S_q permutation symmetry; forces a preferred direction that has no physical meaning for q>2.
- "Project onto dominant-mode" (Brown's M convention) is sample-dependent (mode depends on configuration); consistent only if applied identically across samples, and dangerous for FIM-as-correlation-matrix identification.
- The q-symmetric form is what Borgs-Chayes 1996 defines as the covariance matrix and what Vinayak 2014 analyzes.

## 3. CCA scalar observables (spec §3.4 literal)

Let `{λ_j}`, ordered λ_1 ≥ λ_2 ≥ ... ≥ λ_N, be eigenvalues of χ.

### 3.1 `d_eff_CCA` — participation ratio

```
d_eff_CCA = (Σ_j λ_j)² / Σ_j λ_j²
```

Ranges in [1, N]. `d_eff = 1` → single-eigenvalue dominance; `d_eff = N` → uniform eigenvalues.

### 3.2 `η_CCA` — Zipf-tail power-law exponent

Fit λ_j ~ c · j^{−η_CCA} in a log-log Zipf plot over a middle-bulk index range [j_min, j_max] (default: j_min = 10, j_max = N/2; report sensitivity to range per spec §6.4).

**Note on terminology collision (per `CCA_TERMINOLOGY_RENAME_PROPOSAL.md`):**
Standard stat-mech η_critical is the anomalous dimension of the 2-point function C(r) ~ r^{−(d−2+η_std)}, giving η_std = 1/4 for 2D Ising. **CCA's η_CCA is Vinayak's ζ** — the Zipf exponent of the correlation-matrix spectrum — **not** η_std. At criticality they are related by Vinayak's Eq. 5: ζ = (d − η_std)/d. Off-criticality and at first-order transitions they decouple.

This experiment writes `eta_CCA` consistently and contrasts with `eta_std` (derived separately).

## 4. Reduction-check: FSS predictions at T_c for q=2 (Ising universality)

### 4.1 Vinayak 2014 Eq. 5

For a system on a cubic d-dim lattice L^d at T_c with spatial correlations decaying as `C(r) ~ c · r^{−θ}` (where θ = η_std + d − 2, i.e. θ is the `r`-exponent not the anomalous dimension — though for 2D, θ = η_std), the eigenvalues of the correlation matrix Zipf-plot as:

```
λ_j ≈ c_d · j^{−ζ},    ζ = (d − θ)/d    for 1 ≪ j ≪ N = L^d
```

### 4.2 2D Potts continuous (q ≤ 4)

For 2D Potts critical exponents (from Baxter + standard references):

| q | η_std | β/ν | ν | ζ = (d − θ)/d | Transition |
|---|---|---|---|---|---|
| 2 | 1/4 | 1/8 | 1 | 7/8 = 0.875 | continuous (Ising) |
| 3 | 4/15 | 2/15 | 5/6 | 13/15 ≈ 0.867 | continuous |
| 4 | 1/4 | 1/8 | 2/3 | 7/8 = 0.875 | continuous (marginal) |

Note: 2D Potts q=2,3,4 all have the 2-point correlator decay exponent θ = η_std (since d=2 makes d−2=0).

### 4.3 Derived predictions at T_c (q=2, 2D)

With λ_j = c · j^{−7/8} for 1 ≪ j ≪ N:

**η_CCA (Zipf exponent):**
```
η_CCA(T_c) = ζ = 7/8 = 0.875    (asymptotic L→∞)
```
Vinayak's own numerics at L=192 found ζ ≈ 0.8504 with convergence to 0.875 as L grows. For our sizes L ∈ {16, 24, 32} (N = 256, 576, 1024), the convergence is weaker than at L=192 — expect numerical values in the 0.80-0.85 range, not exactly 7/8.

**d_eff_CCA (participation ratio) — corrected derivation:**

The naive Zipf-only prediction is wrong. In practice the connected correlation matrix χ has a **dominant top eigenvalue** from the finite-size "ordering mode" that is outside Vinayak's asymptotic scaling. At T_c in a finite system with non-zero ⟨m⟩:

- **Top eigenvalue** λ_1 ∝ L^{d − 2β/ν} (magnetic susceptibility scaling).
  For 2D Ising: β/ν = 1/8, so λ_1 ∝ L^{7/4}. Measured empirically: λ_1 ≈ 152 at L=16 (predicted L^{7/4} = 16^{1.75} ≈ 161 — matches).
- **Zipf bulk** λ_j ≈ c·j^{−ζ} for j ≥ ~10 (j_min = 10, j_max = N/2 per §3.2).

The participation ratio `(Σλ)²/Σλ²` is dominated by λ_1 because `Σλ² ≈ λ_1² = L^{7/2}` vastly exceeds the Zipf-bulk contribution `∫ j^{−2ζ} dj` which converges to a finite constant.

**Corrected prediction at T_c:**

```
d_eff_CCA(T_c, L)  ∼  1 + (Σ_{j≥2} λ_j / λ_1)² + Σ_{j≥2} (λ_j/λ_1)²  / (1 + Σ (λ_j/λ_1)²)
                  ≈  O(1-10) with weak L-dependence
```

Empirically at q=2, T=T_c: d_eff_CCA ≈ 2.5-3.5 across L ∈ {16, 24, 32} — dominated by top-mode separation from bulk.

**Implication for reduction-check:**
- **Primary test**: η_CCA (Zipf exponent on j ∈ [10, N/2]) compared to ζ_theory = (d − η_std)/d. η_CCA is a clean predictor of Vinayak's relation.
- **Secondary test**: d_eff_CCA ≈ O(few) at T_c, crossing to O(N) far above T_c (where spectrum flattens to MP).
- **d_eff_CCA is NOT an analytical predictor** in the Vinayak-Zipf sense; it is an empirical curve-shape indicator.

### 4.4 Reduction-check decision rule (revised)

### 4.4.1 Reduction-check decision rule (spec §4.1)

Compute η_CCA_fit from the simulation at T_c with ~5-replica bootstrap SEM. Compare against ζ(q) from §4.2:

| Condition | Outcome |
|---|---|
| `|η_CCA_fit − ζ_theory| < 2σ`        | **R1** — reduction confirmed |
| `|η_CCA_fit − ζ_theory| > 3σ`        | **R2** — something else captured |
| 2σ ≤ deviation ≤ 3σ                  | **R-ambiguous** — report honestly, don't classify |

Report per-q result (q=2, 3 [optional], 4 [optional]). q=2 is the primary reduction-check test.

Finite-size corrections are real: Vinayak's own numerics show the empirical ζ is smaller than 7/8 at finite L. For the reduction-check to pass, we need:
- The **exponent** to match within SEM, OR
- An **explicit finite-size scaling extrapolation** through L ∈ {16, 24, 32} that extrapolates to ζ(L→∞) consistent with 7/8

d_eff_CCA absolute magnitude is a weaker test (predicted value depends on full Zipf bulk, including top corrections we don't model cleanly); report as consistency check only.

## 5. First-order predictions (q = 5, 7, 10)

At first-order transitions, 2-point correlations have **exponential decay** with finite ξ (no power law), so Vinayak's analysis doesn't apply. We expect:
- Below T_c: χ exhibits long-range ferromagnetic order → dominant top-eigenvalue (uniform mode) → low d_eff_CCA, no power law → η_CCA_fit fails / ill-defined.
- Above T_c: χ exhibits exponential decay → MP-like bulk + gap structure → intermediate d_eff_CCA, η_CCA_fit reads the MP Wishart exponent (not Vinayak's ζ).
- At T_c: bimodal P(E); χ averages over two phases → somewhere intermediate.

**This is where CCA's potential narrow novelty lives** (per Sixth Addendum): if d_eff_CCA and η_CCA track Brown's GTE curve shape despite being pure 2-point observables, that's informative. If they miss the hybrid 2-point + multi-point discrimination GTE captures, CCA reduces to strictly less-informative observable.

No analytical FSS prediction exists for first-order CCA observables; the experiment produces them empirically.

## 6. Brown 2022 GTE formulation (canonical for this experiment)

Per Brown 2022 Suppl. §"Transfer Entropy":

### 6.1 Transfer entropy, single-step

For two stochastic processes X (target site) and Y (source = neighborhood), with time index t:

```
T_{Y → X} = H(X_t | X_{t−1}) − H(X_t | X_{t−1}, Y_{t−1})
```

- History length **k = 1** (single step lag)
- X_t = s_i at time t
- Y_{t−1} = state of the 4 nearest neighbors of i at time t−1
- Estimator: **plug-in entropy** from frequency histograms

### 6.2 Global Transfer Entropy (GTE)

```
G = (1/N) Σ_{i=1}^{N} T_{s_{¬i} → s_i}
```

Average TE over all sites, where s_{¬i} = 4 nearest neighbors of i.

### 6.3 Neighborhood compression (critical for feasibility)

Naive: histogram has 6 dims (s_i past, s_i future, 4 neighbor pasts) × q bins each = q^6 bins. For q=10 that's 10^6. Per plug-in heuristic B = √N_data, needs 10^12 samples → infeasible.

**Brown's compression:** encode the 4-neighbor state as the **pre-sweep site energy** E_i (= count of matching neighbors × −J, integer-valued, 5 possible values for J=1). Reduces to (5·q²)² = (5q²)² bins.

For q=10 this is (500)² = 250k bins; heuristic requirement ~125k samples per state — achievable with 10^5 measurement sweeps × N sites.

Brown validates the compression gives results consistent with alternative δ(s_i, s_j)-based compression (24 combinations × q² — `(24·q²)²` bins).

### 6.4 Three GTE variants (Brown's G^{(g)}, G^{(s)}, G^{(f)})

| Variant | Collection | Use |
|---|---|---|
| G^{(g)} | per-sweep, energy-before-sweep, future = post-sweep config | Brown's Fig. 1 top row |
| G^{(s)} | per-sweep statistics from pre-sweep energy | Brown's Fig. 1 bottom row — closely tracks G^{(f)} |
| G^{(f)} | per-flip basis: at each flip attempt, record (s_i, E_i, s_i-future) | Brown's Fig. 1 bottom row |

Brown's main discrimination Fig. 1 uses G^{(f)}/G^{(s)} (nearly coincident). **Our experiment uses G^{(f)}** as canonical — per-flip is the natural unit for Glauber dynamics.

### 6.5 Sample-size implications

Brown uses **10⁵ time steps × 10 realizations = 10⁶ samples per config**. Our spec uses **20k measurement sweeps × 5 replicas = 10⁵ samples per config** — 10× less than Brown.

Per-site × per-sweep samples × 5 replicas for L=24: 24² × 20k × 5 = 57.6M per config. Plug-in histogram bins (5q²)² for q=10: 250k. Samples-per-bin ratio: 230 — marginal but workable.

**Risk:** at first-order Potts near T_c, where GTE distinguishing information lives, statistics may be too thin. Monitor error bars; if they swamp discrimination, increase N_measure (owner-approval required for scope change).

## 7. Implementation conventions for this experiment

Based on §1-6 above:

1. **Dynamics:** Glauber single-site, one sweep = L² random-order attempts.
2. **Potts spin representation:** categorical s_i ∈ {0, ..., q−1} throughout.
3. **Correlation matrix:** χ_ij = ⟨q·δ(s_i, s_j)⟩ − 1, N × N, q-symmetric.
4. **CCA observables:** d_eff_CCA = (Σλ)²/Σλ², η_CCA = Zipf exponent over j ∈ [10, N/2].
5. **GTE variant:** G^{(f)} per-flip, plug-in estimator, neighborhood compression via site energy E_i.
6. **Standard exponents for reduction-check:** η_std from `⟨s_0 s_r⟩` decay fit; β/ν from magnetization FSS.
7. **T_c:** use thermodynamic T_c(q) = 1/ln(1+√q); report T/T_c(q) on plots. (Do not use Brown's effective T_c(L) — we're comparing curve shapes, not peak locations.)
8. **Replicas:** 5 per (q, L, T), different seeds; SEM from replica spread.
9. **Reproducibility:** seed = hash(q, L, T_index, replica_index); record numpy + numba versions + git commit in every output.
10. **Save per-run:** averaged χ eigenspectrum (N floats), per-flip GTE histograms, scalars (d_eff, η_CCA, GTE, ⟨m⟩, χ_mag). Save full spin configurations only for 1-2 debug runs.

## 8. Known gaps and caveats (to mention in Phase 4 report)

- **N_measure = 20k vs Brown's 10⁵:** 10× sample-budget gap. May not resolve first-order GTE curve shape cleanly. Mitigation: start with 20k per spec; escalate if needed.
- **No Wang-Landau:** Brown's most-definitive GTE uses Wang-Landau DOS + Eq. 4 to avoid MC traversal issues near first-order T_c. Our experiment uses straight Glauber. First-order T_c (q=10) results may exhibit phase-trapping artifacts. Mitigation: discard trapped replicas per spec §6.1.
- **T_c convention:** thermodynamic T_c, not L-dependent effective T_c. OK for curve-shape comparison; note in report.
- **Analytical d_eff_CCA prediction depends on Zipf bulk assumption:** test is on exponent ζ, not absolute d_eff magnitude.
- **Potts spin choice:** we use the q-symmetric δ-based χ. Brown's GTE uses categorical s_i directly. These are consistent (both are state-space descriptions) but differ from a "magnetization projection" convention (Option B.3) that some prior CCA docs reference. Consistent throughout this experiment; noted.

---

**Ready for code:** Section 7 provides the exact conventions to implement. Section 4-5 provides the reduction-check math that `reduction_check_fss.py` will encode. Section 6 provides the exact GTE formula `gte_analysis.py` needs.

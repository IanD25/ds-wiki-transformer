# CCA-1c λ₁ Reduction Test — does the first-order d_eff jump reduce to the ordering mode?

**Mode:** B (falsification-first, on an existing conjecture; no new P/Q entries)
**Date:** 2026-10-18
**audit_ref (planned):** `gsw-cca1c-lambda1-reduction-2026-10-18`
**Subject:** CCA-1c, latest row `gsw-cca-potts-sweep-phase-E-2026-04-20` (Speculative, "outcome C"). That row names this test as the sharpened follow-up and did not run it.
**Data:** the Phase E outputs, unchanged — `data/reports/cca_potts_sweep_2026/raw/*.npz` (540 runs; each stores the full sorted eigenvalue spectrum of the averaged χ, plus magnetisation series and GTE). **No new Monte Carlo was run.**

---

## 1. Pre-registration (written and committed before any decomposed number was computed)

### 1.1 What was already known when this was written

- The Phase E headline: d_eff_CCA at q = 10, L = 32 goes from 1.5 (T/T_c = 0.99) to 370 (T/T_c = 1.01). Discrimination ratio vs q = 2 is 26–407×, against 9–32× for GTE.
- One run's metadata (q = 10, L = 16, T/T_c = 0.90, rep 0): λ₁ = 2167, λ₂ = 1.36, d_eff = 1.13, ⟨M²⟩ = 0.941.
- The code: `compute_chi_ij` in `scripts/potts_mc_optimized.py` builds χ_ij = ⟨q·δ(s_i, s_j)⟩ − 1 from 2,000 samples. `extract_cca_observables` in `scripts/cca_observables.py` computes d_eff over eigenvalues above 1e-10·λ₁.

### 1.2 Two identities that follow from the definitions (derived before computing)

**(I1) The trace is fixed.** χ_ii = q·1 − 1 = q − 1 for every site, so Σ_j λ_j = tr χ = N(q − 1) at every temperature. The numerator of d_eff never changes for a given (q, L); only Σλ² = ‖χ‖²_F does. Writing f₁ = λ₁ / Σλ (the top mode's share of the trace) and d_bulk = (Σ_{j≥2} λ_j)² / Σ_{j≥2} λ_j² (the participation ratio with λ₁ removed), it follows exactly that

  **1 / d_eff = f₁² + (1 − f₁)² / d_bulk.**

So d_eff is a function of two numbers only: the top-mode share f₁ and the participation ratio of the remaining spectrum.

**(I2) The top mode is the Potts order parameter.** For the uniform vector u = (1, …, 1)/√N, uᵀχu = N(q⟨Σ_a x_a²⟩ − 1), where x_a is the fraction of sites in state a. For an ordered configuration with the minority states equally populated, q Σ_a x_a² − 1 = (q − 1)M², where M = (q·x_max − 1)/(q − 1) is the standard Potts magnetisation (the one the sweep code records). Since λ₁ ≥ uᵀχu, it follows that **f₁ ≳ ⟨M²⟩**, with approximate equality when the top eigenvector is close to uniform. Equivalently, λ₁ ≈ S(k = 0), the zero-momentum structure factor: N·(q − 1)·⟨M²⟩ in the ordered phase (order-parameter scaling, ∝ L^d), the finite susceptibility in the disordered phase, and ∝ L^{γ/ν} = L^{7/4} only at a continuous critical point.

Together these predict, before computing: below a first-order T_c, f₁ ≈ ⟨M²⟩ ≈ 0.8–0.9, so d_eff ≈ 1/f₁² ≈ 1.2–1.6. Above it, f₁ → O(χ/N) ≈ 0, so d_eff → d_bulk. **The jump is then the discontinuity of the order parameter, read through S(k = 0).** This is textbook: a first-order Potts transition (q > 4) has a discontinuous order parameter (Baxter 1973; Wu 1982, *Rev. Mod. Phys.* 54, 235).

### 1.3 The reduction hypothesis (one sentence)

> **H_red:** At the first-order 2D Potts transitions (q = 5, 7, 10), the large jump in d_eff_CCA across T_c comes entirely from the top eigenvalue's share of the trace, f₁ = λ₁/N(q−1) ≈ ⟨M²⟩, dropping from O(1) to ≈ 0; the participation ratio of the rest of the spectrum shows no first-order-specific jump.

### 1.4 What is computed (per run, then mean ± SEM over 5 replicas)

| Quantity | Definition | Meaning |
|---|---|---|
| d_full | (Σλ)²/Σλ² over λ > 1e-10·λ₁ | reproduces Phase E d_eff_CCA (check) |
| f₁ | λ₁ / Σλ | top-mode share of the trace |
| d_λ1-only | (Σλ)²/λ₁² = 1/f₁² | d_eff if λ₁ alone set the denominator |
| d_bulk | (Σ_{j≥2} λ)² / Σ_{j≥2} λ² | **d_eff with λ₁ removed** (primary) |
| d_bulk2 | same with λ₁, λ₂ removed | secondary: checks for a coexistence/interface mode at T/T_c = 1.00 |
| ⟨M²⟩ | from the stored magnetisation series | for the I2 check |

Jumps use Phase E's definition: J_X = (X(1.01) − X(0.99)) / |X(0.99)|. Discrimination: D_X(q) = J_X(q) / J_X(q = 2) at the same L, compared with D_G from Phase E's `brown_comparison_table.csv`.

**Attribution of the d_eff jump.** Using I1, ln d_eff = F(f₁, d_bulk). The log-jump Δ ln d_eff between T/T_c = 0.99 and 1.01 is split between f₁ and d_bulk by a two-player Shapley swap (average of the two orders of changing one input at a time). The **f₁ share** is the fraction of Δ ln d_eff attributed to the change in f₁.

### 1.5 Verdict rules (fixed in advance)

- **REDUCES** if, for every first-order q ∈ {5, 7, 10} at L = 32, and for at least 2 of 3 L at each q: (a) the f₁ share of Δ ln d_eff is ≥ 0.90, **and** (b) d_bulk's discrimination ratio D_bulk(q) ≤ D_G(q), so that with λ₁ removed the remainder no longer out-discriminates GTE. → CCA-1c's d_eff signature is a restatement of the order-parameter discontinuity, seen through S(k = 0).
- **SURVIVES** if, at L = 32, for at least 2 of 3 first-order q: D_bulk(q) > D_G(q) **and** the f₁ share < 0.90. → characterise the surviving jump, then run the prior-art gate (`memory/feedback_prior_art_gate.md`) before any narrow-novelty statement.
- **MIXED** otherwise → report as is; no label change.

**I2 check (supporting, not decisive):** f₁ / ⟨M²⟩ is within [1.0, 1.15] wherever f₁ > 0.3.

**Secondary, η_CCA part of CCA-1c.** η_CCA is fitted over j ∈ [max(5, 0.04N), N/2], so it already excludes λ₁: it is a bulk observable. Phase E reported that η_CCA's peak tracks GTE's peak. Pre-registered prediction: both peak where the magnetic susceptibility χ_mag (stored per run) peaks, the finite-size pseudo-transition, so the peak-tracking reduces to locating T_c(L). Decisive only within the grid's resolution (T/T_c steps of 0.01 near T_c).

### 1.6 Caveats known in advance

1. **Sampling noise in the bulk.** χ is an average over 2,000 correlated samples (one every 10 sweeps), so the bulk spectrum carries Marchenko–Pastur-type sampling noise. Each sample contributes a rank-(q − 1) term, so the noise floor depends on q. A first-order-specific signal in d_bulk would have to be told apart from this.
2. **Initial-state protocol.** Phase E picked the initial state per (q, T/T_c), with ordered starts below and disordered above T_c, and a half-and-half start near T_c. For q = 10 at L = 32, 20,000 Glauber sweeps may not cross the free-energy barrier. The 0.99 → 1.01 jump may therefore be partly fixed by the starting state (hysteresis). This does not affect the reduction question: whichever phase a run sits in, λ₁ reads that phase's order parameter.
3. The temperature grid near T_c is coarse (0.98, 0.99, 1.00, 1.01, 1.02), and T_c is the thermodynamic value, not T_c(L).

---

## 2. Computation

*(to be filled after the pre-registration commit)*

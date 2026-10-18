# CCA-1c λ₁ Reduction Test — does the first-order d_eff jump reduce to the ordering mode?

**Mode:** B (falsification-first, on an existing conjecture; no new P/Q entries)
**Date:** 2026-10-18
**audit_ref (planned):** `gsw-cca1c-lambda1-reduction-2026-10-18`
**Subject:** CCA-1c, latest row `gsw-cca-potts-sweep-phase-E-2026-04-20` (Speculative, "outcome C"). That row names this test as the sharpened follow-up and did not run it.
**Result (added after computing; §1 is unchanged from commit `d00e5fe`):** **REDUCES.** The first-order d_eff jump is the Potts order-parameter jump read through λ₁ ≈ N(q−1)⟨M²⟩. With λ₁ removed, the rest of the spectrum's participation ratio *falls* across T_c rather than jumps. CCA-1c: Speculative → **Retired (Folded)**. See §3.
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

*Pre-registration committed as `d00e5fe` before this section was written.*

**Script:** [`scripts/cca1c_lambda1_reduction.py`](../../scripts/cca1c_lambda1_reduction.py). It reads the 540 Phase E `.npz` files and writes [`data/reports/cca1c_lambda1_reduction_2026_10/`](../../data/reports/cca1c_lambda1_reduction_2026_10/): `per_run.csv`, `by_config.csv` (108 configurations, mean ± SEM over 5 replicas), `jumps.csv`, and `summary.json`.

**Sanity checks (all pass):**
- The recomputed d_full matches Phase E's stored d_eff_CCA exactly in all 540 runs (maximum relative difference 0).
- Σλ / N(q − 1) lies in [1 − 1.3·10⁻¹⁵, 1 + 1·10⁻¹⁵] in every run (identity I1).
- The identity 1/d_full = f₁² + (1 − f₁)²/d_bulk holds to 8·10⁻¹⁶.
- Initial state: every q ≥ 5 configuration at T/T_c = 0.98–1.01 used the same `half_half` start. The 0.99 → 1.01 jump is therefore not caused by switching between ordered and disordered starts (resolves caveat 1.6.2 for this window).

### 2.1 The jump, decomposed (L = 32; mean ± SEM, 5 replicas)

| q | d_full 0.99 → 1.01 | 1/f₁² at 0.99 | f₁ 0.99 → 1.01 | ⟨M²⟩ at 0.99 | d_bulk 0.99 → 1.01 | f₁ share of Δ ln d | D_full | D_bulk | D_G |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 3.61 ± 0.21 → 5.77 ± 0.48 | 3.63 | 0.528 → 0.418 | 0.527 | 191 ± 24 → 157 ± 17 | 1.00 | 1 | 1 | 1 |
| 5 | 2.44 ± 0.06 → 40.9 ± 14 | 2.45 | 0.640 → 0.171 | 0.638 | 347 ± 23 → 165 ± 8 | 1.01 | 26.3 | 2.9 | 8.6 |
| 7 | 1.85 ± 0.04 → 189 ± 10 | 1.85 | 0.737 → 0.038 | 0.736 | 493 ± 39 → 237 ± 8 | 1.05 | 169 | 2.9 | 17.4 |
| 10 | 1.52 ± 0.01 → 371 ± 11 | 1.52 | 0.812 → 0.016 | 0.811 | 605 ± 4 → 398 ± 7 | 1.03 | 407 | 1.9 | 31.9 |

L = 16 and 24 are the same in every respect: f₁ share 1.003–1.032, D_bulk 1.8–4.6, against D_G 9.0–61.0 (full table in `jumps.csv`).

How to read it:
- **Below T_c, d_eff is 1/f₁².** At T/T_c = 0.99, 1/f₁² equals d_full to within 1% in every (q, L), and f₁ equals ⟨M²⟩ to within 0.5%. The denominator Σλ² is λ₁² to that accuracy.
- **Above T_c, d_eff is d_bulk.** f₁ falls to 0.02–0.17, so d_full approaches the participation ratio of the remaining spectrum.
- **The f₁ share exceeds 1 in every configuration.** d_bulk moves *against* the jump: it falls by a factor of 1.5–2.1 across T_c at every q, including q = 2 (−7% to −18%). The whole jump, and more, is the top mode's collapse.
- **With λ₁ removed, nothing jumps upward.** D_bulk is a ratio of two *decreases*, and is at most 4.6 against GTE's 8.6–61. Phase E's "9–400× beyond GTE" belongs entirely to f₁.

### 2.2 Identity I2: λ₁ is the order parameter

Where f₁ > 0.3 (70 configurations), f₁ / ⟨M²⟩ lies in [1.0001, 1.17], with 69 of 70 inside the pre-registered [1.0, 1.15]. The one miss is q = 10, L = 24, T/T_c = 1.00. At coexistence, replicas mix ordered and disordered states, so the equal-minority approximation fails. The rigorous bound λ₁ ≥ uᵀχu = N(q⟨Σ_a x_a²⟩ − 1) still holds there. Below T_c, λ₁ ∝ N·(q − 1)·⟨M²⟩: order-parameter scaling (∝ L^d at fixed ⟨M²⟩), not L^{γ/ν}. At q = 2 near T_c the same identity holds (f₁ = 0.528 vs ⟨M²⟩ = 0.527), and there ⟨M²⟩ itself carries the critical L^{−2β/ν} finite-size scaling.

### 2.3 λ₂ and the coexistence point (secondary)

At T/T_c = 1.00, λ₂ rises (q = 5/7/10 at L = 32: 69 / 103 / 54, against 14–34 at 0.98–0.99). This is consistent with an interface (slab) mode at phase coexistence. It is two orders of magnitude below λ₁ and changes nothing. d_bulk2 (λ₁ and λ₂ removed) behaves like d_bulk throughout.

### 2.4 Secondary: η_CCA peak location (pre-registered prediction NOT confirmed at grid resolution)

| q | L | peak η_CCA | peak GTE | peak χ_mag |
|---|---|---|---|---|
| 5 | 16 / 24 / 32 | 1.05 / 1.02 / 1.02 | 1.05 / 1.02 / 1.02 | 1.02 / 1.01 / 1.01 |
| 7 | 16 / 24 / 32 | 1.02 / 1.02 / 1.01 | 1.02 / 1.02 / 1.01 | 1.01 / 1.01 / 1.00 |
| 10 | 16 / 24 / 32 | 1.02 / 1.01 / 1.01 | 1.02 / 1.01 / 1.01 | 1.01 / 1.00 / 1.00 |
| 2 | 16 / 24 / 32 | 1.10 / 1.10 / 1.10 | 1.05 / 1.05 / 1.05 | 1.05 / 1.05 / 1.05 |

At first order, η_CCA and GTE share a peak in all 9 configurations (Phase E reported 8 of 9 on its own table). The prediction that both peak at the χ_mag peak fails: they sit **one grid step (0.01) above it**, every time. On a 0.01 grid this is a one-bin offset. It is consistent with both being disordered-side quantities that peak just above the coexistence point, which is Brown 2022's own description of GTE (STAT6). It is not resolved here. It does not bear on the d_eff verdict, and no claim is made from it.

---

## 3. Verdict

**REDUCES**, by the pre-registered rule (`summary.json`: `reduces_all_first_order_L32 = true`, `reduces_per_q_2of3_L = true`, `survives_2of3_L32 = false`).

> **Plain statement:** The jump in d_eff_CCA at first-order 2D Potts transitions is the jump in the Potts order parameter. Because tr χ = N(q − 1) is fixed, d_eff = 1/[f₁² + (1 − f₁)²/d_bulk]. The top eigenvalue's share f₁ equals ⟨M²⟩, which is O(1) below T_c and ≈ 0 above. The rest of the spectrum's participation ratio does not jump; it falls slightly.

- **Triviality check (charter rule 2):** yes, this is a 5-minute derivation. The trace identity follows from χ_ii = q − 1. That λ₁ ≈ S(k = 0) = N(q − 1)⟨M²⟩ follows from the Rayleigh quotient on the uniform vector. The discontinuity of the order parameter at q > 4 is textbook: Wu 1982, *Rev. Mod. Phys.* 54, 235 (doi:10.1103/RevModPhys.54.235; bibliographic record verified 2026-10-18); Baxter's 1973 exact solution (latent heat) and Baxter's 1982 magnetisation result. Phase E's "dramatic discontinuous change in effective rank" is that discontinuity read through 1/⟨M²⟩².
- **Framing check (rule 3):** in the standard framing, d_eff is a monotone function of ⟨M²⟩ in the ordered phase. Any order-parameter-sensitive scalar "out-discriminates" GTE on jump magnitude, because GTE is not an order parameter. The 9–400× ratio is a comparison between an order parameter and a non-order-parameter, not evidence of extra content.
- **Erratum to §1.2:** the pre-registration attributed the discontinuous order parameter to "Baxter 1973". Citing papers attribute Baxter 1973 to the free energy and latent heat at T_c, and the magnetisation at T_c to Baxter 1982. Wu 1982 (verified) is the citation used in the calibration row. The J. Phys. venues for both Baxter papers were not checked.
- **Prior-art gate:** not triggered. Nothing survived that would need a novelty statement. The restatement verdict cites a textbook result, not a narrow-novel claim.

### 3.1 What survives, and what does not

| Part of CCA-1c (Phase E outcome C) | After this test |
|---|---|
| d_eff_CCA jump magnitude, "9–400× beyond GTE" | **Restatement:** Potts order-parameter discontinuity via S(k = 0). Wu 1982. |
| d_eff_CCA "peak" at T/T_c = 1.10 (range edge) | Not a peak: d_eff → d_bulk → N (the white-noise limit) as correlations shorten. A monotone approach, by I1. |
| η_CCA peak tracks GTE peak | Co-location with Brown 2022's GTE peak (STAT6). By Phase E's own account a re-expression of Brown's signature, not a distinct discriminator. One-bin offset from χ_mag left unresolved (§2.4). |
| q = 2 continuous η_CCA reduction (Vinayak) | Unchanged (Phase E R1 soft pass). |

Nothing remains that is distinctive to CCA. Under the owner's Folded-vs-Falsified rule (`memory/feedback_diagnostic_labels.md`), the literature answers CCA-1c's question the way CCA-1c did: yes, the observable discriminates, through the order-parameter jump. So CCA-1c closes as **Retired — Folded**, not Falsified.

### 3.2 Calibration

- **CCA-1c:** Speculative → **Retired**. "Folded: d_eff jump = Potts order-parameter discontinuity read through λ₁ = S(k=0) ≈ N(q−1)⟨M²⟩ (Wu 1982, RMP 54:235)". Pattern tags: `restatement-in-new-vocabulary`, `answer-forced-by-definition` (the trace identity fixes d_eff as a function of f₁ and d_bulk). audit_ref `gsw-cca1c-lambda1-reduction-2026-10-18`.
- **STAT3:** label unchanged (Supported). This appends a correction to the Phase E row, which counted "d_eff_CCA jump magnitudes exceed GTE by 9–400×" as strengthening. That strengthening is withdrawn. Whether STAT3's Supported label stands on its remaining basis is the owner's call.
- **Wiki text:** `gloss_phase_transition` "Why this disambig exists" gets a dated qualifier after the Phase E sentence (migration `scripts/migrations/cca1c_lambda1_reduction_2026_10_18.py`, dry-run first).
- **QR-007** (Questions Raised Log) said "if it reduces, QR-007 folds". It reduces; the log is updated.

### 3.3 Limitations

1. The verdict is about **this observable on this data** (2D Potts, L ≤ 32, Glauber, 2,000 samples per run). The identities I1 and I2 do not depend on L, so larger L cannot change the reduction. They depend only on χ_ii = q − 1 and on the uniform mode being the order-parameter mode.
2. d_bulk carries finite-sample (Marchenko–Pastur-type) noise, which depends on q (caveat 1.6.1). This could bias the *size* of the small d_bulk decrease. It cannot produce the missing upward jump.
3. The small, q-dependent d_bulk decrease (|J| 0.29–0.52 at first order vs 0.07–0.19 at q = 2) is not characterised. It runs opposite to the claimed signature and below GTE's discrimination at every (q, L). It is plausibly the standard ordered-vs-disordered correlation-length difference at the transition, but that was not tested and no claim is made.
4. The η_CCA vs χ_mag one-bin offset (§2.4) is unresolved at this grid resolution.

### 3.4 Follow-ups (not done here)

- `CCA_brown_mechanism_question` (Speculative, 2026-04-08) asks whether pure two-point CCA can reproduce GTE's discrimination. This result answers its d_eff half: it does, through the order parameter, which any order-parameter measure does. Its row is not updated here (owner's call).
- STAT3 label review, given the withdrawn Phase E strengthening.

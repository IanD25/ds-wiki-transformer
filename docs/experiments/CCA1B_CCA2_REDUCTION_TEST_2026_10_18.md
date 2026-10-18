# CCA-1b-magnitude and CCA-2 Reduction Test — do the last two "Supported" CCA results reduce to known physics?

**Mode:** B (falsification first, on existing claims; no new P/Q entries)
**Date:** 2026-10-18
**audit_ref (planned):** `gsw-cca1b-cca2-reduction-2026-10-18`
**Subjects (latest rows in `claim_status_latest`):**
- **CCA-1b-magnitude** — Supported (2026-04-08, `M0_2026-04-08_primary_sources`): "~20× dη/dT magnitude separation between Potts q = 10 (first-order) and q = 2 (continuous)", Phases C and D.
- **CCA-2** — Supported (2026-04-08, `M0_2026-04-08`): "d_eff = d_lattice + 1 confirmed for 2D and 3D tori only", Phase A.

**Template:** [`CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md`](CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md): pre-registration committed before computing, exact identities, fixed verdict rules, reuse of saved data.

**Data (saved, April):**
- Phase A: `data/reports/ising_fim_test/topology_sweep.json` (bare tori, paths and complete graphs; 9 kernel values α).
- Phase C: `data/reports/ising_fim_test/potts_comparison_neglog.json` (L = 16, q ∈ {2, 10}).
- Phase D: `data/reports/ising_fim_test/cca1b_scaling/cca1b_scaling_fast.json` (q ∈ {2, 10}, L ∈ {16, 32, 48}, 21 temperatures T/T_c = 0.92–1.12).
- Phase E (secondary only): `data/reports/cca_potts_sweep_2026/raw/*.npz`.

---

## 1. Pre-registration (written and committed before any number below §1 was computed)

### 1.1 Which "d_eff" and which "η" — established from the code first (brief, lead 1)

**Neither claim uses the Phase E observables.** Phase E (and CCA-1c) used the spectrum of the N × N connected correlation matrix χ, with d_eff_CCA = participation ratio and η_CCA = Zipf exponent. Phases A–D used the older wiki-graph Fisher tool, `analyze_node` in `src/analysis/fisher_diagnostics.py`:

1. Build a graph. Phase A: a bare lattice with unit edge weights, no spin model. Phases C/D: the L × L torus with edge weight w_e = −ln c_e, where c_e is the Monte Carlo average of δ(s_i, s_j) on nearest-neighbour bond e. The scripts call this "neglog".
2. For a centre node v and each of its k neighbours w_j: Dijkstra distances, kernel K(u) = exp(−α d(·, u)), normalised to distributions p_v, p_{w_j} over all N vertices (α = 1 in Phases C/D).
3. Score vectors s_j(u) = ln p_{w_j}(u) − ln p_v(u) (finite differences, not derivatives), and the k × k matrix **F_ij = Σ_u p_v(u) s_i(u) s_j(u)**. This is an *uncentred* second moment: E_v[s_j] = −KL(p_v ‖ p_{w_j}) ≠ 0.
4. Singular values σ_1 ≥ … ≥ σ_k of F. **d_eff = argmax_i (σ_i / σ_{i+1}) + 1**, the position of the largest consecutive-ratio gap. **η = σ_{d_eff+1} / σ_{d_eff}**, the ratio just after the gap. Phases C/D average η and d_eff over 25 sampled centre nodes.

So CCA-2's "d_eff" is a gap position in a k × k matrix (k = 2d on a hypercubic torus), and CCA-1b's "η" is a gap-sharpness ratio in a 4 × 4 matrix. This is the v0.1 definition the rename proposal's notation table marks as superseded. Consequences for the brief's leads:
- **Lead 2** (fixed trace tr χ = N(q − 1), λ₁ ≈ ⟨M²⟩) **does not apply**: neither observable is a function of χ's spectrum.
- **Lead 3** (circulant χ, eigenvalues = S(k)) **does not apply to CCA-2 as measured**: Phase A has no correlation matrix. It is answered for the χ reading in a secondary check (§1.5).

Two facts follow from the definition alone:
- **d_eff ≤ k − 1** (there are k − 1 consecutive ratios). An interior node of a 1D path has k = 2, so d_eff = 1 always. This is why CCA-2 is stated for d ≥ 2: d + 1 = 2 cannot be reached in 1D.
- On a vertex-transitive graph every node gives the same F, so Phase A's average over 20 nodes is a single value.

### 1.2 CCA-2: identity derived before computing

**Factorisation.** On the d-dimensional L^d torus with unit edges, the graph distance is the sum of cyclic distances per axis, d(u, v) = Σ_a δ_L(u_a − v_a). The kernel therefore factorises: p_v(u) = Π_a π(u_a − v_a), with π(x) = e^{−α δ_L(x)} / Z₁. Every node has the same normaliser, so for the neighbour displaced by ±1 along axis a:

  s_{a±}(u) = −α [δ_L(x_a ∓ 1) − δ_L(x_a)],  x = u − v.

This depends on the single coordinate x_a. For even L it takes only the values ±α: +α where the neighbour is closer, −α where it is farther.

**Structure of F.** Index the 2d neighbours by (axis a, sign σ). Coordinates are independent under p_v, so

  F_{(a,σ),(b,τ)} = m² (a ≠ b), F_{(a,σ),(a,τ)} = M_{στ},

where m = E_π[s_{a+}] = E_π[s_{a−}] (by reflection symmetry) and M is a 1D 2 × 2 matrix. Splitting each axis into its antisymmetric combination (s_{a+} − s_{a−}) and its symmetric combination (s_{a+} + s_{a−}) gives **exactly three distinct eigenvalues**:

| Sector (hyperoctahedral irrep) | Multiplicity | Eigenvalue |
|---|---|---|
| antisymmetric: the d translations (vector irrep) | d | λ_T = M₊₊ − M₊₋ |
| symmetric, all axes in phase (trivial irrep, "radial") | 1 | λ_A = c_S + 2d m² |
| symmetric, axes out of phase | d − 1 | λ_E = c_S |

where c_S = M₊₊ + M₊₋ − 2m². In closed form, with π₀ = 1/Z₁, π_h = e^{−αL/2}/Z₁ and Z₁ = 1 + 2Σ_{r=1}^{L/2−1} e^{−αr} + e^{−αL/2}:

- **λ_T = 2α² (1 − π₀ − π_h)**
- **λ_A = 2α² [(π₀ + π_h) + (d − 1)(π₀ − π_h)²]**
- **λ_E = 2α² [(π₀ + π_h) − (π₀ − π_h)²]**

(m = −α(π₀ − π_h), M₊₊ = α², M₊₋ = α²[2(π₀ + π_h) − 1].)

**Consequences, before any computation:**
1. λ_A − λ_E = 2d m² ≥ 0. **The trivial (radial) mode splits off from the E modes only because of the mean score m.** That is the uncentred-moment term, m = −KL per axis. In a centred Fisher matrix (the covariance of the scores) λ_A = λ_E, and the spectrum has two levels of multiplicity d each.
2. Because the gap must fall between distinct levels, and λ_A > λ_E always, **d_eff ∈ {1, d, d + 1}**. Which value appears depends only on the ordering and the ratios of λ_T, λ_A and λ_E, all 1D functions of (α, L) and d.
3. **d_eff = d + 1** happens exactly when the d translation modes and the single radial mode sit above the d − 1 E modes, and the gap to the E block is the largest ratio. "d + 1" counts **d (translations: a location family in d dimensions has d-dimensional Fisher information) + 1 (the mean-score mode)**. It is a count of irrep dimensions of the hypercubic point group acting on the 2d nearest neighbours, plus an artefact of the uncentred estimator. It is not a property of "criticality" or "constraint".
4. **With the centred matrix, d_eff = d** (when λ_T ≠ λ_E). Removing the mean-score term turns "d + 1" into "d".
5. For large α, π₀ → 1 and λ_T → 0, so d_eff → 1. For small α (and large L), λ_T ≫ λ_A ≈ λ_E, so d_eff → d. **d + 1 occurs only in a window of α.** CCA-2's wording "at the optimal kernel scale" selects that window.

**Reduction hypothesis H₂ (one sentence):** On hypercubic tori, Phase A's d_eff is fixed by the three-level spectrum above; "d_eff = d + 1" is the d-dimensional translation sector plus the one radial mode split off by the mean score, within an α window, and nothing else.

### 1.3 CCA-1b: identity derived before computing

**Uniform-weight reduction.** If every bond had the same weight w̄ = −ln c̄, Dijkstra distances would be w̄ × the hop distance, and K = exp(−α w̄ · hop). Phase D's graph would then be *exactly* the Phase A torus at kernel α′ = α w̄ = −ln c̄ (α = 1). So

  **η(T) = H_L(α′(T)), α′ = −ln c̄(T),**

with H_L the gap-ratio function of the 2D torus from §1.2 (d = 2, same L). In the 2D Potts model with H = −J Σ_bonds δ(s_i, s_j), **c̄ = ⟨δ⟩_NN = −E / (2NJ)**: the mean nearest-neighbour equal-state probability *is* the internal energy per bond. Then

  dη/dT = H_L′(α′) · (−1/c̄) · dc̄/dT, with dc̄/dT = C(T) / (2J) (C = specific heat per site, k_B = 1).

**Prediction.** CCA-1b's ~20× separation is then (i) the energy changing much faster across a first-order T_c, a latent-heat jump (Baxter 1973; Wu 1982, *Rev. Mod. Phys.* 54, 235), than across the 2D Ising point, where the specific heat diverges only logarithmically (Onsager 1944); times (ii) the slope of a fixed geometric function H_L, evaluated at the different α′ ranges the two models visit: q = 2 has c̄ ≳ 0.75; q = 10 crosses from c̄ ≈ 0.8+ to ≈ 0.4–0.5. Both factors are textbook, not CCA content.

**Known approximation.** The real c_e vary from bond to bond: finite-sample noise, plus spatial domain structure near a first-order T_c with Metropolis random starts. Dijkstra takes minimum-weight paths, so heterogeneity changes distances. The uniform-weight form is therefore an approximation, and the residual measures how much η carries beyond the mean energy.

**Reduction hypothesis H_1b (one sentence):** Phase C/D η(T) is, to good approximation, a fixed function of the mean nearest-neighbour bond energy c̄(T), so the q = 10 vs q = 2 separation in max|dη/dT| is the separation in dE/dT (latent heat vs log-divergent specific heat) seen through that function.

### 1.4 What is computed

**CCA-2 (Phase A, no Monte Carlo):**
- C2.1 For every Phase A torus (2D L = 8, 12, 16; 3D L = 4, 6) at every α in the Phase A grid (45 configurations): F and its singular values from `analyze_node`'s own functions, on 3 nodes (vertex-transitivity check).
- C2.2 Closed-form multiset {λ_T × d, λ_A × 1, λ_E × (d − 1)} vs those singular values (relative tolerance 1e-8). Closed-form d_eff and η, run through `decompose_fim`, vs the values recorded in `topology_sweep.json`.
- C2.3 Centred matrix F_c = F − μμᵀ (μ_j = E_v[s_j]): its gap-based d_eff in every configuration.
- C2.4 α window: on a grid α ∈ [0.01, 5] (step 0.01), the α interval where closed-form d_eff = d + 1, for d = 2…6 and L ∈ {Phase A sizes, 32, 64, 128}. Descriptive, not decisive.

**CCA-1b (Phases D and C, no Monte Carlo):**
- B.1 For each Phase D point (q, L, T): α′ = −ln(mean_corr); η_pred = H_L(α′) and d_eff_pred from the §1.2 closed form at d = 2, same L. Checked against `analyze_node` on a uniform-weight torus for a few points.
- B.2 Pooled R² = 1 − Σ(η_meas − η_pred)² / Σ(η_meas − ⟨η_meas⟩)² over all 126 Phase D points; also per (q, L).
- B.3 S_max,pred from η_pred(T) by the same central difference Phase D used; ratio R_pred(L) = S_max,pred(q=10) / S_max,pred(q=2) vs the measured R_meas(L) (17.8 / 25.4 / 19.6 per the April handover).
- B.4 Energy factor vs lens factor (descriptive): the ratio of max|dα′/d(T/T_c)| between q = 10 and q = 2, and the ratio of |H_L′| at the S_max points.
- B.5 Phase C (L = 16, q ∈ {2, 10}): the same collapse. Secondary.

### 1.5 Verdict rules (fixed in advance)

**CCA-2:**
- **REDUCES** if (i) the closed-form multiset matches the computed singular values to 1e-8 in all 45 torus configurations, and the closed-form d_eff equals the recorded Phase A d_eff in all 45, with η within 1e-6; **and** (ii) the centred matrix gives d_eff = d in every configuration where λ_T ≠ λ_E (relative difference > 1e-6). → "d_eff = d + 1" = d translations + 1 mean-score mode in an α window. Tags: `answer-forced-by-definition`, `trivial-from-known-result` (point-group irreps; Fisher information of a location family).
- **PARTLY REDUCES** if (i) holds but (ii) fails, or (i) holds in one dimension only.
- **DOES NOT REDUCE** if (i) fails in general, i.e. the spectrum is not the three-level structure. Then the d + 1 count needs another explanation, and the prior-art gate applies before any novelty statement.

**CCA-1b-magnitude:**
- **REDUCES** if pooled R² ≥ 0.90 **and** 0.5 ≤ R_pred(L) / R_meas(L) ≤ 2 at all three L. → The separation is the energy slope (latent heat vs specific heat) through a fixed function of c̄. Tags: `restatement-in-new-vocabulary`, `trivial-from-known-result`.
- **PARTLY REDUCES** if pooled R² ≥ 0.50 and the REDUCES conditions are not all met. → State what is left over (e.g. bond heterogeneity at coexistence). Only then consider a small rerun of the Phase D script (deterministic seeds) that saves per-bond c_e, to separate noise from spatial structure.
- **DOES NOT REDUCE** if pooled R² < 0.50 → characterise, then run the prior-art gate before any narrow-novelty statement.

**Secondary, χ reading of CCA-2 (brief, lead 3), not decisive for CCA-2:** if "d_eff" is read as Phase E's participation ratio of χ, the torus makes ⟨χ⟩ circulant, its eigenvalues are S(k), and d_eff = (Σ_k S(k))² / Σ_k S(k)². With S(k) ~ k^{−(2−η)} at T_c, Σ_k S(k)² is dominated by the smallest k and scales as L^{2(2−η)}, while (Σ S)² = (N(q−1))² ~ L^{2d}. So **d_eff(T_c) ~ L^{2d − 4 + 2η}**: L^{1/2} in 2D Ising and ~L^{2.07} in 3D. That is not a constant d + 1. Pre-registered check on Phase E q = 2 at T/T_c = 1.00: d_eff(L = 32) / d_eff(L = 16) ∈ [1.15, 1.6] (asymptotic √2 ≈ 1.41), and d_eff is not within ±0.3 of 3 at all three L.

### 1.6 Caveats known in advance

1. I have already seen Phase A's recorded table (d_eff = 2 / 3 / 1 at different α on the 2D tori; 3 / 4 / 1 on the 6³ torus; 1 at every α on the 4³ torus) and Phase D's headline S_max values. I have **not** compared Phase D's η with mean_corr point by point, and I have not evaluated the closed form numerically.
2. Phase C/D graphs are not uniform, so H_1b is an approximation by construction. That is why its threshold is R² ≥ 0.9, not an identity check.
3. Phase D used Metropolis random starts at every temperature. For q = 10 at large L, runs below T_c may sit in multi-domain states. This does not affect the reduction question: η follows whatever c̄ the run had.
4. Phase D's S_max uses a 0.01 grid in T/T_c (central difference over 0.02). This was already identified as resolution-limited (CCA-1b-scaling, Falsified). The ratio test inherits the same grid on both sides.

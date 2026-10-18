# CCA-1b-magnitude and CCA-2 Reduction Test — do the last two "Supported" CCA results reduce to known physics?

**Mode:** B (falsification first, on existing claims; no new P/Q entries)
**Date:** 2026-10-18
**audit_ref (planned):** `gsw-cca1b-cca2-reduction-2026-10-18`
**Subjects (latest rows in `claim_status_latest`):**
- **CCA-1b-magnitude** — Supported (2026-04-08, `M0_2026-04-08_primary_sources`): "~20× dη/dT magnitude separation between Potts q = 10 (first-order) and q = 2 (continuous)", Phases C and D.
- **CCA-2** — Supported (2026-04-08, `M0_2026-04-08`): "d_eff = d_lattice + 1 confirmed for 2D and 3D tori only", Phase A.

**Result (added after computing; §1 is unchanged from commit `9a3c125` apart from the typo fix noted in §2.0):** **CCA-1b-magnitude REDUCES.** Phase C/D η is a fixed algebraic function of the nearest-neighbour bond energy c̄ = −E/(2NJ): pooled R² = 0.992, and the predicted q = 10 / q = 2 ratio is within 0.98–1.26× of the measured ratio at every L. The ~20× is latent heat against a log-divergent specific heat. **CCA-2 REDUCES on substance, with a deviation from the letter of the rule.** The three-level closed form reproduces every Phase A d_eff and η exactly. "d + 1" = d translation modes + 1 mode created by the uncentred estimator, inside an α window, and the centred matrix gives d at every α. One pre-registered tolerance (spectrum to 1e-8) failed in 10 of 45 configurations, by at most 3·10⁻⁷. The cause is the tool's own 10⁻¹⁰ probability cut-off (§2.2). Proposed: both **Supported → Retired**, owner's decision. See §3.

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

---

## 2. Computation

*Pre-registration committed as `9a3c125` before this section was written.*

### 2.0 Deviations from the pre-registration

1. **Typo fixed before committing.** The first draft of §1.2 had λ_A with (2d − 1)(π₀ − π_h)²; it was corrected to (d − 1) before the commit, and the committed text is what was tested. The draft's "d_eff ∈ {1, d, d + 1, 2d − 1}" was also tightened to {1, d, d + 1} before the commit, since λ_A > λ_E always.
2. **Coded verdict stricter than the written rule.** The script's verdict function falls through to "DOES NOT REDUCE" whenever condition (i) fails in both dimensions. The written rule reserves DOES NOT REDUCE for a spectrum that "is not the three-level structure". This matters for CCA-2 (§2.2). The written rule governs; the script's label is reported as `verdict_by_letter_of_rule` and not used.
3. **One post-hoc check added** (CCA-2, §2.2), labelled `posthoc` in the outputs. It is not part of the rule.

**Script:** [`scripts/cca1b_cca2_reduction.py`](../../scripts/cca1b_cca2_reduction.py). It reads the saved Phase A, C and D JSON and the CCA-1c `by_config.csv`, runs under a second, and writes [`data/reports/cca1b_cca2_reduction_2026_10/`](../../data/reports/cca1b_cca2_reduction_2026_10/): `cca2_phaseA.csv` (45 configurations), `cca2_alpha_windows.csv`, `cca1b_phaseD_points.csv` (126 points) and `summary.json`. **No Monte Carlo was run.**

### 2.1 CCA-1b: η is a function of the bond energy

**Identity checks:**
- The closed form H_L(α′) equals `analyze_node` on a uniform-weight torus at 6 spot points (q ∈ {2, 10}, L ∈ {16, 32, 48}). Agreement is to ≤ 10⁻¹⁵ at four points and to 5·10⁻⁷ / 2·10⁻⁶ at the two large-α′ points (L = 32, 48). That is consistent with the EPS cut of §2.2.
- The recomputed measured S_max equals the recorded S_max exactly in all 6 (q, L).

**Collapse (B.2):** pooled R² = **0.992** over all 126 Phase D points (threshold 0.90). Per curve, R² is 0.94–0.999 and the RMS residual is 0.004–0.031. The largest residual is q = 10 at L = 16, the smallest lattice. The predicted d_eff (2 or 3) matches the recorded mean d_eff at all 122 points where that mean is an integer. The other 4 (q = 10, L = 16) are 2.04–2.08 against a predicted 2, and 2.92 against a predicted 3. At q = 10 the 2 → 3 switch falls exactly where α′ = −ln c̄ crosses ≈ 0.6, the lower edge of the CCA-2 window (§2.2).

**Separation (B.3):**

| L | S_max q = 2 (meas / pred) | S_max q = 10 (meas / pred) | R_meas | R_pred | R_pred / R_meas | energy ratio, max\|dc̄/dT\| (q10/q2) | lens ratio \|H′\| |
|---|---|---|---|---|---|---|---|
| 16 | 0.880 / 0.749 | 15.66 / 16.84 | 17.8 | 22.5 | 1.26 | 8.7 | 1.40 |
| 32 | 0.805 / 0.828 | 20.45 / 20.69 | 25.4 | 25.0 | 0.98 | 14.6 | 1.49 |
| 48 | 0.884 / 0.867 | 17.31 / 17.95 | 19.6 | 20.7 | 1.06 | 17.6 | 0.81 |

All three ratios fall inside the pre-registered band [0.5, 2]. The S_max temperature matches at q = 10 at every L (0.99–1.00). At q = 2 it matches at L = 32, but at L = 16 and 48 the measured maximum sits at 1.09 and 1.03, against a predicted 1.01. q = 2's η curve is nearly flat, so its maximum slope is set by noise (amplitude ≈ 0.005).

**Reading the decomposition.** Most of the separation is the energy factor: max|dc̄/dT| is 9–18× larger at q = 10 (in α′ = −ln c̄ terms, 11–24×). That is the latent-heat jump in c̄ (≈ 0.86 → 0.51 between T/T_c = 0.99 and 1.00 at L = 32) against the 2D Ising energy's smooth, log-divergent slope. The geometric lens H_L′ contributes 0.8–1.5× either way.

**Phase C (secondary, L = 16):** pooled R² = 0.954. S_max measured / predicted: q = 2 0.444 / 0.454, q = 10 8.68 / 8.91. Phase C's "two orders of magnitude" (0.05 vs 7.7 in the April write-up, computed there with its own differencing) is the same energy jump.

**Why the collapse works: closed forms (derived after computing, from §1.2, L → ∞).** With c̄ = e^{−α′} and π₀ = tanh(α′/2) = (1 − c̄)/(1 + c̄), the gap-ratio η of the 2D torus is an explicit function of c̄:

| α′ = −ln c̄ | d_eff | η |
|---|---|---|
| ≲ 0.61 (c̄ ≳ 0.54) | 2 | (1 − c̄) / [c̄(1 + c̄)] |
| 0.61–0.88 | 3 | **c̄** |
| 0.88–1.21 | 3 | (1 − c̄) / (1 + c̄) |
| ≳ 1.21 | 1 | c̄(1 + c̄) / (1 − c̄) |

In the middle branch the "isotropy index" η equals the mean nearest-neighbour equal-state probability, i.e. minus the energy per bond. Check: q = 10, L = 32, T/T_c = 1.00 gives c̄ = 0.5067 and η_pred = 0.5067. Finite L shifts the branch edges slightly.

### 2.2 CCA-2: the three-level spectrum

| Check (pre-registered) | Result |
|---|---|
| Vertex-transitivity (3 nodes per configuration) | identical to 3.7·10⁻¹⁵ |
| Closed-form d_eff = `analyze_node` d_eff = Phase A recorded d_eff | **45 / 45** |
| Closed-form η vs Phase A recorded η | **45 / 45** within 1e-6 (max 1.3·10⁻⁷) |
| Closed-form spectrum vs computed singular values, tolerance 1e-8 | **35 / 45** (max deviation 3.0·10⁻⁷) |
| Centred matrix gives d_eff = d where λ_T ≠ λ_E | **all** applicable configurations |

**The 10 tolerance misses (post-hoc diagnosis).** All 10 sit at large α (1.5–5), where the centre distribution's smallest probability falls below 10⁻¹⁰. There `build_score_vectors` treats p as exactly zero (its `EPS = 1e-10` guard) and sets those score entries to 0 or ±20. Recomputing the same F without that cut, using log-probabilities directly, gives a maximum deviation from the closed form of **3.5·10⁻¹⁵ in all 45 configurations**. The spectrum is the three-level structure. The miss is in the tool's numerical guard, not in the identity, and it shifts no d_eff and no η beyond 1.3·10⁻⁷.

**Every Phase A torus value, explained:**
- **2D tori:** d_eff = 2 for α ≤ 0.5 (λ_T > λ_A ≈ λ_E: the gap sits after the two translation modes), 3 for α = 0.75–1.0, and 1 for α ≥ 1.5 (λ_A dominates).
- **3D 6³:** d_eff = 3 / 4 / 1 by the same mechanism.
- **3D 4³** (d_eff = 1 at every α, which April called a "finite-size artifact"): at L = 4 the closed form gives λ_T ≡ λ_E *identically*. With x = e^{−α}, 1 − 2(π₀ + π_h) + (π₀ − π_h)² = 0 for Z₁ = (1 + x)². The spectrum is λ_A plus five equal values, so the only gap is at position 1. This is exact, not a finite-size fluctuation.
- **Paths:** two neighbours, one ratio, so d_eff = 1 by construction (§1.1).
- **Complete graphs:** the neighbour set splits 1 + (N − 2) under permutation symmetry, so d_eff ∈ {1, N − 2}. Recorded: 1.

**α windows (C2.4).** On α ∈ [0.01, 5], closed-form d_eff = d + 1 holds only on a single contiguous interval covering 10–12% of the grid:

| d | L | d + 1 window (α) |
|---|---|---|
| 2 | 8 | 0.57–1.17 |
| 2 | 12 to ∞ | 0.61–1.21 |
| 3 | 4 | none (λ_T ≡ λ_E) |
| 3 | 6 | 0.42–0.92 |
| 3 | 32 to ∞ | 0.52–1.09 |
| 4 / 5 / 6 | 32 to ∞ | 0.45–1.01 / 0.41–0.95 / 0.37–0.91 |

Outside the window d_eff is d (smaller α) or 1 (larger α). The window exists in every dimension tested, so "d + 1" would "hold" for any hypercubic torus with L ≥ 6. It holds because the count is forced, not because it measures anything about criticality.

**Centred control.** Removing the mean score (F_c = F − μμᵀ) gives d_eff = d in every configuration where λ_T ≠ λ_E. **The "+1" is the mean-score term of the uncentred estimator.** That term is λ_A − λ_E = 2d·m², with m = −KL per axis: the neighbours' kernels differ in KL from the centre's, and the uncentred moment adds that offset along the all-neighbours direction.

### 2.3 Secondary: the χ reading of "d + 1" (brief, lead 3)

Phase E, q = 2, T/T_c = 1.00, χ participation ratio: **3.65 ± 0.09 (L = 16), 3.73 ± 0.18 (L = 24), 4.72 ± 0.34 (L = 32)**. The ratio d(32)/d(16) = 1.29 lies inside the pre-registered [1.15, 1.6]. The values are not all within ±0.3 of 3. Both pre-registered predictions hold. As the CCA-1c identity requires, the value tracks 1/⟨M²⟩² (3.69, 3.73, 4.72). The χ participation ratio at T_c grows with L, ~L^{2η} asymptotically, and does not sit at d + 1. Read either way, "d_eff = d + 1" is not a property of the critical point.

---

## 3. Verdict

### 3.1 CCA-1b-magnitude: **REDUCES** (pre-registered rule; `summary.json` `cca1b.verdict`)

> **Plain statement:** The April "η" (Phases C/D) is a fixed algebraic function of the average nearest-neighbour bond energy. In one branch it *equals* that energy per bond. The ~20× larger dη/dT at q = 10 is the energy jumping at a first-order transition (latent heat), against the 2D Ising energy, which changes continuously with only a logarithmic specific-heat peak.

- **Triviality check (charter rule 2):** yes. The uniform-weight reduction is a two-line rescaling: neglog weights scale all Dijkstra distances by −ln c̄, so α′ = −ln c̄. Then c̄ = −E/(2NJ) for the δ-function Potts Hamiltonian. The physics is textbook: latent heat for 2D Potts q > 4 (Baxter 1973, *J. Phys. C* 6, L445; review Wu 1982, *Rev. Mod. Phys.* 54, 235) and the logarithmic specific heat of 2D Ising (Onsager 1944, *Phys. Rev.* 65, 117). Citations are from standard references and were not re-fetched in this session.
- **Framing check (rule 3):** in the standard framing, any smooth function of the internal energy has a derivative ∝ C(T), and C(T) is a delta-like spike (latent heat) at a first-order point but only log-divergent at 2D Ising. A large derivative ratio is guaranteed. The 20× is "first-order transitions have latent heat", restated.
- **The brief's lead 2 does not apply:** this η is not built from χ. The question "is it λ₁ / the order parameter?" is moot. It is the energy, not the magnetisation.
- **Prior-art gate:** not triggered. Nothing survived.
- **Pattern tags:** `restatement-in-new-vocabulary` (η = bond energy through a fixed lens); `trivial-from-known-result` (latent heat vs log specific heat).
- **Folded, not Falsified** (owner rule): the literature answers the question the way the claim did. The observable does separate the orders, through the energy discontinuity.

### 3.2 CCA-2: **REDUCES on substance; one pre-registered tolerance missed** (owner to confirm)

> **Plain statement:** On a d-dimensional square/cubic torus, the April "d_eff" can only be 1, d or d + 1, by symmetry. It equals d + 1 when the d "shift" directions and one extra direction outrank the rest. That extra direction exists only because the matrix was not mean-centred. This happens in a window of the kernel setting (about a tenth of the range tried). Elsewhere d_eff is d or 1. Centring the matrix makes it d everywhere.

- **By the letter of §1.5:** condition (i)'s spectral clause (1e-8) failed in 10/45 configurations. So the result is not REDUCES by the letter. The PARTLY REDUCES conditions are not met either. The written DOES NOT REDUCE condition ("the spectrum is not the three-level structure") is false. The rules did not anticipate a numerical guard inside the tool. Every quantity CCA-2 is actually about (d_eff and η) matches in 45/45, and the centred control passes. **Recommendation: treat as REDUCES, recorded with this deviation.** Owner's call.
- **Triviality check:** yes. The neighbour set of a hypercubic lattice splits under its point group into irreps of dimension d (vector), 1 (trivial) and d − 1. A location family in d dimensions has Fisher rank d. The gap-position d_eff can only land on a boundary between levels, and the 1 is lifted above the d − 1 by the uncentred mean.
- **Framing check:** in the standard (centred) Fisher-information framing, the answer is d, the translation rank, for every α. "d + 1" is an estimator artefact selected by the "optimal kernel scale" choice.
- **Pattern tags:** `answer-forced-by-definition` (gap position + symmetry + uncentred estimator); `trivial-from-known-result` (point-group irreps; Fisher rank of a location family). Also arguably `post-hoc-feature-fit`, because "at the optimal kernel scale" picks the α where the count equals d + 1. That tag is offered for the owner to accept or drop.
- **Folded vs Falsified:** within its window the statement is true, and nothing in the literature contradicts it. It is forced, not wrong. Proposed: **Retired — forced by definition**, with the same label class as CCA-1c, not Falsified.

### 3.3 Proposed calibration (NOT applied, awaiting owner approval)

audit_ref `gsw-cca1b-cca2-reduction-2026-10-18`, append-only:
- **CCA-1b-magnitude:** Supported → **Retired**. "Folded: Phase C/D η is a fixed function of the NN bond energy c̄ = −E/2NJ (η = c̄ in one branch); the ~20× dη/dT separation is latent heat (Baxter 1973; Wu 1982) vs 2D Ising log specific heat (Onsager 1944)".
- **CCA-2:** Supported → **Retired**. "Forced by definition: gap-position d_eff on hypercubic tori ∈ {1, d, d+1} by point-group symmetry; d+1 = d translations + 1 uncentred-mean mode, in an α window only; centred FIM gives d".

Proposed text edits (same approval): CLAUDE.md status and conjecture summary; a dated banner on `docs/CCA_MATHEMATICAL_FORMALIZATION.md` (§4 results tables still say CONFIRMED); and in `ds_wiki.db` a dated qualifier on `gloss_effective_dimension` → "Why this disambig exists". That qualifier says the April Phase A–D d_eff was the gap position (`fisher_diagnostics.decompose_fim`), a sixth sense the page omits. The page currently attributes "the CCA framework" only to the participation ratio.

### 3.4 Limitations

1. CCA-1b's reduction uses the uniform-weight approximation. The residual (RMS ≤ 0.03, R² ≥ 0.94 per curve) is bond-to-bond heterogeneity: sampling noise and domains. It is not characterised, and no claim is made from it. It does not move the ratio outside [0.98, 1.26] of the measured value.
2. CCA-2 was examined on hypercubic tori only, the only family it was ever tested on. On other lattices the possible d_eff values are fixed by the irreps of their neighbour shell, which is a prediction of this reduction, not tested here.
3. q = 2's S_max is noise-limited (§2.1), so ratios built on it carry ~±15% scatter. The band [0.5, 2] absorbs this.
4. Citations in §3.1 (Baxter 1973, Onsager 1944) were not re-fetched in this session. Wu 1982 was verified in the CCA-1c session.

### 3.5 Follow-ups (not done here)

- **M6 / DFIG check (owner).** The same tool (`fisher_diagnostics`, gap-position d_eff) underlies M6's Fisher-rank D_eff validation "on tori, fractals, random graphs" (ref 90, Darling 2026 preprint). On hypercubic tori this report shows that d_eff is fixed by symmetry and α: d for small α, d + 1 in a window, 1 for large α. Whether M6's torus validation used this observable, and so measured the point group rather than dimension, was not checked. It bears on P5 and Ax2.
- **`fisher_diagnostics` EPS guard.** The 10⁻¹⁰ cut perturbs spectra at large α (§2.2). It is harmless here, but it is a known numerical artefact for any large-α use of the tool.
- **STAT3** "FDS SV2/SV1" diagnostic (row 99, item 5): likely the same gap-ratio family as Phases C/D, so possibly the same energy reduction. Untested.
- After this, no CCA item is labelled Supported. CCA-1b-magnitude, CCA-1c and CCA-2 would all be Retired; CCA-1 and CCA-1b-scaling Falsified.

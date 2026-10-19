# DFIG Reduction Test — does the wiki's effective-dimension thread reduce to known results, symmetry or definitions?

**Mode:** A (establish what was measured), then B (falsification first, on existing claims; no new P/Q entries)
**Date:** 2026-10-19
**audit_ref (planned):** `gsw-dfig-reduction-2026-10-19`
**Subjects (latest labels, `claim_status_latest` where a row exists):**
- **M6** Fisher Information Rank — Established (2026-05-04, `gsw-maldacena-deep-research-2026-05-04`): "legitimate as parameter-space diagnostic". Internal construction, `needs-review`.
- **P5** Fisher rank = D_eff — Supported, as an application of Machta et al. 2013 (M0 2026-04-08; refined 2026-04-20).
- **P6** fractal dimension converges with Fisher rank — Speculative, contradicted by own tests.
- **P7** D_eff non-increasing under any valid coarse-graining — Speculative, partially falsified.
- **Ax2** (D_eff axiom), **OmD** (Ω_D operator), **T1** (rank-monotonicity test) — internal constructions, no calibration rows.

**Templates:** [`CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md`](CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md) and [`CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md`](CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md) (closed form of §1.2 there is reused here).

---

## 1. Pre-registration (written and committed before any number below §1 was computed)

### 1.1 What was measured — established from code, data and calibration rationale (brief, step 1)

**Where M6's validation lives.** M6, P5, P6, P7, Ax2 and T1 all cite "Darling 2026, preprint" for their Phase 1 results. The code and results are the owner's repository `D_eff-Test-1.0` (local copy `~/Documents/Kiro Git/D_eff-Test-1.0`, HEAD `8f8094b`, 2026-03-27), folder `PHASE1_GEOMETRIC/`. Read-only here; nothing in it was changed.

**The construction** (`compute_fisher_dimension` in `ds_phase1_validation.py`; the same function body in `ds_phase1_periodic_rgg.py`, `ds_phase1_random_graphs.py`, `ds_phase1_coarsegraining_v2.py`, `ds_phase1_extension_v4.py`, `ds_phase1_symmetrized_fim.py`):
1. p_v(u; σ) = exp(−d(v, u)/σ) / Z_v, with d the unweighted BFS distance. So α = 1/σ in the notation of the CCA-2 report.
2. For centre v₀ with neighbours w₁ … w_k: s_j(u) = log p_{w_j}(u) − log p_{v₀}(u).
3. **F_ij = Σ_u p_{v₀}(u) s_i(u) s_j(u)**, the *uncentred* second moment (E[s_j] = −KL(p_{v₀} ‖ p_{w_j}) ≠ 0).
4. "Fisher rank" = **gap position**: argmin_i (σ_{i+1}/σ_i) + 1 over the singular values of F. "PR" = (Σσ_i)² / Σσ_i².

This is the same object as `src/analysis/fisher_diagnostics.analyze_node` (gap-position d_eff), with two differences: it uses log-probabilities directly (no 10⁻¹⁰ EPS guard), so the CCA-2 closed form applies to it exactly; and σ is the kernel's length scale rather than α. **So M6's torus and coarse-graining validation used the gap-position d_eff that the CCA-2 test showed is fixed by hypercubic symmetry.** It did not use the χ-spectrum participation ratio.

**P5's support rows** rest on two different objects:
- The two M0 rows (2026-04-08) cite the Phase 1 validation: "tori, random graphs, random geometric graphs" — the construction above.
- The 2026-04-20 row ("reduction-check confirms q=2 continuous reduction to η_std") is about a **third** object: the Zipf exponent of the N × N connected correlation matrix χ in Phase E (`scripts/cca_observables.py`). That row is already a reduction by its own wording (Vinayak et al. 2014, STAT5). χ is the Fisher matrix of the per-site-field Ising/Potts family (IT09: for an exponential family the FIM is the covariance of the conjugate observables). It is positive definite at every T > 0, so its exact rank is N. It never tested "rank = dimension".

**What I had already seen before writing this** (the recorded targets, not decompositions):
- The Phase 1 results files: `PHASE1_RESULTS.md` (2D 200² rank 2, PR 2.759; 3D 50³ rank 3, PR 4.134; σ = 3), `PHASE1_EXTENSION_RESULTS.md` (4D 12⁴: rank 5, 5, 4, 4, 4 and PR 6.809, 6.493, 6.037, 5.731, 5.615 at σ = 1.5, 2, 3, 5, 8; SV profile [1, 1, 1, 1, 0.381, 0.242, 0.242, 0.242]), `PHASE1_COARSEGRAIN_RESULTS.md` and `_V2_RESULTS.md` (all tables), `PHASE1_SYMMETRIZED_FIM_RESULTS.md` (summary table), `PHASE1_EXTENSION_V4_RESULTS.md` (gasket and carpet PR(σ) tables), the RGG/ER summary in the README and the first RGG block of `PHASE1_RANDOM_GRAPHS_RESULTS.md`.
- **One number computed in my head** while reading: the L → ∞ closed-form PR of the 2D torus at α = 1/3, ≈ 2.758, against the recorded 2.759. No other closed-form value, centred matrix, kagome value or RGG decomposition has been computed.

### 1.2 Identities derived before computing

**(D1) Tori: the three-level spectrum (from CCA-2 §1.2, any L).** On the L^d torus the kernel factorises over axes, and F has exactly three distinct eigenvalues: λ_T (multiplicity d, the antisymmetric "translation" combinations s_{a+} − s_{a−}), λ_A (1, all axes' symmetric combinations in phase) and λ_E (d − 1). With π the 1D cyclic kernel, s_±(x) = −α[δ_L(x ∓ 1) − δ_L(x)], m = E_π[s_+], M_{++} = E_π[s_+²], M_{+−} = E_π[s_+ s_−]:

  λ_T = M_{++} − M_{+−}, λ_E = M_{++} + M_{+−} − 2m², λ_A = λ_E + 2d·m².

These hold for odd L as well (the 3 × 3 blocking hierarchy has L = 81, 27, 9); the even-L closed forms of CCA-2 are a special case. Consequences: the gap-position rank ∈ {1, d, d + 1}, and

  **PR_torus = (d λ_T + λ_A + (d − 1) λ_E)² / (d λ_T² + λ_A² + (d − 1) λ_E²).**

Every torus value in Phase 1 — rank and PR, every σ, every size, every coarse-graining level — is then a function of (α = 1/σ, L, d) alone. "Zero variance across vertices" is vertex-transitivity. "Rank = d" is the multiplicity of the translation sector: the 2d nearest neighbours of a hypercubic site span a d-dimensional space of displacements, and a d-parameter location family has a rank-d Fisher matrix. That is a textbook property of location families, read through the lattice's point group.

**(D2) The symmetrised matrix.** `ds_phase1_symmetrized_fim.py` replaces each s_j by (s_j − s_{opp(j)})/2, where opp(j) is the most anti-parallel neighbour. On a torus opp(a±) = a∓, so the symmetrised matrix keeps only the translation sector: d equal eigenvalues λ_T (each from a pair), the rest zero. **Symmetrised PR = d exactly**, for every σ and L, by construction.

**(D3) Block-spin of a torus is a torus.** The 2 × 2 (2 × 2 × 2) blocking in `block_spin_2d/3d` maps the L^d torus onto the (L/2)^d torus with unit edges (the owner's own sanity check says so; re-checked here by graph isomorphism for one level in each d). Each coarse-graining level is therefore a fresh torus, and the rank at each level is the D1 value at (1/σ_level, L_level, d). The coarse F is recomputed from scratch on the new graph with a new kernel. **It is not the fine-level Fisher information processed through a Markov kernel, so the data processing inequality is not engaged.** The DPI for Fisher information (F after a parameter-independent Markov kernel ⪯ F before, hence rank non-increasing; Zamir 1998, *IEEE Trans. Inf. Theory* 44:1246, citation to be verified in the QR-001 map) is a theorem; what the Phase 1 test measured is D1 at shrinking L.

**(D4) Uncentred = covariance + rank-one mean term.** For any graph, F = C + μμᵀ, with C = Cov_{p_{v₀}}(s) and μ_j = E_{p_{v₀}}[s_j] = −KL(p_{v₀} ‖ p_{w_j}). By eigenvalue interlacing (a rank-one PSD update), F's eigenvalues interlace C's: λ_i(C) ≤ λ_i(F) ≤ λ_{i−1}(C). A rank-one update can lift exactly one eigenvalue across a gap. On a torus μ lies along the all-neighbours direction and is what splits λ_A from λ_E (CCA-2). On a random geometric graph the per-vertex normalisers Z_w differ (local density varies), so μ also carries the offsets log Z_{v₀} − log Z_{w_j}. **Hypothesis: the RGG "+1 disorder direction" is this mean term, and the Erdős–Rényi "rank 1" is the mean term dominating everything else.**

**(D5) Large-σ PR depends on neighbour-axis angles.** As σ → ∞, s_j(u) → −α[Δ_j(u) − E_unif Δ_j] with Δ_j(u) = d(w_j, u) − d(v₀, u), so F → α² Cov_unif(Δ). For a vertex whose 4 neighbours lie on two straight lines at angle θ, an isotropic distance field gives a translation block with eigenvalues ∝ 1 ± cos θ, so PR → 2/(1 + cos²θ): 2 for θ = 90°, **1.6 for θ = 60°**. Interior vertices of the Sierpiński gasket have exactly this 60° geometry (each is the shared corner of two triangles). So, before computing anything, the gasket's PR ≈ 1.6–1.7 (d_H = 1.585) may be the 60° angle, not the fractal dimension. **The kagome lattice has the same local geometry** (degree 4, two corner-sharing triangles, neighbours on two straight lines at 60°), but it is an ordinary 2D lattice with d_H = 2. It is the decisive counter-test for P6's participation-ratio form. (D5 is a heuristic: the graph metric is not isotropic, which is why the test is numerical.)

### 1.3 Reduction hypotheses (one sentence each)

- **H-T (tori; M6 class I, P5):** Every Phase 1 torus rank and PR is the D1 closed form at (1/σ, L, d); "rank = d" is the translation-sector multiplicity in a σ window, flanked by d + 1 and 1.
- **H-CG (coarse-graining; P7, T1):** Every Phase 1 coarse-graining rank and PR, in all three σ schedules, is the D1 closed form at the coarse level's (1/σ, L, d), including the rank increases d → d + 1 recorded under the σ ∝ side schedules.
- **H-RGG (P5, M6 class IV):** On periodic random geometric graphs the "+1" is the rank-one mean term μμᵀ: the covariance C has gap position d.
- **H-ER (M6 class V):** On Erdős–Rényi graphs the "rank 1" is the mean direction: F's top singular vector is aligned with μ.
- **H-P6 (fractals):** The participation ratio on the gasket reflects local neighbour geometry, not d_H: the kagome lattice (d_H = 2) gives a PR well below 2.

### 1.4 What is computed

All deterministic graph computations; **no Monte Carlo**. Script: `scripts/dfig_reduction_2026_10_19.py`; outputs under `data/reports/dfig_reduction_2026_10/`. The F, rank and PR functions are re-implemented to match Phase 1 exactly (§1.1, steps 1–4) and are checked against the Phase 1 recorded values where those exist.

**T (tori).**
- T.1 D1 closed form (1D numerical sums, any L) for: 2D 200², 3D 50³ at σ = 3; 4D 12⁴ at σ ∈ {1.5, 2, 3, 5, 8}. Compare rank (exact) and PR (± 0.002) with the recorded values; the 4D SV profile (normalised) with the recorded [1, 1, 1, 1, 0.381, 0.242, 0.242, 0.242] (± 0.002).
- T.2 Identity check: F built on the actual graph (one vertex; vertex-transitive) vs closed form, max relative deviation of the spectrum ≤ 1e-8, for 2D 200², 3D 50³, 4D 12⁴ at σ = 3.
- T.3 Symmetrised PR on 2D 200² and 3D 50³ at σ = 3 vs recorded 2.000 / 3.000 and vs D2 (= d).
- T.4 Descriptive: the σ window in which the rank equals d, for d = 2, 3, 4 at the Phase 1 sizes.

**CG (coarse-graining).**
- CG.1 Isomorphism check, block_spin(torus(L)) ≅ torus(L/2): 2D 16 → 8 and 3D 8 → 4.
- CG.2 D1 closed form for every recorded entry of `PHASE1_COARSEGRAIN_V2_RESULTS.md` with side ≥ 4 (2D: sides 128 … 4 × schedules fixed σ = 3, B σ = side/8, C σ = side/16; 3D: sides 32 … 4 × the same schedules) and for `PHASE1_COARSEGRAIN_RESULTS.md`'s 3 × 3 hierarchy (81, 27, 9; σ = 3). Rank exact; PR ± 0.002 (where recorded to 3 decimals; ± 0.0002 where recorded to 4). Side-2 entries are excluded: a side-2 cycle has coincident ± neighbours, so it is not a 2d-neighbour torus.

**RGG / ER.**
- R.1 Periodic RGG, d = 2 (N = 5000, r = 0.03) and d = 3 (N = 5000, r = 0.09), largest connected component, as in `ds_phase1_periodic_rgg.py`; seeds 0, 1, 2 (three graph realisations); 50 random vertices per realisation; σ ∈ {2, 3}.
- R.2 For each vertex: uncentred gap rank r_u (reproduction check: mode d + 1 expected), centred gap rank r_c (gap position of C = F − μμᵀ), and |cos| between F's top singular vector and μ̂.
- E.1 ER(1000, 0.015) and ER(2000, 0.0075), seeds 0, 1, 2; 30 vertices; σ ∈ {2, 3}. Same quantities.

**P6 (kagome counter-test).**
- K.1 Sierpiński gasket level 9 (29,526 vertices), built as in `ds_phase1_extension_v4.py`; 20 random degree-4 vertices; PR(σ) on σ ∈ {3, 5, 8, 12, 20, 30, 50, 80, 130, 220}.
- K.2 Kagome torus (triangular lattice of side M with the (odd, odd) sites removed; every vertex degree 4), M chosen so that its graph diameter is within 10% of the gasket's (512); 20 random vertices (vertex-transitive up to the three sublattices, so 20 is ample); the same σ grid.
- K.3 Control: the square torus at the same diameter, from D1 (PR → 2 at large σ expected).
- K.4 Descriptive: the triangular torus (degree 6) at the same diameter.

### 1.5 Verdict rules (fixed in advance)

**H-T.** **REDUCES** if T.1 matches every recorded rank exactly and every PR and SV-profile value within tolerance, **and** T.2 and T.3 pass. **PARTLY REDUCES** if ranks match but some PR misses tolerance. **DOES NOT REDUCE** if any recorded torus rank differs from D1.

**H-CG.** **REDUCES** if CG.1 passes and CG.2 matches every rank exactly and every PR within tolerance. **PARTLY REDUCES** if ranks all match but some PR misses. **DOES NOT REDUCE** if any rank differs. Under REDUCES, the recorded rank increases under schedules B and C (2D: 2 → 3; 3D: 3 → 4) are exact closed-form values, not sampling noise, whatever their σ.

**H-RGG.** **REDUCES** if, in both d at σ = 2 (Phase 1's main σ), pooled over seeds: mode(r_u) = d + 1 (reproduction), mode(r_c) = d, and frac(r_c = d) ≥ frac(r_u = d + 1) − 0.10. **PARTLY REDUCES** if mode(r_c) = d in one d only, or in both but the fraction condition fails. **DOES NOT REDUCE** if mode(r_c) ≠ d in both. If mode(r_u) ≠ d + 1 (phenomenon not reproduced), the test is **VOID** and reported as such. σ = 3 is reported, not decisive.

**H-ER.** **REDUCES** if, at σ = 2 pooled: r_u = 1 at ≥ 90% of vertices and |cos(top singular vector, μ̂)| ≥ 0.95 at ≥ 90%. **DOES NOT REDUCE** otherwise.

**H-P6.** Let PR_K and PR_G be the kagome and gasket means at the largest σ in the grid that is ≤ 0.45 × both diameters.
- **FALSIFIED (P6, participation-ratio form)** if PR_K ∉ [1.90, 2.10]: a non-fractal lattice with d_H = 2 misses its d_H by more than the 5% the gasket was credited with, so PR does not track d_H.
- **SURVIVES THIS TEST** if PR_K ∈ [1.90, 2.10].
- Descriptive (mechanism, not decisive): |PR_K − PR_G| at each σ; the square-torus control (K.3) must give PR within 0.05 of 2 at the same σ, else the test is reported as **UNCALIBRATED** and no verdict is drawn.

**Per-claim mapping (fixed in advance).**

| Claim | Verdict follows from |
|---|---|
| **M6** (Phase 1 validation of Fisher rank as dimension) | REDUCES if H-T, H-CG, H-RGG and H-ER all REDUCE; PARTLY if H-T and H-CG do. M6's "Established" (textbook FIM as a parameter-space diagnostic) is not under test: the Fisher matrix is textbook. |
| **P5** (rank = D_eff, "supported as application") | REDUCES if H-T and both H-RGG and H-ER REDUCE (the 2026-04-20 χ row already reduces by its own text). |
| **P6** | Rank form already contradicted (mixed integers). PR form: H-P6 verdict. |
| **P7** | Rank pass REDUCES if H-CG REDUCES. If, in addition, the rank increases are exact closed-form values, P7 as stated ("non-increasing under any valid coarse-graining") has a counterexample in the project's own data, unless the owner rules the σ ∝ side schedules invalid coarse-grainings. PR failure stands as before. |
| **T1** | Theorem part: the DPI for Fisher information (D3), a known result. Phase 1 "pass": H-CG. |
| **Ax2** | A definition (D_eff := rank F). Its Grounding section's evidence = H-T, H-CG, H-RGG/ER, H-P6. |
| **OmD** | Analytic only, no computation (§1.6). |

**Proposed label changes follow mechanically** and go to the owner: REDUCES → Retired (folded or forced by definition); FALSIFIED → Falsified; otherwise no change. M6 gets a correction row with its label unchanged if M6 reduces. Ax2, OmD and T1 have no calibration rows; whether to give them one is the owner's choice, and the default is banner text only (so the claim count stays at 47).

### 1.6 Analytic items (no computation)

- **OmD.** Ω_D = ((D − 2)/2)^λ, with separate λ_G, λ_h, λ_m. Its only checkable property, Ω_D = 1 at D = 4, holds by construction (the entry says so). With the λ's unfixed it makes no prediction; P3 already carries `over-parameterized-unification`. Ω_D is not built from any Fisher computation, so nothing in this test bears on it beyond the definition. Expected verdict: **REDUCES (definition)**; no label change.
- **Exact rank is the parameter count.** For any family with a positive-definite Fisher matrix, rank F equals the number of parameters. A "D_eff" different from the parameter count therefore always comes from a summary statistic (gap position, PR, a threshold), and its value is set by that choice: in Phase 1 by the neighbour basis (k = 2d on a torus), in sloppy models by the noise floor. This is the reason the Sethna group reports spectra, not a scalar (IT09; to be confirmed in the QR-001 map).

### 1.7 Caveats known in advance

1. The RGG and ER graphs are fresh realisations with fixed seeds; Phase 1's exact graphs cannot be regenerated (different RNG streams). The test is of the mechanism, not of reproducing Phase 1's histograms.
2. The kagome comparator matches the gasket's local geometry and diameter, not its vertex count or boundary (the gasket has 3 corner vertices of degree 2; the kagome torus has no boundary). The square-torus control calibrates finite-diameter effects.
3. The QR-006b window-0.5 benchmark is running (9 workers). These computations are BFS on graphs of ≤ ~200,000 vertices, single process, minutes; no Monte Carlo.
4. Citations in §1 marked "to be verified" are verified (or not) in `docs/prior_art_reviews/QR-001_SLOPPY_MODELS_MAP_2026_10_19.md`.

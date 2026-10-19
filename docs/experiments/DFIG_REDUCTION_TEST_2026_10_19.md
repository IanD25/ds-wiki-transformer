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

**Result (added after computing; §1 is unchanged from commit `f29dd61`):** Tori **REDUCE** and coarse-graining **REDUCES**: every Phase 1 rank and PR on tori, at every σ, size and coarse-graining level (43 + 7 entries), is an exact closed-form function of (σ, L, d), including the recorded rank *increases*. The Erdős–Rényi "rank 1" **REDUCES** to the estimator's mean term. The RGG "+1" **DOES NOT REDUCE**: it survives centring and is unexplained. **P6 is FALSIFIED** in its participation-ratio form: the kagome lattice (d_H = 2) gives PR 1.61. Proposed (owner): P6 and P7 → Falsified; correction rows on P5 and M6. See §3.

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

---

## 2. Computation

*Pre-registration committed as `f29dd61` before this section was written. §1 is unchanged.*

**Script:** [`scripts/dfig_reduction_2026_10_19.py`](../../scripts/dfig_reduction_2026_10_19.py), 85 s, single process, while the QR-006b benchmark was running. Outputs in [`data/reports/dfig_reduction_2026_10/`](../../data/reports/dfig_reduction_2026_10/): `tori.csv`, `coarsegrain.csv` (43 entries), `rgg_er_vertices.csv` (1,440 vertex rows), `kagome_gasket.csv`, `summary.json`. **No Monte Carlo.** A post-hoc diagnostic, [`scripts/dfig_reduction_posthoc_rgg.py`](../../scripts/dfig_reduction_posthoc_rgg.py) → `posthoc_rgg.csv`, is labelled as such and is not part of any verdict (§2.3).

### 2.0 Deviations from the pre-registration

1. **Graph diameters.** The gasket's diameter is 512. The kagome and triangular tori are M = 704, diameter 469 (0.92 of 512, inside the pre-registered 10%). The decisive σ is therefore the largest grid value ≤ 0.45 × 469 = 211, i.e. **σ = 130**, not 220. That follows the written rule; σ = 220 is reported too.
2. None other.

### 2.1 H-T (tori): REDUCES

| System | σ | rank recorded / closed form | PR recorded / closed form |
|---|---|---|---|
| 2D 200² | 3 | 2 / 2 | 2.759 / 2.7586 |
| 3D 50³ | 3 | 3 / 3 | 4.134 / 4.1343 |
| 4D 12⁴ | 1.5 | 5 / 5 | 6.8086 / 6.8086 |
| 4D 12⁴ | 2 | 5 / 5 | 6.4929 / 6.4929 |
| 4D 12⁴ | 3 | 4 / 4 | 6.0369 / 6.0369 |
| 4D 12⁴ | 5 | 4 / 4 | 5.7306 / 5.7306 |
| 4D 12⁴ | 8 | 4 / 4 | 5.6151 / 5.6151 |

- The 4D singular-value profile at σ = 3 is [1, 1, 1, 1, 0.3813, 0.2420, 0.2420, 0.2420], exactly as recorded: four translation modes, the one radial mode λ_A, three E modes.
- **Identity (T.2):** F built on the actual graphs matches the closed form to ≤ 1.1·10⁻¹² (relative) on 2D 200², 3D 50³ and 4D 12⁴.
- **Symmetrised PR (T.3):** 2.000, 3.000 (and 4.000 in 4D) — exactly d, as D2 requires for every σ.
- **σ windows (T.4):** the rank equals d only for σ ≥ 1.65 (2D, L = 200), ≥ 1.96 (3D, L = 50), ≥ 2.28 (4D, L = 12). Below that it is d + 1, and below σ ≈ 0.8–1.0 it is 1. Phase 1's "stable regime σ ∈ [2, 8]" and "σ ≥ 2.0 for reliable rank" (P1-7) are the d window of this closed form.

### 2.2 H-CG (coarse-graining): REDUCES

- **Isomorphism (CG.1):** block-spin of the 16² torus is the 8² torus edge for edge, and the same for 8³ → 4³.
- **All 43 recorded entries** (V2 table: 2D sides 128–4 and 3D sides 32–4 under three σ schedules; V1 table: the 2 × 2, 3 × 3 and 2 × 2 × 2 hierarchies at σ = 3) match the closed form: every rank exactly, every PR within 4.5·10⁻⁴ (3-decimal entries) or 3.9·10⁻⁵ (4-decimal entries).
- The fixed-σ sequence [2, 2, 2, 2, 2, 1] is the closed form at σ = 3 as L shrinks. The drop at L = 4 is where the ordering of λ_T, λ_A and λ_E changes on a 4-cycle (and in 3D, L = 4 is the λ_T ≡ λ_E identity found in the CCA-2 test).
- **The rank increases are exact.** Under the two schedules that keep σ/side fixed (B: σ = side/8, C: σ = side/16), the closed form gives **2 → 3** in 2D (C at side 16, B at side 8) and **3 → 4** in 3D (C at side 16, B at side 8). These are the values Phase 1 recorded and set aside as "σ < 2, unreliable". They are not noise: they are the d + 1 window of the same closed form, which every coarse-graining hierarchy crosses when σ shrinks with the lattice.

### 2.3 H-RGG: DOES NOT REDUCE (H-ER: REDUCES)

**H-ER (Erdős–Rényi):** rank 1 at 180 / 180 vertices at σ = 2 (and 180 / 180 at σ = 3); the top singular vector of F is aligned with the mean-score vector μ at every vertex (median |cos| 0.9996 and 0.9992 for n = 1000 and 2000). **The negative control's "rank 1" is the uncentred estimator's mean term, −KL to each neighbour, dominating everything else.**

**H-RGG (periodic random geometric graphs):** the phenomenon reproduces on fresh graphs (uncentred rank mode = d + 1: 83% of vertices in 2D, 71% in 3D at σ = 2). But **centring does not remove the +1**:

| | uncentred rank (σ = 2) | centred rank (σ = 2) | frac(centred = d) |
|---|---|---|---|
| RGG d = 2 (150 vertices) | mode 3 (125 of 150) | mode **3** (112 of 150) | 0.17 |
| RGG d = 3 (150 vertices) | mode 4 (106 of 150) | mode **4** (112 of 150) | 0.12 |

The same holds at σ = 3. The top singular vector is not the mean direction (median |cos| 0.25 and 0.34). By the pre-registered rule this is **DOES NOT REDUCE**: the RGG "+1" is a genuine feature of the score covariance, not the rank-one mean term. Hypothesis D4 was wrong for RGGs.

**Post-hoc diagnostic (not pre-registered; no claim rests on it).** For each vertex: the share of the top d eigenvectors of C lying in the span of the neighbours' Euclidean displacements, and what the (d + 1)-th eigenvector correlates with.
- The top d modes are mostly the d displacement directions (median share 0.90 in 2D, 0.77 in 3D).
- In 2D the extra mode is roughly the all-neighbours-in-phase ("radial") combination (median |cos| 0.81 where the centred rank is 3); in 3D it is not (0.36).
- It is not the neighbours' Euclidean distance from v (|corr| ≈ 0.2) and only weakly tied to the neighbours' degrees (≈ 0.3–0.4).

So the +1 is not explained here. Phase 1's interpretation, "one disorder direction", is an unexplained observation rather than a measured dimension. It also means that on RGGs the gap rank returns d + 1, not the dimension d.

### 2.4 H-P6 (kagome counter-test): FALSIFIED (participation-ratio form)

| σ | gasket L = 9 (d_H = 1.585) | **kagome torus (d_H = 2)** | triangular torus (d_H = 2) | square torus, closed form (d_H = 2) |
|---|---|---|---|---|
| 3 | 2.070 ± 0.148 | 1.953 | 2.415 | 2.759 |
| 8 | 1.946 ± 0.087 | 1.740 | 2.137 | 2.265 |
| 20 | 1.883 ± 0.110 | 1.657 | 2.052 | 2.102 |
| 50 | 1.839 ± 0.184 | 1.623 | 2.020 | 2.041 |
| **130 (decisive)** | **1.768 ± 0.250** | **1.612** | 2.011 | 2.020 |
| 220 | 1.710 ± 0.273 | 1.610 | 2.010 | 2.017 |

(± is the s.d. over 20 sampled gasket vertices; the lattices are vertex-transitive, s.d. < 10⁻¹¹.)

- **Control passes:** the square torus gives 2.020 at σ = 130 (within 0.05 of 2), and the triangular torus 2.011.
- **The kagome lattice, an ordinary 2D lattice with d_H = 2, gives PR = 1.612** at the decisive σ, far outside [1.90, 2.10]. It levels off at **1.6 = 2/(1 + cos² 60°)**, the value D5 predicts from its 60° neighbour geometry.
- The gasket, which has the same local geometry, sits between that 1.6 and the lattices' 2 and is still falling at the largest σ (Phase 1's own L = 10 table: 1.659 at σ = 450). Phase 1's "within 4.7% of d_H" is the value at the last σ tried on a curve that keeps descending. The carpet's 1.905 against d_H = 1.893 is a square grid's ≈ 2 lowered slightly by its holes; d_H = 1.893 is close to 2.

**The participation ratio does not track the Hausdorff dimension.** It is set by the angles between a vertex's neighbour directions, plus finite-σ corrections.

---

## 3. Verdicts

### 3.1 Summary against the pre-registered mapping

| Hypothesis | Verdict | Plain statement |
|---|---|---|
| H-T | **REDUCES** | Every Phase 1 torus number is a closed-form function of (σ, L, d). "Rank = d" is the d-fold translation sector of the hypercubic neighbour shell, in a σ window. |
| H-CG | **REDUCES** | Every coarse-graining number is the same closed form on a smaller torus. Recorded rank increases (2 → 3, 3 → 4) are exact. |
| H-ER | **REDUCES** | The negative control's "rank 1" is the estimator's mean term. |
| H-RGG | **DOES NOT REDUCE** | The RGG "+1" survives centring. Unexplained; not the mean term. |
| H-P6 | **FALSIFIED** | A d_H = 2 lattice gives PR 1.61. PR follows neighbour angles, not d_H. |

| Claim | Outcome (by the §1.5 mapping) |
|---|---|
| **M6** | **PARTLY REDUCES** (H-T, H-CG reduce; H-RGG does not). |
| **P5** | **Does not meet REDUCES** (needs H-RGG). Torus and ER legs reduce; the RGG leg shows d + 1, not d. Mechanical rule: no label change. |
| **P6** | **FALSIFIED** (PR form, kagome); rank form was already contradicted. |
| **P7** | Rank pass **REDUCES**; the rank increases under σ ∝ side are exact, so P7 as stated has a counterexample in the project's own data, **unless the owner rules those schedules invalid coarse-grainings**. PR failure stands. |
| **T1** | Theorem part = the DPI for Fisher information (a known result; see the QR-001 map). Phase 1 pass = H-CG, **REDUCES**. |
| **Ax2** | A definition. The evidence its Grounding section cites: tori and coarse-graining **forced by symmetry**; fractal PR convergence **falsified**; RGGs give **d + 1**, not d. |
| **OmD** | **REDUCES (definition)**, analytic (§1.6). Nothing here bears on it beyond its D = 4 identity by construction. |

### 3.2 Triviality and framing checks (charter rules 2 and 3)

- **Tori and coarse-graining:** yes, a 5-minute result. The kernel factorises over axes, the 2d neighbours split under the point group into irreps of dimension d, 1 and d − 1, and a d-parameter location family has Fisher rank d. In the standard framing, "the Fisher information about a d-dimensional position has rank d" is a textbook statement. It does not need a graph, a fractal or an axiom.
- **The DPI framing:** the Phase 1 coarse-graining test recomputes F on a new graph. The theorem T1 invokes is about processing the *same* data through a Markov kernel. In that setting monotonicity is guaranteed, and nothing is left to test. In the setting Phase 1 used, it is not guaranteed, and the closed form shows it fails at the d + 1 window.
- **Fractals:** the kagome result is the framing check. A lattice with the gasket's local geometry gives the gasket's PR, so the agreement with d_H was a coincidence of the 60° angle.
- **Machta 2013 is not the right anchor for Phase 1.** M0 read P5 as "a re-parameterisation of sloppy models". The Phase 1 object is not a sloppy-model Fisher matrix: it has no model parameters, only the k neighbour displacements of a location family. Its "dimension" is the span of those displacements, not a stiff subspace selected by coarse-graining. The reduction is to the Fisher information of a location family, not to Machta et al.

### 3.3 Proposed calibration (NOT applied; awaiting owner approval)

audit_ref `gsw-dfig-reduction-2026-10-19`, append-only, one row each:

| Entity | Current | Proposed | Reason (diagnostic label) | Pattern tags |
|---|---|---|---|---|
| **P6** | Speculative (contradicted by own tests) | **Falsified** | "Falsified by the 2026-10-19 kagome counter-test: the participation ratio of the Phase 1 Fisher matrix is 1.61 on the kagome lattice (d_H = 2), levelling at 2/(1 + cos² 60°) = 1.6. It follows neighbour angles, not d_H; the gasket's ≈ 1.66 shares the 60° geometry. The gap-rank form was already contradicted (mixed integers)." | `contradicted-by-own-tests`; new tag proposed: `local-geometry-coincidence` |
| **P7** | Speculative (partially falsified) | **Falsified** — owner's ruling needed | "Falsified by own Phase 1 data, shown exact 2026-10-19: under σ ∝ side block-spin schedules the gap rank rises d → d + 1 (2D side 16/8, 3D side 16/8); these are closed-form values, not noise. PR fails at every tested level. The rank's fixed-σ 'pass' is the torus closed form at shrinking L, and the DPI is not engaged (F recomputed on a new graph)." | `contradicted-by-own-tests`; `answer-forced-by-definition` (the rank pass) |
| **P5** | Supported (as application) | **Supported, correction row, label unchanged** (mechanical) — *or* Speculative (owner's option) | "Phase 1 support re-examined 2026-10-19: torus 'rank = d' is the translation sector of the hypercubic point group (textbook location-family Fisher rank), exact closed form; ER 'rank 1' is the uncentred mean term; on RGGs the rank is d + 1, not d, and the +1 is unexplained. The 2026-04-20 χ row is a re-expression of standard exponents. Machta 2013 is a vocabulary anchor, not the same object." | `answer-forced-by-definition`; `restatement-in-new-vocabulary` |
| **M6** | Established | **Established, correction row, label unchanged** | "Label covers the textbook Fisher matrix only. The Phase 1 graph validation (tori, coarse-graining, ER) is forced by lattice symmetry and the uncentred estimator (2026-10-19 reduction test); the RGG d + 1 is unexplained; PR → d_H falsified (kagome)." | `answer-forced-by-definition` |

**Owner's two rulings:**
1. **P7:** are the σ ∝ side schedules (fixed physical scale) valid coarse-grainings? If yes, Falsified. If no, the claim survives only as "the gap rank at fixed σ on tori is non-increasing", which is the closed form and would be **Retired — forced by definition**.
2. **P5:** keep Supported with the correction row (what the pre-registered rule gives), or downgrade to Speculative because its only reproduced support is now the textbook location-family fact, plus a d + 1 on RGGs that contradicts "rank = dimension" as stated.

**Ax2, OmD, T1** (no calibration rows; default = banner text only, so the claim count stays 47):
- Ax2: dated banner on "Grounding and Risk": the Phase 1 evidence is symmetry-forced (tori, coarse-graining), falsified (PR → d_H) or d + 1 (RGGs).
- T1: dated banner on "Phase 1 Results": the pass is the closed form; the σ ∝ side schedules give rank increases; the theorem part is the DPI for Fisher information.
- OmD: no change.

**Text edits (same approval):** dated banners on M6's "Phase 1 Validation" section, P6 and P7 claim text, and a line in `gloss_effective_dimension` noting that M6's Phase 1 used the gap-position sense. CLAUDE.md status and counts (proposed to the owner, not edited while qr005-corrections runs). If P6 and P7 both become Falsified: **24 Speculative · 5 Supported · 7 Established · 7 Falsified · 4 Retired** (47).

### 3.4 Limitations

1. RGG and ER graphs are fresh realisations (seeds 0–2), not Phase 1's exact graphs; the RGG phenomenon reproduced, so this does not affect the verdict.
2. The kagome test fixes local geometry and diameter, not boundary or vertex count. The gasket's PR keeps falling at the largest σ, so where it would end is not established here. The verdict rests on the kagome value, not on the gasket's.
3. D5's 1.6 is a heuristic for an isotropic distance field; the kagome lattice reaching 1.610 is consistent with it, not a proof of it.
4. The RGG +1 is unexplained (§2.3). If anyone wants to claim it as a new "disorder direction", the prior-art gate applies first. Random-geometric-graph hop metrics distort Euclidean distance, a known effect, and are the first place to look.
5. External repository `D_eff-Test-1.0` was read, not modified; values were transcribed from its results files at `8f8094b`.

### 3.5 Owner rulings (2026-10-19)

1. **P7:** the σ ∝ side schedules (physical scale held fixed) are valid coarse-grainings → **Falsified**, as proposed.
2. **P5:** downgraded **Supported → Speculative**, not kept with a correction row. Reason: the only reproduced support left is the textbook fact that a d-dimensional location family has Fisher rank d, and on random geometric graphs the rank is d + 1, which contradicts the claim as stated. This departs from the mechanical outcome of §1.5 (no change) by owner decision.
3. New pattern tag **`local-geometry-coincidence`** accepted (P6).

Resulting counts (`claim_status_latest`, 47 claims): **25 Speculative · 4 Supported · 7 Established · 7 Falsified · 4 Retired**.

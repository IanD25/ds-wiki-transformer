# Test Spec — CCA Potts q=2,5,7,10 Sweep with Dual Observables

**Spec date:** 2026-04-20
**Spec author:** prepared as handover for a future Claude session
**Status:** READY_TO_RUN (pending owner go-ahead)
**Estimated scale:** ~24,000 MC runs; days on a workstation, hours on RTX 2000 GPU

---

## 1. What this experiment settles

**The narrow research question (from the 2026-04-18 M0 audit and the 2026-04-20 conjecture review):**

> Does the CCA framework's pure 2-point observables (FIM-derived `d_eff`, `η`) capture the same phase-transition discrimination information that Brown-Bossomaier-Barnett 2022's Global Transfer Entropy (GTE) — a hybrid 2-point + multi-point observable — captures across continuous and first-order 2D Potts transitions?

Three possible outcomes, all epistemically informative:

| Outcome | CCA observables vs Brown's GTE | Interpretation | Status move |
|---|---|---|---|
| **A** | CCA qualitatively tracks GTE across q=2,5,7,10 | CCA captures same information via pure 2-point — defensible narrow novelty | CCA-1c promotable from Speculative → Supported |
| **B** | CCA fails to discriminate where GTE does | CCA strictly less informative than GTE for this problem | CCA-1c stays Speculative or gets falsified for first-order discrimination |
| **C** | CCA discriminates differently than GTE (different curve shapes, different q-ordering) | Two frameworks capture different information; neither strictly dominates | CCA-1c remains Speculative pending mechanistic explanation |

**Plus the M0 charter requires a reduction-check:** at T_c for continuous transitions (q=2,3,4), CCA's `d_eff` and `η` should be computable from standard critical exponents (η_critical, β/ν) via finite-size scaling.

| Reduction-check outcome | Interpretation |
|---|---|
| **R1** | CCA observables at T_c match FSS predictions from η_critical, β/ν | Continuous-transition CCA reduces to standard exponents. No novel content at T_c; any novel content lives in off-T_c behavior or in first-order regime |
| **R2** | CCA observables at T_c disagree with FSS predictions | Something else is being captured; investigate what structural property differs |

**The experiment runs both tests in one integrated sweep.**

---

## 2. Background that matters (read before implementing)

### 2.1 Prior work already in-repo

- [`scripts/potts_fim_test.py`](../../scripts/potts_fim_test.py) — existing Potts MC + FIM analysis for q=2 and q=10 only. **Reuse the MC core; extend sweep.**
- [`scripts/ising_fim_mc_test.py`](../../scripts/ising_fim_mc_test.py) — Ising MC baseline
- [`scripts/cca1b_finite_size_scaling.py`](../../scripts/cca1b_finite_size_scaling.py) — finite-size scaling infrastructure
- [`src/analysis/fisher_diagnostics.py`](../../src/analysis/fisher_diagnostics.py) — `analyze_node()` + `KernelType` for FIM eigendecomposition
- [`data/reports/ising_fim_test/`](../../data/reports/ising_fim_test/) — existing outputs from Phase A-D 2026-04-07 experiments

### 2.2 Key prior-art papers (anchored in wiki_history.db via STAT3/P5/P6/P7 anchors)

| Paper | DOI / arXiv | Role |
|---|---|---|
| Machta-Chachra-Transtrum-Sethna 2013 | doi:10.1126/science.1238723 | The sloppy-models foundational paper. CCA lives in this lineage. |
| Brown-Bossomaier-Barnett 2022 | (check wiki anchors for DOI) | GTE on Potts q=2,5,7,10 — direct comparator. Download and read before implementing GTE. |
| Mattingly 2018 PNAS | (check anchors) | **Terminology collision warning:** uses `d_eff` with a *different* formula (d_eff = Σ_r r·Ω_r from optimal prior weight) vs CCA's d_eff = (Σλ)²/Σλ². Must cite and distinguish. |
| Vinayak-Prosen-Buča-Seligman 2014 | arXiv:1403.7218 | Correlation-matrix eigenvalue power-law at 2D Ising criticality from η_critical. Relevant for reduction-check. |
| Borgs-Chayes 1996 | arXiv:adap-org/9411001 | Rigorous Potts covariance matrix ↔ FK cluster bridge. Relevant for reduction-check mechanism. |

Use the GSW lookup tool to pull anchors for STAT3 / P5 / P6 / P7:
```bash
python3 scripts/gsw_lookup.py "Fisher information matrix lattice critical phenomena Potts" --top-k 15
```

### 2.3 Known constraints from prior falsifications

- **CCA-1 (isotropy = criticality):** FALSIFIED at 2026-04-07 Phase C. Don't build on CCA-1 as assumed.
- **CCA-1b L^d scaling:** FALSIFIED Phase D.
- **CCA-1b magnitude separation:** qualitatively confirmed single-test (q=2 vs q=10), this experiment extends that.
- **CCA-1c curve shape:** qualitatively confirmed single-test (q=2 vs q=10), this experiment extends and compares to GTE.

### 2.4 Terminology — do not confuse

- **CCA `d_eff`:** participation ratio of FIM eigenvalues. `(Σ λ_k)² / Σ λ_k²`. A scalar summary of how spread-out the eigenspectrum is.
- **Mattingly `d_eff`:** different formula from discrete prior weights on manifold boundaries. Collision.
- **CCA `η`:** a power-law exponent from the eigenvalue spectrum tail. The wiki's `η` is *not* standard stat-mech η_critical (anomalous dimension) — see `docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md`.
- **Standard `η_critical`:** the anomalous dimension from two-point correlation function at criticality. For 2D Ising η_critical = 1/4 exactly.
- **In this spec,** write `d_eff_CCA`, `η_CCA`, `η_std` explicitly in all outputs to prevent confusion.

---

## 3. Experimental parameters

### 3.1 Model

2D q-state Potts model on L×L torus with Hamiltonian:

```
H = -J · Σ_{<i,j>} δ(s_i, s_j),    s_i ∈ {0, 1, ..., q-1}
```

Set J = 1, k_B = 1. Then critical temperature (exact for 2D): `T_c(q) = 1 / ln(1 + √q)`.

| q | T_c (exact) | Transition order |
|---|---|---|
| 2 | 2.269 | continuous (= 2D Ising) |
| 5 | 0.852 | weakly first-order (latent heat small) |
| 7 | 0.773 | first-order |
| 10 | 0.702 | strongly first-order |

### 3.2 Sweep grid

- **q values:** 2, 5, 7, 10 (covers continuous → strongly first-order)
- **Lattice sizes:** L ∈ {16, 24, 32}
  - L=16 for fast prototyping and statistical robustness
  - L=24 for main results
  - L=32 for finite-size-scaling verification (reduction-check)
- **Temperature range:** T/T_c ∈ {0.90, 0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05, 1.10}
  - 9 points, denser near T_c to resolve transition structure
  - Each q has its own T_c, so T values are `T_k = (ratio) · T_c(q)`

**Grid cardinality:** 4 q-values × 3 lattice sizes × 9 T points = **108 configurations**.

### 3.3 MC parameters per configuration

- Algorithm: **Metropolis-Hastings single-site** (matches existing `potts_fim_test.py` infrastructure; Swendsen-Wang cluster would be faster but changes FIM interpretation — keep Metropolis for consistency)
- Equilibration sweeps: **N_equil = 10,000** (higher than existing 8,000 because first-order transitions near T_c need longer)
- Measurement sweeps: **N_measure = 20,000** (higher than existing 15,000 for same reason)
- Sampling cadence: measure every **10 sweeps** → 2,000 samples per configuration
- Independent seeds: **5 replicas** per configuration for error bars
- Near T_c for q=5,7,10: **doubled equilibration** due to metastability at first-order transition

**Total MC runtime budget:** 108 configs × 5 replicas = 540 independent runs. Per-run ~1-10 minutes depending on L and q. Total: **~1-3 days on workstation, ~12 hours on RTX 2000 GPU**.

### 3.4 Observables per MC sample

From each MC sample, compute:

**Observable set A — CCA (pure 2-point):**
1. Connected correlation matrix χ_ij = ⟨s_i s_j⟩ - ⟨s_i⟩⟨s_j⟩ for all site pairs (i,j)
2. Eigenspectrum {λ_1, λ_2, ...} of χ
3. `d_eff_CCA = (Σ λ_k)² / Σ λ_k²`
4. `η_CCA` from power-law fit to eigenvalue tail (follow existing `fisher_diagnostics.analyze_node` convention)

**Observable set B — Brown 2022 (hybrid 2-point + multi-point):**
5. Global Transfer Entropy (GTE): `GTE = Σ_i H(s_i^{t+1} | s_i^t) - H(s_i^{t+1} | s_i^t, S^t_{¬i})`
   - Follow Brown-Bossomaier-Barnett 2022 specification precisely; download paper first
   - Requires estimating conditional entropies from MC time-series (separate analysis pass)

**Observable set C — Standard exponents (for reduction-check):**
6. Order parameter ⟨m⟩ and susceptibility χ_{magnetic} (for β/ν extraction)
7. Two-point correlation ⟨s_0 s_r⟩ at criticality (for η_std = η_critical extraction via fit `⟨s_0 s_r⟩ ~ r^{-(d-2+η_std)}`)

### 3.5 Averaging

- Within-replica average over N_measure samples
- Across-replica average of 5 replicas → mean ± SEM

---

## 4. Success criteria

### 4.1 Reduction-check (R1 vs R2)

At T_c for q=2 (Ising):
- Compute d_eff_CCA, η_CCA from sweep
- Compute FSS prediction: from η_critical = 1/4 and β/ν = 1/8, what do d_eff_CCA and η_CCA predict under power-law eigenvalue density? (Need to derive the prediction analytically — see Vinayak 2014 for framework.)
- Compare: |observed - predicted| / SEM
  - < 2σ → **R1 (reduction confirmed)**
  - > 3σ → **R2 (something else captured)**

### 4.2 Brown comparison (A vs B vs C)

For each q ∈ {2, 5, 7, 10}:
- Compute d_eff_CCA(T/T_c) curve
- Compute η_CCA(T/T_c) curve
- Compute GTE(T/T_c) curve
- Plot all three on same axes, one subplot per q

**Discrimination metric per observable:** magnitude of peak-height difference between q=2 and q=10 curves, normalized by q=2 peak.
- `discrim_d_eff = |peak(d_eff_CCA, q=10) - peak(d_eff_CCA, q=2)| / peak(d_eff_CCA, q=2)`
- `discrim_η = ...`
- `discrim_GTE = ...`

**Outcome classification:**

| Condition | Outcome |
|---|---|
| `discrim_d_eff > 0.5 · discrim_GTE` AND peak positions track | **A — CCA tracks GTE** |
| `discrim_d_eff < 0.2 · discrim_GTE` OR peak positions diverge | **B — CCA misses** |
| intermediate OR CCA discriminates differently (different q-ordering) | **C — different information** |

### 4.3 Mechanism question (if outcome A)

If CCA tracks GTE: does the interfacial-length mechanism Brown 2022 proposes for GTE also explain CCA's curve shape? Measure FK cluster interfacial length at each (q, T, L) via existing cluster-identification code and correlate with d_eff_CCA.

### 4.4 Go/no-go threshold for status promotion

**For CCA-1c to move from Speculative → Supported:**
1. Outcome A confirmed at p < 0.01 via bootstrap over replicas
2. Reduction-check R1 confirms no novel content AT T_c (so novelty lives in off-T_c or first-order behavior)
3. At least 2 of 3 first-order q values (5, 7, 10) show CCA-GTE agreement
4. Written up in `docs/CCA_POTTS_SWEEP_REPORT_2026.md` with all raw data in `data/reports/cca_potts_sweep_2026/`

If any condition fails → CCA-1c stays Speculative (or gets falsified depending on mode of failure).

---

## 5. Deliverables

### 5.1 Code to write

```
scripts/
  cca_potts_sweep_main.py       # orchestrator: runs all 108 configs × 5 replicas
  potts_mc_optimized.py         # MC core (reuse/extend from potts_fim_test.py)
  gte_analysis.py               # Global Transfer Entropy computation per Brown 2022
  reduction_check_fss.py        # derive and test FSS predictions for d_eff_CCA, η_CCA
  cca_potts_plots.py            # final plotting script
```

### 5.2 Data outputs

```
data/reports/cca_potts_sweep_2026/
  raw/
    mc_samples_q{2,5,7,10}_L{16,24,32}_T{...}_rep{0-4}.npz   # MC configurations + FIM
  derived/
    observables_by_config.csv      # d_eff_CCA, η_CCA, GTE, ⟨m⟩, χ per (q, L, T, rep)
    observables_mean_sem.csv       # same, averaged over replicas
  analysis/
    reduction_check_table.csv      # FSS predictions vs observations at T_c
    brown_comparison_table.csv     # discrim_{d_eff, η, GTE} per q
    outcome_classification.json    # A/B/C verdict with confidence
  figures/
    d_eff_vs_T_per_q.png
    eta_vs_T_per_q.png
    gte_vs_T_per_q.png
    overlay_all_observables_q{2,5,7,10}.png
    reduction_check_scatter.png
```

### 5.3 Report

```
docs/
  CCA_POTTS_SWEEP_REPORT_2026.md   # final writeup: setup, results, outcome verdict, next steps
```

Structure the report:
1. Executive summary (1 paragraph, outcome verdict)
2. Method (points to this spec; note any deviations)
3. Reduction-check result (R1 or R2)
4. Brown comparison result (A, B, or C)
5. Mechanism analysis (if A)
6. Status implications for CCA-1c, CCA-2, STAT3, P5, P6, P7
7. M0 confidence calibration update (rows to write to `confidence_calibration` table)
8. Honest limitations + known gaps

### 5.4 Confidence calibration update

After completing, write a calibration migration:
```
scripts/migrations/m0_cca_potts_sweep_2026_MM_DD.py
```
that inserts rows into `wiki_history.db.confidence_calibration` for:
- `CCA-1c` (outcome-dependent: Supported / Speculative / Falsified)
- `STAT3` (same)
- `P5`, `P6` (may gain confirmation or disconfirmation evidence)

---

## 6. Implementation gotchas

### 6.1 First-order metastability

At q=5,7,10 near T_c, the Metropolis MC sees two metastable phases (ordered / disordered) with exponentially slow tunneling. Single long runs may get stuck in one phase and give biased correlations.

Mitigation:
- Double equilibration near T_c
- Use multiple seeds per (q, L, T) and verify phase identified correctly by looking at ⟨m⟩ distribution
- For strongly first-order (q=10), consider multicanonical sampling if standard MC produces hysteresis
- Flag and discard any replica that shows obvious phase-trapping

### 6.2 FIM computation

FIM in CCA framework is the connected correlation matrix χ_ij — not a finite-difference numerical derivative. Compute directly from MC samples:
```
χ_ij = ⟨s_i s_j⟩ - ⟨s_i⟩⟨s_j⟩   (for Ising; for Potts use appropriate q-state generalization)
```

For Potts q>2, the "spin" is categorical. The canonical generalization uses Kronecker delta or projection onto a preferred direction (depends on Brown's convention — match Brown's choice for apples-to-apples GTE comparison).

### 6.3 GTE estimation

Conditional entropies from finite samples are notoriously biased. Follow Brown-Bossomaier-Barnett 2022's exact estimator choice. If their paper specifies plug-in estimator vs Miller-Madow correction vs KSG estimator, use the same.

Don't use mutual-information estimator as a stand-in — GTE is different.

### 6.4 η_CCA fitting

Power-law fit to eigenvalue tail is sensitive to:
- Where the tail starts (fit range must exclude bulk)
- Finite-size cutoffs

Report η_CCA with fit-range sensitivity analysis (try 2-3 different tail definitions; report range).

### 6.5 CPU vs GPU

MC loops in pure Python-Numpy are slow. Options:
- **Numba `@njit`** on the inner sweep loop — 10-100x speedup
- **CuPy** on GPU for the correlation matrix accumulation
- **C extension** via Cython for maximum speed

The existing `scripts/potts_fim_test.py` is pure Numpy. For the full 108-config sweep, Numba is probably the right trade-off.

### 6.6 Reproducibility

- Fix all seeds deterministically as function of (q, L, T, replica_index)
- Log scikit / numpy / torch versions in every output file
- Save git commit hash alongside results

---

## 7. Prior-art gate (per charter)

Before running the experiment:

1. **Download and read Brown-Bossomaier-Barnett 2022 in full.** Not just the abstract. Understand their exact GTE definition, estimator, lattice sizes, and conclusion.
2. **Download and read Vinayak-Prosen-Buča-Seligman 2014 EPL 108, 20006.** This is the analytical framework for correlation-matrix eigenvalue density at criticality — will inform the reduction-check derivation.
3. **Download and read Borgs-Chayes 1996 J. Stat. Phys. 82, 1235.** Rigorous Potts-covariance-vs-FK-cluster mapping; will inform any mechanism claim.
4. **Check for newer prior art** via arXiv since 2024-01 on "Potts model Fisher information" or "Potts eigenvalue spectrum" — if someone published the comparison in the last 2 years, update scope.

Use GSW lookup for live prior-art:
```bash
python3 scripts/gsw_lookup.py "Potts model Fisher information eigenvalue spectrum" --top-k 20
python3 scripts/gsw_lookup.py "global transfer entropy Potts critical" --top-k 15
```

---

## 8. Owner decisions required before running

1. **Approve budget:** ~24,000 MC runs; 1-3 days workstation / ~12h GPU. OK?
2. **Approve deviation from `potts_fim_test.py` MC params:** N_equil 8000→10000, N_measure 15000→20000, add q=5,7 (currently only q=2,10). OK?
3. **GPU or CPU?** RTX 2000 on ShadowPC available per CLAUDE.md. Prefer.
4. **Stop conditions:** should the experiment auto-abort if outcome is determined early (e.g., q=2 reduction-check fails at L=16 obvious-large-deviation)? Or always complete the full sweep for completeness?

---

## 9. What this experiment does NOT settle

- **Whether CCA has value beyond the Potts problem.** Other lattice models (Heisenberg, XY), off-lattice continuous systems, quantum systems all remain untested.
- **Whether the wiki's Fisher-gravity chain (GT01→GT10) is correct.** P7's monotonicity was falsified separately; this experiment doesn't touch the gravity thread.
- **Whether the whole DFIG framework is a re-parameterization of sloppy models.** The M0 audit's broader question is not resolved by a single experiment; this experiment resolves one specific sub-question.

Per the charter: **one experiment at a time, honest documentation, no silent promotion.** Whatever outcome this produces, the status moves go into `confidence_calibration` with explicit audit_ref.

---

## 10. Appendix — file-map reference

| Path | Purpose |
|---|---|
| `docs/CCA_MATHEMATICAL_FORMALIZATION.md` | Full CCA math spec (pre-M0; read with skepticism per M0 findings) |
| `docs/M0_MILESTONE_COMPILATION.md` | M0 audit findings including Fourth Addendum (Brown 2022) |
| `docs/SESSION_HANDOVER_2026-04-16.md` | M0 closeout, explicit statement of the open question this experiment answers |
| `docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md` | d_eff and η naming collisions — resolve in report writeup |
| `data/wiki_history.db` | `confidence_calibration` table has M0 baseline for STAT3, P5, P6, P7 |
| `scripts/potts_fim_test.py` | **Reuse this MC core** |
| `src/analysis/fisher_diagnostics.py` | `analyze_node()` does the FIM work |

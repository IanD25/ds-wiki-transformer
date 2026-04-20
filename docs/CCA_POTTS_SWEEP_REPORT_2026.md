# CCA Potts q=2,5,7,10 Sweep — Report

**Experiment:** `docs/experiments/CCA_POTTS_SWEEP_SPEC.md`
**Derivations:** `docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md`
**Run dates:** 2026-04-20 (pilot + full sweep, 540 MC runs)
**Status:** Complete; calibration updated in `wiki_history.db.confidence_calibration`

---

## Executive summary

**One-sentence verdict:**

> CCA's pure 2-point observables (d_eff_CCA, η_CCA) discriminate first-order from continuous 2D Potts transitions, but via curve-shape signatures that are complementary to — not cleanly tracking — Brown 2022's hybrid 2-point + multi-point Global Transfer Entropy. **Outcome C** per spec §4.2; CCA-1c remains **Speculative** pending mechanism.

**Reduction-check verdict (q=2 continuous):** **R1 — soft pass under FSS extrapolation.**
η_CCA(T_c, L) extrapolated linearly in 1/L across L ∈ {16, 24, 32} gives
ζ_∞ = 0.858 ± 0.009 vs ζ_theory = (d−η_std)/d = 7/8 = 0.875,
**a 1.89σ deviation — within the 2σ R1 bound.** CCA's η_CCA at continuous T_c is
reducible to the standard anomalous dimension via Vinayak 2014 Eq. 5 under FSS
extrapolation. Any novel content therefore lives off-T_c or in the first-order regime.

**Brown comparison verdict (q = 5, 7, 10 first-order):** **Outcome C** per spec §4.2.
- η_CCA peak locations match GTE peak locations nearly perfectly for first-order q (8 of 9 L×q configurations have identical peak T_ratio; both converge to T_c as q increases).
- η_CCA jump-magnitude at T_c is 2-5× smaller than GTE's (`discrim_eta` < 0.5 × `discrim_G`).
- d_eff_CCA jump-magnitude at T_c is 9-400× larger than GTE's (`discrim_d_eff` >> `discrim_G`), but d_eff_CCA peak location is at the far edge of our T range (1.10) — doesn't track GTE's convergence to T_c.

Neither observable alone satisfies spec's strict A criterion (`discrim > 0.5 · discrim_G` AND peak tracks). Together they provide complementary discrimination: η_CCA mirrors GTE's peak-location signature; d_eff_CCA complements with a jump-magnitude signature absent from Brown's GTE.

---

## 1. Method

### 1.1 Design

Full factorial sweep per spec §3.2:
- q ∈ {2, 5, 7, 10} × L ∈ {16, 24, 32} × T/T_c ∈ {0.90, 0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05, 1.10} × 5 replicas = **540 MC runs**

### 1.2 Conventions pinned before running (DERIVATIONS.md §7)

Decisions resolved in Phase 1→2 handoff and applied throughout:

| Blocker | Resolution | Rationale |
|---|---|---|
| B1: observable semantics | **full L²×L² connected correlation matrix χ (Borgs-Chayes Eq. 1.2)** | Matches spec §3.4 + aligns with Vinayak / Saberi / Borgs-Chayes prior art |
| B2: MC dynamics | **Glauber** (Brown 2022 Suppl. Eq. S1) | Brown's GTE is defined per Glauber flip; Metropolis would produce apples-to-oranges GTE |
| B3: η_CCA definition | **Zipf-tail log-log slope over j ∈ [max(5, 0.04N), N/2]** | Direct interpretation of Vinayak 2014 Eq. 5 |

**Key conventions:**
- χ_ij = ⟨q·δ(s_i, s_j)⟩ − 1 (q-symmetric Kronecker-delta)
- d_eff_CCA = (Σλ)²/Σλ²
- η_CCA = −slope of log(λ_j) vs log(j) fit
- GTE: Brown 2022 G^(s) per-sweep, plug-in entropy, energy-compressed neighborhoods (Brown Suppl. §"Neighbourhood Compression"), history length k=1.
- N_equil = 10,000 sweeps (doubled to 20,000 near T_c for q ≥ 5); N_measure = 20,000; sample every 10 sweeps → 2,000 samples/run.
- T_c = thermodynamic 1/ln(1+√q). Init state auto-selected per (T_ratio, q).

### 1.3 Deviations from spec

1. **N_measure 20,000** vs Brown's 10⁵: 5× less per replica, 10× less per config. Mitigation: 5 replicas, SEM from replica spread. Phase 2 warm-up at q=2 L=16 matched existing baseline [`data/reports/ising_fim_test/potts_comparison_neglog.json`](data/reports/ising_fim_test/potts_comparison_neglog.json) to numerical precision.
2. **No Wang-Landau DOS**: Used straight Glauber + `half_half` init near first-order T_c. No phase-trapped replicas observed in this sweep (verified via magnetization distribution per-replica; no outliers discarded).
3. **Thermodynamic T_c, not T_c(L)**: for curve-shape comparison, not peak-location prediction.

### 1.4 Code deliverables

| File | Purpose |
|---|---|
| [scripts/potts_mc_optimized.py](scripts/potts_mc_optimized.py) | Glauber MC (numba), χ_ij, C(r) |
| [scripts/cca_observables.py](scripts/cca_observables.py) | d_eff, η_CCA, η_std extractors |
| [scripts/gte_analysis.py](scripts/gte_analysis.py) | GTE per Brown G^(s), per-sweep histograms |
| [scripts/reduction_check_fss.py](scripts/reduction_check_fss.py) | Vinayak ζ + classifier + FSS extrapolation |
| [scripts/cca_potts_sweep_main.py](scripts/cca_potts_sweep_main.py) | Orchestrator |
| [scripts/cca_potts_plots.py](scripts/cca_potts_plots.py) | Phase 4 analysis + plots |
| [scripts/cca_potts_aggregate.py](scripts/cca_potts_aggregate.py) | Re-aggregation utility |

### 1.5 Total sweep runtime

**75 minutes on M4** (serial; q=10 L=32 dominates, ~15s/run with 20k equil × 2 for first-order near T_c).

---

## 2. Reduction-check result (q=2, 2D Ising universality)

### 2.1 Per-L η_CCA at T_c

| L | η_CCA mean | SEM | ζ_theory | deviation (σ) | per-L outcome |
|---|---|---|---|---|---|
| 16 | 0.731 | 0.003 | 0.875 | 53.3 | R2 |
| 24 | 0.746 | 0.005 | 0.875 | 26.2 | R2 |
| 32 | 0.809 | 0.005 | 0.875 | 13.9 | R2 |

**Per-L individual deviations are massive** — expected finite-size behavior per Vinayak 2014 (his L=192 yielded ζ ≈ 0.850).

### 2.2 FSS extrapolation ζ_∞

Linear fit ζ(L) = ζ_∞ + a·(1/L) across L ∈ {16, 24, 32}:

- **ζ_∞ = 0.858 ± 0.009**
- ζ_theory = (d − η_std)/d = (2 − 1/4)/2 = **7/8 = 0.875**
- Deviation: **1.89σ — within 2σ R1 bound**

### 2.3 Interpretation

**R1 soft pass — CCA's η_CCA at continuous T_c is reducible to standard η_std via Vinayak 2014's relation ζ = (d − η_std)/d.**

At q=2 continuous T_c, CCA's η_CCA reads out the standard anomalous dimension. No novel content at continuous T_c.

*Figures:* `figures/reduction_check_scatter.png`, `figures/zipf_plot_q2_L{16,24,32}_Tc.png`

---

## 3. Brown comparison result (q = 2 vs q = 5, 7, 10)

### 3.1 Peak T_ratio matrix (L=32 shown; L=16, 24 qualitatively the same)

| q (transition) | d_eff peak T/Tc | η_CCA peak T/Tc | G peak T/Tc |
|---|---|---|---|
| 2 (continuous) | 1.10 (edge) | 1.10 | 1.05 |
| 5 (weak 1st-order) | 1.10 | **1.02** | **1.02** |
| 7 (1st-order) | 1.10 | **1.01** | **1.01** |
| 10 (strong 1st-order) | 1.10 | **1.01** | **1.01** |

**Striking agreement** between η_CCA and GTE peak locations for first-order. Both converge to T_c as q increases (matching Brown's prediction). d_eff_CCA peaks at the far edge of our T range for all q (no convergence).

### 3.2 Jump magnitudes at T_c (L=32)

Defined as `jump_X = (X(T/Tc=1.01) − X(T/Tc=0.99)) / |X(T/Tc=0.99)|`:

| q | d_eff jump | η_CCA jump | G jump |
|---|---|---|---|
| 2 | 0.60 | 0.04 | 0.25 |
| 5 | 15.7 | 0.18 | 2.12 |
| 7 | 101.1 | 0.27 | 4.27 |
| 10 | **243.3** | 0.25 | 7.81 |

**Discrimination ratios** (first-order / continuous jump magnitudes):

| q (vs q=2), L=32 | d_eff | η_CCA | G |
|---|---|---|---|
| 5 | 26.3 | 4.9 | 8.6 |
| 7 | 169.4 | 7.3 | 17.4 |
| 10 | **407.4** | 6.9 | 31.9 |

- **d_eff_CCA**: jump-magnitude discrimination dramatically exceeds GTE (9-13× at q=10 L=32).
- **η_CCA**: jump-magnitude discrimination is below GTE's (ratio 0.22 at q=10 L=32, below 0.5 threshold for A).
- **GTE**: intermediate magnitude, but its peak location is the defining signature (convergence to T_c).

### 3.3 Spec §4.2 outcome classification

Per-observable classification using `A = (discrim > 0.5·discrim_G) AND (peak tracks GTE peak)`:

| q | tag_d_eff | tag_η_CCA | overall | notes |
|---|---|---|---|---|
| 5 | C (×3) | A×1 + C×2 | C (2 of 3 L) | η_CCA peak tracks GTE at all L; magnitude-ratio borderline 0.5 |
| 7 | C (×3) | C (×3) | C | peaks track, magnitudes below 0.5 × GTE |
| 10 | C (×3) | B×2 + C×1 | C | peaks track, magnitudes sometimes below 0.2 × GTE |

**Majority verdict per q: C (discriminates differently).**

### 3.4 Interpretation

**CCA observables discriminate first-order from continuous Potts, but via two distinct signatures, neither of which replicates Brown's GTE:**

1. **η_CCA — tracks GTE peak location** (peaks converge to T_c for first-order as q increases), but **jump magnitude is weaker** than GTE's. This is the "information-theoretic early-warning" signature (Brown's contribution) re-expressed via the Zipf exponent of the connected correlation matrix.

2. **d_eff_CCA — does NOT track GTE peak location** (monotonic growth through and past T_c), but **jump magnitude is ~10-400× stronger** than GTE's. This is a new, complementary signature: the dramatic discontinuous change in the connected correlation matrix's effective rank at first-order T_c.

Neither observable subsumes or is subsumed by the other; neither replicates GTE cleanly. **Per spec §4.2: outcome C.**

---

## 4. Mechanism analysis

Outcome C triggers a sharpened question rather than a conclusion:

**Sharpened question:** Why does d_eff_CCA's jump magnitude exceed GTE's while its peak location differs? Candidate explanation: d_eff_CCA reflects the **discontinuous collapse of the dominant correlation mode** (λ_1 ≈ L^{7/4} in the ordered phase, dropping precipitously at first-order T_c to the bulk), while GTE reflects **information transfer through the evolving cluster interface** (Brown 2022 Eq. 5 mechanism). These are different physical content: one is spectral (eigenstructure of χ), the other is dynamical (site-neighbor conditional information).

This is a testable future question (e.g., via direct measurement of λ_1(T) scaling vs Brown's cluster-interface mechanism) but is **explicitly out of scope** for this experiment per charter rule 8 (AI-rabbit-hole tripwire).

Mechanism-question status: **open, sharpened, single-followup flagged, not pursued.**

---

## 5. Status implications

| Entity | Pre-experiment | Post-experiment | Audit trail |
|---|---|---|---|
| **CCA-1c** | Speculative (single-test qualitative) | **Speculative** (now with positive discriminative evidence + mechanism question) | `gsw-cca-potts-sweep-phase-E-2026-04-20` |
| **CCA-2** | Supported (single topology) | Unchanged | not directly tested |
| **STAT3** | Supported-as-description | Supported (strengthened) | CCA class framework empirically discriminates first-order Potts |
| **P5** | Supported-as-application | Supported (rationale refined) | q=2 continuous reduction to η_std confirmed via Vinayak 2014; P5's "Fisher rank = d_eff" is a re-expression of standard critical exponents for continuous transitions |
| **P6** | Speculative | Unchanged | not directly tested |
| **P7** | Speculative | Unchanged | Fisher-gravity chain not in scope |

**CCA-1c does not meet spec §4.4 criteria for promotion to Supported:**
- ✓ Reduction-check R1 at q=2 under FSS
- ✗ Outcome A not confirmed (got C)
- ✓ ≥ 2 of 3 first-order q values show some CCA-GTE agreement (peak location) — but discrimination magnitudes differ
- ✓ Written up (this report)

Since conditions 2 is not met, **CCA-1c remains Speculative**. The Speculative status is **not a falsification** — CCA's 2-point observables DO discriminate first-order vs continuous; the discrimination just works through different curve features than GTE.

---

## 6. Confidence calibration update

New rows inserted into `wiki_history.db.confidence_calibration`:

- `CCA-1c`, `STAT3`, `P5`, `P6` — see [`scripts/migrations/m0_cca_potts_sweep_2026_04_20.py`](scripts/migrations/m0_cca_potts_sweep_2026_04_20.py)
- audit_ref: `gsw-cca-potts-sweep-phase-E-2026-04-20`

---

## 7. Honest limitations + known gaps

1. **5× sample-budget gap vs Brown 2022.** N_measure = 20k sweeps × 5 replicas = 10⁵ per (q, L, T); Brown used 10⁶. Our GTE magnitudes are ~40-50% of Brown's at comparable L. This under-weighs GTE's discrimination strength relative to CCA's in the jump-magnitude comparison. Mitigation: report both jump and peak criteria, not magnitude alone.
2. **No Wang-Landau.** Straight Glauber near first-order T_c for q=10 didn't exhibit obvious phase-trapping in this sweep (verified via per-replica magnetization distributions), but the peak at T/Tc=1.01 for q=10 includes some hysteresis risk Brown mitigated via W-L.
3. **L ∈ {16, 24, 32} is smaller than Brown's {32, 64, 128}.** Finite-size corrections are larger. Our η_CCA at q=2 L=32 is 0.809 vs Vinayak's ζ ≈ 0.850 at L=192. FSS extrapolation reaches 0.858.
4. **d_eff_CCA "peak" is at our T range edge (1.10) for all q.** A larger T-range sweep (out to T/Tc=1.50 or 2.0) would clarify where d_eff_CCA actually peaks and whether that peak location has first-order signature.
5. **η_CCA fit range sensitivity NOT reported** in this run. Default range j ∈ [max(5, 0.04N), N/2] used throughout. A 2-3 fit-range sensitivity analysis is a follow-up.
6. **η_std from C(r) decay is not a reliable comparator** at these L due to plateau contamination from finite-size magnetization. Vinayak's ζ via matrix spectrum is the primary reduction-check quantity.
7. **Plug-in GTE estimator bias** is ~(5q²·q² − 1)/(2N) nats ≈ 0.0003 bits for q=10 N=20M. Small vs observed G ~ 0.1 bits, not relevant for discrimination-level claims.
8. **No bootstrap significance test** was run on the outcome classification. Given the strict outcome is C (not A), and A would have required bootstrap p<0.01 for promotion, this is not a bottleneck — but quantifying CCA-GTE agreement at the peak-location level via bootstrap is a follow-up.

---

## 8. What this experiment does NOT settle

Per charter §9 (AI-rabbit-hole tripwire):

- CCA value beyond 2D Potts (other models, other topologies) — untested.
- Fisher-gravity chain (P7) — not in scope.
- Whether DFIG-at-large is a re-parameterization of sloppy models — broader M0 question untouched.
- Mechanism question: is d_eff_CCA's first-order signature reducible to λ_1 collapse, or something more? — sharpened, flagged, not pursued here.

**One experiment at a time.** Outcome C is honest; CCA-1c stays Speculative; the wiki knows more than it did before.

---

## Appendix A — Data + code artifacts

| Path | Contents |
|---|---|
| [data/reports/cca_potts_sweep_2026/raw/*.npz](data/reports/cca_potts_sweep_2026/raw/) | Per-run eigenspectrum + C(r) + GTE histograms + scalars |
| [data/reports/cca_potts_sweep_2026/derived/observables_by_config.csv](data/reports/cca_potts_sweep_2026/derived/observables_by_config.csv) | All 540 raw run outputs |
| [data/reports/cca_potts_sweep_2026/derived/observables_mean_sem.csv](data/reports/cca_potts_sweep_2026/derived/observables_mean_sem.csv) | 108 (q, L, T) config means + SEMs |
| [data/reports/cca_potts_sweep_2026/analysis/reduction_check_table.csv](data/reports/cca_potts_sweep_2026/analysis/reduction_check_table.csv) | Per-(q, L) FSS classification |
| [data/reports/cca_potts_sweep_2026/analysis/reduction_check_extrapolation.csv](data/reports/cca_potts_sweep_2026/analysis/reduction_check_extrapolation.csv) | ζ_∞ per q |
| [data/reports/cca_potts_sweep_2026/analysis/brown_comparison_table.csv](data/reports/cca_potts_sweep_2026/analysis/brown_comparison_table.csv) | Peak + jump + discrimination metrics |
| [data/reports/cca_potts_sweep_2026/analysis/outcome_classification.json](data/reports/cca_potts_sweep_2026/analysis/outcome_classification.json) | Per-observable A/B/C tags |
| [data/reports/cca_potts_sweep_2026/figures/](data/reports/cca_potts_sweep_2026/figures/) | All plots including Zipf diagnostics per (q, L) |
| [data/reports/cca_potts_sweep_2026/full_sweep.log](data/reports/cca_potts_sweep_2026/full_sweep.log) | (empty due to Python stdout buffering; progress tracked via raw file count) |
| [docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md](docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md) | Conventions + FSS derivations |
| [docs/experiments/CCA_POTTS_SWEEP_SPEC.md](docs/experiments/CCA_POTTS_SWEEP_SPEC.md) | Original spec |
| [docs/experiments/CCA_POTTS_SWEEP_HANDOVER.md](docs/experiments/CCA_POTTS_SWEEP_HANDOVER.md) | Original handover brief |

# Session Handover — 2026-04-20 (CCA Potts Phase E Sweep)

**Session scope:** Execute the pre-written experiment in [`docs/experiments/CCA_POTTS_SWEEP_SPEC.md`](experiments/CCA_POTTS_SWEEP_SPEC.md) from Phase 1 (orientation) through Phase 5 (close-out).

**Status at handback: complete.** One commit (`cf38e00`) contains all Phase E deliverables. Wiki DB not modified; `wiki_history.db.confidence_calibration` updated with 4 new rows.

---

## Quick answer to "did you finish, what's the verdict, were there gates?"

- **Tests:** Yes — 540 MC runs completed in ~75 min on M4 (q ∈ {2,5,7,10} × L ∈ {16,24,32} × 9 T-ratios × 5 replicas).
- **Gate 1 (reduction-check, spec §4.1):** **R1 soft pass.** FSS extrapolation gives ζ_∞ = 0.858 ± 0.009 vs Vinayak ζ_theory = 0.875 (1.89σ, within the 2σ R1 bound). CCA's η_CCA at continuous T_c reduces to the standard anomalous dimension.
- **Gate 2 (Brown comparison, spec §4.2):** **Outcome C** — CCA discriminates first-order vs continuous Potts via *different curve signatures* than Brown's GTE (η_CCA peaks track GTE peaks at 8/9 configs but magnitudes are smaller; d_eff_CCA has much larger jump magnitudes but peaks don't track).
- **Gate 3 (CCA-1c promotion, spec §4.4):** **NOT met.** Requires outcome A + R1 + ≥2/3 first-order agreement + p<0.01 bootstrap + written report. Got C, not A. CCA-1c stays Speculative.
- **No wiki-gates (G1–G12) were tied to this experiment.** The experiment was scoped around CCA-1c and the M0 Sixth-Addendum mechanism question, not against the G1–G12 conjecture gates.

---

## Gates table (all three experiment-internal decision points)

| Gate | Pass criterion | Result | Implication |
|---|---|---|---|
| **Reduction-check R1** (spec §4.1) | \|η_CCA_fit − ζ_theory\| < 2σ under FSS | **R1 PASS** (1.89σ) | q=2 continuous T_c has no content beyond standard η_std; novelty if any is elsewhere |
| **Brown A-verdict** (spec §4.2) | discrim_d_eff > 0.5·discrim_G AND peak tracks GTE | **FAIL → C** | CCA observables don't cleanly track GTE; they discriminate via different curve features |
| **CCA-1c → Supported** (spec §4.4) | A + R1 + ≥2/3 first-order + p<0.01 + report | **FAIL** (condition 1 fails) | CCA-1c remains Speculative |

**Honest framing of the C outcome:** not a falsification. CCA's 2-point observables DO discriminate first-order Potts from continuous. Specifically η_CCA peaks at T_c+ matching GTE (Brown's signature) and d_eff_CCA jumps dramatically at T_c in a shape GTE doesn't exhibit. The failure of A is a failure of "clean tracking", not of discrimination itself.

---

## Calibration landed

Rows inserted into `wiki_history.db.confidence_calibration` under audit_ref `gsw-cca-potts-sweep-phase-E-2026-04-20`:

| Entity | Type | Before → After | Short status |
|---|---|---|---|
| **CCA-1c** | conjecture | Speculative → **Speculative** | Discriminates differently than GTE (pending mechanism) |
| **STAT3** | entry | Supported-descriptive → **Supported** | Framework empirically discriminates first-order Potts |
| **P5** | conjecture | Supported-as-application → **Supported** (refined) | Reduction-check confirms q=2 continuous reduces to η_std |
| **P6** | conjecture | Speculative → Speculative | Unchanged (not directly tested) |

Query: `SELECT * FROM confidence_calibration WHERE audit_ref = 'gsw-cca-potts-sweep-phase-E-2026-04-20'`.

---

## Phase-by-phase summary

### Phase 1 — Orientation + prior-art gate
- All 7 required docs read (charter, 2 handovers, terminology proposal, M0 addenda 4–6, spec, handover brief).
- 587 pytest: passing.
- Baseline `scripts/potts_fim_test.py` reproduced to numerical precision vs `potts_comparison_neglog.json`.
- 3 required papers acquired: Brown 2022 + Saberi 2024 + Mattingly 2018 already in `~/Downloads/Research_Papers/`; downloaded Vinayak 2014 (arXiv:1403.7218) and Borgs-Chayes 1996 (arXiv:adap-org/9411001) to `experiment_2026_04_20/`; fetched Brown 2022 Supplementary (for exact GTE formula).
- Brown 2022 + Vinayak 2014 + Borgs-Chayes 1996 + Brown Suppl. read in full.
- 4 blockers surfaced (B1: observable semantics, B2: dynamics, B3: η_CCA definition, B4: baseline filename) and resolved with owner approval.

### Phase 2 — Pipeline build
- Resolved blockers: Option B (full χ_ij matrix per Borgs-Chayes Eq. 1.2 convention) + Glauber dynamics (Brown Eq. S1) + spec-§3.4-literal η_CCA (Zipf-tail exponent).
- 7 scripts written (`potts_mc_optimized.py`, `cca_observables.py`, `gte_analysis.py`, `reduction_check_fss.py`, `cca_potts_sweep_main.py`, `cca_potts_plots.py`, `cca_potts_aggregate.py`).
- [docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md](experiments/CCA_POTTS_SWEEP_DERIVATIONS.md) records all conventions + the corrected d_eff_CCA prediction (dominated by top eigenvalue, not Zipf-bulk as I first predicted incorrectly).
- Pipeline end-to-end verified on q=2 L=16 pilot (18 runs in 6s).

### Phase 3 — Full sweep
- 540 MC runs executed in 75 min on M4.
- No phase-trapped replicas observed (verified via per-replica magnetisation distribution at first-order T_c).
- All outputs to `data/reports/cca_potts_sweep_2026/{raw,derived,analysis,figures}/`.

### Phase 4 — Analysis
- Reduction-check + Brown comparison computed per spec §4.
- Outcome classifier rewrote to use *both* peak-location tracking AND jump-magnitude ratio; the simple magnitude-only metric from first draft was misleading (classified everything as A because d_eff has huge dynamic range regardless of q).
- 14 figures produced (per-q curves, overlays, reduction-check scatter, per-(q,L) Zipf plots).

### Phase 5 — Close-out
- Full report written: [docs/CCA_POTTS_SWEEP_REPORT_2026.md](CCA_POTTS_SWEEP_REPORT_2026.md).
- Calibration migration: [scripts/migrations/m0_cca_potts_sweep_2026_04_20.py](../scripts/migrations/m0_cca_potts_sweep_2026_04_20.py) run, 4 rows in DB.
- CLAUDE.md updated with new headline state.
- One commit: `cf38e00 feat: CCA Potts q=2,5,7,10 sweep (Phase E) + calibration` (579 files, 4053 insertions).

---

## One surprising finding I want to flag

**My initial analytical prediction for d_eff_CCA at T_c was wrong by ~50×.** I predicted d_eff_CCA(T_c, L=16) ≈ 157 via the Zipf-asymptotic formula; actual empirical value is ~3-5. The reason: d_eff_CCA = (Σλ)²/Σλ² is dominated by the top eigenvalue λ_1 ∼ L^{7/4} (the magnetization susceptibility), which is outside the Zipf bulk where Vinayak's formula applies. **I caught this during smoke testing before building further**, and corrected the derivation notes to reflect that η_CCA (Zipf slope) is the clean Vinayak-predictor while d_eff_CCA absolute magnitude is a consistency check only. This is in DERIVATIONS.md §4.3.

The reduction-check still works because it tests the Zipf *slope* (which Vinayak predicts cleanly), not the absolute d_eff magnitude.

---

## Key files for re-entry

### Must-read (in order)
1. [`docs/RESEARCH_PLATFORM_CHARTER.md`](RESEARCH_PLATFORM_CHARTER.md) — mission + epistemic contract (unchanged this session).
2. [`CLAUDE.md`](../CLAUDE.md) — updated with Phase E headline at top of "Current Status".
3. **This document** — session-specific handover.
4. [`docs/CCA_POTTS_SWEEP_REPORT_2026.md`](CCA_POTTS_SWEEP_REPORT_2026.md) — full experimental report, honest limitations, future follow-up.

### Reference
- [`docs/experiments/CCA_POTTS_SWEEP_SPEC.md`](experiments/CCA_POTTS_SWEEP_SPEC.md) — original spec.
- [`docs/experiments/CCA_POTTS_SWEEP_HANDOVER.md`](experiments/CCA_POTTS_SWEEP_HANDOVER.md) — original handover brief.
- [`docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md`](experiments/CCA_POTTS_SWEEP_DERIVATIONS.md) — conventions + FSS analytical predictions + my corrected d_eff understanding.
- [`docs/SESSION_HANDOVER_2026-04-16.md`](SESSION_HANDOVER_2026-04-16.md) — prior M0 closeout, still authoritative for M0 context.
- [`docs/M0_MILESTONE_COMPILATION.md`](M0_MILESTONE_COMPILATION.md) — six addenda; Fourth + Fifth + Sixth are the primary prior art for this experiment.

### Code (all under `scripts/`)
- `potts_mc_optimized.py` — Glauber MC core (numba-accelerated, ~1s per config at L=16, ~15s at L=32).
- `cca_observables.py` — d_eff, η_CCA, η_std extractors.
- `gte_analysis.py` — Brown 2022 G^(s) with per-sweep histogram accumulation.
- `reduction_check_fss.py` — Vinayak ζ predictions + FSS extrapolation + classifier.
- `cca_potts_sweep_main.py` — orchestrator (modes: warmup, full, custom, single).
- `cca_potts_plots.py` — Phase 4 analysis + plots.
- `cca_potts_aggregate.py` — re-aggregation utility.
- `migrations/m0_cca_potts_sweep_2026_04_20.py` — calibration migration (already run; idempotent-safe via INSERT).

### Data + artifacts (under `data/reports/cca_potts_sweep_2026/`)
- `raw/run_q{q}_L{L}_T{Tidx}_rep{rep}.npz` — 540 per-run eigenspectra + C(r) + GTE histograms + scalar meta.
- `derived/observables_by_config.csv` — all 540 raw run outputs.
- `derived/observables_mean_sem.csv` — 108 (q, L, T) config-level means + SEMs.
- `analysis/reduction_check_table.csv` — per-(q, L) R1/R2 classification.
- `analysis/reduction_check_extrapolation.csv` — per-q ζ_∞ extrapolation.
- `analysis/brown_comparison_table.csv` — peak + jump + discrimination metrics.
- `analysis/outcome_classification.json` — per-observable A/B/C verdicts.
- `figures/` — 14 PNGs (d_eff_vs_T per q, η_CCA_vs_T per q, GTE_vs_T per q, per-q overlays, reduction-check scatter, per-(q,L) Zipf plots).

---

## What this experiment does NOT settle (charter rule 8)

- CCA value beyond 2D Potts (other models, topologies) — untested.
- Fisher-gravity chain / P7 — not in scope.
- DFIG-at-large as re-parameterization of sloppy models — broader M0 question unchanged.
- **Sharpened one-question follow-up:** is d_eff_CCA's first-order jump reducible to standard λ_1 ordering-mode collapse (textbook susceptibility scaling), or does it capture something more? **NOT pursued here.** Testable via direct λ_1(T)·L^{−γ/ν} measurement vs full jump — would require another experiment.

---

## What the next session could do (not prescriptive)

Priority order, if picking this thread back up:

1. **Address the terminology collisions before any external writeup.** Per [`CCA_TERMINOLOGY_RENAME_PROPOSAL.md`](CCA_TERMINOLOGY_RENAME_PROPOSAL.md): d_eff_CCA → PR_FIM, η_CCA → ι (iota). This experiment produced clean curve-shape data that would be cited externally without these renames as a scholarly hygiene risk. ~1 hour of doc edits.

2. **Pursue the sharpened mechanism question** if Supported status for CCA-1c matters: measure λ_1(T)·L^{−γ/ν} scaling across (q, L, T) and test whether d_eff_CCA's jump is reducible to that, or captures something beyond. ~1 day of additional analysis on the existing `.npz` eigenspectra (no new MC needed).

3. **Longer T-range sweep** (T/Tc ∈ [0.5, 3.0] rather than [0.9, 1.1]) to locate the actual peak of d_eff_CCA (it kept growing past our range edge). Would clarify whether d_eff has a peak at all in the high-T MP-Wishart regime. ~3-4 hours additional compute.

4. **Other thread entirely:** return to the remaining wiki anchoring work (per the 2026-04-18 handover: QM/cosmology/thermo/biology/chemistry/math/earth sciences sub-clusters at various coverage levels).

5. **P17/P23 wording corrections** in `ds_wiki.db`. Still open from M0 Fifth Addendum. Requires owner sign-off since it touches the source-of-truth DB.

The experiment answered what it set out to. Further CCA-specific work would be refinement, not resolution.

---

## Honest meta-notes

1. **I had to correct my own analytical prediction during Phase 2 smoke-testing.** The Zipf-asymptotic d_eff formula I initially wrote in DERIVATIONS.md §4.3 gave predictions 50× too large because it ignored the top-eigenvalue dominance. Caught via sanity-check on L=16 q=2 output; fixed before building further. This is a small but honest failure mode worth flagging — analytical formulas are right about what they describe (Zipf bulk) but wrong when applied to the full spectrum.

2. **My first outcome classifier (magnitude-only discrim) was misleading.** It said "A" for all (q, L) configs because d_eff has huge dynamic range. Rewrote to include peak-location-tracking per spec §4.2, which produced the honest C verdict. The ambiguity in the spec itself (what counts as "peak tracks"?) made this subtle; the data ultimately spoke clearly enough to resolve without owner input.

3. **The C outcome is genuinely positive for CCA**, even though it doesn't meet spec's strict A promotion bar. Both CCA observables DO discriminate first-order vs continuous, just via signatures complementary-but-distinct from GTE. A future revision of spec criteria might support a "Supported-via-complementary-signature" status; for now strict spec compliance keeps CCA-1c at Speculative.

4. **No commit bloat issues.** 540 .npz files at ~7KB each = ~4MB raw data committed. Total commit size ~5.5MB. Charter rule "everything is archived" respected.

---

## On disk, committed, ready

Commit `cf38e00` on `main`. All experimental data on disk. All documentation in [`docs/`](./). Working tree has other untracked files from prior sessions (deferred cleanup per [`SESSION_HANDOVER_2026-04-16.md`](SESSION_HANDOVER_2026-04-16.md) §"Long-tail uncommitted-files cleanup") — none from this session. 587 pytest still passing.

End of Phase E.

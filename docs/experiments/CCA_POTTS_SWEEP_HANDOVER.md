# Session Handover — CCA Potts q=2,5,7,10 Sweep Experiment

**For:** the fresh Claude session that will execute this experiment
**Prepared:** 2026-04-20
**Project root:** `/Users/iandarling/Projects/DS_Wiki_Transformation`
**Assignment:** run the experiment in [docs/experiments/CCA_POTTS_SWEEP_SPEC.md](CCA_POTTS_SWEEP_SPEC.md)

---

## 1. What to do in your first 30 minutes

Do NOT start coding. Your first task is to orient correctly. In order:

1. Read [`docs/RESEARCH_PLATFORM_CHARTER.md`](../RESEARCH_PLATFORM_CHARTER.md) — the mission and epistemic contract. You are a skeptical research collaborator, not an implementation assistant.
2. Read [`CLAUDE.md`](../../CLAUDE.md) — current project state (will be auto-loaded on your session start).
3. Read [`docs/experiments/CCA_POTTS_SWEEP_SPEC.md`](CCA_POTTS_SWEEP_SPEC.md) — the test spec you'll implement. This is the definitive contract for what to do.
4. Read **this document** — the context around that spec.
5. Read [`docs/M0_MILESTONE_COMPILATION.md`](../M0_MILESTONE_COMPILATION.md) Fourth Addendum — the M0 audit finding that motivates the experiment.
6. Skim [`docs/SESSION_HANDOVER_2026-04-16.md`](../SESSION_HANDOVER_2026-04-16.md) — prior session M0 closeout.
7. Skim [`docs/SESSION_HANDOVER_2026-04-07.md`](../SESSION_HANDOVER_2026-04-07.md) — CCA Phase A-D falsification cascade (gives you the experimental lineage this extends).

After that reading, you should be able to answer:
- What outcome A, B, C mean for CCA-1c's status
- Why the reduction-check matters independently of Brown comparison
- What the two terminology collisions are (d_eff and η)

If you can't, re-read. Don't start coding until you can.

---

## 2. What this experiment is part of

### The project

**DS Wiki Research Platform** — a personal research platform for Ian Darling (no academic affiliation, not chasing publication). Structured lab notebook with epistemic guardrails. NOT a product; NOT a paper validator.

### The specific research thread

The wiki has a central framework called **DFIG (Dimensional Fisher Information Geometry)** and a downstream application called **CCA (Constrained Critical Attractor)**. The M0 audit of 2026-04-08 found:

- CCA's general setting (FIM eigenvalue spectrum on 2D lattice phase transitions) substantially overlaps with the **Sethna sloppy-models program** (Machta 2013 Science). Likely a re-parameterization at the level of P5 (Fisher rank = d_eff).
- CCA-1 (isotropy = criticality) was FALSIFIED 2026-04-07.
- CCA-1b L^d scaling was FALSIFIED 2026-04-07.
- CCA-1b magnitude and CCA-1c curve-shape are **qualitatively confirmed on a single test** (q=2 vs q=10 Potts).
- M0's sharpest open question: can CCA's pure 2-point observables reproduce Brown-Bossomaier-Barnett 2022's hybrid 2-point + multi-point discrimination of first-order vs continuous Potts transitions?

**This experiment answers that question.**

### The status stakes

23 conjectures exist (P1-P23). 18 are resolved-against-literature; 5 remain honestly IC. Of the resolved 18:
- **P5, P6, P7, STAT3 are all Sethna-anchored.** These four form the wiki's central research cluster.
- If outcome A: CCA-1c promotes to Supported; P5/P6/STAT3 gain narrow novelty beyond Sethna
- If outcome B: CCA-1c falsified-for-first-order; P5/P6/STAT3 remain "re-parameterization of Sethna" with no demonstrated novelty
- If outcome C: open — needs further investigation

Whatever you find, **write it honestly.** The charter explicitly warns against the "AI rabbit hole" pattern where stacking conjectures without testing produces drift. This experiment is the corrective.

---

## 3. Critical constraints (non-negotiable)

### Charter rules that apply to this experiment

1. **Novelty skepticism is the default.** Before claiming any outcome is "novel," search literature for prior art. If someone has run this specific comparison before you, reframe your work as replication or extension.
2. **Triviality check.** If the outcome is "d_eff matches GTE via the obvious cluster-interfacial-length mechanism Brown 2022 already identifies," that's re-derivation, not novel.
3. **Framing check.** Ask: "Is there a standard framing where this becomes obvious or vacuous?" For Potts at T_c, the obvious framing is standard critical exponents — the reduction-check tests exactly that.
4. **Falsification first.** Try to falsify the hypothesis that CCA matches GTE *before* trying to support it. Look at the cases where you expect disagreement most strongly (strongly first-order q=10).
5. **Plain-language statement.** Every outcome claim must be statable in one sentence a physicist without wiki context could understand.
6. **Tripwire phrases.** Stop and audit if your report draft contains: "unification," "breakthrough," "paradigm," "fundamental insight," "solves," "novel" without completed literature search.
7. **Confidence calibration.** Every status move goes into the `confidence_calibration` table with explicit audit_ref. No silent promotion.
8. **AI-rabbit-hole tripwire.** If you find yourself writing follow-up conjectures before this experiment is complete, STOP. One thing at a time.

### Read-only database

- `data/ds_wiki.db` — **NEVER schema-alter.** Read-only source of truth. All new tables go in `data/wiki_history.db`.
- `data/wiki_history.db` — this is where you write confidence calibration updates after completing the experiment.

### Hysteresis policy on embedding snapshots

- `data/wiki_history.db` is kept under 100MB via `src/snapshot_retention.py`. Keeps latest 3 snapshots. If you run `src.sync` it will auto-prune. This is expected.
- Do NOT add embedding snapshots as part of this experiment. The experiment is about MC data, not wiki content.

### Prior-art gate (mandatory)

Per `memory/feedback_prior_art_gate.md`:
- No new Q/P/Postulate lands without deep literature review first
- This experiment is not a new conjecture — it's a test of existing ones. But the **interpretation** of results may tempt you to formulate new claims. If so, STOP and run the prior-art gate.
- Specifically: before concluding "this is novel," search arXiv for 2022-2026 papers on Potts FIM eigenvalue spectra, Potts transfer entropy, Potts sloppy-models analysis.

### Preserve falsifications

Per `memory/feedback_preserve_falsifications.md`:
- If outcome B (CCA fails to match GTE): **do not delete or soften the CCA-1c claim.** Mark it falsified with specific rationale ("Falsified by Potts q=10 sweep 2026-MM-DD: CCA observables discriminate at < 20% of GTE effect size"). The falsification IS the learning.

### Diagnostic labels

Per `memory/feedback_diagnostic_labels.md`:
- When updating `confidence_calibration`, use specific labels ("Falsified by Phase E Potts q=5,7,10 sweep", "Supported by Potts GTE-matching test") — not generic ones. The meta-signal depends on specificity.

---

## 4. Tools at your disposal

### GSW anchor lookup (new — use heavily)

```bash
python3 scripts/gsw_lookup.py "your topic here" --top-k 20 [--expand]
```
Returns canonical sources connected to a topic via the wiki's anchor graph. Use this for:
- Prior-art checks before claiming novelty
- Finding related entries with shared canonical sources
- Cross-referencing the CCA cluster ({P5, P6, P7, STAT3}) with sources

Also available as MCP tool `get_canonical_sources_for_topic(query, top_k_entries)` when you're in an MCP-enabled Claude Code session.

### Fisher Suite (existing)

```bash
python3 scripts/run_fisher_suite.py --mode node --wiki-db data/ds_wiki.db --node-id STAT3
python3 scripts/run_fisher_suite.py --mode ds_wiki --wiki-db data/ds_wiki.db
```

### Confidence calibration queries

```python
import sqlite3
c = sqlite3.connect('data/wiki_history.db')
for row in c.execute("""
    SELECT calibration_date, audit_ref, confidence, short_status, rationale
    FROM confidence_calibration
    WHERE entity_id IN ('STAT3', 'P5', 'P6', 'P7', 'CCA-1c')
    ORDER BY entity_id, id
"""):
    print(row)
```

### Memory system (auto-loaded)

See `.claude/projects/-Users-iandarling-Projects-DS-Wiki-Transformation/memory/MEMORY.md`. Four critical memories apply to this experiment:
- `epistemic_contract.md` — falsification first, push back not cheerlead
- `feedback_preserve_falsifications.md` — don't soften falsifications
- `feedback_diagnostic_labels.md` — specific labels required
- `feedback_prior_art_gate.md` — mandatory literature review before novelty claims

---

## 5. Expected workflow

### Phase 1 — Orient and verify (day 1, morning)

1. Reading pass (§1 above) — ~90 min
2. Run existing tests: `python3 -m pytest tests/ -v --tb=short` (should be 587 passing)
3. Run `python3 scripts/potts_fim_test.py` as-is — confirm existing q=2, q=10 results match `data/reports/ising_fim_test/potts_comparison.json`
4. Download Brown-Bossomaier-Barnett 2022 PDF (check `Research_Papers/` folder first; if not there, fetch via DOI in anchor table)
5. Download Vinayak 2014 EPL 108, 20006 (arXiv:1403.7218)
6. Download Borgs-Chayes 1996 (arXiv:adap-org/9411001)
7. Read Brown 2022 in full. Note their GTE estimator, lattice sizes, q values, conclusions.
8. Read Vinayak 2014 §II-III — enough to derive the FSS prediction for d_eff_CCA and η_CCA at T_c.

### Phase 2 — Build the code (day 1 afternoon + day 2)

1. Create experiment directory: `mkdir -p data/reports/cca_potts_sweep_2026/{raw,derived,analysis,figures}`
2. Write `scripts/potts_mc_optimized.py` — Numba-accelerated MC core (extend from `potts_fim_test.py`)
3. Write `scripts/gte_analysis.py` — GTE computation matching Brown 2022 exactly
4. Write `scripts/reduction_check_fss.py` — FSS prediction for d_eff_CCA and η_CCA
5. Write `scripts/cca_potts_sweep_main.py` — orchestrator
6. Test each module independently before full sweep

### Phase 3 — Run the sweep (day 2-4)

1. Small warm-up: q=2, L=16, all T values, single replica. Verify pipeline end-to-end.
2. If pipeline OK, launch full sweep (108 configs × 5 replicas = 540 runs)
3. While running, implement `scripts/cca_potts_plots.py` and analysis code
4. Monitor for phase-trapping at first-order q=10 runs — flag bad replicas

### Phase 4 — Analyze and write (day 4-5)

1. Compute observable means + SEMs
2. Run reduction-check (R1 vs R2)
3. Run Brown comparison (A vs B vs C)
4. Draft `docs/CCA_POTTS_SWEEP_REPORT_2026.md`
5. Iterate with owner — honest limitations, clear verdicts

### Phase 5 — Close out (day 5)

1. Write `scripts/migrations/m0_cca_potts_sweep_2026_MM_DD.py` — calibration updates
2. Run migration; verify calibration table has new rows
3. Update `CLAUDE.md` with the new result
4. Commit with descriptive message

---

## 6. Gotchas and known-hard problems

### 6.1 Phase-trapping at first-order q=10

This will happen. Single-site Metropolis near first-order T_c sees hysteresis. You'll see one replica stuck in ordered phase and another in disordered phase. Detection:
- Look at ⟨m⟩ distribution across replicas — if bimodal, phase-trapping happened
- Either: (a) reject trapped replicas, (b) use multicanonical sampling, (c) use Wang-Landau. Simplest: (a).

### 6.2 GTE estimator bias

Finite-sample conditional entropy estimates are biased. Brown 2022 specifies their estimator; use theirs exactly. Do NOT substitute "a mutual-information estimator" — GTE is a different quantity.

### 6.3 η_CCA fit range sensitivity

The tail-power-law fit depends on where you start fitting. Report results with 2-3 fit ranges; if outcomes differ across fit-range choices, report the uncertainty honestly.

### 6.4 The reduction-check derivation is non-trivial

Deriving d_eff_CCA and η_CCA from η_critical=1/4 and β/ν=1/8 via FSS requires some analytical work. Vinayak 2014 gives the correlation-matrix eigenvalue density framework. The actual derivation should show the prediction formulas explicitly in the report.

If the derivation defeats you, that's information: it means the wiki's d_eff_CCA and η_CCA aren't *derivable* from standard exponents in closed form, which is itself meaningful.

### 6.5 Potts spin representation for χ_ij

For q>2, what's "s_i s_j"? Options:
- Kronecker delta: ⟨δ(s_i, s_j)⟩ - 1/q
- Signed projection: map each of q states to a point on (q-1)-simplex; use inner product
- Order parameter: m_i = q·δ(s_i,0) - 1 for the preferred direction

Brown 2022 uses a specific convention — match it. If unclear from Brown, default to the symmetric δ-based definition (standard in Potts literature).

### 6.6 Computational cost blowup

A naive implementation does FIM = correlation matrix over L² sites → L⁴ storage. For L=32, that's 32⁴ = 1M floats per sample, times 2000 samples per replica × 540 runs → terabytes if you save raw. Save only:
- Per-run averaged FIM (L²×L² per run, ~4MB for L=32)
- Eigenspectrum (L² floats per run)
- Scalar observables (d_eff, η, GTE, ⟨m⟩, etc.)

Raw samples only saved for 1-2 representative runs for debug.

### 6.7 Scholarpedia WebFetch is flaky

If you need to cite Scholarpedia, budget 3 retries. Per prior session experience, single fetches time out ~60% of the time.

---

## 7. What a "good" outcome report looks like

Whatever A/B/C you find, the report should:

1. **Lead with the one-sentence verdict.** "CCA pure 2-point observables [A: match / B: miss / C: differ from] Brown 2022 GTE discrimination of first-order vs continuous Potts transitions at the q=2,5,7,10 sweep."

2. **Show the data.** Plots of all three observables vs T/T_c for each q, with error bars from replica spread. Don't hide variance.

3. **State reduction-check outcome first.** R1 vs R2 determines whether continuous-transition novelty is on the table at all.

4. **State Brown comparison outcome second.** A/B/C.

5. **Be explicit about what this does NOT settle.** Other models, other observables, other framework questions (Fisher-gravity chain, etc.).

6. **Give the calibration update as a concrete patch** — what rows go into the `confidence_calibration` table.

7. **Propose one (only one) follow-up question** if warranted — not a list of speculations.

8. **Honest limitations section.** Sample sizes, fit-range sensitivity, any phase-trapping episodes, Brown-convention deviations.

### What a BAD outcome report looks like

- "These preliminary results suggest a new framework..." → stop. Not preliminary. Not new framework. State the verdict.
- "Further research is needed to fully understand..." → bureaucratic filler; name the specific question.
- "This opens up exciting possibilities for..." → tripwire phrase. Audit.
- A "future work" section with more than 2 items → accumulation drift. Stop.
- Silent promotion of any other conjecture based on this result → no.

---

## 8. Budget and stop-conditions

**Time:** 5 working days expected. If at day 3 you have no MC data yet, stop and reassess — the implementation is likely broken.

**Compute:** ~12h on RTX 2000 GPU, ~1-3 days on workstation CPU. If estimated runtime exceeds 7 days, reduce scope (skip L=32 or reduce replicas to 3) and document the reduction.

**Stop for owner input if:**
- Brown 2022 GTE definition doesn't match what we can compute from our MC samples (may need to redefine sampling cadence)
- Reduction-check derivation is analytically intractable (may need different comparison method)
- MC infrastructure fails to equilibrate at L=32, q=10 even with doubled N_equil (may need to skip or switch algorithm)
- Outcome is so clear from small L=16 sweep that full sweep is redundant (may be able to save compute)

**Do NOT expand scope without owner sign-off.** Resist:
- Adding q=3, q=4 "for completeness" — these are well-studied; skip
- Adding Heisenberg or XY model — different scope
- Computing additional observables "while we're at it" — accumulation
- Testing on other lattice topologies — scope creep

---

## 9. Communication protocol with owner

Owner (Ian Darling) wants:
- **Plain-language updates at phase transitions.** When you finish Phase 1 (reading), Phase 3 (MC sweep complete), Phase 4 (draft report), ping.
- **Honest uncertainty.** If you're not sure about a DOI, say "DOI reconstructed from publisher pattern, not CrossRef verified." Don't round up confidence.
- **Push back.** If the spec has a bug, say so. If reduction-check is pointless given some finding, say so.

Owner does NOT want:
- Cheerleading
- Premature "exciting!" language
- Silent scope expansion
- Long summaries of what you already did (the logs show that)

---

## 10. What success looks like across all outcomes

**Outcome A (CCA matches GTE):**
- Report states A with confidence and specific metrics
- CCA-1c → Supported in calibration table with audit_ref "gsw-cca-potts-sweep-phase-E-2026-MM-DD"
- STAT3 calibration updated: "narrow novelty confirmed for first-order discrimination via pure 2-point observables"
- Follow-up: test whether mechanism is interfacial-length (matching Brown) or something different
- **Success = honest documented progress, not vindication**

**Outcome B (CCA misses GTE):**
- Report states B with confidence and specific metrics
- CCA-1c → Falsified-for-first-order-discrimination in calibration table
- STAT3 calibration updated: "first-order discrimination cannot be recovered from pure 2-point observables; GTE-style hybrid required"
- Follow-up: consider whether CCA has a valid narrower scope (continuous transitions only?)
- **Success = honest falsification documented; wiki now knows something it didn't**

**Outcome C (CCA discriminates differently):**
- Report states C with a clear characterization of how curves differ
- CCA-1c → Speculative-pending-mechanism in calibration table
- Follow-up: single mechanism question — what does CCA see that GTE doesn't, or vice versa?
- **Success = a sharper, more specific research question than we started with**

---

## Appendix A — Quick file map for orientation

```
Top-level files to touch:
  docs/experiments/CCA_POTTS_SWEEP_SPEC.md        ← the spec (read first)
  docs/experiments/CCA_POTTS_SWEEP_HANDOVER.md    ← this file
  docs/CCA_POTTS_SWEEP_REPORT_2026.md             ← you will write this (end of experiment)

Reference docs:
  CLAUDE.md                                        ← auto-loaded project state
  docs/RESEARCH_PLATFORM_CHARTER.md                ← mission + epistemic rules
  docs/M0_MILESTONE_COMPILATION.md                 ← M0 audit findings
  docs/SESSION_HANDOVER_2026-04-16.md              ← M0 closeout
  docs/SESSION_HANDOVER_2026-04-18.md              ← GSW anchor architecture
  docs/SESSION_HANDOVER_2026-04-07.md              ← CCA Phase A-D falsification cascade
  docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md          ← d_eff and η collisions
  docs/CCA_MATHEMATICAL_FORMALIZATION.md           ← CCA math (read with M0 skepticism)

Existing code to extend:
  scripts/potts_fim_test.py                        ← current q=2, q=10 infrastructure
  scripts/ising_fim_mc_test.py                     ← Ising baseline
  scripts/cca1b_finite_size_scaling.py             ← FSS tooling
  src/analysis/fisher_diagnostics.py               ← FIM analysis

New code to write:
  scripts/potts_mc_optimized.py
  scripts/gte_analysis.py
  scripts/reduction_check_fss.py
  scripts/cca_potts_sweep_main.py
  scripts/cca_potts_plots.py
  scripts/migrations/m0_cca_potts_sweep_2026_MM_DD.py

Data:
  data/ds_wiki.db                                  ← READ ONLY
  data/wiki_history.db                             ← calibration writes go here
  data/reports/ising_fim_test/                     ← existing CCA-related outputs
  data/reports/cca_potts_sweep_2026/               ← CREATE; your outputs here
```

---

## Appendix B — One last thing

You're joining a project that has done substantial honest work. The M0 audit walked back claims. The GSW anchoring pass documented prior art. 18 of 23 conjectures are now connected to literature with typed relationships, 5 honestly labeled as wiki-internal. This experiment is the next concrete step: an honest test that will either support, falsify, or refine a specific claim about CCA.

The charter's "worst failure mode" is *accumulating speculative claims that feel grounded because they're inside a well-organized wiki.* Your job is the opposite: produce a result that sharpens belief regardless of which direction it moves.

Whatever you find, write it cleanly. The wiki is better off knowing the truth than having the framework feel bigger than it is.

Good luck.

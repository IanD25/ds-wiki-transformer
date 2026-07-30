# Session Handover — 2026-05-04

> **Read order for fresh sessions:**
> 1. [`docs/RESEARCH_PLATFORM_CHARTER.md`](RESEARCH_PLATFORM_CHARTER.md) — mission, epistemic contract
> 2. [`CLAUDE.md`](../CLAUDE.md) — project context
> 3. **This document**
> 4. [`docs/SCALING_RESEARCH_QUEUE_2026_05_04.md`](SCALING_RESEARCH_QUEUE_2026_05_04.md) — if picking up the scaling thread
> 5. [`docs/SESSION_HANDOVER_2026-04-20.md`](SESSION_HANDOVER_2026-04-20.md) — prior session (CCA Potts Phase E)

**Commits:** `17b6742`, `5741f9c`, `4cf550c`, `faca047` — all on `main`, **all unpushed**.
**Final ChromaDB snapshot:** `snap_20260725_223034`
**Uncommitted:** `docs/demo/` — see §Interview demo (decision pending).

---

## One-paragraph summary

Two deep-research passes and a new subsystem. The first pass (five agents, triggered by a Maldacena interview) confirmed M0's Fisher-gravity downgrade against 2020–2025 literature and produced eight prose corrections including retracting a claimed "second independent path" from Fisher information to gravity. The second (three agents, on Kolokotrones et al. 2010) found a **fabricated citation** in the wiki, downgraded a claim from established to contested, and — unexpectedly — **derived** H5's functional form, which the same session had spent hours dismantling. Between them, a glossary subsystem was built to make "name the specific mathematical object" enforceable by structure rather than discipline. Net: the scaling framework is smaller, one conjecture is falsified, one has a real definition for the first time, and one item is runnable.

---

## Threads, in order

### 1. Memory relocation

The project moved to iCloud; the six standing-rule memory files were still at the old path and not loading. Copied to the new location with a cleaned index. The prior-art gate, preserve-falsifications, diagnostic-labels, and age-is-not-decay rules now load automatically again.

### 2. Maldacena deep-research pass

Trigger: an interview transcript on emergent spacetime. Five agents on the information-geometry / emergent-gravity landscape.

**Headline: M0's Fisher-gravity downgrade is correct and conservative.** No peer-reviewed paper 2020–2025 constructs a theorem-level bridge from classical Fisher information on a parameter manifold to the modular-Hamiltonian machinery used in emergent-Einstein derivations. The closest theorem-level results sit entirely on the quantum side.

Corrections applied:

- **`CCA_GRAVITY_FINDINGS.md` §1.3 RETRACTED.** Bianconi 2025 uses *quantum* relative entropy on density-matrix-valued metrics — Hessian is the Bures/Petz-family metric, not classical Fisher-Rao. It is not an independent second path from Fisher Rank to gravity. Original prose preserved with the conclusion struck.
- **GT10** gains the Casini-Galante-Myers 2016 scope caveat: Jacobson's modular-Hamiltonian-as-boost assumption fails for relevant operators with low conformal dimensions.
- **P17/P23** DESI σ-levels corrected to 2.8–4.2σ across SN compilations. The 5σ figure was Amendola's *forecast* for ~250 future events, not current data.
- **P21** split: classical Chentsov uniqueness vs quantum Petz *classification* (a family of monotone metrics, no single canonical choice).
- **BR04/IT08** cross-linked — Brody-Rivier 1995 proved Ruppeiner is Fisher-Rao on the Gibbs canonical family in the thermodynamic limit.

Also surfaced: the CCA docs define `d_eff` and `η` with **different formulas** than the Phase E experiment actually computed. Notation banner added; Phase E definitions are canonical going forward.

23 anchors, 10 calibrations under `gsw-maldacena-deep-research-2026-05-04`.

### 3. Glossary subsystem (new)

The operational form of "name the specific mathematical object, every time."

- Schema: `disambiguates from` link type; `term_uses` and `glossary_meta` tables
- 20 disambiguation pages + 21 sense entries (including `gloss_lambda`, added later)
- `src/glossary/` — markup parser for `[[g:slug]]`, three renderers, load-bearing-word lint
- First punch list: **611 high-severity flags across 122 entries** — [`data/reports/glossary_lint_2026_05_04.md`](../data/reports/glossary_lint_2026_05_04.md)

Top-flagged entries match the deep research findings exactly: GT04, GT03, IT05, IT08, RG06, BR04.

### 4. Hypothesis / unexpected-links review

500 surprising pairs, 265 unlinked. Triage in [`data/reports/hypothesis_2026_05_04/`](../data/reports/hypothesis_2026_05_04/).

**Methodologically the most useful finding:** the tool's #3 cross-type unlinked candidate was GT04 ↔ IT08 — the exact vocabulary-overlap conflation the deep research had just audited. The generator surfaces vocabulary stacking indistinguishably from real adjacency. Its outputs are candidates for triage, not link recommendations.

### 5. Scaling framework — three passes

Triggered by a Veritasium video on metabolic scaling, then extended.

**Corrections:**
- X1's `d_f ≈ 2.7` was labelled "empirical WBE value." It is not — WBE's derivation uses `d_f = 3`; 2.7 is back-calculated by inverting β = d_f/(d_f+1) on the observed 0.73.
- C1's implied `D_eff` column: two values exceed the embedding dimension (reptiles 3.2, fish 7.3). Geometrically impossible. Column retired from inference.
- **P11 structural bound:** β(λ) is bounded above by 1 and cannot express urban superlinear exponents (~1.15).

**Root diagnosis:** every symptom traced to one cause — β(λ) interpolates between *chosen* endpoints rather than deriving from a mechanism. H5 reframed as a descriptive interpolation with a documented endpoint failure (observed BMR 0.676 falls below the 0.750 floor for any λ ∈ [0,1]).

**Queue decisions:** P12 falsified on cross-domain universality. P14 split into a λ-free empirical core (P14a, runnable) and a blocked mechanism (P14b). P16's promotion withdrawn — its blocker is *specification* (Q4), not measurement.

**Endpoint decision (owner):** [2/3, 3/4]. MMR excluded on ontological grounds — see §Owner contributions.

### 6. Kolokotrones research pass — and a reversal

Trigger: the previous pass had written "Kolokotrones' proposed mechanism has not been read and is NOT reconstructed here" into the wiki as a flagged gap. Owner asked for the actual text. Three agents; full text obtained.

**Fabricated citation found.** C1 attributed the ~10 kg breakpoint to "Xiao et al. (2015)." **No such paper exists.** It is Dodds, Rothman & Weitz 2001 — already anchored to C1 earlier the same day. Third mislabelled quantity in this cluster in one session.

**Curvature downgraded** from established to contested. Griebeler & Werner 2016 (519 species): linear beat curvature in 16 of 17 orders. Hudson 2013: aquatic intercept shift, "not real." Plants curve *concave* — opposite sign. Invertebrate curvature vanishes under phylogenetic grouping. No replication in birds, reptiles, or fish. MacKay 2011: only Rodentia survives a scale-invariant test, at 2% of variance. Packard: log-curvature follows from a non-zero arithmetic intercept. The quadratic adds 0.3% of variance.

**Slope range corrected** from "~2/3 to ~3/4" to the paper's actual **0.57–0.87**.

**Direction puzzle resolved — min-rule vs sum-rule.** The puzzle assumed constraints combine as a *minimum*, under which the lower exponent binds at large mass → concave. The models that reproduce the curvature use *sums*, where the lower exponent dominates at small mass → convex. The thermal physics was sound; the combination rule was wrong.

**Derivation found — H5's form is not arbitrary.** For B = a·M^p + b·M^q the local log-log slope is **p·f + q·(1−f)** with **f = a·M^p / B** — exactly β(λ), with **λ = the fractional contribution of one process to total metabolic rate.**

This **reverses** the same session's H5 diagnosis. "Interpolation without mechanism" was right about construction, wrong that no mechanism exists.

---

## Owner contributions worth preserving

Two arguments from the owner that did real work:

**λ as realisation fraction.** Proposed when three Claude-generated candidates had failed. It was the first to pass the topology-vs-efficiency test — efficiency changes move the prefactor, only topology changes the exponent. Superseded by the two-process derivation, but it was the reading that made the question tractable.

**MMR as overclock.** Maximum metabolic rate is temporary, unsustainable, costly, individual, trainable, and never a baseline. BMR and MMR are therefore different *kinds* of quantity, not two points on one continuum. This reframed a supposed range failure as a category error in the framing. It generalises — continuous vs peak power rating, base vs boost clock, yield vs ultimate strength — and it is **unaffected** by the later Kolokotrones findings.

---

## Where the scaling thread stands

**Resolved:** λ has an operational definition (fractional process contribution), measurable without touching β, mass-dependent by construction. The endpoint question is superseded — endpoints are the two processes' exponents.

**Open:** *which* two processes. Candidates: Ballesteros 2018 (isometric + surface) vs Zhao (both from Murray-law network geometry, explicitly denying the small-mass 2/3 is the surface law). Two papers; bounded work.

**Runnable:** P14a — branching variance vs BMR/MMR exponent gap. No upstream dependencies.

**Dead:** P15's Landauer motivation. λ is not a synchronisation and not something an organism maintains.

Full detail: [`SCALING_RESEARCH_QUEUE_2026_05_04.md`](SCALING_RESEARCH_QUEUE_2026_05_04.md).

---

## Honest meta-notes

**1. Three self-corrections mid-session.** I claimed C1 lacked a circularity caveat and lacked the mass-crossover competitor — both were already present. I nominated P16 for promotion before reading Q4 closely enough to see its blocker was conceptual. And the H5 "no mechanism" diagnosis was reversed by the second research pass. All three are recorded in migration docstrings so they are not re-litigated.

**2. The research pass should have been proposed, not requested.** The wiki carried "the mechanism has not been read" as a flagged gap while the paper was one search away. The prior-art gate was applied to the owner's conjectures all session and not to Claude's own reasoning.

**3. A migration bug worth remembering.** The first Tier-B migration pre-computed two edits to the *same column* from the same base value; the second UPDATE silently overwrote the first. Caught by post-write verification. All later migrations abort on duplicate `(table, row, column)` targets, and one uses a `replace_then_append` mode to compose two changes into a single write.

**4. The derivation wants a second pair of eyes.** It is elementary algebra and was verified, but it was produced at the end of a long session and it conveniently rescues a formula that session had spent hours dismantling. Recorded in H5 with steps shown so it can be checked rather than trusted.

**5. Every falsification this session was self-generated.** The curvature result had been sitting in C1 unread for its implications. The fabricated citation had been in the wiki through multiple prior sessions. Nothing external forced any of it.

---

## Interview demo (built this session, commit decision pending)

Built in `docs/demo/`: a five-minute screen-share demo of the wiki, framed for a business
audience. The subject is the **verification apparatus**, not the science.

| File | |
|---|---|
| `TALKING_POINTS_TATE_DEMO.md` | Timed script at 145 wpm, anchor lines, Q&A, prep checklist, fact-check appendix |
| `tab1_inversion.html` | Operating model: AI as adversarial auditor rather than author |
| `tab2_apparatus.html` | Anchors, glossary flags, calibration records, falsified-kept rule |
| `tab3_catch.html` | **Centrepiece** — the three audit findings, in the exemplar's failure-tab format |
| `tab4_playbook.html` | The six rules, framed as domain-agnostic |
| `WIKI_DEMO_LEAVE_BEHIND.pdf` | 8 pages, 2 per tab |

Every figure is computed from the project's real database files and carries a fact-check
appendix entry naming its source. Load-bearing numbers: 278 entries, 23 conjectures, 900
anchors across 274 entries, 82 calibration records across 11 audit passes, 47 entries
labelled "no external source exists", 611 vague-term flags across 122 entries, 3 formally
falsified claims.

**Why it is not committed.** The repo has a GitHub remote and `CLAUDE.md` describes it as a
"GitHub-shareable repo." The talking-points document contains a job requisition number, the
hiring company, the interviewer's role, and personal interview strategy. That is private
material and does not belong in a shareable repository by default. Three options, owner's
call:

1. **Keep local only** — add `docs/demo/` to `.gitignore`. Simplest, and the material stays private.
2. **Move it out** — relocate to a personal directory outside the repo.
3. **Commit deliberately** — only if this repo is in fact private, which should be verified
   rather than assumed.

Note also that **four commits are currently unpushed**, so nothing has left the machine yet
either way.

## Deferred / not done

- **Defined-term audit.** The lint punch list exists (611 flags, 122 entries) but no entries have had `[[g:slug]]` markup applied. That is the next glossary phase.
- **P17/P23 wording** in `ds_wiki.db` — partially corrected this session for σ-levels; the broader Amendola/Cadoni rewording from M0 Fifth Addendum is still open.
- **CCA terminology rename** — banners are in place, body-text migration is not.
- **Wiki anchoring** — ~175 entries still unanchored from the 2026-04-18 pass.
- **Deeds, Savage & Fontana 2011** reply to MacKay is paywalled and unread. Anchored at `medium` confidence with that stated. Anyone leaning on the MacKay critique should read it first.

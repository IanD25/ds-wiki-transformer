# Session Handover — 2026-10-18 (pre-merge consistency pass)

> **Read order for fresh sessions:**
> 1. [`docs/RESEARCH_PLATFORM_CHARTER.md`](RESEARCH_PLATFORM_CHARTER.md) — mission, epistemic contract
> 2. [`CLAUDE.md`](../CLAUDE.md) — project context (rewritten this pass)
> 3. **This document**
> 4. [`docs/M1_MILESTONE_COMPILATION.md`](M1_MILESTONE_COMPILATION.md) — what we believe now
> 5. [`docs/PODCAST_CROSSWALK_2026-10-18.md`](PODCAST_CROSSWALK_2026-10-18.md) — if working on the podcast merge
> 6. [`docs/SESSION_HANDOVER_2026-05-04.md`](SESSION_HANDOVER_2026-05-04.md) — prior handover; read its dates erratum first

**Mode:** A (curation / grounding). No promotions, no new conjectures, no experiments.
**audit_ref:** `gsw-consistency-pass-2026-10-18` (plus `gsw-consistency-pass-2026-10-18-h5-gate` for one owner-approved collision, §6).
**Commits (pushed to `origin/main` 2026-10-18, through `0d162f2`):** `c30bce3` (Ph 1) · `7233acd` (Ph 2) · `208f799` (Ph 3) · `9b7c78e` (Ph 5) · `4560aa0` (Ph 6a) · `d66b227` (Ph 4) · `ca1e642` (Ph 7) · `70deb71` (Ph 6b) · this commit (Ph 8). Phase 4 was committed after 5 and 6a because its literature read ran in parallel.
**Milestone snapshot:** `snap_20261018_190812` (trigger `milestone:pre-merge-baseline`) — the pre-merge baseline, exempt from pruning.
**Not touched:** `docs/demo/` (owner's decision; see §8 for one accidental read).

---

## 1. Summary

The wiki is about to merge with the *Relatively Human* podcast, whose "DS framework" segments were written before the M0 audit. This pass made the wiki internally consistent first, then built a crosswalk from podcast claims to current wiki status. The source database now mirrors the calibration record, and the dates of the "2026-05-04" work are reconciled. Corrected claims that had survived elsewhere were removed, including the fabricated Xiao citation, still live in H5. Errors the podcast shares with the wiki were found and fixed: three podcast-listed ones and one more found during the crosswalk. H5's "derivation" was shown to be a 2003 result. Calibration reporting now separates claims from process records. **No label changed in this pass**; seven calibration rows were appended to record corrections.

## 2. Before → after

| | Before | After |
|---|---|---|
| Tests | 575 pass / 12 fail | 575 pass / 12 fail (identical failing set; stale hard-coded counts) |
| Entries / links / conjectures / gates | 319 / 849 / 23 / 12 | unchanged |
| External anchors | 900 over 274 entities | **910 over 276** (+ Frank 2009, Braunstein–Caves 1994, Carney et al. 2025, Bettencourt 2013, six on H5) |
| Internal constructions | 47 | 47 |
| Non-glossary orphans | 1 (GT05) | **0** |
| Calibration rows / audit refs | 82 / 11 | 89 / 13 |
| Calibrated entities | 55 | 55 |
| **Claims** (`claim_status_latest`) | not separable | **47: 29 Speculative · 8 Supported · 7 Established · 3 Falsified** |
| Process records | — | 8 |
| Snapshots | 3 (all 2026-07-25, no milestone) | 3 incl. 1 milestone |

## 3. What this pass did, by phase

1. **Dates.** The "2026-05-04" session was two calendar days. Maldacena, the glossary and the hypothesis review ran on 2026-05-04. The scaling passes, endpoint decision and Kolokotrones pass ran on 2026-07-25 under a carried-over label. All four commits are dated 07-25. The evidence is the migration file times, the sync backups, `calibration_date = date.today()`, and the snapshot IDs. The erratum is at the top of the 05-04 handover and the scaling queue. Nothing was renamed, no calibration row was edited, and no banner was rewritten.
2. **Source DB ↔ calibration.** `three_state` on all 23 conjectures now has the format "label — pointer [pattern tags] | was: original". `conjecture_summary.status` uses the same format (owner-approved; P18–P20 have no row). Status banners were added to 14 claims (P2 P5 P6 P7 P8 P10 P11 P12 P13 P15 P18 P19 P20 P21): six as directed, eight where the latest calibration contradicts the claim. P7 now states that the participation ratio failed monotonicity everywhere. P8 names Gefen–Mandelbrot–Aharony 1980, and notes they found exponents depend on topology as well as dimension (abstract verified). The Fifth-Addendum rewording of P17/P23 was applied, and "LVK O4" was relabelled GWTC-3. Correction notes were appended to anchors 818/819 (owner-approved).
3. **Residual errors.** Fixed: Xiao and the slope gloss in H5; the slope gloss in C1's Regime-First section and in anchor 900's note; 5σ and "generic" Cadoni in GT11 (three sections), G12 and CCA_GRAVITY_FINDINGS §4.3. A stale status on `saberi_2024_prb_priority_read` was corrected. Podcast-origin errors found in the wiki: Fisher information ↔ uncertainty principle (IT05; M6→QM2 link) and Frank 2009 as mechanism (BIO3). Seven of the nine podcast items were absent from the wiki.
4. **H5 gate.** The two-process identity is the elasticity-of-a-sum rule, a **re-derivation**. Verdict: **RESTATEMENT of West et al. 2003** (b = Σcᵢbᵢ, cᵢ = Bᵢ/B), verified from the preprint text. Two side-findings: Ballesteros' f is a constant, not λ; Zhao 2015 is a single-network model, not a decomposition. Report: `docs/prior_art_reviews/H5_TWO_PROCESS_PRIOR_ART_2026_10_18.md`. Six anchors were added; banners went on H5 and the queue. H5 stays Speculative.
5. **Claims vs process.** Added the views `claim_status_latest` and `process_status_latest`, with owner-approved type overrides. The blueprint's raw-count figures and two system-description errors were corrected, and the blueprint is committed for the first time.
6. **Docs + orphan.** GT05 is anchored to Carney, Karydas, Scharnhorst, Singh & Taylor 2025, checked against the full text. GT05 had misdescribed the paper: the mechanism is free-energy, not entanglement, and the noise term is S_FF(0), not ω^−α. Corrections were also made to BR01 and two links. The CLAUDE.md stale sections were rewritten. The 05-04 handover's "~175 unanchored" item got a correction note.
7. **Crosswalk.** `docs/PODCAST_CROSSWALK_2026-10-18.md` covers 16 + 12 claims, with exact quotes (60 checked first-hand), verified wiki mappings, labels and on-air errata. Several mappings in the brief were corrected (§5 of the final report). One more shared error was found and fixed: C2's "β = 1 ± 1/D_eff" restates Bettencourt 2013 (verified from the full text).
8. **M1.** `docs/M1_MILESTONE_COMPILATION.md` uses the charter's five sections, with numbers from `claim_status_latest`.

## 4. Work since the last handover that no handover covered

- **`1d58451` (2026-07-30).** Added the *Interview demo* section to the 05-04 handover: what is in `docs/demo/`, why it is deliberately uncommitted (job requisition, employer and interview strategy in a GitHub-shareable repo), and three options for the owner.
- **2026-07-31, memory.** New memory file `user_owner_physics_intuitions.md` plus an index line. It came from an exploratory (Mode B) conversation about the owner's information-first worldview. It records the worldview, its prior-art map (entropic gravity = the wiki's own GT10/Fisher–gravity thread; Connes–Rovelli thermal time; holographic RG), and a drift pattern to watch: an aesthetic pull towards closure and conservation, and a retreat to unfalsifiable ground when a favoured claim meets a test. No wiki content changed.
- **`519e053` (2026-08-06).** Milestone-exempt snapshot retention (`snapshot_retention.py`, `sync.py --milestone`, `trigger_sync(milestone=True)`). Motivation: a check of a generalised architecture brief (published as a private claude.ai artifact, not in the repo) showed "drift over time" was unbacked, because keep-3 pruning left three same-day snapshots. First used this pass.

## 5. Calibration rows appended (labels unchanged throughout)

`P17`, `P23` (Fifth-Addendum prose corrections) · `H5` (Xiao + slope + superseded items) · `C1` (Regime-First slope gloss) · `saberi_2024_prb_priority_read` (not direct prior art) · `endpoint_decision_revised` (endpoints are inputs, not derivable) — all under `gsw-consistency-pass-2026-10-18`. `H5` (re-derivation; RESTATEMENT of West 2003) under `gsw-consistency-pass-2026-10-18-h5-gate`. Rule followed: a row only where a correction is recorded **and** the entity already had calibration history. GT05, GT11, G12, BIO3, IT05 and C2 were corrected via banners and anchors without a first-ever label.

## 6. Decisions the owner made this session

Milestone sync deferred to after the last content change. `conjecture_summary` updated. Anchors 818/819 annotated, not rewritten. View overrides: λ collision, endpoint decision and root diagnosis → process; matrix spectrum → scientific. A collision sub-ref for H5, because `confidence_calibration` is UNIQUE on (entity_id, calibration_date, audit_ref) and H5 already held this pass's slot.

## 7. Honest status (charter §8)

**Grounded:** P21 and M6 (as stated, narrowly), BR04, C1's power-law core, GT10 (linearized), and the CCA falsifications. **Supported on one test family or one domain:** P5, CCA-1b magnitude, CCA-2, STAT3, P18–P20. **Speculative — almost everything framework-original:** the D_eff/Fisher-rank thread, β(λ), the Fisher–gravity chain, and cosmological coupling. **The framework's own derivations keep turning out to be literature:** P2 (WBE 1997), P5 (Machta 2013), P8 (Gefen 1980), P11 (Bettencourt 2007), H5 (West 2003), C2 (Bettencourt 2013). That is `restatement-in-new-vocabulary`, the dominant drift pattern, now seen six times. **Two labels look generous** and are flagged in M1, unchanged: `mmr_sustained_vs_peak_distinction` and `scaling_framework_root_diagnosis` (both Established). Note for the merge: the podcast states as fact several things the wiki holds as Speculative or worse. The crosswalk's errata lines are the corrective.

## 8. Meta-notes — errors I made this pass

1. **Idempotency bug (Phase 2).** Correction banners quote the original wording, so on a re-run the find-strings matched inside the banner. A dry re-run caught it before any bad write; the fix is to check the applied suffix first.
2. **Missed UNIQUE constraint (Phase 4).** The H5 row was silently skipped, and my verification passed falsely because it only checked that *a* row existed. Caught from the row count; fixed with an explicit collision report and the owner-approved sub-ref.
3. **docs/demo/ read by accident (Phase 5).** A grep exclusion filter didn't match the path format, so matching lines from `docs/demo/TALKING_POINTS_TATE_DEMO.md` appeared in output. The file was not opened, changed or used. The lines showed it quotes the raw "82 records, 53/13/13/3" figures that Phase 5 corrected elsewhere; it is the owner's to fix.
4. **Number typo.** I wrote "909" in an anchor-count note; the true count is 910. Caught by recount.
5. **Agent research.** Literature and quote extraction ran in background agents. Every load-bearing quote used in the wiki was re-verified first-hand (West, Ballesteros, Zhao, Carney, Bettencourt, Gefen abstract, Amendola abstract; 60 podcast quotes). Items the agents could not read (Banavar 2003, the Darveau reply, Maino 2014) are not anchored.

## 9. Deferred / not done

- Glossary markup; the CCA and λ "phase coherence" renames in body text; moving P9 to the Q-series.
- 12 stale-count tests (they expect 278/231/209 entities; the glossary made it 319); `wiki_meta.total_entries` still says "278 entries … 818 links".
- `.venv` editable install points at the dead path `/Users/iandarling/Projects/DS_Wiki_Transformation/src`.
- Memory catalog: the pattern tags `over-extension-beyond-formula-range` and `conditional-claim-with-unsatisfiable-antecedent` (used on P12) are not yet in `feedback_diagnostic_labels.md`.
- Fisher-rank monotonicity "as a theorem" (T1/M6): true for exact rank under fixed-parameter Markov coarse-graining, not for RG or the participation ratio. Recorded in the crosswalk; wiki not edited.
- **Push:** done 2026-10-18 on the owner's instruction — 15 commits, `0b05eb1..0d162f2`. **`docs/demo/`** — still the owner's call; not committed.

---

## 10. Continuation — later on 2026-10-18 (written before compacting the session)

After the consistency pass and the push (`0b05eb1..8affb8c`), the session went back to the wiki's original purpose: compile real science, map the connections, and log questions to ask the world.

**Done (local commits, not pushed):**

| Commit | What |
|---|---|
| `f21b24f` | **Questions Raised Log** started (`docs/QUESTIONS_RAISED_LOG.md`), QR-001 to QR-006; QR-006 (information measures vs classical early warnings) is the owner's priority |
| `4214cdd`, `2548e72` | **Prior-art fold-in**, run in its own session: 12 reference entries (BIO12–16, IT09–11, STAT4–6, URB1) written from primary sources. P2 Retired as "Folded" (WBE 1997); P8 and P11 **Falsified** by their sources (Gefen 1980; Bettencourt 2013). Report: `docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md` |
| `07fcbdc` | CLAUDE.md: three source mis-statements corrected (Vinayak, Borgs–Chayes, Brown) and numbers refreshed. **T5** bannered: the Sierpiński gasket has T_c = 0 |
| `bc70959`, `0002d78` | QR-006 literature map (`docs/prior_art_reviews/QR-006_EWS_LITERATURE_MAP_2026_10_18.md`), compiled by an agent, with corrections |
| `84e73db` | **Gate 2, the worth-asking gate** (`docs/QUESTION_GATES.md`), owner-requested, run after the prior-art gate; also saved as memory `feedback_worth_asking_gate.md` |
| `b32c1e8` | QR-006 well-posedness review and both gates (`docs/prior_art_reviews/QR-006_BENCHMARK_GATES_2026_10_18.md`). QR-006 was not well posed. Re-scoped to **QR-006b**: on a common labelled benchmark at matched false-alarm rates, do information indicators beat lag-1 autocorrelation and variance where the linear-Gaussian assumptions fail? Verdicts: the generic benchmark is **open in the literature** (Dakos et al. 2024 names the gap); the regime-stratified version has **no prior art found (provisional)**. The Gaussian equivalence is **FOLDED** (`trivial-from-known-result`); QR-006b is **RE-SCOPE → PROCEED (provisional)** |

**In flight — early-warning fold-in session** ([`local_c28d2239-29f6-4c4c-9e54-a48130e4e4e2`](#local_c28d2239-29f6-4c4c-9e54-a48130e4e4e2)). It has applied 10 entries, EWS1–EWS10, with the owner's decisions (all as recommended). Totals: 341 entries, 911 links, 957 anchors over 298 entities, 0 non-glossary orphans. Its index rebuild, test run and commits were still pending when this note was written; its uncommitted files are in the working tree. EWS8 records the Gaussian equivalences. *Update: committed as `30841fa` (data) and `9d42905` (report).*

**Loose ends (do these next):**
1. **Done** (follow-up commit after `9d42905`). **After the EWS fold-in commits**, edit `docs/QUESTIONS_RAISED_LOG.md`:
   - add Gate 2 to the status ladder (raised → literature-mapped → Gate 1 → Gate 2 → filed);
   - add **QR-006b** with its gate verdicts, linking the gate report;
   - add **QR-007**: can correlation-matrix observables (CCA's participation ratio) classify transition *order* — first-order vs continuous? This is CCA's distinct angle; the CCA-1c reduction test bears on it.

   Also add Gate 2 to CLAUDE.md's fresh-session step 8.
2. **Done** (same commit). **Downgrade one marker** in the gate report: Bandt & Shiha 2007 is marked "verified, abstract", but it was seen only via a search summary of its abstract. The EWS fold-in could not find the abstract or open text. Change the marker to "abstract via search summary".
3. **Second, independent search for QR-006b.** Use a different session and different vocabulary, include the machine-learning early-warning literature, and read the *Entropy* 28:628 (2026) review (blocked with HTTP 403 this time), Dakos & Soler-Toscano 2017, and Eason et al. 2014. Only then does PROCEED stop being provisional.
4. **Then design the benchmark** as a pre-registered Mode B project:
   - Indicators: AC1, variance, lagged MI, TE, permutation entropy, the FI index, and the covariance-eigenvalue share and participation ratio.
   - Data: Bury et al. 2021's simulation scripts with null runs, plus the anoxia, thermoacoustic and paleoclimate records (CC BY-NC-SA 4.0), and the Weinans model family.
   - Method: identical preprocessing for every indicator, ROC-AUC, and lead time at a fixed false-alarm rate, stratified by regime: Gaussian vs non-Gaussian noise, B- vs N- vs R-tipping.
5. **Still pending from earlier:**
   - CCA-1c reduction-test and P7-restatement session cards (proposed, not started);
   - P5 banner attribution check (Quinn 2023 vs Machta 2013);
   - X0's Established / Tier 1 label looks generous (owner decision);
   - Kooijman DEB book anchor;
   - glossary `[[g:…]]` markup for the 22 new entries;
   - QR-001 to QR-005 have not yet been through either gate.
6. **Push** — `main` was 8 commits ahead of `origin/main` before the EWS fold-in commits; the owner decides. `docs/demo/` is git-excluded locally (`.git/info/exclude`) and is still the owner's decision.

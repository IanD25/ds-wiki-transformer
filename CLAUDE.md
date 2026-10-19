# DS Wiki Research Platform — Claude Code Context

> **This file is auto-loaded by Claude Code on every session start.**
> **Read the charter first: `docs/RESEARCH_PLATFORM_CHARTER.md`** — it defines mission, epistemic rules, and working modes.
> Session history: `MASTER_SUMMARY.md` (legacy technical narrative, partially superseded) and latest `docs/SESSION_HANDOVER_*.md`.

---

## What This Project Is (2026-04-08 Reset)

A **personal research platform** — a structured, grounded lab notebook for Ian Darling's physics and cross-domain research. It is a guardrail against speculation, a cross-domain mapper, a hypothesis generator, and a continuous research journal.

It is **not** a product, not a paper validator, not seeking publication. See `docs/RESEARCH_PLATFORM_CHARTER.md` for the full mission statement and epistemic contract.

**Prior framing (archived):** The project was previously scoped as "Principia Formal Diagnostics (PFD)" — a paper validation tool. That framing is no longer active. The product-arc documents (`PFD_PROJECT_FOUNDATIONAL_PLAN.md`, `SCF_PHASE3_DESIGN.md`, Phase 3/4/5 plans) are historical reference only.

- GitHub: `https://github.com/IanD25/ds-wiki-transformer`
- Python: 3.13, Apple M4 dev machine | also: Windows ShadowPC with RTX 2000 GPU
- Owner: Ian Darling (no academic affiliation, not chasing publication)

---

## The Epistemic Contract (Critical — Read Charter For Full Version)

Claude's standing instructions when working on this platform:

1. **Novelty skepticism is the default.** When something looks new, literature-search for prior art before treating it as a discovery. Report searches before celebrating.
2. **Triviality check.** Before promoting a finding, ask: *"Is this a 5-minute derivation from a known result?"* If yes, it's a re-derivation, not a discovery.
3. **Framing check.** Ask: *"Is there a standard framing where this becomes obvious or vacuous?"*
4. **Falsification first.** When the owner proposes a conjecture, try to break it before trying to support it.
5. **Plain-language statement.** Every conjecture must be statable in one sentence a physicist without wiki context could understand.
6. **Tripwire phrases.** Stop and audit if the session produces: "unification," "breakthrough," "paradigm," "fundamental insight," "solves [big problem]," "novel [X]" without a completed literature search.
7. **Confidence calibration.** Every claim tagged **Established** / **Supported** / **Speculative**. No silent promotion.
8. **AI-rabbit-hole tripwire.** Claude's job is to push back, not cheerlead. Stacking conjectures without testing them is drift. Feature-fitting to post-hoc definitions is drift. Flag it.

**The worst failure mode:** accumulating speculative claims that feel grounded because they're inside a well-organized wiki. The wiki's structure is not evidence for the wiki's content.

---

## Current Status (2026-10-19; pre-merge baseline 2026-10-18)

> **Read [`docs/SESSION_HANDOVER_2026-10-18.md`](docs/SESSION_HANDOVER_2026-10-18.md) first.** Mode A consistency pass `gsw-consistency-pass-2026-10-18`: the source DB brought in line with the calibration record, residual errors swept (including errors shared with the *Relatively Human* podcast), the H5 prior-art gate, claim/process views, a podcast crosswalk, and the M1 milestone. Milestone snapshot `snap_20261018_190812` is the **pre-merge baseline** for the planned wiki + podcast merge.

> **Later the same day (after that baseline; all owner-approved, corrections and fold-ins only, no promotions):**
> - **Prior-art fold-in:** BIO12–16, IT09–11, STAT4–6, URB1 ([report](docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md)).
> - **Early-warning-signal fold-in:** EWS1–EWS10 ([report](docs/prior_art_reviews/EWS_FOLD_IN_2026_10.md)).
> - **CCA reduction tests:** CCA-1c, CCA-1b magnitude and CCA-2 retired (see the CCA thread).
> - **QR-004 corrections** `gsw-qr004-corrections-2026-10-18` ([report](docs/prior_art_reviews/QR004_CORRECTIONS_2026_10_18.md)): 28 thermodynamics-of-information errors, mostly Landauer charged to operations that are not erasures (new drift tag `landauer-scope-overreach`).
> - **QR-004 fold-in** `gsw-qr004-fold-in-2026-10-18` ([report](docs/prior_art_reviews/QR004_FOLD_IN_2026_10_18.md)): NE07–NE10, BIO17–BIO25.
> - **IT06 geodesic check** `gsw-it06-geodesic-check-2026-10-18` ([report](docs/prior_art_reviews/IT06_GEODESIC_CHECK_2026_10_18.md)).
> - **QR-006b:** pilot passed and protocol frozen (tag `qr006b-prereg-frozen`); predictions recorded beforehand ([note](docs/experiments/QR006B_PREDICTIONS_2026_10_18.md)). Results on 2026-10-19, below.
>
> **2026-10-19 (owner-approved, corrections and fold-ins only, no promotions):**
> - **QR-005 corrections** `gsw-qr005-corrections-2026-10-19` ([report](docs/prior_art_reviews/QR005_CORRECTIONS_2026_10_19.md)). The 27 gravity-strand errors from the QR-005 map, all re-checked against primary sources, plus 10 further entries repeating the Bianconi misdescription.
>   - Main pattern: a thermodynamic, entropic or induced derivation of gravity read as "not quantum / no gravitons", although each uses ħ. New drift tag `emergent-read-as-classical`.
>   - Writes: 67 section banners and 19 links. Three wrong anchors fixed (HB09's Wall 2009 DOI pointed at Kerr/CFT; two GT02 anchors credited Dai & Stojkovic to Hossenfelder). Four calibration rows, labels unchanged. A dated banner in `CCA_GRAVITY_FINDINGS.md` §1.1.
> - **QR-005 fold-in** `gsw-qr005-fold-in-2026-10-19` ([report](docs/prior_art_reviews/QR005_FOLD_IN_2026_10_19.md)): GT12–GT17, the experimental side of the question.
>   - The entries: BMV entanglement witness; the excluded pairwise classical channel; Oppenheim's classical–quantum gravity; Diósi–Penrose collapse bounds; Schrödinger–Newton gravity; minimum-noise tests.
>   - The Oppenheim/Janse window discrepancy (S5) is resolved: the map used arXiv v1, not the published version.
>
> - **QR-006b confirmatory run** ([results](docs/experiments/QR006B_CONFIRMATORY_RESULTS_2026_10_19.md), [lead-time audit](docs/experiments/QR006B_LEADTIME_AUDIT_2026_10_19.md)): **NO in all decidable regimes** (Supported). See the early-warning thread.
> - **DFIG reduction test** `gsw-dfig-reduction-2026-10-19` ([report](docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md)): P6 and P7 Falsified, P5 → Speculative (owner); new drift tag `local-geometry-coincidence`.
> - **QR-001** literature-mapped ([map](docs/prior_art_reviews/QR-001_SLOPPY_MODELS_MAP_2026_10_19.md)).
> - **QR-005 gates** ([report](docs/prior_art_reviews/QR-005_GATES_2026_10_19.md)): re-scoped to QR-005b, parked as a watch item; GT12 Plávala note.
>
> The latest per-pass hand-over notes are these reports; no newer `SESSION_HANDOVER` file exists.

**Mission state:** M0 audit complete (2026-04-08). **M1 compiled 2026-10-18** — [`docs/M1_MILESTONE_COMPILATION.md`](docs/M1_MILESTONE_COMPILATION.md). Nothing has been promoted since M0. Every pass since (2026-10-18/19) made corrections, fold-ins, retirements and falsifications only.

**What we believe — 47 scientific claims, latest status each (`claim_status_latest` view in `wiki_history.db`):** 25 Speculative · 4 Supported · 7 Established · 7 Falsified · 4 Retired (P2, CCA-1c and CCA-1b magnitude folded; CCA-2 forced by definition). These are the counts after the DFIG reduction (commit `927c975`): P6 and P7 → Falsified, P5 → Speculative. Eight process records (terminology decisions, reading priorities, framework diagnoses) are tracked separately in `process_status_latest`. **Quote numbers from these views, never from raw calibration rows** (107 rows / 21 audit refs as of 2026-10-19 — several rows per entity, and process items mixed in).

**State by thread:**
- **D_eff / Fisher-rank (DFIG)** — reduction-tested 2026-10-19 (`gsw-dfig-reduction-2026-10-19`, commit `927c975`; [report](docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md)). M6's Phase 1 validation (owner repo `D_eff-Test-1.0`) used the uncentred gap-position Fisher rank, the same object as CCA-2.
  - **Tori and coarse-graining reduce:** every recorded rank and PR is an exact closed form in (σ, L, d), fixed by lattice symmetry. "Rank = d" is the d-fold translation sector (the Fisher rank of a d-dimensional location family), in a σ window only. The Erdős–Rényi "rank 1" is the estimator's mean term.
  - **Random geometric graphs give d + 1, not d;** the +1 survives centring and is unexplained.
  - **P5 Speculative** (downgraded from Supported by the owner; the 2026-04-20 χ-spectrum row re-expresses standard exponents). **P6 Falsified:** the kagome lattice (d_H = 2) gives PR 1.61, set by 60° neighbour angles (`local-geometry-coincidence`). **P7 Falsified:** at fixed physical scale the rank rises d → d + 1 under block-spin; the Fisher DPI (Zamir 1998) is not engaged because F is recomputed on a new graph. **M6** Established for the textbook Fisher matrix only (correction row).
  - Machta 2013 is a vocabulary anchor, not the same object: the Phase 1 matrix has no model parameters. P8 **Falsified** by Gefen–Mandelbrot–Aharony 1980 (STAT4). Ax2, OmD and T1 remain internal constructions; Ax2 and T1 carry 2026-10-19 banners.
- **CCA** — CCA-1 and CCA-1b scaling Falsified; **no CCA item is Supported any more**. CCA-1b magnitude and CCA-2 **Retired** 2026-10-18 by a pre-registered reduction test ([report](docs/experiments/CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md)): the April Phase A–D observables were the gap-position d_eff and gap-ratio η of `fisher_diagnostics` (not the χ spectrum). Phase C/D η is a fixed function of the nearest-neighbour bond energy, so the ~20× dη/dT separation is latent heat vs the 2D Ising log specific heat (Folded); on hypercubic tori d_eff ∈ {1, d, d+1} by symmetry, with d+1 = d translations + 1 uncentred-mean mode in an α window only (forced by definition; the 1e-8 spectral tolerance was missed via the tool's EPS guard, deviation accepted by owner). CCA-1c **Retired — Folded** 2026-10-18 by the λ₁ reduction test ([report](docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md)): because tr χ = N(q−1) is fixed, the first-order d_eff jump is the Potts order-parameter jump read through λ₁ ≈ N(q−1)⟨M²⟩ (Wu 1982); with λ₁ removed nothing jumps. STAT3 (the CCA class) **downgraded Supported → Speculative** 2026-10-18 (owner): its only support was that d_eff result; it is a classification, its "novel framing" claim is ungated and overlaps QR-002 / self-organised criticality. Terminology renames (d_eff vs Mattingly 2018; η vs η_critical) proposed, banners in place, body text not migrated.
- **Fisher–gravity chain** — Speculative: a conceptual analogy stacking "relative entropy" across different objects, confirmed by the 2026-05-04 Maldacena pass. Bianconi 2025 is not an independent second path (it uses quantum relative entropy). GT10 Supported, linearized only. P21 Established for Chentsov's classical theorem only. The IT06 check (2026-10-18) found that the slow-driving minimum-dissipation metric is the friction tensor (Sivak & Crooks 2012), which is Fisher–Rao only for constant relaxation time. So P21's instance (4) is withdrawn from Chentsov coverage (label unchanged), and X8's "Seifert bound" was mis-stated (its measured η values stand). The chain itself does not depend on IT06.
  - **QR-005 corrections (2026-10-19)** found three of the chain's four hop descriptions wrong as written; the label stays Speculative:
    - Hop 2's identity (Fisher = Hessian of KL) is not Cramér–Rao.
    - Hop 3 (IT03 → GT10) rests on the first law of entanglement (Jacobson 2016 Eq. 16). The relative-entropy variation vanishes for *any* state, whether or not Einstein's equation holds, so that link carries no Einstein content. The quantity is quantum relative entropy, not KL.
    - Hop 4's "classical limit" is not in Jacobson 2016. Both derivations are semiclassical; 2016 calls its key step "the usual Clausius relation" at T = ħ/2π.
  - Bianconi 2025 uses no Fisher metric at all (full text; the earlier "Bures" reading was an inference).
  - GT10 stays Supported, restated as: semiclassical, first-order state variations, no holography, silent on gravitons.
- **Cosmological coupling (P17, P23, GT11)** — Speculative, high risk. GW tension with k = 3 is ~3σ (Amendola 2024's 5σ was a forecast); Cadoni 2023's k = 1 is universal for regular BHs, with their own analysis preferring k = 3. Wording corrected throughout 2026-10-18.
- **Scaling** — P12 Falsified (β(λ) ≤ 1). P11 **Falsified** by Bettencourt 2013 (δ = H/[D(D+H)], not D/(D+1); now URB1). P2 **Retired — folded** into WBE 1997 (BIO12). H5's two-process form is a re-derivation and a **RESTATEMENT of West et al. 2003** ([prior-art report](docs/prior_art_reviews/H5_TWO_PROCESS_PRIOR_ART_2026_10_18.md)). C1's curvature is contested. C2's "β = 1 ± 1/D_eff" withdrawn as a restatement of Bettencourt 2013. P14a is the only runnable item. See [`docs/SCALING_RESEARCH_QUEUE_2026_05_04.md`](docs/SCALING_RESEARCH_QUEUE_2026_05_04.md), banners included.
- **Thermodynamics of information (QR-004)** — the answer, now folded in:
  - Cells run 10× (translation) to ~10⁸× (neural signalling) above Landauer: Established. Most cellular operations are not erasures, and copying is logically reversible (NE07, BIO19).
  - Against the bounds that do apply (TUR NE09, proofreading BIO17, sensing BIO20/BIO21), a few machines sit within ~2–6×, all from fitted models. The evidence says they are tuned for speed, not minimum energy (BIO18).
  - Whether near-bound operation buys fitness is open in the literature (BIO23; Yang 2021).
  - Q5/P15's "cost of coherence" has a published answer that contradicts the ansatz in form for molecular clocks (NE10: Zhang 2020, cost diverges as 1/(1−r)). Continuous oscillator models are model-dependent.
  - The B5/E2/TD3 "D-sensitive" facet was corrected to D-invariant.
- **Gravity: quantum or thermodynamic? (QR-005)** — map, corrections and fold-in done 2026-10-19:
  - **"Quantum vs thermodynamic" is largely a false choice.** Every thermodynamic derivation of gravity (Jacobson 1995/2016, Verlinde 2011, Sakharov) uses ħ and is silent on whether the field is quantized. Reading it as "not quantum" is the drift tag `emergent-read-as-classical`. "Einstein's equation behaves like an equation of state" is Supported; "therefore gravity is not quantum" is not what the cited authors claim.
  - **The live question is experimental: does gravity entangle, and if not, how much noise must it add?** Excluded: the pairwise classical channel (GT13); parameter-free Diósi–Penrose (GT15; R₀ > 4.5 × 10⁻¹⁰ m); Oppenheim's "noise everywhere" kernel (GT14).
  - **Still open:** Oppenheim's other kernels, with ~9 and ~11 orders left on direct data (GT14); a positive BMV witness would rule out LOCC gravity but not by itself prove gravitons, which is open in the literature (GT12); the noise route (GT17; threshold ~10⁻¹⁸ m s⁻²/√Hz at 1 mm, from one preprint).
  - The experiments are 7.5–10 orders of magnitude away. Nothing here is decidable in-house.
  - **Gated 2026-10-19** ([report](docs/prior_art_reviews/QR-005_GATES_2026_10_19.md)).
    - **As worded, ill-posed** (`emergent-read-as-classical`); re-scoped to QR-005b, *does gravity entangle?*
    - **The thermodynamic half is answered** and folded (`premise-false`).
    - **"Thermodynamic ⇒ irreversible, noisy gravity" restates Galley, Giacomini & Selby 2023** (*Quantum* 7:1142).
    - **QR-005b is open in the literature; Gate 2 DROP in-house** (`undecidable-with-obtainable-data`). **Parked 2026-10-19 (owner)**; resume conditions are in the log.
    - **Plávala 2026** (*PRD* 113:085004) argues that an indirect single-mass test is possible now, under stated assumptions. So "7.5–10 orders" applies to the direct experiment only. GT12 now records this route (note and anchor, `gsw-qr005-gates-2026-10-19`).
- **Early-warning signals (QR-006 / QR-006b)** — answered 2026-10-19 by a pre-registered benchmark ([results](docs/experiments/QR006B_CONFIRMATORY_RESULTS_2026_10_19.md)):
  - **NO in all decidable regimes (Supported).** No information indicator (lagged MI, transfer entropy, permutation and sample entropy, Fisher index, RPDE) beat the best non-information indicator by ΔAUC ≥ 0.05 in multiplicative noise, α-stable noise, flickering, or the multivariate network. The near-ties are near-copies: the Fisher index tracks variance, and MI tracks autocorrelation.
  - **Two strata gave no decision.** S4 (noise-induced tipping) is undetectable by any indicator. S5 (rate-induced) is inconclusive, with every indicator near chance.
  - **Window-0.5 sensitivity (done 2026-10-19):** with doubled windows the information indicators did not improve in S1, S2, S3 or SM (most fell), so the NO is not a data-length effect.
  - **Lead-time scores are unreliable in ramped strata** (causal-detrending artefact, found in the post-hoc audit). One Speculative lead remains: the Fisher index's online detection under flickering.
  - **For QR-008 (exploratory, not pre-registered):** the best *classical* indicator varies by regime. AC1 wins under multiplicative noise, MAD under α-stable noise, variance under flickering.
- **Glossary** — 41 entries; lint punch list 611 flags across 122 entries; `[[g:slug]]` markup not yet applied.

**Open items:**
1. *Relatively Human* podcast — **direction changed 2026-10-19 (owner).**
    - No errata or retrospectives; Seasons 1–2 stand as an archive, and the [crosswalk](docs/PODCAST_CROSSWALK_2026-10-18.md) carries an archive-status note.
    - Season 3 explores open questions across fields: established science tiered, a "same math or same mechanism?" segment, an optional labelled hunch segment.
    - The wiki is the research desk: question log → map → primer → tiered script → fact-check against the wiki.
    - First outline: `Season 3/S3E1 Can We See Collapse Coming/RH_S3E1_BeatOutline_v1.md` in the podcast folder, built on QR-006 / QR-006b.
    - The owner allows writing to the podcast folder for transcripts and new-episode files only.
2. Apply glossary markup from the lint punch list.
3. Renames: CCA d_eff / η in body text; λ "phase coherence" → process-contribution fraction (H3 title, C1, P13, P15).
4. P14a (branching-ratio variance vs BMR/MMR exponent gap) — runnable, not run.
5. Scaling item ②: does metabolic rate decompose into separate parallel fluxes at all? (Zhao 2015 is a single-network rival, not a decomposition.)
6. P9 is a monitoring gate and belongs in the Q-series; not moved.
7. Anchors 818/819 (P6/P7 `contradicts` Machta 2013): notes look swapped and P7's relationship is doubtful — owner review.
8. Content-property gaps: HB09, GT07, IT06 and X8 have no `mathematical_archetype` or `dimensional_sensitivity` (allow-listed as `KNOWN_UNTAGGED` in `tests/test_integration.py`); 10 entries (CM9–CM11, CR1, EM12, EM13, FM7, GV4, MS1, TD14) carry duplicate, identical rows for both properties. Not fixed — values need a judgment call. (The stale hard-coded test counts were fixed 2026-10-18: tests now read expected counts from the DB.)
9. `docs/demo/` commit decision — owner's.
10. QR-004 leftovers:
    - sub-question S6 (does the synchronization-cost threshold depend on network dimension?) needs both gates before any work, and carries a drift warning: it revives the d_f thread;
    - small corrections: RG04 (DPI ⇒ c-theorem overstatement, as fixed in INFO4), IT03 ("free energy = kT·KL between thermal states"), the CHEM2→B5 analogy link.
11. The `dimensional_sensitivity` facet in many entries (QM2, Q3, T6, T9 …) rests on the DS-internal posit that Ω_D acts on k_B and ℏ, not on any reference law. A DFIG-level review, not a quick fix.
12. QR-005 leftovers ([corrections report](docs/prior_art_reviews/QR005_CORRECTIONS_2026_10_19.md) §5):
    - map §G R7–R14 not folded in (owner deferred);
    - gates run 2026-10-19; QR-005b parked; the GT12 Plávala note was added;
    - link 869 (GT10 → HB09, "Einstein equation as fixed point of the GSL") is unsourced;
    - BR01's `mathematical_archetype` (conservation-law) does not fit.
13. DFIG / QR-001 leftovers ([reduction report](docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md) §3.4; [QR-001 map](docs/prior_art_reviews/QR-001_SLOPPY_MODELS_MAP_2026_10_19.md)):
    - QR-001 literature-mapped (partial), not gated; likely FOLD for the wiki's version, open in the literature for general probabilistic models (Quinn 2023 §8.2);
    - the RGG d + 1 is unexplained (prior-art gate first if anyone claims it);
    - ~~P5's anchor 100 holds the wrong DOI~~: fixed 2026-10-19 (`gsw-p5-anchor-doi-2026-10-19`; now 10.1063/1.4923066, Crossref-checked).
14. QR-006b leftovers ([results](docs/experiments/QR006B_CONFIRMATORY_RESULTS_2026_10_19.md) §7):
    - ~~window-0.5 sensitivity~~: done 2026-10-19 for S1–S3 and SM (results report §4b); no improvement;
    - the other §5.7 sensitivities (detrending, buffer 50, observation noise, Null-B) and stratum E (empirical) not run;
    - the S3 Fisher-index lead-time lead is Speculative and parked;
    - QR-008 is the natural follow-on and has not been gated.
15. QR-002 and QR-003 were parked "until QR-006b and QR-004 are finished". That condition is now met; the owner kept both parked (2026-10-19).

**Standing M0 findings (2026-04-08; P17/P23 wording since corrected).**

> **Superseded in part, 2026-10-18/19. The thread bullets above take precedence.** The DFIG bullet's "P5 Supported as application" no longer holds: P5 is Speculative, and Machta 2013 is a vocabulary anchor, not the same object. The CCA bullet's "CCA-1c remains Speculative / narrow-novel" no longer holds: every CCA item is now Falsified or Retired. The rest stands as historical context.

- **DFIG is a re-parameterization of the sloppy-models program** (Sethna group, 2006–present). Not novel. P5 is Supported as application, not Established as discovery.
- **CCA's general setting is Machta-Chachra-Transtrum-Sethna Science 2013** (arXiv:1303.6738) — confirmed via primary-source reading. FIM eigenvalue spectrum on 2D Ising at criticality with stiff/sloppy hierarchy. Uses global couplings, not per-site fields. Does not sweep temperature. No Potts, no first-order discrimination. **Primary-source reading of 4 additional papers completed** (Transtrum 2015 JCP perspective, Mattingly 2018 PNAS, Brown-Bossomaier-Barnett 2022 Sci. Rep., Quinn 2023 Rep. Prog. Phys.): **no paper covers CCA's specific construction** (per-site fields + d_eff/η + T-sweep + first-order-vs-continuous discriminator). However, **two important findings from primary-source reading**: (1) **Mattingly 2018 is a mandatory citation** — it uses the term `d_eff` with a DIFFERENT formula (d_eff = Σ_r r·Ω_r from optimal discrete prior weight on manifold boundaries vs CCA's d_eff = (Σλ)²/Σλ² participation ratio) — CCA must cite Mattingly and distinguish the two formulas. (2) **Brown-Bossomaier-Barnett 2022 is the prior art for the broader research program** — they study Potts q=5,7,10 via Global Transfer Entropy (q=2 enters only through their earlier Ising work (corrected 2026-10-18 per `docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md` §5)) and find curve-shape differences qualitatively similar to CCA-1c, with a simple physical mechanism (cluster interfacial length). CCA currently lacks a comparable mechanism. **Highest-leverage open question:** can CCA's d_eff/η be explained via cluster interfacial geometry, or does it measure something structurally different from transfer entropy? See `docs/M0_MILESTONE_COMPILATION.md` Fourth Addendum for full findings. CCA-1 and CCA-1b L^d scaling are FALSIFIED; CCA-1b magnitude and CCA-1c shape are qualitatively supported on a single test only; charter rule prohibits promoting above Speculative without a second independent test (recommended: extend to q=2,5,7,10 to enable direct comparison with Brown et al.).
- **Fisher-gravity chain is downgraded from "structural coherence result" to conceptual analogy.** It stacks vocabulary ("relative entropy") across three distinct mathematical objects; Jacobson 2016 uses quantum entanglement entropy, not classical Fisher.
- **P17 is Speculative, high risk.** Citations VERIFIED via deep-research pass (Fifth Addendum): Amendola, Rodrigues, Kumar, Quartin 2024 MNRAS 528, 2377 (arXiv:2307.02474) is real — but wiki's "5σ" claim was the paper's FORECAST, not current data; current GWTC-3 gives 2σ upper limit k<2.1 with ~3σ tension. Cadoni et al. 2023 JCAP 11, 007 (arXiv:2306.11588) verified — 7-author paper, "universal" not "generic" k=1 for regular BHs, and crucially their own KS analysis prefers k=3 over k=1. Wiki wording for P17/P23/GT11/G12 corrected 2026-10-18.
- **CCA prior-art surface broadened by Fifth Addendum deep-research pass; corrected by Sixth Addendum primary-source reading.** The FIM in CCA IS the connected correlation matrix χ_ij — textbook stat mech. Prior-art map: **Vinayak-Prosen-Buča-Seligman 2014 EPL 108, 20006** (arXiv:1403.7218) gives a *rank* (Zipf) law for correlation-matrix eigenvalues at 2D Ising criticality, λ_j ≈ c_d/j^ζ with ζ = (d − θ)/d in the correlation-decay exponent θ — not a density law in η_critical; θ = η only in d = 2 (corrected 2026-10-18 per `docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md` §5); **Borgs-Chayes 1996 J. Stat. Phys. 82, 1235** (arXiv:adap-org/9411001) rigorously connects the q × q *colour* covariance matrix of a site pair to FK clusters — not the N × N site–site matrix, about whose spectrum it says nothing (corrected 2026-10-18 per `docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md` §5). **Saberi-Saber-Moessner 2024 PRB 110, L180102** (arXiv:2503.03472) is NOT direct prior art (Sixth Addendum correction): their matrix is the spin configuration arranged as L×L matrix, not the connected correlation matrix. Different mathematical object. Saberi uses rescaled max eigenvalue as order parameter, recovers Onsager magnetization with β/ν=1/8. CCA-1c remains Speculative; narrow-novelty surface is slightly broader than Fifth Addendum claimed. Sharpened mechanism question (Brown 2022): Brown's GTE is (in the wiki's description, not the authors' — GTE is a lag-1 dynamical conditional mutual information) a hybrid 2-point + multi-point observable; CCA's d_eff/η are pure 2-point. At first-order Potts, can pure 2-point reproduce hybrid 2-point + multi-point discrimination? Or only partial signal? Test via q=2,5,7,10 with both observables. **Saberi is the obvious external reviewer** for any CCA writeup — works on both cluster geometry and matrix-spectrum of 2D Ising. **Two terminology collisions** flagged: CCA d_eff vs Mattingly 2018 d_eff (different formulas), CCA η vs standard stat-mech η_critical (anomalous dimension). Both must be renamed.

Before any new experimental or conjecture work: read Transtrum-Machta-Sethna 2015, Quinn et al. 2022, Janke-Johnston-Kenna 2004, Prokopenko-Lizier 2011 (prior-art reading list in M0).

**Wiki scale (2026-10-19):**
- **363 entries** = 322 content entries + **41 glossary entries** (21 disambiguation pages, 20 defined terms).
  - The 322 content entries: 257 reference_law, 18 method, 15 law, 9 instantiation, 8 open question, 5 constraint, 3 axiom, 3 parameter, 3 theorem, 1 mechanism.
  - The reference_law count includes recent fold-ins: on 2026-10-18, 12 prior-art entries, 10 early-warning-signal entries (EWS1–EWS10) and 13 QR-004 thermodynamic-limits entries (NE07–NE10, BIO17–BIO25); on 2026-10-19, 6 QR-005 gravity-test entries (GT12–GT17) and 3 QR-010 machine-learning entries (ML1, ML2, ML5; the wiki's first ML generalisation entries).
- **994 links**, **1,302 property rows**, **2,320 ChromaDB chunks**
- **23 conjectures (P1–P23)**, **12 gates (G1–G12)**
- **587 tests** — all pass (2026-10-19, run after the QR-010 fold-in commit `4f4d436`)

**Provenance (2026-10-19):**
- **1,070 external anchors over 320 entities**, plus **47 internal constructions**
- Every non-glossary entry has an anchor or an internal-construction flag (the last orphan, GT05, was anchored 2026-10-18). The 21 glossary disambiguation pages have neither, by design.
- History: 42% provenance on 2026-04-18; full non-glossary coverage from commit `89a989d` (2026-04-20).

---

## Working Modes

Be explicit about which mode you're in at the start of any work session:

- **Mode A — Curation / Grounding.** Adding established science, cleaning links, running diagnostics on the wiki itself, literature searches to ground entries. Success = wiki better reflects cited science.
- **Mode B — Exploratory Research.** Testing owner's conjectures, running experiments, falsification attempts. Success = conjectures move through lifecycle with honest documentation.

Mode B depends on Mode A. Don't run experiments on ungrounded foundations.

---

## Quick Start (Fresh Machine)

> **The local iCloud copy is canonical:** `~/Library/Mobile Documents/com~apple~CloudDocs/Projects/DS_Wiki_Transformation`. GitHub (`origin/main`) is pushed periodically at the owner's request; check `git status -sb` — anything local and unpushed is newer than a fresh clone. Also: the `.venv` editable install still points at the old path `/Users/iandarling/Projects/DS_Wiki_Transformation/src` (tracebacks show it); re-run `pip install -e .` from the iCloud path if imports misbehave.

```bash
# 1. Clone
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd ds-wiki-transformer

# 2. One-command environment setup
bash setup.sh

# 3. Verify
source .venv/bin/activate
python3 -m pytest tests/ -v --tb=short   # 587 tests, all passing

# 4. Optional: start MCP server (for Claude tool access)
python3 src/mcp_server.py
```

**Data:**
- `data/ds_wiki.db` — the knowledge graph (READ ONLY, committed)
- `data/rrp/` — external dataset bundles (zoo_classes, ecoli_core, periodic_table, opera, ccbh, ieee_power_grid)
- `data/chroma_db/` — ChromaDB semantic index (bge-large 1024-dim, committed)
- `data/wiki_history.db` — embedding snapshots + **GSW anchor tables** + **domain tagging** + **calibration records** + the `claim_status_latest` / `process_status_latest` views. ~29 MB, tracked. Snapshot retention keeps the 3 most recent plus every **milestone** snapshot (trigger `milestone:*`, never pruned — each adds ~10 MB). Anchors, tags and calibration rows are reconstructible from `scripts/migrations/`; historical embeddings are not.
- `data/reports/` — diagnostic reports + experiment outputs

**Rebuild only if ds_wiki.db changes:** `python3 -m src.sync` (add `--milestone` only for a snapshot that must be kept permanently)

---

## Architecture (Unchanged — Tools Are Solid)

```
ds_wiki.db (SQLite, READ-ONLY)           RRP bundles (rrp_*.db, per-dataset)
        │                                        │
        ▼                                        ▼
   chroma_db/ (semantic index)         Pass 1: Parse → entries/links
        │                              Pass 1.5: EntityCatalogPass
        │                              Pass 2: CrossUniverseQuery
        │◄───────── bridges ──────────────────────│
        ▼
   MCP Server (mcp_server.py) — exposes tools to Claude
```

**Tools available:**
- **Fisher Suite** — `scripts/run_fisher_suite.py` with 6 modes (node, ds_wiki, internal_rrp, bridge, report, bridges). Structural analysis via FIM eigenvalue decomposition.
- **RRP ingestion** — parsers for 6 dataset types (zoo_classes_json, cobra_json, flat_json, ro_crate, frictionless, codemeta/citation_cff)
- **Cross-universe bridge detection** — semantic similarity matching between RRP and wiki
- **Gap analyzer** — finds isolated entries, sparse properties, link-type imbalances
- **Hypothesis generator** — surprising-pair detection via cosine similarity + type baselines
- **Visualizations** — tier-1 (D3.js network, regime charts) and tier-2 (bridge histogram, bipartite network, domain heatmap)

---

## Key Files

| File | Purpose |
|------|---------|
| `docs/RESEARCH_PLATFORM_CHARTER.md` | **ANCHOR DOCUMENT** — mission, epistemic contract, lifecycle |
| `docs/SESSION_HANDOVER_2026-10-18.md` | **Most recent session handover (2026-10-18)** — pre-merge consistency pass, podcast crosswalk, M1 |
| `docs/M1_MILESTONE_COMPILATION.md` | **M1 belief snapshot (2026-10-18)** — pre-merge baseline, numbers from `claim_status_latest` |
| `docs/PODCAST_CROSSWALK_2026-10-18.md` | *Relatively Human* podcast claims vs current wiki status, with on-air corrections |
| `docs/KNOWLEDGE_BASE_BLUEPRINT.md` | Generalised build blueprint for a knowledge base like this one |
| `docs/SESSION_HANDOVER_2026-05-04.md` | Prior handover — glossary, Maldacena + Kolokotrones passes, scaling (two calendar days; dates erratum at top) |
| `docs/SCALING_RESEARCH_QUEUE_2026_05_04.md` | Current state of the scaling cluster — what is runnable, open, falsified, retired |
| `src/glossary/` | Glossary subsystem — `[[g:slug]]` markup parser, renderers, load-bearing-word lint |
| `data/reports/glossary_lint_2026_05_04.md` | Punch list: 611 high-severity flags across 122 entries needing term binding |
| `docs/SESSION_HANDOVER_2026-04-18.md` | Earlier handover (2026-04-18) — GSW anchor architecture + retagging (provenance reached full coverage 2026-04-20) |
| `docs/GSW_ANCHOR_ARCHITECTURE.md` | **GSW anchor schema + design** — relationships, canonical roles, tiering, durability model |
| `docs/GSW_SOURCE_BASKET.md` | Per-domain canonical-source basket audit across 10 top-level domains × 5 canonical roles |
| `docs/prior_art_reviews/` | Prior-art gate reports, literature maps (QR-001, QR-004, QR-005, QR-006), correction and fold-in reports, anchor proposals |
| `docs/QUESTIONS_RAISED_LOG.md` | Open questions the wiki raises, with status (raised → mapped → gated → filed / parked) |
| `docs/QUESTION_GATES.md` | Gate 1 (prior art) and Gate 2 (worth asking): rules and verdicts |
| `docs/experiments/` | Pre-registered tests: reduction tests (CCA, DFIG), the QR-006b benchmark (pre-registration, predictions, pilot, results, audit) |
| `docs/primers/` | Plain-language primers for the owner (QR-005 gravity) |
| `docs/M0_MILESTONE_COMPILATION.md` | M0 belief snapshot (2026-04-08) — post-audit conjecture calibration, headline downgrades, action items |
| `src/config.py` | Paths, model, thresholds |
| `src/sync.py` | Rebuild chroma_db + wiki_history.db from ds_wiki.db |
| `src/mcp_server.py` | FastMCP server exposing tools to Claude |
| `src/embedder.py` | BGE embedding, ChromaDB operations |
| `src/analysis/fisher_diagnostics.py` | FIM math, `analyze_node`, `sweep_graph`, `build_bridge_graph` |
| `src/analysis/fisher_bridge_filter.py` | Per-bridge quality scoring |
| `src/analysis/fisher_report.py` | Two-tier diagnostic report (wiki health tool) |
| `src/analysis/gap_analyzer.py` | Gap detection on the wiki |
| `src/analysis/hypothesis_generator.py` | Surprising-pair detection |
| `src/analysis/coverage_analyzer.py` | Coverage metrics |
| `src/ingestion/rrp_bundle.py` | RRP SQLite schema |
| `src/ingestion/cross_universe_query.py` | Pass 2: RRP → wiki bridge detection |
| `src/ingestion/passes/entity_catalog_pass.py` | Pass 1.5: pattern extraction |
| `scripts/run_fisher_suite.py` | Fisher CLI (6 modes) |
| `scripts/run_entity_catalog_pass.py` | Pass 1.5 + 2b CLI |
| `data/ds_wiki.db` | The knowledge graph (READ ONLY — never schema-alter) |
| `MASTER_SUMMARY.md` | Legacy technical narrative (partially superseded by charter) |
| `docs/SESSION_HANDOVER_2026-04-16.md` | Prior session handover — M0 audit closeout (six addenda) performed 2026-04-08 |
| `docs/SESSION_HANDOVER_2026-04-07.md` | Earlier session handover — CCA falsification cascade (Phase A-D experiments) |
| `docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md` | Proposed (banners in place, body text not migrated): CCA d_eff vs Mattingly d_eff; CCA η vs η_critical |
| `docs/CCA_MATHEMATICAL_FORMALIZATION.md` | CCA framework — audited in M0 (six addenda) and Phase E; notation banner |
| `docs/CCA_GRAVITY_FINDINGS.md` | Fisher-gravity chain — audited: conceptual analogy; §1.3 (Bianconi path) retracted 2026-05-04 |
| `docs/archive/` | Product-arc docs (PFD foundational plan, Phase 3 designs) — historical only |

**Deprecated / deprioritized (still exist, no longer primary):**
- `src/analysis/result_validator.py` — paper claim validator. Useful as a quick-check utility. Not a featured capability.
- `src/analysis/link_classifier.py` — LLM link-type classifier. Wiki curation only.
- `src/analysis/structural_alignment.py` — SCF structural alignment. Not being built on.
- `src/analysis/semantic_position_test.py` — parked prototype.

---

## Current Embedding Model

```python
# src/config.py — auto-detected at import time
# CUDA (ShadowPC RTX 2000): "BAAI/bge-large-en-v1.5"  # 1024-dim
# MPS  (Mac Apple Silicon): "BAAI/bge-large-en-v1.5"  # 1024-dim
# CPU  (fallback):          "BAAI/bge-base-en-v1.5"   # 768-dim
DEVICE, EMBED_MODEL, EMBED_DIM = _detect_device()
```

**Windows note:** DS Wiki entry data contains Unicode math symbols. Always prefix Python commands with `PYTHONUTF8=1` on ShadowPC:
```powershell
PYTHONUTF8=1 .venv\Scripts\python.exe scripts\run_entity_catalog_pass.py ...
```

---

## Key Commands

```bash
# Rebuild semantic index after any ds_wiki.db change
python3 -m src.sync

# Run all tests
python3 -m pytest tests/ -v   # 587 tests

# Wiki self-analysis (check wiki health)
python3 scripts/run_fisher_suite.py --mode ds_wiki --wiki-db data/ds_wiki.db

# Single-node structural analysis
python3 scripts/run_fisher_suite.py --mode node \
    --wiki-db data/ds_wiki.db --node-id CHEM5

# Internal RRP diagnostics (for imported datasets)
python3 scripts/run_fisher_suite.py --mode internal_rrp \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db

# Cross-domain bridge detection (RRP vs wiki)
python3 scripts/run_fisher_suite.py --mode bridge \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db --min-sim 0.75

# Run Pass 1.5 + Pass 2b on an RRP bundle
python3 scripts/run_entity_catalog_pass.py \
    data/rrp/periodic_table/rrp_periodic_table.db \
    data/chroma_db \
    data/ds_wiki.db
```

---

## Critical Architectural Constraints

1. **Never schema-alter `ds_wiki.db`** — read-only source of truth; all new tables go in `wiki_history.db`
2. **INSERT OR IGNORE throughout** — all migration scripts safe to re-run
3. **numpy only** (no scipy) in ingestion passes — scipy not installed
4. **Confidence calibration required** — every new entry or conjecture tagged Established / Supported / Speculative; no silent promotion
5. **Falsification before support** — no conjecture reaches "Supported" without at least one honest falsification attempt
6. **Literature check before novelty claims** — charter § Epistemic Contract rule 1

---

## Conjecture Summary (23 P-series + CCA — status as of 2026-10-19)

Labels are the latest calibration rows (`claim_status_latest`); `conjectures.three_state` now carries the same label as a prefix (2026-10-18).

- **Falsified:** P12 (structural bound β(λ) ≤ 1); P8 (by Gefen–Mandelbrot–Aharony 1980; STAT4); P11 (by Bettencourt 2013; URB1); P6 (kagome counter-test, 2026-10-19); P7 (rank rises d → d + 1 at fixed physical scale, 2026-10-19); CCA-1 (Phase C); CCA-1b L^d scaling (Phase D)
- **Retired — folded into the literature:** P2 (WBE 1997; BIO12); CCA-1c (order-parameter discontinuity via λ₁ = S(k=0); Wu 1982 — 2026-10-18 λ₁ reduction test); CCA-1b magnitude (η = function of NN bond energy; latent heat vs log specific heat — 2026-10-18 reduction test)
- **Retired — forced by definition:** CCA-2 (gap-position d_eff = d+1 only in an α window, from hypercubic symmetry + uncentred estimator — 2026-10-18 reduction test)
- **Established:** P21 — Chentsov's classical uniqueness theorem only; the quantum case is Petz's classification
- **Supported:** P18, P19, P20 (single-domain, US equities / AlphaEntropy)
- **Speculative — support reduced to a textbook fact:** P5 (torus rank = d is the location-family Fisher rank via lattice symmetry; RGGs give d + 1; downgraded 2026-10-19, owner)
- **Speculative — ansatz without derivation:** P13, P15 (P15's Landauer motivation void), P23
- **Speculative — heterodox, no unique prediction:** P1, P4, P10
- **Speculative — other:** P3 (over-parameterized operator), P9 (monitoring gate; belongs in Q-series), P14 (split into P14a runnable / P14b blocked), P16 (blocked on Q4 specification), P17 (high risk), P22 (trichotomy unproven)

**Fisher-gravity chain** (M6→IT05→IT03→GT10→GT01): Speculative — conceptual analogy, not a structural result. Hops 2–4 were also mis-described; hop 3 is vacuous (first law of entanglement). Corrected 2026-10-19 under `gsw-qr005-corrections-2026-10-19`.

---

## Repo Organization

```
/
├── CLAUDE.md                            ← YOU ARE HERE
├── docs/
│   ├── RESEARCH_PLATFORM_CHARTER.md     ← ANCHOR — read this first
│   ├── SESSION_HANDOVER_2026-10-18.md   ← most recent (pre-merge consistency pass)
│   ├── M1_MILESTONE_COMPILATION.md      ← current belief snapshot (M0 is the 2026-04-08 one)
│   ├── PODCAST_CROSSWALK_2026-10-18.md  ← podcast claims vs wiki status
│   ├── SESSION_HANDOVER_2026-*.md       ← earlier handovers (05-04, 04-20, 04-18, 04-16, 04-07, …)
│   ├── SCALING_RESEARCH_QUEUE_2026_05_04.md
│   ├── CCA_MATHEMATICAL_FORMALIZATION.md ← audited (M0, Phase E)
│   ├── CCA_GRAVITY_FINDINGS.md          ← audited (analogy; §1.3 retracted)
│   ├── prior_art_reviews/               ← prior-art gate reports
│   ├── FISHER_PIPELINE_REDESIGN.md      ← tool spec (still valid)
│   ├── ARCHITECTURE_DECISIONS.md        ← ADR log
│   └── archive/                         ← product-arc docs (historical only)
│       ├── PFD_PROJECT_FOUNDATIONAL_PLAN.md
│       ├── SCF_PHASE3_DESIGN.md
│       └── (other deprecated specs)
├── README.md
├── MASTER_SUMMARY.md                    ← legacy narrative (partially superseded)
├── USER_GUIDE.md                        ← legacy (product framing)
├── setup.sh
├── requirements.txt
├── src/
│   ├── config.py
│   ├── sync.py, embedder.py, extractor.py, topology.py, mcp_server.py
│   ├── analysis/          ← Fisher Suite + diagnostic tools
│   ├── ingestion/         ← RRP parsers and passes
│   └── viz/               ← tier-1/tier-2 visualization
├── scripts/
│   ├── run_fisher_suite.py
│   ├── run_entity_catalog_pass.py
│   ├── ising_fim_*.py, potts_fim_test.py, cca1b_*.py   ← CCA experiments
│   └── migrations/        ← one-time DB insert scripts
├── tests/                 ← pytest suite (587 tests, all passing)
├── data/
│   ├── ds_wiki.db         ← READ ONLY
│   ├── chroma_db/, wiki_history.db
│   ├── reports/           ← diagnostic reports + experiment outputs
│   └── rrp/               ← external dataset bundles
└── Outside Ref/           ← external analysis documents
```

---

## If You're A Fresh Claude Session

1. **Read `docs/RESEARCH_PLATFORM_CHARTER.md` first.** It defines the mission and the epistemic rules.
2. **Read `docs/SESSION_HANDOVER_2026-10-18.md`** — the latest session handover (its §10 covers the start of the later passes). The **Current Status** block above, the per-pass reports it links and `docs/QUESTIONS_RAISED_LOG.md` cover everything since. Then read `docs/M1_MILESTONE_COMPILATION.md` for beliefs as of the M1 baseline. The claim counts above supersede M1's. For older context: `docs/SESSION_HANDOVER_2026-05-04.md` (note its dates erratum) and `docs/SESSION_HANDOVER_2026-04-18.md` (GSW anchor architecture).
3. **Read `docs/GSW_ANCHOR_ARCHITECTURE.md`** for the schema and design decisions (relationship taxonomy, canonical roles, durability model).
4. **For anchoring work, read `docs/GSW_SOURCE_BASKET.md`** — per-domain canonical source reference.
5. **Prior context**: `docs/SESSION_HANDOVER_2026-04-16.md` (M0 audit closeout) is still relevant for conjecture calibration.
6. **Operate as a skeptical research collaborator, not an assistant.** Your job is to push back. Stacking claims is drift. Feature-fitting is drift. Flag both.
7. **Confidence tag everything new.** Established / Supported / Speculative. No silent promotion. Anchor confidence: high / medium / low.
8. **Run both question gates before any new Q/P/Postulate or Questions Raised Log entry** — see `docs/QUESTION_GATES.md`. Gate 1, prior art (`memory/feedback_prior_art_gate.md`): mandatory deep literature review; "yes and" scaffolding is explicitly harmful. Gate 2, worth asking (`memory/feedback_worth_asking_gate.md`): if no prior work is found, find out why — trivial, absent for a reason, obvious or erroneous, avoided by experts — before PROCEED / RE-SCOPE / FOLD / DROP. Open questions are logged in `docs/QUESTIONS_RAISED_LOG.md`.
9. **Preserve falsifications.** Never delete wrong claims — label as falsified per `memory/feedback_preserve_falsifications.md`. Use specific labels per `memory/feedback_diagnostic_labels.md`.
10. **Provenance is complete for non-glossary entries** (1,070 anchors over 320 entities + 47 internal constructions, 2026-10-19). New entries need an anchor or an internal-construction flag at creation; check orphans with one JOIN (entries in neither table). Use the cluster-template pattern per `SESSION_HANDOVER_2026-04-18.md` when anchoring a batch.
11. **Report numbers from `claim_status_latest` / `process_status_latest`**, not raw calibration rows. If a correction collides with an existing (entity, date, audit_ref) row, use a `-<topic>` sub-ref (precedent: `gsw-consistency-pass-2026-10-18-h5-gate`).

# Podcast Crosswalk — *Relatively Human* claims vs current wiki status

> **Archive status, 2026-10-19 (owner decision).** Seasons 1–2 explored the DS framework. Since this crosswalk was written, the framework's main claims have been tested and largely retired in the wiki:
> - every CCA item Falsified or Retired;
> - P6 and P7 Falsified, and P5 Speculative (DFIG reduction test, 2026-10-19);
> - the Fisher–gravity chain an analogy;
> - P2, P8, P11 and P12 folded or falsified.
>
> The owner has chosen **not** to produce errata or retrospective segments. The past episodes stand as an archive, and the current state of each topic is in the wiki (`CLAUDE.md`, `docs/QUESTIONS_RAISED_LOG.md`). This crosswalk is kept as a historical record and will not be refreshed item by item.
>
> Season 3 changes direction. It explores open questions across fields, with the established science tiered, a recurring "same math or same mechanism?" segment and an optional labelled hunch segment. The wiki is the research desk. The first outline is `Season 3/S3E1 Can We See Collapse Coming/RH_S3E1_BeatOutline_v1.md` in the podcast folder.
>
> Machine transcripts (whisper-large-v3-turbo) were added on 2026-10-19 to the nine episode folders that lacked one.

**Date:** 2026-10-18 · **audit_ref:** `gsw-consistency-pass-2026-10-18` · **Purpose:** pre-merge bridge between the podcast (produced Feb–Mar 2026, before M0) and the wiki as it now stands.

**How to read this.** For each podcast claim: the episode, the exact wording (quoted from the scripts/transcripts — the podcast folder was read only), the matching wiki ID(s), the wiki's current label from `claim_status_latest` (latest calibration row per scientific entity, `wiki_history.db`) with its `audit_ref`, and a one-line correction fit for an on-air errata segment. Where a wiki entity has **no calibration record**, that is stated and the entry's own `status` field and internal-construction flag are given instead — those are weaker evidence than a calibration row.

**Provenance of quotes.** Quotes were extracted by a read-only pass over the podcast folder and **spot-checked first-hand (27 of them, all exact matches)** against the source files; the Season 1 Retrospective scorecard was also checked. Paths are relative to the podcast root `My Drive/1.a.Work Outputs/Releativly Human/`. `L` = line number in the .md/.txt file; for .docx/.pages sources it refers to a text conversion and is approximate.

**Episode labels do not match folder names.** `S1E3 Fisher's Ghost/` holds `RH_S1E4_Fishers_Ghost_Script.md` (script: "Season 1 · Episode 4"); `S1E4 Quantum Computer/` holds `RH_S1E6_The_Parallel_Architecture_Script.md` ("Episode 6"); `S1E5 …Purge_Equation_Script.md` says "Episode 6"; `S1E8 …WherTheWindCantBeCombed_Script.md` says "Episode 5". **S1E1 has no materials in the archive** (the Retrospective says it "is reconstructed from callbacks").

---

## Summary

| # | Episode | Claim (short) | Wiki ID(s) | Current wiki status | Verdict for errata |
|---|---|---|---|---|---|
| 1 | S1E2 | D_eff "the hidden variable"; exponents interpolate on fractals; Gate G5 | P8, G5, Ax2, T5 | P8 **Speculative** — restatement of Gefen–Mandelbrot–Aharony 1980 + JJK 2004 | **Correct on air** |
| 2 | Fisher's Ghost | Fisher Information Rank *is* effective dimensionality; Gate G1 | P5, M6, G1, T1 | P5 **Supported as application** — restatement of Machta et al. 2013 | **Correct on air** |
| 3 | Fisher's Ghost | Chentsov uniqueness; Frank 2009; quantum Fisher info & the uncertainty principle | P21, BIO3, IT05, QM2 | P21 **Established, classical theorem only**; BIO3/IT05 corrected this pass | **Correct on air** (Frank, uncertainty); nuance (Chentsov) |
| 4 | Parallel Architecture | D_eff governs measurement constraints at the quantum–classical boundary | P4, P5 | P4 **Speculative** — heterodox, no discriminating test | Hedged on air; minor note |
| 5 | Purge Equation | purge cascades as dimensional reduction | no wiki entity | — | Flag as analogy |
| 6 | Cell That Remembers | D_eff governs memory-kernel structure | no wiki entity (M4 Mori–Zwanzig is adjacent) | — | Flag as untested, no record |
| 7 | S1E8 (not S1E7) | Fisher rank drops at slip boundaries; singularities as "residue of dimensional projection" | no wiki entity; "Gate G1" misused | — | Flag as untested; gate mislabel |
| 8 | S1E9/E10/E13 | fractal dim, Fisher rank, attractor dim may be one quantity | P6, gloss_effective_dimension | P6 **Speculative — contradicted by own tests** | Update on air |
| 9 | S1E13 | "specified prediction": Fisher-rank monotonicity under coarse-graining | P7, G1, T1 | P7 **Speculative, partially falsified** | **Correct on air** |
| 10 | S1E13 | "specified prediction": metabolic exponent = D/(D+1) of vasculature | P2, C1, X1 | P2 **Speculative** — restatement of WBE 1997 | **Correct on air** |
| 11 | S1 Retrospective | scorecard: Fisher Information "In Progress" | P21, fisher_gravity_chain, M6 | P21 Established (classical only); chain **Speculative — analogy** | Clarify |
| 12 | S2 Primer | Conjectures 10–13 (emergence as a phase transition in constraint space; D_eff the governing variable) | Ax2 (11); no wiki entity (10, 12, 13) | Ax2: no calibration; internal construction, high-novelty-risk | Flag |
| 13 | S2E3 | Ashby's requisite variety ≡ attractor dimension | F1 (no such claim in wiki) | F1 established; wiki keeps them distinct | **Correct on air** |
| 14 | S2E5 | do exponents interpolate on fractional dimensions? (and "early results suggest smooth interpolation") | P8, G5 | P8 Speculative | **Correct on air** (the "suggest" line) |
| 15 | S1E1 / S2E2 | ¾ metabolic scaling; urban ≈ 1.17 and the "15% rule" | C1, X1, H5, P2, P11, P12, C2 | C1 Established (curvature contested); P12 **Falsified**; H5 **Speculative — re-derivation** | S2E2 fine; framework extensions need errata |
| 16 | (written docs only) | Ω_D | P3, OmD | P3 **Speculative — over-parameterized unification** | Never aired; no action |

---

## 1. Item by item

### 1 · S1E2 *Tipping Points* — D_eff as "the hidden variable"; interpolating exponents; Gate G5
**Quotes** — `Season 1/S1E2 Tipping points/RH_S1E2_Tipping_Points_Script.md`
- L26: "Conjecture P8: critical exponents interpolate continuously on fractional-D substrates, making dimension the hidden variable behind universality."
- L238 (HOST): "the Dimensional Scaling framework proposes that effective dimensionality is the hidden variable that unifies all of this, and that D-eff can be fractional, producing a continuous spectrum of universality classes."
- L214 (EXPERT): "The framework's research program — what it calls Gate G5 — lays out exactly what would constitute a pass and what would constitute a failure."

Note: G5 is a finite-size-scaling simulation on fractal lattices, **not** a bootstrap test — the script itself says the bootstrap "hasn't been applied to non-integer dimensions" (L210).

**Wiki:** P8 (claim), G5 (gate, "Critical exponent interpolation (P8)"), Ax2 (D_eff), T5 (test design).
**Status:** P8 — **Speculative**, `M0_2026-04-08`: rediscovery within the Gefen–Mandelbrot–Aharony 1980 / Janke–Johnston–Kenna 2004 lineage (`reframing_of` both). This pass added: Gefen et al. found critical properties on fractals depend on the fractal dimension **and** on topology (ramification, connectivity, lacunarity), with T_c = 0 and T_c > 0 systems at the same dimension. Ax2 has no calibration record (entry status `conjectured`; internal construction, high-novelty-risk).
**Errata:** "We said effective dimension is the hidden variable behind universality. That idea is not ours, and it is not that simple: in 1980 Gefen, Mandelbrot and Aharony showed that on fractals the exponents depend on how the fractal is connected as well as on its dimension — some fractals have no phase transition at all. Gate G5 is a test we proposed, not a result."

### 2 · *Fisher's Ghost* — Fisher Information Rank = effective dimensionality; "three gates"
**Quotes** — `Season 1/S1E3 Fisher's Ghost/RH_S1E4_Fishers_Ghost_Script.md`
- L27: "Conjectures P5–P7: Fisher Information Rank equals effective dimensionality. If correct, Fisher information isn't just useful in every field — it's the measurement tool for the hidden variable (D_eff) that governs all scaling laws."
- L195: "that rank — the number of statistically distinguishable parameters — *is* the effective dimensionality of the system at that scale."
- L217: "Three things, laid out as Gate G1 in the framework's research program." (The brief's "three experimental gates" is one gate with three tests.)

**Wiki:** P5, M6, G1 ("Fisher Rank monotonicity (P5, P7)"), T1.
**Status:** P5 — **Supported as application**, `gsw-cca-potts-sweep-phase-E-2026-04-20`: a restatement of Machta, Chachra, Transtrum & Sethna 2013 (sloppy models), applied to new model classes; at a continuous transition it reduces to standard critical exponents. M6 — **Established** (`gsw-maldacena-deep-research-2026-05-04`) only as a parameter-space diagnostic, with no emergent-spacetime content.
**Errata:** "We presented 'Fisher rank equals effective dimensionality' as the framework's idea. It restates the 2013 'sloppy models' work of Machta, Sethna and colleagues, applied to new systems. Where we tested it at an ordinary phase transition, it simply reproduced the standard critical exponents."

### 3 · *Fisher's Ghost* — Chentsov; Frank 2009; quantum Fisher information and the uncertainty principle
**Quotes** — same file
- L88: "Nikolai Chentsov proved in 1972 that the Fisher information metric is the only Riemannian metric on statistical models that is invariant under sufficient statistics." / "If you want a geometry on probability space, Fisher information is the only candidate."
- L143: "He showed that Fisher's Fundamental Theorem isn't just analogous to Fisher information — it *is* Fisher information."
- L231 (HOST): "Quantum Fisher information showed it underpins the uncertainty principle." … "Frank showed it's the engine of natural selection."
- L98: "The Heisenberg uncertainty principle … can be derived as a consequence of the quantum Cramér-Rao bound." / "The uncertainty principle isn't a separate postulate."

**Wiki:** P21 (Chentsov); BIO3 (Frank); IT05, QM2 and the M6→QM2 link (uncertainty).
**Status:** P21 — **Established for the classical theorem only**, `gsw-maldacena-deep-research-2026-05-04`: Chentsov uniqueness (up to scale, under sufficient statistics) holds; the quantum case is Petz 1996's *family* of monotone metrics, with no single canonical choice. BIO3, IT05, QM2: no calibration records (entries `established`); **the same two errors were found in the wiki and corrected in this pass** (see §2).
**Errata:**
- Chentsov — "The uniqueness result is real for ordinary probability. In quantum mechanics there is a whole family of such metrics, not one."
- Frank — "Steven Frank's 2009 result rewrites Fisher's theorem of natural selection in information terms. It's a reformulation, not the engine of natural selection, and Frank said so himself." (S1E13 L258 already corrected this on air.)
- Uncertainty — "Fisher information doesn't underpin the uncertainty principle. The uncertainty principle comes from quantum observables that don't commute. The quantum Cramér–Rao bound is a separate result, about how precisely you can measure."

### 4 · *The Parallel Architecture* — D_eff and measurement constraints at the quantum–classical boundary
**Quotes** — `Season 1/S1E4 Quantum Computer/RH_S1E6_The_Parallel_Architecture_Script.md`
- L25: "DS Conjectures P4, P5 as open questions about whether effective dimensionality governs measurement constraints at the quantum-classical boundary."
- L287: "effective dimensionality governs the constraints on measurement and resource generation at any scale … But that's a conjecture, not a result."
- L50: "We are not claiming mitochondria are quantum computers." (D_eff is never tied to mitochondria.)

**Wiki:** P4 (cytochrome c oxidase 1.5 ms as a "refresh rate"); P5. No entity for "D_eff governs measurement constraints".
**Status:** P4 — **Speculative**, `M0_2026-04-08`: no experiment has distinguished the refresh-rate reading from an ordinary kinetic speed limit [heterodox-alternative-without-unique-prediction].
**Errata:** "The 'refresh rate' reading of the CcO cycle has never been distinguished from a plain kinetic speed limit, and the idea that effective dimension governs measurement limits has no test behind it." (The episode already hedges this as Tier 3.)

### 5 · *The Purge Equation* — purge cascades as dimensional reduction
**Quotes** — `Season 1/S1E5 Autocratic Collapse/RH_S1E5_Purge_Equation_Script.md`
- L267: "Each execution is a coarse-graining operation on the state's information network. And the Data Processing Inequality guarantees that information lost in this way cannot be recovered"
- L360: "Tier 3 — framework-original conjecture … The interpretation of purge cascades as dimensional reduction — as a decrease in the effective dimensionality of the state's information network."

**Wiki:** no wiki entity.
**Errata:** "This was an analogy. Nobody has measured an 'effective dimensionality' for a political system, and the data-processing inequality is a theorem about information channels, not about executions."

### 6 · *The Cell That Remembers* — D_eff governs memory-kernel structure
**Quotes** — `Season 1/S1E6 Cell That Remembers/RH_S1E6_The_Cell_That_Remembers_Script.md`
- L391: "the structure of the memory kernel — its timescale, its decay profile, its effective rank — is governed by a single parameter: the effective dimensionality of the system's information geometry."
- L424: "Tier 3 — conjecture. The proposal that effective dimensionality governs memory kernel structure."

**Wiki:** no wiki entity. M4 (Mori–Zwanzig projection, established) is the adjacent established result; the wiki does not claim D_eff governs it.
**Errata:** "The memory-kernel claim is untested speculation, and it isn't even recorded as a conjecture in the research notes it came from."

### 7 · S1E8 *Where the Wind Can't Be Combed* — slip boundaries; "residue of dimensional projection"
**Quotes** — `Season 1/S1E8 Mathematics is the art of giving /RH_S1E8_WherTheWindCantBeCombed_Script.md` (script label "Episode 5"). **S1E7 contains no Fisher-rank or DS content.**
- L317: "every 'slip boundary' we've discussed … is a surface where the effective dimensionality drops sharply."
- L319: "The singularities — the polar vortices, the edge channels, the anyons, the Turing spots — are, on this view, the computational residue of dimensional projection."
- L323: "The prediction is that Fisher rank should be higher in the bulk of the jet stream … and lower at the boundary … This is Gate G1 in the framework's falsification program."

**Wiki:** no wiki entity. Gate G1 in the wiki is "Fisher Rank monotonicity (P5, P7)", not a slip-boundary test.
**Errata:** "The slip-boundary prediction is untested, and it isn't Gate G1 — that gate is a different test. Treat the 'dimensional projection' picture as a metaphor."

### 8 · S1E9 / S1E10 / S1E13 — are fractal dimension, Fisher rank and attractor dimension one quantity?
**Quotes** — `Season 1/S1E10 Chaos Is a Vital Sign?/Script/RH_S1E10_Chunk3_Synthesis_Wrapup.md`
- L27: "Whether those different measures are all getting at the same underlying quantity is an open question. … Nobody has proven it."
- L41: "when someone measures the fractal dimension, the Fisher information rank, and the attractor dimension of the same system at the same scale and checks whether they agree — we'll have an answer."

Posed as an open question on air, not stated as fact. S1E7 L162 separately calls the atmosphere's Kaplan–Yorke dimension its "effective dimensionality".

**Wiki:** P6 (fractal dimension ↔ Fisher rank); `gloss_effective_dimension` (disambiguation page: these are different senses).
**Status:** P6 — **Speculative**, `gsw-cca-potts-sweep-phase-E-2026-04-20` (M0: contradicted by own tests). The project's own Phase 1 tests found gap-based Fisher rank does **not** converge to the Hausdorff dimension on fractals; only the participation ratio, a different observable, does.
**Errata:** "Part of that open question has an answer now, and it's 'no': when we tested it, Fisher rank did not match fractal dimension on fractals. And the Kaplan–Yorke 'effective dimension' of the weather episode is a different quantity again."

### 9 · S1E13 *Sufficient Allegory* — Fisher-rank monotonicity as a "specified prediction"
**Quotes** — `Season 1/S1E13/RH_S1E13_Script_Final.md`
- L316: "Fisher information rank should decrease monotonically under coarse-graining in Ising models, gene regulatory networks, and financial time series. That's testable, specified, and untested."

Related: `RH_S1E4_Fishers_Ghost_Script.md` L203: "It must. That's not a conjecture — it's a mathematical theorem."

**Wiki:** P7, G1, T1.
**Status:** P7 — **Speculative, partially falsified**, `M0_2026-04-08`: the participation ratio failed monotonicity in **every** tested configuration; only gap-based rank on lattices under block-spin coarse-graining passed [contradicted-by-own-tests]. Nuance on the "theorem" line: if you coarse-grain the data through a Markov map with the parameters held fixed, Fisher information can only decrease, and exact rank cannot rise — that much is a theorem. It does not cover RG coarse-graining that changes the parameterisation, or the participation-ratio proxy the project actually used.
**Errata:** "It wasn't untested by the time this aired — part of it had already failed. The participation-ratio version broke in every case we tried; only the strict rank version held, on simple lattices. Calling it 'a mathematical theorem' in the Fisher episode went too far."

### 10 · S1E13 — metabolic exponent tracks vascular dimensionality
**Quotes** — `Season 1/S1E13/RH_S1E13_Script_Final.md` L316: "The metabolic scaling exponent should equal the effective dimensionality of the vascular network divided by that dimensionality plus one. That's precise, falsifiable, and unconfirmed." (First stated in *Fisher's Ghost* L213.)

**Wiki:** P2; C1; X1.
**Status:** P2 — **Speculative**, `M0_2026-04-08`: the formula α = D/(D+1) is West, Brown & Enquist 1997 (`reframing_of`); the "tracks D_eff" framing adds nothing testable without vascular data that does not exist. C1 retired its implied-D_eff column (2026-07-25): inverting this formula gives two values above the embedding dimension.
**Errata:** "That formula is West, Brown and Enquist's from 1997, not a new prediction. When the formula is run backwards from real exponents, it gives impossible values, such as a dimension above three for blood vessels in three-dimensional space."

### 11 · Season 1 Retrospective — Fisher Information "In Progress"
**Quote** — `General Docs/RH_S1_Retrospective_Document.docx`, §5 scorecard: "Fisher Information | Passed (Chentsov) | Partial (Frank 2009; reformulation, not mechanism) | Limited | In Progress | E4". The Fisher-rank = D_eff conjecture is not on the scorecard; it sits under the unrated "dimensional convergence" question.

**Wiki:** P21; fisher_gravity_chain; M6.
**Status:** P21 — Established (classical theorem only). fisher_gravity_chain — **Speculative**, `gsw-maldacena-deep-research-2026-05-04`: a conceptual analogy that stacks "relative entropy" across different mathematical objects [vocabulary-stacking-analogy]. M6 — Established as a parameter-space diagnostic only.
**Errata:** "'In progress' is generous. Chentsov's uniqueness holds for ordinary probability. The idea that thermodynamics, scaling and gravity share one Fisher-information foundation is an analogy, and the gravity link mixes up different kinds of entropy."

### 12 · Season 2 Primer — Conjectures 10–13
**Quotes** — `General Docs/RH_S2_Primer_v1.md`
- L72 (10): "Phase transitions across domains share a universal constraint-resetting mechanism."
- L75 (11): "Effective dimensionality is the governing variable that determines which features persist through transitions." / "The DS framework's central conjecture."
- L78 (12): "Batterman's asymptotic borderland concept generalizes beyond physics."
- L81 (13): "Emergence is a phase transition in constraint space."

The Primer's numbers are its own, not wiki P-numbers.

**Wiki:** 11 → Ax2 (no calibration record; entry `conjectured`; internal construction, **high-novelty-risk**), tested via G1 / P7. 10, 12, 13 → no wiki entity.
**Errata:** "These were framing ideas for Season 2. None of them is supported yet. The 'governing variable' idea depends on a test that has partly failed (see item 9)."

### 13 · S2E3 *Your Heart Isn't a Clock* — Ashby's variety ≡ attractor dimension
**Quotes** — `Season 2/S2E3 Why_a_healthy_heart_needs_chaos/RH_S2E3_WhyYourHeartIsntAClock_Script_v1.md`
- L250: "It's the same quantity wearing different clothes. When we said a healthy heart lives on a strange attractor with dimension around five, we were saying it has roughly five independent regulatory modes … Ashby counts those as variety."
- Transcript (`.pages`, approx. L158): "They are the exact same mathematical property."
- L531: "this specific bridge is novel."

**Wiki:** F1 (Ashby's law, `established`, no calibration record). **The wiki makes no such equation**: F1 records Ashby's bound as independent of spatial D_eff. No wiki entity for attractor dimension.
**Errata:** "Requisite variety and attractor dimension are not the same quantity. Variety counts distinguishable states; attractor dimension is a scaling exponent. The link is an analogy, and calling the bridge 'novel' needed a literature check we hadn't done."

### 14 · S2E5 *The Phase Between* — do exponents interpolate on fractional dimensions?
**Quotes** — `Season 2/S2E5 Precise_Symmetry_of_Natural_Chaos/RH_S2E5_ThePhaseBetween_Script_v1.md`
- L586: "Do the exponents interpolate smoothly between the integer values … Or do they snap — jump to the nearest integer universality class?" / "The early results from Gefen, Mandelbrot, and Aharony suggest smooth interpolation."

**Wiki:** P8, G5 (as item 1).
**Errata:** "The question is fine, but the answer we hinted at isn't. Gefen, Mandelbrot and Aharony showed that critical behaviour on fractals depends on more than the dimension, so 'smooth interpolation' is not what they found."

### 15 · ¾ metabolic scaling (S1E1, absent from the archive) and S2E2 *The City That Thinks* (≈ 1.17, the "15% rule")
**Quotes** — `Season 2/S2E2 The City That Thinks/RH_S2E2_TheCityThatThinks_Script_v1.md`
- L102: "derived a predicted exponent of seven-sixths, about 1.17. Geoffrey West popularized this as 'the 15% rule' — double the population, get roughly 15% more output per person."
- L106: "It's not a constant of nature. … It's a basin the data keeps falling into, not a fixed point the data obeys."

S2E2 does not discuss ¾ metabolic scaling; S1E1 is not in the archive.

**Wiki:** C1 (Kleiber), X1, H5, P2, P11, P12, C2 (urban).
**Status:** C1 — **Established** (power-law metabolism) with curvature **contested** and no universal exponent (`gsw-kolokotrones-research-2026-05-04`, run 2026-07-25; slope gloss corrected this pass). X1 — **Speculative**, d_f = 2.7 retired. H5 — **Speculative**, two-process form a re-derivation (`gsw-consistency-pass-2026-10-18-h5-gate`). P11 — **Speculative, scope bounded**: the D/(D+1) form cannot exceed 1, so it cannot produce 1.17. P12 — **Falsified** (`gsw-scaling-queue-2026-05-04`, run 2026-07-25). C2 — no calibration record; its "β = 1 ± 1/D_eff" was withdrawn this pass as a restatement of Bettencourt 2013.
**Errata:** "S2E2 was right: 7/6 is Bettencourt's 2013 derivation, from cities being two-dimensional, and it's contested. What needs correcting is the framework's gloss: Kleiber's ¾ is not universal, and the 'effective-dimension fingerprint' readings of these exponents don't hold up."

### 16 · Ω_D
**Quotes:** not in any spoken dialogue. Written only in `Season 1/S1E2 Tipping points/RH_S1E2_Tipping_Points.docx` (entry table: "Ω_D | Scaling Operator | Tier 3 ‡_p | Operator that connects D_eff to physical parameters"), the S2E2 handoff document, and "do not name" guardrails. The phrase "a single scaling operator" does not appear.

**Wiki:** P3, OmD (entry `conjectured`; internal construction, high-novelty-risk), T3.
**Status:** P3 — **Speculative**, `M0_2026-04-08`: one operator with a free exponent per quantity; its over/under-constraint audit has never been done [over-parameterized-unification].
**Errata:** none needed on air. Keep it out of any merged material until T3 is run.

---

## 1b. Further podcast claims that map to wiki entities

| Claim (quote, file:line) | Wiki | Note / errata |
|---|---|---|
| "That's not a conjecture — it's a mathematical theorem … So Fisher Rank can only decrease" — *Fisher's Ghost* L203 | T1, M6, P7 | See item 9: true for exact rank under fixed-parameter Markov coarse-graining; not for RG reparameterisation or the participation ratio. |
| "In the DS framework, the metabolic scaling exponent is D-eff over D-eff plus one." — *Fisher's Ghost* L213 | P2 | WBE 1997 (item 10). |
| "A branching vascular tree might have effective dimension 3.5." — S1E8 L313 | C1 (retired implied-D_eff column) | Contradicts the script's own "fewer dimensions than the space" definition. The wiki made the same error (reptiles 3.2, fish 7.3) and retired the column on 2026-07-25. |
| "Prediction: β = 1 ± 1/D_eff." — `S2E1 More than the Sum/S2E2_Handoff_Document.md` L63 | C2, P11 | Present in the wiki, corrected this pass (§2). |
| "Conjecture P7 states that effective dimensionality … must decrease monotonically. This explains why Yamanaka’s reprogramming is so difficult" — `Season 2/S2E6/Cell Differentiation_ A Hard Science Narrative.md` L25 (editorial "Yes And" document, not a script) | P7 | P7 is partially falsified; it explains nothing yet. Keep this document out of the merge. |
| "Water at three hundred seventy-four degrees, iron at seven hundred seventy degrees, and a random forest at its percolation threshold share the same critical exponents to eight decimal places" — S2E5 L21 (transcript adds "Ising symmetry") | no wiki entity (wiki is clean) | Water/CO₂ = 3D Ising; iron = 3D Heisenberg; percolation is its own class (and the episode's forest is 2D). Same pattern in S1E2 L89/L97 and S1E13 L84, which put superfluid helium among the Ising systems: it is 3D XY. |
| "the fractal dimension of that boundary is exactly 91/48" — `RH_S2E5_BeatOutline_v2.md` L210; transcript L212–214 ("fire boundary") | no wiki entity | 91/48 is the 2D percolation **cluster** dimension; the hull is 7/4. The S2E5 script itself says "cluster" correctly. |
| "the conformal bootstrap, now confirmed to nine decimal places" — S1E13 L248; "eight decimal places" — S2E5 L462; "six decimal places" — S1E2 L97 | T5 (wiki accurate) | Bootstrap precision is theoretical. Experiments on real fluids and magnets agree to roughly 2–4 significant figures, Monte Carlo to roughly 5–6. The episodes also disagree with each other (six/eight/nine). |
| "So √25,000 gives you approximately 158 … It's strikingly close." — S1E10 `Chunk2_Act2_BrainGene.md` L205–215 | no wiki entity | Kauffman's √N scaling was disproven (Samuelsson & Troein 2003, superpolynomial growth). S2E6 already retracted it on air ("a mirage"). |
| "Why … the universe guarantees it" — S2E4 L3; "Wilson proved that this *had to work*. Not just in physics — anywhere the separation of scales holds." — S2E4 L342 | no wiki entity (wiki is clean) | RG and irrelevant operators outside physics are an analogy, not a guarantee. The script's own tier table rates it "Tier 1 to 2". |
| "The same ratio of 4.669 governing the spacing of successive bifurcations." — S1E9 `Chunk2_Act2A_Act2B.md` L139; "The same constant. In the heart." — S1E10 `Chunk1` L145 | D2 (Feigenbaum, established; no cardiac claim in the wiki) | Period-doubling has been observed in cardiac tissue and models; Feigenbaum's constant has not been measured in hearts. |
| "We know the atmosphere's effective dimension is about two hundred" — S1E7 L280 | gloss_effective_dimension | Kaplan–Yorke dimension is one sense of "effective dimension"; not the framework's Fisher-rank D_eff. |

---

## 2. Wiki errors that came from the same source

The podcast and the wiki share an origin, so the podcast's errors were searched for in the wiki (`gsw-consistency-pass-2026-10-18`, Phase 3.2 and Phase 7).

**Present in the wiki, corrected this pass** (dated banners; original text kept):

1. **Fisher information "underpins" the uncertainty principle** — present as an analogy containing errors in **IT05** (*Constraint Category*: "both state that precision is bounded by the curvature of the underlying probability/wavefunction space") and the **M6 → QM2** link ("Fisher Information Rank is the classical … analog of the Heisenberg Uncertainty Principle: both bound the simultaneous precision of parameter estimation"). Corrected: Cramér–Rao is an estimation bound using Fisher information, not its rank; Heisenberg–Robertson follows from the commutator; the quantum Cramér–Rao bound is metrology. Anchor added: Braunstein & Caves 1994 on IT05.
2. **Frank 2009 as mechanism** — present, uncited, in **BIO3** in three sections ("additive genetic variance in fitness IS the Fisher information … Natural selection is Fisher information maximization"). Corrected to a reformulation. Anchor added: Frank 2009 on BIO3.
3. **"β = 1 ± 1/D_eff" for urban scaling** — present in **C2** *What's Conjectured*, with "implied D_eff ≈ 8" and "≈ 4.8". It restates Bettencourt 2013's derived β = 1 ± δ (δ = H/[D(D+H)] ≃ 1/6 → 7/6, 5/6) with a free D_eff, obtained by inverting single exponents, and contradicts P11's D/(D+1). Anchor added: Bettencourt 2013 (`reframing_of`) on C2.

**Present in the wiki, already corrected before this pass:** implied dimensions above the embedding dimension (podcast: "vascular tree … 3.5"; wiki: C1's reptile 3.2 / fish 7.3), retired 2026-07-25.

**Not present in the wiki:** the liquid–gas / iron / percolation universality lump; superfluid helium as Ising; 91/48 as a boundary dimension; "confirmed to N decimal places"; Kauffman √N matching cell types; Ashby variety ≡ attractor dimension; RG "guaranteed" outside physics; Feigenbaum governing the heart.

**Nuanced, left unchanged:** the wiki's T1 and M6 derive Fisher-rank monotonicity from the data-processing inequality. That holds for exact rank under fixed-parameter Markov coarse-graining but not for the RG and participation-ratio settings P7 was tested in. Recorded here for the owner; no edit made.

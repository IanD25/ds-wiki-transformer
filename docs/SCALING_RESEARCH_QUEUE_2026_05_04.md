# Scaling Research Queue — 2026-05-04

> **ERRATUM — dates (added 2026-10-18, `gsw-consistency-pass-2026-10-18`).** The work recorded under "2026-05-04" happened on **two calendar days**, and the label was carried onto the second.
>
> - **2026-05-04 (true date):** the Maldacena deep-research pass, the glossary subsystem, and the hypothesis / unexpected-links review. Evidence: `m0_maldacena_*` and `m0_glossary_*` migrations last modified 2026-05-04 11:48–14:16; sync backups `backup_20260504_160902` and `_181746` (UTC); `CCA_GRAVITY_FINDINGS.md` / `CCA_MATHEMATICAL_FORMALIZATION.md` modified 2026-05-04 11:50; `data/reports/hypothesis_2026_05_04/` and `glossary_lint_2026_05_04.md` written 2026-05-04; `gsw-maldacena-deep-research-2026-05-04` calibration rows dated 2026-05-04.
> - **2026-07-25 (true date):** the three scaling passes, the endpoint decision, and the Kolokotrones pass. Evidence: `m0_scaling_corrections` / `_reformulation` / `_queue`, `m0_endpoint_decision`, `m0_kolokotrones_research` last modified 2026-07-25 16:31–18:28; five sync backups dated 2026-07-25; every calibration row under those five audit_refs is dated 2026-07-25 (the scripts set `calibration_date` from `date.today()`, so the database recorded the real day); final snapshot `snap_20260725_223034`.
> - **Commits:** `17b6742`, `5741f9c`, `4cf550c`, `faca047` were all made 2026-07-25 — the 2026-05-04 work stayed uncommitted for 82 days and went in together with the 07-25 work. This queue document was written and then revised on 2026-07-25 (`5741f9c`, `faca047`); its "REVISED late 2026-05-04" header below refers to the 2026-07-25 Kolokotrones pass.
>
> **What carries the wrong date.** The five audit_ref suffixes `gsw-scaling-corrections-`, `gsw-scaling-reformulation-`, `gsw-scaling-queue-`, `gsw-endpoint-decision-`, `gsw-kolokotrones-research-` **`2026-05-04`**; those migrations' filenames; and the prose banners they wrote into `ds_wiki.db` reading "2026-05-04" — on **C1, H3, H5, X1, P11, P12, P14, P16**. Read that suffix as a session label; the work was done 2026-07-25. Banners on GT02, GT04, GT10, P17, P21, P23 and the `gloss_*` entries are correctly dated 2026-05-04. Per the no-deletion and append-only rules, nothing was renamed, no calibration row was edited, and no banner text was rewritten.

> **REVISED late 2026-05-04**, after a three-agent research pass on Kolokotrones et al. 2010 obtained the full text. The earlier version of this document listed "settle the endpoints" as a decision blocking λ's definition. **Both items are now resolved differently than anticipated** — see §Resolved. The revision is recorded rather than silently overwritten; the superseded framing is summarised at the end.
>
> **Audit refs:** `gsw-scaling-corrections`, `gsw-scaling-reformulation`, `gsw-scaling-queue`, `gsw-endpoint-decision`, `gsw-kolokotrones-research` — all `-2026-05-04`

---

## The one-line state

β(λ)'s functional form turns out to be **derivable** from two processes contributing additively, which supplies the mechanism the framework lacked and gives λ an operational definition. What remains open is **which two processes**. Separately, P12 is falsified, curvature is contested rather than established, and one conjecture is runnable today.

---

## Resolved this session

> **PRIOR-ART GATE — added 2026-10-18 (`gsw-consistency-pass-2026-10-18`; report: [`prior_art_reviews/H5_TWO_PROCESS_PRIOR_ART_2026_10_18.md`](prior_art_reviews/H5_TWO_PROCESS_PRIOR_ART_2026_10_18.md)).** The two-process identity below is a **re-derivation, not a finding** (charter rule 2), and a **RESTATEMENT of West, Savage, Gillooly, Enquist, Woodruff & Brown 2003** (*Nature* 421:713; arXiv:physics/0211058). They give b = Σ cᵢbᵢ with cᵢ = Bᵢ/B — exactly "λ = fractional contribution" — as the corrected form of Darveau et al. 2002's allometric-cascade equation, and call the additive model "only a consistency check of energy conservation, which must be trivially correct". H5 stays **Speculative**. What this section overstates:
>
> - **"λ has a definition"** — yes, as a share of the total. But that share is measurable only where the two fluxes are genuinely separate and add in parallel, which has to be shown for any proposed pair (West et al.'s objection to Darveau was double-counting steps that act in series).
> - **"The endpoint question is superseded"** — relocated, not answered. p and q are inputs to the identity; it says nothing about their values.
> - **"Supplies the mechanism the framework lacked"** (one-line state, above) — it supplies a meaning for λ, not a mechanism.
>
> **Open item ② needs reframing.** Ballesteros et al. 2018's f is a mass-independent constant, not λ (their λ-equivalent is fkM/B). Zhao 2015 is **not** a two-process decomposition: it is a single-network model, B = αM^x / log(M/β), that yields convex curvature with no second process — a rival account of the curvature. The live question is whether metabolic rate decomposes into separate parallel fluxes at all, and if so which. The text below is kept as written.

### λ has a definition

> **λ is the fractional contribution of one process to total metabolic rate**, where rate is a sum of two processes with different mass exponents.

From B = a·M^p + b·M^q, the local log-log slope is **p·f + q·(1−f)** with **f = a·M^p / B**. That is exactly β(λ). Recorded in H5 *What The Math Says* with the derivation shown.

Mentions no exponent. Measurable by measuring the two contributions separately. **Mass-dependent by construction**, which closes the earlier question about whether λ could be a species constant — it cannot, and now for a reason.

### The endpoint question is superseded, not answered

The endpoints are the two processes' exponents. Identify the processes and the endpoints follow. The earlier framing — "pick two bounding exponents" — was the wrong question.

The [2/3, 3/4] decision taken earlier today is **neither confirmed nor reversed**. Its stated rationale weakened on all three grounds (Kolokotrones' local slopes run 0.57–0.87, outside the wedge at both ends; 0.676 is a tangent slope at the mean of White & Seymour's mass distribution rather than a property of mammals; the curvature it accommodated is contested). But the question it answered no longer needs answering.

### The curvature-direction puzzle: min-rule vs sum-rule

The puzzle assumed constraints combine as a **minimum**, under which the lower exponent binds at large mass → concave. The models that reproduce the curvature use **sums**, where the lower exponent dominates at small mass → convex, the observed direction.

The thermal physics was sound. The combination rule was wrong.

**Vocabulary consequence:** "which constraint binds" implies a min-rule and yields the wrong curvature sign. Under an additive decomposition nothing binds — processes contribute in proportion. The framework has been sliding between two different physics with opposite signatures.

---

## What is runnable now

### ① P14a — branching variance vs. exponent gap

Unchanged by this session's findings, and still the only item with zero upstream dependencies.

| | |
|---|---|
| **Measure** | branching-ratio variance — micro-CT or corrosion casting |
| **Against** | published BMR/MMR exponent gaps, multiple taxa |
| **Method** | phylogenetically-corrected regression |
| **Confirms** | R² > 0.6 |
| **Kills** | no significant correlation after controlling for body mass |

**Design caveat.** MMR is individual, trainable, and transient, so a null result is ambiguous between "no relationship" and "obscured by MMR heterogeneity." Pre-register that concern. A within-species design (micro-CT plus V̇O₂max on the *same* animals) is cleaner and matches MMR's actual level of description, at higher protocol cost — treat it as confirmatory.

---

## What is open

### ② Which two processes — *a literature question, not a free choice*

This replaces the old endpoint question and is the live item.

Named candidates:

| Source | Decomposition |
|---|---|
| Ballesteros et al. 2018, *Sci. Rep.* 8:1448 | isometric (p=1) + surface (q=2/3), additive |
| Zhao, arXiv:1509.08912 | both 2/3 and 3/4 from a single Murray-law network; **explicitly denies** the small-mass 2/3 is the surface law |
| Kolokotrones et al. 2010 | vascular: pulsatile-to-smooth transition at a constant *fraction* of levels from the heart rather than a constant *number* from the capillaries |

Reading these two papers directly is bounded work and would settle what the endpoints are.

### ③ Q4 — *a specification step*

P16 (RLCT = d_f) would supply a β-independent route to d_f. Blocked at step zero: an RLCT is a property of a *specified* statistical model, and no biological learning problem has been mapped to SLT in a way yielding a computable one. **The queue item is Q4, not P16.**

---

## Falsified

**P12** — cross-domain universality. β(λ) is bounded above by 1 for every d_f and λ ∈ [0,1]; urban socioeconomic exponents ~1.15 lie outside its range **structurally**. Falsified without new data.

Its biological half remains *blocked* rather than falsified — the antecedent is untested and currently unsatisfiable.

P12's stated `would_kill` anticipated the wrong failure mode: it expected mismatched β for matched parameters, where the actual failure is β values the formula cannot produce at all.

---

## Corrected or retired

**Fabricated citation.** C1 attributed the ~10 kg breakpoint to "Xiao et al. (2015)." No such paper exists. It is Dodds, Rothman & Weitz 2001 — α = 0.668 ± 0.019 below 10 kg, 0.877 ± 0.088 above.

**Curvature downgraded** from established to contested. Griebeler & Werner 2016 (519 species): linear beat curvature in 16 of 17 orders. Hudson 2013: aquatic intercept shift. Plants curve concave. Invertebrate curvature vanishes under phylogenetic grouping. No replication in birds, reptiles, fish. MacKay 2011: only Rodentia survives a scale-invariant test. Packard: log-curvature from a non-zero arithmetic intercept. Quadratic adds 0.3% of variance. Full table in C1.

What *is* well supported is the weaker negative: **no universal exponent exists** (Glazier 2022; White & Marshall 2023; Clarke 2025). Price et al. 2012, co-authored by both Savage and Dodds, concedes WBE's derivation is incomplete and a fuller treatment gives a curve that is not a pure power law.

**Slope range corrected** to Kolokotrones' actual 0.57–0.87.

**Inverted d_f retired** — C1's implied column and X1's 2.7. Both produced by inverting β = d_f/(d_f+1); two values exceed the embedding dimension.

**P15's motivation is dead.** (1−λ)²·d_f was justified as a Landauer cost of maintaining synchronisation. Under the resolved definition λ is not a synchronisation and not something an organism maintains. Any surviving P15 needs a wholly different rationale.

---

## MMR is out of scope, on ontological grounds

Not because the formula cannot reach 0.87. Because MMR is a temporary **overclock** — unsustainable, costly, individual rather than species-characteristic, trainable, never a baseline.

| | BMR | MMR |
|---|---|---|
| Level | species-characteristic | individual |
| Duration | sustainable indefinitely | minutes |
| Cost | none beyond upkeep | recovery debt, oxidative stress |
| Trainable | no | substantially |

Generalises beyond metabolism: continuous vs peak power rating, base vs boost clock, yield vs ultimate strength, sustained vs burst bandwidth. Sustained capacity is limited by what can be held indefinitely; peak by instantaneous output plus tolerance for accumulating debt. No reason one formula covers both.

This argument is **unaffected** by the Kolokotrones findings and stands on its own grounds.

---

## Suggested order

1. **Run P14a.** No dependencies. Real result either way.
2. **Read Ballesteros 2018 and Zhao** to settle ②. Bounded — two papers.
3. **Q4** if the SLT thread is worth a separate project.

1 and 2 are independent.

---

## One thing worth a second pair of eyes

The derivation in §Resolved is elementary and was verified, but it was produced by Claude at the end of a long session and it conveniently rescues a formula that same session had spent hours dismantling. That combination warrants scepticism. It is recorded in H5 with the steps shown so it can be checked rather than taken on trust.

---

## Symbol warning

λ carries at least four unrelated meanings, **two in adjacent conjectures**: the process-contribution fraction (H3/H5/P13/P14/P15) and λ_RLCT, Watanabe's Real Log-Canonical Threshold (Q4/P16). Also λ_i for eigenvalues in the CCA work, and wavelength in QM4. See `gloss_lambda`.

The name "phase coherence" is now wrong under the resolved definition and should change — *process-contribution fraction* is honest.

---

## Superseded framing (kept for the record)

The earlier version of this document listed three blockers: an endpoint **decision**, a λ **definition** blocked on it, and Q4 as a **specification**. It leaned toward [2/3, 3/4] and put "decide the endpoints" second in the suggested order.

That framing treated the endpoints as something to choose. The two-process derivation shows they are something to *derive*, once the processes are identified. The blocker was never a decision — it was a missing mechanism, and the mechanism turned out to be addition.

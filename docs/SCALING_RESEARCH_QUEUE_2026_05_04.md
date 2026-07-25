# Scaling Research Queue — 2026-05-04

> **Purpose.** After a session that reframed H5, retired two derived quantities, and falsified P12's cross-domain claim, the scaling cluster needs an explicit statement of what is actually runnable and in what order. This is that statement.
>
> **Audit refs:** `gsw-scaling-corrections-2026-05-04`, `gsw-scaling-reformulation-2026-05-04`, `gsw-scaling-queue-2026-05-04`

---

## The one-line state

The β(λ) framework has a **documented endpoint failure** and its central cross-domain conjecture is **falsified**. One conjecture in the cluster is testable today with no upstream dependencies. Everything else is blocked, and the blockers are of three distinct kinds that should not be conflated.

---

## What is runnable now

### ① P14a — branching variance vs. exponent gap

> Does vascular branching-ratio variance correlate with the BMR/MMR metabolic exponent gap across taxa?

**The only item in the cluster with zero upstream dependencies.** No λ, no P13, no Q1, no resolution of the endpoint question.

| | |
|---|---|
| **Measure** | branching-ratio variance — micro-CT or corrosion casting |
| **Against** | published BMR/MMR exponent gaps, multiple taxa |
| **Method** | phylogenetically-corrected regression |
| **Confirms** | R² > 0.6 |
| **Kills** | no significant correlation after controlling for body mass |

Both criteria are inherited unchanged from P14 and both are already stated in the entry. Succeeds or fails independently of the mechanism claim.

---

## What is blocked, and by what kind of thing

The three blockers below are genuinely different and need different work. Treating them as one queue is what produced the earlier "promote P14 and P16" recommendation, which was too coarse.

### ② The endpoint question — *a decision, not a measurement*

β(λ) is a weighted average, so its output is confined between its two endpoints. With WBE's d_f = 3 the range is [0.750, 1.000], narrowing to [0.750, 0.875] under P13's floor. **Observed strict mammalian BMR is 0.676 — below the floor.**

Nothing downstream can be settled until the endpoints are chosen, because the endpoints determine what λ is a fraction *of*.

Candidates, none adopted:

| Endpoints | Contains BMR? | Reaches MMR 0.87? | Reaches urban 1.15? | Notes |
|---|---|---|---|---|
| [0.75, 1.00] | ✗ | ✓ | ✗ | current; requires rejecting d_f = 3 |
| [2/3, 3/4] | ✓ | ✗ | ✗ | maps onto the historical 2/3-vs-3/4 debate; gives curvature a natural reading |
| regime-dependent pairs | ✓ | ✓ | ✗ | two formulas wearing one name |
| abandon weighted-average form | — | — | — | most work, most freedom |

**Current lean:** [2/3, 3/4] for resting metabolism specifically. It contains the data and matches the real history. Its cost is silence on MMR and cities — which may be honest rather than fatal, if those are different questions.

### ③ λ's definition — *blocked on ②*

H3 defines λ by its effect on the exponent, which is circular, and the wiki uses it for two incompatible quantities (state variable in X1, structural variable in C1's table).

Most promising replacement, from this session: **λ as realisation fraction** — how much of the theoretically optimal network topology a real vasculature achieves. Anatomically measurable, and it changes *topology* rather than *efficiency*, which matters because efficiency moves the prefactor while only topology moves the exponent.

Candidates rejected on that test: capillary recruitment (wrong sign), impedance-matching degradation (prefactor, not exponent).

Cannot be finalised until ② is settled — "fraction of the optimum" requires knowing which optimum.

### ④ Q4 — *a specification step, not an experiment*

P16 (RLCT = d_f) would supply exactly the β-independent route to d_f the framework needs. It is blocked at step zero: an RLCT is a property of a *specified* statistical model, and no biological learning problem has been mapped to the SLT framework in a way yielding a computable RLCT.

**The queue item is Q4, not P16.** No measurement can help until metabolism is formulated with an explicit p(x|θ).

---

## Falsified

**P12** — cross-domain universality. β(λ) is bounded above by 1 for every d_f and every λ ∈ [0,1]; urban socioeconomic exponents ~1.15 lie outside its range **structurally**, not for want of measurement. Falsified without new data.

The biological half of P12 remains *blocked* rather than falsified — its antecedent ("whenever d_f and λ are independently measured") is untested and currently unsatisfiable.

Worth noting: P12's stated `would_kill` anticipated the wrong failure mode. It expected mismatched β for matched parameters; the actual failure is that β values exist which the formula cannot produce at all. A falsification criterion that misses how a claim actually fails is itself a finding.

---

## Retired as quantities

Both retained visibly per the no-deletions rule; withdrawn from use in inference.

- **C1's implied D_eff column** — produced by inverting β = d_f/(d_f+1) on observed exponents. Invalid outside its derivation range, applied to possibly-artifactual exponents, and yields values above the embedding dimension (reptiles 3.2, fish 7.3 — geometrically impossible).
- **X1's d_f ≈ 2.7** — same inversion. The predictions computed from it reproduce the exponent used to generate the input.

---

## The constructive direction

Recorded as its own calibration entry (`scaling_framework_root_diagnosis`).

**Predict individual organisms from measured anatomy, not cross-species exponents.**

> For a single animal, measured vascular network geometry predicts measured metabolic rate.

No exponent appears. This sidesteps the curvature problem entirely (no slope is fitted), sidesteps the 2/3-vs-3/4 debate, is falsifiable at n = 1, and yields the scaling result as a *consequence* rather than assuming it as input.

The WBE decomposition supports this:

**B = N_capillaries × (metabolic load per capillary)**

which splits one hard question into two separately measurable ones — an anatomical question (how does capillary count scale?) and a physiological one (is load per capillary constant?). It also localises the anomaly: if capillary count scales as M^0.676, the deviation is anatomical and WBE's geometric premises are what's wrong; if count scales as M^0.75 but load varies, the anatomy is fine and the deviation is physiological. The current framework cannot tell these apart because everything collapses into one exponent.

It also resolves BMR-vs-MMR without a structural parameter: same animal, same capillary count, different load per capillary.

---

## Suggested order

1. **Run P14a.** Only item with no dependencies. Real result either way.
2. **Decide the endpoints (②).** A decision you can make from the desk; unblocks λ.
3. **Define λ (③)** once ② is settled, then check it is measurable without touching β.
4. **Q4 (④)** if the SLT thread is worth pursuing — a separate, harder project.

Items 1 and 2 are independent and can proceed in parallel.

---

## Symbol warning

λ carries at least four unrelated meanings in this project, **two of them in adjacent conjectures**: phase coherence (H3/H5/P13/P14/P15) and λ_RLCT, Watanabe's Real Log-Canonical Threshold (Q4/P16). Also λ_i for eigenvalues in the CCA work, and λ for wavelength in QM4.

Unlike the *Fisher information*, *effective dimension*, and *η* collisions found in the same session's deep-research pass, this one is entirely internal — no external literature forced it. See the `gloss_lambda` disambiguation page.

# Prior-Art Gate — H5 two-process "derivation" and λ as fractional contribution

**Date:** 2026-10-18 · **audit_ref:** `gsw-consistency-pass-2026-10-18` · **Mode A** (no promotion)
**Entity:** H5 (Scaling Exponent β(λ)), *What The Math Says* → "DERIVATION FOUND" block, written 2026-07-25 under a "2026-05-04" session label
**Requested by:** the 2026-05-04 handover ("the derivation wants a second pair of eyes") and the 2026-10-18 consistency-pass brief

---

## 1. The claim, in plain language

> If an animal's metabolic rate is the sum of two processes that scale with body mass at different powers, then the slope of log(rate) against log(mass) at any mass is the average of the two powers, weighted by each process's share of the total.

The wiki's further claims: this makes β(λ) "not arbitrary", gives λ an operational definition (λ = the fractional contribution of one process), makes the endpoints "not a free choice", and supplies the mechanism whose absence an earlier diagnosis had complained of.

## 2. Triviality check (charter rule 2)

For B = a·M^p + b·M^q, d ln B / d ln M = p·f + q·(1−f), with f = a·M^p / B. This is one line of calculus: d ln Σᵢ Bᵢ / d ln M = Σᵢ (Bᵢ/B) · d ln Bᵢ / d ln M, true for any positive terms. In economics and metabolic control analysis it is the **elasticity of a sum** rule, El(f+g) = (f·El f + g·El g)/(f+g).

**Verdict: re-derivation, not a finding.** It is correct, and the wiki was right that the β(λ) shape follows from a two-term sum. It is a five-minute consequence of a known result, not a discovery.

## 3. Searches (four angles)

1. **The obvious lineage:** multi-process "allometric cascade" models — Darveau et al. 2002 and the published replies.
2. **Adjacent field:** ecophysiology / Dynamic Energy Budget two-term models (Ballesteros 2018, Kooijman/DEB, Maino et al. 2014, Glazier's metabolic-level boundaries).
3. **Textbook framing:** the elasticity-of-a-sum rule.
4. **Rival accounts of curvature:** Zhao 2015 (single network), Kolokotrones et al. 2010.

Literature reading was done by a background research agent with full-text access where available. **The load-bearing quotes for West et al., Ballesteros et al. and Zhao were re-verified first-hand in this session** against the full texts (West preprint PDF, PMC full text, arXiv PDF). Darveau et al.'s Eq. 2 and the Glazier reading rest on the agent's full-text reading.

## 4. Sources

| Source | Read | What it says | Relationship to H5 |
|---|---|---|---|
| **West, Savage, Gillooly, Enquist, Woodruff & Brown 2003**, *Nature* 421:713, doi:10.1038/421713a; preprint "Red herrings and rotten fish", arXiv:physics/0211058 | preprint full text (verified) | b = Σ cᵢbᵢ with cᵢ ≡ ∂ln B/∂ln Bᵢ; "This is the formula that DSAH should have used to determine b." For parallel contributions "cᵢ ≡ ∂ ln B/∂ ln Bᵢ = Bᵢ/B", "the correct, dimensionally homogeneous, version of Eq. (2)". The additive model is "only a consistency check of energy conservation, which must be trivially correct." | **reframing_of** — H5's identity is the two-process case of their correction; λ = Bᵢ/B is their cᵢ |
| Elasticity-of-a-sum rule (e.g. Sydsæter & Hammond, *Mathematics for Economic Analysis*) | via encyclopedia + course notes; textbook page not seen | El(f+g) = (f·El f + g·El g)/(f+g); log–log slope is the elasticity | **specialization_of** |
| **Darveau, Suarez, Andrews & Hochachka 2002**, *Nature* 417:166, doi:10.1038/417166a | full text (agent) | Eq. 2: MR = a Σ cᵢ M^bᵢ, with cᵢ fixed control coefficients summing to 1 | **contradicts** — H5's share-weighted form is what Darveau's fixed weights got wrong; West et al. show Eq. 2 gives b ≈ 0.76 (kg), 0.78 (g), 1.08 (pg) on the same data |
| **Ballesteros et al. 2018**, *Sci. Rep.* 8:1448, doi:10.1038/s41598-018-19853-6 | PMC full text (verified) | B = fkM + (1−f)k′M^{2/3}; f = "the fraction of the energy income that is used 'efficiently'"; f, k, k′ "independent of M"; credits DEB for the isometric + allometric sum | **generalization_of** (H5 = arbitrary p, q). **Caution:** their f is a mass-independent constant; H5's λ is fkM/B, which varies with M. Equating the two would repeat Darveau's error in reverse |
| **Zhao 2015**, arXiv:1509.08912 | full text (verified) | B = αM^x / log(M/β), x = 11/12 (fit 0.868); one Murray-law network gives both regimes; "the 2/3-rule does not originate from the classical surface law" | **adjacent_concept** — a rival single-network account; *not* a two-process decomposition. The wiki and scaling queue list it as a competing *pair of processes*; that framing is wrong |
| Glazier 2005 / 2010 (*Biol. Rev.*), 2014 (*Systems*) — metabolic-level boundaries | 2014 full text (agent) | exponent bounded between 2/3 and 1 by "shifts in the relative importance" of surface- and volume-related processes; qualitative, no share-weighted formula | **adjacent_concept** |
| Banavar, Damuth, Maritan & Rinaldo 2003, *Nature* 421:713, doi:10.1038/421713b | abstract only (paywalled) | cascade model "is flawed and is therefore meaningless" | not anchored (content beyond abstract unverified) |
| Darveau et al. 2003 reply, doi:10.1038/421714a; Maino et al. 2014 *J. Anim. Ecol.* 83:20; Kolokotrones et al. 2010 full text | not read | — | not anchored |

## 5. Drift-pattern check

- **`restatement-in-new-vocabulary`** — yes. The identity, and its use to give a process-share meaning to the weight, is West et al. 2003.
- **Escalation within one session** — the 2026-07-25 pass went from "interpolation without mechanism" to "derivation found, this reverses the diagnosis" in hours. The identity supplies a *meaning* for λ, not a *mechanism*; West et al. call the additive model trivially correct bookkeeping. The earlier diagnosis was closer to right than the reversal suggested.

## 6. What the identity does and does not buy

**Does:** gives λ a definition that mentions no exponent (a process's share of the total); makes λ mass-dependent by construction; shows a sum gives convex curvature (the observed sign) where a minimum rule gives concave; and is dimensionally consistent (λ = ½ at the crossover mass M* = (b/a)^{1/(p−q)}), unlike Darveau's Eq. 2.

**Does not:**
1. **Fix the endpoints.** p and q are inputs. "Identify the processes and the endpoints follow" is true, but the identity does none of the identifying.
2. **Make λ measurable from scaling data.** Only measuring the two fluxes separately does that, and only where they are genuinely separate and add in parallel. West et al.'s objection to Darveau — summing steps that act in series double-counts — applies to any pair proposed here.
3. **Supply a mechanism.** All explanatory content sits in which two processes, and why their exponents are p and q.

## 7. Verdict and recommendation

**RESTATEMENT of West et al. 2003** (itself the elasticity-of-a-sum rule applied to allometry). Ballesteros et al. 2018 is the special case p = 1, q = 2/3, with a constant f.

- **H5 stays Speculative.** The identity is correct and textbook; any particular choice of the two processes is Speculative. No new entity.
- **The scaling queue's open item ② needs reframing.** "Ballesteros vs Zhao" is not a contest between two decompositions: Zhao is a rival *single*-process account. The real question is whether metabolic rate decomposes into separate parallel fluxes at all, and if so which.

## 8. Recorded in the wiki (this pass)

- H5 *What The Math Says*: dated prior-art banner before the "DERIVATION FOUND" block; original text unchanged.
- Anchors on H5 (H5 previously had none — only an internal_construction flag, which is kept): `reframing_of` West et al. 2003; `specialization_of` elasticity-of-a-sum rule; `contradicts` Darveau et al. 2002; `generalization_of` Ballesteros et al. 2018; `adjacent_concept` Zhao 2015; `adjacent_concept` Glazier 2010.
- Calibration (append-only, labels unchanged): H5 (re-derivation recorded); `endpoint_decision_revised` (its "endpoints are now derivable, not chosen" overstates — p and q are inputs).
- `docs/SCALING_RESEARCH_QUEUE_2026_05_04.md` §Resolved: dated banner.

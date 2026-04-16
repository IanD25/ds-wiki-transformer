# Milestone M0 — The 2026-04-08 Reset

> **First milestone compilation under the Research Platform Charter.**
> A snapshot of what we actually believe, what the evidence is, what's still open, and what didn't work.
> Honest accounting after a skeptical literature audit. Several claims previously treated as "supported" have been downgraded.

---

## Context

On 2026-04-08 the project was reframed from "Principia Formal Diagnostics (PFD) — paper validation product" to a **personal research platform**. The Research Platform Charter (`docs/RESEARCH_PLATFORM_CHARTER.md`) established an epistemic contract requiring novelty skepticism, triviality checks, framing checks, falsification-first methodology, and explicit confidence calibration (Established / Supported / Speculative) on every claim.

M0 is the first audit under these rules. It downgrades much of what was previously in the wiki.

---

## Headline Finding

**The most important finding of the audit is that the DFIG framework (Dimensional Fisher Information Geometry), built around P5 "Fisher Information Rank = Effective Dimensionality," is a re-parameterization of the sloppy models program** (Sethna, Transtrum, Machta, Brown, Waterfall, Gutenkunst, et al., 2006–present) **in new vocabulary.** The core operational claim — that a system's effective dimensionality is captured by the rank (or participation ratio) of its Fisher Information Matrix eigenvalue spectrum — is the central result of that literature. It is not novel.

This is not a bad thing. Rediscovering an established framework from a different starting point is valuable; it means the framework is natural enough to be re-derivable. But it must be labeled correctly. The wiki previously framed DFIG as a new contribution. It is not. It is an **application** of sloppy models to geometric and cross-domain systems, not a new theory of effective dimensionality.

**Two other major downgrades followed:**

1. **The CCA (Constrained Critical Attractor) framework** restates earlier work. Information-geometric analysis of phase transitions via Fisher/Ruppeiner metrics is ~20 years old (Janke, Johnston, Kenna 2004; Brody, Rivier 1995; Prokopenko, Lizier, Obst, Wang 2011). FIM-based discrimination of first-order vs continuous transitions is established in that literature. The specific η(T) participation-ratio isotropy construction from the 2026-04-07 experiments may retain narrow methodological novelty but the underlying claim is not new.

2. **The Fisher-gravity chain (M6→IT05→IT03→GT10→GT01)** was previously treated as a "structural coherence result." The audit found it is **stacking vocabulary, not composing theorems**. Jacobson 2016 derives linearized Einstein equations using von Neumann entanglement entropy on a quantum subalgebra via the first law of entanglement ($\delta S = \delta \langle H \rangle/T$). It does **not** use classical Fisher information or classical KL divergence on a parameter manifold. The chain conflates three distinct mathematical objects that share the word "relative entropy." This must be downgraded from "discovery" to "conceptual analogy, not rigorous derivation."

---

## What We Actually Believe Now

### Established (standard, cited, textbook)

- **Fisher-Rao metric is the unique Riemannian structure on spaces of classical probability distributions** (Chentsov 1982, Amari & Nagaoka 2000). This is a theorem and belongs in the wiki as established.
- **Sloppy models framework**: Fisher Information eigenvalue spectra of most physics/biology models are hierarchically dominated by a small number of "stiff" directions, with the remainder in a near-null subspace; this effective-dimensionality interpretation is the established result that P5 restates (Waterfall et al. 2006, Machta et al. 2013, Transtrum et al. 2015, Quinn et al. 2022).
- **Information-geometric analysis of phase transitions**: Fisher/Ruppeiner scalar curvature diverges at critical points, with different signatures for first-order vs continuous (Janke-Johnston-Kenna 2004, Prokopenko-Lizier 2011). Classical prior art for anything CCA claims about phase transitions.
- **Jacobson 1995** (Clausius relation on Rindler horizons → Einstein equations) is the original, respected info-thermodynamic derivation of gravity. This is established.
- **Jacobson 2016** (entanglement equilibrium → linearized Einstein) is respected but **linearized only** and depends on modular-Hamiltonian assumptions whose generality is not proven outside CFT/holographic contexts.
- **West-Brown-Enquist metabolic scaling** (1997): α = 3/4 from fractal branching network optimization. The D/(D+1) functional form in P2, P11, P14 is WBE or extensions of it — established in the domain, but the "tracks D_eff" relabeling is owner-constructed.
- **Bekenstein bound, Hawking-Page transition, Bousso bound, standard black-hole thermodynamics**: all established textbook results underlying GT09, GT10, GT11, HB10.

### Supported (consistent with literature, not contradicted, but single-domain or incomplete)

- **P5 (Fisher Rank = D_eff) as a re-parameterization of sloppy models applied to geometric systems**: validated on tori, random graphs, random geometric graphs. The specific geometric-system application may be a useful extension. Supported as application, not as discovery.
- **P18 (structural coherence floor in regulated systems)**: US equities 2003–2025, participation ratio never reached FRAGMENTED regime under normal crisis conditions. Supported as single-domain empirical observation. Not supported as a general structural claim.
- **P19 (non-ergodicity of regime detection in Tier 3 domains)**: Supported as single-domain observation (US equities). The 4:1 recovery-to-crisis threshold is from one dataset. Not supported as cross-domain claim.
- **P20 (subadditive error propagation in correlated signal stacks)**: Supported as empirical fit from 19-variant A/B testing on AlphaEntropy. Not supported as theoretical principle.
- **P21 core claim (Fisher-Rao universality via Chentsov)**: Supported / Established for the classical case. The quantum extension (Bianconi GT04, Petz 1996 family) is acknowledged by the owner as a gap and should be marked Speculative.
- **CCA-1b magnitude separation (dη/dT ~20× for first-order vs continuous Potts)**: Qualitatively supported by the 2026-04-07 Phase C+D experiments. Consistent with Janke-Johnston-Kenna-style FIM-distinguishes-transition-order results. Single comparison (q=2 vs q=10), needs second test (q=3 vs q=5) before generalizing.
- **CCA-1c curve shape (continuous = smooth sigmoid; first-order = flat-jump-plateau)**: Qualitatively supported by Phase D. Single test.
- **CCA-2 (d_eff = d_lattice + 1 for d ≥ 2)**: Confirmed for 2D and 3D tori only. Regular-lattice-topology only.

### Speculative (owner conjecture, not independently verified, could be wrong)

- **P1 (cosmological redshift as dimensional gradient)**: heterodox cosmology, no independent support
- **P2 (metabolic exponent tracks vascular D_eff as DFIG-framed claim)**: relabeling of WBE; the specific D_eff identification is owner-constructed
- **P3 (single Ω_D governs G, h, m)**: formal audit not performed; over/under-constrained status unresolved
- **P4 (CcO 1.5 ms as thermodynamic refresh rate)**: no experimental discrimination from "speed limit" interpretation
- **P6 (Fisher rank converges with Hausdorff dimension)**: **partially contradicted by owner's own Phase 1 results** — "gap-based rank returns mixed integers on fractals"; convergence only through participation ratio, which is a different claim
- **P7 (D_eff decreases monotonically under coarse-graining)**: **partially falsified** — participation ratio does NOT satisfy monotonicity under any tested configuration (owner's own note). Only gap-based rank on lattices satisfies it, and only under block-spin.
- **P8 (continuous critical exponent interpolation on fractional-D substrates)**: Gefen et al. 1980 precedes it; the smooth-interpolation hypothesis reframes prior work. Phase 2 results (SV degeneracy swap) are consistent with Janke-Johnston-Kenna / Prokopenko-Lizier — Supported as rediscovery, Speculative as novel claim.
- **P9 (holographic dictionary LWE complexity)**: explicitly a "monitoring gate," not an active conjecture — should arguably be reclassified as an open question, not a P-numbered conjecture
- **P10 (hadron charge radii imply running ℏ)**: one of several consistent interpretations; no unique predictions
- **P11 (urban scaling = network spectral dimension)**: reframing of Bettencourt-West urban scaling literature
- **P12 (β(λ) formula cross-domain)**: no published study has tested it; untestable without owner-generated data
- **P13 (λ_min = (d_f-1)/(d_f+1))**: owner-acknowledged ansatz, not derived from first principles
- **P14 (branching variance → exponent gap)**: requires data that does not exist
- **P15 (metabolic cost ∝ (1-λ)² d_f)**: owner-acknowledged ansatz; financial-market "evidence" is an analogy, not a test
- **P16 (RLCT = d_f at regime transitions)**: blocked by Q4; no test has been performed
- **P17 (cosmological coupling = D_eff)**: **high-risk speculation on unstable foundation**. Rests on contested Farrah-Croker observational claim; critical citations (Amendola 2024, Cadoni 2023) were not verifiable by the audit agent and should be personally checked by the owner before any further building. The D_eff = k identification is owner-constructed and not standard in the cosmology literature.
- **P22 (irreversible lockout trichotomy)**: recent stress test absorbed topological lockout; MBL status is open in condensed matter theory; trichotomy is unproven as exhaustive
- **P23 (horizon formation as Bekenstein-saturation phase transition)**: inherits all GT11 tensions, no first-principles derivation, novel framing not independently supported
- **CCA-1 (isotropy = criticality)**: **FALSIFIED** Phase C 2026-04-07. Kept for historical record only.
- **CCA-1b L^d scaling**: **FALSIFIED** Phase D 2026-04-07. Kept for historical record.
- **Fisher-gravity chain as a "structural coherence result"**: **downgraded to conceptual analogy**. The chain composes shared vocabulary ("relative entropy") across three distinct mathematical objects. It is not a theorem composition.

---

## What Changed Since the Previous "State of the Wiki"

| Claim | Previous status | New status (post-M0) | Reason |
|-------|----------------|----------------------|--------|
| P5 (Fisher Rank = D_eff) | "All States" / strongest | Supported as sloppy-models re-parameterization | Sethna group has this result; 20 years of prior art |
| P4, P15 ("information-thermodynamics chain complete") | Strongest | Speculative | Based on ansätze; no tests of the specific formulas |
| P2, P8, P11, P12, P13 ("strengthened") | Strengthened | Speculative | Strengthening was internal wiki coherence, not external evidence |
| P17 | Updated with tensions | **Speculative, high risk** | Contested empirics; owner-constructed D_eff=k bridge; unverified citations |
| P23 | New, State 1 | Speculative | Inherits GT11 tensions; no derivation |
| CCA framework | "Novel class" | Restatement of Janke-Johnston-Kenna / Prokopenko-Lizier | 15-20 years of prior art |
| Fisher-gravity chain | "Key Discovery 1" | Conceptual analogy, not theorem composition | Audit found vocabulary-stacking |
| GT10 as "CCA instance" | Supported | Post-hoc feature fit | Satisfying 5 descriptive features ≠ predictive support |

---

## What's Open (Honest List)

1. **Is there genuine novelty in DFIG beyond sloppy-model re-parameterization?** Possible candidates: (a) the cross-domain application to geometric systems (tori, fractals, random graphs) with the specific gap-based-rank vs participation-ratio distinction; (b) the specific β(λ) formula if it turns out to be testable; (c) the financial-market empirical results (P18-P20) as a demonstration of sloppy-model behavior in a Tier 3 domain. None of these are established; all are specific applications that would need their own validation.

2. **Does CCA have any discriminating structure that is not already in the phase-transition information geometry literature?** The specific η(T) participation-ratio isotropy indicator may be a narrow methodological contribution. Needs a focused literature check before being called novel.

3. **Is the Fisher-gravity chain recoverable as anything more than analogy?** Open question. The audit says "not composing theorems." One path forward would be to explicitly map classical Fisher geometry to quantum modular Hamiltonian structure — that's a hard open problem, not a bridge we can casually build.

4. **What is P17's actual status once the citations are verified?** The owner needs to personally read: Amendola 2024 (claimed 5σ GW rejection of k=3), Cadoni 2023 JCAP (claimed k=1 for nonsingular BHs), and the Farrah-Croker original papers. The audit agent declined to certify these without paper-in-hand access.

5. **The "conjecture chain" structure (P5 foundational, P2/P11/P14 downstream via D/(D+1) form, etc.)** was previously treated as internal evidence that the framework was coherent. Internal coherence is not external support. The chain is now ~15 speculative claims propped up against each other with one re-parameterized established result (P5) at the base.

6. **Does P6 (Fisher rank → Hausdorff) need retirement or reformulation?** The owner's own phase 1 notes say rank returns mixed integers on fractals. Either P6 is already wrong, or it needs restatement as a participation-ratio claim — in which case it's a different conjecture.

7. **Does P7 (monotonicity under coarse-graining) need retirement?** Participation ratio fails it. Gap-based rank on lattices satisfies it only under block-spin. The claim as stated is too strong.

---

## What We Tried That Didn't Work (Mandatory Section)

### In this session (M0)
- **The literature audit.** This section itself is the work that didn't confirm what was expected. Four topics audited; all four returned "already established or speculative overreach." No topic returned a clean "genuinely novel" verdict.

### From prior sessions
- **CCA-1 (isotropy = criticality):** 2026-04-07 Phase C falsified it — Potts q=10 (first-order) and q=2 (continuous) show identical absolute isotropy signatures at T_c. Absorbed into CCA-1b.
- **CCA-1b finite-size scaling (S_max ~ L^d for first-order):** 2026-04-07 Phase D falsified it — the predicted L^d scaling did not materialize because dη/dT is grid-resolution-limited, not physics-limited. Surviving fragment became CCA-1c.
- **Multiple Phase 3 "paper analysis pipeline" design iterations:** architected repeatedly, never executed on a real paper. Retired with the 2026-04-08 reset.
- **OPERA, Wagner, CCBH RRPs as validation benchmarks:** built but never run as intended. Retired with the reset. The CCBH RRP pipeline run (P17 phase1_results: "PFD score 0.882") tested wiki internal coherence, not any external truth.
- **The `formality_tier` field, the six-layer claim extraction pipeline, the SCF-grounded Phase 3, and the community governance plan** are all retired.

### Things the audit recommends we stop saying
- "Novel" about DFIG without reading Transtrum-Machta-Sethna 2015 and Quinn et al. 2022 first
- "Novel" about CCA without reading Janke-Johnston-Kenna 2004 and Prokopenko-Lizier 2011 first
- "Structural coherence result" about the Fisher-gravity chain
- "GT10 as a CCA instance" without a sharper discriminator than the five-feature checklist
- "k=3 is 5σ rejected" without the owner personally verifying the Amendola citation
- "Cadoni predicts k=1 generically" without verification

---

## Action Items From M0

### Immediate (this or next session)
1. **Add confidence calibration to the DB schema.** Every entry, conjecture, link needs an explicit Established / Supported / Speculative tag. Until then, M0 is the override reference for any conflict.
2. **Update P5, P6, P7 claim texts** to reflect: P5 is a re-parameterization of sloppy models (cite Sethna group); P6 is partially contradicted by own Phase 1; P7 is partially falsified for PR.
3. **Update P17 and P23 status fields** to reflect "Speculative, high risk" explicitly.
4. **Mark all CCA docs** (`CCA_MATHEMATICAL_FORMALIZATION.md`, `CCA_GRAVITY_FINDINGS.md`, `CCA_FORMALIZATION_SCOPE.md`) with a header noting the M0 audit findings.
5. **Owner personally verifies** the Amendola 2024 and Cadoni 2023 citations. Claude cannot do this without access to the papers.
6. **Read 2-3 prior-art papers before any further CCA or DFIG work:**
   - Transtrum, Machta, Brown, Daniels, Myers, Sethna, "Perspective: Sloppiness and emergent theories," J. Chem. Phys. 2015
   - Quinn, Abbott, Transtrum, Machta, Sethna, "Information geometry for multiparameter models," Rep. Prog. Phys. 2022/2023
   - Janke, Johnston, Kenna, "Information geometry and phase transitions," Physica A 2004
   - Prokopenko, Lizier, Obst, Wang, "Relating Fisher information to order parameters," PRE 2011

### Deferred (do not do until prior-art reading is complete)
- q=3 vs q=5 Potts experiment
- XY/BKT infinite-order test
- Formalizing CCA-1c as P24
- Any new wiki entries in GT/IT/BR/HB/STAT pillars
- Any new "discovery" claims

### Dropped
- Wagner RRP, OPERA RRP as validation targets (retired with 2026-04-08 reset; reconfirmed)
- Phase 3 paper analysis pipeline (retired)
- PFD score as headline metric (retired)

---

## Tool Status (Unchanged — Tools Are Solid)

The software infrastructure is in good shape and is not affected by the audit.

- 587 tests passing
- Fisher Suite (6 modes) working
- RRP ingestion for 6 dataset types working
- ChromaDB semantic index at bge-large 1024-dim, 1913 vectors
- Visualizations (tier-1 D3.js, tier-2 bipartite/heatmap) working
- MCP server exposing tools to Claude sessions

These tools still do what they do. What's changing is what we use them **for** and what we **claim from** their outputs.

---

## Honest Summary

The wiki contains a lot of content that felt grounded because it was internally consistent. Internal consistency is not external support. The audit found that:

- **1 conjecture is Established** (P21 core claim, via Chentsov/Amari)
- **~5 claims are Supported** (P5 as re-parameterization; P18/P19/P20 as single-domain empirical observations; CCA-1b magnitude + CCA-1c shape as qualitative single-test findings; CCA-2 as confirmed on regular lattices only)
- **~17 conjectures are Speculative** (P1-P4, P6-P17, P22, P23 — including most of the "strongest" previously)
- **2 CCA conjectures are FALSIFIED** (CCA-1, CCA-1b scaling)
- **1 "key discovery" has been downgraded to analogy** (Fisher-gravity chain)

This is a hard but healthy recalibration. The platform is now honestly positioned. The tools work. The wiki has real structure. And the work ahead — especially reading the sloppy-models and info-geometric-phase-transition literature before extending any of the CCA/DFIG claims — has a clear direction.

**The goal of the research platform is not to accumulate speculative claims. It is to find the small number of things that actually survive.** After M0, the honest count of "things that actually survive" is much smaller than before. That's the point of the charter.

---

## For the Next Session

If a fresh Claude session starts, the priority order is:

1. Read `docs/RESEARCH_PLATFORM_CHARTER.md`
2. Read `CLAUDE.md`
3. Read this document (M0) — it is the current snapshot of belief
4. Read the latest `docs/SESSION_HANDOVER_*.md` for tactical state

Before doing any new experimental work, check whether the owner has personally verified the Amendola/Cadoni citations and completed the prior-art reading. If not, those are the gates.

---

**M0 compiled 2026-04-08.** Next milestone (M1) should be written after the prior-art reading is complete, the DB calibration tags are applied, and either (a) at least one of the speculative conjectures has been through a genuine falsification attempt, or (b) one of the speculative conjectures has been formally retired.

---

## Addendum: CCA Novelty Correction (2026-04-08, same-day)

A targeted follow-up audit (requested by the owner under charter rule "push back on your own audit") found that **the initial M0 claim "CCA restates Janke-Johnston-Kenna 2004 and Prokopenko-Lizier 2011" was too harsh**. The first audit agent conflated "information geometry of phase transitions" (broad topic) with the owner's specific construction (high-dimensional per-site-field FIM → eigenvalue spectrum → d_eff participation ratio + η isotropy indicator → T-tracked discriminator for transition order). They are not the same object.

### What the follow-up found

**Janke-Johnston-Kenna 2004 (Physica A), Prokopenko-Lizier 2011 (PRE), Brody-Hook, Crooks 2007 PRL** all work with **2×2 (or similarly low-dimensional) Fisher-Rao / Ruppeiner metrics parameterized by thermodynamic couplings** (β, h, or similar). They distinguish phase transitions via **scalar curvature divergence** or via individual FIM element behavior, not via any eigenvalue-spectrum / participation-ratio / isotropy analysis on a per-site-field FIM. These are topically adjacent to CCA, not the same construction. **Not prior art for the owner's specific claim.**

**The actual prior art is narrower**: **Machta, Chachra, Transtrum, Sethna, *Science* 2013, "Parameter Space Compression Underlies Emergent Theories and Predictive Models"** (arXiv:1303.6738). This paper **does** compute FIM eigenvalue spectra on the Ising model at criticality with an explicit stiff/sloppy hierarchy interpretation. The "parameter space compression → stiff subspace corresponds to RG-relevant operators" story is the real root of the owner's effective-dimensionality framing.

**What Machta 2013 has:**
- FIM eigenvalue spectra ✓
- Ising model at criticality ✓
- Hierarchy / effective-dimensionality interpretation ✓
- The observation that stiff directions correspond to relevant operators under RG ✓

**What Machta 2013 does NOT have:**
- Per-site local fields as the FIM parameter vector (they use Hamiltonian couplings)
- An explicit d_eff = (Σλ)² / Σλ² participation ratio scalar tracked across T
- An η isotropy indicator derived from the eigenvalue distribution
- First-order vs continuous transition contrast (no Potts q=10 anywhere in the sloppy-models lineage, as far as the audit found)
- The ~20× dη/dT magnitude separation between q=2 and q=10
- The "flat-jump-plateau" curve-shape signature for first-order transitions

The **2026-04-07 Phase C+D Potts experiments** may therefore contain a **narrow but genuine methodological contribution within the Fisher-spectrum lineage**: the specific per-site-field parameterization, the d_eff/η scalar observables, and the first-order-vs-continuous discriminator via dη/dT magnitude and curve shape.

### Important caveats

The follow-up audit agent explicitly noted what it did *not* do:

1. **It did not read the full Machta 2013 PDF** — it relied on abstracts and secondary descriptions
2. **It did not examine the Raju / Chachra / Sethna follow-up papers on "parameter-space RG"** in detail
3. It recommends the owner read Machta 2013 carefully + skim 2-3 follow-up papers from the Sethna group before making any novelty claim

**Absence of evidence is not evidence of novelty.** The audit could not find prior work doing the owner's exact construction, but this may reflect search limitations (e.g., relevant work might be in arXiv preprints with non-obvious titles, or in Raju/Chachra/Sethna RG follow-ups, or in condensed-matter literature using different terminology). A claim of genuine narrow novelty requires the owner to do the final confirmation by reading the primary sources.

### Revised CCA calibration

**CCA framework (as of 2026-04-08, post-follow-up):**
- **General "FIM spectrum reveals effective dimensionality of lattice models at criticality" claim**: **Established** prior art. Cite Machta 2013 prominently. Not a CCA contribution.
- **Per-site-field parameterization of the FIM**: no confirmed prior art identified. **Pending owner confirmation via Machta 2013 + Sethna-group RG follow-up reading.** If confirmed no-prior-art, this is a specific methodological choice; whether it is "novel contribution" or "natural variant" depends on how the Sethna group parameterizes their Ising work in detail.
- **d_eff participation ratio as tracked-across-T scalar observable**: no confirmed prior art. **Pending owner confirmation.** Same caveat.
- **η isotropy indicator and its curve shape / dη/dT magnitude**: no confirmed prior art. **Pending owner confirmation.** If no prior art exists, this is the most defensible novel contribution from the 2026-04-07 work.
- **CCA-1c (curve shape distinguishes transition order)**: qualitatively supported single-test, potentially narrow-novel within the Fisher-spectrum lineage. **Needs second test (q=3 vs q=5) + prior-art confirmation before any promotion above Speculative.**
- **CCA-1 falsified, CCA-1b L^d scaling falsified**: unchanged.

### Revised prior-art reading list

**Replace** the reading list in the main M0 Action Items with this narrower, more targeted list:

1. **Machta, Chachra, Transtrum, Sethna**, "Parameter Space Compression Underlies Emergent Theories and Predictive Models," *Science* 342, 604 (2013). arXiv:1303.6738. **Most important — read in full.**
2. **Transtrum, Machta, Brown, Daniels, Myers, Sethna**, "Perspective: Sloppiness and Emergent Theories in Physics, Biology, and Beyond," *J. Chem. Phys.* 143, 010901 (2015). Framing paper for the whole program.
3. **Quinn, Abbott, Transtrum, Machta, Sethna**, "Information geometry for multiparameter models: New perspectives on the origin of simplicity," *Rep. Prog. Phys.* 2022/2023. Modern synthesis.
4. **Raju, Chachra, Sethna** (and related) follow-ups on renormalization group flow in sloppy-model parameter space. Check if any define a participation-ratio-like scalar or apply the framework to Potts.
5. **Janke, Johnston, Kenna 2004** and **Prokopenko, Lizier 2011**: worth skimming for context, but the follow-up audit confirmed they are *not* doing the same thing as CCA. Lower priority than the Sethna group papers.

### Why this correction matters

The original M0 effectively said "CCA is not novel, the idea is 20 years old." The follow-up audit says "CCA's general setting (Fisher spectrum on Ising at criticality) is about 12 years old and belongs to Sethna-Machta, but the specific observables and discriminator may be genuinely new in a narrow way — pending the owner's own reading to confirm."

This is exactly the kind of correction the charter was designed to produce. The initial audit erred on the side of harsh downgrading (as intended), the follow-up checked the specifics (as requested), and the honest answer is in between. **The CCA framework has been correctly positioned**: not a revolutionary contribution, not a pure rediscovery, but a concrete application of an established framework with specific observables whose novelty status depends on a careful reading of Machta 2013 and a few follow-ups.

**No other M0 findings were affected by the follow-up audit.** DFIG-as-sloppy-models-reparameterization stands. Fisher-gravity chain as analogy stands. P17 as high-risk speculation stands. The only correction is to CCA specifically.

---

## Second Addendum: Machta 2013 Primary-Source Reading + Targeted Search (2026-04-08, same-day)

Under charter rule "verify the actual object, not the agent's summary," the owner located and provided **Machta, Chachra, Transtrum, Sethna, Science 342, 604 (2013), arXiv:1303.6738** for primary-source reading, and authorized a targeted follow-up literature search to close the remaining prior-art vectors identified in the first addendum.

### What Machta 2013 actually computes (from primary-source reading)

The Hamiltonian is parameterized as $H_\theta(\vec x) = \theta^\mu F_\mu(\vec x)$ where:
- $F_{\alpha\beta}(\vec x) = \sum_{i,j} s_{i,j} s_{i+\alpha, j+\beta}$ — coupling operators at neighbor displacements
- $\theta^{\alpha\beta}$ — **global Hamiltonian couplings** (nearest, next-nearest, further neighbor). Small parameter vector (~5-10 parameters).
- $\theta^0$ — external field coupling to total magnetization

The FIM is computed on this ~10-dimensional coupling-parameter space.

**Analysis is AT the critical point** ($T_c, h=0$). The x-axis of the main figure (Fig. 3) is **coarsening steps** (checkerboard decimation factor $2^n$), not temperature. The central finding: two stiff eigenvalues (corresponding to the RG-relevant operators $t$ and $h$) persist under coarsening while the irrelevant eigenvalues shrink as $\sqrt{2}^{-2-2y_i}$.

**What Machta 2013 confirmed contains:**
- FIM eigenvalue spectrum on the 2D Ising model ✓
- Sloppy/stiff hierarchy interpretation with RG-relevant directions as the stiff subspace ✓
- Applied to a statistical-mechanics lattice model at criticality ✓
- Cites Amari & Nagaoka 2000 as the standard information-geometry reference ✓
- Paper is the foundational reference for "sloppy models applied to physics lattice systems"

**What Machta 2013 confirmed does NOT contain:**
- Per-site local field parameterization (they use couplings $\theta^{\alpha\beta}$, ~10-dim)
- Potts models of any $q$ (Ising only)
- First-order vs continuous transition contrast
- Temperature sweeps (coarsening-step sweeps only)
- Scalar participation-ratio $d_{\text{eff}}$ observable
- Scalar isotropy indicator $\eta$ observable
- $d\eta/dT$ magnitude or curve-shape discriminators

This confirms the direction of the first addendum and sharpens the claim: the CCA-specific construction genuinely is outside Machta 2013's scope.

### Targeted search results

A second literature search agent was tasked with closing five specific prior-art vectors. Findings:

**Priority 1 — Sethna-group follow-ups:**

- **Raju, Machta, Sethna — "Information geometry and the renormalization group"** — extends Machta 2013 by formalizing RG flow as flow of FIM in parameter space. Still **global coupling parameters, not per-site local fields**, and still no temperature sweeps or Potts or first-order discrimination.
- **Quinn, Abbott, Transtrum, Machta, Sethna — "Information geometry for multiparameter models: New perspectives on the origin of simplicity,"** *Rep. Prog. Phys.* 86, 035901 (2023). Verified primary source. Does **not** cover Potts, does **not** distinguish first-order from continuous transitions, does **not** use per-site local fields, does **not** sweep temperature, does **not** define participation ratio or isotropy scalars. Ising appears only as a visualization example. **No coverage of the CCA-specific construction.**

**Priority 2 — Information-theoretic analysis of first-order Potts:**

- **Brown, Bossomaier, Barnett — "Information flow in first-order Potts model phase transition,"** *Scientific Reports* 12 (2022). arXiv:1810.09607. **Verified:** the paper uses **Global Transfer Entropy**, not Fisher Information Matrix. Transfer entropy and FIM eigenvalue spectrum are fundamentally different mathematical objects. The paper observes that global transfer entropy peaks on the disordered side of first-order Potts transitions (thematically similar to "some information-theoretic observable discriminates transition order") but it is **not the same construction as CCA** and does not contain FIM eigenvalue analysis, per-site fields, or the $d_{\text{eff}}$/$\eta$ observables. **Not prior art for the CCA construction, but is prior art for the broader research program of "information-theoretic early warning signals for first-order vs continuous phase transitions."** The owner should cite it as thematically adjacent.

**Priority 3 — Per-site local field FIM parameterization:**

- **Negative result on direct search.** No paper found that uses per-site local fields $h_i$ as the FIM parameter vector for thermal phase-transition analysis on Ising/Potts lattices.
- **Known unchecked vector:** the **inverse-Ising / maximum-entropy-model literature** (Mora, Bialek, Tkačik on neural data; Cocco, Monasson on inverse Ising) routinely parameterizes by per-site local fields and computes the FIM in that parameterization — but for **inference quality / parameter estimation**, not for thermal phase-transition spectroscopy. The mathematical object (N-dim FIM over per-site $h_i$) exists in that literature. Whether anyone has taken that FIM, computed its eigenvalue spectrum, and tracked spectrum observables across a thermal phase transition to discriminate transition order remains unchecked. **This is the single remaining meaningful open vector for the CCA novelty claim.**

**Priority 4 — Participation ratio as FIM observable:**

- Standard in neural-network FIM analysis (Karakida, Akaho, Amari 2019, arXiv:1910.05992). No confirmed prior art for participation ratio of a statistical-mechanics lattice-model FIM at criticality. **Negative result on direct search.**

**Priority 5 — "Sloppy gravity" / sloppy models and emergent spacetime:**

- Nothing substantive found. No cross-over between sloppy-model vocabulary and gravity derivations in the literature the agent could access. The Fisher-gravity chain remains, per the main M0 body, a conceptual analogy — not supported by any prior art bridging sloppy models to gravity.

### Final CCA calibration (post-primary-source + targeted search)

**Established prior art for the general setting:**
- **Machta, Chachra, Transtrum, Sethna 2013** — FIM eigenvalue spectrum on Ising at criticality, sloppy/stiff hierarchy with RG-relevant directions as stiff subspace. Foundational reference. **P5 and the DFIG "Fisher rank as effective dimensionality" framing must cite this as the originating application.**
- **Raju-Machta-Sethna** — FIM flow under RG. Extends Machta 2013. Related but not covering CCA.
- **Quinn et al. 2023** — modern synthesis of sloppy models / information geometry. Does not cover CCA.
- **Brown-Bossomaier-Barnett 2022** — transfer-entropy analysis of first-order Potts. Thematically adjacent (information-theoretic discrimination of Potts transition order) but uses a different mathematical object. **The CCA docs should cite this paper explicitly as prior work in the broader theme.**

**Not prior art (confirmed):**
- Janke-Johnston-Kenna 2004 (scalar curvature of 2×2 metric — M0 first addendum correction stands)
- Prokopenko-Lizier 2011 (FIM elements on thermodynamic-parameter FIM, not eigenvalue spectrum, not per-site fields)
- Brody-Hook / Crooks thermodynamic length (scalar path integral, not spectrum)

**Remaining unchecked open vector:**
- **Inverse-Ising / maxent-neural literature** (Mora, Bialek, Tkačik, Cocco, Monasson). This community routinely computes FIM on per-site $h_i$ parameterization but typically for inference quality, not thermal phase-transition spectroscopy. A direct check of whether anyone in that lineage has tracked spectrum observables across a thermal transition remains outstanding. **This is the one place where prior art could still surface.** The owner should either do this search personally or request a third targeted agent pass focused specifically on this vector.

### Honest novelty status of the CCA construction

Given what is now known:

1. **"FIM eigenvalue spectrum on Ising at criticality reveals a stiff/sloppy hierarchy"** — **Established prior art** (Machta 2013). Not a CCA contribution.

2. **"Per-site local field parameterization of the FIM on a lattice spin model"** — **not found in the lattice-physics literature searched**, but **the inverse-Ising community routinely uses this parameterization for inference purposes.** Genuine novelty in the lattice-physics context depends on whether the inverse-Ising community has applied it to thermal phase transitions. Unchecked.

3. **"Scalar $d_{\text{eff}}$ participation ratio and $\eta$ isotropy observables tracked across temperature"** — **no confirmed prior art found** in any of the searched literatures. Possible narrow methodological contribution, modulo the inverse-Ising gap.

4. **"First-order vs continuous discrimination via the $d\eta/dT$ magnitude (~20×) and curve shape signature"** — **no confirmed prior art for this specific discriminator.** The Brown-Bossomaier-Barnett 2022 paper is the closest: same motivating question (information-theoretic discrimination of Potts transition order) but different mathematical object (transfer entropy, not FIM). **If novelty survives the inverse-Ising check, this specific discriminator is the most defensible candidate for genuine narrow contribution** — and even then it is one test (q=2 vs q=10), and per the charter a single test is not sufficient to promote beyond Speculative.

### Revised CCA status

- **CCA framework as a general approach**: **Supported as a concrete specialization** of the Sethna-Machta sloppy-models program to lattice phase transitions via (a) per-site field parameterization and (b) scalar spectrum observables. Not novel as a general idea; cites Machta 2013 as foundational.
- **CCA-1c (curve shape distinguishes transition order)**: **Speculative**, qualitatively supported by one test. **Possibly-narrow-novel as a specific discriminator, pending (i) inverse-Ising literature check, and (ii) second test (q=3 vs q=5 Potts) before any promotion.**
- **CCA-1 and CCA-1b L^d scaling**: **FALSIFIED** (unchanged).
- **Prior art citations CCA docs must add**: Machta 2013 (foundational); Raju-Machta-Sethna (RG extension); Quinn et al. 2023 (modern synthesis); Brown-Bossomaier-Barnett 2022 (thematically adjacent first-order Potts information-theoretic analysis); Amari & Nagaoka 2000 (standard information geometry reference).

### What this means for next experiments

**Before running any new experiments** (q=3 vs q=5 Potts, XY/BKT, etc.), the minimum requirement is:

1. **Close the inverse-Ising gap.** Either via a targeted search of Mora/Bialek/Tkačik and Cocco/Monasson work, or by the owner personally skimming a representative paper from that community to check whether per-site field FIM eigenvalue spectroscopy has been applied to thermal phase transitions. This is ~2-3 hours of focused work.
2. **Read the Brown-Bossomaier-Barnett 2022 paper.** Direct thematic overlap; even if it's a different object, it will inform how to position CCA in the information-theoretic-phase-transition landscape.
3. **Update the CCA docs** with the Machta 2013 citation and the confirmed non-coverage by Machta, Raju, Quinn, and the thematic-adjacency note for Brown-Bossomaier-Barnett.

After those three steps, if no additional prior art is found covering per-site fields + temperature-sweep + spectrum observables + transition-order discrimination, then CCA-1c may be cautiously characterized as "a narrow methodological contribution within an established research program" — and then tested on q=3 vs q=5 as the next experimental step. If prior art is found, CCA-1c is absorbed into that prior work as a replication or extension.

### Net effect on M0

The harsh first-addendum posture ("CCA might restate JJK/Prokopenko-Lizier") was wrong in detail and has been corrected twice now. The primary-source verification and targeted search together produce this honest position:

**CCA's general setting (sloppy models applied to lattice phase transitions) is Machta 2013. CCA's specific construction (per-site fields + d_eff/η + temperature sweep + transition-order discrimination) has no confirmed prior art in the searched literatures, with one remaining unchecked vector (inverse-Ising / maxent). It may be a genuine narrow methodological contribution, or it may replicate unchecked prior work. Novelty status is "pending final check, cautiously optimistic."**

This is the third iteration of the CCA calibration in a single M0 session, and the progressive sharpening is exactly what the charter's "verify the object, not the summary" rule is designed to produce. The next iteration of this calibration should not happen until (a) the inverse-Ising gap is closed and (b) at least one additional experiment (q=3 vs q=5) is run.

**No other M0 findings were affected by the primary-source reading or the targeted search.** DFIG-as-sloppy-models-reparameterization (Machta 2013 is now the confirmed primary reference) stands. Fisher-gravity chain as analogy stands (the targeted search found no sloppy-gravity bridge literature). P17 as high-risk speculation stands.

---

## Third Addendum: Inverse-Ising / Maxent Gap Closure (2026-04-08, same-day)

Under the recommendation from the second addendum, a third targeted agent search was run focused specifically on the inverse-Ising / maximum-entropy-model / neural-criticality community — the one open prior-art vector remaining after the second addendum. This community routinely parameterizes Fisher information matrices by per-site local fields $h_i$ for inference purposes, so it was the most plausible remaining location for prior art covering CCA's specific construction.

### Researchers searched

Targeted publication-record search across: **Thierry Mora, William Bialek, Gašper Tkačik, Simona Cocco, Rémi Monasson, Martin Weigt, John Hertz, Erik Aurell, Elad Schneidman, Michael Berry II**, plus generic phrase-space search on inverse-Ising, direct coupling analysis, maxent neural models, Boltzmann machine learning, and thermodynamic-integration inference methods.

### Findings

**Closest adjacent hit (neural criticality lineage):**

- **Tkačik, Marre, Mora, Amodei, Schneidman, Berry, Bialek** — *"Thermodynamics for a network of neurons: Signatures of criticality,"* **PNAS 112, 11508 (2015)**, arXiv:1407.5946. This is the canonical "retinal populations near criticality" paper. The construction: fit a pairwise maximum-entropy model to $N \leq 160$ retinal neurons, then do thermodynamic integration by rescaling inferred couplings with a fictitious inverse temperature $\beta$ and trace the heat capacity $C(\beta)$. Peak is found near $\beta=1$.
- **What they do that is similar to CCA**: sweep a temperature-like parameter across a (putative) critical point; track an information-theoretic observable; observe a peak structure at criticality.
- **What they do not do**: compute FIM eigenvalue spectrum, define participation ratio or isotropy observable, discriminate transition orders. Their observable is heat capacity / specific heat, not FIM spectrum.
- **Verdict**: thematically adjacent, **not prior art** for CCA's specific construction. Must be cited in CCA docs as the closest work in the neural-criticality subliterature.

**Inverse-Ising inference-quality lineage:**

- **Nguyen, Zecchina, Berg** — *"Inverse statistical problems: from the inverse Ising problem to data science,"* **Advances in Physics 66, 197 (2017)**, arXiv:1702.01522. Uses susceptibility $\chi$ (= FIM on couplings and fields) and $\chi^{-1}$ to bound inference error. **Discusses FIM eigenvalue hierarchy as an identifiability / sloppiness diagnostic for inferred parameters**, not as a probe tracked across a transition.
- **Verdict**: Uses FIM eigenvalue structure, but for inference quality — not for phase-transition spectroscopy. **Not prior art** for CCA's specific construction.

**Most recent candidate checked directly:**

- **arXiv:2507.02574 (2025)** — *"Learning and Testing Inverse Statistical Problems For Interacting Systems Undergoing Phase Transition."* This paper covers Ising, vector Potts, Blume-Capel across phase transitions using ML, pseudo-likelihood, and mean-field inference methods — a maximally plausible direct hit on title. **Verified via direct abstract fetch**: the paper is about **inference-method performance comparison** across transitions (which inference algorithm recovers parameters best in which regime), **not about FIM eigenvalue spectrum analysis**. Abstract makes no mention of participation ratio, isotropy indicator, spectrum tracking, or transition-order discrimination via FIM observables.
- **Verdict**: Not prior art. Different research question. **Residual risk**: owner should spot-check the methods section personally if they want certainty, but the abstract framing makes it highly unlikely to contain the CCA construction.

**Genre collision noted (not prior art but worth mentioning):**

- **Quantum Fisher information (QFI) across quantum phase transitions** — there is a substantial literature (PRA 82, 022306; arXiv:1509.01739; arXiv:2211.00813 and others) computing QFI for the transverse-field Ising, Dicke, LMG, and related models as a function of a global parameter (temperature, field, or coupling) across a critical point. **These use QFI with respect to a single global parameter (scalar output) on quantum states**, not a per-site-field FIM matrix spectrum on classical lattice configurations. Different mathematical object, different parameterization. But "Fisher information across a phase transition" is an already-populated phrase in a related literature, and the owner should cite this as a prior-art adjacency when positioning CCA — a reviewer would bring it up.

**Participation-ratio-on-FIM spectrum genre**:

- Participation ratio as an FIM-spectrum observable is standard in the **deep-network FIM literature** (Karakida, Akaho, Amari 2019; Pennington-Worah follow-ups). The owner's $d_\text{eff} = (\sum\lambda)^2 / \sum\lambda^2$ is mathematically identical to observables from that literature transplanted to spin systems. If the owner ever positions $d_\text{eff}$ as a novel observable, this transplant history must be cited: the observable is not new, the *application* to lattice-spin FIMs possibly is.

### Bottom line (third addendum)

**Status: NO direct prior art found for CCA's specific construction, with moderate confidence.**

After three iterations of the audit (harsh first pass → follow-up correction → primary-source reading → targeted Sethna-group search → targeted inverse-Ising/maxent search), the following is the honest status:

- **Confirmed prior art for the general setting**: Machta-Chachra-Transtrum-Sethna 2013 (FIM eigenvalue spectrum on Ising at criticality; global couplings, no temperature sweep, no Potts, no transition-order discrimination)
- **Confirmed adjacent work in three distinct literatures**:
  1. Sloppy-models lineage (Sethna group, Raju, Quinn) — same FIM-spectrum-of-physical-model setting, different parameterization, no CCA coverage
  2. Neural-criticality lineage (Tkačik-Mora-Bialek 2015) — thermodynamic integration across criticality via heat capacity, not FIM spectroscopy
  3. Inverse-Ising inference lineage (Nguyen-Zecchina-Berg, Cocco-Monasson) — FIM eigenvalue hierarchy for inference quality, not phase-transition spectroscopy
  4. Quantum Fisher information lineage (various) — scalar QFI vs global parameter, not per-site-field matrix spectrum
  5. Deep-network FIM lineage (Karakida, Pennington) — participation ratio as observable, transplantable to spin systems but not done
  6. Transfer-entropy first-order Potts (Brown-Bossomaier-Barnett 2022) — same motivating question, different mathematical object

- **No confirmed prior art** for the specific combination: per-site local field parameterization + $d_\text{eff}$/$\eta$ scalar observables + temperature sweep + first-order-vs-continuous Potts discrimination

### Residual risks (what "moderate confidence" means)

Three specific gaps remain that the agent could not close:

1. **Supplementary materials** of the Tkačik/Mora/Bialek 2012–2020 neural-criticality papers were not exhaustively checked. A supplementary figure computing FIM eigenvalue dispersion across $\beta$ in a retinal maxent model is technically possible and would collapse the novelty claim.
2. **Non-English-language literature** (Chinese, Japanese, Russian, and pre-2005) is under-indexed in the searches performed.
3. **Direct expert correspondence**: a direct email query to Mora, Tkačik, Nguyen, or another senior researcher in the community asking "has anyone done per-site-field FIM eigenvalue spectroscopy across thermal transitions?" would give a better answer than any amount of web searching. This is owner-action, not agent work.

### Final CCA calibration (after three audit iterations)

- **CCA general framework (FIM spectroscopy on lattice phase transitions)**: **Supported as a concrete specialization** of the Machta-Sethna sloppy-models program. Not novel as a general idea. Must cite Machta 2013 as foundational.

- **CCA-specific construction** (per-site field parameterization + $d_\text{eff}$/$\eta$ tracked across $T$ + transition-order discriminator via $d\eta/dT$ magnitude and curve shape): **possibly narrow-novel** — no confirmed prior art across three targeted searches. **Status: "Cautiously speculative-positive"** — methodological novelty is plausible, but charter rule prohibits promoting above Speculative without (i) a second independent test (q=3 vs q=5 Potts) and (ii) ideally a direct expert verification.

- **CCA-1c (curve shape discriminates transition order)**: **Speculative.** Single test (q=2 vs q=10). Consistent with no prior art the audit could find. **Candidate for genuine narrow contribution** but blocked on the charter's "single test is not support" rule.

- **CCA-1 (isotropy = criticality)** and **CCA-1b L^d scaling**: **FALSIFIED.** Unchanged.

- **Quantum Fisher information lineage** must be cited as prior-art adjacency when positioning CCA externally, even though it uses a different mathematical object. Reviewers will bring it up.

### Required citations for CCA docs (final, after all three addenda)

Any CCA document making a claim about FIM-based phase-transition analysis **must** cite:

1. **Machta, Chachra, Transtrum, Sethna**, *Science* 342, 604 (2013); arXiv:1303.6738 — **foundational**, FIM spectrum on Ising at criticality
2. **Raju, Machta, Sethna** — "Information geometry and the renormalization group" — **extension** of Machta 2013
3. **Quinn, Abbott, Transtrum, Machta, Sethna**, *Rep. Prog. Phys.* 86, 035901 (2023) — **modern synthesis** of the program
4. **Tkačik, Marre, Mora, Amodei, Schneidman, Berry, Bialek**, *PNAS* 112, 11508 (2015); arXiv:1407.5946 — **neural criticality via thermodynamic integration**, closest adjacent work in a different community
5. **Nguyen, Zecchina, Berg**, *Adv. Phys.* 66, 197 (2017); arXiv:1702.01522 — **inverse Ising inference** using FIM eigenvalue hierarchy
6. **Brown, Bossomaier, Barnett**, *Sci. Rep.* 12 (2022); arXiv:1810.09607 — **transfer-entropy first-order Potts**, thematically closest work to CCA-1c
7. **Amari & Nagaoka**, *Methods of Information Geometry* (AMS 2000) — **standard info-geometry reference**
8. **Karakida, Akaho, Amari**, "Universal Statistics of Fisher Information in Deep Neural Networks" (2019); arXiv:1910.05992 — **participation-ratio-on-FIM-spectrum precedent** in deep learning
9. **Quantum Fisher information lineage** (at least 1-2 representative papers, e.g., arXiv:1509.01739) — **genre adjacency** for "Fisher information across a phase transition"

### What this means for next CCA experimental work

Per charter rule "Mode B depends on Mode A" (no experiments on ungrounded foundations), the minimum preconditions for running q=3 vs q=5 Potts or any other CCA experiment are:

1. **Add the 9 citations above to CCA_MATHEMATICAL_FORMALIZATION.md main body** (not just the header note)
2. **Read Brown-Bossomaier-Barnett 2022** — closest adjacent work; understanding it will sharpen how CCA-1c is positioned
3. **Optional but recommended: read Tkačik 2015 supplementary materials** — closes the highest residual risk on the novelty claim
4. **Optional but highest-value: a direct email query** to Mora, Tkačik, Nguyen, or a similar senior researcher asking about per-site-field FIM eigenvalue spectroscopy on thermal transitions. Owner action.

If all four are done and no additional prior art surfaces, CCA-1c can be characterized in the next experimental writeup as "a narrow methodological contribution within the Machta-Sethna sloppy-models program, with no confirmed prior art across three targeted searches but with one residual expert-correspondence gap." This is the maximum honest novelty claim the audit supports.

### Meta-note on the M0 audit process

This audit iterated three times in a single session: harsh first pass → corrected follow-up → primary-source verification with two additional targeted searches. The CCA novelty calibration went: **"already done 20 years ago"** → **"partial prior art Machta 2013, pending owner confirmation"** → **"confirmed prior art for general setting, no confirmed prior art for specific construction with one open vector"** → **"no confirmed prior art across three targeted searches, moderate confidence, residual risks named explicitly."**

Each iteration sharpened the claim by replacing agent-summarized verdicts with primary-source facts. The charter's "push back on your own work" and "verify the object, not the summary" rules directly produced this progression. A single-pass audit would have left the wiki in a substantially wrong state — either "this has all been done" (the first pass's posture) or "this is novel" (the default AI posture without an epistemic contract). The three-iteration result is neither — it is a specific, grounded, calibrated claim about what is known, what is adjacent, and what is genuinely open.

**This is the M0 calibration. Further sharpening requires either owner action (primary-source reading, direct expert correspondence) or new experimental evidence (second independent test of CCA-1c).** No further audit iterations are productive without one of those inputs.

---

## Fourth Addendum: Primary-Source Reading (2026-04-08, same day)

The owner obtained and provided four primary-source PDFs from his `Research_Papers/` folder: Machta-Chachra-Transtrum-Sethna 2013 Science (already covered in the Second Addendum), Transtrum et al. 2015 J. Chem. Phys. perspective, Mattingly-Transtrum-Abbott-Machta 2018 PNAS (bonus), Brown-Bossomaier-Barnett 2022 Sci. Rep., and Quinn-Abbott-Transtrum-Machta-Sethna 2023 Rep. Prog. Phys. All four were read in full (or to the end of technical content for the 60-page Quinn 2023 review).

This closes the audit's highest-residual-risk vectors via direct primary-source verification rather than agent summarization.

### Summary table of primary-source findings

| Paper | Uses FIM eigenvalue spectrum? | Per-site fields? | T-sweep primary axis? | Potts? | Transition-order discrimination? | Covers CCA construction? |
|---|---|---|---|---|---|---|
| Machta 2013 Science | ✓ | ✗ (global couplings) | ✗ (coarsening) | ✗ (Ising) | ✗ | ✗ |
| Transtrum 2015 JCP | discussed via Machta | ✗ | ✗ | ✗ | ✗ | ✗ |
| Mattingly 2018 PNAS | ✗ (uses optimal prior atoms) | ✗ (exp decay model) | ✗ | ✗ | ✗ | ✗ |
| Brown-Bossomaier-Barnett 2022 Sci. Rep. | ✗ (uses transfer entropy) | ✗ (global states) | ✓ | ✓ (q=2,5,7,10) | ✓ | ✗ (different object) |
| Quinn 2023 Rep. Prog. Phys. | ✓ | ✗ (global couplings) | ✗ | ✗ | ✗ | ✗ |

**No paper in the four primary sources covers CCA's specific construction.** The construction (per-site fields + $d_\text{eff}$/η scalar observables + T-sweep + transition-order discrimination via $d\eta/dT$ magnitude and curve shape) remains cautiously-possibly-narrow-novel, confirmed now by direct reading rather than agent summary.

### Important finding 1: Mattingly 2018 defines $d_\text{eff}$ with a different formula — mandatory citation

**Mattingly, Transtrum, Abbott, Machta**, *"Maximizing the information learned from finite data selects a simple model,"* **PNAS 115, 1760 (2018)**, arXiv:1705.01166.

This paper is in the Sethna lineage (Transtrum and Benjamin Machta are co-authors). Its topic is maximally informative priors on sloppy-model parameter manifolds. In Figure 4C and surrounding text, **the paper defines a scalar "effective dimensionality" observable**:

$$d_\text{eff} = \sum_{r=1}^{D} r \cdot \Omega_r$$

where $\Omega_r$ is the total weight of the optimal discrete prior $p_\star(\theta)$ on edges of dimension $r$ of the parameter manifold. As the measurement noise $\sigma$ decreases (more data), this $d_\text{eff}$ grows smoothly from 0 toward the full parameter-space dimension $D$, corresponding to weight migrating from lower-dimensional boundaries into the interior.

**This is a different formula from CCA's $d_\text{eff}$**:

| | Mattingly 2018 $d_\text{eff}$ | CCA $d_\text{eff}$ |
|---|---|---|
| **Formula** | $\sum_r r \cdot \Omega_r$ | $(\sum_i \lambda_i)^2 / \sum_i \lambda_i^2$ |
| **Object** | Weights of optimal maximally informative discrete prior on manifold boundaries | Participation ratio of FIM eigenvalue spectrum |
| **What grows** | Data quality (smaller σ) → weight migrates inward | Smaller λ₂/λ₁ ratio → more isotropic spectrum |
| **Used on** | Sum-of-exponentials, Bernoulli coin, Gaussian measurement | 2D Ising / Potts lattice at various T |

The two observables are computationally and conceptually different, but **both are called "$d_\text{eff}$" in the sloppy-models community, and both measure "how many effective dimensions are operational"**. Mattingly 2018 is five years earlier and comes from the authoritative lineage.

**Mandatory action:** when CCA is written up (even just in `CCA_MATHEMATICAL_FORMALIZATION.md` main body), Mattingly 2018 **must** be cited, and the distinction between Mattingly's $d_\text{eff}$ and CCA's $d_\text{eff}$ must be drawn explicitly. Failing to do this will produce confused readers and a legitimate prior-art challenge. This is a **citation miss**, not a novelty challenge — the formulas are different — but citing the prior usage of the terminology is basic scholarly hygiene.

### Important finding 2: Brown-Bossomaier-Barnett 2022 is more relevant than the audit assumed

**Brown, Bossomaier, Barnett**, *"Information flow in first-order Potts model phase transition,"* **Sci. Rep. 12, 15145 (2022)**, arXiv:1810.09607.

Read in full. Key facts:

- **Uses Global Transfer Entropy (GTE)**, not FIM. Confirmed different mathematical object from CCA.
- **Studies Potts q = 2, 5, 7, 10** — directly overlaps the CCA Phase C/D comparison (q=2 vs q=10). The q=5 and q=7 cases are exactly the "second test" CCA needs per the charter's "single test is not support" rule.
- **Key empirical findings:**
  - For **continuous** transitions (q=2 Ising): GTE peaks on the disordered side, peak location stays stable above T_c as L increases.
  - For **first-order** transitions (q=5, 7, 10): GTE peaks on the disordered side, but peak location converges toward T_c as q and L increase, and the curve shows a sharp jump.
  - **The curve-shape difference** (smooth stable peak vs converging peak with sharp jump) is qualitatively similar to what CCA-1c claims for η(T).
- **Physical mechanism (Eqs. 5-6 in their paper):** $G \propto \sum_c p(c) L_c$ where $L_c$ is the average interfacial length of clusters of size $c$. Information flows at cluster boundaries. At high T, clusters are small and thermal noise dominates; at low T, one dominant cluster has shrinking internal holes so interfacial length falls; the peak sits in between on the disordered side. **Average interfacial length matches GTE behavior across all q and L tested (their Fig. 3).** This is a simple, testable physical mechanism.

**Implications for CCA:**

1. **The broader research program — "information-theoretic early warning / discrimination of first-order Potts transitions" — is not CCA's contribution.** Brown et al. published it in arXiv 2018, Sci. Rep. 2022. CCA's motivation is in their shadow.

2. **CCA-1c's curve-shape claim is in the same family of observations** as Brown et al.'s GTE-shape-difference claim. CCA's specific observable (η derived from FIM spectrum) may be a methodological variant, but the **observation** "information-theoretic quantities distinguish Potts transition order via curve shape" is Brown et al.'s.

3. **Brown et al. have a transparent physical mechanism (interfacial length) that CCA currently lacks.** This is a real gap. The owner should explicitly ask: *"Can CCA's $d_\text{eff}(T)$ and $\eta(T)$ behavior be explained via cluster interfacial geometry, or is it measuring something structurally different from transfer entropy and interfacial length?"* This is the single highest-leverage scientific question the audit has surfaced. If the answer is "yes, interfacial length explains both," then CCA is a Fisher-geometric restatement of Brown et al.'s result, and its contribution is methodological only (same observation, different calculation path). If the answer is "no, CCA measures something different," then CCA captures a genuinely different aspect of the transition, and its contribution is both methodological and phenomenological.

4. **The q=3 vs q=5 test the charter prescribes can be sharpened.** Instead of just running q=3 vs q=5, the owner should replicate Brown et al.'s q=2, 5, 7, 10 comparison with FIM observables and **check whether the curve-shape/peak-location behavior tracks GTE or diverges from it.** If they track, this is strong evidence that both observables are proxies for the same underlying physics (interfacial length). If they diverge, CCA captures something different and the novelty claim strengthens.

5. **Brown et al. must be cited prominently in any CCA writeup**, not just as "thematically adjacent." The honest framing is: *"The CCA construction extends the broader information-theoretic program for discriminating first-order Potts transitions initiated by Brown, Bossomaier, and Barnett (2018/2022) from transfer entropy to Fisher information matrix spectrum observables."*

### Important finding 3: Quinn 2023 admits Ising is not sloppy

In Quinn 2023 Section 8.2 ("Understanding emergent low-dimensional behaviors"), the authors explicitly write:

> *"The Ising model is not sloppy, and has no beautiful emergent theory, unless one only cares about long length and time scales."*

This is a tacit acknowledgment that at the microscopic level — 2 parameters (temperature-like and field-like) — Ising isn't even in the sloppy regime. Sloppiness in Ising only emerges under coarse-graining (Machta 2013's demonstration).

**Implication for DFIG / P5:** The Sethna lineage's own view is that **Ising at its microscopic parameterization is NOT a sloppy model**. The P5 claim "Fisher Rank = D_eff" as applied to Ising is not well-positioned as "applying sloppy models to Ising" because Ising microscopically isn't sloppy. What Machta 2013 actually demonstrated is that **under coarse-graining, Ising becomes sloppy in the RG-relevant/irrelevant sense**. P5's geometric-systems applications (tori, random graphs, random geometric graphs) may be closer to "applying the sloppy-model framework to a different class of models entirely" than to "applying Machta 2013's specific Ising result."

**Action:** P5's rationale in the calibration table should note this. The downgrade stays Supported-as-application, but the "application of what, to what" needs more careful phrasing than the previous audit rounds used.

### Important finding 4: The Raju reference is now confirmed

From Quinn 2023 reference 39: **Raju, Machta, Sethna**, *"Information loss under coarse graining: A geometric approach,"* **Physical Review E 98, 052101 (2018)**, arXiv:1710.05787.

This is the exact citation I could not verify in earlier audits. Now confirmed via primary source. The paper extends Machta 2013 by deriving the RG-flow equation for the FIM (Eq. 15 in Quinn 2023). Still global couplings, still no per-site fields, still no temperature sweep. Not prior art for CCA's specific construction, but the correct citation to use when referring to "FIM flow under RG" in the Sethna lineage.

### Updated required-citations list for CCA docs (final, after primary-source reading)

Any CCA document making a claim about FIM-based phase-transition analysis **must** cite:

1. **Machta, Chachra, Transtrum, Sethna**, *Science* **342**, 604 (2013); arXiv:1303.6738 — **foundational**, FIM spectrum on Ising at criticality
2. **Raju, Machta, Sethna**, *Phys. Rev. E* **98**, 052101 (2018); arXiv:1710.05787 — **RG flow of FIM**, extension of Machta 2013
3. **Transtrum, Machta, Brown, Daniels, Myers, Sethna**, *J. Chem. Phys.* **143**, 010901 (2015); arXiv:1501.07668 — **framing** of sloppy-models program
4. **Mattingly, Transtrum, Abbott, Machta**, *PNAS* **115**, 1760 (2018); arXiv:1705.01166 — **PRIOR USE of "$d_\text{eff}$" terminology** with a different formula; mandatory citation for terminology hygiene
5. **Quinn, Abbott, Transtrum, Machta, Sethna**, *Rep. Prog. Phys.* **86**, 035901 (2023) — **modern synthesis**
6. **Brown, Bossomaier, Barnett**, *Sci. Rep.* **12**, 15145 (2022); arXiv:1810.09607 — **closest adjacent work**, prior art for the broader research program, must be cited prominently (not as a footnote)
7. **Tkačik, Marre, Mora, Amodei, Schneidman, Berry, Bialek**, *PNAS* **112**, 11508 (2015); arXiv:1407.5946 — **neural criticality via thermodynamic integration**, adjacent lineage
8. **Nguyen, Zecchina, Berg**, *Adv. Phys.* **66**, 197 (2017); arXiv:1702.01522 — **inverse Ising FIM hierarchy for inference**, adjacent lineage
9. **Amari & Nagaoka**, *Methods of Information Geometry* (AMS 2000) — standard reference
10. **Karakida, Akaho, Amari**, arXiv:1806.01316 — **participation-ratio observable precedent** in deep-network FIM
11. **Hauke, Heyl, Tagliacozzo, Zoller**, *Nature Physics* **12**, 778 (2016); arXiv:1509.01739 — **quantum Fisher information across critical points**, genre adjacency

### Final calibration after primary-source reading

The calibrations from the Third Addendum **are not changed** by the primary-source reading. The findings confirm them:

- **CCA's general setting** (FIM spectrum on Ising at criticality) is Machta 2013. **Confirmed via primary source.**
- **CCA's specific construction** (per-site fields + $d_\text{eff}$/η + T-sweep + transition-order discrimination) has **no confirmed prior art across four primary sources read in full + three targeted agent searches**. Status: **NO prior art found, moderate-to-good confidence** (upgraded from "moderate" in the Third Addendum).
- **Mattingly 2018 is a terminology precedent for "$d_\text{eff}$"**, not a construction precedent. Different formula. Must cite.
- **Brown-Bossomaier-Barnett 2022 is the prior art for the broader research program** (information-theoretic discrimination of first-order Potts transitions). CCA's contribution is at most a specific methodological variant within that program, using a different mathematical object.
- **CCA needs a physical mechanism** comparable to Brown et al.'s interfacial-length explanation before the η/d_eff observables can be interpreted as anything more than correlates.
- **The q=3 vs q=5 test should be extended to q=2, 5, 7, 10** (replicating Brown et al.'s q-sweep) and **directly compared against GTE values** if computable. This turns the "second test" into a meaningful cross-observable comparison rather than just a replication.

### Owner actions after primary-source reading

The following are now blocked on owner action (cannot be done by Claude):

1. **Read Brown-Bossomaier-Barnett 2022 carefully.** Their interfacial-length physical mechanism is the most important scientific comparison point for CCA. Understanding it informs how to position CCA-1c honestly.
2. **Decide on the mechanism question:** does CCA's $d_\text{eff}(T)$ and $\eta(T)$ measure something reducible to cluster interfacial geometry, or something structurally different? If you cannot answer this without running an experiment, the experiment is **run q=2, 5, 7, 10 Potts with FIM observables alongside a transfer-entropy computation, and compare curve shapes directly.**
3. **Update CCA_MATHEMATICAL_FORMALIZATION.md main body** with the eleven required citations above and explicit discussion of how CCA relates to Brown et al. 2022 and how CCA's $d_\text{eff}$ relates to Mattingly 2018's.
4. **Verify the Amendola 2024 and Cadoni 2023 citations for P17.** Still pending from Main M0.

No additional audit iterations are productive. The prior-art question is now as closed as reasonable web-searching + primary-source reading can make it. Remaining uncertainty (non-English literature, Tkačik 2015 supplementary materials, direct expert correspondence) are owner-action items that do not change the calibration significantly.

**M0 is complete after four addenda.** Next milestone (M1) should be written after: (a) the three required citations are added to CCA doc main bodies, (b) the owner has read Brown-Bossomaier-Barnett 2022 and answered the mechanism question, and (c) at least one new experiment has been run with the expanded q-value sweep or (if that is not run) one of the Speculative conjectures has been formally retired.

---

## Fifth Addendum: Deep-Research Pass on Open Questions (2026-04-08, same day)

The owner directed Claude to execute deep research on the open questions left by the Fourth Addendum: (a) the Brown-Bossomaier-Barnett 2022 mechanism question for CCA, and (b) the Amendola 2024 + Cadoni 2023 citation verifications for P17/P23. Three parallel agent passes plus direct primary-source verification produced findings that **substantially update** the M0 calibration, including a major new prior-art identification and a terminology collision that must be addressed.

### Finding 1: Amendola 2024 — VERIFIED but the "5σ" figure was a forecast, not a current result

**Paper located and verified:** **Amendola, Rodrigues, Kumar, Quartin**, *"Constraints on cosmologically coupled black holes from gravitational wave observations and minimal formation mass,"* **MNRAS 528, 2377 (2024)**, DOI:10.1093/mnras/stae143, **arXiv:2307.02474**. Code: github.com/davi-rodrigues/CCBH-Numerics.

**What the paper actually says:**
- Uses 72 confident binary-BH events from the **GWTC-3 catalog** (LIGO O1+O2+O3). **Does NOT use O4** — O4 was still in progress at submission.
- **Current-data results**: 2σ upper limits on k:
  - **k < 2.1** (PLPP method, log-uniform delay-time prior)
  - **k < 2.5** (direct method, log-uniform delay-time prior)
  - **k < 1.1** (PLPP, with Ghodla 2023 corrected delay-time)
- **Tension with k=3 from current GWTC-3 data is roughly 2.6–3.7σ depending on methodology**, NOT 5σ.
- Authors' own conclusion (verbatim): *"the CCBH as proposed by Farrah et al. (2023b) is in strong tension with what we know about stellar progenitor BHs, but there still is an open parameter space where it can survive the present test."*
- **The "5σ" figure DOES appear in the paper but is a forecast**, verbatim: *"For the forecast and k = 3, the rejection level goes beyond 5σ."* The forecast is for a future LVK run with ~250 additional events.

**Verification verdict**: PARTIALLY VERIFIED. The citation is real. The qualitative direction (GW data disfavors k=3) is correct. The quantitative "5σ" framing in the wiki is **incorrect** — it conflates the paper's forecast with its current-data result.

**Required correction to P17/P23**: replace "Amendola 2024 5σ rejection of k=3" with *"Amendola, Rodrigues, Kumar & Quartin 2024 (MNRAS 528, 2377; arXiv:2307.02474) place 2σ upper limits k < 2.1 (PLPP method, GWTC-3) on cosmologically-coupled BHs, in strong tension (~3σ) with k=3 but not ruling it out from current data; their forecast for ~250 additional events reaches >5σ rejection of k=3."*

### Finding 2: Cadoni 2023 — VERIFIED with one wording caveat

**Paper located and verified:** **Cadoni, Sanna, Pitzalis, Banerjee, Murgia, Hazra, Branchesi**, *"Cosmological coupling of nonsingular black holes,"* **JCAP 11 (2023) 007**, DOI:10.1088/1475-7516/2023/11/007, **arXiv:2306.11588**.

**What the paper actually says (verbatim from abstract):**
> *"We find that the leading contribution to the resulting growth of the BH mass (M_BH) as a function of the scale factor a stems from the curvature term, yielding M_BH ∝ a^k, with k=1. We demonstrate that such a linear scaling is **universal for spherically-symmetric objects**, and it is the only contribution in the case of **regular BHs**. For nonsingular horizonless compact objects we instead obtain an additional **subleading model-dependent term**."*

**Key nuances the wiki entry currently misses:**
1. The paper uses "**universal**" rather than "generic." k=1 is "the only contribution" only for **regular BHs**; for horizonless compact objects there's an additional model-dependent term.
2. **Multi-author** (7 authors), not solo Cadoni.
3. **The paper's own KS-distance analysis on the Farrah elliptical-galaxy sample actually prefers k=3 over their theoretical k=1.** They take this as evidence that BHs may be non-GR objects, not as confirmation of their theoretical prediction.
4. The paper's conclusion: GR nonsingular BHs / regular BHs (with k=1 cosmological coupling) are **"unlikely to be the source of dark energy."**

**Verification verdict**: VERIFIED with wording caveat. The k=1 prediction is real.

**Required correction to P17/P23**: replace "Cadoni 2023 generic k=1 for nonsingular BH interiors" with *"Cadoni, Sanna, Pitzalis, Banerjee, Murgia, Hazra & Branchesi 2023 (JCAP 11, 007; arXiv:2306.11588) prove that k=1 is the universal leading-order cosmological-coupling prediction for spherically-symmetric regular (nonsingular) BHs in GR; their own KS analysis on the Farrah-Croker elliptical-galaxy sample prefers k=3 over k=1, which they interpret as possible evidence that astrophysical BHs are non-GR objects rather than as support for the Farrah-Croker scenario."*

### Finding 3: MAJOR — CCA's prior-art surface is BROADER than the Fourth Addendum identified

The deep-research literature scan on "FIM eigenvalue spectrum vs cluster interfacial geometry" produced a **substantial prior-art finding that requires updating the CCA calibration**.

**The mathematical foundation (textbook, not novel):** For a 2D classical spin lattice (Ising or Potts) parameterized by per-site local fields $h_i$, the Fisher Information Matrix at $h=0$ equals the connected 2-point correlation matrix:

$$F_{ij} = \frac{\partial^2 (-\log Z[h])}{\partial h_i \partial h_j}\bigg|_{h=0} = \langle s_i s_j \rangle - \langle s_i \rangle \langle s_j \rangle = \chi_{ij}$$

**This is textbook stat mech.** The "FIM in CCA" is the connected susceptibility matrix — a century-old object. CCA's novelty (if any) cannot be in the use of this matrix, only in the specific scalar observables derived from its spectrum.

**Newly identified prior art for the broader CCA program:**

1. **Vinayak, Prosen, Buča, Seligman**, *"Spectral analysis of finite-time correlation matrices near equilibrium phase transitions,"* **Europhys. Lett. 108, 20006 (2014)**, **arXiv:1403.7218**.
   - Proves analytically that the **eigenvalue density of the spatial correlation matrix at a phase transition is a power law derivable from the spatial correlation function**.
   - Validated numerically on **2D Ising with Metropolis** dynamics.
   - Off-criticality: semicircle-like / gapped spectrum. At criticality: power-law bulk.
   - Establishes that **the power-law exponent of the spectral density is fixed by the standard η critical exponent of the correlation function** ($C(r) \sim r^{-(d-2+\eta)}$, so for 2D Ising η=1/4).
   - **Does NOT compute participation ratio as a scalar tracker. Does NOT define η isotropy. Does NOT do Potts q>2. Does NOT discriminate first-order vs continuous.**
   - **Verdict**: prior art for the **general approach** "FIM-of-Ising-spectrum-as-phase-transition-probe." CCA's specific observables may still be narrow-novel within this framework, but the framework itself is established.

2. **Saberi, Saber, Moessner**, *"Interaction-correlated random matrices,"* **Phys. Rev. B 110, L180102 (2024)**, **arXiv:2503.03472**.
   - Constructs random-matrix ensemble from **2D Ising Boltzmann factors**.
   - Reports **bell-shaped bulk with universal heavy tail at criticality** vs **semicircle off-critical**.
   - **Rescaled maximum eigenvalues used as order parameter** for ferromagnetic Ising transition.
   - Extreme eigenvalue statistics become **Fréchet** at criticality (not Tracy-Widom).
   - **Studies only Ising. Does NOT do Potts q>2. Does NOT use participation ratio. Does NOT discriminate transition orders.**
   - **Notably co-authored by Saberi**, who is also the SLE/cluster-perimeter expert cited by Brown-Bossomaier-Barnett 2022. The same researcher works in both the cluster-geometry literature and the random-matrix-of-correlation literature.
   - **Verdict**: Active 2024 publication in the **same broader research program** (correlation-matrix spectrum on 2D Ising as transition probe). Closer to CCA than Vinayak 2014 in "spectrum-vs-temperature as transition discriminator" framing.

3. **Borgs & Chayes**, *"The covariance matrix of the Potts model: A random cluster analysis,"* **J. Stat. Phys. 82, 1235 (1996)**, **arXiv:adap-org/9411001**.
   - **Rigorously connects** the **Potts connected covariance matrix** (= the FIM in CCA) to **Fortuin-Kasteleyn cluster representations**.
   - Proves: in the ordered phase, eigenvalues are 0, $G_1(x-y)$ [simple], $G_2(x-y)$ [(q-2)-fold degenerate]. Eigenvalues are expressible via cluster connectivities and cluster covariances.
   - Proves: one of the correlation lengths extracted from an eigenvalue equals the inverse decay rate of the **diameter** of finite FK clusters.
   - **The closest mathematical bridge between the FIM-like spectrum and cluster geometry in Potts.**
   - **Geometric object is cluster diameter, not cluster perimeter / interfacial length.** These scale the same way at criticality (both fractal) but are different observables.
   - **Verdict**: Direct prior art for the relationship between Potts connected correlation matrix and cluster geometry. CCA cannot claim novelty in "linking Potts FIM to cluster geometry" — Borgs-Chayes did this rigorously 30 years ago.

### Finding 4: Resolution of the Brown-Bossomaier-Barnett 2022 mechanism question

**The mechanism question:** Can CCA's $d_\text{eff}(T)$ and $\eta_\text{CCA}(T)$ be explained via cluster interfacial geometry (Brown et al.'s mechanism), or do they capture something structurally different from transfer entropy?

**Mathematical analysis based on FIM = connected correlation matrix:**

- **CCA's $d_\text{eff}$** (participation ratio of FIM spectrum) and **$\eta_\text{CCA}$** (isotropy indicator of FIM spectrum) are **scalar functionals of the connected 2-point correlation matrix**.
- **Cluster interfacial length** is a **multi-point geometric observable** that depends on cluster connectivity, which involves joint distributions of arbitrary numbers of spins.
- **At a continuous critical point in 2D** (Ising, Potts q≤4), scale invariance and conformal symmetry mean the 2-point function is "complete" in the sense that higher-point functions are constrained by it via OPEs. Both CCA observables and Brown's interfacial length are governed by the same underlying scaling exponents (η_critical, fractal dimension d_f). **They should track each other up to scaling factors at criticality**.
- **At first-order transitions** (Potts q≥5 in 2D), scale invariance fails. The 2-point function has exponential decay with finite correlation length; cluster interfacial length is determined by the latent heat / discontinuity structure. **The 2-point and multi-point observables decouple** — CCA observables and Brown's interfacial length should diverge.

**Concrete experimental check the owner can do**: At T=T_c for Potts q=2 (continuous in 2D, Ising universality class with η_critical = 1/4):
- CCA's $d_\text{eff}(T_c)$ and $\eta_\text{CCA}(T_c)$ should be **derivable from η_critical = 1/4 via finite-size scaling theory** if they're reading out the standard critical exponent.
- If the numerical values from Phase B/C agree with the analytical prediction from η_critical: CCA observables on continuous transitions are reading out a known critical exponent. **No novel content at continuous transitions.**
- If they disagree: CCA observables capture something η_critical doesn't.

**Tentative answer to the mechanism question**: At continuous transitions (q≤4 Potts), CCA observables are **likely reducible to the standard η_critical critical exponent of the correlation function**, which in turn governs both Brown's interfacial-length behavior and CCA's spectrum behavior. **At first-order transitions (q≥5), CCA observables and Brown's interfacial length should both still distinguish transition order, but via different mathematical mechanisms**: Brown's via interfacial geometry, CCA's via the breakdown of the power-law spectrum. **This is where CCA may have genuine narrow-novel content**: the first-order regime, where the FIM spectrum's behavior can no longer be derived from a critical exponent and reflects the latent heat / discontinuity structure directly.

### Finding 5: TERMINOLOGY COLLISION — CCA's "η" conflicts with standard stat-mech "η"

This is a basic scholarly hygiene issue that **must** be addressed:

- **Standard stat-mech η** (anomalous dimension of two-point function): $C(r) \sim r^{-(d-2+\eta)}$. For 2D Ising universality class, η = 1/4.
- **CCA's η** (isotropy indicator of FIM eigenvalue spectrum): some function of the eigenvalue distribution.

These are **completely different objects** but **share the symbol η**. Worse, since the FIM IS the connected correlation matrix, and the standard η governs the spectrum of the FIM at criticality, **the two η's are mathematically related** — CCA's $\eta_\text{CCA}$ at criticality is a function of the standard $\eta_\text{critical}$. This compounds the confusion.

**This is the second terminology collision in CCA** (the first was Mattingly 2018's $d_\text{eff}$ vs CCA's $d_\text{eff}$, both meaning "effective dimensionality" with different formulas). Both must be addressed when CCA is written up:
1. **Rename CCA's $\eta$** to something unambiguous (e.g., "spectrum isotropy indicator" $\iota$, or $\eta_\text{spec}$ with an explicit subscript distinguishing it from the critical exponent).
2. **Clearly distinguish CCA's $d_\text{eff}$** from Mattingly 2018's $d_\text{eff}$.

### Finding 6: The 2024 PRB paper (Saberi-Saber-Moessner) deserves separate audit attention

The Saberi-Saber-Moessner 2024 PRB paper is genuinely close to CCA's research program. It is **the most direct prior art among the new findings**. Specifically:
- Same general framework (correlation-matrix spectrum on 2D Ising as transition probe)
- Same 2D Ising target system
- Same publication timing as CCA's work (active research community, 2024)
- Different scalar observable (top eigenvalue vs PR/isotropy)
- Different scope (Ising only vs Potts q=2,10)

**Potential outcomes when the owner reads this paper:**
- **If they use top eigenvalue as their order-parameter observable and CCA uses PR/isotropy**: complementary observables on the same construction. CCA and Saberi 2024 are sister-paper prior art for each other's general approach; the specific scalar observables differ.
- **If they happen to discuss participation ratio or other isotropy observables in the body**: more direct prior art and CCA's novelty surface shrinks further.
- **If they discuss Potts**: even more direct overlap.

**The owner should read Saberi-Saber-Moessner 2024 PRB carefully** — this is now the **highest-priority single paper** for assessing CCA's novelty surface. Higher priority than Brown-Bossomaier-Barnett 2022, because it's more directly in CCA's specific mathematical framework.

### Updated CCA novelty status (after Fifth Addendum)

**Prior art for the CCA general approach** ("FIM = connected correlation matrix spectrum on 2D lattice as phase transition probe") is now established at multiple levels:

1. **Mathematical foundation (textbook)**: FIM = connected correlation matrix is in any stat mech textbook.
2. **Spectral analysis at criticality** (Vinayak-Prosen-Buča-Seligman 2014 EPL): power-law spectrum derivable from η_critical.
3. **Cluster geometry connection** (Borgs-Chayes 1996 J. Stat. Phys.): rigorous bridge between Potts covariance matrix and FK cluster representation.
4. **Modern transition discriminator via spectrum** (Saberi-Saber-Moessner 2024 PRB): top eigenvalue as order parameter on 2D Ising correlation-matrix RMT ensemble.

**CCA's remaining specific contributions** (after this round):
1. **Per-site local field parameterization** explicitly framed as the CCA construction. (Note: this is the natural parameterization for the FIM = χ identification, so it's not novel — anyone deriving the FIM as the connected correlation matrix would arrive here. The "per-site fields" framing is just notation.)
2. **Participation ratio + η_isotropy as paired scalar observables tracked across T**. (Vinayak 2014 didn't do this; Saberi 2024 uses top eigenvalue not PR. Possibly narrow-novel pending Saberi 2024 full read.)
3. **First-order vs continuous discrimination** specifically via PR/isotropy curve shape on Potts q=2 vs q=10. (Brown 2022 did the discrimination via transfer entropy; the FIM-spectrum version of the same discrimination may be CCA's specific contribution, but only if the q=10 first-order signature is genuinely outside the Vinayak/Saberi power-law-spectrum framework. This is uncertain pending the q=2 critical-exponent check above.)

**Status update for CCA-1c**: **Speculative** (unchanged), but the rationale now includes:
- **Prior art for general approach is established at 4 levels** (Borgs-Chayes 1996, Vinayak 2014, Saberi 2024 PRB, broader sloppy-models from Machta 2013)
- **At continuous transitions, CCA observables are likely reducible to standard η_critical critical exponent**. This must be tested directly via Phase B Ising analytical comparison.
- **The first-order regime is the remaining candidate territory** for genuine narrow novelty, but only if CCA's first-order observables are **not** derivable from the breakdown of the η_critical power-law structure (which would still be a known type of behavior).
- **Saberi-Saber-Moessner 2024 PRB must be read** before any further novelty claim.

### Required corrections to existing CCA documents

Before any new CCA experimental work:

1. **Rename CCA's η** to avoid collision with the standard stat-mech η critical exponent. Suggested: "$\iota_\text{CCA}$" (iota for isotropy) or "$\eta_\text{spec}$" (with subscript) or a non-Greek symbol entirely.
2. **Rename or clearly distinguish CCA's d_eff** from Mattingly 2018's d_eff.
3. **Add the new citations** to the required-citations list:
   - Vinayak, Prosen, Buča, Seligman 2014 EPL 108, 20006 — arXiv:1403.7218 — power-law spectrum from η_critical
   - Borgs & Chayes 1996 J. Stat. Phys. 82, 1235 — arXiv:adap-org/9411001 — Potts covariance matrix and FK clusters
   - Saberi, Saber, Moessner 2024 PRB 110, L180102 — arXiv:2503.03472 — interaction-correlated RMT on 2D Ising
4. **Add the analytical-comparison-at-T_c experimental check** to the next-experiments list: derive CCA observables from η_critical = 1/4 for 2D Ising and compare to Phase B numerical results.

### Owner action priorities (updated after Fifth Addendum)

In priority order:

1. **Read Saberi-Saber-Moessner 2024 PRB (arXiv:2503.03472)**. Now the highest-priority single paper — most direct prior art in CCA's mathematical framework. Higher priority than Brown 2022.
2. **Read Vinayak-Prosen-Buča-Seligman 2014 EPL (arXiv:1403.7218)**. Establishes the analytical framework relating correlation-matrix spectrum to η_critical on 2D Ising.
3. **Read Borgs-Chayes 1996 J. Stat. Phys. (arXiv:adap-org/9411001)**. The rigorous cluster-geometry-vs-covariance-matrix bridge. Determines whether CCA observables can be expressed in terms of Borgs-Chayes' FK cluster decomposition.
4. **Read Brown-Bossomaier-Barnett 2022 (arXiv:1810.09607)**. Still important for the GTE ↔ interfacial-length physical mechanism.
5. **Update P17 and P23 wording** in the wiki to reflect verified Amendola/Cadoni citations with corrected statistical figures (Amendola is 2σ upper limit not 5σ; Cadoni is 7-author, "universal" not "generic," with elliptical-sample preferring k=3).
6. **Address the η terminology collision** in CCA docs.
7. **Run the analytical-comparison-at-T_c check** for q=2 against η_critical = 1/4 before any new experimental phase.

**Note that priorities 1-3 supersede the Fourth Addendum's recommendation to read the Sethna-lineage papers (Quinn 2023, etc.) first.** The Sethna-lineage papers are framing documents; the new prior art (Vinayak, Borgs-Chayes, Saberi) is in a closer mathematical lineage and is more likely to constrain CCA's novelty claim.

### Net effect on M0 calibration

- **CCA's general setting prior art is now broader**: Vinayak 2014 + Borgs-Chayes 1996 + Saberi 2024 PRB join Machta 2013 + Brown 2022 in the prior-art map.
- **CCA's specific construction may still be narrow-novel**, but the surface has shrunk: PR/isotropy as paired observables and Potts first-order discrimination remain the candidate territory.
- **The mechanism question from Brown 2022 has a partial answer**: at continuous transitions both CCA and Brown observables likely reduce to η_critical; at first-order they may diverge, and that's where CCA may have content.
- **P17 and P23 statuses do not change** (still Speculative, high-risk) — the citation verifications confirm the underlying tensions are real but the specific quantitative claims in the wiki need correction.
- **Two terminology collisions** (CCA d_eff vs Mattingly d_eff; CCA η vs standard η_critical) are now mandatory hygiene items.

This is the final M0 update. Further iterations require either owner primary-source reading of the new prior art (Saberi 2024, Vinayak 2014, Borgs-Chayes 1996) or new experimental data (analytical comparison at T_c, extended q-sweep).





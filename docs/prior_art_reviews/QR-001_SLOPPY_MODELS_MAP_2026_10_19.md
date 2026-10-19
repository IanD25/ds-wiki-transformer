# QR-001 Literature Map — why is nature describable with so few parameters?

**Mode:** A (literature mapping, light). **Date:** 2026-10-19. **Status after this map:** Literature-mapped (partial). No gates run.
**Question (from the log):** Is there a measurable, domain-general signature of when a complex system admits a low-dimensional effective description, and when it does not?
**Companion:** [`../experiments/DFIG_REDUCTION_TEST_2026_10_19.md`](../experiments/DFIG_REDUCTION_TEST_2026_10_19.md), the same day's reduction test of the wiki's own effective-dimension (DFIG) thread.

**Headline.** The field's answer has two parts, and only one is settled.
- **Settled (mechanism, in two model classes):** for smooth least-squares models, approximation theory bounds the widths of the model manifold geometrically, so a few parameter combinations control predictions. For physical models under coarse-graining, irrelevant directions contract at rates set by their RG exponents.
- **Open, by the field's own statement:** why the same hierarchy appears in general probabilistic models, and whether the least-squares and RG explanations are one explanation or two. Quinn et al. 2023 say they "do not yet have an explanation for this in general" (§8.2).
- **The wiki's DFIG claims are not part of this literature.** Today's reduction test shows that the Phase 1 "Fisher rank = dimension" results are the Fisher information of a location family read through lattice symmetry. That is not a sloppy-model Fisher matrix, so the M0 framing ("P5 re-parameterises sloppy models") was too generous.

---

## How to read the reading markers

Each source carries its reading level as of this session. Markers are never upgraded without a new reading.
- **[abstract]** — abstract read (arXiv, Crossref, PMC).
- **[full text skimmed: §…]** — targeted questions asked of the full text through an automated reader, for the sections named. Weaker than reading end to end.
- **[read directly: …]** — the named passage extracted and read.
- **[metadata only]** — bibliographic record only.
- **[secondary]** — content known only through another paper that was read.

Verification was done by a sub-agent this session (notes kept in the session scratchpad); bibliographic details are from Crossref unless stated.

---

## 1. What is settled

### 1.1 The phenomenon: hierarchical Fisher spectra ("sloppiness")
- **Waterfall et al. 2006**, *PRL* 97, 150601 (doi:10.1103/PhysRevLett.97.150601) [abstract]. Models from systems biology, quantum Monte Carlo and curve fitting share a roughly flat density of log-eigenvalues of the Fisher matrix over many decades; linear regression and random matrices do not. Proposes a "sloppy universality class", reproduced by a Vandermonde ensemble in one limit (a model of the class, not a proof).
- **Gutenkunst et al. 2007**, *PLoS Comput. Biol.* 3, e189 (doi:10.1371/journal.pcbi.0030189) [abstract]. Systems-biology models universally have sensitivity eigenvalues spread over many orders of magnitude, so fits leave parameters poorly constrained while predictions can be tight.
- **Status: Established** as an empirical regularity. Quinn et al. 2023 §2.1 itself calls the ubiquity "an empirical fact", holding "in the cases studied so far" [full text skimmed: §2.1].

### 1.2 The geometry: model manifolds, widths and boundaries
- **Transtrum, Machta & Sethna 2010**, *PRL* 104, 060201, "Why are Nonlinear Fits to Data so Challenging?" (doi:10.1103/PhysRevLett.104.060201) [abstract], and **2011**, *PRE* 83, 036701 (doi:10.1103/PhysRevE.83.036701) [abstract]. The manifold of model predictions has widths and curvatures in a geometric series; fits stall near its boundaries. ("Hyperribbon" does not appear in either abstract; the coinage was not traced.)
- **Transtrum & Qiu 2014**, *PRL* 113, 098701 (doi:10.1103/PhysRevLett.113.098701) [abstract; PMC text queried for scope]. The manifold boundary approximation method (MBAM): follow a geodesic along the sloppiest direction to a boundary and take the limit, removing one parameter. Stated for general probabilistic models with a Fisher matrix; the authors present RG as one case.
- **Quinn, Wilber, Townsend & Sethna 2019**, *PRL* 122, 158302 (doi:10.1103/PhysRevLett.122.158302) [abstract]. Chebyshev approximation theory gives universal bounds on manifold widths for smooth models: **this is the settled explanation**, for smooth least-squares predictions.
- **Status: Established** for smooth least-squares models (Quinn 2019; Quinn 2023 §3). Not established beyond them (§2).

### 1.3 The RG link: coarse-graining compresses parameter space
- **Machta, Chachra, Transtrum & Sethna 2013**, *Science* 342, 604–607 (doi:10.1126/science.1238723; arXiv:1303.6738) [abstract; full text skimmed for how combinations are counted]. In a hopping model and a 2D Ising model, the microscopic Fisher matrix is not sloppy. Observed coarsely, the eigenvalues of irrelevant directions shrink and the relevant ones do not. The count of combinations that matter is described qualitatively ("a few stiff combinations"), not as a rank. Already in the wiki as **IT09**.
- **Raju, Machta & Sethna 2018**, *PRE* 98, 052112 (doi:10.1103/PhysRevE.98.052112) [abstract]. Covariant version: under RG, manifold distances along relevant directions are preserved and those along irrelevant directions contract at rates set by the RG exponents. Universality as information loss.
- **Bény & Osborne 2015**, *PRA* 92, 022330 (doi:10.1103/PhysRevA.92.022330; arXiv:1206.7004, 2012) [abstract]. **Quantum** information-geometric RG: RG as quantum channels, information loss as distinguishability of thermal states. Note for the wiki: this is quantum, not classical Fisher information, the same split already flagged for the Fisher–gravity chain.
- **Status: Established** for the models treated (lattice models with RG exponents, diffusion).

### 1.4 Effective dimension: the field avoids a single number
- **Transtrum et al. 2015**, *J. Chem. Phys.* 143, 010901 (**doi:10.1063/1.4923066**; arXiv:1501.07668) [full text skimmed: §§I, III, IV, VI, VII]. There is no sharp stiff/sloppy boundary (§I); eigenvalues alone do not establish a low effective dimension, because they depend on the parameterisation, and manifold widths compared with the noise are the better measure (§III).
- **Mattingly, Transtrum, Abbott & Machta 2018**, *PNAS* 115, 1760–1765 (doi:10.1073/pnas.1715306115; arXiv:1705.01166) [abstract; **read directly**: the d_eff definition around Fig. 4C]. The prior that maximises information learned from finite data is discrete and sits on manifold boundaries when data are poor. **d_eff = Σ_r r·Ω_r**, with Ω_r the prior weight on boundary pieces of dimension r. It rises from 0 towards the parameter count as noise falls. It is **not** a Fisher rank, an eigenvalue count or a participation ratio. **Mandatory citation** wherever the wiki writes "d_eff" (the wiki's `gloss_effective_dimension_mattingly` already records it).
- **Quinn, Abbott, Transtrum, Machta & Sethna 2023**, *Rep. Prog. Phys.* 86, 035901 (doi:10.1088/1361-6633/aca6f8; arXiv:2111.07176; online December 2022) [full text skimmed: §§1–8]. No scalar effective dimension defined in the parts read.
- **The exact rank of a Fisher matrix is the parameter count** whenever it is positive definite; "effective dimension" always needs a resolution (the noise floor, a prior). Standard derivation; for a d-dimensional location family the Fisher matrix is constant in θ and full rank d. *Source pointer unverified:* Cover & Thomas 2006 §11.10 [metadata only: section title]; Liu & Viswanath, arXiv:cs/0604028 [read directly: §1] define the translation Fisher matrix. Do not cite a Lehmann & Casella section until checked.

### 1.5 Monotonicity under processing
- **Zamir 1998**, *IEEE Trans. Inf. Theory* 44(3), 1246–1250 (doi:10.1109/18.669301) [metadata only; content **secondary** via Liu & Viswanath, read directly]. Data-processing inequality for Fisher information: J(Y; θ) ≤ J(X; θ) when the kernel from X to Y does not depend on θ. The matrix (Loewner) form is inferred from the secondary source's context. **This is the theorem T1 and P7 invoke.** It concerns processing the same data, not recomputing a new model on a coarse graph.

### 1.6 Adjacent explanations of "few parameters"
- **Lin, Tegmark & Rolnick 2017**, *J. Stat. Phys.* 168, 1223–1247 (doi:10.1007/s10955-017-1836-5; arXiv:1608.08225) [abstract]. Physics-type data have symmetry, locality, compositionality and polynomial log-probability, so they are cheap to approximate; depth helps for hierarchical generation, related to RG. A different route to "few parameters": properties of the Hamiltonians, not of the Fisher geometry.
- **Daniels, Chen, Sethna, Gutenkunst & Myers 2008**, *Curr. Opin. Biotechnol.* 19, 389–395 (doi:10.1016/j.copbio.2008.06.008) [abstract]. A large "sloppy neutral subspace" may give robustness non-adaptively and bears on evolvability.

---

## 2. What is open, and who says so

1. **Why probabilistic models are sloppy in general.** Quinn et al. 2023 §8.2: hyperribbon structure is seen in probabilistic models through intensive embeddings (InPCA, isKL) but not explained outside exponential families [full text skimmed: §8.2]. The rigorous bounds (Quinn 2019; Quinn 2023 §3) cover smooth least-squares models, mostly with one independent variable; Transtrum 2015 §III states the same limit [full text skimmed].
2. **One explanation or two.** Quinn 2023 §8.2: physics emergence (RG) and least-squares sloppiness (smoothness, approximation theory) seem to have different explanations; whether a unified theory exists is posed as a question [full text skimmed].
3. **Why the methods succeed at all.** Transtrum 2015 §VII asks openly, e.g. whether it is a selection effect of the models people build [full text skimmed].
4. **Definitions.** Jagadeesan, Raman & Tangirala 2023, *PLOS ONE* 18, e0282609 (doi:10.1371/journal.pone.0282609) [abstract and first ~60% skimmed]: sloppiness lacks a formal definition, depends on inputs and the region of parameter space, and its root cause is little studied.
5. **Sloppiness is not identifiability, and design can beat it.**
   - Chis, Villaverde, Banga & Balsa-Canto 2016, *Math. Biosci.* 282, 147–161 (doi:10.1016/j.mbs.2016.10.009) [abstract]: sloppy models can be identifiable.
   - Apgar, Witmer, White & Tidor 2010, *Mol. BioSyst.* 6, 1890–1900 (doi:10.1039/b918098b) [abstract]: five designed experiments pinned all parameters of a "sloppy" model. Comment by Chachra, Transtrum & Sethna 2011 and reply [metadata only].
   - White, Tolman, Thames, Withers, Mason & Transtrum 2016, *PLoS Comput. Biol.* 12, e1005227 (doi:10.1371/journal.pcbi.1005227) [abstract]: pinning every parameter can expose missing mechanisms and does not guarantee prediction.
   - Monsalve-Bravo et al. 2022, *Sci. Adv.* 8, eabm5952 (doi:10.1126/sciadv.abm5952) [abstract]: a Bayesian version separates prior-informed from data-informed stiff directions.
6. **Philosophy of explanation.** Freeborn, *Erkenntnis* 90, 645–673 (2025; online 2023; doi:10.1007/s10670-023-00728-w) [abstract only, from search excerpts]: sloppy models give at best a very partial explanation of the success of science.

**Not found:** a 2024–2026 physics paper claiming to solve the general probabilistic case. The search was light; that absence is weak evidence.

**Reading on QR-001's "what would decide it".** The log's decider ("eigenvalue-spectrum shape of the Fisher information, tested on model classes from different fields before fitting") is close to Waterfall 2006 and Gutenkunst 2007 (spectrum shape across fields), and the field itself warns that eigenvalues are parameterisation-dependent (Transtrum 2015 §III). The open problem is the explanation, items 1–2 above, not a new signature.

---

## 3. Where the wiki's DFIG claims sit

| Wiki claim | Relation to the literature | After the 2026-10-19 reduction test |
|---|---|---|
| **M6** Fisher information rank as D_eff | The Fisher matrix is textbook. "Rank = effective dimension" is not how the sloppy-models programme counts (§1.4). | Phase 1 graph validation: tori and coarse-graining are an exact closed form fixed by lattice symmetry; ER "rank 1" is the estimator's mean term; RGG "+1" unexplained. |
| **P5** rank = D_eff ("application of Machta 2013") | Phase 1's object has no model parameters: it is a location family over neighbour displacements. Machta 2013 is a vocabulary match, not the same object. | Torus "rank = d" = Fisher rank of a d-dimensional location family (§1.4), read through the hypercubic point group. RGGs give d + 1. |
| **P6** fractal dimension = Fisher rank | No literature support sought or found. | PR form falsified: kagome lattice (d_H = 2) gives PR 1.61, set by 60° neighbour angles. |
| **P7 / T1** monotonicity under coarse-graining | The valid form is Zamir 1998's DPI (§1.5): guaranteed, nothing to test. | Phase 1 recomputes on a new graph (DPI not engaged); the gap rank rises d → d + 1 under σ ∝ side, exactly. |
| **Ax2** D_eff := rank F(ℓ) | A definition. The sloppy-models literature deliberately avoids collapsing the spectrum to a number (§1.4). | Its cited evidence is forced, falsified or d + 1. |
| **OmD** Ω_D operator | No relation to this literature. | Definition (identity at D = 4 by construction). |
| **IT09** sloppy models (reference entry) | Faithful summary; its DOI for Transtrum 2015 (10.1063/1.4923066) is correct. | — |

**Wiki errors found (none applied):**
1. P5's anchor (id 100) carries DOI **10.1063/1.4918623**, which is an unrelated *Rev. Sci. Instrum.* paper on Raman thermal conductivity; the correct DOI is 10.1063/1.4923066. The anchor's note already records a 2026-10-18 correction; the identifier field itself still holds the wrong DOI. Owner to decide whether to append a corrected anchor row.
2. CLAUDE.md and M0 cite "Quinn et al. 2022" and "Quinn 2023" for the same review; both are right (online December 2022, volume 86 is 2023). Cite by volume.
3. Bény & Osborne 2015 is quantum; if any entry cites it as classical Fisher RG, that is the `vocabulary-stacking-analogy` pattern.

---

## 4. Suggested next steps (not done)

- **Gate QR-001** (both gates). Likely outcome: Gate 1 `open-in-literature` (Quinn 2023 §8.2 frames the open part), and the wiki has no new angle on it now that DFIG has reduced. Probably **FOLD** for the wiki-specific version and a record of the open problem as `open_in_literature`.
- Read Quinn 2023 §8.2 and Transtrum 2015 §III end to end, to upgrade those markers honestly.
- Optional fold-in: reference entries for Quinn 2019 (Chebyshev bounds) and Raju 2018 (geometric RG information loss), which the wiki lacks.

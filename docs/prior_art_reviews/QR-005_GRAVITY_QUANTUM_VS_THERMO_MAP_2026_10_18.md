# QR-005 literature map — is gravity quantum, or thermodynamic? (2026-10-18)

> **Provenance (2026-10-18).** Mode A, literature mapping only. This is the map for Questions Raised Log entry **QR-005**, un-parked today at the owner's request. Following the deep-research pattern, the search was fanned out across seven read-only research sub-agents:
> 1. thermodynamic and entropic derivations of gravity;
> 2. critiques of entropic gravity, and tests of Verlinde 2016;
> 3. gravitationally mediated entanglement (BMV): the proposals, the interpretation debate and the roadmap;
> 4. classical, stochastic and collapse models, with their bounds;
> 5. free-energy (entropic) models with force-noise predictions;
> 6. black-hole thermodynamics as the bridge;
> 7. what current experiments constrain, with numbers.
>
> The main session read the wiki's gravity entries directly from `ds_wiki.db`: GT01–GT07, GT10, GT11, HB01–HB05, HB07, HB09, BR01–BR05, GT08, IT02–IT05 and the links among them. It also read their anchors in `wiki_history.db`, read-only. It then re-checked the load-bearing citations itself; see column "MS" in §I.
>
> **Sub-agent summaries are leads, not readings.** §I gives each source's reading marker as reported, never upgraded. The sub-agents' notes are kept outside the repo, in the session notes folder (`research_notes/Gravity quantum or thermodynamic/`, files 1–7).
>
> **No gate has been run, and nothing has been written to the databases.** Confidence tags: **Established / Supported / Speculative**.

---

## (A) The answer in plain terms

**For the owner, in one paragraph each.**

- **"Quantum or thermodynamic" is mostly a false choice.** Every thermodynamic or entropic derivation of gravity uses quantum inputs: Jacobson 1995 and 2016, Verlinde 2011, Padmanabhan and Sakharov all do. Those inputs are:
  - the Unruh or Hawking temperature, which contains ħ;
  - an entropy per unit horizon area that fixes G = 1/(4ħη);
  - the entanglement of the quantum vacuum;
  - or a one-loop quantum effective action.

  What these programmes claim is that Einstein's equation behaves like an *equation of state*, not a fundamental field equation. They do not claim that gravity is classical. None of their authors says so, and Jacobson 1995's own analogy (sound waves in air) points the other way: sound is quantized, as phonons. So a thermodynamic origin for the field equations is compatible with gravitons, as collective modes. The real dividing line is a different one: *can the gravitational field carry quantum information?*
- **That question is now experimental, but not yet decidable.** There are two routes.
  - **Entanglement.** If two masses, each in a superposition of two places, become entangled through gravity alone, gravity cannot be a classical channel. This is the Bose–Marletto–Vedral (BMV) test.
  - **Noise.** Any gravity that *cannot* entangle must add a minimum amount of force noise or decoherence. A clean enough noise measurement can therefore do the same job.

  No experiment has done either. The gaps are large:
  - the heaviest object put in a two-place superposition is about 7.5 orders of magnitude too light;
  - the smallest mass whose gravity has been measured (90 mg) is about 10 orders too heavy;
  - mm-scale force sensors are about 9 orders too noisy for the noise route.

  No published roadmap commits to a date.
- **Even a positive entanglement result would not prove gravitons.** It would rule out gravity acting as a *local classical* channel. That covers Kafri–Taylor–Milburn, mean-field gravity and Oppenheim's classical gravity. But an instantaneous Newtonian interaction, a non-local collapse model (Diósi–Penrose, per Trillo & Navascués 2025) or, contestedly, classical gravity acting on quantum fields (Aziz & Howl 2025) can also entangle. Going from "not classical" to "gravitons" needs extra assumptions: locality, or Lorentz invariance and unitarity. The field says this openly.
- **Some classical and thermodynamic options are already squeezed or ruled out.**
  - The parameter-free Diósi–Penrose collapse model is excluded (Donadi et al. 2021).
  - The pairwise classical-channel model is excluded by atom interferometry (Altamirano et al. 2018).
  - Oppenheim's "noise everywhere" variant is excluded. His other variants survive in windows of roughly 9–31 orders of magnitude, depending on the variant and on whose numbers you use.
  - The free-energy models of Carney et al. 2025: the non-local version with zero suppression length is excluded, and the local version survives only in a narrow window of lattice spacing, roughly 10–100 μm. That window comes from a single-group preprint.
- **What this means for the wiki.** The wiki's gravity strand has the same kind of error QR-004 found for Landauer: a correct result applied beyond its scope. Here the result is a thermodynamic or entropic derivation of the field equations, and the overreach is reading it as "gravity is not quantum" or "no gravitons". §F lists 27 items; 16 contain at least one outright error, including three wrong anchors (two on GT02, one on HB09). The proposed new drift tag is `emergent-read-as-classical`, alongside the existing `vocabulary-stacking-analogy`. The wiki also has **no entries** on the experimental side of the question (BMV, Diósi–Penrose, Oppenheim, classical-channel models, semiclassical gravity), so the QR-005 log line "Coverage is good" is wrong.

**Calibrated summary.**

| Claim | Tag |
|---|---|
| Black-hole thermodynamics, and every thermodynamic derivation of Einstein's equation, uses ħ-dependent quantum inputs | **Established** |
| These derivations are silent on whether the gravitational field is quantized; none of their authors claims gravity is classical | **Supported**: assembled from the primary texts; no single proponent sentence says it outright |
| Gravity cannot be a *pairwise local classical channel* (Kafri–Taylor–Milburn type) | **Established**: excluded by existing atom-interferometry data (Altamirano et al. 2018) |
| Parameter-free Diósi–Penrose collapse is excluded; DP survives with R₀ as a free parameter, R₀ > 4.5 × 10⁻¹⁰ m | **Established** for the Markovian model |
| A positive BMV witness would rule out LOCC-type classical gravity | **Supported**: broad agreement; Aziz & Howl 2025 dissent, with at least seven rebuttals |
| A positive BMV witness would prove gravitons exist | **Speculative**: needs locality or S-matrix assumptions; openly debated |
| A BMV-type test is feasible within a stated time | **No sourced estimate exists**; the gaps are 7.5–10 orders of magnitude on different axes |

---

## (B) Settled — Established

1. **Black-hole thermodynamics needs ħ, but only through quantum matter on a classical spacetime.** Classical GR gives four laws that only *resemble* thermodynamics: classically a black hole's temperature is absolute zero.
   - Hawking's T = ħκ/2πck_B comes from quantum fields outside the horizon, and the calculation uses no gravitational field equations (Wald 2001, *Living Rev. Rel.* 4:6, §§2–3).
   - Once T is fixed, the first law fixes S = k_B c³A/(4Għ).
   - Classical gravity fixes only the product: T_H·S_BH = Mc²/2 for Schwarzschild, with ħ cancelling (main session's arithmetic).
2. **Exact microstate counts reproduce A/4 only for special black holes:**
   - five-dimensional extremal BPS black holes (Strominger & Vafa 1996) and their string-theory successors;
   - BTZ/AdS₃ via the Cardy formula;
   - extreme Kerr under the Kerr/CFT assumptions (Guica et al. 2009), where the duality itself is conjectural.

   No count derives A/4 for Schwarzschild or ordinary astrophysical Kerr. Loop quantum gravity derives S ∝ A but **calibrates** the 1/4 through the Immirzi parameter (Ashtekar, Baez, Corichi & Krasnov 1998; Wald 2001 §5).
3. **The Bekenstein bound S ≤ 2πER/ħc contains no G.** In Casini's 2008 form (positivity of a vacuum-subtracted relative entropy) it holds automatically in flat-space quantum field theory and avoids the species problem. It is a QFT statement motivated by a black-hole argument. The *holographic* bound S ≤ A/4 is the gravitational one; it fails as a general spacelike statement and is replaced by Bousso's covariant bound.
4. **Jacobson 1995 derives Einstein's equation from four inputs:**
   - δQ = T dS on every local Rindler horizon;
   - entropy ∝ area;
   - the Unruh temperature T = ħκ/2π;
   - local equilibrium (vanishing expansion and shear at the point).

   Λ enters as an arbitrary constant from energy conservation and the Bianchi identity, "as enigmatic as ever" (full text, MS). His remark concerns *canonically* quantizing the Einstein equation, not whether gravity is quantum (abstract, MS). Out of equilibrium the derivation needs entropy-production (viscosity) terms (Eling, Guedens & Jacobson 2006).
5. **Jacobson 2016 links the *semiclassical* Einstein equation to maximal vacuum entanglement:**
   - **Scope:** for first-order variations of the local vacuum, exactly for conformal fields; for non-conformal fields "modulo a conjecture" (abstract, MS).
   - **Contested:** that conjecture fails for some relevant operators (Casini, Galante & Myers 2016; Speranza 2016).
   - **Other ingredients:** it uses no holography or Ryu–Takayanagi, and takes no position on gravitons (sub-agent full text).
6. **Quantum matter obeys the Schrödinger equation in an external gravitational field.** Tested by neutron interferometry (COW 1975), quantized neutron states (Nesvizhevsky et al. 2002), qBounce, equivalence-principle tests with superposed atoms (~10⁻¹²), the gravitational Aharonov–Bohm effect (Overstreet et al. 2022) and atoms held for ~70 s near a small source mass (Panda et al. 2024). **None of these puts the *source* in a superposition, so none can tell a quantum field from a classical one.** That is a logical point, not a gap in precision.
7. **Gravity is not a pairwise local classical channel.** The Kafri–Taylor–Milburn model forces a minimum decoherence rate. For a 0.54 m rubidium superposition it predicts a coherence time of ~2 × 10⁻³ s, and the observed visibilities exceed its predictions by factors of 2.5 to 10¹⁸ (Altamirano et al. 2018, *CQG* 35:145005; abstract MS, sub-agent full text).
8. **Parameter-free Diósi–Penrose is excluded.** Spontaneous-radiation searches give:
   - R₀ > 0.54 × 10⁻¹⁰ m at 95% probability (Donadi et al. 2021, *Nat. Phys.* 17:74), against Penrose's natural R₀ = 0.05 × 10⁻¹⁰ m for germanium (full text, MS);
   - R₀ > 2.54 × 10⁻¹⁰ m (Majorana Demonstrator, after the 2023 erratum; search summary);
   - **R₀ > 4.9 × 10⁻¹⁰ m at 90% C.L., and > 4.5 × 10⁻¹⁰ m at 95% C.L.** (XENONnT, *PRL* 136:120201, 2026; full text, MS).

   This applies to the Markovian model; dissipative and coloured-noise variants evade it.
9. **No graviton has been detected.** The gravitational-wave bound on a graviton mass, m_g ≤ 1.92 × 10⁻²³ eV/c² (GWTC-4.0, 90%; abstract), tests a dispersion relation, not quantization. Single-graviton "clicks" would be explainable by classical waves (Carney, Domcke & Rodd 2024, *PRD* 109:044009; abstract MS).

---

## (C) Measured or constrained — which experiment, and how tight

| Hypothesis or model | Constraint | Source | How tight |
|---|---|---|---|
| Pairwise local classical channel (Kafri–Taylor–Milburn 2014) | Atom-interferometer visibilities far exceed its minimum decoherence | Altamirano et al. 2018 | **Excluded** |
| Diósi–Penrose, parameter-free | Underground X-ray/γ searches | Donadi 2021; XENONnT 2026 | **Excluded**, by ~90× in R₀ |
| Diósi–Penrose, free R₀ | R₀ > 4.5 × 10⁻¹⁰ m (95% C.L.); "effective collapse" requires R₀ ≲ 10⁻⁴ m (Figurato et al. 2024, partly arbitrary) | XENONnT 2026; Figurato 2024 | Window ~5.5 orders of magnitude |
| Oppenheim classical-quantum gravity, ultra-local continuous kernel | Torsion balances give D₂ ≤ 10⁻⁴¹ kg² s m⁻³; interferometry requires D₂ ≥ 10⁻²⁴ | Oppenheim et al. 2023, *Nat. Commun.* 14:7910 (full text, MS) | **Excluded** (bounds contradict) |
| Oppenheim, discrete (jump) kernel | 10⁻¹ ≥ (l_P³/m_P)D₂ ≥ 10⁻²⁵ kg s (original) | same | ~24 orders open (original) |
| Oppenheim, non-local (DP-kernel) | 10⁻⁹ ≥ l_P²D₂ ≥ 10⁻⁴⁰ kg² s m⁻¹ (original) | same | ~31 orders open (original) |
| Oppenheim, both surviving kernels, re-bounded | Upper bound ≥15 orders lower from existing force-noise experiments; up to 25 orders if LISA Pathfinder and atom interferometry apply, which the authors themselves doubt | Janse et al. 2024, *PRR* 6:033076 (abstract and text, MS) | Conservative windows ~9 and ~11 orders (sub-agent). **Janse's and Oppenheim's window figures do not reconcile; check the published versions before quoting.** |
| Carney et al. 2025 non-local free-energy model | Atom interferometry excludes λ = 0; requires λT² ≳ 10⁻¹⁴ J; no upper bound on λ known; at large λ it is indistinguishable from graviton exchange | *PRX* 15:031038 (fetch, MS; sub-agent full text) | λ = 0 **excluded**; the rest is not falsifiable by noise alone |
| Carney et al. 2025 local (lattice) model | Fifth-force tests exclude a ≳ 1 mm (paper); force noise requires a ≳ ~10 μm (LISA Pathfinder, sub-agent arithmetic; agrees with Fabiano et al. 2026) | Carney 2025; Fabiano, Fujita, Matsumura & Carney 2026 (preprint) | Window ~10–100 μm (single group, not peer-reviewed) |
| Mean-field (Schrödinger–Newton) semiclassical gravity | With standard collapse it permits faster-than-light signalling; Page & Geilker 1981 refutes only the no-collapse version | Bahrami et al. 2014 | Excluded **on consistency grounds**, not by experiment |
| Verlinde 2016 emergent gravity (apparent dark matter) | Solar-system perihelia off by ~7 orders (Hees et al. 2017); clusters excluded at >5σ (Halenka & Miller 2020); radial-acceleration-relation tension (Lelli et al. 2017); lensing mixed (Brouwer 2017, 2021) | sub-agent, INSPIRE-checked | Weak-field formula as published is **disfavoured to excluded** |
| Inverse-square law at short range | No gravitational-strength Yukawa force above ~38.6 μm (95% C.L.) | Lee et al. 2020, *PRL* 124:101101 (abstract) | Constrains any lattice or screen model with an O(1) deviation above tens of μm |

**The mass gap** (main session's check of the sub-agents' arithmetic):

| Axis | Best achieved | BMV target (Bose et al. 2017) | Gap |
|---|---|---|---|
| Mass in a two-place superposition | ~2.8 × 10⁻²² kg (sodium clusters >170 kDa; Pedalino et al., arXiv 2025 abstract MS; Nature 2026 per search) | ~10⁻¹⁴ kg | ~7.5 orders |
| Delocalisation of a levitated nanoparticle | ~70 pm (Rossi et al. 2025; press figure) | ~250 μm | ~6.5 orders |
| Smallest *source* mass whose gravity has been measured | 90 mg (Westphal et al. 2021; abstract MS) | ~10⁻¹⁴ kg, in superposition | ~10 orders; no source has ever been delocalised |
| Force noise at mm separation (noise route) | ~4 × 10⁻⁹ m s⁻²/√Hz (Westphal); ~1 × 10⁻⁹ (Fuchs et al. 2024, 0.43 mg levitated) | ~10⁻¹⁸ m s⁻²/√Hz (the non-entangling threshold at d ≈ 1 mm, Fabiano 2026; Carney's λ = 0 floor) | ~9 orders |

Carney et al. call the λ = 0 noise level "nearly observable" (MS, fetch). On the arithmetic above that wording is optimistic by about 10⁹. λ = 0 is already excluded, so the surviving models predict even less noise.

---

## (D) Open — and who frames it as open

1. **What a positive entanglement witness would prove.**
   - **Agreed:** it excludes LOCC-type classical gravity.
   - **Disputed:** whether it shows the field has quantum degrees of freedom, or that gravitons exist.
     - Deflationary side: Anastopoulos & Hu 2018; Hall & Reginatto 2018; Fragkos, Kopp & Pikovski 2022; Martín-Martínez & Perche 2023; Huggett, Linnemann & Schneider 2022.
     - Strengthening side: Christodoulou & Rovelli 2019; Belenchia et al. 2018; Danielson, Satishchandran & Wald 2022; Carney 2022 (which gets "massless bosons universally coupled to mass" and leaves spin-0 open); Galley, Giacomini & Selby 2022 (a no-go theorem given a mediation premise); Christodoulou et al. 2023 (a delayed entanglement signal as the sharp test).
   - **No consensus statement exists** (sub-agent, 2024–26 search). The main review is Bose et al., *Rev. Mod. Phys.* 97:015003 (2025).
2. **Can classical gravity entangle after all?**
   - Trillo & Navascués 2025 (*PRD* 111:L121101) show Diósi–Penrose dynamics can entangle two masses closer than a critical distance (abstract, MS).
   - Aziz & Howl 2025 (*Nature*) claim classical gravity entangles quantum-field matter through local processes (abstract, MS). At least seven 2025–26 rebuttals followed: Marletto–Vedral; Marletto–Oppenheim–Vedral–Wilson; Diósi; Schneider–Huggett–Linnemann; Gundhi–Infantino–Bassi; Xue et al.; Tibau Vidal–Iyer. No published reply was found.
   - Unresolved in print. Most of the published response is against the claim.
3. **How much room is left for classical-quantum gravity.** The kernel family is open by construction: ruling out "classical gravity" means ruling out kernels one by one. Framed by Oppenheim et al. 2023 and Janse et al. 2024. Grudka et al. 2024 leave open whether renormalisation preserves complete positivity.
4. **Whether a noise measurement can replace the entanglement test.** Kafri & Taylor 2013 and Fabiano et al. 2026 (preprint) argue that any non-entangling Newtonian gravity must inject a minimum noise, so measuring below that threshold would be equivalent to demonstrating entanglement. Lami, Pedernales & Plenio 2024 (*PRX* 14:021022) give an LOCC inequality that needs no delocalisation (abstract, MS). Open: the threshold's generality, and whether anyone can reach it.
5. **What black-hole entropy counts.** Either quantum-gravitational microstates (string theory, loop quantum gravity) or entanglement of quantum matter with G itself induced (Jacobson 1994; Sakharov). No observation discriminates between them. Wald 2001 and Carlip 2014 list the nature of the microstates and the "universality" of A/4 as open.
6. **Timeline.** No published date. The only sourced phrase is Plávala (*PRD* 2026): optimistic projections place the experiment "outside of the short-term future" (search summary). A late-2025 preprint finds current ground-based designs short by a factor of 4–5 and points to space (search summary).

   > **Note 2026-10-19 (QR-005 gates, [`QR-005_GATES_2026_10_19.md`](QR-005_GATES_2026_10_19.md) §5).** This quotes only Plávala's background sentence. His paper (full text read 2026-10-19; DOI 10.1103/87dc-qt73) argues that today's matter-wave interferometers could establish gravity-mediated entanglement *indirectly*. The argument is: verify the Schrödinger equation for a single delocalised mass interacting with an external mass, then infer entanglement under one of two assumptions (a ~20 g mass delocalisable with exchange-symmetric dynamics; or an interaction depending only on m₁m₂). He calls theory, not experiment, the main bottleneck. *The text above is unchanged.*

---

## (E) What the wiki holds, and its gaps

**Holdings (thermodynamic and holographic side; extensive):**
- **Gravity-from-thermodynamics:** GT01 Jacobson 1995, GT02 Verlinde 2011, GT03 Padmanabhan, GT04 Bianconi, GT05 Carney et al. 2025 (corrected 2026-10-18), GT06 Sakharov, GT07 non-equilibrium spacetime thermodynamics, GT08 equivalence principle, GT10 Jacobson 2016;
- **Holographic bounds:** HB01–HB10;
- **Bridges:** BR01–BR05;
- **Information-theory entries the Fisher–gravity chain runs through:** IT02–IT05.

Anchors are in place for all of them (GT02 carries six, including the Kobakhidze and Visser critiques).

**Gaps (the experimental side of QR-005; empty):**
- no entry for gravitationally mediated entanglement (BMV) or its interpretation debate;
- no classical-channel or LOCC gravity (Kafri–Taylor–Milburn; Altamirano 2018);
- no Oppenheim classical-quantum gravity or decoherence–diffusion trade-off;
- no Diósi–Penrose collapse or its underground bounds;
- no semiclassical (Schrödinger–Newton) gravity, Page–Geilker or Tilloy–Diósi;
- no minimum-noise theorems or entanglement-free tests (Kafri–Taylor 2013; Lami–Pedernales–Plenio 2024);
- no entry for quantum matter in external gravity (COW, qBounce, the Aharonov–Bohm and Panda results), nor for what such experiments cannot show;
- no mass-gap or experimental-state entry (Westphal; Fuchs; Pedalino);
- no graviton-detectability entry (Dyson; Carney–Domcke–Rodd);
- no scope statement for microstate counting;
- no Page curve or islands;
- no Verlinde 2016 as its own entry; GT02 mixes the two theories;
- no compatibility literature on emergent gravity (Sindoni 2012; Carlip 2014; Weinberg–Witten).

The QR-005 log line "Coverage is good" holds only for the thermodynamic side.

**Not re-audited here:** GT11, P17 and P23 (cosmological coupling). They were corrected earlier today and sit outside the tabletop question.

---

## (F) Wiki errors found, with proposed corrections

*Proposals only: nothing is applied. Severity: **E** = wrong, **Q** = needs qualifying, **H** = hygiene. "MS" = checked by the main session against the source; otherwise a sub-agent reading (see §I) or the main session's own reasoning, as stated.*

| # | Entry / field | Claim as written | Verdict | Proposed correction | Source |
|---|---|---|---|---|---|
| 1 | GT10 "What The Math Says"; GT10 "What It Claims" | "gravity is not a fundamental force transmitted by gravitons; it is the condition for equilibrium of quantum entanglement"; "No temperature, no heat, no thermodynamics — just entanglement structure" | **E** | Jacobson 2016 derives the *semiclassical* Einstein equation. It leaves gravitons out of the entanglement count to avoid double counting and takes no position on whether they exist. It uses the vacuum modular Hamiltonian with T = ħ/2π, and calls δS = (2π/ħ)δ⟨K⟩ "the usual Clausius relation". So temperature is present, and the result is silent on quantization. Tag `emergent-read-as-classical`. | Jacobson 2016 (abstract MS; full text, sub-agent) |
| 2 | GT10 Mathematical Form and cross-ref to GT01; link GT10→GT01 "generalizes"; also `CCA_GRAVITY_FINDINGS.md` §1.1 Hop 4 | "GT10 is the quantum-informatic generalization of GT01"; "the 1995 result is the classical-thermodynamic limit of the 2016 entanglement-equilibrium derivation"; Hop 4: "Jacobson 2016 explicitly recovers Jacobson 1995 as the classical limit" | **E** | Jacobson 2016 contains no such statement. Neither derivation is classical: 1995 uses T = ħκ/2π and G = 1/4ħη. They are two different semiclassical derivations: Clausius on local Rindler horizons, and entanglement stationarity in small causal diamonds. Hop 4's "zero additional assumptions" falls with it. | Jacobson 1995 (full text MS); Jacobson 2016 (full text, sub-agent) |
| 3 | GT10 Constraint Category; link GT10→HB07 "derives from" | The Ryu–Takayanagi formula "is promoted from a static holographic identity to a dynamical principle" | **E** | Jacobson 2016 says it uses no holography; Ryu–Takayanagi is not invoked. The area term is the *assumed* finite, universal UV entanglement density η, whose match to 1/4ħG is a consistency check. Re-type the link as `analogous to`, or describe the holographic results (Faulkner et al. 2014) as parallel work. | Jacobson 2016 (full text, sub-agent) |
| 4 | Link 855 GT10→IT03 "couples to"; GT10 cross-ref to IT03 | "GT10's stationarity condition δS_EE = 0 is equivalent to δD_KL = 0 at the vacuum state" ("around the maximally entangled vacuum state") | **E** | Three faults. (a) The relevant quantity is *quantum* relative entropy, not classical KL (IT03). (b) The first-order variation of relative entropy around the reference state vanishes identically, for any state: this is the first law of entanglement, δS = δ⟨K⟩, which holds whether or not the Einstein equation does. The Einstein content comes from balancing the *area* variation against it. (c) The vacuum is not "maximally entangled"; the hypothesis is maximal entanglement entropy at fixed volume. This is hop 3 of the Fisher–gravity chain. Tag `vocabulary-stacking-analogy`. | Main session's reasoning (Supported); Casini–Galante–Myers 2016 (sub-agent full text: "first law of entanglement") |
| 5 | GT10 Mathematical Form | "This IS the Einstein equation: G_ab + Λg_ab = 8πG T_ab", unqualified | **Q** | Add: with ⟨T_ab⟩ (semiclassical), for first-order state variations, exactly only for conformal fields. Non-conformal fields need a conjecture that fails for some relevant operators unless the reference curvature depends on the ball size (v4 of the paper). Coherent states remain a problem (Varadarajan 2016, cited by Jacobson). | Jacobson 2016 abstract (MS); CGM 2016, Speranza 2016 |
| 6 | GT01 "What The Math Says" | Λ "appears as an undetermined integration constant, exactly as in the standard derivation from the Einstein-Hilbert action" | **E** | In the Einstein–Hilbert action Λ is a parameter of the action. In Jacobson 1995 it is an arbitrary constant forced by energy conservation and the Bianchi identity ("remains as enigmatic as ever"). That is the unimodular structure: Alonso-Serrano & Liška 2020 argue the thermodynamic route gives unimodular (Weyl transverse) gravity. | Jacobson 1995 (full text MS); Alonso-Serrano & Liška 2020, *PRD* 102:104056 (abstract, sub-agent) |
| 7 | GT01 "What It Claims", Constraint Category | "gravity may not be a fundamental force but rather an emergent thermodynamic phenomenon"; "This is not an analogy: it is an exact mathematical derivation"; "the geometric content (curvature) equals the thermodynamic content (entropy production) at every point" | **Q** | (a) "Exact" holds only given four inputs, two of them quantum (ħ), plus local equilibrium. (b) The derivation *assumes no entropy production* (expansion and shear vanish at the point). Production terms appear only out of equilibrium (GT07; EGJ 2006). (c) Add Jacobson's own scope: it may not be right to *canonically* quantize the Einstein equation, "even if" the phenomenon is ultimately quantum. His sound analogy permits graviton-like collective quanta, as phonons are. Tag `emergent-read-as-classical`. | Jacobson 1995 (full text MS); EGJ 2006 (sub-agent full text) |
| 8 | GT01 DS cross-ref to TD3 | "The Clausius relation δQ = TdS is a consequence of the second law applied locally" | **Q** | δQ = TdS is the *reversible*, equilibrium equality; the second law gives the inequality dS ≥ δQ/T. Jacobson calls it "the fundamental relation" and requires local equilibrium; the non-equilibrium form is dS = δQ/T + d_iS (GT07). | Jacobson 1995 (MS); EGJ 2006 |
| 9 | GT02 status paragraph; GT02 anchors | "Hossenfelder & collaborators 2017 (JHEP 11, 007 'Inconsistencies in Verlinde's emergent gravity')". Anchor "Hossenfelder 2017 - Inconsistencies…" (doi:10.1007/JHEP11(2017)007). Anchor "Hossenfelder 2017 - A covariant version…" (arxiv:1706.07854) | **E** (attribution) | JHEP 11 (2017) 007 is by **Dai & Stojkovic**. arXiv:1706.07854 is Dai & Stojkovic's "A note on a covariant version…", published as *PRD* 96:108501 and already anchored separately. Hossenfelder's own paper is arXiv:1703.01415, *PRD* 95:124018. Fix the prose and both anchor titles; add Hossenfelder's paper with its own DOI. | Crossref and arXiv metadata (MS) |
| 10 | GT02 status paragraph | Positive evidence: Brouwer et al. 2017 agreement "WITHOUT free parameters" | **Q** | Brouwer tested **Verlinde 2016** ("Emergent Gravity and the Dark Universe"), a different theory from the entry's Verlinde 2011 entropic force. Brouwer's own caveats: static, spherically symmetric point mass; ΛCDM background; "a first step". The negative results are missing: Lelli, McGaugh & Schombert 2017; Hees, Famaey & Bertone 2017 (*PRD* 95:064019, perihelia off by ~7 orders); Halenka & Miller 2020 (*PRD* 102:084007, >5σ in clusters); Brouwer et al. 2021 (*A&A* 650:A113, mixed, with a ≥6σ difference between early- and late-type galaxies). Recommend a separate Verlinde 2016 entry (§G R13). | Sub-agent (INSPIRE-checked); Verlinde 2016 abstract |
| 11 | GT02 status paragraph | Kobakhidze 2011: "quantized gravitational states observed in the GRANIT ultra-cold-neutron experiment are inconsistent with an entropic-force derivation"; Visser 2011: "require unphysical entropy structures and multiple temperature baths" | **Q / H** | The experiment is Nesvizhevsky et al. 2002 (*Nature* 415:297, ILL). Add that the argument is contested: Chaichian, Oksanen & Tureanu 2011 (*PLB* 702:419); Kobakhidze's reply (arXiv:1108.4161) is unpublished. It has since become a bound on entropic-force *noise* (Schimmoller et al. 2021, *PRR* 3:033065: compatible with qBounce for σ ≳ 250), not a no-go for every entropic model. Visser: a conservative n-body force needs n(n−1)/2 heat baths, which he calls "baroque", not "unphysical". He states that Jacobson's and Padmanabhan's versions are not directly affected. | Kobakhidze abstract (MS); sub-agent (abstracts) |
| 12 | GT02 What It Claims and Mathematical Form | Newton's law from "the Bekenstein bound for information on holographic screens"; "gravity is not mediated by a graviton" | **Q** | ΔS = 2πk_B mcΔx/ħ is Verlinde's *postulate*, motivated by Bekenstein's thought experiment; it is not the Bekenstein bound. G is *defined* through N = Ac³/Għ, as Verlinde says, so Newton's law is largely an input. The 2011 paper never mentions gravitons: it says gravity is not a *fundamental* force and that closed strings must be emergent. Tag `emergent-read-as-classical`. | Verlinde 2011 (abstract MS; full text via fetch, sub-agent) |
| 13 | GT03 "What It Claims", "What The Math Says" | At N_sur = N_bulk "expansion halts" | **E** | Only the **Hubble volume** stops changing. That is de Sitter space, which expands exponentially. The entry contradicts itself ("approaches de Sitter"). N_bulk is defined with a sign factor ε and is positive only with the stated convention. The equation is algebraically the Friedmann acceleration equation, and Padmanabhan himself warns against counting re-expressions as insight. | Padmanabhan 2012 (abstract MS; full text, sub-agent) |
| 14 | GT03 c-theorem passages; GT03 cross-ref to GT10 | "The structural parallel to the Zamolodchikov c-theorem is exact"; GT10 "is the microscopic foundation for Padmanabhan's holographic equipartition" | **Q** | No theorem: there is no monotone c-function or proof here, only an analogy. No source makes the GT10 claim; Jacobson 2016 does not mention Padmanabhan's equipartition. Label both as internal analogies. Tag `vocabulary-stacking-analogy`. | Main session; Jacobson 2016 (sub-agent full text) |
| 15 | GT03 "What It Claims" and Concept Tags | The c-theorem paragraph appears twice; six concept tags are duplicated | **H** | Deduplicate. | Direct read |
| 16 | GT04 "What It Claims", Mathematical Form, "What The Math Says"; link 747 GT04→IT05 "derives from" | "Gravity = curvature of the Fisher-Rao metric on quantum state space"; "network-native"; "treats gravitational dynamics as optimal transport"; the quantum Fisher matrix "becomes the spacetime metric" | **E** (per abstract; **verify** against full text) | Bianconi 2025's action is the quantum relative entropy between the *spacetime metric, treated as an operator* ("effective density matrix"), and the metric induced by matter fields (Dirac–Kähler form). The modified equations reduce to Einstein's equations with Λ = 0 at low coupling, and an auxiliary "G-field" gives a small positive Λ. The abstract has no Fisher metric on a state space, no network and no optimal transport. It presents a classical field theory whose quantization "could bring new insights". So "quantum relative entropy" here does not make gravity quantum. Tag `vocabulary-stacking-analogy`. | Bianconi 2024/25 arXiv:2408.14391 abstract (MS) |
| 17 | GT06 Constraint Category, Mathematical Form | "Thermodynamic (Th) … a thermodynamic/statistical effect"; "1/G_ind = (c³/ℏ)·Σ N_s ∫ dk/16π²" | **Q / E** (formula) | Induced gravity is a **one-loop quantum** (order ħ) effect of matter fields on a classical background. The heat-kernel coefficient of R is *quadratic* in the cutoff (1/G_ind ~ N_s ħ κ²/c³ up to O(1) factors), not linear as ∫dk gives. "Established" fits the one-loop generation of an R term; gravity being *wholly* induced is Speculative. On S_ent = A/4G_ind: the match holds for minimally coupled spin-0 and spin-½ fields; spin-1 fields add a horizon contact term (Kabat 1995). Tag `emergent-read-as-classical`. | Visser 2002 *MPLA* 17:977 (sub-agent full text); Kabat 1995 (abstract) |
| 18 | GT07 "What It Claims", "What The Math Says"; notation | Chirco & Liberati 2010 give spacetime "an effective bulk viscosity"; σ used for both shear and entropy production | **E / H** | Eling, Guedens & Jacobson 2006 already contain both terms. f(R) *requires* a bulk viscosity 3ħαf/4π; pure GR with shear carries a **shear** viscosity 1/16πG (η/s = ħ/4π). Chirco & Liberati identify the GR shear term with Hartle–Hawking tidal heating and extend it to f(R). Use different symbols for shear and entropy production. Label the Jarzynski, Crooks and Seifert parallels as analogies (`vocabulary-stacking-analogy`). | EGJ 2006; Chirco–Liberati 2010 (sub-agent full text) |
| 19 | HB01 "What It Claims", "What The Math Says" | "nature has a finite information density: there is a maximum number of bits per unit volume"; "the bound arises from requiring that the system not form a black hole" | **E / Q** | The Bekenstein bound scales with E·R, with no cap per volume, and contains no G. Casini 2008 shows a well-defined form holds automatically in flat-space QFT. The "do not form a black hole" argument gives the spherical or holographic bound S ≤ A/4 (Susskind 1995), a different bound that scales with area. | Casini 2008 abstract (MS); sub-agent |
| 20 | HB02 "What It Claims"; HB02 cross-ref to IT02; IT02 cross-ref to HB02; link HB02→IT02 | "reproduced by string theory microstate counting (Strominger & Vafa, 1996)"; "now understood to equal the entanglement entropy … whose von Neumann entropy exactly equals A/4l_P²" | **E** (second clause) / **Q** (first) | Strominger–Vafa covers a class of 5D extremal BPS black holes only. No exact count exists for Schwarzschild or astrophysical Kerr, and loop quantum gravity calibrates the 1/4. Entanglement entropy across a horizon is UV-divergent and depends on the cutoff and the number of species. It matches A/4G only through renormalisation of G (Susskind & Uglum 1994; Jacobson 1994); fully, only if gravity is wholly induced (Speculative); and spin-1 fields add contact terms (Kabat 1995). | Strominger–Vafa abstract (MS); Wald 2001 §5 (sub-agent full text) |
| 21 | HB03 "What It Claims", cross-ref to HB01 | "at most one bit per Planck area"; "the holographic principle follows from the Bekenstein bound" | **H / Q** | S ≤ A/4l_P² in nats is ≈ 0.36 bits per Planck area. The entry's own figure, 1.4 × 10⁶⁹ bits/m², already uses this. The spacelike holographic bound is motivated by the GSL and collapse arguments, not derived from the Bekenstein bound. It fails in general and is replaced by Bousso's covariant bound. | Main session's arithmetic; sub-agent |
| 22 | HB04 "What It Claims" | Hawking radiation is "fundamentally an information-theoretic phenomenon: … transferring information from behind the horizon to the exterior" | **E** | In Hawking's calculation the radiation is exactly thermal and carries no information about the interior; that is the paradox, as the entry's next sentence says. Add the 2019–20 result: semiclassical path-integral calculations with islands give a unitary Page curve (Almheiri et al., *RMP* 93:035002, 2021). This says *how much* information comes out, not *how*. | Wald 2001 (sub-agent full text); Almheiri et al. 2021 abstract (sub-agent) |
| 23 | BR03 "What It Claims", "What The Math Says"; HB07 cross-ref to BR03 | "As entanglement is reduced, the Ryu-Takayanagi surface grows, corresponding to the wormhole throat stretching", alongside "the throat area shrinks to zero" | **E** (internal contradiction) | The RT area is 4G times the entanglement entropy, so less entanglement means a *smaller* minimal surface (throat area), while the wormhole gets *longer*. Fix both entries. | Main session (from RT's definition, HB07) |
| 24 | BR01, BR03 Mathematical Form and text; BR03 cross-ref to GT04; BR01 archetype | The thermofield double "is a maximally entangled state"; "the Fisher metric on quantum states generates the geometric structure that Van Raamsdonk shows is entanglement-dependent"; "the amount of each is conserved in the equivalence" | **Q / H** | The thermofield double has thermal weights e^{−βE_n/2}; it is maximally entangled only as β → 0. The Bianconi sentence is unsupported (see #16). The "conserved" archetype has no content; drop it. | Main session |
| 25 | HB09 all sections; HB09 anchor | The GSL and the fluctuation theorems "are consequences of the non-negativity of KL divergence D_KL(p_forward‖p_reverse)". Anchor "Wall 2009 Ten proofs of the generalized second law" carries doi:10.1103/PhysRevD.80.124008 | **Q**; anchor **E** | Wall's GSL proofs are semiclassical (quantum fields on a classical background) and rest on stated axioms checked for free fields and 1+1 CFTs. The relative-entropy route uses *quantum* relative entropy under restriction to later horizon slices (main session's knowledge; verify). It is not classical path-space KL. Keep the fluctuation-theorem parallel as an analogy (`vocabulary-stacking-analogy`). **The anchor DOI belongs to the Kerr/CFT paper** (Guica, Hartman, Song & Strominger); Wall's paper is *JHEP* 06 (2009) 021, doi:10.1088/1126-6708/2009/06/021, arXiv:0901.3865. | Crossref (MS); Wall 2012 abstract (sub-agent) |
| 26 | IT05 "What It Claims" | Fisher information "connects statistical inference to general relativity (Ruppeiner geometry)" | **Q** | Ruppeiner geometry lives on *thermodynamic state space* (including black-hole thermodynamic parameters), not on spacetime. Write "to thermodynamic geometry (Ruppeiner)". Tag `vocabulary-stacking-analogy`. | Main session; BR04 anchor (Brody & Rivier 1995) |
| 27 | GT05 (banner already in place); `CCA_GRAVITY_FINDINGS.md` §1.1 Hop 2 | GT05: the paper's "nearly observable" is repeated without numbers. Hop 2: "Fisher information is the second derivative of KL divergence … This is the Cramér-Rao bound" | **Q** / **E** | GT05: add that mm-scale mutual-gravity sensors are ~10⁹ above the λ = 0 floor, and that λ = 0 is excluded. Hop 2: the Hessian identity is not the Cramér–Rao bound, which bounds estimator variance by the inverse Fisher information. | Carney 2025 (MS, fetch) and §C arithmetic; main session |

**Pattern (for the drift catalogue).** Items 1, 2, 7, 12 and 17 share one shape, the gravity analogue of `landauer-scope-overreach`. A thermodynamic, entropic or induced derivation of gravitational dynamics is described as non-quantum, or taken to imply that gravity is classical or has no gravitons. Yet its inputs are quantum (Unruh or Hawking temperature, entanglement area law, one-loop effective action), and it is silent on whether the field is quantized.

Suggested tag: **`emergent-read-as-classical`**.

Items 4, 14, 16, 18, 24 (Bianconi clause), 25 and 26 are instances of the existing `vocabulary-stacking-analogy`. This confirms the M0 diagnosis of the Fisher–gravity chain at the level of individual link descriptions, not only the chain as a whole.

---

## (G) Candidate fold-in reference entries (owner decides; nothing written)

| # | Proposed entry | Core sources | Would correct / anchor |
|---|---|---|---|
| R1 | Gravitationally mediated entanglement witness (BMV) and what it would show | Bose et al. 2017; Marletto & Vedral 2017; Feynman 1957; Galley–Giacomini–Selby 2022; Danielson–Satishchandran–Wald 2022; Carney 2022; Fragkos–Kopp–Pikovski 2022; Martín-Martínez–Perche 2023; Christodoulou et al. 2023 | QR-005; GT05; BR01 |
| R2 | Gravity is not a pairwise local classical channel | Kafri–Taylor–Milburn 2014; Altamirano et al. 2018 | — |
| R3 | Classical-quantum (postquantum) gravity and the decoherence–diffusion trade-off | Oppenheim 2023 *PRX* 13:041040; Oppenheim et al. 2023 *Nat. Commun.* 14:7910; Janse et al. 2024; Layton–Oppenheim–Weller-Davies 2024 | — |
| R4 | Diósi–Penrose collapse and underground bounds | Diósi 1987/89; Penrose 1996; Donadi et al. 2021; Majorana 2022 (+ erratum); XENONnT 2026; Figurato et al. 2024; Trillo & Navascués 2025 | — |
| R5 | Semiclassical (Schrödinger–Newton) gravity and Page–Geilker | Bahrami et al. 2014; Page & Geilker 1981; Yang et al. 2013; Tilloy & Diósi 2016 | — |
| R6 | Minimum noise of non-entangling gravity; entanglement-free tests | Kafri & Taylor 2013; Lami–Pedernales–Plenio 2024; Angeli et al. 2025 (preprint); Fabiano et al. 2026 (preprint) | GT05 |
| R7 | Quantum matter in an external gravitational field, and what it cannot show | COW 1975; Nesvizhevsky 2002; qBounce; Asenbaum 2020; Overstreet 2022; Panda 2024 | GT02 (Kobakhidze) |
| R8 | State of the experiments: the mass gap | Westphal 2021; Fuchs 2024; Pedalino 2025/26; Rossi 2025; Bose et al. *RMP* 2025 | — |
| R9 | Graviton detectability | Dyson 2013; Carney–Domcke–Rodd 2024; Tobar et al. 2024; GWTC graviton-mass bounds | — |
| R10 | Scope of black-hole microstate counting | Strominger–Vafa 1996; Ashtekar et al. 1998; Guica et al. 2009; Wald 2001; Carlip 2014 | HB02 |
| R11 | Bekenstein bound as a QFT relative-entropy statement; holographic vs covariant bounds | Casini 2008; Bousso 1999; Bousso–Casini–Fisher–Maldacena 2014 | HB01, HB03 |
| R12 | Page curve and islands | Penington 2019; Almheiri et al. 2019; Almheiri et al. *RMP* 2021 | HB04 |
| R13 | Verlinde 2016 emergent gravity and its tests, as its own entry | Verlinde 2017 *SciPost* 2:016; Brouwer 2017, 2021; Lelli 2017; Hees 2017; Halenka & Miller 2020 | GT02 |
| R14 | Compatibility of emergent gravity with gravitons; constraints on emergent models | Sindoni 2012 *SIGMA* 8:027; Carlip 2014 (arXiv:1207.2504); Weinberg & Witten 1980; Alonso-Serrano & Liška 2020 | GT01, GT02, GT10 |

R1–R6 are the priority: together they would let the wiki state QR-005's question in its own terms.

---

## (H) Candidate sub-questions, and what would decide each

| # | Sub-question | Deciding data | Disposition (suggested; no gate run) |
|---|---|---|---|
| S1 | Does a thermodynamic or entropic derivation of Einstein's equation, by itself, predict anything different from quantized gravity in the lab? | None needed: the derivations concern field equations, not quantization. Only a specific microscopic model (e.g. Carney et al. 2025) makes a lab prediction | **Looks answered** (no, it does not). Gate 1 likely `answered`; fold via R14 and corrections #1, #2, #7, #12 |
| S2 | Do existing data already exclude free-energy (entropic) mediator models? | Force-noise and decoherence bounds against the two Carney models | **Partly answered**: non-local λ = 0 excluded, the rest unfalsifiable by noise. The local-model window (~10–100 μm) rests on one preprint. Record it; re-check when Fabiano et al. 2026 is published |
| S3 | What would a positive BMV witness establish? | A theoretical consensus that does not yet exist | **Open in the literature** (Huggett et al.; Fragkos et al.; Bose et al. *RMP* 2025). Not decidable by us |
| S4 | Is there a classical-gravity model that survives a positive witness? | Peer-reviewed resolution of Aziz & Howl; tests of Diósi–Penrose entanglement dynamics | **Open in the literature**. Record it; not decidable by us |
| S5 | How large is the remaining window for Oppenheim's classical-quantum gravity, given that Janse 2024 and Oppenheim 2023 disagree? | Read the published versions and reconcile the inequalities | **Mode A bookkeeping**, decidable in-house in an hour or two. Worth doing before any fold-in of R3; not a research question, so no gate |
| S6 | Can a below-threshold force-noise measurement substitute for the entanglement witness, and how far are current sensors? | The threshold's generality (Kafri–Taylor; Fabiano 2026), plus sensor noise at mm separation | **Open in the literature**; the sensor gap (~9 orders) is computed here. The closest thing to a near-term deciding observable |
| S7 | Does the ħ in S = A/4ħG count gravitational microstates or matter entanglement? | Nothing obtainable | **DROP** suggested (`undecidable-with-obtainable-data`). Expert-recognised as open (Wald; Carlip) |

**Overall.** QR-005 as worded looks headed for Gate 1 `open-in-literature`, framed by Bose et al. 2025, Carney et al. 2025 and Huggett et al. 2022. Its "thermodynamic" half largely dissolves: thermodynamic derivations are not a rival prediction (S1). The live rival hypotheses are *classical* or *stochastic* gravity and collapse models, not thermodynamic gravity. None of S1–S7 is a question the wiki could decide by its own work, except the bookkeeping in S5.

**Drift note.** The owner's strand (gravity from information or a holographic surface) maps onto GT01, GT02, GT10 and the Fisher–gravity chain. The evidence here supports a modest version: the field equations behave like an equation of state, which is Supported. It does not support the stronger version: that gravity is therefore not quantum, or that information is the substrate. The stronger version is not what the cited authors claim. If the reflex arises to retreat to "it's all information anyway", that move forbids nothing. The useful test is the one the field already uses: *does the model entangle, and if not, how much noise must it add?*

---

## (I) Sources and reading markers

**Markers (sub-agent):** "full text" means the agent read the body: directly, or through a fetch tool, or partially, as stated. Then "abstract"; "search summary"; and "not retrieved", which means from memory and must be verified.

**MS** = what the main session checked itself:
- **cit** — title, authors and venue confirmed through Crossref or arXiv metadata;
- **abs** — abstract read through the arXiv API;
- **ft** — body text read through a PDF text extraction or fetch, for the stated passages.

Nothing below is upgraded.

| Source | Marker (sub-agent) | MS |
|---|---|---|
| Jacobson 1995, *PRL* 75:1260, arXiv:gr-qc/9504004 | full text | ft (derivation, Λ, quantization remark) |
| Jacobson 2016, *PRL* 116:201101, arXiv:1505.04753 | full text (v4) | abs |
| Casini, Galante & Myers 2016, *JHEP* 03:194, arXiv:1601.00528 | full text (intro, discussion) | abs |
| Speranza 2016, *JHEP* 04:105, arXiv:1602.01380 | abstract | — |
| Eling, Guedens & Jacobson 2006, *PRL* 96:121301 | full text | — |
| Chirco & Liberati 2010, *PRD* 81:024016 | full text (passages) | — |
| Verlinde 2011, *JHEP* 04:029, arXiv:1001.0785 | full text (via fetch) | abs |
| Verlinde 2017, *SciPost Phys.* 2:016, arXiv:1611.02269 | abstract + passages | — |
| Padmanabhan 2012, arXiv:1206.4916 (no journal ref) | full text | abs |
| Padmanabhan 2010, *Rep. Prog. Phys.* 73:046901 | abstract + passages | — |
| Visser 2002, *MPLA* 17:977 (Sakharov review) | full text (passages) | — |
| Jacobson 1994, arXiv:gr-qc/9404039 | full text | — |
| Kabat 1995, *NPB* 453:281 | abstract | — |
| Alonso-Serrano & Liška 2020, *PRD* 102:104056 | abstract | — |
| Sindoni 2012, *SIGMA* 8:027 | abstract + passages | — |
| Carlip, "Challenges for emergent gravity", arXiv:1207.2504 (*Stud. Hist. Phil. Mod. Phys.* 46:200, venue unverified) | full text (passages) | — |
| Kobakhidze 2011, *PRD* 83:021502, arXiv:1009.5414 | abstract | abs |
| Chaichian, Oksanen & Tureanu 2011, *PLB* 702:419 | abstract | — |
| Visser 2011, *JHEP* 10:140, arXiv:1108.5240 | abstract | — |
| Dai & Stojkovic 2017, *JHEP* 11:007 | (INSPIRE-checked) | cit |
| Dai & Stojkovic 2017, *PRD* 96:108501 (= arXiv:1706.07854) | (INSPIRE-checked) | cit |
| Hossenfelder 2017, *PRD* 95:124018, arXiv:1703.01415 | (INSPIRE-checked) | cit |
| Brouwer et al. 2017, *MNRAS* 466:2547; Brouwer et al. 2021, *A&A* 650:A113 | abstract | — |
| Lelli, McGaugh & Schombert 2017; Hees, Famaey & Bertone 2017, *PRD* 95:064019; Halenka & Miller 2020, *PRD* 102:084007 | abstract | — |
| Schimmoller et al. 2021, *PRR* 3:033065 | abstract | — |
| Bianconi 2025, *PRD* 111:066001, arXiv:2408.14391 | — | abs |
| Bose et al. 2017, *PRL* 119:240401, arXiv:1707.06050 | full text (machine-extracted) | abs |
| Marletto & Vedral 2017, *PRL* 119:240402, arXiv:1707.06036 | abstract | abs |
| Feynman 1957, Chapel Hill, ch. 23 (DeWitt & Rickles 2011) | full text (summarised) | — |
| Anastopoulos & Hu 2018, arXiv:1804.11315 | abstract | — |
| Hall & Reginatto 2018, *J. Phys. A* 51:085303 | abstract | — |
| Christodoulou & Rovelli 2019, *PLB* 792:64 | abstract | — |
| Belenchia et al. 2018, *PRD* 98:126009 | abstract | — |
| Danielson, Satishchandran & Wald 2022, *PRD* 105:086001 | abstract | abs |
| Carney 2022, *PRD* 105:024029 | abstract | abs |
| Galley, Giacomini & Selby 2022, *Quantum* 6:779 | abstract | abs |
| Fragkos, Kopp & Pikovski 2022, *AVS Quantum Sci.* 4:045601 | abstract | abs |
| Martín-Martínez & Perche 2023, *PRD* 108:L101702 | abstract | abs |
| Christodoulou et al. 2023, *PRL* 130:100202 | abstract | — |
| Huggett, Linnemann & Schneider 2022, arXiv:2205.09013 | abstract | — |
| Lami, Pedernales & Plenio 2024, *PRX* 14:021022 | abstract | abs |
| Trillo & Navascués 2025, *PRD* 111:L121101 | abstract | abs |
| Aziz & Howl 2025, *Nature* (doi:10.1038/s41586-025-09595-7) | abstract | abs |
| Aziz–Howl rebuttals (Marletto–Vedral 2510.19969; Marletto et al. 2511.07348; Diósi 2511.00852; Schneider et al. 2511.19242; Gundhi et al. 2604.19696; Xue et al. 2604.16276; Tibau Vidal & Iyer 2607.03429; Lin & Mondal *PRD* 113:L061901) | abstract / title | — |
| Plávala 2026, *PRD* 113:085004, arXiv:2508.03052 | abstract / search summary | — |
| Bose et al. 2025, *Rev. Mod. Phys.* 97:015003, arXiv:2311.09218 | abstract | abs |
| Carney, Stamp & Taylor 2019, *CQG* 36:034001 | abstract | — |
| Oppenheim 2023, *PRX* 13:041040, arXiv:1811.03116 | abstract | abs (venue from the APS page, sub-agent) |
| Oppenheim, Sparaciari, Šoda & Weller-Davies 2023, *Nat. Commun.* 14:7910 | full text | abs + ft (bounds, Eqs. 44–47) |
| Janse et al. 2024, *PRR* 6:033076, arXiv:2403.08912 | full text (v1) | abs + ft (orders-of-magnitude statements) |
| Layton, Oppenheim & Weller-Davies 2024, *Quantum* 8:1565; Grudka et al. 2024, arXiv:2402.17844 | abstract | — |
| Kafri, Taylor & Milburn 2014, *NJP* 16:065020 | abstract | — |
| Kafri & Taylor 2013, arXiv:1311.4558 | abstract | — |
| Altamirano et al. 2018, *CQG* 35:145005 | full text | abs |
| Donadi et al. 2021, *Nat. Phys.* 17:74, arXiv:2111.13490 | full text | abs + ft (R₀ bound, Penrose value) |
| Arnquist et al. (Majorana) 2022, *PRL* 129:080401; erratum *PRL* 130:239902 | abstract / search summary (erratum value) | — |
| XENONnT (Aprile et al.) 2026, *PRL* 136:120201, arXiv:2506.05507 | full text (results) | abs + ft (R₀ bounds) |
| Figurato et al. 2024, *NJP* 26:113004 | abstract | — |
| Bahrami, Großardt, Donadi & Bassi 2014, *NJP* 16:115007 | full text (part) | — |
| Page & Geilker 1981, *PRL* 47:979 | not retrieved | — |
| Tilloy & Diósi 2016, *PRD* 93:024026 | abstract | — |
| Carney, Karydas, Scharnhorst, Singh & Taylor 2025, *PRX* 15:031038, arXiv:2502.17575 | full text (v1 + PRX) | abs + ft (fetch: "nearly observable", λ = 0 excluded, a ≳ 1 mm, "not all realizations") |
| Fabiano, Fujita, Matsumura & Carney 2026, arXiv:2603.26075 (preprint) | full text (partial) | abs |
| Manley et al. 2026, *Phys. Rev. Applied* 25:054033 | abstract | — |
| Westphal et al. 2021, *Nature* 591:225, arXiv:2009.09546 | full text (extraction) | abs |
| Fuchs et al. 2024, *Sci. Adv.* 10:eadk2949 | full text (PMC, extraction) | — |
| Pedalino et al. 2025/26, arXiv:2507.21211 (*Nature* 649:866 per search) | abstract / search summary | abs |
| Rossi et al. 2025, *PRL* 135:083601 | search summary | — |
| Panda et al. 2024, *Nature* 631:515 | search summary | — |
| Lee et al. 2020, *PRL* 124:101101 | abstract | — |
| COW 1975; Nesvizhevsky 2002; Asenbaum 2020; Overstreet 2022; Kovachy 2015 | not retrieved (memory) | — |
| Carney, Domcke & Rodd 2024, *PRD* 109:044009 | abstract | abs |
| GWTC-4.0 tests of GR II, arXiv:2603.19020 | abstract | — |
| Tobar et al. 2024, *Nat. Commun.* 15:7229; Dyson 2013 | abstract / not retrieved | — |
| Wald 2001, *Living Rev. Rel.* 4:6 | full text (~87%) | — |
| Strominger & Vafa 1996, *PLB* 379:99 | abstract | abs |
| Guica, Hartman, Song & Strominger 2009, *PRD* 80:124008 | abstract | cit |
| Ashtekar, Baez, Corichi & Krasnov 1998, *PRL* 80:904 | abstract | — |
| Carlip 2014, *IJMPD* 23:1430023 | abstract | — |
| Casini 2008, *CQG* 25:205021 | abstract | abs |
| Wall 2012, *PRD* 85:104049 | abstract | — |
| Wall 2009, *JHEP* 06:021, arXiv:0901.3865 | — | cit |
| Almheiri et al. 2021, *RMP* 93:035002 | abstract | — |
| Isi et al. 2021, *PRL* 127:011103; LVK GW250114, *PRL* 135:111403 | abstract | — |

**Unresolved, flagged for whoever folds this in:**
- the Janse vs Oppenheim window figures (S5);
- the Majorana erratum value (search summary only);
- Pedalino's journal details;
- the Fuchs 2024 force value (30 vs 1030 aN);
- the GWTC-4.0 vs GWTC-3 graviton-mass discrepancy;
- Bianconi's full text (#16);
- the relative-entropy route of Wall's GSL proof (#25);
- that Oppenheim's model cannot entangle: asserted by Oppenheim et al. and Kryhin & Sudhir 2025, but Angeli & Carlesso 2025 show some Markovian hybrid models can, so verify per kernel.

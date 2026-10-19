# Is gravity quantum, or thermodynamic? A primer (QR-005, 2026-10-18)

> **What this is.** A companion to the literature map [`prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md`](../prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md), written for the owner, who has strong thermodynamic intuition and less quantum background. It runs in layers. Read (a) and (b) first; the rest builds on them.
>
> **Citations** point to the map's sources table (§I), which records how each source was read (full text, abstract or search summary). Confidence tags: **Established / Supported / Speculative**. Nothing here is new research; it is a guide to what the field knows.

---

## (a) The minimum quantum mechanics you need

Four ideas carry the whole subject: superposition, entanglement, decoherence and measurement disturbance. Each is given once in plain words, with one concrete example.

### 1. Superposition: being in two places is not the same as being in one place we don't know

A quantum object can be in a *superposition* of two states, for example "here" and "there". This is **not** ignorance. With ignorance (a probability distribution, the thermodynamic picture) the possibilities simply add. With a superposition, each possibility carries an *amplitude*, a number with a phase, and amplitudes can add or **cancel**. That cancellation is interference, and it is how we know both paths were really taken.

**Example.** In a 10 m atom fountain at Stanford, single rubidium atoms were split into two wave packets **54 cm apart** and recombined, and they interfered (Kovachy et al. 2015). Each atom went both ways. If it had secretly taken one path, there would be no interference pattern. **Established.**

*Thermodynamic hook:* a probability distribution is a mixture, and entropy measures your ignorance of it. A superposition is a *pure* state with zero entropy, even though "where is it?" has no single answer.

### 2. Entanglement: correlation that survives every way of looking

Two systems are *entangled* when their joint state cannot be written as "state of A" times "state of B". Measuring them then gives correlations stronger than any shared classical randomness could produce (Bell's theorem). Classical correlation is like two coins drawn from the same bag: they match on heads and tails, and that is all. Entangled systems stay correlated whichever *question* you ask of them.

**The property that matters for gravity:** entanglement **cannot be created by local operations and classical communication**, called *LOCC* in the literature. If two labs can only act locally and phone each other with classical messages, they can build correlation but never entanglement. So if two objects become entangled, whatever connected them must have carried more than classical information. **Established** (a theorem of quantum information theory).

**Example.** In the Bose–Marletto–Vedral proposal, each of two tiny diamonds carries a spin that "tags" which of two positions it is in. Gravity between the diamonds gives each combination of positions a slightly different phase. If gravity can do that coherently, the four combinations end up in a joint state that cannot be factored: the diamonds are entangled. The spins are then read out to check (Bose et al. 2017).

### 3. Decoherence: superpositions leak information into the environment

A superposition survives only as long as *nothing in the environment records which branch is real*. One gas molecule bouncing off the "here" branch, or one thermal photon scattered, carries away which-path information. The interference then disappears, and the object behaves as if it were in one place or the other. No collapse postulate is needed: the information has spread into the surroundings. Bigger separations and bigger objects decohere faster; the rate grows roughly with the square of the separation.

**Example.** To keep two diamonds of 10⁻¹⁴ kg in superpositions ~250 μm wide for ~2.5 s, the Bose et al. design needs a vacuum of **10⁻¹⁵ Pa** and an internal temperature of **0.15 K**. That is far beyond ordinary ultra-high vacuum: essentially no gas molecule may hit either diamond during the run. **Established** as the stated requirement; whether it can be met is **Speculative**.

*Thermodynamic hook:* decoherence is irreversibility seen from the information side. Which-path information spreads into many environmental degrees of freedom and cannot practically be gathered back. This is where your intuition is strongest, and it turns out to matter (see (e)).

### 4. Measurement disturbance: you cannot learn without disturbing

Getting which-path information out of a superposition, by any means, destroys its interference. Turn it around: anything that could in principle be measured *without* disturbing the system is acting classically.

This gives the logic of the gravity experiments in one line. Suppose gravity were a **classical** go-between, something whose value could be read off without disturbing anything. Then it could only carry classical messages between the masses, so it could not entangle them. And a classical field that *responds to* a superposed mass would effectively be measuring where the mass is, which must decohere it. The more faithfully it responded, the more decoherence or noise it would cause. That trade-off is the basis of the "noise route" in (d). **Supported**: a theorem in specific frameworks, for example Oppenheim et al. 2023 and Kafri & Taylor 2013.

---

## (b) Why black-hole thermodynamics already involves quantum theory

This is the point where "quantum versus thermodynamic" starts to come apart.

1. **Classical general relativity has thermodynamic look-alike laws but no temperature.** Classically, a black hole's surface gravity behaves like a temperature and its horizon area like an entropy, and the area never decreases. But a classical black hole absorbs everything and emits nothing, so its physical temperature is **absolute zero**. With classical physics alone, the laws are a resemblance and nothing more (Wald 2001). **Established.**
2. **Hawking supplied the temperature, and it needs ħ.** Quantum fields near a horizon make the black hole glow with a perfect blackbody spectrum at T = ħc³/(8πGMk_B). For a solar-mass black hole that is about 6 × 10⁻⁸ K, colder than the cosmic microwave background, so it is never seen. Once T exists, the first law forces an entropy:

   S = k_B · A / (4 ℓ_P²), where ℓ_P² = Għ/c³.

   The entropy counts horizon area in units of the Planck area, and that unit contains ħ. **Established.**
3. **Classical gravity fixes only the product.** For a non-rotating black hole, T × S = Mc²/2, and ħ cancels. Gravity alone says how much "heat × entropy" there is; quantum theory says how to split it into a temperature and an entropy. As ħ → 0, T → 0 and S → ∞, the familiar problem of classical statistical mechanics having no absolute zero of entropy. **Established** (a five-minute derivation).
4. **But the ħ comes from quantum *matter*, not quantum *gravity*.** Hawking's calculation treats the spacetime as classical and only the fields on it as quantum; it uses no gravitational field equations at all (Wald 2001). The proofs of the generalized second law are also done this way (Wall 2012). So black-hole thermodynamics shows that matter near horizons is quantum. It does **not** by itself show whether the gravitational field is quantum. **Supported.**
5. **The same holds for every thermodynamic derivation of gravity.** Jacobson 1995 derives Einstein's equation from δQ = TdS on tiny horizons, and the T there is the Unruh temperature, which contains ħ. Jacobson 2016 uses the entanglement of the quantum vacuum. Verlinde 2011 uses the Unruh temperature and a bit count containing ħ. Sakharov's induced gravity is a one-loop quantum effect. In every case the "thermodynamic" story runs on quantum inputs. **Established.**

**So the real question is narrower than "quantum or thermodynamic".** Thermodynamic descriptions are, by design, silent about the microscopic degrees of freedom. The question an experiment can answer is:

> **Can the gravitational field carry quantum information, that is, put two masses into an entangled state? Or does it act like a classical, possibly noisy, channel?**

Jacobson 1995 offers an analogy here. He says it may be no more appropriate to *canonically* quantize Einstein's equation than to quantize the equation for sound in air. Sound *is* quantized, though, as phonons, which are collective modes of quantum atoms. So the analogy, read carefully, makes room for gravitons as collective modes. It does not rule them out (map §B4, §F7).

---

## (c) The main hypotheses, side by side

| Hypothesis | What it says | What it predicts in the lab | How it can be tested | Status now |
|---|---|---|---|---|
| **Quantized (perturbative) gravity** | Gravity is a quantum field at low energy, with gravitons, whatever the deeper theory is | Masses in superposition **get entangled**; no extra noise | Entanglement witness (BMV), or force noise below the "classical" threshold | Standard expectation; untested at the quantum level |
| **Thermodynamic or emergent field equations** (Jacobson, Padmanabhan, Verlinde 2011) | Einstein's equation is an equation of state of unknown quantum microstructure | Nothing different from the row above, unless a specific microscopic model is given | Not separately testable at tabletop scale | Derivations **Supported** given their assumptions; silent on quantization |
| **Free-energy mediator models** (Carney et al. 2025) | Newton's force comes from the free energy of a thermal bath of qubits | **Force noise** and decoherence; the non-local version can still entangle, the local one cannot | Force noise versus separation and mass; decoherence of atom interferometers; entanglement | Non-local version with no suppression **excluded**; local version left with a narrow window (one group's preprint) |
| **Classical-quantum gravity** (Oppenheim 2023) | Spacetime is genuinely classical but jittery (stochastic) | **No entanglement**; random metric "diffusion" whose size is tied to decoherence: less of one forces more of the other | Precision mass and acceleration noise, together with interferometer coherence times | "Noise everywhere" version **excluded**; other versions alive in wide windows |
| **Classical channel** (Kafri–Taylor–Milburn 2014) | Gravity acts like continuous measurement plus feedback between pairs of masses | No entanglement; a minimum decoherence | Long-baseline atom interferometry | **Excluded** (Altamirano et al. 2018) |
| **Gravity-caused collapse** (Diósi–Penrose) | Superpositions of differently curved spacetimes collapse on their own | Superpositions die at a rate set by gravitational self-energy; random kicks make charged matter **glow faintly in X-rays** | Underground radiation searches | Parameter-free version **excluded** (Donadi 2021); free-parameter version bounded (XENONnT 2026: R₀ > 4.5 × 10⁻¹⁰ m) |
| **Mean-field semiclassical gravity** (Schrödinger–Newton) | Gravity responds to the *average* position of a superposed mass | No entanglement; odd self-gravity effects | Optomechanical frequency shifts (proposed) | Inconsistent with standard quantum measurement (allows faster-than-light signalling); kept alive only with extra collapse rules |

Two features of this table matter most.
- **The rivals to quantum gravity are mostly *classical* or *noisy* gravity, not "thermodynamic gravity".** Thermodynamic derivations do not compete at this level; specific noisy models do.
- **Every classical rival must pay for its classicality somewhere:** in decoherence, in noise, in collapse radiation, or in a consistency problem. That price is what experiments look for.

---

## (d) The experiments, in plain terms, with timelines

### What has already been done

- **Quantum matter in Earth's gravity.** Neutrons and atoms behave exactly as quantum mechanics predicts in an external gravitational field:
  - interference from height differences (1975);
  - quantized neutron "bouncing" states (2002);
  - atoms kept coherent for ~70 s near a small source mass (2024);
  - the equivalence principle holding for superposed atoms to ~10⁻¹².

  In every one of these, though, the *source* of gravity (Earth, a tungsten block) sits in one definite place. So they cannot tell a quantum field from a classical one. **Established** as a logical point.
- **The pairwise classical-channel model is ruled out** by atom-interferometer data. **Established.**
- **Underground searches** (Gran Sasso germanium, Majorana, XENONnT) found no collapse X-rays, excluding Penrose's natural version of gravity-caused collapse. **Established.**
- **Oppenheim's classical gravity has been squeezed** from both sides, using old torsion-balance data and molecule-interference data; one version is excluded. **Supported.**
- **The smallest object whose gravity has been measured** is a 90 mg gold sphere: gravity between two of them was detected in Vienna in 2021. **Established.**

### The flagship test: gravitationally mediated entanglement

Two tiny diamonds, each about 10⁻¹⁴ kg, are each put into a superposition of two places a quarter of a millimetre apart. They fall side by side for a few seconds, close enough that gravity between them matters and shielded from everything else. Then spins inside them are read out to check whether they became entangled. If they did, gravity carried quantum information.

### Where things stand: three gaps

| What is needed | Best so far | Shortfall |
|---|---|---|
| Heavy object in a two-place superposition (~10⁻¹⁴ kg) | ~3 × 10⁻²² kg sodium clusters (Vienna, 2025–26) | ~7.5 orders of magnitude (factor ~30 million) |
| Superposition ~250 μm wide | ~70 picometres for a levitated nanoparticle | ~6.5 orders |
| Measure the gravity *of* a 10⁻¹⁴ kg object | 90 mg | ~10 orders, and no source mass has ever been in a superposition |

### The noise route, which may come sooner

There is a cheaper idea. Any gravity that *cannot* entangle must add a minimum amount of jitter, so a measurement quieter than that floor would rule it out without building the full entanglement experiment. Related proposals use torsion pendula with no superpositions at all (Lami, Pedernales & Plenio 2024). Current mm-scale force sensors are still about **9 orders of magnitude** too noisy (map §C, computed there). Several groups (Aspelmeyer; Oosterkamp and Ulbricht; Hosten; Taylor; Bonaldi and co-workers) are building milligram-scale, millikelvin oscillators aimed at this regime.

### Timelines

**No published roadmap gives a date.** The 2025 review in *Reviews of Modern Physics* and a 55-author 2025 white paper set out paths but not years. One 2026 paper puts even optimistic projections "outside of the short-term future".

My own reading of the gaps (an inference, not a sourced estimate) is that the direct entanglement test is a multi-decade project. Collapse and classical-gravity bounds will keep tightening year by year in the meantime. Treat any "within ten years" headline with caution unless it cites a design that closes all three gaps.

### Even success would not settle everything

A positive entanglement result would rule out every *local classical* account of gravity. It would not, on its own, prove gravitons exist. An instantaneous Newtonian interaction would give the same signal, and so might some non-local collapse models (Trillo & Navascués 2025). A 2025 *Nature* paper (Aziz & Howl) even argues that classical gravity can entangle matter described by quantum field theory; at least seven rebuttals followed. Researchers on both sides agree that the experiment is worth doing because it would be the first test of gravity *sourced by* a mass in superposition. **Supported.**

---

## (e) Where a thermodynamics-first view is well supported, and where it overreaches

### Well supported

- **Einstein's equation behaves like an equation of state.** Jacobson's 1995 derivation is correct given its inputs; this is **Supported** and widely respected. Out of equilibrium it picks up viscosity-like terms (Eling, Guedens & Jacobson 2006), much as a fluid does.
- **Horizons really are thermodynamic.** Hawking radiation, black-hole entropy and the generalized second law (proved semiclassically) are some of the firmest results connecting gravity, quantum theory and thermodynamics. **Established.**
- **Information is the right bookkeeping for black holes.** The 2019–20 "Page curve" calculations show, in model systems, that the entropy of Hawking radiation behaves as if information is not lost. They do not yet explain *how* it gets out. **Supported** in those models.
- **Your feel for irreversibility is exactly what the rivals turn on.** Every classical alternative to quantum gravity is, in effect, "gravity is an irreversible, noisy channel":
  - Oppenheim's classical gravity diffuses;
  - Carney's free-energy models add force noise;
  - Diósi–Penrose collapse heats matter;
  - Galley, Giacomini & Selby 2023 argue that any consistent coupling of classical gravity to quantum matter must be irreversible (title-level reading).

  So a thermodynamics-first instinct, made precise, becomes a **testable** hypothesis: *gravity adds noise and decoherence that quantum gravity would not*. That is a good scientific position: it forbids quiet, entangling gravity.

### Overreaches

- **"Gravity is thermodynamic, therefore not quantum."** This does not follow. The thermodynamics of a gas does not tell you whether its atoms are quantum: thermodynamics is silent about microphysics by construction. Every thermodynamic derivation of gravity uses ħ. The wiki makes this slip in several places (GT10, GT01, GT02, GT06; map §F #1, #2, #7, #12, #17). The proposed tag for the error is `emergent-read-as-classical`.
- **"No gravitons."** Jacobson's sound-wave analogy permits graviton-like collective modes, as phonons are. Verlinde 2011 never mentions gravitons. Jacobson 2016 takes no position on them.
- **Stacking "relative entropy".** The Fisher–gravity chain treats four objects that share the name as one:
  - classical KL divergence;
  - quantum relative entropy of matter states;
  - quantum relative entropy of *metric operators* (Bianconi);
  - the first law of entanglement.

  They are different objects, and one link in the chain is an identity that holds whether or not Einstein's equation does (map §F #4). This was already diagnosed at M0; the map finds it in individual link descriptions too.
- **"The Bekenstein bound caps bits per unit volume."** It caps entropy relative to energy × size, and contains no G at all; it is really a quantum-field-theory statement (Casini 2008). The area-scaling bound is a different, gravitational one.
- **"Black-hole entropy *is* entanglement entropy."** This holds only after the entanglement's infinities are absorbed into the strength of gravity, and fully only if gravity is wholly induced by matter. That last step is **Speculative**.
- **Small-print slips worth knowing about:**
  - Verlinde's derivation *puts G in* through its bit count; it does not predict G.
  - Padmanabhan's equation stops the *Hubble volume* changing, not the expansion: a de Sitter universe keeps expanding exponentially.

### A note on drift

Your recurring picture (gravity from a holographic surface, information as the substrate) is the wiki's own GT01/GT10/Fisher–gravity strand. The evidence supports a **modest** version of it: the field equations look like an equation of state. It does not yet support the strong version, that information is the fundamental substance and gravity is therefore not quantum.

The useful habit is to ask of any version: *what does it forbid?*
- "Gravity is quantum" forbids non-entangling gravity.
- "Gravity is classical" forbids quiet gravity: it must add noise.
- "It's all information anyway" forbids nothing, and that is the sign to stop and sharpen it.

---

## (f) Reading list, easiest first

1. **Castelvecchi, "Is gravity quantum? Experiments could finally probe one of physics' biggest questions"**, *Nature* 644:320 (2025). News feature; a quick orientation. *(Listed from citation metadata; not read in this pass.)*
2. **Feynman at Chapel Hill (1957)**, "The Necessity of Gravitational Quantization", ch. 23 in DeWitt & Rickles (eds.), *The Role of Gravitation in Physics* (Edition Open Sources, 2011; free online). Two pages of Feynman stating the whole problem with a ball and a Stern–Gerlach magnet.
3. **Wald, "The Thermodynamics of Black Holes"**, *Living Rev. Relativity* 4:6 (2001), §§1–3. Why black holes are thermodynamic, and why that needs quantum theory. Some maths, but the prose carries it.
4. **Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State"**, *PRL* 75:1260 (1995). Four pages; the derivation behind your intuition, in its author's own careful words.
5. **Bose et al. 2017** (*PRL* 119:240401) **and Marletto & Vedral 2017** (*PRL* 119:240402). The two short papers proposing the entanglement test.
6. **Carney, Stamp & Taylor, "Tabletop experiments for quantum gravity: a user's manual"**, *CQG* 36:034001 (2019). A guided tour of what each kind of experiment would show.
7. **Huggett, Linnemann & Schneider, "Quantum Gravity in a Laboratory?"** (arXiv:2205.09013). Philosophers of physics on what a positive result would and would not prove; conceptual, little maths.
8. **Fragkos, Kopp & Pikovski 2022** (*AVS Quantum Sci.* 4:045601). Why "entanglement implies gravitons" needs extra assumptions.
9. **Oppenheim, Sparaciari, Šoda & Weller-Davies 2023** (*Nat. Commun.* 14:7910). The decoherence-versus-diffusion trade-off: how classical gravity could be ruled out *without* the entanglement experiment.
10. **Carney, Karydas, Scharnhorst, Singh & Taylor 2025** (*PRX* 15:031038). The closest thing to "thermodynamic gravity you can test": entropic-force models with definite noise predictions.
11. **Donadi et al. 2021** (*Nat. Phys.* 17:74). How an underground germanium detector ruled out Penrose's natural collapse model.
12. **Jacobson 2016** (*PRL* 116:201101) **with Casini, Galante & Myers 2016** (*JHEP* 03:194). Entanglement equilibrium and its known limits. Needs quantum field theory.
13. **Bose et al., "Massive quantum systems as interfaces of quantum mechanics and gravity"**, *Rev. Mod. Phys.* 97:015003 (2025). The full current review; the reference to return to.

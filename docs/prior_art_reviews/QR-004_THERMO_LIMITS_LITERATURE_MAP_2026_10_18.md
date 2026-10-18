# QR-004 literature map — how close do living systems run to the thermodynamic limits of information processing? (2026-10-18)

> **Provenance (2026-10-18).** Mode A, literature mapping only. This is the map for Questions Raised Log entry **QR-004**. The search was fanned out across seven read-only research sub-agents, following the deep-research pattern at the owner's request:
> 1. Landauer tests and how far cells sit from the bound;
> 2. TURs (thermodynamic uncertainty relations): theory, scope and measurements;
> 3. the cost of sensing and adaptation;
> 4. proofreading and oscillators;
> 5. clocks and synchronization in depth;
> 6. motors and the speed–accuracy–dissipation trade-off;
> 7. critiques and negative results.
>
> The main session read the nine QR-004 wiki entries (and 30 adjacent entries that mention Landauer) directly from `ds_wiki.db` and their anchors in `wiki_history.db`, read-only. It also re-checked the load-bearing citations itself; see column "MS" in §I. **Sub-agent summaries are leads, not readings**: §I gives each source's reading marker as reported, never upgraded. **No gate has been run, and nothing has been written to the databases.** Confidence tags: **Established / Supported / Speculative**.

---

## (A) The answer in plain terms

**For the owner, in one paragraph.**
- **Landauer.** Living cells do **not** run near Landauer's limit, and the field already knows this. Measured costs sit between about ten times the limit (protein synthesis) and a hundred million times it (nerve signalling). The reasons are known too:
  - most of what cells do is not "erasing bits", which is the only thing Landauer's limit prices;
  - cells must work fast and accurately, and both cost energy far above the slow, ideal limit.
- **The bounds that do apply.** Against the newer, better-suited limits, some systems come within a few times the minimum:
  - **TUR:** a law that says precise output costs energy;
  - **proofreading bounds:** limits on how cheaply errors can be removed;
  - **sensing bounds:** limits on how well a cell can measure its surroundings.

  The systems that come close are kinesin motors, *E. coli*'s adaptation machinery and DNA polymerase. Others are far off: the ribosome, chaperones and circadian clocks.
- **What running near a bound buys.** This half of the question is still mostly open, and researchers say so explicitly. The best evidence says evolution tunes these machines for **speed**, with accuracy held at a "good enough" level, not for minimum energy.
- **The wiki's "cost of coherence".** The honest version of the retired idea has a published answer. Keeping oscillators synchronized has a minimum energy cost, and that cost **rises without limit** as synchrony approaches perfect. The wiki's retired formula said the opposite: that perfect coherence is free.

**Calibrated summary.**

| Claim | Tag |
|---|---|
| Cells operate far above Landauer for every measured process | **Established** |
| Several molecular machines operate within ~2–6× of the TUR or of process-specific bounds | **Supported**: model-fitted dissipation, not calorimetry |
| Running near the bound is selected for, or buys fitness | **Speculative**; open in the literature (Yang et al. 2021; Barato & Seifert 2015; Horowitz & Gingrich 2020) |
| Rigorous Landauer or TUR results at organism or ecosystem scale | **None found** |

---

## (B) Settled — Established

1. **Landauer's bound and its scope.**
   - **What it prices.** Resetting a memory lowers its Shannon entropy. The average heat released to a bath at temperature T is at least kT times that drop: kT ln 2 for one unbiased bit.
   - **Where it comes from.** It is a **second-law** result. It counts states, not degrees of freedom, so it does **not** depend on spatial dimension.
   - **What it does not price.** Logically reversible operations have no such floor. This includes measurement and copying onto a blank register (Bennett 1982).
   - **Generalisations:**
     - non-uniform or non-equilibrium memories take a relative-entropy form (Esposito & Van den Broeck 2011);
     - Sagawa & Ueda 2009 split the cost between measurement and erasure;
     - finite reservoirs add a size-dependent correction (Reeb & Wolf 2014);
     - finishing in finite time τ costs an excess that scales as 1/τ (Proesmans, Ehrich & Bechhoefer 2020).
   - **Classical or quantum:** the bound applies to both (Piechocinska 2000; Reeb & Wolf 2014).
2. **Experimental confirmation of Landauer.**
   - Bérut et al. 2012: the mean heat reaches kT ln 2 only in the slow-cycle limit, by extrapolation, and with incomplete erasure.
   - Jun, Gavrilov & Bechhoefer 2014: the precision test. Erasure costs 0.71 ± 0.03 kT against ln 2 = 0.69. A matched control that erases nothing costs 0.05 ± 0.03 kT.
   - Hong et al. 2016 (nanomagnets) and Gaudenzi et al. 2018 (molecular nanomagnet, quantum): within roughly 1–2× of the bound.
   - The philosophical dispute (Norton 2005, 2011) concerns how general the *proofs* are, not the measured cost of a specified erasure.
3. **The TUR is a fluctuation bound, not a universal one.**
   - **Statement:** for currents in a **non-equilibrium steady state** of classical continuous-time Markov-jump or overdamped dynamics with constant driving, (relative variance) × (total entropy production) ≥ 2k_B.
   - **History:** Barato & Seifert 2015 proved it near equilibrium and for single cycles and conjectured the general case. Gingrich et al. 2016 proved the long-time case, and Horowitz & Gingrich 2017 the finite-time case.
   - **It is not an equilibrium result:** it is vacuous at equilibrium.
   - **Known violations outside its assumptions:** inertial dynamics (Pietzonka 2022 counterexample), periodic or time-dependent driving, magnetic fields or broken time-reversal symmetry, quantum-coherent transport, and discrete-time chains (Horowitz & Gingrich 2020 review).
4. **Kinetic proofreading** (Hopfield 1974; Ninio 1975).
   - Spending free energy on an extra checking step can push errors below the equilibrium discrimination limit, roughly squaring the error.
   - Reaching the minimum error needs unbounded dissipation or time (Bennett 1979; Murugan, Huse & Leibler 2012).
   - Error reduction is capped by the chemical driving of the proofreading step (Sartori & Pigolotti 2015).
5. **Sensing.**
   - Counting noise sets a precision limit (Berg & Purcell 1977; Bialek & Setayeshgar 2005). It is not thermodynamic.
   - Beating the equilibrium receptor limit requires dissipation (Govern & ten Wolde 2014 PRL).
   - Energy, receptors × time, and readout molecules are three resources that **cannot substitute for one another** (Govern & ten Wolde 2014 PNAS).
   - Fuel-driven readout networks cannot reach the Landauer-type copy bound (ten Wolde et al. 2016; Ouldridge, Govern & ten Wolde 2017).
6. **Oscillators** (within Markov models).
   - Coherence costs free energy (Cao et al. 2015).
   - The number of coherent cycles is bounded by driving affinity and by the number of states in the cycle (Barato & Seifert 2017 conjecture, proved by Ohga, Ito & Kolchinsky 2023).
   - Oberreiter, Seifert & Barato 2022 conjecture a minimum of 4π² kT per coherent oscillation. It is proved only in a limit, so it is **not Established**.

---

## (C) Measured against a bound — which system, and how close

| System | Bound | How close | Basis | Source (marker) |
|---|---|---|---|---|
| Colloidal bead, feedback trap | Landauer | 1.0× (0.71 vs 0.69 kT) | measured | Jun 2014 (sub-agent full text) |
| Translation (ribosome) | generalised Landauer, per amino acid | ~10× (abstract: "about an order of magnitude"); ~26× in the body per sub-agent | estimated from ATP/GTP budgets | Kempes et al. 2017 (MS: abstract) |
| DNA replication | generalised Landauer | ~165× | estimated | Kempes 2017 (sub-agent) |
| Neural signalling (blowfly) | Landauer | ~10⁴ ATP/bit (synapse) to 10⁶–10⁷ ATP/bit (graded, spikes): ~3×10⁵ to 3×10⁸ × kT ln 2 (sub-agent arithmetic, ATP ≈ 20 kT) | measured information rates, ATP from models | Laughlin et al. 1998 (search summary) |
| *E. coli* sensory adaptation | information–thermodynamic minimum (not Landauer) | slightly over 2× | modelled from literature parameters | Sartori et al. 2014 (MS: abstract + discussion via fetch) |
| *E. coli* chemotaxis, resource allocation | Govern–ten Wolde optimality | balanced within ~3× | model + measured copy numbers | Govern & ten Wolde 2014 PNAS (sub-agent full text) |
| *E. coli* chemotaxis behaviour | information-limited drift speed | ~65% of the maximum | measured | Mattingly et al. 2021 (sub-agent full text; MS: citation) |
| *E. coli* chemosensing | molecule-counting limit | ~100× below it; internal noise is the cause | measured | Mattingly et al., *Nat. Phys.* 2026 follow-up (abstract / search) |
| Kinesin-1 | TUR (Q ≥ 2) | Q ≈ 7.2 at cellular conditions (3.6×); ≈4 near 4 pN load | **model fit**, not measured dissipation | Hwang & Hyeon 2018 (MS: abstract) |
| F1-ATPase / dynein / myosin V | TUR | Q ≈ 7.7 / 9.1 / 13 | model fit | Hwang & Hyeon 2018 |
| Kinesin, hidden dissipation | efficiency | ~80% of input lost inside the molecule at 2 pN; ~19% efficient at maximum power (sub-agent arithmetic) | measured (Harada–Sasa) | Ariga, Tomishige & Mizuno 2018 (sub-agent full text) |
| F1-ATPase | free-energy transduction | stall work ≈ Δμ of one ATP; little internal loss | measured | Toyabe et al. 2010 PRL; 2011 PNAS (fetch summary) |
| T7 DNA polymerase | error–cost bound; TUR | almost on the error–cost bound; Q ≈ 10 | model fit | Yu, Kolomeisky & Igoshin 2022 (abstract); Song & Hyeon 2020/21 |
| *E. coli* ribosome | error–cost bound; TUR | far: high-dissipation regime; Q ≈ 45–50 | model fit | Yu 2022; Song & Hyeon 2021 |
| Polymerase and ribosome | speed–accuracy optimum | tuned for **speed**: minimum error ~150× (T7) / ~50× (ribosome) lower but ~3,500× / ~500× slower | model fit to kinetics | Banerjee, Kolomeisky & Igoshin 2017 (MS: citation + search) |
| GroEL chaperone | TUR | Q ≳ 2×10³ | rough estimate | Song & Hyeon 2021 |
| KaiABC clock | oscillator-coherence bounds | ≥10× to >100× above (models disagree); ~16 ATP per KaiC monomer per cycle against ~2 needed for phosphorylation | ATP measured, coherence modelled | Terauchi 2007; Marsland et al. 2019; Oberreiter 2022; Yang et al. 2021 (MS: full text via fetch, §"Open Question") |
| *S. elongatus* clock in vivo | timing precision | <~5% error per cycle, needs thousands of Kai proteins | measured; no ATP budget | Chew et al. 2018 (sub-agent) |

**What stands out (Supported):**
- No measurement anywhere pairs a clock's **measured** dissipation with its measured coherence.
- No sensing or regulation process has a TUR "Q" computed from **measured** dissipation.
- Every biological Q value comes from a fitted kinetic model.

---

## (D) Open — and who frames it as open

1. **How close do cells operate to these limits, and do energetic costs become fitness costs?** Yang et al. 2021 *PNAS* (Introduction, and "Open Question" sections). Main session: full text via fetch.
2. **Did the trade-off between precision and cost guide evolution?** Barato & Seifert 2015 raise it. Hwang & Hyeon 2018 call motors "semi-optimized", which is an interpretation without a baseline (Supported only as description).
3. **An organised hierarchy of TURs with clear validity domains; response analogues; combining bounds for model selection in biology.** Horowitz & Gingrich 2020.
4. **What replaces the TUR for inertial dynamics.** Open since Pietzonka 2022's counterexample.
5. **The right performance measure for sensing; dynamic signals; prediction; how cells implement maximum-likelihood sensing.** ten Wolde et al. 2016 review.
6. **Is the energy–speed–accuracy relation universal?** Questioned by Wang, Lan & Tang 2015 and by Harvey, Lahiri & Ganguli 2023.
7. **Why *E. coli* acquires ~100× less information than the physical limit yet uses it efficiently.** Mattingly et al. 2021 and the 2026 follow-up, which attribute it to internal noise.
8. **Does KaiC's surplus ATP pay for synchronization?** Predicted by Zhang et al. 2020; untested.
9. **The minimum-cost conjecture for coherent oscillations** (4π² kT per coherent cycle). Oberreiter et al. 2022; proved only in the weak-noise limit.
10. **Organism and ecosystem scale.** No rigorous Landauer or TUR application was found.
    - Wolpert 2016 (*Entropy*) gives a formal organism-level cost–benefit framework (abstract only).
    - Ecosystem "maximum entropy production" claims rest on a derivation shown to be in error (Grinstein & Linsker 2007, on Dewar 2005) and on weak tests (Meysman & Bruers 2010). All search summary.
    - This is an absence in three targeted searches, not an exhaustive review.

---

## (E) What the wiki holds, and its gaps

**Holdings (read 2026-10-18).**
- **B5 (Landauer):** anchored to Landauer 1961; cites Bérut 2012 and Bennett 1982 in its text.
- **TD3, INFO1, INFO2, INFO4, INFO5:** canonical anchors are good (Shannon 1948, Khinchin, Cover & Thomas, Clausius, Lieb & Yngvason).
- **BIO5:** Crick 1970.
- **F1:** Ashby 1956; anchor confidence medium.
- **F5:** flagged as an internal construction (P4 / CcO programme).
- **Adjacent useful entries:**
  - IT06 (Seifert stochastic thermodynamics);
  - NE03–NE05 (Jarzynski, Crooks, fluctuation–dissipation);
  - NE06 (England);
  - BIO10 (homeostasis).

**Gaps.** The wiki holds none of the following:
- the TUR;
- kinetic proofreading (Hopfield appears nowhere);
- Bennett's reversible computation as its own result (it is cited only inside B5);
- Sagawa–Ueda or Esposito–Van den Broeck generalisations;
- any sensing limit (Berg–Purcell appears nowhere; the word "chemotaxis" appears nowhere);
- the cost of oscillations or synchronization;
- motor energetics;
- any **measured** biological energy-per-bit figure (Laughlin, Kempes).

In short, the physics bound sits on the map, but the whole literature that tests biology against it does not. That literature is what QR-004 needs.

---

## (F) Wiki errors found, with proposed corrections

*Proposals only: nothing is applied. Severity: **E** = wrong, **Q** = needs qualifying, **H** = hygiene. "MS" = checked by the main session; otherwise the source is a sub-agent reading (see §H).*

| # | Entry / field | Claim as written | Verdict | Proposed correction | Source |
|---|---|---|---|---|---|
| 1 | B5, E2, TD3 `dimensional_sensitivity` = D-sensitive; the archetype boilerplate "Landauer and Heisenberg involve k_BT and ℏ, both acted on by Ω_D" sits in **22 entries** (Ax1, B3, B5, E2, EM11, ES6, F1, F2, F5, G3, KC3, KC5, M1, Q3, Q5, QM2, T6, T9, TD13, TD3, TD4, TD8) | Landauer's bound is D-sensitive through k_B | **E** | Landauer's derivation counts states and allows any number of degrees of freedom; it does not depend on dimension. Set B5 to D-invariant, or mark the Ω_D sentence as a DFIG internal claim, not part of the reference law. B5's own "What's Conjectured" already says the bound is D_eff-invariant, contradicting its own property row. | Landauer 1961 §3 (sub-agent read directly) |
| 2 | Archetype boilerplate in **21 entries** (same list minus B3) | "Thermodynamic bounds cannot be violated by any mechanism, no matter how clever" | **Q** | "Second-law (mean) bounds have no known violation once all reservoirs and information are counted. Fluctuation bounds such as the TUR hold only within stated model classes and have explicit counterexamples outside them." | Horowitz & Gingrich 2020; Pietzonka 2022 |
| 3 | TD2 cross-ref | Erasing a bit is "a first-law consequence for information" | **E** | A **second-law** consequence. | Landauer 1961; Esposito & Van den Broeck 2011 |
| 4 | EM11 cross-ref | "Even reversible computation produces Joule-like dissipation at k_BT ln 2 per bit" | **E** | Reversible computation has no Landauer floor. Finite-speed dissipation scales as 1/τ and depends on the protocol (Jun 2014's no-erasure control: 0.05 kT). | Bennett 1982; Proesmans 2020; Jun 2014 |
| 5 | NE06 cross-ref to B5 | "Copying one bit costs at least kT ln 2" | **E** | Copying onto a blank register has no minimum cost. The cost belongs to resetting the blank, or to discarding the copy's correlations (≥ kT × mutual information if the correlations are not used). A persistent template copy stores free energy that can be recovered only by destroying it. | Bennett 1982; Ouldridge, Govern & ten Wolde 2017 PRX; Ouldridge & ten Wolde 2017 PRL (MS: title/venue) |
| 6 | BIO5 cross-ref to B5 | "Transcription and translation are irreversible information operations with thermodynamic cost" | **E** | Template copying is not inherently logically irreversible. The real cost (20–100 kT per monomer) pays for speed and accuracy, not erasure. | Bennett 1982 (RNA-polymerase passage); Andrieux & Gaspard 2008; Sartori & Pigolotti 2015 |
| 7 | BIO5 Mathematical Form | "Replication fidelity ~10⁻⁹ per base per replication (with proofreading)" | **Q** | "~10⁻⁹–10⁻¹⁰ overall, from base selection (~10⁻⁴–10⁻⁵), exonuclease proofreading (~10⁻²) **and** mismatch repair. *E. coli* wild type measures 2.2×10⁻¹⁰ per nt per generation; without mismatch repair, ~3×10⁻⁸." | Lee et al. 2012 PNAS (MS: via search/BioNumbers); Bębenek 2018 |
| 8 | INFO4 cross-ref to BIO5 | "The DPI explains why reverse translation cannot occur" | **E** | The DPI bounds information *about a source* along a Markov chain. It does not forbid a molecular mechanism that writes *a* (non-unique) coding sequence for a protein. The Central Dogma is an empirical claim about which transfers occur (Crick 1970). | Main session's own reasoning (Supported); Crick 1970 anchor |
| 9 | INFO4 cross-ref to B5 | Irreversible processing costs "ΔI × kT ln 2" | **Q** | A lower bound ("at least"), and only for information actually erased, or correlations discarded without use. | Ouldridge et al. 2017 PRX; Sagawa & Ueda 2009 |
| 10 | B5 "Why It Matters Here" | "Every neural spike, every enzymatic decision that discards information, pays at least kT ln 2" | **Q** | "The floor applies only to information actually erased. Measured neural costs are ~10⁴–10⁷ ATP per bit (~10⁵–10⁸ × kT ln 2). A spike is not an erasure." | Laughlin et al. 1998; Kempes et al. 2017 |
| 11 | B5 "What's Established" | Bérut 2012 measured dissipation "approaching the kT ln 2 limit" | **Q** | Add: approached only asymptotically, at slow cycles, with incomplete erasure. The precision test is Jun, Gavrilov & Bechhoefer 2014 (0.71 ± 0.03 kT). | Bérut 2012 (MS: search); Jun 2014 (MS: search) |
| 12 | D1 Key Connections | "Neural encoding pays Landauer cost per bit of stimulus resolution" | **Q** | Encoding is not erasure. Cite Laughlin 1998 for the actual metabolic cost per bit. | Laughlin et al. 1998 |
| 13 | B5 "Phase Coherence Cost", H3 body, **Q5** ("has not been published"; Nearest Existing Literature) | Synchronization cost is a Landauer-class erasure, Cost ∝ (1−λ)²·d_f; the combination "has not been published" | **E** for Q5's literature claim | The cost of coherence and synchronization **is** published. Under Zhang et al. 2020's optimal design, the minimum excess dissipation **diverges as 1/(1−r)** as the Kuramoto order parameter r → 1 (their Eq. 15). Below a critical dissipation there is no synchrony at all. Coherence of a single oscillator costs free energy roughly linearly (Cao 2015) and is bounded by affinity and number of states (Barato & Seifert 2017). None of this is Landauer erasure: it is continuous dissipation to stay out of equilibrium. Zhang's analysis is mean-field: **no dimension or d_f dependence**. Proposed: a Q5 banner stating that the literature answer exists and **contradicts the ansatz in form** (cost vanishing at full coherence vs diverging), with Zhang 2020, Cao 2015 and Barato & Seifert 2017 added to Nearest Existing Literature. Caveat: under the 2026-07-25 redefinition λ is no longer a coherence, so this compares only against the original "phase coherence" reading. P15 already has a banner. | Zhang, Cao, Ouyang & Tu 2020 *Nat. Phys.* 16:95 (MS: PMC7363412 results + Eq. 15 via fetch); Cao 2015; Barato & Seifert 2017 |
| 14 | B5 "Why It Matters Here" (holographic) | Total erasure cost ≤ A·k_BT ln 2 / 4ℓ_P² | **Q** | S ≤ A/4ℓ_P² is in units of k_B (nats), so the erasure-cost bound is kT·A/4ℓ_P², without the ln 2; T is also unspecified. | Main session's arithmetic (Supported) |
| 15 | INFO1 "What It Claims", Constraint Category | Shannon entropy is unique given "continuity, symmetry, and additivity for independent variables" | **E** | Additivity for independent variables does not single out Shannon entropy (Rényi entropies share it). Shannon's uniqueness uses the **grouping / chain-rule** (strong additivity) property; the Aczél–Forte–Ng route needs subadditivity and "small for small probabilities" as well. | Wikipedia "Entropy (information theory)", an existing anchor (MS: read via fetch); Rényi 1961 (not read) |
| 16 | INFO5 Mathematical Archetype | "Irreversible operations (like lossy compression) increase K relative to the original" | **E** | Wrong direction: K(f(x)) ≤ K(x) + K(f) + O(1), so computable processing cannot raise K by more than the program's own complexity. Lossy compression typically lowers it. | Li & Vitányi (anchored textbook; not re-read) |
| 17 | INFO5 cross-ref to B5 | "Minimum energy to erase the description of x is K(x) × kT ln 2" | **Q** | Zurek's 1989 proposal: deterministic computation, up to constants, with K uncomputable. Kolchinsky 2023 shows the cost can be paid in heat, noise or protocol complexity. | Zurek 1989; Kolchinsky 2023 PRE 108:034101 (abstract) |
| 18 | IT03 cross-ref | kT ln 2 "equals kT times the KL divergence between the initial and erased states" | **Q** | Direction-dependent: D(erased‖initial) = ln 2, while the reverse is infinite. The general statement is W − ΔF_eq ≥ kT·ΔD(ρ‖ρ_eq). | Esposito & Van den Broeck 2011 |
| 19 | CS11 cross-ref | Sorting's minimum cost = Ω(n log n) comparisons × kT ln 2 | **Q** | Right size, wrong reason: comparisons can be done reversibly. The unavoidable cost is discarding the input order, kT ln(n!) ≈ kT n ln n, and it is zero if the permutation is kept. | Sub-agent derivation from Landauer and Bennett (Supported; no primary source on sorting) |
| 20 | E2 "Why It Matters Here" | "At the historical rate the Landauer limit would be reached around 2080"; "state of the art (2025) ~10⁻¹⁹ J/op, ~35×" | **E / unsourced** | Koomey et al. 2011 never mentions Landauer and projects no year (sub-agent read the full text). Secondary sources extrapolate ~2048–2050 at the 1.57-year doubling, and the trend slowed after ~2000. The 10⁻¹⁹ J figure needs a source or should be removed. | Koomey et al. 2011 *IEEE Ann. Hist. Comput.* 33:46 |
| 21 | B5 "What The Math Says" | Reversible (quantum) computing "can avoid this cost entirely" | **Q** | No floor in principle, but ancilla preparation, garbage disposal, finite speed and error-correction resets all pay it in practice. | Bennett 1982; sub-agent (search summary on QEC) |
| 22 | F1 Formula and "What's Established" | V_controller ≥ V_system − V_channel; the law "follows directly from Shannon's channel coding theorem" | **E** | Ashby's law in log-variety form: H(outcomes) ≥ H(disturbance) − H(regulator). It follows from elementary entropy inequalities, not the channel coding theorem. The rigorous control version is Touchette & Lloyd 2000 (PRL 84:1156; not read this session, verify). The "kT ln 2 per bit suppressed" link is a heuristic; the formal route is Sagawa–Ueda feedback thermodynamics. The "four layers needed, five observed" mitochondrial argument is internal (DS 2.0) content inside an Established entry: label it so. | Ashby 1956 ch. 11 (anchored, not re-read); main session's assessment |
| 23 | TD3 DS Cross-References | AlphaEntropy firms "at thermodynamic equilibrium … consistent with maximum work extraction occurring at equilibrium" | **E** (physics) | No work can be extracted from a system at equilibrium. Maximum *power* occurs away from equilibrium: η at maximum power is ½ in linear response (Van den Broeck 2005; Schmiedl & Seifert 2008). Label the AlphaEntropy passage as analogy and remove the physics claim. | Sub-agent (motors), search summary for Van den Broeck |
| 24 | NE06 TD3 cross-ref and Mathematical Form | England's theory: "organisms maximise entropy production"; bound written as ⟨ΔS⟩ ≥ −Δs_int + log(n_rep/n_init) | **Q / verify** | England 2013's abstract derives a *lower bound* on heat production in terms of growth rate, internal entropy and durability. It does not say organisms maximise entropy production. Check the formula against England's equation (it should involve growth and decay rates). Note Kolchinsky 2024's critique (arXiv:2404.01130): no universal link between dissipation and replicator rates. | England 2013 abstract (MS: arXiv:1209.1179); Kolchinsky 2024 (sub-agent) |
| 25 | IT06 (adjacent) | "Minimum-dissipation paths are geodesics on the Fisher–Rao manifold"; Jarzynski "s_tot = β(W − ΔF)" | **Q / verify** | Sivak & Crooks 2012 derive a **friction-tensor** metric (linear response), not the Fisher–Rao metric in general. Jarzynski needs an equilibrium initial state. **Flag:** X8's "Seifert's bound ⟨W_diss⟩ ≥ d_geodesic²/τ" and the Fisher–gravity analogy lean on this sentence. Recommend a separate check; out of QR-004's scope. | Sivak & Crooks 2012 arXiv:1201.4166 (MS: abstract) |
| 26 | INFO4 c-theorem text | The DPI "provides the information-theoretic proof that RG flow is irreversible" | **Q / verify** | Overstated: Zamolodchikov's proof uses reflection positivity, and the entropic proof (Casini–Huerta 2004) uses strong subadditivity of *quantum* entanglement entropy. Treat the DPI as an analogy. From knowledge, not read this session; separate check recommended. | — |
| 27 | INFO4 | RG04 cross-ref sentence and six concept tags duplicated | **H** | Deduplicate. | Direct read |
| 28 | F5 Mathematical Archetype | Lower edge "from quantum tunnelling rates", upper edge "from thermal denaturation" | **H** (self-contradiction) | Its own body gives ATP failure and oxidative damage. The B5→F5 link "sets minimum energy cost of biological information processing" has no bearing on the O₂ corridor. F5 is already flagged as an internal construction. | Direct read |

**Pattern (for the drift catalogue).** Errors 3–6, 9, 10, 12, 13, 19 and 21 share one shape: **Landauer applied to operations that are not erasures** (copying, encoding, spikes, comparisons, synchronization, "processing"). This is the same mistake that voided P15's motivation. Suggested tag: `landauer-scope-overreach`.

---

## (G) Candidate fold-in reference entries (owner decides; nothing written)

| # | Proposed entry | Core sources | Would correct / anchor |
|---|---|---|---|
| R1 | Logical vs thermodynamic reversibility (Bennett) | Bennett 1982; Sagawa 2014 | B5, BIO5, NE06, EM11 |
| R2 | Generalised and finite-time Landauer | Esposito & Van den Broeck 2011; Sagawa & Ueda 2009; Proesmans et al. 2020; Jun et al. 2014 | B5, IT03 |
| R3 | Thermodynamic uncertainty relation, with scope and violations | Barato & Seifert 2015; Gingrich et al. 2016; Horowitz & Gingrich 2020; Pietzonka 2022 | archetype boilerplate (error 2) |
| R4 | Kinetic proofreading | Hopfield 1974; Ninio 1975; Bennett 1979; Murugan et al. 2012 | BIO5 |
| R5 | Speed over accuracy in biological error correction | Banerjee et al. 2017; Yu et al. 2022 | BIO5 |
| R6 | Thermodynamics of biochemical copying | Ouldridge, Govern & ten Wolde 2017 PRX; Ouldridge & ten Wolde 2017 PRL; Andrieux & Gaspard 2008 | NE06, BIO5 |
| R7 | Physical limits of chemical sensing | Berg & Purcell 1977; Bialek & Setayeshgar 2005; ten Wolde et al. 2016 | — (gap) |
| R8 | Energy cost of sensing and adaptation | Lan et al. 2012; Sartori et al. 2014; Govern & ten Wolde 2014 (PRL, PNAS) | BIO10, F1 |
| R9 | Free-energy cost of biochemical oscillations and synchronization | Cao et al. 2015; Barato & Seifert 2017; Ohga et al. 2023; Zhang et al. 2020 | Q5, H3, B5 (error 13) |
| R10 | Metabolic cost of neural information | Laughlin et al. 1998; Attwell & Laughlin 2001 | B5, D1 |
| R11 | Energetic efficiency of cellular computation (and the open question) | Kempes et al. 2017; Yang et al. 2021 | B5, E2 |
| R12 | Molecular-motor energetics | Toyabe et al. 2010/2011; Ariga et al. 2018; Hwang & Hyeon 2018 | — (gap) |
| R13 | Information-limited chemotaxis | Mattingly et al. 2021; 2026 follow-up | — (gap) |

Several primary texts were read only at abstract level (Hopfield, Lan 2012, Laughlin 1998, Terauchi). Re-read them before a fold-in, as the EWS fold-in did.

---

## (H) Candidate sub-questions, and what would decide each

| # | Sub-question | What would decide it | Looks like |
|---|---|---|---|
| S1 | How far do cells sit from Landauer, and why? | Already answered (§C, Kempes, Laughlin, Bennett) | **Answered → FOLD** (`found-under-other-vocabulary`) |
| S2 | Do proofreading enzymes sit on their error–cost bound? | Already answered: polymerase near it, ribosome far; speed is prioritised | **Answered → FOLD** |
| S3 | What does coherence or synchronization cost? (P15/Q5's honest form) | Answered in mean-field (Zhang 2020; Cao 2015; Barato & Seifert 2017) | **Answered → FOLD**; contradicts the ansatz |
| S4 | Does a sensing or regulation process sit near the TUR when dissipation is **measured**, not modelled? | Calorimetry or hidden-dissipation methods (Harada–Sasa, variance sum rule as in Di Terlizzi et al. 2024 *Science*) on a signalling network, plus its output precision | **Open in literature** (Yang 2021; Horowitz & Gingrich 2020). Experimental; not decidable by us |
| S5 | Does surplus dissipation buy fitness? (KaiC: ~16 ATP vs ~2 needed) | KaiC ATPase mutants with the same period but different ATP use: measure synchrony, coherence and competitive fitness under light–dark cycles | **Open in literature** (Zhang 2020 prediction; Yang 2021). Experimental; not decidable by us |
| S6 | Does the synchronization-dissipation threshold depend on network topology or spatial dimension (finite-d lattices, fractal networks), beyond Zhang's mean-field? | Simulate thermodynamically consistent stochastic phase oscillators on lattices and networks of varying dimension; measure the critical dissipation and the cost–r curve | **Possible narrow angle, unverified.** Prior art likely: Kuramoto-on-lattices phase-ordering results (lower critical dimension; e.g. Hong, Chaté, Park & Tang 2005/2007; not checked) and the 2026 Chudak / Burnet preprints. Decidable in-house with compute. **Drift warning:** this revives the wiki's d_f thread, where the owner's prior is strongest |
| S7 | Do Landauer or TUR bounds say anything rigorous at organism or ecosystem scale? | A defined Markov model with identifiable currents and a bath at that scale | **Likely DROP** (`ill-posed` / `expert-avoided-for-known-reason`): the bounds need conditions ecosystems do not meet; MEP-style claims have failed |

**Gate prognosis (not a gate run).**
- **S1–S3** would fail Gate 1 as answered; fold the answers in (R1, R4, R5, R9, R10, R11).
- **S4 and S5** are real open problems that others frame. Gate 1 would return `open-in-literature`. Gate 2 would likely find them sound but **undecidable with data we can obtain** (wet-lab), so: record them, don't pursue.
- **S6** is the only candidate that might reach PROCEED and that we could decide ourselves. It needs a dedicated prior-art search first, and the drift warning applies.
- **S7** looks like DROP.

Leaning, as instructed, toward "already answered": **QR-004's first half is answered; its second half is an open, experimental question owned by others.**

---

## (I) Sources and reading markers

**Markers:**
- "full text (direct)": the agent extracted and read the body.
- "full text (fetch)": a fetch tool read the body and summarised it.
- "abstract".
- "search summary": snippet or secondary source only.

**MS** = what the main session checked itself: "cit" means title, venue and year confirmed; "abs" means abstract read; "ft" means body read through a fetch tool. Nothing below is upgraded.

| Source | Marker (sub-agent) | MS |
|---|---|---|
| Landauer 1961, *IBM J. Res. Dev.* 5:183, doi:10.1147/rd.53.0183 | full text (direct, §§1, 3, 4) | — |
| Bennett 1982, *Int. J. Theor. Phys.* 21:905, doi:10.1007/BF02084158 | full text (direct, selected sections) | — |
| Bennett 1979, *BioSystems* 11:85 (DOI unconfirmed) | abstract | — |
| Zurek 1989, *PRA* 40:4731 | search summary | — |
| Kolchinsky 2023, *PRE* 108:034101, arXiv:2301.06838 | abstract | — |
| Sagawa & Ueda 2009, *PRL* 102:250602 | abstract | — |
| Sagawa 2014, *J. Stat. Mech.* P03025 | search summary | — |
| Esposito & Van den Broeck 2011, *EPL* 95:40004, arXiv:1104.5165 | full text (fetch) | — |
| Reeb & Wolf 2014, *NJP* 16:103011 | abstract | — |
| Piechocinska 2000, *PRA* 61:062314 | search summary | — |
| Parrondo, Horowitz & Sagawa 2015, *Nat. Phys.* 11:131 | search summary | — |
| Proesmans, Ehrich & Bechhoefer 2020, *PRL* 125:100602 | full text (fetch, main text) | — |
| Wolpert 2019, *J. Phys. A* 52:193001 | full text (fetch, first third) | — |
| Bérut et al. 2012, *Nature* 483:187, doi:10.1038/nature10872 | full text (fetch; equations missed) | cit (search) |
| Jun, Gavrilov & Bechhoefer 2014, *PRL* 113:190601, arXiv:1408.5089 | full text (fetch) | cit (search) |
| Hong et al. 2016, *Sci. Adv.* 2:e1501492 | full text (fetch; inconsistent extraction) | — |
| Gaudenzi et al. 2018, *Nat. Phys.* 14:565 | preprint full text (fetch); published version search summary | — |
| Yan et al. 2018, *PRL* 120:210601 | full text (fetch) | — |
| Toyabe et al. 2010, *Nat. Phys.* 6:988 | abstract | — |
| Norton 2005, *SHPMP* 36:375; Norton 2011, *SHPMP* 42:184 | search summary / not retrieved | — |
| Ladyman & Robertson 2014, *Entropy* 16:2278 | search summary | — |
| López-Suárez, Neri & Gammaitoni 2016, *Nat. Commun.* 7:12068; Kish 2016, *FNL* 15:1620001, arXiv:1606.09493 | search summary / abstract | — |
| Kempes, Wolpert, Cohen & Pérez-Mercader 2017, *Phil. Trans. R. Soc. A* 375:20160343, arXiv:1706.05043 | full text (fetch, arXiv) | abs ("about an order of magnitude") |
| Laughlin, de Ruyter van Steveninck & Anderson 1998, *Nat. Neurosci.* 1:36 | search summary | — |
| Attwell & Laughlin 2001, *JCBFM* 21:1133 | search summary | — |
| Lynch & Marinov 2015, *PNAS* 112:15690 | full text (fetch) | — |
| Yang et al. 2021, *PNAS* 118:e2026786118 (PMC8255778) | full text (fetch) | ft (Introduction; "Open Question" sections) |
| Ouldridge, Govern & ten Wolde 2017, *PRX* 7:021004, arXiv:1503.00909 | full text (fetch, first ⅔) | — |
| Ouldridge & ten Wolde 2017, *PRL* 118:158103, arXiv:1609.05554 | full text (fetch) | cit (arXiv page) |
| Andrieux & Gaspard 2008, *PNAS* 105:9516 | full text (fetch) | — |
| Koomey et al. 2011, *IEEE Ann. Hist. Comput.* 33(3):46 | full text (direct) | — |
| Barato & Seifert 2015, *PRL* 114:158101, arXiv:1502.05944 | full text | abs |
| Gingrich, Horowitz, Perunov & England 2016, *PRL* 116:120601 | full text (main results) | — |
| Horowitz & Gingrich 2017, *PRE* 96:020103 | abstract | — |
| Horowitz & Gingrich 2020, *Nat. Phys.* 16:15 | full text | — |
| Pietzonka, Barato & Seifert 2016, *J. Stat. Mech.* 124004 | full text | — |
| Pietzonka 2022, *PRL* 128:130606 | abstract + intro | — |
| Barato, Chetrite, Faggionato & Gabrielli 2018, *NJP* 20:103023 | abstract | — |
| Brandner, Hanazato & Saito 2018, *PRL* 120:090601 | abstract + intro | — |
| Chun, Fischer & Seifert 2019, *PRE* 99:042128 | abstract + intro | — |
| Ptaszyński 2018, *PRB* 98:085425; Agarwalla & Segal 2018, *PRB* 98:155438 | abstract | — |
| Di Terlizzi & Baiesi 2019, *J. Phys. A* 52:02LT03 | abstract | — |
| Hwang & Hyeon 2018, *J. Phys. Chem. Lett.* 9:513, arXiv:1710.03499 | full text (main text) | abs |
| Song & Hyeon 2021, *J. Chem. Phys.* 154:130901, arXiv:2101.03673 | full text (key sections) | — |
| Ariga, Tomishige & Mizuno 2018, *PRL* 121:218101 | full text (direct) | — |
| Toyabe et al. 2010, *PRL* 104:198103; Toyabe et al. 2011, *PNAS* 108:17951 | full text (fetch) | — |
| Brown & Sivak 2020, *Chem. Rev.* 120:434 | full text (targeted sections) | — |
| Meister, Lowe & Berg 1987 (flagellar motor efficiency) | abstract | — |
| Schmiedl & Seifert 2008, *EPL* 83:30005; Van den Broeck 2005, *PRL* 95:190602 | search summary | — |
| Berg & Purcell 1977, *Biophys. J.* 20:193 | search summary | — |
| Bialek & Setayeshgar 2005, *PNAS* 102:10040 | abstract | — |
| Endres & Wingreen 2009, *PRL* 103:158101 | abstract | — |
| ten Wolde, Becker, Ouldridge & Mugler 2016, *J. Stat. Phys.* 162:1395 | full text (~93%) | — |
| Lan, Sartori, Neumann, Sourjik & Tu 2012, *Nat. Phys.* 8:422 | abstract (paywalled) | — |
| Wang, Lan & Tang 2015, arXiv:1505.07526 | full text | — |
| Sartori, Granger, Lee & Horowitz 2014, *PLoS Comput. Biol.* 10:e1003974 | full text (equations partly unreadable) | ft (abstract + discussion: "slightly larger than twice"; distinct from Landauer) |
| Mehta & Schwab 2012, *PNAS* 109:17978 | abstract | — |
| Govern & ten Wolde 2014, *PRL* 113:258102 | abstract | — |
| Govern & ten Wolde 2014, *PNAS* 111:17486 | full text (PMC) | — |
| Barato, Hartich & Seifert 2014, *NJP* 16:103024 | full text | — |
| Harvey, Lahiri & Ganguli 2023, *PRE* 108:014403 (venue unconfirmed), arXiv:2002.10567 | abstract | — |
| Mattingly, Kamino, Machta & Emonet 2021, *Nat. Phys.* 17:1426 (PMC8758097) | full text (PMC, ~92%) | cit (search) |
| Mattingly et al., *Nat. Phys.* 2026, "chemosensing accuracy is not limited by stochastic molecule arrivals" (preprint arXiv:2407.07264) | abstract / search summary | cit (search only) |
| Bryant & Machta 2023, *PRL* 131:068401 | search summary | — |
| Wolpert 2016, *Entropy* 18:138 | abstract | — |
| Hopfield 1974, *PNAS* 71:4135 | abstract | — |
| Ninio 1975, *Biochimie* 57:587 | search summary | — |
| Murugan, Huse & Leibler 2012, *PNAS* 109:12034 | full text (fetch; equations missed) | — |
| Sartori & Pigolotti 2013, *PRL* 110:188101; 2015, *PRX* 5:041039 | abstract | — |
| Banerjee, Kolomeisky & Igoshin 2017, *PNAS* 114:5183, doi:10.1073/pnas.1614838114 | full text (fetch, PMC5441828) | cit (search) |
| Yu, Kolomeisky & Igoshin 2022, *J. R. Soc. Interface* 19:20210883 | abstract | — |
| Song & Hyeon 2020, *J. Phys. Chem. Lett.* 11:3136 | abstract | — |
| Piñeros & Tlusty 2020, *PRE* 101:022415 | search summary | — |
| Lee, Popodi, Tang & Foster 2012, *PNAS* 109:E2774 | full text (fetch, PMC3478608) | cit + figure (search / BioNumbers) |
| Bębenek & Ziuzia-Graczyk 2018, *Curr. Genet.* 64:985 | full text (fetch) | — |
| Kunkel 2004, *J. Biol. Chem.* 279:16895 | citation metadata only | — |
| McKeithan 1995, *PNAS* 92:5042 | abstract | — |
| Cao, Wang, Ouyang & Tu 2015, *Nat. Phys.* 11:772, arXiv:1506.05686 | full text (fetch, arXiv version) | — |
| Barato & Seifert 2017, *PRE* 95:062409 | full text (fetch) | — |
| Oberreiter, Seifert & Barato 2022, *PRE* 106:014106 (not PRL) | full text (fetch) | — |
| Ohga, Ito & Kolchinsky 2023, *PRL* 131:077101 | abstract | — |
| Marsland, Cui & Horowitz 2019, *J. R. Soc. Interface* 16:20190098 | full text (intro, §§I–II) | — |
| Zhang, Cao, Ouyang & Tu 2020, *Nat. Phys.* 16:95, doi:10.1038/s41567-019-0701-7, arXiv:2001.10479 (PMC7363412) | full text (direct; §§II.C–E, SI) | ft (Eq. 11, 14, 15; mean-field) |
| Terauchi et al. 2007, *PNAS* 104:16377 | full text (fetch) / abstract (two agents differ) | — |
| Chew, Leypunskiy, Lin, Murugan & Rust 2018, *Nat. Commun.* | search summary | — |
| Chudak, Esposito & Ptaszyński 2026, *PRE* 113:034129; Burnet et al. 2026, arXiv:2604.24553 | abstract | — |
| England 2013, *J. Chem. Phys.* 139:121923, arXiv:1209.1179 | — | abs |
| Kolchinsky 2024, *J. Chem. Phys.*, arXiv:2404.01130 | abstract / search summary | — |
| Grinstein & Linsker 2007; Meysman & Bruers 2010, *Phil. Trans. R. Soc. B* | search summary | — |
| Sivak & Crooks 2012, *PRL* 108:190602, arXiv:1201.4166 | — | abs |
| Wikipedia, "Entropy (information theory)" (existing INFO1 anchor) | — | ft (first 100k characters) |

**Citation corrections the sub-agents made to the brief's starting list:**
- Oberreiter et al. is *PRE* 106:014106, not *PRL*.
- Toyabe "2011 PRL 104:198103" is the **2010** PRL; the 2011 paper is *PNAS* 108:17951.
- Tu 2008 *PNAS* is about the flagellar switch, not adaptation.
- Laughlin's ~10⁴ ATP per bit applies to a synapse; graded and spike signals cost ~10⁶–10⁷.
- Fei et al. 2018 is in *Nat. Commun.*, not *Nat. Phys.*.

Working notes (not in the repo): the sub-agents' files in the session scratchpad.

"""
Option E — Chunk 1: Biology + Chemistry expansion
Inserts 13 new reference_law entries into ds_wiki.db.
Safe to re-run: uses INSERT OR IGNORE on entries, checks sections/properties before inserting.
"""

import sqlite3
import os

SOURCE_DB = "/Users/iandarling/Library/Mobile Documents/com~apple~CloudDocs/Primary Work Outputs/wiki build/ds-wiki-repo/ds_wiki.db"

# ---------------------------------------------------------------------------
# Entry definitions
# Each entry: dict with keys matching entries table + 'sections' list + 'properties' list
# sections: list of (section_name, section_order, content)
# properties: list of (table_name, property_name, property_value, prop_order)
# links: list of (link_type, source_id, source_label, target_id, target_label, description)
# ---------------------------------------------------------------------------

ENTRIES = [

# ── BIOLOGY ────────────────────────────────────────────────────────────────

{
    "id": "BIO4",
    "title": "Cell Theory",
    "filename": "BIO4_cell_theory.md",
    "entry_type": "reference_law",
    "scale": "cellular · molecular",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "All living organisms are composed of one or more cells. The cell is the fundamental unit of structure and function in all life. All cells arise from pre-existing cells (omnis cellula e cellula — Virchow, 1855). This unifies the discontinuous, discrete structure of life: biological organisation is quantised at the cell."),
        ("Mathematical Form", 1,
         "Cell number N(t) = N₀ · 2^(t/T_d) under binary fission, where T_d = ln(2)/μ is the doubling time and μ is the specific growth rate."),
        ("Constraint Category", 2,
         "Informatic/Coordination (In/Co): cells are discrete information-processing and hereditary units. The constraint is combinatorial: no sub-cellular fragment is independently viable. Information is conserved and replicated through division."),
        ("DS Cross-References", 3,
         "BIO1 (Mendelian Laws — genetic information is encoded and replicated within cells). BIO5 (Central Dogma — information flow occurs within and between cells). F2 (Liebig's Law — limiting resources constrain cell growth rate). C1 (Metabolic Scaling — whole-organism metabolism sums over cells)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe total biological information content is conserved through cell division: daughter cells receive exact copies of the hereditary material. The exponential growth form N ~ 2^(t/T_d) is a discrete conservation law — no information is created or destroyed, only replicated."),
        ("What The Math Says", 5,
         "Cell number grows as a power of two: after n generations, N equals N-zero times 2 to the n. The doubling time T-d equals ln(2) divided by the specific growth rate mu. At the population scale, this yields exponential growth dN/dt = mu times N until resource limitation imposes a carrying capacity. The discreteness of cell division means biological information is transmitted in integer packets — no fractional cells."),
        ("Concept Tags", 6,
         "• cell theory\n• cell division\n• binary fission\n• doubling time\n• exponential growth\n• hereditary unit\n• biological organisation\n• omnis cellula e cellula\n• Virchow\n• discrete biological unit"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "cell theory, cell division, binary fission, doubling time, exponential growth, hereditary unit, biological organisation, omnis cellula e cellula, Virchow, discrete biological unit", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "BIO4", "Cell Theory", "BIO1", "Mendelian Laws of Inheritance", "Mendelian alleles are encoded and transmitted within and between cells; Cell Theory provides the physical substrate for genetic inheritance."),
        ("implements", "BIO4", "Cell Theory", "BIO5", "Central Dogma of Molecular Biology", "The Central Dogma operates within the cell; Cell Theory defines the boundary condition for all molecular information flows."),
        ("couples to", "BIO4", "Cell Theory", "C1", "Metabolic Scaling (Kleiber's Law)", "Whole-organism metabolic rate is the aggregate of cellular metabolic rates; cellular geometry sets the surface-to-volume constraint."),
    ],
},

{
    "id": "BIO5",
    "title": "Central Dogma of Molecular Biology",
    "filename": "BIO5_central_dogma.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Genetic information flows in one direction: DNA → RNA → Protein (Crick, 1958). The sequence information in DNA is transcribed into messenger RNA, which is then translated into protein. Information can flow DNA→DNA (replication) and RNA→DNA (reverse transcriptase, as in retroviruses), but protein sequence information is never back-translated into nucleic acid. The protein's amino acid sequence is the terminal sink of sequence information."),
        ("Mathematical Form", 1,
         "Information flow: DNA →[transcription]→ mRNA →[translation]→ Protein\nCodon table: 4³ = 64 codons → 20 amino acids + 3 stop codons (degenerate code)\nReplication fidelity: error rate ~10⁻⁹ per base per replication (with proofreading)"),
        ("Constraint Category", 2,
         "Informatic (In): a strict one-way information flow constraint. The encoding is many-to-one (degenerate genetic code) and irreversible at the protein level. This is the molecular implementation of Crick's sequence hypothesis: once information enters protein, it cannot escape."),
        ("DS Cross-References", 3,
         "Ax1 (Information Primacy — the Central Dogma instantiates directional information flow as a physical law). B5 (Landauer's Principle — transcription and translation are irreversible information operations with thermodynamic cost). BIO1 (Mendelian Laws — alleles in DNA are the physical substrate of Mendelian factors). BIO4 (Cell Theory — all Central Dogma operations occur within the cell boundary)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nSequence information is conserved but not created during transcription and translation: the amino acid sequence is a deterministic function of the nucleotide sequence via the codon table. The degeneracy of the code (multiple codons → one amino acid) is a many-to-one projection that preserves protein-level information while discarding synonymous nucleotide variation."),
        ("What The Math Says", 5,
         "The genetic code maps 64 possible codons (4-cubed triplets of the four nucleotides A, C, G, T) onto 20 amino acids plus three stop signals. This is a surjective but not injective mapping — information is preserved in the direction DNA to protein but cannot be inverted: knowing the protein sequence does not uniquely determine the DNA sequence due to degeneracy. Replication polymerases achieve error rates of approximately 10 to the minus 9 per base, so a human genome of 3 times 10 to the 9 bases accumulates roughly 3 mutations per cell division."),
        ("Concept Tags", 6,
         "• central dogma\n• DNA transcription\n• RNA translation\n• genetic code\n• codon table\n• replication fidelity\n• reverse transcriptase\n• sequence information\n• Crick\n• molecular information flow"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "central dogma, DNA transcription, RNA translation, genetic code, codon table, replication fidelity, reverse transcriptase, sequence information, Crick, molecular information flow", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "BIO5", "Central Dogma of Molecular Biology", "Ax1", "Ax1: Information Primacy", "The Central Dogma is the molecular implementation of information primacy: sequence information is the fundamental substrate of biological structure and function."),
        ("couples to", "BIO5", "Central Dogma of Molecular Biology", "B5", "B5: Landauer's Principle", "Each irreversible step (transcription, translation) has a minimum thermodynamic cost; gene expression is a thermodynamically irreversible information operation."),
        ("derives from", "BIO5", "Central Dogma of Molecular Biology", "BIO1", "Mendelian Laws of Inheritance", "Mendelian factors (alleles) are physically instantiated as DNA sequences; the Central Dogma explains how allelic information produces phenotype."),
    ],
},

{
    "id": "BIO6",
    "title": "Michaelis–Menten Enzyme Kinetics",
    "filename": "BIO6_michaelis_menten.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The rate of an enzyme-catalysed reaction increases hyperbolically with substrate concentration [S]. At low [S], rate is approximately linear (first-order); at high [S], rate saturates at Vmax (zero-order). The Michaelis constant Km is the substrate concentration at half-maximal rate and approximates the enzyme–substrate dissociation constant. This is the quantitative foundation of enzyme kinetics (Michaelis & Menten, 1913)."),
        ("Mathematical Form", 1,
         "v = (Vmax · [S]) / (Km + [S])\nVmax = kcat · [E]total\nKm ≈ (k₋₁ + kcat) / k₁  (Briggs-Haldane)"),
        ("Constraint Category", 2,
         "Thermodynamic bound (Th): Vmax sets the physical ceiling on reaction rate, determined by the concentration of active enzyme and the catalytic rate constant kcat. Km encodes the binding geometry. The hyperbolic form arises from the conservation of enzyme: [E]total = [E]free + [ES]."),
        ("DS Cross-References", 3,
         "F4 (Saturation Dynamics — Michaelis-Menten is the canonical saturation curve; F4 generalises this to multi-state systems). B2 (Arrhenius — kcat and Km are temperature-dependent via Arrhenius; enzyme activity has an optimal temperature). KC1 (Le Chatelier — the enzyme-substrate binding equilibrium shifts with concentration changes). CHEM5 (Mass Action Rate Law — Michaelis-Menten is a special case of mass action kinetics at steady-state)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: sigmoid-saturation\n\nThe hyperbolic (Michaelis-Menten) curve v([S]) = Vmax·[S]/(Km+[S]) is the simplest saturation function: linear at [S] << Km, flat at [S] >> Km. It is the first-order Taylor expansion of a sigmoid and arises whenever a carrier (enzyme, receptor, transporter) has finite capacity and obeys mass conservation."),
        ("What The Math Says", 5,
         "Reaction velocity v equals V-max times substrate concentration divided by the sum of K-m and substrate concentration. When substrate concentration equals K-m, the velocity is exactly half V-max — this is the operational definition of K-m. V-max equals the catalytic rate constant k-cat multiplied by total enzyme concentration. At low substrate (much less than K-m), the equation reduces to v approximately equal to (V-max over K-m) times substrate concentration — a linear, first-order regime. At high substrate (much greater than K-m), v approaches V-max asymptotically — a zero-order, saturated regime."),
        ("Concept Tags", 6,
         "• Michaelis-Menten\n• enzyme kinetics\n• substrate concentration\n• Vmax saturation\n• Km dissociation constant\n• kcat catalytic rate\n• hyperbolic kinetics\n• enzyme-substrate complex\n• Briggs-Haldane\n• biochemical rate law"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Michaelis-Menten, enzyme kinetics, substrate concentration, Vmax saturation, Km dissociation constant, kcat catalytic rate, hyperbolic kinetics, enzyme-substrate complex, Briggs-Haldane, biochemical rate law", 0),
        ("DS Facets", "mathematical_archetype", "sigmoid-saturation", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "BIO6", "Michaelis–Menten Enzyme Kinetics", "F4", "F4: Saturation Dynamics (Consolidated)", "Michaelis-Menten is the foundational saturation curve; F4 extends this principle to multi-state biological saturation systems."),
        ("derives from", "BIO6", "Michaelis–Menten Enzyme Kinetics", "KC1", "Le Chatelier's Principle", "The enzyme-substrate binding equilibrium obeys Le Chatelier: increasing substrate concentration drives reaction forward until enzyme saturation."),
        ("couples to", "BIO6", "Michaelis–Menten Enzyme Kinetics", "B2", "B2: Arrhenius Equation", "kcat follows an Arrhenius temperature dependence; enzyme kinetics has a characteristic activation energy and temperature optimum."),
    ],
},

{
    "id": "BIO7",
    "title": "Lotka–Volterra Predator–Prey Equations",
    "filename": "BIO7_lotka_volterra.md",
    "entry_type": "reference_law",
    "scale": "population",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Two-species predator–prey dynamics produce undamped cyclic oscillations in population sizes. Prey grows exponentially in the absence of predators; predators decline exponentially without prey. The interaction terms (βxy and δxy) couple the populations, producing periodic orbits around a neutrally stable equilibrium. No species permanently excludes the other; populations co-oscillate indefinitely in the absence of additional damping (Lotka 1925, Volterra 1926)."),
        ("Mathematical Form", 1,
         "dx/dt = αx − βxy  (prey: α = growth rate, β = predation rate)\ndy/dt = δxy − γy  (predator: δ = conversion efficiency, γ = death rate)\nEquilibrium: x* = γ/δ, y* = α/β\nConserved quantity: V = δx − γ ln x + βy − α ln y = constant"),
        ("Constraint Category", 2,
         "Dynamical (Di): coupled nonlinear ODEs with a conserved quantity V (a Lyapunov-like functional). The oscillatory solutions arise from the antisymmetric coupling: prey increase drives predator increase which drives prey decrease. No dissipation → neutrally stable orbits rather than limit cycles."),
        ("DS Cross-References", 3,
         "F3 (Gause's Competitive Exclusion — competitive dynamics are the two-species same-resource analog; predator-prey is the trophic version). F4 (Saturation Dynamics — the logistic modification of Lotka-Volterra introduces saturation into prey growth). C1 (Metabolic Scaling — predator-prey energy transfer efficiency ~10% per trophic level). C3 (Heavy-Tailed Distributions — population fluctuations in real ecosystems show heavy tails beyond Lotka-Volterra predictions)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: oscillatory\n\nThe Lotka-Volterra system generates closed periodic orbits in (x, y) phase space. The conserved quantity V is a first integral of the system, analogous to energy conservation in a Hamiltonian system. The frequency of oscillation depends on the geometric mean of the growth and predation parameters: ω ≈ √(αγ). This is the simplest nonlinear oscillator arising from ecological coupling."),
        ("What The Math Says", 5,
         "Prey population x and predator population y obey coupled differential equations. Prey grows at rate alpha in isolation and is removed at rate beta times x times y. Predators grow at rate delta times x times y from predation and die at rate gamma. The equilibrium is x-star equals gamma over delta and y-star equals alpha over beta. Small perturbations around this equilibrium lead to oscillations with angular frequency approximately the square root of alpha times gamma. The system conserves a quantity V equal to delta x minus gamma log x plus beta y minus alpha log y, making the orbits closed curves in phase space."),
        ("Concept Tags", 6,
         "• Lotka-Volterra\n• predator-prey dynamics\n• population oscillations\n• trophic coupling\n• ecological cycles\n• coupled ODEs\n• phase space orbits\n• prey growth rate\n• predation rate\n• ecological equilibrium"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "Lotka-Volterra, predator-prey dynamics, population oscillations, trophic coupling, ecological cycles, coupled ODEs, phase space orbits, prey growth rate, predation rate, ecological equilibrium", 0),
        ("DS Facets", "mathematical_archetype", "oscillatory", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "BIO7", "Lotka–Volterra Predator–Prey Equations", "F3", "F3: Gause's Competitive Exclusion Principle", "Competitive exclusion and predator-prey are the two fundamental two-species interaction archetypes; Lotka-Volterra is the predator-prey complement to Gause's competitive dynamics."),
        ("generalizes", "BIO7", "Lotka–Volterra Predator–Prey Equations", "F4", "F4: Saturation Dynamics (Consolidated)", "The logistic-Lotka-Volterra extension introduces prey saturation (carrying capacity), bridging pure oscillatory dynamics with saturation constraints."),
        ("analogous to", "BIO7", "Lotka–Volterra Predator–Prey Equations", "D2", "D2: Feigenbaum Universality", "Both describe the onset of complex oscillatory and chaotic dynamics from simple deterministic rules; Lotka-Volterra with logistic prey can exhibit period-doubling cascades."),
    ],
},

{
    "id": "BIO8",
    "title": "Neutral Theory of Molecular Evolution",
    "filename": "BIO8_neutral_theory.md",
    "entry_type": "reference_law",
    "scale": "population",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The majority of molecular evolutionary changes (amino acid and nucleotide substitutions) are selectively neutral — neither advantageous nor deleterious — and spread through populations by random genetic drift rather than natural selection (Kimura, 1968). The rate of neutral molecular evolution k equals the neutral mutation rate μ_n, independent of population size N. This generates the molecular clock: sequence divergence accumulates linearly with time."),
        ("Mathematical Form", 1,
         "Rate of substitution: k = μ_n  (independent of N)\nFixation probability of neutral mutation: P_fix = 1/(2N)\nMutation rate neutrally fixed per generation: k = μ_n = 2N · μ_total · f_0 · (1/2N) = μ_total · f_0\nSequence divergence: d = 2μ_n · t"),
        ("Constraint Category", 2,
         "Informatic (In): neutral mutations are random walks through sequence space. The rate of fixation is set by mutation rate alone, not by selection. This is a null model: any departure from k = μ_n signals selection."),
        ("DS Cross-References", 3,
         "BIO3 (Fisher's Fundamental Theorem — selective evolution operates in the complementary regime where mutations are not neutral). BIO2 (Hardy-Weinberg — the equilibrium model assumes neutrality; Neutral Theory extends this to the dynamic process of fixation). BIO9 (Molecular Clock — the direct empirical consequence of Neutral Theory). BIO1 (Mendelian Laws — allele frequency dynamics under neutrality follow binomial sampling rather than selection)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: statistical-distribution\n\nNeutral allele frequencies follow a diffusion process governed by genetic drift. The stationary distribution of allele frequencies under neutrality is the beta distribution. The time to fixation of a neutral mutation has expectation 4N generations. The molecular clock is the ensemble mean of this stochastic process: d(t) = 2μ_n t describes the expected sequence divergence as a Poisson process."),
        ("What The Math Says", 5,
         "A neutral mutation that arises once in a diploid population of size N has fixation probability 1 over 2N. Each generation, 2N times mu total new mutations arise, of which fraction f-zero are neutral. The per-generation neutral fixation rate k equals 2N times mu-total times f-zero times 1 over 2N, which simplifies to mu-total times f-zero — population size cancels completely. Therefore the molecular evolutionary rate k equals the neutral mutation rate, independent of population size. Sequence divergence d between two lineages separated for time t equals 2 times k times t (factor of 2 for two independent lineages)."),
        ("Concept Tags", 6,
         "• neutral theory\n• molecular evolution\n• genetic drift\n• fixation probability\n• molecular clock\n• Kimura\n• neutral mutation rate\n• sequence divergence\n• random walk evolution\n• selectively neutral"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "neutral theory, molecular evolution, genetic drift, fixation probability, molecular clock, Kimura, neutral mutation rate, sequence divergence, random walk evolution, selectively neutral", 0),
        ("DS Facets", "mathematical_archetype", "statistical-distribution", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("tensions with", "BIO8", "Neutral Theory of Molecular Evolution", "BIO3", "Natural Selection — Fisher's Fundamental Theorem", "Fisher's theorem describes the rate of increase of fitness under selection; Neutral Theory describes the complementary regime where selection is absent. The two form the complete picture of molecular evolution."),
        ("derives from", "BIO8", "Neutral Theory of Molecular Evolution", "BIO2", "Hardy–Weinberg Principle", "Hardy-Weinberg describes allele frequency equilibrium under neutrality in infinite populations; Neutral Theory extends this to finite populations where drift drives fixation."),
        ("predicts for", "BIO8", "Neutral Theory of Molecular Evolution", "BIO9", "Molecular Clock Hypothesis", "The molecular clock is the primary empirical prediction of Neutral Theory: linear accumulation of substitutions with time follows directly from k = μ_n."),
    ],
},

{
    "id": "BIO9",
    "title": "Hodgkin–Huxley Action Potential Model",
    "filename": "BIO9_hodgkin_huxley.md",
    "entry_type": "reference_law",
    "scale": "cellular · molecular",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The electrical dynamics of a neuron's membrane are governed by voltage-gated ion channel conductances. An action potential is an all-or-nothing, threshold-triggered nonlinear wave: below threshold, perturbations decay; above threshold, the membrane fires a stereotyped spike and enters a refractory period. The model (Hodgkin & Huxley, 1952) won the 1963 Nobel Prize and remains the quantitative foundation of computational neuroscience."),
        ("Mathematical Form", 1,
         "C_m dV/dt = I_ext − ḡ_Na m³h(V − E_Na) − ḡ_K n⁴(V − E_K) − ḡ_L(V − E_L)\nGating variables m, h, n each obey: dw/dt = (w_∞(V) − w) / τ_w(V)\nThreshold: V_th ≈ −55 mV; resting potential: V_rest ≈ −70 mV"),
        ("Constraint Category", 2,
         "Dynamical/Geometric (Di/Ge): the cable geometry of the axon determines propagation speed (v ∝ √d for unmyelinated, v ∝ d for myelinated axons). Ion channel gating kinetics set the threshold, spike shape, and refractory period. The system is a nonlinear dynamical system with a stable limit cycle (the action potential) separated from the resting fixed point by a saddle."),
        ("DS Cross-References", 3,
         "F4 (Saturation Dynamics — ion channel conductances saturate; gating variables m, h, n are sigmoid-bounded). B2 (Arrhenius — channel kinetics are temperature-dependent; Q₁₀ ≈ 3 for most ion channels). C1 (Metabolic Scaling — neural spike energy cost is ~10⁻¹² J/spike; scales with brain mass). H3 (Phase Coherence — neural synchrony across populations is a coherence phenomenon built on individual action potentials). BIO6 (Michaelis-Menten — ion pump dynamics that restore resting potential follow saturation kinetics)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: threshold-transition\n\nThe Hodgkin-Huxley model is the canonical threshold dynamical system. The action potential is an all-or-nothing nonlinear event: below threshold the system returns to rest; above threshold it executes a fixed-amplitude, fixed-duration excursion. This is the biological implementation of a first-order phase transition in the membrane's electrical state — a sharp transition from sub-threshold to supra-threshold dynamics."),
        ("What The Math Says", 5,
         "The membrane capacitance C-m times the rate of change of voltage equals the sum of external current and three ionic currents. Sodium current is proportional to the cube of activation variable m times inactivation variable h times the driving force (V minus reversal potential E-Na). Potassium current is proportional to the fourth power of activation variable n times its driving force. The leak current provides linear restoring force. The gating variables m, h, n each relax toward voltage-dependent steady-state values with voltage-dependent time constants. The resulting system produces threshold-triggered spikes of approximately 100 mV amplitude and 1 ms duration."),
        ("Concept Tags", 6,
         "• action potential\n• Hodgkin-Huxley\n• voltage-gated ion channels\n• membrane potential\n• threshold dynamics\n• neural spike\n• conductance-based model\n• sodium channel\n• potassium channel\n• refractory period"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "action potential, Hodgkin-Huxley, voltage-gated ion channels, membrane potential, threshold dynamics, neural spike, conductance-based model, sodium channel, potassium channel, refractory period", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "BIO9", "Hodgkin–Huxley Action Potential Model", "F4", "F4: Saturation Dynamics (Consolidated)", "Ion channel gating variables are bounded between 0 and 1; the sigmoid-shaped steady-state activation curves are saturation dynamics applied to membrane conductance."),
        ("couples to", "BIO9", "Hodgkin–Huxley Action Potential Model", "H3", "H3: Phase Coherence (λ)", "Synchronised action potential firing across neural populations is a collective coherence phenomenon; H3's phase coherence parameter λ quantifies this synchrony."),
        ("derives from", "BIO9", "Hodgkin–Huxley Action Potential Model", "B2", "B2: Arrhenius Equation", "All Hodgkin-Huxley gating rate constants are temperature-dependent with Q₁₀ ≈ 3, following Arrhenius kinetics — the biological implementation of thermally-activated rate processes."),
    ],
},

{
    "id": "BIO10",
    "title": "Homeostasis Principle",
    "filename": "BIO10_homeostasis.md",
    "entry_type": "reference_law",
    "scale": "organismal",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Living organisms actively maintain their internal environment (milieu intérieur) within narrow bounds despite external perturbations, through negative feedback mechanisms (Bernard, 1865; Cannon, 1932). Homeostasis is not equilibrium but a dynamically maintained steady state requiring continuous energy expenditure. The set-point is defended against perturbations; deviations trigger compensatory responses proportional to the error."),
        ("Mathematical Form", 1,
         "Generic feedback controller: dX/dt = −k(X − X_set) + d(t)\nSteady state: X_ss = X_set + d/k  (error proportional to disturbance d and inversely to gain k)\nEnergy cost of homeostasis ∝ k · σ²(d)  (maintaining tighter control of larger disturbances costs more)"),
        ("Constraint Category", 2,
         "Coordination/Control (Co): negative feedback coordination maintains set-point. The controller must have sufficient gain (Ashby's Law: requisite variety) to counteract disturbances. Homeostasis is a thermodynamically open steady state — it requires energy input to maintain; it is not an equilibrium."),
        ("DS Cross-References", 3,
         "F1 (Ashby's Law of Requisite Variety — the controller's variety must match the disturbance's variety; homeostasis requires sufficient regulatory complexity). KC1 (Le Chatelier's Principle — the physical analog: systems at equilibrium respond to perturbations by opposing them; homeostasis is the biological extension beyond equilibrium). TD3 (Second Law — maintaining homeostasis requires continuous energy expenditure to counteract entropy production). H3 (Phase Coherence — physiological homeostasis maintains coherent phase relationships among organ systems)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nHomeostasis is a dynamically maintained fixed point: the set-point X_set is a stable attractor of the controlled system. Unlike thermodynamic equilibrium, it is maintained far from equilibrium by energy input. The feedback gain k determines the basin of attraction width and the energy cost of maintaining the set-point against stochastic disturbances."),
        ("What The Math Says", 5,
         "The internal variable X (e.g., body temperature, blood glucose, blood pH) is governed by the differential equation dX/dt equals minus k times the difference between X and X-set plus a disturbance term d of t. The feedback gain k determines how rapidly errors are corrected. At steady state, X equals X-set plus d over k: smaller deviations from set-point require higher gain k. The energetic cost of maintaining homeostasis scales with k times the variance of the disturbance: tighter control of larger fluctuations requires more energy. This is the biological form of the fluctuation-dissipation relationship."),
        ("Concept Tags", 6,
         "• homeostasis\n• negative feedback\n• set-point regulation\n• milieu intérieur\n• Claude Bernard\n• Cannon\n• physiological control\n• steady state\n• feedback gain\n• allostasis"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Co", 0),
        ("entries", "concept_tags", "homeostasis, negative feedback, set-point regulation, milieu intérieur, Claude Bernard, Cannon, physiological control, steady state, feedback gain, allostasis", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "BIO10", "Homeostasis Principle", "F1", "F1: Ashby's Law of Requisite Variety", "Ashby's Law is the information-theoretic foundation of homeostasis: the regulatory system must have variety at least equal to the disturbance variety it must counteract."),
        ("analogous to", "BIO10", "Homeostasis Principle", "KC1", "Le Chatelier's Principle", "Le Chatelier describes equilibrium systems opposing perturbations; homeostasis is the non-equilibrium biological analog: active negative feedback rather than passive equilibrium restoration."),
        ("couples to", "BIO10", "Homeostasis Principle", "C1", "C1: Metabolic Scaling (Kleiber's Law)", "The energetic cost of homeostasis contributes to basal metabolic rate; endotherms expend ~80% of resting metabolism on thermoregulation alone."),
    ],
},

{
    "id": "BIO11",
    "title": "Molecular Clock Hypothesis",
    "filename": "BIO11_molecular_clock.md",
    "entry_type": "reference_law",
    "scale": "population",
    "domain": "biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Neutral molecular substitutions accumulate at an approximately constant rate over evolutionary time (Zuckerkandl & Pauling, 1962). Sequence divergence between two lineages is proportional to the time since their common ancestor. This enables molecular sequences to serve as evolutionary clocks: divergence times can be estimated from sequence differences calibrated against the fossil record."),
        ("Mathematical Form", 1,
         "d = 2k · t  (d = sequence divergence, k = substitution rate per site per year, t = divergence time)\nk ≈ μ_n  (neutral mutation rate, from Neutral Theory)\nRate variation: σ²(k) / k² ≈ 1/(2N_e · μ_n)  (overdispersion relative to strict Poisson clock)"),
        ("Constraint Category", 2,
         "Informatic (In): sequence divergence is a cumulative record of neutral information changes. The clock is a Poisson process in sequence space: each site substitutes independently at rate k. Deviations (rate variation among lineages, episodic selection) are informative signals above the null clock."),
        ("DS Cross-References", 3,
         "BIO8 (Neutral Theory — the molecular clock is the direct empirical prediction; k = μ_n follows from Kimura's theorem). BIO3 (Fisher's Fundamental Theorem — selection accelerates evolution above the clock rate; rate heterogeneity reveals episodes of adaptive evolution). BIO2 (Hardy-Weinberg — the equilibrium assumption underlying neutral substitution rates). B1 (Radioactive Decay — structural analog: both describe exponential accumulation of changes at constant rate; used together in radiometric dating calibrations)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nUnder strict neutrality, expected sequence divergence grows linearly with time: d = 2kt. This is the ensemble mean of a Poisson counting process with rate k per site per year. The linear relationship enables time estimation from sequence data — a molecular ruler. Deviations from linearity (rate variation, branch-length heterogeneity) are detectable and biologically interpretable."),
        ("What The Math Says", 5,
         "Sequence divergence d between two lineages equals 2 times the substitution rate k times the divergence time t. The factor of 2 arises because both lineages accumulate substitutions independently from their common ancestor. Under Neutral Theory, k equals the neutral mutation rate mu-n. For proteins, k is typically 10 to the minus 9 amino acid substitutions per site per year. For synonymous DNA sites, k is approximately 5 times 10 to the minus 9. The variance of the substitution process exceeds a strict Poisson clock (overdispersion) due to rate variation among sites and among lineages, quantified by the ratio of variance to mean greater than 1."),
        ("Concept Tags", 6,
         "• molecular clock\n• sequence divergence\n• substitution rate\n• evolutionary time\n• Zuckerkandl Pauling\n• phylogenetic dating\n• neutral substitution\n• Poisson process\n• rate heterogeneity\n• calibration"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "molecular clock, sequence divergence, substitution rate, evolutionary time, Zuckerkandl Pauling, phylogenetic dating, neutral substitution, Poisson process, rate heterogeneity, calibration", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "BIO11", "Molecular Clock Hypothesis", "BIO8", "Neutral Theory of Molecular Evolution", "The molecular clock is the primary empirical prediction of Neutral Theory: if k = μ_n, then divergence accumulates linearly with time."),
        ("analogous to", "BIO11", "Molecular Clock Hypothesis", "B1", "B1: Radioactive Decay (Gamow Tunneling)", "Both describe time-dependent accumulation processes at constant rates used for dating: molecular clocks date evolutionary divergence, radiometric clocks date geological events."),
        ("tests", "BIO11", "Molecular Clock Hypothesis", "BIO3", "Natural Selection — Fisher's Fundamental Theorem", "Rate variation above the neutral clock rate is a test for adaptive evolution; deviations from strict molecular clock timing reveal episodes of selection."),
    ],
},

# ── CHEMISTRY ──────────────────────────────────────────────────────────────

{
    "id": "CHEM1",
    "title": "Periodic Law",
    "filename": "CHEM1_periodic_law.md",
    "entry_type": "reference_law",
    "scale": "atomic",
    "domain": "chemistry · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The physical and chemical properties of the elements are periodic functions of their atomic number Z (Mendeleev, 1869; Moseley's X-ray law, 1913). Elements arranged in order of increasing Z show recurring patterns in valence electron configuration, electronegativity, atomic radius, and ionisation energy. The period length (2, 8, 18, 32) reflects shell-filling in three-dimensional quantum mechanics."),
        ("Mathematical Form", 1,
         "Moseley's law: √f = a(Z − b)  (X-ray frequency f scales as square root of (Z − screening constant))\nIonisation energy trend: IE₁ ≈ Z²_eff · 13.6 eV / n²  (Bohr model approximation)\nAtomic radius trend: r ≈ n² a₀ / Z_eff  (decreases across period, increases down group)"),
        ("Constraint Category", 2,
         "Geometric/Quantum (Ge): the periodic structure arises from the combinatorial geometry of electron orbital filling — the aufbau principle applied to the three-dimensional quantum geometry of the Coulomb problem. Shell structure (n = 1,2,3,...) and subshell degeneracy (s,p,d,f) determine period lengths. The periodicity is topological: it reflects the discrete symmetry of the Schrödinger equation for the hydrogen-like atom."),
        ("DS Cross-References", 3,
         "QM3 (Pauli Exclusion — the Pauli principle is the direct cause of shell filling and therefore the periodic table's structure). QM1 (Schrödinger Equation — orbital wavefunctions determine chemical properties via electron density distribution). KC8 (Law of Definite Composition — stoichiometry follows from periodic valence; compounds form with fixed integer ratios). EM6 (Coulomb's Law — the nuclear-electron attraction governs Z_eff and determines ionisation energies)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: recursive-self-similarity\n\nThe periodic table exhibits recursive structure: each period reproduces the valence pattern of the previous period with additional electron shells. The recurrence period increases as (2, 8, 8, 18, 18, 32, 32) reflecting the degeneracy of quantum orbital shells. This is a discrete self-similarity: the chemistry of Li mirrors Na mirrors K with increasing atomic complexity, following the same underlying quantum geometry."),
        ("What The Math Says", 5,
         "Moseley showed in 1913 that the square root of characteristic X-ray frequency scales linearly with atomic number Z minus a screening constant b: root-f equals a times (Z minus b). This replaced Mendeleev's empirical arrangement by atomic mass with the correct physical ordering by nuclear charge. Ionisation energies scale approximately as Z-effective squared over n-squared in electron volts, where n is the principal quantum number and Z-effective accounts for electron screening. Atomic radius scales as n-squared divided by Z-effective in units of the Bohr radius. Both trends are consequences of the 3D Coulomb problem solved by quantum mechanics."),
        ("Concept Tags", 6,
         "• periodic law\n• periodic table\n• atomic number\n• Mendeleev\n• Moseley's law\n• electron configuration\n• valence electrons\n• ionisation energy trend\n• atomic radius\n• aufbau principle"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "periodic law, periodic table, atomic number, Mendeleev, Moseley's law, electron configuration, valence electrons, ionisation energy trend, atomic radius, aufbau principle", 0),
        ("DS Facets", "mathematical_archetype", "recursive-self-similarity", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "CHEM1", "Periodic Law", "QM3", "Pauli Exclusion Principle", "The Pauli exclusion principle forces electrons into distinct orbitals; the resulting shell-filling pattern directly generates the periodic structure of the table."),
        ("derives from", "CHEM1", "Periodic Law", "QM1", "Schrödinger Equation", "Orbital wavefunctions (solutions to the Schrödinger equation) determine electron density distributions and therefore chemical bonding and reactivity."),
        ("constrains", "CHEM1", "Periodic Law", "KC8", "Law of Definite Composition", "Periodic valence structure constrains which stoichiometries are possible; elements with valence n form compounds obeying fixed integer combination ratios."),
    ],
},

{
    "id": "CHEM2",
    "title": "Nernst Equation",
    "filename": "CHEM2_nernst_equation.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "chemistry · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The electrode potential of an electrochemical half-cell depends on temperature and the logarithm of the ratio of activities of oxidised to reduced species (Nernst, 1889). At equilibrium, the cell potential equals zero and the ratio defines the equilibrium constant K. The Nernst equation connects electrochemistry to thermodynamics via the relation ΔG = −nFE."),
        ("Mathematical Form", 1,
         "E = E° − (RT/nF) ln Q\nAt equilibrium: E = 0, Q = K → ΔG° = −RT ln K = −nFE°\nAt 298 K: E = E° − (0.0592/n) log₁₀ Q  (in volts)"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): the Nernst equation is a direct consequence of the equality of electrochemical potential across the cell interface. The logarithmic form arises from the chemical potential μ = μ° + RT ln a for each species. The equilibrium condition ΔG = 0 determines E = 0."),
        ("DS Cross-References", 3,
         "TD3 (Second Law — entropy maximisation drives the cell reaction; the Nernst equation describes the free energy available). KC5 (Gibbs-Helmholtz — the full thermodynamic treatment connects E to ΔH and ΔS). KC1 (Le Chatelier — changing the ratio Q shifts the equilibrium potential as predicted by the Nernst equation). B5 (Landauer's Principle — electrochemical information storage in biological membranes (membrane potential) follows Nernst for ion gradients). CHEM3 (Faraday's Laws — the charge transfer n·F in the Nernst equation is quantified by Faraday's laws)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nThe Nernst equation describes the maximum electrical work extractable from a chemical concentration gradient: W_max = nFE = −ΔG. The logarithmic dependence on concentration ratio Q reflects the entropy of mixing: the cell potential decreases logarithmically as the system approaches equilibrium (Q → K). This is the electrochemical analog of the Boltzmann distribution."),
        ("What The Math Says", 5,
         "The cell potential E equals the standard potential E-zero minus RT over nF times the natural logarithm of the reaction quotient Q. Here R is the gas constant, T is temperature, n is the number of electrons transferred per formula unit, F is Faraday's constant (96485 coulombs per mole of electrons), and Q equals the product of activities of products divided by reactants. At 298 K this simplifies to E equals E-zero minus 0.0592 over n times the base-10 logarithm of Q. At equilibrium Q equals K and E equals zero, giving delta-G-zero equals minus RT ln K equals minus nF times E-zero."),
        ("Concept Tags", 6,
         "• Nernst equation\n• electrode potential\n• electrochemical cell\n• reaction quotient\n• equilibrium constant\n• Faraday constant\n• standard potential\n• thermodynamic work\n• concentration gradient\n• membrane potential"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Nernst equation, electrode potential, electrochemical cell, reaction quotient, equilibrium constant, Faraday constant, standard potential, thermodynamic work, concentration gradient, membrane potential", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "CHEM2", "Nernst Equation", "TD3", "Second Law of Thermodynamics", "The Nernst equation follows from the second law: ΔG = −nFE must be negative for a spontaneous cell reaction; at equilibrium ΔG = 0 and E = 0."),
        ("implements", "CHEM2", "Nernst Equation", "KC5", "Gibbs–Helmholtz Equation", "The Nernst equation is the electrochemical form of the Gibbs-Helmholtz relation: it expresses ΔG = −nFE in terms of measurable cell potentials."),
        ("analogous to", "CHEM2", "Nernst Equation", "B5", "B5: Landauer's Principle", "Both describe the thermodynamic cost of information operations in electrochemical systems: the Nernst equation governs biological membrane potentials that encode and transmit electrochemical signals."),
    ],
},

{
    "id": "CHEM3",
    "title": "Faraday's Laws of Electrolysis",
    "filename": "CHEM3_faraday_electrolysis.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "chemistry · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "(1) The mass of a substance deposited or dissolved at an electrode is directly proportional to the total electric charge passed. (2) For the same total charge, the masses of different substances deposited are proportional to their equivalent masses (molar mass M divided by valence z). These laws (Faraday, 1833–1834) established the quantised nature of charge and the relationship between electricity and chemistry before the electron was discovered."),
        ("Mathematical Form", 1,
         "m = (Q · M) / (z · F)  where Q = ∫I dt, F = 96485 C/mol\nFirst law: m ∝ Q  (at fixed M and z)\nSecond law: m₁/m₂ = (M₁/z₁) / (M₂/z₂)  (at fixed Q)"),
        ("Constraint Category", 2,
         "Coordination/Conservation (Co): charge and chemical equivalents are exactly coordinated — each mole of electrons transfers exactly one equivalent of chemical change. This is a quantisation constraint: the discrete nature of charge (and later, the electron) is embedded in the proportionality constant F = N_A · e."),
        ("DS Cross-References", 3,
         "EM5 (Continuity Equation / Charge Conservation — charge is conserved throughout the electrolytic circuit; Faraday's laws are the electrochemical consequence). KC2 (Microscopic Reversibility — electrode reactions are reversible; both oxidation and reduction follow the same proportionality). CHEM2 (Nernst Equation — the charge n·F in the Nernst equation is quantified by Faraday's laws). QM3 (Pauli Exclusion — the electron transfer in electrolysis occurs one electron at a time; the quantisation is a quantum mechanical fact)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nMass deposited is strictly linear in total charge: m = (M/zF)·Q. This is a direct proportionality with a universal constant F = 96485 C/mol. The second law adds a combinatorial dimension: equivalent masses M/z determine the electrochemical equivalence across all elements. The simplicity and universality of this relationship was Faraday's first evidence for the atomic nature of matter."),
        ("What The Math Says", 5,
         "Mass deposited m equals charge Q times molar mass M divided by valence z times Faraday's constant F. Faraday's constant equals Avogadro's number times the elementary charge: F equals N-A times e equals 96485 coulombs per mole. The first law states that doubling the current or the time doubles the mass deposited. The second law states that depositing one mole of monovalent ions (z=1) requires one Faraday (96485 C), depositing one mole of divalent ions (z=2) requires two Faradays. The ratio M over z is the electrochemical equivalent — the mass deposited per Faraday."),
        ("Concept Tags", 6,
         "• Faraday's laws\n• electrolysis\n• electric charge\n• Faraday constant\n• electrodeposition\n• equivalent mass\n• valence\n• coulometry\n• charge quantisation\n• electrochemical equivalent"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Co", 0),
        ("entries", "concept_tags", "Faraday's laws, electrolysis, electric charge, Faraday constant, electrodeposition, equivalent mass, valence, coulometry, charge quantisation, electrochemical equivalent", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "CHEM3", "Faraday's Laws of Electrolysis", "EM5", "Continuity Equation (Charge Conservation)", "Faraday's laws are the electrochemical consequence of charge conservation: every electron transferred at the cathode is balanced by a corresponding electron supplied at the anode."),
        ("implements", "CHEM3", "Faraday's Laws of Electrolysis", "CHEM2", "Nernst Equation", "The electron count n in the Nernst equation (ΔG = −nFE) is precisely defined by Faraday's laws: n electrons per formula unit times F coulombs per mole."),
        ("analogous to", "CHEM3", "Faraday's Laws of Electrolysis", "BIO5", "Central Dogma of Molecular Biology", "Both are discrete-unit transfer laws: Faraday's laws count electrons; the Central Dogma counts codons. Both reveal that nature operates in quantised packets."),
    ],
},

{
    "id": "CHEM4",
    "title": "Henderson–Hasselbalch Equation",
    "filename": "CHEM4_henderson_hasselbalch.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "chemistry · biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The pH of a buffer solution is determined by the pKa of the weak acid and the logarithm of the ratio of conjugate base to acid concentrations (Henderson, 1908; Hasselbalch, 1916). Buffers resist pH change most effectively when pH = pKa, where [A⁻] = [HA]. This equation quantifies the pH of biological fluids, blood, and biochemical buffers with high precision."),
        ("Mathematical Form", 1,
         "pH = pKa + log([A⁻]/[HA])\nDerivation: Ka = [H⁺][A⁻]/[HA] → pH = pKa + log([A⁻]/[HA])\nBuffer capacity: β = 2.303 · C · Ka[H⁺] / (Ka + [H⁺])²  (maximum at pH = pKa)"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): the logarithmic form arises from the acid dissociation equilibrium constant Ka, which is a thermodynamic quantity (ΔG° = −RT ln Ka = 2.303 RT pKa). The equation is exact for ideal solutions and provides a log-linear relationship between pH and the conjugate base-to-acid ratio."),
        ("DS Cross-References", 3,
         "KC1 (Le Chatelier — adding base shifts [A⁻]/[HA] ratio right, raising pH; Le Chatelier predicts the direction). KC5 (Gibbs-Helmholtz — Ka is a thermodynamic equilibrium constant; pKa = −ΔG°/2.303RT). CHEM2 (Nernst Equation — both are log-ratio thermodynamic equations; Nernst is the electrochemical analog of Henderson-Hasselbalch). TD3 (Second Law — equilibrium is the state of maximum entropy; Ka is determined by ΔG° = ΔH° − TΔS°)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nThe Henderson-Hasselbalch equation describes the equilibrium condition for a weak acid buffer: pH is the logarithm of the hydrogen ion activity at the acid-base equilibrium. The buffering capacity maximum at pH = pKa corresponds to the inflection point of the titration curve — where the system has maximum resistance to pH change per mole of added base or acid."),
        ("What The Math Says", 5,
         "pH equals pKa plus the base-10 logarithm of the concentration ratio of conjugate base A-minus to weak acid HA. When the concentrations are equal, pH equals pKa exactly. A ten-fold excess of base over acid raises pH by 1 unit above pKa; a ten-fold excess of acid lowers pH by 1 unit below pKa. Buffer capacity beta has a maximum at pH equals pKa and falls off steeply more than 1 pH unit away. Blood pH of 7.4 is maintained by the carbonate buffer system with pKa of carbonic acid approximately 6.1, requiring approximately 20:1 ratio of bicarbonate to carbonic acid."),
        ("Concept Tags", 6,
         "• Henderson-Hasselbalch\n• buffer solution\n• pH calculation\n• pKa\n• weak acid equilibrium\n• conjugate base\n• buffer capacity\n• acid-base chemistry\n• biological pH\n• titration curve"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Henderson-Hasselbalch, buffer solution, pH calculation, pKa, weak acid equilibrium, conjugate base, buffer capacity, acid-base chemistry, biological pH, titration curve", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "CHEM4", "Henderson–Hasselbalch Equation", "KC1", "Le Chatelier's Principle", "Le Chatelier predicts qualitatively that adding base to a buffer shifts equilibrium toward the base form; Henderson-Hasselbalch quantifies this shift exactly."),
        ("analogous to", "CHEM4", "Henderson–Hasselbalch Equation", "CHEM2", "Nernst Equation", "Both equations describe thermodynamic equilibria as logarithms of concentration ratios: Nernst for electrochemical cells, Henderson-Hasselbalch for acid-base equilibria."),
        ("couples to", "CHEM4", "Henderson–Hasselbalch Equation", "BIO9", "Hodgkin–Huxley Action Potential Model", "Intracellular and extracellular pH (maintained by Henderson-Hasselbalch buffering) directly affects ion channel gating kinetics in the Hodgkin-Huxley model."),
    ],
},

{
    "id": "CHEM5",
    "title": "Law of Mass Action and Reaction Rate Law",
    "filename": "CHEM5_mass_action.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "chemistry · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "At constant temperature, the rate of an elementary chemical reaction is proportional to the product of the concentrations of the reactants, each raised to the power of its stoichiometric coefficient (Guldberg & Waage, 1864). For equilibrium reactions, the equilibrium constant K equals the ratio of forward to reverse rate constants. For non-elementary reactions, rate orders must be determined empirically and may not equal stoichiometric coefficients."),
        ("Mathematical Form", 1,
         "Rate = k[A]^m[B]^n  (m, n = reaction orders; k = rate constant)\nEquilibrium: K_eq = k_f/k_r = [products]^ν / [reactants]^ν\nArrhenius: k = A·exp(−E_a/RT)  (temperature dependence of rate constant)\nHalf-life: t_{1/2} = ln(2)/k (first order); t_{1/2} = 1/(k[A]₀) (second order)"),
        ("Constraint Category", 2,
         "Dynamical (Di): concentration-driven rate equations are the fundamental dynamical law of chemical kinetics. The rate law is a differential equation for concentration evolution: d[A]/dt = −k[A]^m[B]^n. The equilibrium constant K is the ratio at which forward and reverse rates balance — a dynamical fixed point."),
        ("DS Cross-References", 3,
         "B2 (Arrhenius Equation — provides the temperature dependence of k; the Arrhenius parameters E_a and A characterise the energy landscape). KC1 (Le Chatelier — the equilibrium position K = k_f/k_r shifts with concentration; Le Chatelier is the qualitative statement of the mass action equilibrium condition). BIO6 (Michaelis-Menten — enzyme kinetics is mass action applied to the enzyme-substrate complex at quasi-steady-state). B1 (Radioactive Decay — first-order rate law is the simplest mass action case: k[A]^1; the same exponential form)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: power-law-scaling\n\nThe rate law Rate = k[A]^m[B]^n is a power law in concentration space. The exponents m and n define the dimensionality of the kinetic phase space. For elementary reactions, these equal stoichiometric coefficients — a direct coupling between chemistry and dynamics. The rate constant k sets the time scale; the exponents set the concentration dependence. This power-law form is the foundation of all chemical kinetics."),
        ("What The Math Says", 5,
         "The reaction rate equals k times the product of concentrations of reactants each raised to their reaction order. For a first-order reaction, rate equals k times concentration A, and A decays exponentially: A of t equals A-zero times e to the minus k-t, with half-life ln(2) over k. For a second-order reaction rate equals k times A squared, giving A of t equals A-zero over (1 plus k times A-zero times t), with half-life 1 over (k times A-zero). At equilibrium, forward and reverse rates are equal, defining the equilibrium constant K equals k-forward over k-reverse. The Arrhenius equation gives k equals pre-exponential factor A times e to the minus activation energy over RT."),
        ("Concept Tags", 6,
         "• mass action\n• reaction rate law\n• rate constant\n• reaction order\n• equilibrium constant\n• Arrhenius kinetics\n• Guldberg Waage\n• concentration dependence\n• first order reaction\n• chemical kinetics"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "mass action, reaction rate law, rate constant, reaction order, equilibrium constant, Arrhenius kinetics, Guldberg Waage, concentration dependence, first order reaction, chemical kinetics", 0),
        ("DS Facets", "mathematical_archetype", "power-law-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "CHEM5", "Law of Mass Action and Reaction Rate Law", "BIO6", "Michaelis–Menten Enzyme Kinetics", "Michaelis-Menten kinetics is a special case of mass action applied to the enzyme-substrate complex; the quasi-steady-state assumption converts the full mass action system to the hyperbolic rate law."),
        ("couples to", "CHEM5", "Law of Mass Action and Reaction Rate Law", "B2", "B2: Arrhenius Equation", "The Arrhenius equation provides the temperature dependence of the rate constant k in the mass action rate law; together they give the complete kinetic description."),
        ("implements", "CHEM5", "Law of Mass Action and Reaction Rate Law", "KC1", "Le Chatelier's Principle", "Le Chatelier is the qualitative expression of mass action equilibrium: the equilibrium constant K = k_f/k_r determines the direction of response to any perturbation."),
    ],
},

]

# ---------------------------------------------------------------------------
def slugify(s):
    import re
    return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')

def insert_entries(db_path, entries):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    inserted = skipped = 0

    for e in entries:
        # 1. Insert entry row (skip if exists)
        cur.execute("""
            INSERT OR IGNORE INTO entries (id, title, filename, entry_type, scale, domain,
                status, confidence, type_group, authoring_status)
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (e["id"], e["title"], e["filename"], e["entry_type"], e["scale"],
              e["domain"], e["status"], e["confidence"], e["type_group"], None))

        if cur.rowcount == 0:
            print(f"  SKIP (already exists): {e['id']}")
            skipped += 1
            continue

        # 2. Insert sections
        for (sname, sorder, content) in e["sections"]:
            cur.execute("""
                INSERT INTO sections (entry_id, section_name, section_order, content)
                VALUES (?,?,?,?)
            """, (e["id"], sname, sorder, content))

        # 3. Insert properties
        for (tname, pname, pvalue, porder) in e["properties"]:
            cur.execute("""
                INSERT INTO entry_properties (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?,?,?,?,?)
            """, (e["id"], tname, pname, pvalue, porder))

        # 4. Insert links (both directions for symmetric types)
        for (ltype, src, slabel, tgt, tlabel, desc) in e.get("links", []):
            cur.execute("""
                INSERT OR IGNORE INTO links (link_type, source_id, source_label, target_id,
                    target_label, description, link_order, confidence_tier)
                VALUES (?,?,?,?,?,?,?,?)
            """, (ltype, src, slabel, tgt, tlabel, desc, 0, "1.5"))

        print(f"  INSERT: {e['id']} — {e['title']}")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone: {inserted} inserted, {skipped} skipped.")
    return inserted

if __name__ == "__main__":
    print(f"Inserting Chunk 1 ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    n = insert_entries(SOURCE_DB, ENTRIES)
    print(f"\nChunk 1 complete. New entries: {n}")

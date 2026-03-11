"""
add_phase3_concept_tags.py  — Phase 3: Concept Tags

Adds semantic anchor phrases to every entry in ds_wiki.db.

Two insertions per entry:
  1. entry_properties row: concept_tags = "comma, separated, phrases"
     (SQL-queryable for filtering by semantic domain)

  2. sections row: "Concept Tags"
     Short embeddable list of anchor phrases — helps isolated entries
     find cluster neighbors by bridging vocabulary across domains.

Tags are written as dense multi-word phrases (not single words) to
maximise the semantic signal each tag carries. 5-10 tags per entry.

Run: .venv/bin/python scripts/add_phase3_concept_tags.py [--dry-run]
"""

import sqlite3, sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import SOURCE_DB

# ===========================================================================
# CONCEPT TAGS — keyed by entry_id
# Each value is a comma-separated string of semantic anchor phrases.
# ===========================================================================

TAGS: dict[str, str] = {

# ---------------------------------------------------------------------------
# DS-NATIVE: THEOREMS / LAWS / CONSTRAINTS / AXIOMS / PARAMETERS / MECHANISMS
# ---------------------------------------------------------------------------

"A1": (
    "geometric scaling, surface-area-to-volume ratio, dimensional exponent, "
    "power law geometry, scaling with size, D-dimensional volume, fractal surface, "
    "allometric constraint, size-dependent biology, spatial scaling"
),
"A2": (
    "fractal dimension, Hausdorff dimension, ruler paradox, coastline measurement, "
    "self-similar curve, scale-dependent length, log-log slope, fractal geometry, "
    "Richardson effect, measurement resolution"
),
"Ax1": (
    "information primacy, entropy foundation, epistemic constraint, knowledge bounds, "
    "observer-system coupling, measurement information, quantum information, "
    "Shannon entropy, Fisher information, information-theoretic foundation"
),
"Ax2": (
    "effective dimensionality, D_eff definition, dimensional reduction, "
    "Fisher information rank, observable degrees of freedom, coarse-graining, "
    "scale-dependent dimension, information geometry, dimensional collapse"
),
"B1": (
    "quantum tunneling, WKB approximation, barrier penetration, exponential decay, "
    "nuclear decay, half-life, Gamow factor, activation barrier, quantum mechanics, "
    "radioactive isotope"
),
"B2": (
    "activation energy, exponential rate dependence, temperature-driven kinetics, "
    "Arrhenius plot, pre-exponential factor, rate constant, chemical kinetics, "
    "Boltzmann factor, thermally activated process, rate-limiting step"
),
"B3": (
    "peak emission wavelength, blackbody radiation, temperature-color relationship, "
    "thermal radiation, Wien displacement, spectral shift, stellar temperature, "
    "infrared emission, Planck distribution peak, photon energy"
),
"B4": (
    "wavelength-dependent scattering, inverse fourth power, blue sky, sunset red, "
    "particle size dependence, elastic light scattering, Rayleigh regime, "
    "atmospheric optics, sixth power diameter, optical cross section"
),
"B5": (
    "thermodynamic cost of computation, entropy and information, irreversible erasure, "
    "minimum energy per bit, Boltzmann entropy, computation thermodynamics, "
    "logical irreversibility, Maxwell demon, information erasure, reversible computing"
),
"C1": (
    "metabolic scaling, Kleiber law, three-quarter power, body mass exponent, "
    "fractal vascular network, allometric scaling, biological power law, "
    "network geometry, oxygen consumption, mass-specific metabolism"
),
"C2": (
    "urban scaling, city size, superlinear growth, economies of scale, GDP scaling, "
    "social network density, agglomeration effects, population power law, "
    "infrastructure scaling, urban metabolism"
),
"C3": (
    "power law distribution, heavy tail, Pareto principle, Zipf law, rank frequency, "
    "scale-free distribution, extreme events, fat tail statistics, "
    "multiplicative process, preferential attachment"
),
"D1": (
    "psychophysics, sensory perception, power law exponent, modality-specific scaling, "
    "Stevens exponent, stimulus-response, dynamic range compression, "
    "neural encoding, perception scaling, sensory adaptation"
),
"D2": (
    "period doubling, chaos transition, bifurcation sequence, universal constant, "
    "Feigenbaum number, nonlinear dynamics, route to chaos, logistic map, "
    "quadratic maximum, universality class"
),
"E1": (
    "exponential technological growth, Moore law, transistor density, "
    "coordination-limited growth, miniaturization, semiconductor technology, "
    "doubling time, technological trajectory, integrated circuit, computing capacity"
),
"E2": (
    "computational energy efficiency, computations per joule, Koomey law, "
    "efficiency doubling, thermodynamic computing limit, Landauer bound approach, "
    "energy consumption of computation, power efficiency trend"
),
"F1": (
    "control theory, requisite variety, feedback control, cybernetics, "
    "state space matching, information channel capacity, Ashby law, "
    "regulatory complexity, biological homeostasis, adaptive control"
),
"F2": (
    "limiting factor, bottleneck resource, minimum constraint, Liebig barrel, "
    "resource colimitation, binding constraint, agricultural yield, "
    "ecological carrying capacity, nutrient limitation, growth ceiling"
),
"F3": (
    "competitive exclusion, ecological niche, Lotka-Volterra competition, "
    "coexistence condition, intraspecific competition, interspecific competition, "
    "species displacement, carrying capacity, community ecology, niche overlap"
),
"F4": (
    "saturation dynamics, carrying capacity, logistic growth, Michaelis-Menten, "
    "enzyme kinetics, asymptotic approach, S-curve, negative feedback, "
    "resource limitation, sigmoid function"
),
"F5": (
    "oxygen viability window, mitochondrial constraint, CcO turnover, "
    "membrane potential threshold, ROS ceiling, cytochrome c, electron transport chain, "
    "oxidative phosphorylation, constraint intersection, physiological boundary"
),
"G1": (
    "dimensional redshift, effective dimensionality gradient, Hubble parameter generalization, "
    "cosmic structure, large scale redshift, dimensional cosmology, "
    "DS cosmological prediction, light path integral, structure formation"
),
"G3": (
    "holographic principle, bulk-boundary correspondence, computational complexity, "
    "Bekenstein bound, entropy area scaling, holographic reconstruction, "
    "exponential hardness, AdS-CFT, quantum gravity, information bound"
),
"H1": (
    "regime definition, phase state, system mode, regime boundary, "
    "dynamical regime, regime switching, state-dependent behavior, "
    "regime identification, regime transition, phase space region"
),
"H2": (
    "fractal dimension parameter, self-similarity exponent, geometric complexity, "
    "Hausdorff measure, box counting dimension, space-filling degree, "
    "lacunarity, fractal analysis, network fractality"
),
"H3": (
    "phase coherence, synchronization parameter, order parameter, "
    "coherence measure, coupled oscillator, phase transition indicator, "
    "network synchrony, coherent state, lambda parameter, DS coupling"
),
"H4": (
    "topological obstruction, Euler characteristic, Poincare-Hopf theorem, "
    "topological constraint, genus, network topology, structural invariant, "
    "chi_eff, topological bound, defect count"
),
"H5": (
    "unified scaling exponent, beta lambda formula, phase coherence interpolation, "
    "fractal-to-integer transition, DS scaling law, metabolic exponent generalization, "
    "dimensionality signature, power law exponent, dual-parameter scaling"
),
"M1": (
    "KKT conditions, complementary slackness, shadow price, binding constraint, "
    "resource scarcity, optimization theory, Lagrange multiplier, "
    "constrained optimization, active constraint, dual variable"
),
"M2": (
    "regime switching model, OccBin method, rational expectations, "
    "occasionally binding constraint, DSGE model, regime-dependent dynamics, "
    "Blanchard-Kahn, linear approximation, constraint threshold, monetary policy"
),
"M3": (
    "hysteresis model, Preisach operator, relay hysteresis, memory effect, "
    "threshold distribution, path dependence, magnetic hysteresis, "
    "irreversibility, switching threshold, hysteresis classification"
),
"M4": (
    "Mori-Zwanzig projection, memory kernel, Langevin equation, "
    "non-Markovian dynamics, generalized Langevin, bath elimination, "
    "projection operator, coarse-grained dynamics, orthogonal dynamics, fluctuation"
),
"M5": (
    "Blanchard-Kahn condition, rational expectations stability, saddle path, "
    "forward-looking variables, dynamic programming, unit circle eigenvalue, "
    "determinacy, backward induction, linear rational expectations"
),
"M6": (
    "Fisher information matrix, parameter identifiability, information geometry, "
    "statistical curvature, rank deficiency, score function, "
    "effective dimensionality measure, Cramer-Rao bound, likelihood geometry"
),
"OmD": (
    "dimensional scaling operator, Omega_D, effective physical constants, "
    "D-dependent gravity, Planck constant scaling, DS core operator, "
    "dimensional interpolation, D equals 4 recovery, singular D equals 2"
),
"P12_STATUS": (
    "beta lambda validation, cross-domain universality check, scaling law test, "
    "DS framework validation, empirical verification, conjecture status"
),
"P2_STATUS": (
    "metabolic exponent validation, vascular dimension measurement, "
    "micro-CT confirmation, Kleiber generalization, DS biology prediction"
),
"Q1": (
    "fractal dimension from exponent, power law to geometry, scaling inversion, "
    "D_f estimation, box counting, fractal measurement, open problem, "
    "dimension inference, log-log regression"
),
"Q2": (
    "spectral triple, Poincare-Hopf extension, quantum geometry, "
    "Dirac operator, noncommutative geometry, topological invariant, open problem"
),
"Q3": (
    "regime capacity, Fisher rank bound, maximum regimes, information-theoretic bound, "
    "dimensionality limit, capacity theorem, open problem"
),
"Q4": (
    "singular learning theory, RLCT, real log canonical threshold, "
    "algebraic geometry of learning, statistical phase transition, "
    "SLT-biology correspondence, open problem"
),
"Q5": (
    "synchronization cost, information cost, phase coherence maintenance, "
    "energy of order, entropy production, synchronization thermodynamics, open problem"
),
"T1": (
    "Fisher rank monotonicity, data processing inequality, coarse-graining, "
    "D_eff decreases with scale, information compression, dimensionality theorem"
),
"T2": (
    "metabolic exponent formula, alpha equals D_eff over D_eff plus one, "
    "testable DS prediction, vascular geometry, biological dimensionality, "
    "micro-CT test, Kleiber exponent derivation"
),
"T3": (
    "unit consistency, dimensional analysis, Omega_D audit, SI units, "
    "D equals 4 recovery, dimensional regularization, consistency check"
),
"T4": (
    "redshift structure correlation, Hubble residuals, foreground structure, "
    "dimensional gradient test, cosmological observational test, line of sight"
),
"T5": (
    "critical exponent interpolation, universality class, D_eff tuning, "
    "non-integer dimension, phase transition, continuous exponent variation"
),
"T6": (
    "holographic complexity gate, bulk reconstruction hardness, "
    "exponential complexity, computational lower bound, holographic duality gate"
),
"T7": (
    "hadron charge radius, effective Planck constant, GUP prediction, "
    "nuclear scale D_eff, QCD lattice comparison, hadronic test"
),
"T8": (
    "beta lambda universality, cross-domain scaling test, vascular neural ecological, "
    "DS framework empirical test, universality without tuning"
),
"T9": (
    "regime capacity bound, Fisher rank observable, regime count prediction, "
    "dimensionality observable test, capacity theorem test"
),
"T10": (
    "RLCT biology correspondence, singular learning theory, algebraic geometry, "
    "Fisher rank RLCT equivalence, mathematical bridge test"
),
"X0_FIM_Regimes": (
    "Fisher information regimes, FIM classification, three-state framework, "
    "regime identification, information geometry states, phase space"
),
"X1": (
    "vascular instantiation, metabolic regime, fractal vascular network, "
    "biological scaling, oxygen delivery, blood flow"
),
"X2": (
    "information geometry instantiation, statistical manifold, "
    "Riemannian metric, curvature regime, Fisher-Rao metric"
),
"X3": (
    "statistical physics instantiation, phase transition, order parameter, "
    "thermodynamic regime, Ising model, criticality"
),
"X4": (
    "quantum systems instantiation, quantum regime, Schrödinger evolution, "
    "quantum phase, entanglement, decoherence"
),
"X5": (
    "ecological network instantiation, food web, ecological regime, "
    "species interaction, trophic structure, ecological scaling"
),
"X6": (
    "neural network instantiation, brain scaling, neural regime, "
    "synaptic connectivity, neural information, cortical structure"
),
"X7": (
    "developmental biology instantiation, morphogenesis regime, "
    "developmental scaling, tissue formation, growth trajectory"
),

# ---------------------------------------------------------------------------
# REFERENCE LAWS: ANALYTICAL MECHANICS (AM)
# ---------------------------------------------------------------------------
"AM1": (
    "action principle, variational calculus, Lagrangian mechanics, "
    "least action, path integral, Hamilton's principle, classical field theory, "
    "extremal path, generalized coordinates, equations of motion"
),
"AM2": (
    "Euler-Lagrange equation, generalized coordinate, generalized momentum, "
    "Lagrangian formalism, constraint elimination, conjugate momentum, "
    "mechanical degrees of freedom, calculus of variations"
),
"AM3": (
    "Hamilton equations, phase space, canonical coordinates, symplectic structure, "
    "Liouville theorem, Poisson bracket, Hamiltonian mechanics, "
    "phase space flow, energy conservation, canonical transformation"
),
"AM4": (
    "Hamilton-Jacobi equation, principal function, complete integral, "
    "separation of variables, canonical transformation, classical-quantum bridge, "
    "characteristic function, action-angle variables"
),
"AM5": (
    "Noether theorem, symmetry and conservation, conserved current, "
    "continuous symmetry, energy conservation, momentum conservation, "
    "angular momentum conservation, charge conservation, gauge symmetry"
),

# ---------------------------------------------------------------------------
# BIOLOGY (BIO)
# ---------------------------------------------------------------------------
"BIO1": (
    "Mendelian genetics, dominant recessive allele, segregation law, "
    "Punnett square, independent assortment, inheritance pattern, "
    "genotype frequency, phenotype ratio, F2 generation, genetic cross"
),
"BIO2": (
    "Hardy-Weinberg equilibrium, allele frequency, population genetics, "
    "random mating, genetic drift null model, evolutionary forces, "
    "diploid population, gene pool, selection neutral, mating equilibrium"
),
"BIO3": (
    "Fisher fundamental theorem, natural selection, additive genetic variance, "
    "mean fitness increase, adaptive evolution, genetic variation, "
    "selection pressure, fitness landscape, evolutionary rate"
),

# ---------------------------------------------------------------------------
# CLASSICAL MECHANICS (CM)
# ---------------------------------------------------------------------------
"CM1": (
    "Newton laws, inertia, force and acceleration, action reaction, "
    "classical mechanics foundation, F equals ma, momentum, "
    "second law, Newton's three laws, mechanics"
),
"CM2": (
    "inverse square gravity, gravitational constant, mass attraction, "
    "universal gravitation, orbital mechanics, D-dependent exponent, "
    "point mass, gravitational field, Newton's law"
),
"CM3": (
    "elliptical orbit, Kepler orbit, conic section, eccentricity, "
    "semi-latus rectum, perihelion, aphelion, orbital shape, focal point"
),
"CM4": (
    "equal areas, angular momentum conservation, central force, "
    "areal velocity, Kepler second law, orbit speed variation, "
    "conservation law, orbital mechanics"
),
"CM5": (
    "orbital period, semi-major axis, T squared proportional to a cubed, "
    "Kepler third law, planetary orbit timing, period-distance relation, "
    "gravitational scale, solar system"
),
"CM6": (
    "rigid body dynamics, center of mass, torque, angular momentum, "
    "Euler equations, extended body, rotational dynamics, moment of inertia"
),
"CM7": (
    "buoyancy, displaced fluid, Archimedes principle, flotation, "
    "fluid statics, upward force, density comparison, hydrostatics"
),
"CM8": (
    "Lorentz force, electromagnetic force, moving charge, "
    "electric and magnetic field, cross product force, cyclotron motion, "
    "particle in field, electromagnetic interaction"
),

# ---------------------------------------------------------------------------
# DIFFUSION AND TRANSPORT (DM)
# ---------------------------------------------------------------------------
"DM1": (
    "Fick diffusion, concentration gradient, diffusion coefficient, "
    "diffusion equation, random walk, mass transport, heat equation analogy, "
    "Laplacian, Brownian motion, gradient-driven flux"
),
"DM2": (
    "effusion rate, molar mass dependence, Graham law, gas speed, "
    "isotope separation, kinetic theory, velocity distribution, "
    "mass-dependent transport, uranium enrichment"
),
"DM3": (
    "Lamm equation, ultracentrifuge, sedimentation, diffusion balance, "
    "macromolecule characterization, sedimentation coefficient, "
    "analytical ultracentrifugation, concentration profile, molecular weight"
),
"DM4": (
    "partial pressure, gas mixture, Dalton law, mole fraction, "
    "ideal gas mixture, vapor pressure, component pressure, "
    "total pressure additivity, atmospheric pressure"
),

# ---------------------------------------------------------------------------
# ELECTROMAGNETISM (EM)
# ---------------------------------------------------------------------------
"EM1": (
    "Gauss electric law, divergence of E field, charge density, "
    "electric flux, Maxwell equations, source of field, permittivity, "
    "Gauss theorem, electric field lines, Coulomb's law integral form"
),
"EM2": (
    "Gauss magnetic law, no magnetic monopole, zero divergence of B, "
    "closed field lines, magnetic flux, Maxwell equations, "
    "solenoidal field, magnetic field topology"
),
"EM3": (
    "Faraday induction, changing magnetic flux, induced EMF, "
    "Lenz law, electromagnetic induction, Maxwell equations, "
    "curl of E, generator principle, transformer"
),
"EM4": (
    "Ampere Maxwell law, displacement current, curl of B, "
    "Maxwell correction, electromagnetic wave prediction, "
    "speed of light derivation, Maxwell equations, Ampere's law generalized"
),
"EM5": (
    "charge conservation, continuity equation, current density divergence, "
    "local conservation, Maxwell equations, charge density evolution, "
    "Kirchhoff current law microscopic"
),
"EM6": (
    "Coulomb law, electrostatic force, inverse square, point charge, "
    "electric constant, repulsion attraction, charge interaction, "
    "D-dependent exponent, electromagnetic force"
),
"EM7": (
    "Biot-Savart law, magnetic field from current, current element, "
    "magnetic field circulation, solenoid field, wire field, "
    "magnetostatics, cross product field"
),
"EM8": (
    "Lenz law, opposition principle, induced current direction, "
    "flux conservation tendency, energy conservation in induction, "
    "eddy currents, back EMF, opposing field"
),
"EM9": (
    "Ohm law, resistance, conductivity, linear response, "
    "drift velocity, Drude model, resistivity, ohmic conductor, "
    "current-voltage relation, microscopic Ohm"
),
"EM10": (
    "Kirchhoff laws, junction current conservation, loop voltage sum, "
    "circuit analysis, KCL KVL, node analysis, mesh analysis, "
    "electrical network, charge conservation, energy conservation circuit"
),
"EM11": (
    "Joule heating, resistive power dissipation, I squared R, "
    "electrical energy to heat, irreversible heating, power loss, "
    "thermal energy, electron lattice collision, heat generation"
),

# ---------------------------------------------------------------------------
# EARTH SCIENCES (ES)
# ---------------------------------------------------------------------------
"ES1": (
    "spatial autocorrelation, geographic nearness, distance decay, "
    "Tobler law, spatial statistics, kriging, geographic information, "
    "neighborhood effect, proximity correlation"
),
"ES2": (
    "modifiable areal unit, aggregation artifact, scale dependence, "
    "spatial statistics artifact, Arbia law, ecological fallacy, "
    "geographic aggregation, spatial resolution"
),
"ES3": (
    "rock resistivity, porosity, water saturation, Archie law, "
    "petrophysics, hydrocarbon detection, resistivity log, "
    "formation factor, pore connectivity, oil exploration"
),
"ES4": (
    "Coriolis effect, pressure gradient, geostrophic wind, "
    "Buys Ballot law, atmospheric dynamics, rotation effect, "
    "isobar-parallel flow, hemisphere asymmetry, weather pattern"
),
"ES5": (
    "seismic velocity, mean atomic weight, Birch law, "
    "mineral composition, deep Earth inference, mantle composition, "
    "compressional wave, geophysics, seismology"
),
"ES6": (
    "fault friction, rock sliding, Byerlee law, friction coefficient, "
    "shear stress, normal stress, earthquake mechanics, crustal strength, "
    "fault mechanics, seismicity"
),
"ES7": (
    "planetary spacing, Titius Bode, power of two, semi-major axis, "
    "orbital resonance, solar system pattern, planetary formation, "
    "numerical pattern, astronomical empirical"
),
"ES8": (
    "stratigraphic superposition, Steno law, relative age, "
    "sedimentary sequence, layer ordering, geochronology, "
    "stratigraphy foundation, depositional age"
),
"ES9": (
    "original horizontality, sediment deposition, gravity minimization, "
    "horizontal stratum, tectonic deformation inference, Steno principle, "
    "structural geology, bed orientation"
),
"ES10": (
    "lateral continuity, sedimentary basin, layer extent, "
    "stratigraphic correlation, facies extent, basin margin, "
    "gap erosion, stratigraphic mapping"
),
"ES11": (
    "cross-cutting relationships, intrusion age, fault age, "
    "geometric age relationship, relative dating, younger than, "
    "dike intrusion, structural geology"
),
"ES12": (
    "faunal succession, index fossils, biostratigraphy, "
    "fossil assemblage, irreversible sequence, global correlation, "
    "stratigraphic time, paleontology"
),
"ES13": (
    "inclusions and components, xenolith age, clast age, "
    "matrix younger than inclusion, relative chronology, "
    "geological time relationships, conglomerate dating"
),
"ES14": (
    "Walther law, facies succession, lateral-vertical equivalence, "
    "conformable sequence, depositional environment, facies correlation, "
    "transgression regression, environmental reconstruction"
),

# ---------------------------------------------------------------------------
# FLUID MECHANICS (FM)
# ---------------------------------------------------------------------------
"FM1": (
    "Navier-Stokes equation, viscous fluid, convective acceleration, "
    "turbulence, nonlinear fluid dynamics, incompressible flow, "
    "Reynolds number, viscosity, pressure gradient force, millennium problem"
),
"FM2": (
    "Bernoulli principle, pressure-velocity tradeoff, streamline, "
    "ideal fluid, aerodynamic lift, Venturi effect, "
    "dynamic pressure, energy conservation fluid, speed-pressure relation"
),
"FM3": (
    "Euler fluid equation, inviscid flow, inertial force, "
    "high Reynolds number, shock wave, ideal gas dynamics, "
    "acoustic wave, Euler equations, compressible flow"
),
"FM4": (
    "Poiseuille flow, pipe flow, r to the fourth, viscosity, "
    "laminar flow, pressure-driven flow, vascular resistance, "
    "arteriosclerosis, microfluidics, flow rate"
),
"FM5": (
    "Stokes drag, viscous drag, low Reynolds number, creeping flow, "
    "terminal velocity, settling speed, microorganism motion, "
    "particle suspension, Stokes law, sedimentation"
),
"FM6": (
    "Faxen law, non-uniform flow, velocity gradient correction, "
    "Laplacian correction, sphere in shear flow, microfluidics, "
    "near-wall particle, drag correction, flow curvature"
),

# ---------------------------------------------------------------------------
# GAS LAWS (GL)
# ---------------------------------------------------------------------------
"GL1": (
    "ideal gas law, PV equals nRT, pressure volume temperature, "
    "gas constant, equation of state, ideal gas approximation, "
    "molar volume, kinetic theory, combined gas law"
),
"GL2": (
    "Boyle law, isothermal compression, pressure volume inverse, "
    "constant temperature, ideal gas, lung physiology, diving physics"
),
"GL3": (
    "Charles law, isobaric expansion, volume temperature proportional, "
    "absolute temperature, kelvin scale, thermal expansion gas, "
    "gas balloon, hot air balloon"
),
"GL4": (
    "Gay-Lussac law, isochoric heating, pressure temperature proportional, "
    "constant volume, aerosol can, sealed container, kinetic pressure"
),
"GL5": (
    "Avogadro law, equal volumes equal molecules, molar volume, "
    "gas stoichiometry, mole concept, molecular hypothesis, "
    "22.4 liters, gas density"
),

# ---------------------------------------------------------------------------
# GRAVITATION (GV)
# ---------------------------------------------------------------------------
"GV1": (
    "Einstein field equations, spacetime curvature, energy-momentum tensor, "
    "general relativity, metric tensor, Ricci tensor, cosmological constant, "
    "gravitational field equations, nonlinear gravity, black hole"
),
"GV2": (
    "gravitoelectromagnetism, GEM equations, weak-field gravity, "
    "frame dragging, Lense-Thirring, gravitomagnetic field, "
    "linearized general relativity, rotating mass, Gravity Probe B"
),
"GV3": (
    "gravitational Gauss law, shell theorem, divergence of g, "
    "gravitational flux, enclosed mass, Newtonian gravity, "
    "spherical symmetry, gravitational field lines, inverse square"
),

# ---------------------------------------------------------------------------
# CHEMISTRY / KINETICS (KC)
# ---------------------------------------------------------------------------
"KC1": (
    "Le Chatelier principle, equilibrium shift, chemical equilibrium, "
    "Gibbs free energy minimum, opposing perturbation, reaction equilibrium, "
    "pressure temperature concentration effects"
),
"KC2": (
    "microscopic reversibility, detailed balance, kinetic equilibrium, "
    "time reversal symmetry, forward reverse rates, equilibrium constant, "
    "thermodynamic consistency, mechanism reversibility"
),
"KC3": (
    "Hammond Leffler postulate, transition state structure, early late TS, "
    "exothermic endothermic, activation energy thermodynamics, "
    "Bell-Evans-Polanyi, kinetics from thermodynamics"
),
"KC4": (
    "Hess law, enthalpy additivity, state function path independence, "
    "thermochemistry, enthalpy of formation, thermodynamic cycle, "
    "Born-Haber cycle, heat of reaction"
),
"KC5": (
    "Gibbs Helmholtz equation, temperature dependence of free energy, "
    "van't Hoff equation, equilibrium constant temperature, "
    "enthalpy entropy compensation, thermodynamic driving force"
),
"KC6": (
    "Raoult law, vapor pressure, mole fraction, ideal solution, "
    "boiling point elevation, freezing point depression, "
    "solution thermodynamics, colligative properties"
),
"KC7": (
    "Henry law, gas solubility, partial pressure, dissolved gas, "
    "carbonation, oxygen transport, decompression sickness, "
    "gas-liquid equilibrium, solubility pressure dependence"
),
"KC8": (
    "law of definite composition, fixed mass ratio, stoichiometry, "
    "atomic theory evidence, pure compound, Proust law, "
    "elemental ratio, molecular formula"
),
"KC9": (
    "multiple proportions, integer ratio, atomic combination, "
    "Dalton atomic theory, compound stoichiometry, mass ratio, "
    "empirical evidence for atoms, whole number ratio"
),
"KC10": (
    "reciprocal proportions, equivalent weights, combining weights, "
    "atomic mass scale, chemical stoichiometry, mass relationships, "
    "element combining ratios"
),

# ---------------------------------------------------------------------------
# OPTICS (OP)
# ---------------------------------------------------------------------------
"OP1": (
    "Fermat principle, optical path length, least time, "
    "geometric optics variational, reflection refraction unified, "
    "optical Lagrangian, ray optics"
),
"OP2": (
    "reflection law, angle of incidence equals reflection, "
    "specular reflection, wave vector conservation, mirror, "
    "geometric optics, planar reflection"
),
"OP3": (
    "Snell law, refraction, refractive index, angle bending, "
    "total internal reflection, fiber optics, lens design, "
    "optical interface, wave vector tangential conservation"
),
"OP4": (
    "Brewster angle, polarization by reflection, p-polarization, "
    "s-polarization, polarizing filter, glare reduction, "
    "laser Brewster window, dielectric interface"
),
"OP5": (
    "Malus law, polarizer transmission, cosine squared, "
    "polarization angle, light intensity reduction, "
    "crossed polarizers, electromagnetic wave polarization"
),
"OP6": (
    "Beer Lambert law, absorption spectroscopy, concentration measurement, "
    "path length dependence, exponential attenuation, molar absorptivity, "
    "spectrophotometry, optical density, turbidity"
),

# ---------------------------------------------------------------------------
# RADIATION (RD)
# ---------------------------------------------------------------------------
"RD1": (
    "Planck radiation law, blackbody spectrum, spectral energy density, "
    "Bose-Einstein photon, ultraviolet catastrophe solution, "
    "quantum statistics, spectral radiance, thermal emission spectrum"
),
"RD2": (
    "Stefan-Boltzmann law, total radiated power, fourth power temperature, "
    "blackbody radiation, emissivity, radiative cooling, "
    "stellar luminosity, planetary equilibrium temperature"
),
"RD3": (
    "Planck-Einstein relation, photon energy, E equals hf, "
    "quantum of light, photoelectric effect, photon momentum, "
    "light quantum, quantization of radiation"
),

# ---------------------------------------------------------------------------
# QUANTUM MECHANICS (QM)
# ---------------------------------------------------------------------------
"QM1": (
    "Schrödinger equation, quantum state evolution, wavefunction, "
    "Hamiltonian operator, quantum superposition, stationary state, "
    "probability amplitude, wave mechanics, quantum dynamics"
),
"QM2": (
    "Heisenberg uncertainty, position momentum uncertainty, "
    "wave-particle duality, Fourier conjugate variables, "
    "quantum measurement limit, wave packet, time-energy uncertainty"
),
"QM3": (
    "Pauli exclusion, fermion antisymmetry, spin statistics, "
    "atomic shell filling, electron configuration, degeneracy pressure, "
    "Fermi-Dirac statistics, neutron star stability"
),
"QM4": (
    "de Broglie wavelength, matter wave, wave-particle duality, "
    "electron diffraction, particle momentum wavelength, "
    "Davisson-Germer, quantum wave, matter wave interference"
),
"QM5": (
    "special relativity, Lorentz transformation, time dilation, "
    "length contraction, energy-mass equivalence, speed of light, "
    "Lorentz factor, spacetime, invariant interval, relativistic dynamics"
),

# ---------------------------------------------------------------------------
# THERMODYNAMICS (TD)
# ---------------------------------------------------------------------------
"TD1": (
    "zeroth law thermodynamics, temperature transitivity, "
    "thermal equilibrium, thermometer foundation, temperature as state function, "
    "thermometric property, thermal contact"
),
"TD2": (
    "first law thermodynamics, energy conservation, internal energy, "
    "heat and work, perpetual motion impossible, closed system energy, "
    "enthalpy, thermodynamic cycle"
),
"TD3": (
    "second law thermodynamics, entropy increase, arrow of time, "
    "irreversibility, Boltzmann entropy, statistical mechanics, "
    "heat flow direction, Carnot efficiency, perpetual motion second kind"
),
"TD4": (
    "third law thermodynamics, absolute zero, entropy zero, "
    "unattainability of absolute zero, heat capacity vanishes, "
    "absolute entropy scale, Nernst theorem"
),
"TD5": (
    "fundamental thermodynamic relation, entropy internal energy volume, "
    "chemical potential, thermodynamic potential, Legendre transform, "
    "Gibbs Helmholtz enthalpy, Maxwell relations"
),
"TD6": (
    "Onsager relations, cross-coupling transport, Seebeck Peltier, "
    "reciprocal transport coefficients, linear response, irreversible thermodynamics, "
    "thermoelectric effect, time reversal symmetry transport"
),
"TD7": (
    "Boltzmann transport equation, phase space distribution, "
    "collision integral, H theorem, kinetic theory, "
    "non-equilibrium statistical mechanics, mean free path, relaxation time"
),
"TD8": (
    "Carnot efficiency, maximum heat engine, reversible cycle, "
    "thermodynamic temperature ratio, heat pump, refrigerator, "
    "thermodynamic temperature definition, efficiency limit"
),
"TD9": (
    "Newton cooling law, exponential temperature decay, "
    "heat transfer coefficient, forced convection, "
    "thermal time constant, cooling curve, temperature equilibration"
),
"TD10": (
    "Fourier heat conduction, thermal conductivity, temperature gradient, "
    "heat flux, diffusion equation for heat, thermal diffusivity, "
    "Laplacian of temperature, conductive heat transfer"
),
"TD11": (
    "Kopp law, molar heat capacity additivity, equipartition theorem, "
    "compound heat capacity, element contribution, "
    "3R Dulong-Petit, heat capacity solid"
),
"TD12": (
    "Dulong Petit law, 3R heat capacity, equipartition solid, "
    "classical phonon, high temperature limit, Einstein model transition, "
    "molar heat capacity, harmonic oscillator solid"
),
"TD13": (
    "Carnot cycle, thermodynamic temperature definition, "
    "reversible heat engine efficiency, maximum efficiency, "
    "T cold over T hot, heat engine thermodynamics, Kelvin scale"
),

}  # end TAGS dict


# ===========================================================================
# INSERT LOGIC
# ===========================================================================

SECTION_NAME = "Concept Tags"
PROPERTY_NAME = "concept_tags"

def run(db_path: str, dry_run: bool = False):
    print(f"DB: {db_path}")
    conn = sqlite3.connect(db_path)

    # Get all entry ids
    all_entries = conn.execute("SELECT id FROM entries ORDER BY id").fetchall()
    all_ids = [r[0] for r in all_entries]

    covered = [eid for eid in all_ids if eid in TAGS]
    missing = [eid for eid in all_ids if eid not in TAGS]
    extra = [eid for eid in TAGS if eid not in all_ids]

    print(f"Entries in DB : {len(all_ids)}")
    print(f"Tags defined  : {len(TAGS)}")
    print(f"Covered       : {len(covered)}")
    if missing:
        print(f"WARNING — no tags for {len(missing)} entries: {missing}")
    if extra:
        print(f"NOTE — tags defined but not in DB: {extra}")

    # Max section order per entry
    max_order = dict(conn.execute(
        "SELECT entry_id, MAX(section_order) FROM sections GROUP BY entry_id"
    ).fetchall())

    # Build rows
    prop_rows = []
    sec_rows = []
    for eid in covered:
        tags = TAGS[eid]
        # Format section text as readable tag list
        tag_list = [t.strip() for t in tags.split(",")]
        section_text = "\n".join(f"• {t}" for t in tag_list if t)
        order = (max_order.get(eid) or 0) + 1
        prop_rows.append((eid, "entries", PROPERTY_NAME, tags, 0))
        sec_rows.append((eid, SECTION_NAME, section_text, order))

    print(f"\nProperty rows to insert : {len(prop_rows)}")
    print(f"Section rows to insert  : {len(sec_rows)}")

    if dry_run:
        print("\nDRY RUN — Concept Tags")
        print(f"  Would insert: {len(prop_rows)} property rows, {len(sec_rows)} section rows")
        if covered:
            eid = covered[0]
            print(f"  Sample [{eid}]: {TAGS[eid][:100]}...")
        conn.close()
        return

    # Live insert
    cur = conn.cursor()
    p_ins = p_skip = s_ins = s_skip = errors = 0

    for eid, tname, pname, pval, pord in prop_rows:
        try:
            cur.execute("""
                INSERT OR IGNORE INTO entry_properties
                    (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?, ?, ?, ?, ?)
            """, (eid, tname, pname, pval, pord))
            if cur.rowcount: p_ins += 1
            else: p_skip += 1
        except Exception as e:
            print(f"PROP ERROR [{eid}]: {e}"); errors += 1

    for eid, sname, content, order in sec_rows:
        try:
            cur.execute("""
                INSERT OR IGNORE INTO sections
                    (entry_id, section_name, content, section_order)
                VALUES (?, ?, ?, ?)
            """, (eid, sname, content, order))
            if cur.rowcount: s_ins += 1
            else: s_skip += 1
        except Exception as e:
            print(f"SEC ERROR [{eid}]: {e}"); errors += 1

    conn.commit()
    conn.close()

    print(f"\nPhase 3 Concept Tags insertion complete")
    print(f"  Property rows inserted : {p_ins} (skipped {p_skip})")
    print(f"  Section rows inserted  : {s_ins} (skipped {s_skip})")
    print(f"  Errors                 : {errors}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 3: Add concept tags to all entries")
    parser.add_argument("--dry-run", action="store_true", help="Preview without inserting")
    args = parser.parse_args()
    run(SOURCE_DB, dry_run=args.dry_run)

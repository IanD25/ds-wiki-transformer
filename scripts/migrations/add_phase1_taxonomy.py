"""
add_phase1_taxonomy.py  — Phase 1 Taxonomy Expansion

Adds two new semantic layers to every entry in ds_wiki.db:

  1. entry_properties rows:
       mathematical_archetype  → controlled-vocabulary tag (e.g. "inverse-square-geometric")
       dimensional_sensitivity → "D-sensitive" or "D-invariant"

  2. sections row: "Mathematical Archetype"
       Rich prose combining the generic archetype description + entry-specific note
       + dimensional sensitivity reason → gets embedded as its own chunk

Why sections AND properties?
  - The property tag is SQL-queryable ("show all inverse-square laws")
  - The section prose is what the embedding model reads — richer text = better vector

Run: .venv/bin/python scripts/add_phase1_taxonomy.py [--dry-run]
"""

import sqlite3, sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import SOURCE_DB

# ===========================================================================
# 14 ARCHETYPE PROSE DESCRIPTIONS
# Each is embedded as part of every entry that carries this archetype.
# Rich, multi-sentence prose so the model can cluster across domains.
# ===========================================================================

ARCHETYPES = {

"inverse-square-geometric": (
    "A conserved quantity radiates from a point source and distributes over an expanding "
    "spherical surface. In three-dimensional space, surface area grows as r², so density "
    "falls as r⁻². This inverse-square dependence is a direct signature of D=3 Euclidean "
    "geometry — in D spatial dimensions the exponent is −(D−1), not fixed at −2. "
    "All inverse-square laws belong to the same mathematical equivalence class regardless "
    "of physical domain: Newtonian gravity, Coulomb electrostatics, and radiant light "
    "intensity are identical under rescaling of their source strength and coupling constant. "
    "The exponent changes whenever the effective dimensionality of the embedding space "
    "changes — making inverse-square laws among the most sensitive probes of D_eff."
),

"gradient-flux-transport": (
    "A conserved quantity flows from high to low potential at a rate proportional to the "
    "local gradient of that potential. The canonical form is J = −k∇φ where J is flux, "
    "φ is the driving potential (temperature, concentration, voltage, pressure), and k is "
    "a domain-specific conductivity or diffusivity. This is the linearized, first-order "
    "transport equation — valid when the system is near equilibrium and the gradient is "
    "small. All gradient-flux laws belong to the same mathematical equivalence class: "
    "Fourier heat conduction, Fick molecular diffusion, Ohm's electrical conduction, "
    "Darcy groundwater flow, and Poiseuille pipe flow are equivalent under substitution "
    "of conserved quantity and conductivity. The dynamic form — ∂φ/∂t = k∇²φ — is the "
    "diffusion equation, and it is the same equation in all domains."
),

"exponential-decay": (
    "A quantity decreases at a rate strictly proportional to its current value: "
    "dN/dt = −λN, giving N(t) = N₀ e^(−λt). The decay constant λ is independent of N — "
    "each unit interval removes the same fraction regardless of how much remains. This "
    "memoryless, history-independent property defines the exponential family. Exponential "
    "decay appears wherever a barrier must be crossed at a constant probability per unit "
    "time or per unit path: quantum barrier tunneling (radioactive decay), thermal "
    "activation over an energy barrier (Arrhenius kinetics), geometric path attenuation "
    "(Beer-Lambert law), and thermal relaxation (Newton's law of cooling). All share the "
    "same mathematical skeleton with different physical interpretations of λ — making them "
    "structurally equivalent members of a single cross-domain family."
),

"power-law-scaling": (
    "A quantity Y scales as a power of another quantity X: Y = aX^β. The exponent β is "
    "the critical parameter — it is often a rational function of the effective "
    "dimensionality D of the underlying network, geometry, or phase space. Power laws are "
    "scale-free: the ratio Y(cX)/Y(X) = c^β is independent of the absolute value of X, "
    "meaning the same proportional relationship holds at every scale. Power laws appear "
    "wherever a system lacks a characteristic scale: at continuous phase transitions, in "
    "fractal geometries, in networks with preferential attachment, in perceptual encoding, "
    "and in metabolic and urban systems. The exponent β often satisfies simple dimensional "
    "relationships: β = D/(D+1) for fractal vascular networks, β = 3/2 for Keplerian "
    "orbital scaling, β = 1/3 for fractal coastline measurement. Identifying the "
    "dimensional origin of β is the central project of the DS framework."
),

"variational-principle": (
    "The physical system evolves along the path — through configuration space, optical "
    "medium, or phase space — that makes a functional S stationary: δS = 0. The "
    "Euler-Lagrange equations are the necessary conditions for stationarity and generate "
    "all equations of motion as outputs. Variational principles are the most compressed "
    "statement of a physical theory: specifying the action functional S completely "
    "determines all dynamics. All variational principles belong to the same mathematical "
    "class across domains: classical mechanics (least action), optics (Fermat's principle "
    "of least time), quantum mechanics (path integral over all histories weighted by "
    "e^(iS/ℏ)), and general relativity (extremal proper time along geodesics) are all "
    "expressions of the same variational structure in different configuration spaces. "
    "The quantity being extremized — action, optical path length, proper time, free energy "
    "— encodes the physics of each domain."
),

"conservation-law": (
    "A quantity Q that does not change under time evolution of the system: dQ/dt = 0 "
    "(global form), or equivalently ∂ρ/∂t + ∇·J = 0 (local form, where ρ is density "
    "and J is flux of the conserved quantity). By Noether's theorem, every conservation "
    "law corresponds to a continuous symmetry of the system's action: time-translation "
    "symmetry generates energy conservation, spatial translation generates momentum "
    "conservation, rotation generates angular momentum conservation, and gauge symmetry "
    "generates charge conservation. Conservation laws constrain dynamics without "
    "determining them — they reduce the number of degrees of freedom that must be solved, "
    "and they survive changes of reference frame, coordinate system, and — critically — "
    "changes of scale. Whether conservation laws survive changes of effective dimension "
    "D_eff is an open question in the DS framework: Noether's theorem requires "
    "time-translation symmetry, which may be broken if physical constants run with D_eff."
),

"thermodynamic-bound": (
    "A strict inequality constraining achievable performance: X ≤ X_max or X ≥ X_min, "
    "where the bound is set by thermodynamic, statistical, or information-theoretic "
    "arguments — not by engineering limitations. Thermodynamic bounds cannot be violated "
    "by any mechanism, no matter how clever, because they follow from entropy, energy "
    "conservation, and the statistics of distinguishable states. Examples span all "
    "domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost "
    "(E ≥ k_BT ln2 per bit), Ashby regulatory variety (V_controller ≥ V_system − "
    "V_channel), Heisenberg uncertainty (ΔxΔp ≥ ℏ/2), and the Bekenstein bound "
    "(S ≤ A/4ℓ_P²). All share the same logical structure: a system trying to exceed the "
    "bound must violate entropy non-decrease, energy conservation, or the distinguishability "
    "of quantum states. The bound value itself is often D-sensitive: Carnot is "
    "D-invariant; Landauer and Heisenberg involve k_BT and ℏ, both acted on by Ω_D."
),

"diffusion-equation": (
    "A parabolic partial differential equation of the form ∂u/∂t = D∇²u, describing how "
    "a quantity u spreads through space over time. Solutions spread as Gaussian "
    "distributions with width growing as √(Dt) — the diffusive signature. The diffusion "
    "equation arises from combining the continuity equation (conservation of u) with a "
    "gradient-flux transport law (Fick's or Fourier's): conservation + linear transport "
    "= diffusion equation. It describes heat conduction, mass diffusion, random walks, "
    "Brownian motion, probability flow (Fokker-Planck), and — in nonlinear form — "
    "turbulent fluid flow (Navier-Stokes). Strongly dimension-sensitive: in 1D and 2D, "
    "random walks return to their origin with probability 1 (recurrent); in 3D and higher "
    "they escape forever (transient). This transition at D=2 is a fundamental difference "
    "in diffusive behavior that directly tests D_eff."
),

"equilibrium-condition": (
    "A constraint satisfied when a system reaches its minimum-free-energy resting state, "
    "where forward and reverse rates are balanced (detailed balance) or all driving "
    "gradients are zero. Equilibrium conditions specify the final state without prescribing "
    "the path. The general form is: the condition under which no net change occurs — "
    "chemical equilibrium (dG = 0), population genetic equilibrium (allele frequencies "
    "constant), mechanical equilibrium (net force = 0), thermal equilibrium (T uniform). "
    "Perturbations from equilibrium drive restoring forces — Le Chatelier, Lenz's law, "
    "and Hardy-Weinberg deviations are all manifestations of this. The distance from "
    "equilibrium, the speed of return, and the stability of equilibrium all depend on "
    "the system's effective dimensionality through the density of states and the "
    "geometry of the free-energy landscape."
),

"wave-equation": (
    "A hyperbolic partial differential equation describing oscillatory propagation at "
    "finite speed. The classical form ∂²u/∂t² = c²∇²u produces solutions that travel "
    "undistorted at speed c. The quantum Schrödinger equation iℏ∂ψ/∂t = Ĥψ is a "
    "first-order-in-time wave equation for probability amplitude — the probability density "
    "|ψ|² satisfies a conservation law. Maxwell's equations produce electromagnetic waves "
    "as their source-free solutions. All wave equations share: superposition (waves pass "
    "through each other), dispersion relations (ω-k relationship encoding speed and "
    "attenuation), and interference. Critically dimension-sensitive: Huygens' principle "
    "(sharp wave fronts without trailing wake) holds only in odd spatial dimensions. "
    "In even dimensions, waves leave a trailing disturbance. The quantum ℏ that sets the "
    "wave-particle duality scale is acted on by Ω_D in the DS framework."
),

"symmetry-conservation": (
    "A constraint derived from the geometric symmetry of a system or Hilbert space. "
    "Noether's theorem is the master statement: every continuous symmetry of the action "
    "generates a conserved current. Discrete symmetries (parity P, time reversal T, "
    "charge conjugation C) generate selection rules and conservation laws for quantum "
    "numbers. The Pauli exclusion principle is a symmetry constraint on Hilbert space "
    "geometry: fermion wavefunctions must be antisymmetric under particle exchange, "
    "constraining the entire structure of matter. Gauge symmetry generates charge "
    "conservation via Noether. Topological symmetries generate conserved topological "
    "invariants (winding numbers, Chern classes). Symmetry-conservation laws are "
    "D-sensitive when the relevant symmetry group changes with dimension — for instance, "
    "the rotation group SO(D) changes structure as D changes, affecting which "
    "conservation laws are possible."
),

"coupled-field-equations": (
    "A system of partial differential equations where multiple fields mutually drive each "
    "other — no field can be solved independently without knowing the others. The coupling "
    "structure determines propagation modes, wave speeds, and stability. Maxwell's "
    "equations couple the electric field E and magnetic field B: a changing E creates B "
    "and vice versa, producing self-sustaining electromagnetic waves at speed c = "
    "1/√(ε₀μ₀). General relativity couples spacetime curvature to matter-energy content. "
    "Navier-Stokes couples velocity, pressure, and viscous stress in a nonlinear system. "
    "The key feature: the coupled system has qualitatively different behavior from any "
    "individual equation. Coupled field systems are strongly dimension-sensitive because "
    "the coupling constants (c, G, ε₀, μ₀) all involve dimensional structure that Ω_D "
    "modifies, and because the number of independent field components changes with D."
),

"statistical-distribution": (
    "Describes the probability distribution of a quantity across an ensemble of states, "
    "particles, individuals, or events. The shape of the distribution — Gaussian, "
    "power-law, exponential, Boltzmann, Planck — encodes the underlying statistical "
    "physics and geometry. Gaussian distributions arise from independent additive "
    "contributions (Central Limit Theorem). Power-law distributions arise from "
    "multiplicative processes, preferential attachment, or proximity to a critical point. "
    "Boltzmann distributions arise from thermal equilibrium — the probability of a "
    "microstate is e^(−E/k_BT) / Z. Planck distributions arise from quantized harmonic "
    "oscillators in thermal equilibrium. The exponents and shape parameters of "
    "statistical distributions carry dimensional information: k_B connects energy to "
    "temperature (D-sensitive through Ω_D), and critical exponents in power-law "
    "distributions are constrained by the universality class, which depends on D."
),

"geometric-ratio": (
    "A fixed ratio or proportion between geometric quantities that follows exactly from "
    "the structure of space — not from physical forces or thermodynamics, but from "
    "pure geometry. Geometric ratio laws are exact within their domain: the square-cube "
    "law (surface ∝ L^(D−1), volume ∝ L^D) holds exactly in D-dimensional Euclidean "
    "space. Snell's law follows from conservation of the wave vector component parallel "
    "to an interface. Archimedes' principle follows from pressure integration over a "
    "volume. Stoichiometric laws follow from discrete atomic combining geometry. "
    "Geometric ratio laws are D-sensitive when the underlying space is D-sensitive — "
    "the square-cube law changes form with D. They are D-invariant when they arise from "
    "angle relationships or combinatorial structure independent of dimension, such as "
    "the fixed integer ratios in stoichiometry."
),

"dimensional-scaling": (
    "A law whose mathematical form, exponents, or constants explicitly depend on the "
    "effective spatial or network dimensionality D. Dimensional scaling laws are the "
    "primary diagnostic tool of the DS framework: if the observed exponent of a power "
    "law, the coefficient of a transport law, or a physical constant matches a rational "
    "function of D, the system's effective dimension is being revealed. Examples: "
    "Stefan-Boltzmann's T^(D+1) exponent encodes D=3; metabolic scaling's D/(D+1) "
    "encodes the fractal dimension of the vascular network; Feigenbaum's constants "
    "δ and α are universal for 1D maps but change with the dimension of the dynamical "
    "system. The Ω_D operator in the DS framework acts on physical constants (G, h, c, "
    "k_B) to implement dimensional scaling as a field-theoretic operation. Every entry "
    "tagged as dimensional-scaling is a potential site where a change in D_eff produces "
    "a measurable, predictive change in the law's output."
),

}

# ===========================================================================
# ENTRY DATA: (id, archetype, d_sensitive: bool, d_reason, entry_specific_note)
# ===========================================================================

ENTRY_DATA = [

# --- AXIOMS ---
("Ax1", "thermodynamic-bound", True,
 "Ω_D acts on the Bekenstein bound (S ≤ A/4ℓ_P²) — entropy bounded by area not volume; the area-to-volume ratio is D-dependent.",
 "Ax1 (Information Primacy) asserts that physical geometry emerges from information structure. The bound it cites — entropy limited by boundary area — is a thermodynamic ceiling that changes form in D ≠ 3 spatial dimensions."),

("Ax2", "dimensional-scaling", True,
 "Ax2 is the definitional claim that dimension is a running parameter — D_eff is the quantity that all dimensional scaling laws are functions of.",
 "Ax2 (Effective Dimensionality) states that the 'dimension' entering scaling laws is not a fixed integer but a resolution-dependent running parameter D_eff. This entry is the definitional home of dimensional scaling in the DS framework."),

("OmD", "dimensional-scaling", True,
 "Ω_D is the operator that implements D-dependence on all physical constants — it is itself the archetype of dimensional scaling applied to the constants G, h, c, k_B.",
 "Ω_D (Dimensional Scaling Operator) makes physical constants functions of D_eff rather than fixed values. It is the mechanism by which all D-sensitive laws in this database become scale-dependent."),

# --- CONSTRAINTS ---
("F1", "thermodynamic-bound", False,
 "Ashby's inequality is a logical constraint on information variety — the bound is dimensional in the informatic sense but does not depend on spatial D_eff.",
 "F1 (Ashby's Law of Requisite Variety) sets a lower bound on the informational complexity a controller must possess to regulate a system. It is the informatic ceiling of the constraint family, structurally equivalent to Carnot in the thermodynamic domain."),

("F2", "thermodynamic-bound", False,
 "Liebig's minimum constraint applies regardless of spatial dimension — it is a resource-identity bottleneck, not a geometric one.",
 "F2 (Liebig's Law of the Minimum) states that growth is controlled by the scarcest essential resource. It is the single-constraint case of KKT optimization (M1): the active constraint is always the binding minimum."),

("F3", "equilibrium-condition", False,
 "Competitive exclusion is a coordination equilibrium — n niches support n species — that follows from resource competition dynamics regardless of spatial D_eff.",
 "F3 (Gause's Competitive Exclusion Principle) defines the niche equilibrium condition: coexistence requires ecological differentiation. It is the population-level analog of the Pauli exclusion principle — no two entities can stably occupy the same state."),

("F4", "equilibrium-condition", True,
 "Saturation ceilings (Michaelis-Menten Km, logistic K) can depend on D_eff through diffusion-limited binding geometry and the dimensionality of accessible receptor surfaces.",
 "F4 (Saturation Dynamics) describes the kinetic approach to a ceiling through Michaelis-Menten and logistic equations. It is the equilibrium-condition form of the thermodynamic-bound: the ceiling is the equilibrium state approached asymptotically."),

("F5", "thermodynamic-bound", True,
 "The oxygen corridor bounds are set by Arrhenius kinetics (B2) and Gamow tunneling (B1) — both D-sensitive through barrier geometry and ℏ respectively.",
 "F5 (Oxygen Viability Corridor) defines the temperature-pressure envelope where aerobic life is thermodynamically viable. The corridor is a compound bound: lower edge from quantum tunneling rates, upper edge from thermal denaturation."),

# --- DS-NATIVE LAWS ---
("B1", "exponential-decay", True,
 "Gamow tunneling rate contains ℏ explicitly — Ω_D predicts ℏ runs with D_eff, shifting the tunneling probability and thus the decay constant λ.",
 "B1 (Radioactive Decay via Gamow Tunneling) describes exponential decay driven by quantum barrier penetration. The barrier transparency depends on ℏ, making this the most directly D-sensitive exponential decay law in the DS framework."),

("B2", "exponential-decay", True,
 "The Arrhenius pre-exponential factor encodes the number of trajectories over the barrier, which is D-sensitive through the accessible phase-space volume in D dimensions.",
 "B2 (Arrhenius Equation) describes thermally activated barrier crossing. Its exponential form k = A·exp(−E_a/k_BT) makes it a thermal-barrier analog of Gamow tunneling (B1): same mathematical skeleton, different barrier type."),

("B3", "dimensional-scaling", True,
 "Wien's peak wavelength involves h and k_B — both acted on by Ω_D — shifting the spectral peak with D_eff.",
 "B3 (Wien's Displacement Law) constrains the spectral peak of black-body radiation. It is a derived limit of Planck's law (RD1), and its constants h and k_B are both dimensional scalars that Ω_D modifies."),

("B4", "power-law-scaling", True,
 "Rayleigh scattering intensity ∝ d⁶/λ⁴ — the λ⁻⁴ exponent encodes the D=3 geometry of electromagnetic radiation; in D dimensions the wavelength exponent changes.",
 "B4 (Rayleigh Scattering) is a power-law scattering intensity law. The λ⁻⁴ dependence is a D=3 consequence of electromagnetic radiation geometry — it is one of the cleaner tests of whether the effective optical dimension differs from 3."),

("B5", "thermodynamic-bound", True,
 "Landauer's bound k_BT ln2 contains k_B — in D dimensions the relationship between thermal energy and temperature is mediated by the number of accessible degrees of freedom, which is D-dependent.",
 "B5 (Landauer's Principle) sets the thermodynamic floor on information erasure: k_BT ln2 per bit. It is the bridge between thermodynamics (TD3, 2nd law) and information theory (F1, Ashby), making it the most information-theoretically significant entry in the laws group."),

("C1", "power-law-scaling", True,
 "Kleiber's exponent ¾ = D_eff/(D_eff+1) for D_eff=3 — the observed metabolic scaling exponent is a direct rational function of the effective dimension of the vascular branching network.",
 "C1 (Metabolic Scaling / Kleiber's Law) is the DS framework's primary biological scaling law. The ¾ vs ⅔ debate resolves to D_eff=3 network vs D_eff=2 surface geometry — a direct dimensional discrimination."),

("C2", "power-law-scaling", True,
 "Urban scaling exponents (superlinear for innovation, sublinear for infrastructure) depend on the social network's effective dimension — the crossover exponent encodes D_eff of the urban network.",
 "C2 (Urban Scaling / Bettencourt-West) extends metabolic scaling to human cities. The scaling exponent split between innovation (superlinear) and infrastructure (sublinear) reflects the effective network dimension of urban social connectivity."),

("C3", "statistical-distribution", True,
 "Heavy-tailed power-law exponents are constrained by universality classes that depend on D — different effective dimensions produce different sets of possible critical exponents.",
 "C3 (Heavy-Tailed Distributions) is the general law covering power-law tails across all domains. It encompasses Zipf's and Pareto's laws as special cases and connects to universality theory (D2) which determines which exponents are physically possible."),

("D1", "power-law-scaling", False,
 "Stevens' perceptual exponents are empirically determined by neural encoding of each sensory modality — they are psychological constants set by biology, not by spatial geometric dimension.",
 "D1 (Stevens' Power Law) describes how perceived intensity scales with physical stimulus. The power-law form is shared with all scaling laws in this family, but the exponent n is modality-specific rather than dimensionally determined."),

("D2", "dimensional-scaling", True,
 "Feigenbaum constants δ and α are universal for 1D unimodal maps but change with the dimension of the dynamical system — they are dimension-sensitive universality constants.",
 "D2 (Feigenbaum Universality) establishes that period-doubling cascades converge at universal constants that depend on effective dimension. It is the prototypical example of dimension-encoding through universality class membership."),

("E1", "exponential-decay", False,
 "Moore's Law growth rate is set by economic incentives and engineering choices, not physical geometry — the dimensional sensitivity lies in its saturation behavior (F4), not the growth rate itself.",
 "E1 (Moore's Law) tracks exponential transistor-density doubling. The growth is exponential in time rather than in space. Its relevance to the DS framework lies in its approach to saturation (F4) and the Landauer floor (B5)."),

("E2", "thermodynamic-bound", True,
 "Koomey's efficiency improvement is approaching the Landauer floor (B5), which is D-sensitive through k_BT — the ultimate efficiency limit is dimensionally dependent.",
 "E2 (Koomey's Law) tracks exponential improvement in computational energy efficiency. It is approaching the thermodynamic ceiling set by Landauer (B5) — an asymptotic approach to a D-sensitive bound."),

("G1", "dimensional-scaling", True,
 "G1 is definitionally D-sensitive — it proposes that cosmological redshift is caused by D_eff gradients, making it a direct empirical test of dimensional scaling at cosmological scale.",
 "G1 (Dimensional Redshift Law) is the DS framework's most speculative claim: redshift as D_eff attenuation rather than metric expansion. As a dimensional scaling law, it proposes a specific D_eff-dependent form for energy loss of photons."),

("G3", "thermodynamic-bound", True,
 "The Bekenstein bound S ≤ A/4ℓ_P² is area-not-volume — a D=3 constraint. In D dimensions the bound becomes S ≤ A/4ℓ_P^(D−1), changing both the bound and the computational hardness of reconstruction.",
 "G3 (Holographic Complexity Bound) states that bulk reconstruction from boundary data is computationally intractable. It is a compound thermodynamic bound: the Bekenstein entropy ceiling combined with LWE-hardness of the holographic map."),

("H5", "dimensional-scaling", True,
 "β(λ) is derived as an explicit function of D_eff — the entire point of the law is that its exponent changes continuously with effective dimension.",
 "H5 (Scaling Exponent β(λ)) is the DS framework's master dimensional scaling law, generalizing Kleiber and urban scaling to arbitrary domains through a single D_eff-dependent formula."),

# --- MECHANISM ---
("H1", "equilibrium-condition", True,
 "Regime boundaries (ordered/critical/disordered) occur at critical values of control parameters that are D-sensitive — phase boundaries shift with effective dimension.",
 "H1 (Regime) defines the three-state classification of dynamical systems. The regime boundaries are equilibrium conditions: control parameters at which the system transitions between ordered, critical, and disordered behavior — all D-sensitive through their phase-space structure."),

# --- METHODS ---
("M1", "thermodynamic-bound", False,
 "KKT conditions are constraint-qualification inequalities from mathematical optimization — their logical structure is dimension-independent.",
 "M1 (KKT Constraint Binding) identifies the active binding constraint in a constrained optimization. It is the mathematical formalization of Liebig's law (F2): the binding constraint is the operative bottleneck."),

("M2", "equilibrium-condition", False,
 "OccBin is an econometric regime-switching method — its mathematical structure is dimension-independent as a classification procedure.",
 "M2 (OccBin Regime-Switching) classifies regimes based on constraint activity. It is the algorithmic implementation of regime identification, using equilibrium conditions as the switching criterion."),

("M3", "equilibrium-condition", False,
 "Preisach hysteresis classification uses a memory kernel — mathematically dimension-independent.",
 "M3 (Preisach Hysteresis Classification) models memory-dependent regime transitions. Hysteresis is the history-dependence of the equilibrium condition — which equilibrium is reached depends on the path taken."),

("M4", "gradient-flux-transport", True,
 "Mori-Zwanzig projects full phase-space dynamics onto slow variables — the projection structure and memory kernel are D-sensitive through the dimensionality of the full microscopic phase space.",
 "M4 (Mori-Zwanzig Projection) is a systematic technique for coarse-graining: projecting microscopic dynamics onto a slow-variable subspace with an exact memory kernel. It is the formal derivation of gradient-flux transport laws from microscopic reversible dynamics."),

("M5", "variational-principle", False,
 "Blanchard-Kahn backward induction is a mathematical method for saddle-path stability analysis — variational in structure but dimension-independent as a procedure.",
 "M5 (Blanchard-Kahn Backward Induction) finds the stable manifold in dynamical systems by optimizing over the set of non-explosive paths. It is the variational principle of macroeconomic equilibrium selection."),

("M6", "statistical-distribution", True,
 "Fisher Information matrix rank counts statistically distinguishable parameters — this is equivalent to measuring D_eff of the statistical manifold, directly D-sensitive.",
 "M6 (Fisher Information Rank) evaluates the rank of the Fisher Information matrix to identify the effective dimensionality of a statistical model. It is the operational definition of D_eff in the DS framework's information-geometric formulation."),

("T1", "statistical-distribution", True,
 "Fisher Rank Monotonicity tests whether Fisher information rank decreases monotonically across regime transitions — D-sensitive because rank = D_eff.",
 "T1 (Fisher Rank Monotonicity) tests the prediction that D_eff decreases from ordered to critical to disordered regimes via the Fisher information rank."),

("T2", "dimensional-scaling", True,
 "Directly tests whether metabolic exponent tracks D_eff of the vascular network — a dimensional scaling test.",
 "T2 (Metabolic Exponent-Dimensionality Correlation) tests the core DS prediction that Kleiber's ¾ exponent is D_eff/(D_eff+1) by correlating measured metabolic exponents with independently measured vascular fractal dimensions."),

("T3", "dimensional-scaling", True,
 "Tests Ω_D unit consistency — whether physical constants scale with D_eff as the operator predicts.",
 "T3 (Ω_D Unit Consistency Audit) verifies that the Dimensional Scaling Operator produces dimensionally consistent predictions when D_eff ≠ 4."),

("T4", "dimensional-scaling", True,
 "Tests whether cosmological redshift correlates with D_eff structure gradients — a direct dimensional scaling test at cosmological scale.",
 "T4 (Redshift-Structure Correlation) tests G1 (Dimensional Redshift Law) by checking whether observed redshift patterns correlate with D_eff gradients in large-scale cosmic structure."),

("T5", "dimensional-scaling", True,
 "Tests whether critical exponents vary with embedding dimension — a dimensional scaling sensitivity test.",
 "T5 (Critical Exponent-Dimension Sensitivity) tests whether statistical-physics critical exponents shift predictably with effective dimension, as required by universality theory (D2)."),

("T6", "thermodynamic-bound", True,
 "Holographic reconstruction complexity is D-sensitive through the Bekenstein bound's D-dependence.",
 "T6 (Holographic Reconstruction Complexity) empirically tests G3 (Holographic Complexity Bound) by measuring the computational cost of bulk reconstruction from boundary data."),

("T7", "dimensional-scaling", True,
 "Hadron charge radii encode effective ℏ — a direct test of running ℏ with D_eff as predicted by Ω_D.",
 "T7 (Hadron Charge Radii / Effective ℏ) uses precision measurements of proton and neutron charge distributions to test whether ℏ shows signatures of running with D_eff at the quantum chromodynamics scale."),

("T8", "power-law-scaling", True,
 "Tests β(λ) cross-domain universality — whether the same D_eff-dependent scaling formula holds across physics, biology, and networks.",
 "T8 (β(λ) Cross-Domain Universality Test) tests whether H5's scaling exponent formula produces consistent D_eff values across different physical domains — the key cross-domain universality prediction."),

("T9", "thermodynamic-bound", True,
 "Regime capacity bound test is D-sensitive through the bound's dependence on network dimension.",
 "T9 (Regime Capacity Bound Test) empirically tests Q3 (Regime Capacity Bound) against biological data on maximum sustainable regime diversity."),

("T10", "statistical-distribution", True,
 "SLT-Biology correspondence uses real log canonical threshold (RLCT) — an algebraic geometry quantity that is D-sensitive through the model's parameter space dimension.",
 "T10 (RLCT-Biology Correspondence Test) tests whether Singular Learning Theory's RLCT predicts biological model complexity — a test of Q4 (SLT-Biology Correspondence)."),

# --- PARAMETERS ---
("H2", "dimensional-scaling", True,
 "Fractal dimension d_f is a dimensional parameter — it directly measures the effective dimension of a geometric object, which is the core D_eff concept.",
 "H2 (Fractal Dimension d_f) is the parameter that quantifies how a geometric object fills space as a function of measurement scale. It is the operational definition of non-integer effective dimension in physical and biological systems."),

("H3", "statistical-distribution", True,
 "Phase coherence λ measures the correlation structure of the system, which is D-sensitive through the geometry of the order-parameter field.",
 "H3 (Phase Coherence λ) quantifies the spatial or temporal coherence of a system across its regime. It is the order parameter that distinguishes ordered (λ≈1), critical (0 < λ < 1), and disordered (λ≈0) regimes."),

("H4", "symmetry-conservation", True,
 "Topological obstruction χ_eff is a topological invariant (Euler characteristic) that depends on the dimension and topology of the manifold.",
 "H4 (Topological Obstruction χ_eff) measures the topological complexity of the effective phase space. Non-zero χ_eff signals an obstruction to smooth dimensional reduction — the topological cost of projection."),

# --- THEOREMS ---
("A1", "geometric-ratio", True,
 "Square-Cube law is explicitly D-sensitive: in D dimensions surface ∝ L^(D−1), volume ∝ L^D, giving the ratio L^(D−1)/L^D = L^(−1) — but the exponents of each quantity change with D.",
 "A1 (Square-Cube Law) is the foundational geometric scaling theorem: surface area and volume scale with different powers of linear dimension. In D dimensions it becomes surface ∝ L^(D−1) vs volume ∝ L^D — the basis of all metabolic scaling arguments."),

("A2", "power-law-scaling", True,
 "Richardson effect involves fractal dimension d_f directly — measured length ∝ (measurement scale)^(1 − d_f), a D-sensitive exponent.",
 "A2 (Richardson Effect / Fractal Measurement) shows that measured boundary length depends on measurement scale with a power-law exponent encoding fractal dimension. It is the empirical definition of non-integer dimension in geometric objects."),

# --- OPEN QUESTIONS ---
("Q1", "dimensional-scaling", True,
 "Inferring fractal dimension from power-law exponents is definitionally a D_eff measurement — the question is whether the inference is reliable and unique.",
 "Q1 (Fractal Dimension from Power-Law Exponent) asks whether the fractal dimension d_f can be reliably recovered from scaling exponents in empirical data. It is an open question about the dimensional-scaling inference problem."),

("Q2", "symmetry-conservation", True,
 "Poincaré-Hopf theorem relates Euler characteristic to vector field zeros — both the characteristic and the zero count are D-sensitive topological invariants.",
 "Q2 (Effective Poincaré-Hopf via Spectral Triples) asks whether topological constraints on vector fields, generalized to noncommutative geometry via spectral triples, constrain D_eff in physical systems."),

("Q3", "thermodynamic-bound", True,
 "Regime capacity bound depends on the network dimension of the system — the maximum number of sustainable regimes is a D-sensitive capacity.",
 "Q3 (Regime Capacity Bound) asks whether there is a fundamental limit on how many distinct dynamical regimes a system of given D_eff can simultaneously sustain."),

("Q4", "statistical-distribution", True,
 "RLCT is a dimension of the model's singular set in parameter space — D-sensitive through algebraic geometry.",
 "Q4 (SLT-Biology Correspondence) asks whether the real log canonical threshold from Singular Learning Theory predicts biological neural circuit complexity — a deep connection between algebraic geometry and biological information processing."),

("Q5", "thermodynamic-bound", True,
 "The energy cost of synchronization depends on the network topology and effective dimension — higher D_eff networks have different synchronization costs.",
 "Q5 (Information Cost of Synchronization) asks what the thermodynamic minimum cost is for a network to achieve phase synchronization — a Landauer-type bound for collective behavior."),

("P12_STATUS", "dimensional-scaling", True,
 "Validating β(λ) across domains requires measuring D_eff in multiple systems — a dimensional scaling inference problem.",
 "P12 Validation Status tracks empirical evidence for the β(λ) formula's cross-domain validity. It is the observational record for H5 (Scaling Exponent β(λ)) — the central dimensional scaling law."),

("P2_STATUS", "dimensional-scaling", True,
 "Testing whether metabolic exponent tracks vascular D_eff is a direct dimensional scaling inference test.",
 "P2 Validation Status tracks evidence that the metabolic scaling exponent in biological organisms correlates with independently measured vascular network fractal dimension."),

# --- INSTANTIATIONS ---
("X0_FIM_Regimes", "statistical-distribution", True,
 "FIM regime classification is based on Fisher Information matrix rank — directly measuring D_eff of the statistical manifold.",
 "X0 (Three FIM Regime Classification) instantiates the ordered/critical/disordered framework using Fisher Information geometry. The three regimes correspond to high, medium, and low effective dimensionality of the observable parameter space."),

("X1", "power-law-scaling", True,
 "Vascular metabolic scaling exponent = D_eff/(D_eff+1) for the vascular network — the D_eff of branching geometry directly sets the observed scaling exponent.",
 "X1 (Vascular/Metabolic Instantiation) applies the DS framework to organismal metabolism, showing how fractal vascular network dimension determines the Kleiber exponent."),

("X2", "statistical-distribution", True,
 "Information geometry regime is D-sensitive through Fisher matrix rank — D_eff of the statistical manifold is the directly measured quantity.",
 "X2 (Information Geometry Instantiation) applies the DS framework to statistical manifolds, using Fisher information rank as the D_eff probe in the information-geometric regime."),

("X3", "statistical-distribution", True,
 "Statistical physics critical exponents are D-sensitive — the universality class (and thus the exponent set) depends on effective dimension.",
 "X3 (Statistical Physics Instantiation) applies the DS framework to phase transitions, testing whether observed critical exponents match D_eff-dependent predictions from universality theory."),

("X4", "wave-equation", True,
 "Quantum systems instantiation — Schrödinger equation with ℏ that runs with D_eff through Ω_D.",
 "X4 (Quantum Systems Instantiation) applies the DS framework to quantum mechanical systems, testing whether quantum signatures (energy levels, tunneling rates, uncertainty bounds) shift with D_eff as Ω_D predicts."),

("X5", "equilibrium-condition", True,
 "Ecological network structure and stability are D-sensitive through the effective dimension of the interaction network.",
 "X5 (Ecological Networks Instantiation) applies the DS framework to species interaction networks, asking whether the network's effective dimension determines which competitive equilibria are stable."),

("X6", "power-law-scaling", True,
 "Neural scaling laws (neurons, synapses, brain volume) follow power-law exponents that may encode D_eff of the neural connectivity graph.",
 "X6 (Neural Networks Instantiation) applies the DS framework to neural architecture scaling, asking whether the power-law exponents in brain scaling laws encode the effective dimension of neural connectivity."),

("X7", "dimensional-scaling", True,
 "Developmental biology morphogenetic scaling depends on tissue geometry and D_eff of the developmental field.",
 "X7 (Developmental Biology Instantiation) applies the DS framework to embryonic development, asking whether body plan scaling and morphogenetic gradient geometry reflect D_eff of the developmental tissue."),

# ===========================================================================
# REFERENCE LAWS (96 entries)
# ===========================================================================

# --- CLASSICAL MECHANICS ---
("CM1", "conservation-law", True,
 "Newton's laws hold in Euclidean D=3 space — in D dimensions, the equations retain the same form but the geometric structure of force (inverse-square for gravity) changes.",
 "Newton's Laws of Motion define the conservation of momentum (3rd law = action-reaction) and its rate of change (2nd law = F = dp/dt). They are D=3 classical mechanics but their variational parent (AM1, least action) generalizes to any D."),

("CM2", "inverse-square-geometric", True,
 "F ∝ r⁻² is a D=3 Gauss-law consequence — in D spatial dimensions gravitational force scales as r^(−D+1). Ω_D predicts G itself runs with D_eff.",
 "Newton's Law of Universal Gravitation is the defining example of inverse-square geometric dilution — the same mathematical form as Coulomb's law, differing only in the coupling constant and source type."),

("CM3", "geometric-ratio", True,
 "Elliptical orbits are conic sections from inverse-square force in D=3 — the orbital geometry changes if the force law exponent changes with D_eff.",
 "Kepler's First Law (Elliptical Orbits) expresses the geometric consequence of inverse-square gravity: the only closed orbits are ellipses, whose shape parameters encode orbital energy and angular momentum."),

("CM4", "conservation-law", True,
 "Equal areas follows from angular momentum conservation, which follows from rotational symmetry via Noether — rotational symmetry and its conservation law are D-sensitive through the structure of SO(D).",
 "Kepler's Second Law (Equal Areas) is a conservation law — areal velocity is constant because angular momentum is conserved. It is the orbital expression of Noether's theorem applied to rotational symmetry."),

("CM5", "power-law-scaling", True,
 "T² ∝ a³ encodes the r⁻² force exponent in D=3 — in D dimensions the Kepler exponent becomes 2/(D−1), making this a direct dimensional probe of gravitational geometry.",
 "Kepler's Third Law (T² ∝ a³) is a power law whose exponent 3/2 encodes the D=3 gravitational potential. It is structurally analogous to Kleiber's metabolic scaling (C1): both are power laws whose exponents are rational functions of effective dimension."),

("CM6", "conservation-law", True,
 "Euler's rigid-body equations conserve angular momentum in D=3 — the moment of inertia tensor is D-sensitive as a geometric object.",
 "Euler's Laws of Motion for rigid bodies extend Newton's laws to rotational degrees of freedom. They conserve the same quantities (linear and angular momentum) but applied to the rotational geometry of extended bodies."),

("CM7", "geometric-ratio", False,
 "Buoyancy equals weight of displaced fluid — a direct geometric consequence of pressure integration over volume in a gravitational field; the ratio is determined by D=3 volume integration, invariant for practical purposes.",
 "Archimedes' Principle is a geometric ratio law: the buoyant force equals exactly the weight of displaced fluid, following from pressure integration over any submerged shape in a gravitational field."),

("CM8", "coupled-field-equations", True,
 "F = q(E + v×B) couples particle mechanics to Maxwell fields — the cross-product structure is D=3 specific, and the coupling constants ε₀, μ₀ (and thus c) run with D_eff through Ω_D.",
 "The Lorentz Force Law couples the motion of charged particles to electromagnetic fields, completing the system of classical electrodynamics when combined with Maxwell's equations."),

# --- ANALYTICAL MECHANICS ---
("AM1", "variational-principle", True,
 "The action S = ∫L dt is a geometric quantity in configuration space — its stationary paths are geodesics. The constant ℏ that weights paths in the quantum path integral is D-sensitive through Ω_D.",
 "The Principle of Least Action is the variational parent of all of classical mechanics, electrodynamics, general relativity, and quantum mechanics. It is the most compressed statement of physical law: one functional, one condition (δS=0), all dynamics."),

("AM2", "variational-principle", True,
 "Euler-Lagrange equations are derived from least action in any configuration space dimension — but the Lagrangian's kinetic term T depends on the geometry of configuration space, which is D-sensitive.",
 "The Euler-Lagrange Equations are the equations of motion derived from the action principle. Every classical field theory — mechanics, electrodynamics, general relativity — is summarized by specifying a Lagrangian and applying these equations."),

("AM3", "variational-principle", True,
 "Phase space has a natural symplectic structure that is preserved by Hamiltonian flow — symplectic geometry is D-sensitive through the dimension of phase space (2D-dimensional for a D-dimensional system).",
 "Hamilton's Equations reformulate mechanics in phase space (q, p), where the Hamiltonian H generates time evolution. Phase-space geometry is the natural home of statistical mechanics, quantum mechanics, and Fisher information."),

("AM4", "variational-principle", True,
 "Hamilton-Jacobi bridges classical trajectories to quantum wave mechanics through ℏ → 0 limit — ℏ is D-sensitive through Ω_D, shifting where the classical-quantum boundary lies.",
 "The Hamilton-Jacobi Equation is the classical-quantum bridge: in the limit ℏ → 0, the Schrödinger equation reduces to Hamilton-Jacobi. Solutions give classical trajectories as characteristics of a first-order PDE."),

("AM5", "symmetry-conservation", True,
 "Noether's theorem applies to continuous symmetries of the action — symmetry groups change structure with D (e.g., rotation group SO(D) changes), potentially altering which conservation laws exist.",
 "Noether's Theorem is the deepest explanation of conservation laws: every continuous symmetry of the action generates a conserved current. It is the mathematical backbone connecting geometry to physics across all domains."),

# --- THERMODYNAMICS ---
("TD1", "equilibrium-condition", False,
 "Transitivity of thermal equilibrium is a logical property that defines temperature as an equivalence class — it does not depend on spatial dimension.",
 "The Zeroth Law of Thermodynamics defines thermal equilibrium as a transitive relation, making temperature a well-defined global property. It is the logical prerequisite for all other thermodynamic laws."),

("TD2", "conservation-law", False,
 "Energy conservation follows from time-translation symmetry via Noether — and time-translation symmetry may be broken if constants run with D_eff, making this a subtle D-sensitivity.",
 "The First Law of Thermodynamics is the statement that energy is conserved: dU = δQ − δW. It is the Noether consequence of time-translation symmetry and bounds all energy-converting processes."),

("TD3", "thermodynamic-bound", True,
 "Entropy production rates, phase-space volumes, and equilibrium distributions are D-dependent through the density of states — in D dimensions the entropy of ideal systems scales differently.",
 "The Second Law of Thermodynamics (ΔS ≥ 0) is the master thermodynamic constraint. It defines the arrow of time, limits engine efficiency, and sets the thermodynamic cost of information erasure (B5, Landauer)."),

("TD4", "thermodynamic-bound", True,
 "The quantum ground state energy and its degeneracy are D-sensitive — in D dimensions zero-point energy and entropy at T→0 depend on the density of states of the quantum system.",
 "The Third Law of Thermodynamics establishes that entropy approaches a constant minimum at absolute zero, making T=0 unreachable in finite steps. It governs all near-zero-temperature quantum behavior."),

("TD5", "conservation-law", True,
 "The fundamental relation combines all thermodynamic variables — the chemical potential μ and pressure P terms depend on the geometry of available states, which is D-sensitive.",
 "The Fundamental Thermodynamic Relation dU = TdS − PdV + Σμ_i dN_i is the master equation from which all other thermodynamic relations derive through Legendre transformation."),

("TD6", "gradient-flux-transport", False,
 "Onsager symmetry L_ij = L_ji follows from time-reversal symmetry of microscopic dynamics — a discrete symmetry that holds regardless of spatial D_eff.",
 "Onsager Reciprocal Relations state that cross-coupling transport coefficients are symmetric near equilibrium. They are the foundational result of linear non-equilibrium thermodynamics."),

("TD7", "statistical-distribution", True,
 "The Boltzmann equation's H-theorem and equilibrium distribution depend on the dimensionality of velocity space — in D spatial dimensions the Maxwell-Boltzmann distribution has D velocity components.",
 "The Boltzmann Equation describes the statistical evolution of phase-space distribution functions in dilute gases. Its H-theorem bridges microscopic reversibility to macroscopic irreversibility (TD3, 2nd law)."),

("TD8", "thermodynamic-bound", False,
 "Carnot efficiency η = 1 − T_cold/T_hot is a ratio of absolute temperatures — D-invariant as a bound, though the absolute temperature scale involves k_B which is D-sensitive through Ω_D.",
 "Carnot's Theorem establishes the maximum efficiency of any heat engine operating between two temperature reservoirs. It is the thermodynamic ceiling on all energy conversion — a bound analogous to Ashby's variety (F1) in the information domain."),

("TD9", "exponential-decay", False,
 "Newton's cooling rate constant k depends on surface area and heat transfer coefficient — in D dimensions the surface-to-volume ratio changes (A1, Square-Cube), introducing D-sensitivity through geometry.",
 "Newton's Law of Cooling describes exponential thermal equilibration: temperature difference decays at a rate proportional to itself. Same mathematical skeleton as radioactive decay (B1) and Arrhenius (B2)."),

("TD10", "gradient-flux-transport", True,
 "Fourier's law in D dimensions produces a D-dimensional diffusion equation ∂T/∂t = α∇²T — the Laplacian ∇² is D-sensitive, changing how heat spreads in different spatial dimensions.",
 "Fourier's Law of Heat Conduction (q = −k∇T) is the prototype gradient-flux transport law. Combined with energy conservation it yields the heat equation — the same equation that governs mass diffusion (DM1, Fick's), electrical conduction (EM9, Ohm's), and fluid pressure (FM4, Poiseuille's)."),

("TD11", "geometric-ratio", False,
 "Molar heat capacity additivity is an empirical approximation based on atomic count — D-invariant as a counting rule.",
 "Kopp's Law states that molar heat capacity is approximately additive over atomic contributions. It is an empirical approximation to the full quantum statistical result, valid at room temperature."),

("TD12", "statistical-distribution", True,
 "Equipartition assigns k_BT/2 per classical degree of freedom — in D dimensions a monatomic solid has 3D translational + 3D potential = 6D/2 contributions, making the limit D-sensitive.",
 "The Dulong-Petit Law gives the classical high-temperature heat capacity limit of 3R per mole. Its failure at low temperatures historically signaled the need for quantum mechanics — a D-sensitive breakdown."),

("TD13", "thermodynamic-bound", False,
 "The Carnot cycle definition of temperature is a ratio of heat flows — D-invariant as a measurement procedure.",
 "Carnot Efficiency and Thermodynamic Temperature defines the absolute temperature scale operationally through reversible Carnot cycle heat ratios, making temperature a physical quantity independent of any material property."),

# --- ELECTROMAGNETISM ---
("EM1", "inverse-square-geometric", True,
 "∇·E = ρ/ε₀ gives E ∝ r^(−D+1) in D dimensions — the inverse-square in D=3 becomes inverse-cube in D=4. ε₀ runs with D_eff through c = 1/√(ε₀μ₀).",
 "Gauss's Law for Electricity is one of Maxwell's four equations and the electrostatic expression of inverse-square geometric dilution. It has identical mathematical structure to Gauss's Law for Gravity (GV3) — the same equation with different coupling constant."),

("EM2", "symmetry-conservation", True,
 "∇·B = 0 is a topological statement — no magnetic monopoles. In D dimensions the magnetic field structure and its topological constraints change with the dimensionality of the field space.",
 "Gauss's Law for Magnetism (∇·B = 0) is a topological constraint: magnetic field lines always close, with no sources or sinks. It connects to topological invariants (H4, χ_eff) and the non-existence of isolated magnetic charges."),

("EM3", "coupled-field-equations", True,
 "Faraday's law couples changing B to curling E — the coupling constant (speed of light c) runs with D_eff through Ω_D acting on ε₀ and μ₀.",
 "Faraday's Law of Induction (∇×E = −∂B/∂t) describes how changing magnetic fields induce electric fields, completing the electromagnetic coupling. Lenz's law (EM8) gives the sign — the induced current opposes the change."),

("EM4", "coupled-field-equations", True,
 "Ampère-Maxwell law unifies current-driven and displacement-current-driven B fields — the coupling c = 1/√(ε₀μ₀) runs with D_eff, changing the speed of electromagnetic wave propagation.",
 "The Ampère-Maxwell Law (∇×B = μ₀J + (1/c²)∂E/∂t) completes Maxwell's system. Maxwell's addition of the displacement current term predicted electromagnetic waves — one of the greatest theoretical predictions in physics."),

("EM5", "conservation-law", True,
 "∂ρ/∂t + ∇·J = 0 is the local charge conservation law — it follows from gauge symmetry via Noether (AM5). In D dimensions the same PDE structure holds, but D-sensitive through the geometry of J.",
 "The Continuity Equation (∂ρ/∂t + ∇·J = 0) is the local statement of charge conservation, following from the gauge symmetry of electrodynamics. The same PDE form governs mass, energy, probability, and any other locally conserved quantity."),

("EM6", "inverse-square-geometric", True,
 "F ∝ r⁻² is D=3 specific — Coulomb's law is the electrostatic Gauss-law consequence in D=3, identical in structure to Newton's gravity (CM2). ε₀ runs with D_eff.",
 "Coulomb's Law is the electrostatic inverse-square law, structurally identical to Newton's gravitation. Both are D=3 Gauss-law consequences — electric charge and gravitational mass are sources of fields that dilute geometrically over spherical surfaces."),

("EM7", "inverse-square-geometric", True,
 "Biot-Savart produces B ∝ r⁻² in D=3 — the cross-product structure is D=3-specific and the coupling μ₀ runs with D_eff through c = 1/√(ε₀μ₀).",
 "The Biot-Savart Law is the magnetostatic inverse-square law: magnetic field from a current element falls off as r⁻² with a direction given by the cross-product (D=3-specific). It is the magnetic analog of Coulomb's law."),

("EM8", "equilibrium-condition", True,
 "Lenz's law defines the stability condition for electromagnetic induction — the equilibrium is the state of no net flux change. The coupling is D-sensitive through c and ε₀/μ₀.",
 "Lenz's Law states that induced currents oppose the changes causing them — the electromagnetic Le Chatelier principle. It is the stability-restoring condition of the electromagnetic field, analogous to Le Chatelier in chemistry (KC1) and saturation dynamics in biology (F4)."),

("EM9", "gradient-flux-transport", False,
 "V = IR is a linear dissipative transport law — the resistance R is a material property not a geometric dimension. D-invariant in its functional form.",
 "Ohm's Law (V = IR, equivalently J = σE) is the electrical gradient-flux transport law: current density proportional to electric field gradient. It is the electrical member of the transport equivalence class with Fourier (TD10) and Fick (DM1)."),

("EM10", "conservation-law", False,
 "KCL and KVL are network-level conservation laws — charge conservation at nodes (KCL) and energy conservation around loops (KVL). The network topology is D-invariant as a combinatorial property.",
 "Kirchhoff's Laws are the network-level expressions of charge conservation (KCL) and energy conservation (KVL). They are the macroscopic circuit consequences of the microscopic Maxwell equations applied to lumped-element networks."),

("EM11", "thermodynamic-bound", False,
 "Joule heating P = I²R produces entropy at rate P/T — the dissipation is a first-law consequence that is D-invariant in form (though R may be D-sensitive for materials with geometric structure).",
 "Joule's Law (P = I²R) describes the irreversible conversion of electrical energy to heat. It is the thermodynamic consequence of Ohm's law — resistive flow is always dissipative, making perfect conductors thermodynamically special."),

# --- OPTICS ---
("OP1", "variational-principle", True,
 "Optical path length δ∫n ds = 0 is a variational principle in optical configuration space — n(r) plays the role of the Lagrangian, and the effective optical dimension changes with the refractive index structure.",
 "Fermat's Principle of Least Time is the variational parent of geometric optics. It is structurally identical to the Principle of Least Action (AM1) — the same mathematical structure, different configuration space."),

("OP2", "geometric-ratio", True,
 "θ_i = θ_r is a geometric symmetry of path length with respect to the surface normal — in D dimensions reflection geometry changes with the dimensionality of the interface.",
 "The Law of Reflection is a geometric ratio law derived from Fermat's principle: the path of minimum time at a flat interface bisects the angle of incidence and reflection. It expresses the symmetry of optical path length across the surface normal."),

("OP3", "geometric-ratio", True,
 "n₁ sin θ₁ = n₂ sin θ₂ conserves the tangential wave vector at an interface — in D dimensions the wave vector has D−1 tangential components, changing the form of the conservation condition.",
 "Snell's Law of Refraction quantifies how light bends at a medium interface, conserving the tangential component of the wave vector. The refractive index n is the optical analog of D_eff: it governs how wave speed — and thus propagation — changes across a boundary."),

("OP4", "geometric-ratio", True,
 "Brewster's angle encodes the orthogonality condition for reflected/refracted rays — a geometric property of wave polarization in D=3 that changes in other dimensions.",
 "Brewster's Angle is a geometric ratio law: at tan θ_B = n₂/n₁, the reflected and refracted rays are perpendicular, producing fully polarized reflected light. It is an electromagnetic boundary condition with geometric character."),

("OP5", "geometric-ratio", True,
 "I = I₀ cos²θ is a projection law — the transmitted amplitude is the component of the electric field vector aligned with the polarizer. In D dimensions, projection geometry changes with the dimensionality of the field.",
 "Malus's Law describes intensity transmission through polarizers as a squared-cosine projection. The cos²θ projection structure appears across domains: quantum Born rule (|⟨ψ|φ⟩|²), dimensional projection loss (Ax2), and polarization filtering."),

("OP6", "exponential-decay", False,
 "Beer-Lambert's exponential attenuation is governed by absorption cross-section and path length — a geometric path property that is D-invariant in the absorption probability per unit length.",
 "The Beer-Lambert Law describes exponential decay of light intensity with path length through an absorbing medium. It is the optical member of the exponential-decay equivalence class alongside radioactive decay (B1), Arrhenius (B2), and Newton's cooling (TD9)."),

# --- RADIATION ---
("RD1", "statistical-distribution", True,
 "Planck's spectral distribution is D-dependent: radiation density ∝ ν^D in D spatial dimensions, and the Stefan-Boltzmann exponent becomes D+1. h and c both run with D_eff through Ω_D.",
 "Planck's Law of Black-Body Radiation is the parent law generating Wien's law (B3) and Stefan-Boltzmann (RD2) as limits. It is the first quantum statistical distribution law — the birth of quantum mechanics — and one of the most D-sensitive laws in the reference database."),

("RD2", "dimensional-scaling", True,
 "Stefan-Boltzmann exponent T^4 = T^(D+1) for D=3 — the exponent is a direct dimensional signature. In D spatial dimensions it becomes T^(D+1), making this one of the clearest tests of effective dimension in radiation physics.",
 "The Stefan-Boltzmann Law (P/A ∝ T⁴) is a dimensional scaling law: the T⁴ exponent encodes D=3. It is the integrated version of Planck's distribution (RD1) and a structural analog of Kleiber's metabolic scaling (C1) — both have exponents that are simple functions of D."),

("RD3", "conservation-law", True,
 "E = hν quantizes energy in units of h — Ω_D acts on h directly, shifting the quantum of action and thus all energy discretization scales.",
 "The Planck-Einstein Relation (E = hν) quantizes electromagnetic energy into photons. It bridges the thermodynamic energy scale and the geometric frequency scale through the Planck constant h — which Ω_D acts on, making this the most fundamental D-sensitive coupling constant in quantum physics."),

# --- QUANTUM MECHANICS ---
("QM1", "wave-equation", True,
 "Schrödinger equation contains ℏ explicitly — Ω_D predicts ℏ runs with D_eff, shifting energy levels, tunneling rates, and the boundary between quantum and classical behavior.",
 "The Schrödinger Equation (iℏ∂ψ/∂t = Ĥψ) is the wave equation for quantum mechanical probability amplitudes. It is the quantum analog of Hamilton's equations (AM3), with ℏ setting the scale of quantum discretization. If ℏ runs with D_eff as Ω_D predicts, all quantum phenomena become D-sensitive."),

("QM2", "thermodynamic-bound", True,
 "ΔxΔp ≥ ℏ/2 is a bound whose minimum is set by ℏ — D-sensitive through Ω_D. In the DS reading, ℏ encodes the projection grain from higher to lower D_eff.",
 "The Heisenberg Uncertainty Principle is a thermodynamic bound on simultaneous measurement precision. In the DS information-theoretic reading, ℏ encodes the irreducible information loss from projecting higher-D phase space onto lower-D observations — connecting Heisenberg to Ax1 (Information Primacy) and Ax2 (D_eff)."),

("QM3", "symmetry-conservation", True,
 "Fermion antisymmetry is a symmetry constraint on Hilbert space — in D dimensions the permutation group structure changes, and the statistics of particles (fermion vs. boson) depend on D through the spin-statistics theorem.",
 "The Pauli Exclusion Principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions must be antisymmetric under particle exchange. It is the quantum analog of Gause's competitive exclusion (F3) — no two identical fermions can occupy the same quantum state."),

("QM4", "wave-equation", True,
 "λ = h/p involves h directly — D-sensitive through Ω_D. The de Broglie wavelength sets the scale at which quantum effects become important, and this scale shifts if h runs with D_eff.",
 "The de Broglie Wavelength (λ = h/p) is the wave-particle duality relation. It defines the quantum-classical boundary: when λ is comparable to system size, quantum effects dominate. This boundary shifts if h runs with D_eff."),

("QM5", "symmetry-conservation", True,
 "c-invariance is a geometric constraint on spacetime — in D+1 dimensional spacetime the Lorentz group SO(D,1) changes structure. Ω_D takes c as invariant at D_eff=4 by construction.",
 "The Postulates of Special Relativity establish c-invariance as a fundamental spacetime symmetry generating Lorentz transformations. The DS framework takes c as invariant at D_eff=4 by construction of Ω_D, with behavior at D_eff≠4 left as an open conjecture."),

# --- GRAVITATION ---
("GV1", "coupled-field-equations", True,
 "Einstein field equations couple spacetime geometry to matter-energy — the coupling constant 8πG/c⁴ contains both G and c, both of which Ω_D acts on, making GR one of the most D-sensitive coupled field systems.",
 "General Relativity (Einstein Field Equations) identifies gravity with spacetime curvature. It is the most fundamental coupled field system: geometry and matter mutually determine each other. The DS framework's Ω_D modifies the dimensional substrate that GR assumes to be fixed at D=3+1."),

("GV2", "coupled-field-equations", True,
 "GEM equations have Maxwell-like structure with G replacing 1/ε₀ — G runs with D_eff through Ω_D, making gravitomagnetic effects D-sensitive.",
 "Gravitoelectromagnetism describes weak-field GR in Maxwell-like form, revealing the structural identity between gravity and electromagnetism when both are treated as geometric field theories in D=3+1."),

("GV3", "inverse-square-geometric", True,
 "∇·g = −4πGρ gives g ∝ r^(−D+1) in D dimensions — identical structure to EM1 (Gauss electricity). G runs with D_eff through Ω_D.",
 "Gauss's Law for Gravity is the Newtonian analog of Gauss's Law for Electricity (EM1) — the same equation with G replacing 1/ε₀ and mass replacing charge. It is the clearest demonstration that gravity and electrostatics are the same mathematical structure in different physical domains."),

# --- FLUID MECHANICS ---
("FM1", "diffusion-equation", True,
 "Navier-Stokes is strongly D-sensitive: 2D turbulence exhibits inverse energy cascade (large vortices from small inputs); 3D exhibits forward cascade (energy to small scales). This dimensional dependence of cascade direction makes FM1 a direct test of D_eff.",
 "Navier-Stokes Equations are the nonlinear diffusion equation for fluid momentum. Their dimension-dependence is one of the most dramatic in physics: the direction of turbulent energy cascade reverses between D=2 and D=3, providing a direct experimental probe of effective dimension."),

("FM2", "conservation-law", True,
 "Bernoulli's principle is energy conservation along streamlines — in D dimensions the pressure term couples to D-dimensional geometry through the velocity field's geometric structure.",
 "Bernoulli's Principle is energy conservation applied to inviscid fluid flow along a streamline: higher velocity corresponds to lower pressure. It governs aerodynamic lift, cardiovascular pressure, and venturi flow."),

("FM3", "conservation-law", True,
 "Euler fluid equations are the inviscid limit of Navier-Stokes — D-sensitive through the geometric structure of the pressure gradient and velocity field in D dimensions.",
 "Euler's Fluid Equations are the inviscid (zero viscosity) Navier-Stokes. Without dissipation the equations are time-reversible; viscosity (FM1) breaks this symmetry. The transition is a regime change in the sense of H1 (Regime mechanism)."),

("FM4", "power-law-scaling", True,
 "Q ∝ r⁴ — the radius-to-the-fourth scaling is a D=3 geometric consequence of parabolic velocity profile in cylindrical geometry. In D dimensions the exponent changes with the geometry of the conduit.",
 "Poiseuille's Law (Q = πr⁴ΔP/8ηL) is a power-law scaling law: flow scales as radius to the fourth power, a strong geometric effect. It is the microscopic mechanism driving metabolic scaling (C1) — vascular radius distribution determines organismal metabolism."),

("FM5", "gradient-flux-transport", False,
 "Stokes drag F = 6πηrv is linear in velocity — a gradient-flux transport law in the low-Reynolds-number (viscosity-dominated) regime. D-invariant in form for creeping flow.",
 "Stokes' Law gives the drag force on a sphere at low Reynolds number: F ∝ r·v, linear in both size and speed. It governs the motion of cells, bacteria, and colloidal particles — all systems where viscosity dominates over inertia."),

("FM6", "gradient-flux-transport", False,
 "Faxén corrections add gradient terms to Stokes drag — D-invariant in functional form as higher-order flow corrections.",
 "Faxén's Law generalizes Stokes' drag to non-uniform flow fields, adding corrections proportional to the gradient of the undisturbed flow. It is the next-order correction in the gradient-flux transport expansion for viscous drag."),

# --- CHEMISTRY KINETICS & EQUILIBRIUM ---
("KC1", "equilibrium-condition", False,
 "Le Chatelier's principle specifies the direction of equilibrium shift under perturbation — a logical constraint on equilibrium restoration that is D-invariant as a qualitative principle.",
 "Le Chatelier's Principle is the equilibrium-condition of the chemical domain: any perturbation drives a restoring shift. It is the chemical analog of Lenz's law (EM8) and the ecological analog of competitive exclusion stability."),

("KC2", "equilibrium-condition", False,
 "Detailed balance at equilibrium follows from time-reversal symmetry of microscopic dynamics — a discrete symmetry that is D-invariant.",
 "The Law of Microscopic Reversibility (Detailed Balance) states that at equilibrium every elementary process is exactly balanced by its reverse. It is the molecular foundation of Onsager reciprocal relations (TD6) and the thermodynamic condition that defines true equilibrium."),

("KC3", "thermodynamic-bound", False,
 "Hammond-Leffler describes transition state geometry relative to reactant/product energy — a bound on transition state position that is D-invariant in its thermodynamic form.",
 "The Hammond-Leffler Postulate relates transition state geometry to reaction thermodynamics: exothermic reactions have reactant-like transition states; endothermic have product-like. It is an empirical rule linking the geometry of the energy landscape to its thermodynamic slope."),

("KC4", "conservation-law", False,
 "Hess's law is enthalpy conservation along a thermodynamic cycle — a path-independence statement that follows directly from TD2 (first law) and is D-invariant.",
 "Hess's Law states that enthalpy change is path-independent — it depends only on initial and final states. It is the thermochemical expression of energy conservation (TD2), enabling calculation of reaction enthalpies from tabulated values."),

("KC5", "thermodynamic-bound", False,
 "ΔG = ΔH − TΔS sets the thermodynamic spontaneity criterion — D-invariant in form, though T and k_B are D-sensitive through Ω_D.",
 "The Gibbs-Helmholtz Equation (ΔG = ΔH − TΔS) is the master free-energy criterion for spontaneity at constant T and P. It is the thermodynamic potential that determines chemical equilibrium and is the parent of Le Chatelier (KC1) and reaction kinetics (B2, Arrhenius)."),

("KC6", "equilibrium-condition", False,
 "Raoult's law is an ideal-solution equilibrium condition — D-invariant as a mole-fraction proportionality.",
 "Raoult's Law gives the vapor pressure of an ideal solution component as proportional to its mole fraction. It is the equilibrium condition for gas-liquid phase partitioning in ideal solutions — deviations signal non-ideal molecular interactions."),

("KC7", "equilibrium-condition", True,
 "Henry's law C = k_H·P saturates at high P (F4-type behavior) — the saturation ceiling is set by binding geometry, which is D-sensitive through molecular surface area and diffusion-limited kinetics.",
 "Henry's Law describes the linear equilibrium between dissolved gas concentration and partial pressure. The linear regime breaks down at high concentrations — a saturation behavior analogous to F4 (Saturation Dynamics) — governing blood gas exchange and ocean CO₂ absorption."),

("KC8", "geometric-ratio", False,
 "Fixed mass ratios in compounds follow from discrete atomic combining geometry — a combinatorial geometric constraint that is D-invariant.",
 "The Law of Definite Composition states that chemical compounds always contain elements in fixed mass ratios, regardless of source. It is the empirical foundation of atomic theory — discrete atoms combine in fixed integer ratios, an early signal of quantum discretization."),

("KC9", "geometric-ratio", False,
 "Integer combining ratios are a combinatorial consequence of discrete atomic geometry — D-invariant.",
 "Dalton's Law of Multiple Proportions states that when two elements form multiple compounds, the combining mass ratios are small integers. Together with KC8 (Definite Composition), it provides direct evidence for discrete atomic structure preceding quantum mechanics."),

("KC10", "geometric-ratio", False,
 "Equivalent weight consistency is a combinatorial geometric property of atomic bonding — D-invariant.",
 "The Law of Reciprocal Proportions completes the stoichiometric triad with KC8 and KC9: the ratio of combining weights with a third element is consistent across different compounds. All three laws reflect the discrete, combinatorial geometry of atomic bonding."),

# --- DIFFUSION & MASS TRANSPORT ---
("DM1", "gradient-flux-transport", True,
 "Fick's diffusion equation ∂c/∂t = D∇²c is D-sensitive through the Laplacian: in D dimensions diffusive return probability changes (recurrent in D≤2, transient in D>2), dramatically affecting how diffusion-limited processes behave.",
 "Fick's Laws of Diffusion (J = −D∇c; ∂c/∂t = D∇²c) are the mass-transport members of the gradient-flux equivalence class. Structurally identical to Fourier's heat equation (TD10) with concentration replacing temperature and diffusivity replacing thermal conductivity."),

("DM2", "statistical-distribution", False,
 "Graham's law r ∝ 1/√M follows from kinetic energy equipartition — k_BT/2 per degree of freedom — a statistical distribution result that is D-invariant in its mass-dependence.",
 "Graham's Law (diffusion rate ∝ 1/√M) follows from kinetic energy equipartition: at fixed temperature all gas molecules have the same mean kinetic energy, so lighter molecules move faster. It quantifies mass-dependent diffusion in the same framework as DM1 (Fick's)."),

("DM3", "diffusion-equation", True,
 "Lamm equation combines diffusion (∇²c, D-sensitive) with centrifugal sedimentation (radial geometry, D-sensitive through cylindrical coordinate structure).",
 "The Lamm Equation generalizes Fick's diffusion to centrifugal fields, describing sedimentation-diffusion competition. It is the governing equation of analytical ultracentrifugation — the technique for measuring macromolecular masses and shapes."),

("DM4", "conservation-law", False,
 "P_total = ΣP_i is an additive conservation law for ideal gas partial pressures — D-invariant as a superposition principle.",
 "Dalton's Law of Partial Pressures states that total pressure equals the sum of partial pressures. It is a conservation law for ideal gas pressure — each component contributes independently, applying GL1 (Ideal Gas Law) to mixtures."),

# --- GAS LAWS ---
("GL1", "equilibrium-condition", True,
 "PV = nRT — in D spatial dimensions the ideal gas law changes: pressure involves force per (D−1)-dimensional surface, volume is D-dimensional, and the gas constant R = N_Ak_B is D-sensitive through k_B.",
 "The Ideal Gas Law (PV = nRT) unifies Boyle's, Charles's, Gay-Lussac's, and Avogadro's laws into a single equation of state. It is the equilibrium condition for an ideal gas — the reference state from which all real-gas behavior is measured as deviation."),

("GL2", "equilibrium-condition", True,
 "Boyle's isothermal PV = const is a special case of GL1 at fixed T — D-sensitive through the D-dimensional form of the ideal gas law.",
 "Boyle's Law (P₁V₁ = P₂V₂ at constant T) is the isothermal equilibrium condition for ideal gases. It is a special case of GL1 (Ideal Gas Law) historically discovered before the unified picture."),

("GL3", "equilibrium-condition", False,
 "Charles's law V ∝ T at fixed P is the isobaric condition — D-invariant in the ratio form, though absolute temperature involves k_B.",
 "Charles's Law (V/T = const at constant P) is the isobaric equilibrium condition for ideal gases, establishing volume proportional to absolute temperature. Historically used to extrapolate to absolute zero."),

("GL4", "equilibrium-condition", False,
 "Gay-Lussac's P ∝ T at fixed V is the isochoric condition — D-invariant in ratio form.",
 "Gay-Lussac's Law (P/T = const at constant V) is the isochoric equilibrium condition for ideal gases: pressure proportional to absolute temperature at fixed volume. Relevant to pressure vessel safety and gas thermometry."),

("GL5", "equilibrium-condition", True,
 "Avogadro's V ∝ n at fixed T, P — in D dimensions the relationship between molecular count and volume changes through the D-dimensional kinetic theory derivation.",
 "Avogadro's Law (V/n = const at fixed T, P) establishes that volume is determined by molecular count regardless of molecular identity — a profound demonstration that molecular number, not type, determines thermodynamic volume."),

# --- BIOLOGY ---
("BIO1", "statistical-distribution", False,
 "Mendelian ratios (3:1, 1:1, etc.) are combinatorial counting results — discrete probability distributions over allele combinations. D-invariant as combinatorics.",
 "Mendelian Laws of Inheritance describe discrete information transmission: alleles segregate independently and combine combinatorially. They are the genetic analog of definite composition laws (KC8-KC9) — information transmits in discrete quanta, not continuously."),

("BIO2", "equilibrium-condition", False,
 "Hardy-Weinberg equilibrium p² + 2pq + q² = 1 is a population genetics equilibrium condition — D-invariant as a combinatorial probability statement.",
 "The Hardy-Weinberg Principle defines the population genetic equilibrium: allele frequencies remain constant in the absence of evolutionary forces. It is the null model for evolutionary genetics — the equilibrium condition from which all selection, drift, and migration produce measurable departures."),

("BIO3", "statistical-distribution", True,
 "Fisher's fundamental theorem — rate of fitness increase = additive genetic variance in fitness — is D-sensitive because Fisher information is D-sensitive through the dimensionality of the parameter space.",
 "Natural Selection and Fisher's Fundamental Theorem establishes that fitness increase equals additive genetic variance — and additive genetic variance IS Fisher information. This structural bridge (fitness maximization = Fisher information maximization) directly connects evolutionary biology to the DS framework's information-geometric core."),

# --- EARTH SCIENCES ---
("ES1", "gradient-flux-transport", True,
 "Spatial correlation decay rate encodes D_eff of the geographic substrate — a slower decay suggests higher-dimensional connectivity, directly testable with Ax2.",
 "Tobler's First Law of Geography (near things are more related than distant things) describes spatial autocorrelation decay. The decay rate encodes the effective dimensionality of the geographic network — making it a geographic probe of D_eff analogous to fractal dimension (H2)."),

("ES2", "dimensional-scaling", True,
 "Arbia's aggregation effect is a spatial scale-dependence of correlation — directly analogous to Ax2: observed correlations depend on the resolution of observation, which is a D_eff-scaling effect.",
 "Arbia's Law of Geography quantifies how spatial aggregation inflates apparent correlations. It is the geographic expression of the modifiable areal unit problem — the observation that measured statistics depend on the scale of measurement, exactly as Ax2 predicts for D_eff."),

("ES3", "power-law-scaling", True,
 "Archie's cementation exponent m encodes the fractal dimension of the pore network — a power-law scaling law with a D-sensitive exponent.",
 "Archie's Law (ρ_rock ∝ φ^(−m)) is a power-law scaling law relating rock resistivity to porosity. The cementation exponent m is a proxy for pore network fractal dimension — a D-sensitive parameter directly analogous to H2 (Fractal Dimension d_f)."),

("ES4", "coupled-field-equations", True,
 "Coriolis force is a rotating-frame geometric effect specific to D=3 — the cross-product structure of the Coriolis term (2Ω×v) is D=3-specific.",
 "Buys Ballot's Law describes wind direction relative to pressure gradients under Coriolis deflection. The Coriolis force is a D=3-specific geometric effect of rotating reference frames — it couples wind velocity to Earth's rotation through a cross-product, changing in D≠3."),

("ES5", "gradient-flux-transport", False,
 "Birch's law V_P ∝ M̄ is an empirical linear relationship — D-invariant in form as an empirical transport property correlation.",
 "Birch's Law relates compressional seismic velocity to mean atomic weight in minerals. It is an empirical linear transport law — analogous in form to gradient-flux transport laws but phenomenological rather than derived from first principles."),

("ES6", "thermodynamic-bound", False,
 "Byerlee's law gives a bilinear friction bound — the threshold shear stress is a thermodynamic dissipation limit. D-invariant as an empirical friction bound.",
 "Byerlee's Law gives the shear stress threshold for fault sliding — nearly universal across rock types. The bilinear form (two regimes separated at ~200 MPa) is a regime transition (H1) in frictional behavior, with the bound representing the thermodynamic ceiling for fault stability."),

("ES7", "power-law-scaling", True,
 "Titius-Bode's geometric spacing may reflect resonance conditions in protoplanetary disk D_eff — the exponential sequence a_n ≈ 0.4 + 0.3×2ⁿ suggests a period-doubling-like geometric progression.",
 "The Titius-Bode Law describes approximate geometric spacing of planetary orbits. Its status is contested (no established physical derivation), but the exponential progression connects structurally to Feigenbaum universality (D2) and period-doubling cascades."),

("ES8", "geometric-ratio", False,
 "Vertical stratigraphic ordering from gravitational deposition — a geometric constraint from gravity (CM2) that is D-invariant as a temporal ordering rule.",
 "Steno's Law of Superposition (oldest layers at bottom) is a geometric ratio law: gravitational deposition imposes vertical temporal ordering. It is the foundational principle of stratigraphy — spatial position (depth) encodes time."),

("ES9", "equilibrium-condition", False,
 "Minimum potential energy of gravitational field drives horizontal deposition — an equilibrium condition from gravitational mechanics. D-invariant.",
 "The Principle of Original Horizontality states that sedimentary layers are originally deposited horizontally — the gravitational potential energy minimum. Tilted strata indicate post-depositional deformation."),

("ES10", "geometric-ratio", False,
 "Lateral spatial continuity is a topological connectivity constraint — a geometric ratio law about spatial extent at deposition. D-invariant as a connectivity statement.",
 "The Principle of Lateral Continuity states that sedimentary layers extend laterally until they thin or reach basin edges. It allows correlation of rock layers across spatial gaps where physical continuity cannot be directly observed."),

("ES11", "geometric-ratio", False,
 "Geometric intersection implies temporal ordering — a topological containment argument. D-invariant as a logical geometric statement.",
 "The Principle of Cross-Cutting Relationships states that any feature cutting another must be younger. It is a topological temporal ordering from geometric intersection — the same logical structure as topological ordering in directed graphs (H4, χ_eff)."),

("ES12", "equilibrium-condition", False,
 "Faunal succession is a globally consistent temporal ordering — an equilibrium condition in evolutionary time. D-invariant as a historical record.",
 "The Principle of Faunal Succession states that fossil assemblages follow a globally consistent sequence, providing worldwide stratigraphic correlation. It is the geological record of evolutionary selection (BIO3) — natural selection operating over geological time."),

("ES13", "geometric-ratio", False,
 "Containment implies prior existence — a geometric ratio law from spatial inclusion. D-invariant as a logical statement.",
 "The Principle of Inclusions and Components states that rock fragments in a host rock predate the host. It is a geometric ratio law: containment implies temporal precedence — the same logical structure as cross-cutting relationships (ES11)."),

("ES14", "geometric-ratio", True,
 "Walther's law maps lateral spatial gradients to vertical temporal sequences — a space-time transformation that encodes the effective dimension of the depositional environment.",
 "Walther's Law of Facies states that laterally adjacent sedimentary environments appear vertically adjacent in the stratigraphic record. It is a space-time transformation law — lateral position maps to vertical (temporal) position — and is D-sensitive through the geometry of the depositional basin."),

]  # end ENTRY_DATA

# ===========================================================================
# Insertion
# ===========================================================================

def build_section_text(archetype: str, d_sensitive: bool, d_reason: str, entry_note: str) -> str:
    d_label = "D-sensitive" if d_sensitive else "D-invariant"
    prose = ARCHETYPES[archetype]
    return (
        f"Mathematical archetype: {archetype}\n\n"
        f"{prose}\n\n"
        f"Applied to this entry: {entry_note}\n\n"
        f"Dimensional sensitivity: {d_label} — {d_reason}"
    )


def run(db_path: str, entries: list, dry_run: bool = False):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    prop_inserted = 0
    sec_inserted = 0
    skipped = 0
    errors = []

    for row in entries:
        eid, archetype, d_sensitive, d_reason, entry_note = row

        # Verify entry exists
        if not cur.execute("SELECT 1 FROM entries WHERE id=?", (eid,)).fetchone():
            errors.append((eid, "entry not found in DB"))
            continue

        d_label = "D-sensitive" if d_sensitive else "D-invariant"
        section_text = build_section_text(archetype, d_sensitive, d_reason, entry_note)

        try:
            # --- entry_properties: mathematical_archetype ---
            cur.execute("""
                INSERT OR IGNORE INTO entry_properties
                  (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?, 'DS Facets', 'mathematical_archetype', ?, 1)
            """, (eid, archetype))
            prop_inserted += cur.rowcount

            # --- entry_properties: dimensional_sensitivity ---
            cur.execute("""
                INSERT OR IGNORE INTO entry_properties
                  (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?, 'DS Facets', 'dimensional_sensitivity', ?, 2)
            """, (eid, d_label))
            prop_inserted += cur.rowcount

            # --- section: Mathematical Archetype ---
            # Get max section_order for this entry
            max_ord = cur.execute(
                "SELECT MAX(section_order) FROM sections WHERE entry_id=?", (eid,)
            ).fetchone()[0] or 0

            cur.execute("""
                INSERT OR IGNORE INTO sections
                  (entry_id, section_name, section_order, content)
                VALUES (?, 'Mathematical Archetype', ?, ?)
            """, (eid, max_ord + 1, section_text))
            sec_inserted += cur.rowcount

            if not dry_run and cur.rowcount:
                pass  # silent on success for brevity

        except Exception as e:
            errors.append((eid, str(e)))

    if not dry_run:
        conn.commit()

    # Summary
    total = len(entries)
    print(f"\n{'DRY RUN — ' if dry_run else ''}Phase 1 taxonomy expansion complete")
    print(f"  Entries processed : {total}")
    print(f"  Property rows     : {prop_inserted} {'(would insert)' if dry_run else 'inserted'}")
    print(f"  Section rows      : {sec_inserted} {'(would insert)' if dry_run else 'inserted'}")
    if errors:
        print(f"\n  ERRORS ({len(errors)}):")
        for eid, msg in errors:
            print(f"    {eid}: {msg}")
    else:
        print(f"  Errors            : 0")

    conn.close()
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    import argparse
    args = parser.parse_args()

    print(f"DB: {SOURCE_DB}")
    print(f"Entries to process: {len(ENTRY_DATA)}")
    print(f"Archetypes defined: {len(ARCHETYPES)}")

    errs = run(str(SOURCE_DB), ENTRY_DATA, dry_run=args.dry_run)
    sys.exit(1 if errs else 0)

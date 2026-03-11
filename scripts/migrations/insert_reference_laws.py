"""
insert_reference_laws.py
Batch-inserts ~97 reference_law entries into ds_wiki.db.
entry_type = "reference_law" — canonical established science, distinct from DS-native entries.
Sections per entry: What It Claims · Mathematical Form · Constraint Category · DS Cross-References
Run: .venv/bin/python scripts/insert_reference_laws.py
"""

import sqlite3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import SOURCE_DB

# ---------------------------------------------------------------------------
# Data: (id, title, domain, scale, status, confidence, constraint, sections_dict)
# constraint: Th=Thermodynamic · Ge=Geometric · In=Informatic · Co=Coordination · Di=Dimensional
# sections_dict keys: "What It Claims", "Mathematical Form", "Constraint Category", "DS Cross-References"
# ---------------------------------------------------------------------------

ENTRIES = [

# ==========================================================================
# I. CLASSICAL MECHANICS  (CM1–CM8)
# ==========================================================================

("CM1", "Newton's Laws of Motion", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Three axioms governing the motion of bodies under forces. "
        "First: a body at rest or uniform motion remains so unless acted on by a net force (inertia). "
        "Second: net force equals rate of change of momentum, F = dp/dt, reducing to F = ma for constant mass. "
        "Third: every action has an equal and opposite reaction. "
        "Together they define classical mechanics and are exact within non-relativistic, non-quantum regimes."
    ),
    "Mathematical Form": (
        "F = 0 ⟹ v = const (1st) | F = ma (2nd) | F₁₂ = −F₂₁ (3rd). "
        "In the Lagrangian formulation these derive from the Euler–Lagrange equations applied to the kinetic Lagrangian L = T − V."
    ),
    "Constraint Category": (
        "Geometric (Ge): the laws encode motion through Euclidean D=3 space. "
        "In D_eff ≠ 3, the geometric structure of force and inertia changes — the inverse-square gravitation law is the clearest signature."
    ),
    "DS Cross-References": (
        "Foundation for A1 (Square-Cube Law — scaling in D=3 space). "
        "F = G m₁m₂ / r² is a D=3 Gauss-law consequence; Ω_D acts on G and changes the exponent. "
        "Connects to AM1 (Least Action) as its variational parent."
    ),
}),

("CM2", "Newton's Law of Universal Gravitation", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Every pair of masses attracts with a force proportional to the product of their masses and inversely proportional to the square of their separation: F = G m₁m₂ / r². "
        "The inverse-square dependence is a geometric consequence of flux spreading over a sphere in D=3 space. "
        "It is the non-relativistic limit of general relativity and breaks down at strong-field or high-velocity scales."
    ),
    "Mathematical Form": "F = G m₁m₂ / r²  |  G ≈ 6.674×10⁻¹¹ N·m²·kg⁻²",
    "Constraint Category": (
        "Geometric (Ge): the r⁻² dependence is a D=3 Gauss-law consequence. "
        "In D spatial dimensions, gravitational force scales as r^(1−D). "
        "Ω_D predicts G is not fixed but runs with D_eff."
    ),
    "DS Cross-References": (
        "Ω_D (G as a running constant). G1 (Dimensional Redshift — alternative to ΛCDM built on changing D_eff). "
        "CM5 (Kepler's 3rd law derives from this). Coulomb's law (EM5) has identical geometric structure."
    ),
}),

("CM3", "Kepler's First Law — Elliptical Orbits", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Planets orbit the Sun in ellipses with the Sun at one focus. "
        "This follows from the inverse-square gravitational force: the only closed orbits under an inverse-square central force are conics (ellipses, parabolas, hyperbolas). "
        "The shape encodes the energy and angular momentum of the orbit."
    ),
    "Mathematical Form": "r = ℓ / (1 + e·cosθ)  where ℓ = semi-latus rectum, e = eccentricity",
    "Constraint Category": "Geometric (Ge): conic sections are the geometric consequence of inverse-square force in D=3.",
    "DS Cross-References": "Derives from CM2 (gravitation). Connects to CM5 (Kepler's 3rd) and AM1 (least action).",
}),

("CM4", "Kepler's Second Law — Equal Areas", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A line joining a planet to the Sun sweeps out equal areas in equal times. "
        "This is a direct consequence of conservation of angular momentum: the areal velocity dA/dt = |L|/2m is constant whenever no torque acts. "
        "It is therefore a special case of Noether's theorem applied to rotational symmetry."
    ),
    "Mathematical Form": "dA/dt = |L| / 2m = const  (L = angular momentum)",
    "Constraint Category": "Geometric (Ge): rotational symmetry → conserved angular momentum → areal velocity constant.",
    "DS Cross-References": "AM5 (Noether's theorem) is the parent: rotational symmetry → angular momentum. Connects to CM2 and CM5.",
}),

("CM5", "Kepler's Third Law — Orbital Period Scaling", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The square of a planet's orbital period is proportional to the cube of its semi-major axis: T² ∝ a³. "
        "The exponent 3/2 is a power law whose base comes directly from the r⁻² force law in D=3 space. "
        "It is structurally analogous to metabolic scaling (C1): both are power laws whose exponents encode the effective dimensionality of the underlying potential or network."
    ),
    "Mathematical Form": "T² = (4π²/G(m+M)) · a³",
    "Constraint Category": "Geometric (Ge): exponent 3/2 = D_eff / 2 for D=3. Changes if gravitational potential dimension changes.",
    "DS Cross-References": (
        "Analogue of C1 (metabolic scaling): both are power laws with dimension-encoding exponents. "
        "CM2 (gravitation — parent law). Ω_D (G runs with D_eff, changing the proportionality constant)."
    ),
}),

("CM6", "Euler's Laws of Motion (Rigid Body)", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Extension of Newton's laws to rigid bodies: net force equals rate of change of linear momentum of the center of mass; "
        "net torque about the center of mass equals rate of change of angular momentum. "
        "Together they fully describe the translational and rotational motion of any rigid body."
    ),
    "Mathematical Form": "F = dp/dt  |  τ = dL/dt  (for rigid body about center of mass)",
    "Constraint Category": "Geometric (Ge): rotation and translation are geometric degrees of freedom in D=3.",
    "DS Cross-References": "Derives from CM1 (Newton). Connects to AM2 (Euler–Lagrange) for the variational formulation.",
}),

("CM7", "Archimedes' Principle", "physics", "organismal", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A body immersed in a fluid experiences an upward buoyant force equal to the weight of the fluid it displaces. "
        "The principle follows from the pressure gradient in a gravitational field integrated over the body's volume. "
        "It is a consequence of the geometric relationship between volume displacement and pressure in D=3."
    ),
    "Mathematical Form": "F_buoy = ρ_fluid · g · V_displaced",
    "Constraint Category": "Geometric/Thermodynamic (Ge/Th): volume–pressure geometry under gravity.",
    "DS Cross-References": "A1 (Square-Cube Law): buoyancy force scales with volume while weight scales with mass; intersection sets size limits. FM3 (Bernoulli) is the flow analog.",
}),

("CM8", "Lorentz Force Law", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A charged particle moving in electromagnetic fields experiences a force F = q(E + v × B). "
        "The electric part is radial (Coulomb-like); the magnetic part is velocity-dependent and perpendicular to motion. "
        "The law couples particle mechanics to Maxwell's field equations, forming the complete classical electrodynamics system."
    ),
    "Mathematical Form": "F = q(E + v × B)",
    "Constraint Category": "Geometric (Ge): the cross-product structure is specific to D=3 geometry (no natural cross-product in other dimensions).",
    "DS Cross-References": "Couples to Maxwell's equations (EM1–EM5). Ω_D: if c changes with D_eff, E and B field strengths re-couple.",
}),

# ==========================================================================
# II. ANALYTICAL MECHANICS & VARIATIONAL PRINCIPLES  (AM1–AM5)
# ==========================================================================

("AM1", "Principle of Least Action", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The actual path taken by a physical system between two states is the one for which the action S = ∫L dt is stationary (usually minimal). "
        "The Lagrangian L = T − V encodes kinetic minus potential energy. "
        "This single variational principle generates all of classical mechanics, electrodynamics, general relativity, and — via path integrals — quantum mechanics. "
        "It is the most compressed statement of the laws of physics."
    ),
    "Mathematical Form": "δS = δ∫L dt = 0  ⟹  Euler–Lagrange equations",
    "Constraint Category": (
        "Geometric (Ge): action is a geometric quantity — it is path-length in configuration space weighted by dynamics. "
        "Least action is the geodesic principle of mechanics."
    ),
    "DS Cross-References": (
        "Parent of AM2 (Euler–Lagrange), AM3 (Hamilton), AM4 (Hamilton–Jacobi). "
        "OP1 (Fermat's principle) is the optical analog. "
        "H5 (scaling exponent β) can be derived variationally: the exponent that extremizes information flow."
    ),
}),

("AM2", "Euler–Lagrange Equations", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The equations of motion derived from the action principle for a system with generalized coordinates q_i. "
        "They state: d/dt(∂L/∂q̇_i) = ∂L/∂q_i. "
        "Every classical field theory — mechanics, electrodynamics, general relativity — is summarized by specifying a Lagrangian and applying these equations."
    ),
    "Mathematical Form": "d/dt(∂L/∂q̇ᵢ) = ∂L/∂qᵢ  for each generalized coordinate qᵢ",
    "Constraint Category": "Geometric (Ge): equations live in configuration space; geometry of L determines equations of motion.",
    "DS Cross-References": "Derived from AM1 (least action). Connects to M4 (Mori–Zwanzig): projection onto slow variables is a Lagrangian reduction.",
}),

("AM3", "Hamilton's Equations", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A symplectic reformulation of mechanics using generalized coordinates q and momenta p. "
        "The Hamiltonian H (total energy) generates time evolution: ṗ = −∂H/∂q, q̇ = ∂H/∂p. "
        "Phase-space (q, p) has a natural geometric structure (symplectic form) preserved by Hamiltonian flow, making it the natural home of statistical mechanics and quantum mechanics."
    ),
    "Mathematical Form": "∂p/∂t = −∂H/∂q  |  ∂q/∂t = ∂H/∂p",
    "Constraint Category": "Geometric (Ge): symplectic geometry of phase space; Liouville's theorem (volume preserved) is a Ge constraint.",
    "DS Cross-References": "Derived from AM1. Parent of AM4 (Hamilton–Jacobi). Phase-space geometry connects to Fisher information (M6): Fisher metric is the symplectic metric on statistical manifolds.",
}),

("AM4", "Hamilton–Jacobi Equation", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A first-order PDE for the action function S(q, t): H(q, ∂S/∂q, t) = −∂S/∂t. "
        "Its solutions give classical trajectories as characteristics. "
        "In the limit ℏ → 0, the Schrödinger equation reduces to the Hamilton–Jacobi equation, making it the classical–quantum bridge."
    ),
    "Mathematical Form": "H(q, ∂S/∂q, t) = −∂S/∂t",
    "Constraint Category": "Geometric/Dimensional (Ge/Di): the ℏ → 0 limit bridges classical geometry and quantum wave mechanics.",
    "DS Cross-References": "Bridge to QM1 (Schrödinger equation). AM1 (least action) parent. Ω_D: if ℏ runs with D_eff, the classical–quantum boundary shifts.",
}),

("AM5", "Noether's Theorem", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Every continuous symmetry of the action corresponds to a conserved quantity. "
        "Time-translation symmetry → energy conservation. Spatial-translation symmetry → momentum conservation. "
        "Rotational symmetry → angular momentum conservation. Gauge symmetry → charge conservation. "
        "This theorem is the deepest explanation of why conservation laws exist — they are not independent axioms but consequences of geometric symmetry."
    ),
    "Mathematical Form": "Continuous symmetry of S ⟺ conserved Noether current J^μ with ∂_μ J^μ = 0",
    "Constraint Category": (
        "Geometric (Ge): symmetry is a geometric property of the action; the theorem maps symmetry groups to conservation laws. "
        "It is the backbone behind all conservation laws in the taxonomy."
    ),
    "DS Cross-References": (
        "Parent of: conservation of energy (TD2), momentum (CM1), angular momentum (CM4), charge (EM4). "
        "Ω_D: if physical constants run with D_eff, the time-translation symmetry is broken → energy may not be globally conserved across scales. "
        "This is the deepest tension in the DS framework's running-constants conjecture."
    ),
}),

# ==========================================================================
# III. THERMODYNAMICS & STATISTICAL MECHANICS  (TD1–TD13)
# ==========================================================================

("TD1", "Zeroth Law of Thermodynamics", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "If system A is in thermal equilibrium with system B, and system B with system C, then A is in equilibrium with C. "
        "This transitivity defines temperature as an equivalence class of thermal states — it is what makes thermometry possible. "
        "It is logically prior to the other laws but was named last."
    ),
    "Mathematical Form": "T_A = T_B ∧ T_B = T_C ⟹ T_A = T_C",
    "Constraint Category": "Thermodynamic (Th): defines the equilibrium condition that all other thermodynamic laws presuppose.",
    "DS Cross-References": "Foundation for TD3 (2nd law, which requires thermal equilibrium as a reference). Connects to TD6 (Onsager relations near equilibrium).",
}),

("TD2", "First Law of Thermodynamics", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "Energy is conserved: the change in internal energy of a system equals heat absorbed minus work done by the system, dU = δQ − δW. "
        "No process can create or destroy energy, only convert between forms. "
        "This is Noether's theorem applied to time-translation symmetry — the universe has no preferred moment, so energy is conserved."
    ),
    "Mathematical Form": "dU = δQ − δW  (closed system)  |  dU = δQ − δW + Σ μᵢ dNᵢ  (open system)",
    "Constraint Category": "Thermodynamic (Th): hard ceiling on all energy exchange processes. No perpetual motion machine of the first kind.",
    "DS Cross-References": "AM5 (Noether) is the parent via time symmetry. B5 (Landauer): erasing a bit dissipates k_BT ln2 — a first-law consequence for information. TD3 (2nd law) adds directionality to this.",
}),

("TD3", "Second Law of Thermodynamics", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The total entropy of an isolated system never decreases: ΔS ≥ 0. "
        "Entropy S measures the number of microstates consistent with a macrostate (Boltzmann: S = k_B ln Ω). "
        "The second law is the master thermodynamic constraint: it defines the arrow of time, sets the limit on engine efficiency (Carnot), "
        "and — in its information-theoretic reading — sets the cost of erasing information (Landauer). "
        "It applies at every scale from molecular collisions to cosmological structure formation."
    ),
    "Mathematical Form": "ΔS ≥ 0  (isolated system)  |  S = k_B ln Ω  (Boltzmann form)  |  dS = δQ_rev / T",
    "Constraint Category": (
        "Thermodynamic/Informatic (Th/In): entropy is simultaneously a thermodynamic state function and a measure of missing information. "
        "The second law constrains both heat engines and information processors."
    ),
    "DS Cross-References": (
        "Grounds B5 (Landauer: erasing information costs entropy). "
        "F1 (Ashby: regulatory variety has an entropy cost). "
        "Ax1 (information primacy: information loss = physical irreversibility). "
        "TD8 (Carnot: efficiency ceiling follows directly). "
        "The DS framework's vector history topology is an application of entropy growth: the semantic manifold drifts irreversibly."
    ),
}),

("TD4", "Third Law of Thermodynamics", "physics", "quantum", "established", "Tier 1", "Th", {
    "What It Claims": (
        "As temperature approaches absolute zero, the entropy of a perfect crystal approaches a constant minimum (zero for a non-degenerate ground state). "
        "This implies absolute zero is unreachable in a finite number of steps. "
        "The third law fixes the absolute reference point of the entropy scale and governs the behavior of all thermal properties near T = 0."
    ),
    "Mathematical Form": "S → 0 as T → 0  (for a perfect crystal with unique ground state)",
    "Constraint Category": "Thermodynamic (Th): lower bound on entropy at finite temperature; makes absolute-zero a geometric asymptote.",
    "DS Cross-References": "Connects to QM2 (Heisenberg uncertainty) — at T=0 quantum fluctuations dominate. TD3 (2nd law) is the parent constraint.",
}),

("TD5", "Fundamental Thermodynamic Relation", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The master equation linking all thermodynamic state variables: dU = TdS − PdV + Σ μᵢ dNᵢ. "
        "It combines the first and second laws with chemical potential, giving the complete differential of internal energy. "
        "All other thermodynamic relations (Maxwell relations, Gibbs-Helmholtz, etc.) are derived from this by Legendre transformations."
    ),
    "Mathematical Form": "dU = TdS − PdV + Σ μᵢ dNᵢ",
    "Constraint Category": "Thermodynamic (Th): master differential constraint on all equilibrium thermodynamic systems.",
    "DS Cross-References": "Parent of KC6 (Gibbs-Helmholtz). TD2 (1st law) and TD3 (2nd law) are embedded. Connects to AM3 (Hamilton): thermodynamic potentials are Legendre transforms, like Hamiltonians.",
}),

("TD6", "Onsager Reciprocal Relations", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "Near thermodynamic equilibrium, the cross-coupling coefficients in linear response theory are symmetric: L_ij = L_ji. "
        "This means that if force X_i drives flux J_j, then the same force scale X_j drives flux J_i equally. "
        "The relations follow from microscopic time-reversal symmetry (detailed balance) and are the foundation of non-equilibrium thermodynamics."
    ),
    "Mathematical Form": "Jᵢ = Σⱼ Lᵢⱼ Xⱼ  |  Lᵢⱼ = Lⱼᵢ  (near equilibrium)",
    "Constraint Category": "Thermodynamic (Th): symmetry of linear response near equilibrium; consequence of microscopic reversibility.",
    "DS Cross-References": "TD3 (2nd law) is the parent: Onsager relations are the linear-response limit of entropy production. Connects to M4 (Mori–Zwanzig): projection onto slow variables yields Onsager-like linear equations.",
}),

("TD7", "Boltzmann Equation", "physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "Describes the statistical evolution of a gas's phase-space distribution function f(r, p, t) due to streaming and collisions: ∂f/∂t + p/m · ∇f + F · ∂f/∂p = (∂f/∂t)_coll. "
        "The H-theorem (Boltzmann) shows this implies entropy increases: the bridge from microscopic reversibility to macroscopic irreversibility. "
        "All of hydrodynamics (Navier-Stokes) and kinetic theory derive from its moments."
    ),
    "Mathematical Form": "∂f/∂t + (p/m)·∇f + F·(∂f/∂p) = C[f]  (C = collision operator)",
    "Constraint Category": "Thermodynamic/Informatic (Th/In): the H-theorem is an entropy-production statement; f is a probability distribution — information about particle positions.",
    "DS Cross-References": "Bridge to FM1 (Navier-Stokes: derived as 2nd moment). M4 (Mori–Zwanzig) is a modern generalization of this projection from micro to macro. TD3 (2nd law) is the macroscopic limit.",
}),

("TD8", "Carnot's Theorem", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "No heat engine operating between two thermal reservoirs at temperatures T_hot and T_cold can be more efficient than a Carnot engine: η ≤ 1 − T_cold/T_hot. "
        "The Carnot engine is reversible and achieves this maximum efficiency. "
        "The theorem is a direct consequence of the second law and establishes the thermodynamic ceiling on all energy conversion."
    ),
    "Mathematical Form": "η_max = 1 − T_cold / T_hot  (Carnot efficiency)",
    "Constraint Category": "Thermodynamic (Th): hard upper bound on efficiency — a ceiling constraint analogous to F1 (Ashby) for energy systems.",
    "DS Cross-References": (
        "Derived from TD3 (2nd law). "
        "Structural analog to F1 (Ashby's law): both are hard informatic/thermodynamic ceilings. "
        "E2 (Koomey's law) is approaching B5 (Landauer floor) — Carnot is the thermal analog of this approach to a physical limit."
    ),
}),

("TD9", "Newton's Law of Cooling", "physics", "organismal", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The rate of heat loss from a body is proportional to the temperature difference between the body and its environment: dT/dt = −k(T − T_env). "
        "This gives exponential cooling — the same mathematical structure as radioactive decay (B1) and Arrhenius kinetics (B2). "
        "It is a linear approximation valid for small temperature differences."
    ),
    "Mathematical Form": "dT/dt = −k(T − T_env)  ⟹  T(t) = T_env + (T₀ − T_env)e^(−kt)",
    "Constraint Category": "Thermodynamic (Th): dissipative equilibration; the exponential decay is a Th relaxation signature.",
    "DS Cross-References": "Same exponential relaxation structure as B1 (radioactive decay), B2 (Arrhenius). TD10 (Fourier's law) is the field-theoretic version of this.",
}),

("TD10", "Fourier's Law of Heat Conduction", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "Heat flux is proportional to the negative temperature gradient: q = −k∇T. "
        "Heat flows from hot to cold, with magnitude proportional to how steep the temperature gradient is. "
        "Combined with energy conservation, it yields the heat equation ∂T/∂t = α∇²T — the prototype of all diffusion equations."
    ),
    "Mathematical Form": "q = −k∇T  |  Heat equation: ∂T/∂t = α∇²T  (α = thermal diffusivity)",
    "Constraint Category": "Thermodynamic (Th): diffusive transport driven by gradient; same mathematical form as Fick's diffusion (DM1).",
    "DS Cross-References": "Structural pair with DM1 (Fick's laws of diffusion): same ∇-proportional flux form, different conserved quantity. Connects to FM1 (Navier-Stokes) for momentum transport. TD3 (2nd law) is the thermodynamic parent.",
}),

("TD11", "Kopp's Law", "chemistry", "molecular", "established", "Tier 2", "Th", {
    "What It Claims": (
        "The molar heat capacity of a solid compound is approximately the sum of the atomic heat capacities of its constituent elements. "
        "It is an empirical rule that holds reasonably at room temperature but breaks down at low temperatures (quantum effects) and high temperatures. "
        "A coarse-grained additivity principle for thermal storage."
    ),
    "Mathematical Form": "C_compound ≈ Σ C_element (molar contributions)",
    "Constraint Category": "Thermodynamic (Th): approximate additivity of thermal degrees of freedom.",
    "DS Cross-References": "Approximate version of TD12 (Dulong-Petit). Connects to the idea that effective degrees of freedom (D_eff) are additive within a regime.",
}),

("TD12", "Dulong–Petit Law", "physics · chemistry", "molecular", "established", "Tier 2", "Th", {
    "What It Claims": (
        "At sufficiently high temperatures, the molar heat capacity of a monatomic crystal approaches 3R ≈ 24.9 J/(mol·K), where R is the gas constant. "
        "Each atom has 3 kinetic and 3 potential degrees of freedom, each contributing k_B/2 (equipartition). "
        "This law fails at low temperatures where quantum effects freeze out degrees of freedom — a breakdown that historically prompted quantum mechanics."
    ),
    "Mathematical Form": "C_V → 3R  as T → ∞  (classical equipartition limit)",
    "Constraint Category": "Thermodynamic (Th): equipartition assigns k_BT/2 per classical degree of freedom — a Th ceiling approached from below.",
    "DS Cross-References": "Failure of Dulong-Petit at low T was one of the first signs of quantization — connects to QM1 (Schrödinger), QM2 (Heisenberg). Ax2 (effective dimensionality): the number of active degrees of freedom is D_eff, not fixed.",
}),

("TD13", "Carnot Efficiency and Thermodynamic Temperature", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The thermodynamic (Kelvin) temperature scale is defined operationally through Carnot cycle efficiency: T_cold/T_hot = Q_cold/Q_hot for a reversible cycle. "
        "This makes temperature a fundamental ratio, independent of any working substance. "
        "It is the absolute definition of temperature that underpins all of thermodynamics."
    ),
    "Mathematical Form": "T_cold / T_hot = Q_cold / Q_hot  (for reversible Carnot cycle)",
    "Constraint Category": "Thermodynamic (Th): the absolute temperature scale defined operationally through reversible heat ratios.",
    "DS Cross-References": "Foundation for TD3 (2nd law expressed in terms of absolute T). TD8 (Carnot's theorem) uses this. TD1 (Zeroth law) defines equivalence classes that this quantifies.",
}),

# ==========================================================================
# IV. ELECTROMAGNETISM — MAXWELL'S EQUATIONS  (EM1–EM5) + OTHERS (EM6–EM11)
# ==========================================================================

("EM1", "Gauss's Law for Electricity", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The electric flux through any closed surface equals the enclosed charge divided by permittivity: ∮E·dA = Q_enc/ε₀, or in differential form ∇·E = ρ/ε₀. "
        "It is the electric field analog of Newton's gravitation in D=3: charge spreads flux over a sphere, giving inverse-square field decay. "
        "One of Maxwell's four equations."
    ),
    "Mathematical Form": "∇·E = ρ/ε₀  (differential)  |  ∮E·dA = Q_enc/ε₀  (integral)",
    "Constraint Category": "Geometric (Ge): D=3 Gauss theorem; flux through a sphere scales as r² → E ~ r⁻². In D dimensions: E ~ r^(1−D).",
    "DS Cross-References": "Same geometric structure as CM2 (gravitation). Ω_D: ε₀ runs with D_eff through c = 1/√(ε₀μ₀). Part of unified Maxwell system (EM1–EM5).",
}),

("EM2", "Gauss's Law for Magnetism", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The magnetic flux through any closed surface is zero: ∇·B = 0. "
        "This is a topological statement: there are no magnetic monopoles; magnetic field lines always close on themselves. "
        "The constraint is exact and has never been violated experimentally."
    ),
    "Mathematical Form": "∇·B = 0",
    "Constraint Category": "Geometric (Ge): topological constraint on field topology — no sources or sinks of B field.",
    "DS Cross-References": "Part of Maxwell system. The topological character (no monopoles) connects to H4 (topological obstruction χ_eff). Q2 (Poincaré-Hopf via spectral triples) explores similar topological constraints.",
}),

("EM3", "Faraday's Law of Induction", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A changing magnetic field induces a curling electric field: ∇×E = −∂B/∂t. "
        "The induced EMF in a loop equals the negative rate of change of magnetic flux through the loop (Faraday's law of induction). "
        "Lenz's law (EM8) specifies that the induced current opposes the change — an electromagnetic Le Chatelier principle."
    ),
    "Mathematical Form": "∇×E = −∂B/∂t  |  EMF = −dΦ_B/dt",
    "Constraint Category": "Geometric (Ge): curl of E field driven by time-varying B — a geometric coupling between field components.",
    "DS Cross-References": "Part of Maxwell system. EM8 (Lenz's law) is the consequence. Together with AM5 (Noether), gauge symmetry of electrodynamics → charge conservation.",
}),

("EM4", "Ampère–Maxwell Law", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A magnetic field is produced both by electric currents and by changing electric fields (displacement current): ∇×B = μ₀J + (μ₀ε₀)∂E/∂t. "
        "Maxwell's addition of the displacement current term was the theoretical prediction of electromagnetic waves. "
        "Together the four Maxwell equations give c = 1/√(ε₀μ₀), unifying electricity, magnetism, and light."
    ),
    "Mathematical Form": "∇×B = μ₀J + (1/c²)∂E/∂t  |  c = 1/√(ε₀μ₀)",
    "Constraint Category": "Geometric (Ge): coupling between spatial curl of B and temporal change of E — the source of electromagnetic wave propagation.",
    "DS Cross-References": "Part of Maxwell system. Ω_D: c = 1/√(ε₀μ₀) — if ε₀ and μ₀ run with D_eff, c runs. GV1 (General Relativity) and G1 (Dimensional Redshift) both depend on c being fixed.",
}),

("EM5", "Continuity Equation (Charge Conservation)", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Charge is locally conserved: the rate of decrease of charge in any volume equals the outward flux of current density. "
        "∂ρ/∂t = −∇·J. "
        "This follows from Maxwell's equations and is equivalent to the gauge symmetry of electrodynamics — a Noether consequence (AM5). "
        "The same mathematical form applies to mass, energy, probability, and particle number in appropriate contexts."
    ),
    "Mathematical Form": "∂ρ/∂t + ∇·J = 0",
    "Constraint Category": "Geometric/Thermodynamic (Ge/Th): conservation law; same form applies universally to any conserved density.",
    "DS Cross-References": "AM5 (Noether): gauge symmetry → charge conservation. The same PDE structure governs TD10 (Fourier), DM1 (Fick's), FM1 (Navier-Stokes). Universal conservation form.",
}),

("EM6", "Coulomb's Law", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Two point charges exert forces on each other proportional to the product of their charges and inversely proportional to the square of their separation: F = kq₁q₂/r². "
        "This is the electrostatic limit of Maxwell's equations in D=3, with exactly the same geometric structure as Newton's gravitation. "
        "The r⁻² dependence signals D=3 geometry — in D dimensions, the exponent is D−1."
    ),
    "Mathematical Form": "F = k q₁q₂/r²  |  k = 1/(4πε₀) ≈ 8.99×10⁹ N·m²·C⁻²",
    "Constraint Category": "Geometric (Ge): inverse-square from D=3 Gauss theorem. Identical structure to Newton's gravitation (CM2).",
    "DS Cross-References": "CM2 (gravitation): identical inverse-square structure — both are D=3 Gauss-law consequences. Ω_D acts on ε₀ → k runs with D_eff. EM1 (Gauss's law) is the field formulation.",
}),

("EM7", "Biot–Savart Law", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The magnetic field at a point due to a current element Idl is dB = (μ₀/4π) · I(dl × r̂)/r². "
        "It is the magnetostatic analog of Coulomb's law — the magnetic field produced by a steady current distribution. "
        "The cross-product structure is specific to D=3 geometry."
    ),
    "Mathematical Form": "dB = (μ₀/4π) · I(dl × r̂) / r²",
    "Constraint Category": "Geometric (Ge): cross-product and inverse-square are both D=3 specific.",
    "DS Cross-References": "Static limit of EM4 (Ampère–Maxwell). Ω_D: μ₀ runs with D_eff through c = 1/√(ε₀μ₀).",
}),

("EM8", "Lenz's Law", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The direction of an induced current is always such that it opposes the change causing it. "
        "This is a specific application of EM3 (Faraday's law) that encodes a stability constraint: electromagnetic systems resist change in their flux state. "
        "It is the electromagnetic analog of Le Chatelier's principle in chemistry."
    ),
    "Mathematical Form": "Induced EMF = −dΦ/dt  (sign = opposition)",
    "Constraint Category": "Thermodynamic (Th): resistance to change — a stability constraint in electromagnetic systems.",
    "DS Cross-References": "Follows from EM3 (Faraday). Structural analog to KC1 (Le Chatelier's principle) — both describe system resistance to perturbation. F4 (Saturation Dynamics) generalizes this: all systems resist changes that push them past their operating regime.",
}),

("EM9", "Ohm's Law", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The voltage across a conductor is proportional to the current through it: V = IR, where R is resistance. "
        "Microscopically, resistance arises from scattering of charge carriers — it is a dissipative, irreversible process. "
        "Ohm's law is a linear approximation that holds in a vast range of materials but breaks down in semiconductors, superconductors, and nonlinear elements."
    ),
    "Mathematical Form": "V = IR  |  J = σE  (σ = conductivity, microscopic form)",
    "Constraint Category": "Thermodynamic (Th): linear dissipative response; power P = I²R is irreversibly dissipated as heat.",
    "DS Cross-References": "Linear transport law — same class as TD10 (Fourier), DM1 (Fick): flux ∝ driving force. TD6 (Onsager): Ohm's law is a special case of linear response theory.",
}),

("EM10", "Kirchhoff's Laws", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "Two rules for electrical circuits: (1) Current law (KCL): the sum of currents entering any node equals currents leaving — charge conservation. "
        "(2) Voltage law (KVL): the sum of voltages around any closed loop is zero — energy conservation. "
        "These are network-level expressions of the more fundamental EM5 (continuity) and TD2 (first law)."
    ),
    "Mathematical Form": "KCL: Σ Iᵢₙ = Σ Iₒᵤₜ  |  KVL: Σ Vᵢ = 0 (around loop)",
    "Constraint Category": "Thermodynamic/Geometric (Th/Ge): conservation at nodes (Th) and topological loop constraint (Ge — relates to network topology).",
    "DS Cross-References": "Network-level consequence of EM5 (charge conservation) and TD2 (energy conservation). The node topology connects to C2 (Urban Scaling) and network D_eff arguments.",
}),

("EM11", "Joule's Law", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The rate of heat dissipated in a resistor is P = I²R = V²/R. "
        "This is irreversible: electrical energy converts to thermal energy and cannot be recovered. "
        "Joule heating is the fundamental mechanism of electrical energy dissipation and the reason perfect conductors (superconductors) are so technologically significant."
    ),
    "Mathematical Form": "P = I²R = V²/R = VI",
    "Constraint Category": "Thermodynamic (Th): irreversible dissipation — entropy production at rate P/T.",
    "DS Cross-References": "Combines EM9 (Ohm's law) with TD3 (2nd law). B5 (Landauer): in the limit, even reversible computation produces Joule-like dissipation at k_BT ln2 per bit.",
}),

# ==========================================================================
# V. OPTICS  (OP1–OP6)
# ==========================================================================

("OP1", "Fermat's Principle of Least Time", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Light travels between two points along the path that takes the least time (or more precisely, the path of stationary optical path length). "
        "This variational principle generates all of geometric optics: reflection, refraction, and the laws of lens design. "
        "It is the optical analog of AM1 (principle of least action) — the same variational structure appears in mechanics, optics, and quantum mechanics."
    ),
    "Mathematical Form": "δ ∫ n(r) ds = 0  (n = refractive index, s = path length)",
    "Constraint Category": "Geometric (Ge): light path is the geodesic in a medium with spatially varying refractive index.",
    "DS Cross-References": "Exact structural analog of AM1 (least action). Generates OP2 (reflection) and OP3 (Snell's law) as special cases. The variational cluster: AM1 ↔ OP1 ↔ QM1 (Schrödinger via path integrals).",
}),

("OP2", "Law of Reflection", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "When light reflects from a surface, the angle of incidence equals the angle of reflection, both measured from the normal to the surface. "
        "This follows from Fermat's principle (OP1) at a flat interface and expresses the preservation of wave vector component parallel to the surface."
    ),
    "Mathematical Form": "θᵢ = θᵣ  (angles from surface normal)",
    "Constraint Category": "Geometric (Ge): symmetry of path length with respect to surface normal.",
    "DS Cross-References": "Derived from OP1 (Fermat's principle). Pairs with OP3 (Snell's law) — reflection is the limiting case of refraction.",
}),

("OP3", "Snell's Law of Refraction", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "When light crosses an interface between two media with refractive indices n₁ and n₂, the angles satisfy n₁ sin θ₁ = n₂ sin θ₂. "
        "The bending of light at interfaces is a consequence of the change in wave speed, and the law conserves the wave vector component parallel to the interface. "
        "Derived from OP1 (Fermat's principle)."
    ),
    "Mathematical Form": "n₁ sin θ₁ = n₂ sin θ₂",
    "Constraint Category": "Geometric (Ge): conservation of tangential wave vector at interface.",
    "DS Cross-References": "Derived from OP1. The refractive index n is analogous to D_eff: it governs how wave propagation changes across a boundary — just as dimensional transitions alter propagation in the DS framework.",
}),

("OP4", "Brewster's Angle", "physics", "cross-scale", "established", "Tier 2", "Ge", {
    "What It Claims": (
        "At Brewster's angle, reflected light is completely polarized with its electric field parallel to the surface. "
        "The condition is tan θ_B = n₂/n₁. At this angle, reflected and refracted rays are perpendicular. "
        "A geometric consequence of electromagnetic boundary conditions in D=3."
    ),
    "Mathematical Form": "tan θ_B = n₂/n₁",
    "Constraint Category": "Geometric (Ge): polarization state is a geometric property of the electromagnetic field.",
    "DS Cross-References": "Derived from OP3 (Snell) + Maxwell equations. A specific geometric constraint on wave-interface interaction.",
}),

("OP5", "Malus's Law", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "When polarized light passes through a polarizer, the transmitted intensity is I = I₀ cos²θ, where θ is the angle between the light's polarization direction and the polarizer axis. "
        "This is a projection law: only the component of the electric field vector aligned with the polarizer passes through. "
        "It is a direct geometric consequence of vector projection in D=3."
    ),
    "Mathematical Form": "I = I₀ cos²θ",
    "Constraint Category": "Geometric (Ge): intensity is the square of the projected amplitude — a Ge constraint on information throughput.",
    "DS Cross-References": "The cos²θ projection structure appears in quantum mechanics (Born rule, QM4) and information theory (projection loss in dimensional compression). Connects to Ax2 (D_eff as observer-dependent projection).",
}),

("OP6", "Beer–Lambert Law", "physics · chemistry", "molecular", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The intensity of light transmitted through an absorbing medium decays exponentially with path length: I = I₀ e^(−αℓ), where α is the absorption coefficient. "
        "Each infinitesimal layer absorbs a constant fraction — exponential decay is the signature of a memoryless, path-length-dependent geometric process. "
        "Same mathematical form as radioactive decay (B1) and Arrhenius kinetics (B2)."
    ),
    "Mathematical Form": "I = I₀ e^(−αℓ)  |  α = absorption coefficient × concentration (Beer's law)",
    "Constraint Category": "Geometric (Ge): absorption probability per unit path is constant — geometric dilution of surviving photons.",
    "DS Cross-References": "Same exponential decay structure as B1 (Gamow/radioactive decay) and B2 (Arrhenius). All three are instances of memoryless barrier-crossing: geometric path, thermal barrier, quantum barrier.",
}),

# ==========================================================================
# VI. RADIATION — NEW ENTRIES  (RD1–RD3; B1, B3, B4 already exist)
# ==========================================================================

("RD1", "Planck's Law of Black-Body Radiation", "physics", "quantum", "established", "Tier 1", "Th", {
    "What It Claims": (
        "A black body in thermal equilibrium at temperature T emits radiation with a spectral energy density: "
        "u(ν, T) = (8πhν³/c³) / (e^(hν/kT) − 1). "
        "This law resolved the ultraviolet catastrophe of classical physics and was the birth of quantum mechanics. "
        "It is the parent law from which Wien's displacement law (B3) and Stefan-Boltzmann (RD2) are derived as limits. "
        "The radiation density is dimension-sensitive: in D spatial dimensions the exponent of ν becomes D (not 3), and the Stefan-Boltzmann exponent becomes D+1."
    ),
    "Mathematical Form": "u(ν,T) = (8πhν³/c³) · 1/(e^(hν/k_BT) − 1)",
    "Constraint Category": "Thermodynamic/Dimensional (Th/Di): dimension-sensitive — radiation density scales with D; the Planck constant h is the quantum of action that Ω_D acts on.",
    "DS Cross-References": "Parent of B3 (Wien's law) and RD2 (Stefan-Boltzmann). Ω_D acts on h and c directly — this is one of the most sensitive tests of running constants. Connects to RD3 (Planck-Einstein), QM1 (Schrödinger).",
}),

("RD2", "Stefan–Boltzmann Law", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The total power radiated per unit area by a black body is proportional to the fourth power of its temperature: P/A = σ T⁴. "
        "The exponent 4 = D + 1 for D = 3 spatial dimensions — it is a direct signature of geometry. "
        "In D spatial dimensions, this becomes P/A ∝ T^(D+1). "
        "Stefan-Boltzmann is obtained by integrating Planck's law (RD1) over all frequencies."
    ),
    "Mathematical Form": "P/A = σT⁴  |  σ = 2π⁵k_B⁴/(15h³c²) ≈ 5.67×10⁻⁸ W·m⁻²·K⁻⁴",
    "Constraint Category": "Thermodynamic/Dimensional (Th/Di): the T⁴ exponent encodes D=3 — a direct dimension-sensitive scaling law.",
    "DS Cross-References": "Derived from RD1 (Planck). The exponent 4 = D+1 makes this structurally analogous to C1 (Kleiber: exponent encodes D_eff of vascular network). Ω_D: both h and c enter σ — running constants shift the Stefan-Boltzmann constant.",
}),

("RD3", "Planck–Einstein Relation", "physics", "quantum", "established", "Tier 1", "Di", {
    "What It Claims": (
        "The energy of a photon is proportional to its frequency: E = hν = ℏω. "
        "This was Einstein's 1905 explanation of the photoelectric effect — light comes in discrete quanta of energy. "
        "The Planck constant h is the proportionality between energy (Th domain) and frequency (Ge domain), making it the bridge between thermodynamic and dimensional scales. "
        "Ω_D acts on h directly — if h runs with D_eff, all quantum energy scales shift."
    ),
    "Mathematical Form": "E = hν = ℏω  |  h ≈ 6.626×10⁻³⁴ J·s",
    "Constraint Category": "Dimensional (Di): h is the quantum of action; it sets the scale at which quantum discretization becomes relevant relative to classical continuum.",
    "DS Cross-References": "Ω_D acts on h — central to running-constants conjecture. B3 (Wien), B1 (Gamow tunneling), QM1 (Schrödinger), QM2 (Heisenberg) all involve h. B5 (Landauer) involves k_B — the thermal partner of h.",
}),

# ==========================================================================
# VII. QUANTUM MECHANICS  (QM1–QM5)
# ==========================================================================

("QM1", "Schrödinger Equation", "physics", "quantum", "established", "Tier 1", "Di", {
    "What It Claims": (
        "The quantum state |ψ⟩ of a non-relativistic system evolves unitarily according to iℏ d|ψ⟩/dt = Ĥ|ψ⟩. "
        "The Hamiltonian Ĥ generates time evolution; the wavefunction encodes all probabilistic information about the system. "
        "This is the quantum analog of Hamilton's equations (AM3): Ĥ plays the role of the classical Hamiltonian. "
        "The DS framework conjectures ℏ runs with D_eff — if true, quantum evolution itself becomes scale-dependent."
    ),
    "Mathematical Form": "iℏ ∂ψ/∂t = Ĥψ  (time-dependent)  |  Ĥψ = Eψ  (time-independent)",
    "Constraint Category": "Dimensional (Di): ℏ is the quantum of action; D_eff governs how much of phase space is accessible at each resolution scale.",
    "DS Cross-References": "Ω_D acts on ℏ — running ℏ shifts tunneling rates (B1), spectral positions (B3), energy discretization (RD3). AM4 (Hamilton-Jacobi) reduces to Schrödinger in the quantum limit. G3 (holographic complexity): solving Schrödinger in high-D Hilbert space is the computational bottleneck.",
}),

("QM2", "Heisenberg Uncertainty Principle", "physics", "quantum", "established", "Tier 1", "In", {
    "What It Claims": (
        "Position and momentum cannot be simultaneously known to arbitrary precision: ΔxΔp ≥ ℏ/2. "
        "Similarly for energy-time: ΔEΔt ≥ ℏ/2. "
        "In the information-theoretic reading: the uncertainty principle is a constraint on how much information about position and momentum an observer can extract simultaneously — a dimensional constraint on measurement. "
        "The DS framework reads ℏ as encoding the projection grain from higher to lower D_eff: the minimum uncertainty is the irreducible loss from dimensional projection."
    ),
    "Mathematical Form": "ΔxΔp ≥ ℏ/2  |  ΔEΔt ≥ ℏ/2",
    "Constraint Category": "Informatic/Dimensional (In/Di): a fundamental informatic constraint — sets the minimum information grain at quantum scale. Directly involves ℏ which Ω_D modulates.",
    "DS Cross-References": "Ω_D on ℏ changes the uncertainty floor. Ax1 (information primacy): uncertainty is information-theoretic, not just physical. Ax2 (D_eff): the uncertainty at a given scale is the projection loss from higher-D phase space. Q5 (information cost of synchronization) is the many-body analog.",
}),

("QM3", "Pauli Exclusion Principle", "physics", "quantum", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "No two identical fermions can occupy the same quantum state simultaneously. "
        "Mathematically, the wavefunction of a multi-fermion system must be antisymmetric under particle exchange: ψ(...rᵢ...rⱼ...) = −ψ(...rⱼ...rᵢ...). "
        "This is not a force but a geometric constraint on Hilbert space — it is what makes matter solid, gives electrons their shell structure, and determines the periodic table."
    ),
    "Mathematical Form": "ψ(r₁,...,rᵢ,...,rⱼ,...) = −ψ(r₁,...,rⱼ,...,rᵢ,...) for fermions (spin s = half-integer)",
    "Constraint Category": "Geometric/Informatic (Ge/In): a topological constraint on the structure of Hilbert space for identical fermions. Sets the information capacity of quantum states.",
    "DS Cross-References": "Geometric constraint in Hilbert space — connects to H4 (topological obstruction χ_eff). F3 (Gause competitive exclusion) is the ecological analog: no two species can occupy the same niche = no two fermions in the same state.",
}),

("QM4", "de Broglie Wavelength", "physics", "quantum", "established", "Tier 1", "Di", {
    "What It Claims": (
        "Every particle with momentum p has an associated de Broglie wavelength λ = h/p. "
        "This wave-particle duality is the foundation of quantum mechanics — particles have wavelike properties whose scale is set by h. "
        "When λ becomes comparable to the scale of a system, quantum effects dominate over classical behavior."
    ),
    "Mathematical Form": "λ = h/p  |  p = ℏk  (k = wave vector)",
    "Constraint Category": "Dimensional (Di): the wavelength sets the scale boundary between quantum and classical regimes — a D_eff transition boundary.",
    "DS Cross-References": "Directly involves h, which Ω_D acts on. X4 (Quantum Systems instantiation) — de Broglie wavelength determines when quantum effects become important. QM1 (Schrödinger): this is the initial condition for the matter wave.",
}),

("QM5", "Postulates of Special Relativity", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Two postulates generate all of special relativity: (1) The laws of physics are identical in all inertial frames. "
        "(2) The speed of light c is the same in all inertial frames regardless of the motion of source or observer. "
        "These imply Lorentz transformations: time dilation, length contraction, and E = mc². "
        "The DS framework takes c as fixed at D_eff = 4 by construction of Ω_D; deviation at other D_eff values is an open conjecture."
    ),
    "Mathematical Form": "Lorentz transformation: A' = ΛA  |  E² = (pc)² + (mc²)²  |  γ = 1/√(1−v²/c²)",
    "Constraint Category": "Geometric (Ge): c-invariance is a geometric constraint on the structure of spacetime — Minkowski geometry.",
    "DS Cross-References": "Foundation for GV1 (General Relativity). Ω_D: c is set to be frame-invariant at D_eff=4 by construction. G1 (Dimensional Redshift): proposes that c is invariant but D_eff varies — energy attenuates, light slows cosmologically.",
}),

# ==========================================================================
# VIII. GRAVITATION & COSMOLOGY  (GV1–GV3)
# ==========================================================================

("GV1", "General Relativity — Einstein Field Equations", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Spacetime curvature (geometry) equals energy-momentum content: G_μν + Λg_μν = (8πG/c⁴)T_μν. "
        "Gravity is not a force but the curvature of spacetime caused by mass-energy. "
        "The cosmological constant Λ represents vacuum energy density. "
        "The DS framework proposes that Ω_D modifies the dimensional substrate that GR assumes to be fixed D=3+1: Λ may be a dimensional gradient effect rather than a vacuum energy."
    ),
    "Mathematical Form": "R_μν − (R/2)g_μν + Λg_μν = (8πG/c⁴)T_μν",
    "Constraint Category": "Geometric/Dimensional (Ge/Di): geometry = energy is a D=3+1 specific claim. Ω_D modifies both G and c entering the coupling constant.",
    "DS Cross-References": "G1 (Dimensional Redshift): alternative to ΛCDM built on Ω_D acting on D_eff. Ω_D: both G and c in the coupling factor 8πG/c⁴ are dimensional. G3 (Holographic Complexity Bound) derives from GR's holographic structure.",
}),

("GV2", "Gravitoelectromagnetism (GEM)", "physics · cosmology", "cosmological", "established", "Tier 2", "Ge", {
    "What It Claims": (
        "In the weak-field, slow-motion limit of general relativity, the gravitational field equations take on a Maxwell-like structure. "
        "A gravitoelectric field g and a gravitomagnetic field B_g obey equations analogous to Maxwell's. "
        "This reveals the deep structural correspondence between gravity and electromagnetism when both are viewed as geometric field theories in D=3+1."
    ),
    "Mathematical Form": "∇·g = −4πGρ  |  ∇×B_g = −(4G/c²)J  (in weak-field limit)",
    "Constraint Category": "Geometric (Ge): the Maxwell-like structure is a D=3+1 consequence; Ω_D acts on G.",
    "DS Cross-References": "Linearized limit of GV1 (GR). Shows structural identity with Maxwell equations (EM1-EM5). CM2 (Newton's gravitation) is the static, non-relativistic limit.",
}),

("GV3", "Gauss's Law for Gravity", "physics · cosmology", "cosmological", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The gravitational flux through any closed surface is proportional to the enclosed mass: ∇·g = −4πGρ. "
        "This is the Newtonian analog of Gauss's law for electricity — inverse-square gravity is a Gauss-law consequence in D=3. "
        "The Bekenstein bound (G3 in DS wiki) generalizes this to an entropy-area law, bounding information by geometric surface."
    ),
    "Mathematical Form": "∇·g = −4πGρ  (Newtonian form)  |  ∮g·dA = −4πGM_enc",
    "Constraint Category": "Geometric (Ge): inverse-square law from D=3 flux geometry.",
    "DS Cross-References": "CM2 (Newton's gravitation) is equivalent. Structural pair with EM1 (Gauss's law for electricity). G3 (Bekenstein bound) generalizes from mass to information.",
}),

# ==========================================================================
# IX. FLUID MECHANICS & TRANSPORT  (FM1–FM6)
# ==========================================================================

("FM1", "Navier–Stokes Equations", "physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The equations of motion for a viscous, incompressible fluid: ρ(∂u/∂t + u·∇u) = −∇P + μ∇²u + f. "
        "They describe how momentum, pressure, and viscosity govern fluid flow. "
        "Turbulence — one of the major unsolved problems in physics — arises from the nonlinear term (u·∇u). "
        "Critically dimension-sensitive: 2D turbulence exhibits inverse energy cascade (large vortices from small); 3D exhibits forward cascade (energy to small scales). "
        "This D-dependence makes Navier-Stokes a natural D_eff test bed."
    ),
    "Mathematical Form": "ρ(∂u/∂t + u·∇u) = −∇P + μ∇²u + f  |  ∇·u = 0  (incompressible)",
    "Constraint Category": "Thermodynamic/Geometric (Th/Ge): momentum conservation with dissipation (Th) in geometric embedding space (Ge — dimension-sensitive).",
    "DS Cross-References": "D=2 vs D=3 turbulence cascade direction is the most direct phenomenological test of dimensionality. Connects to A1 (Square-Cube): viscous dissipation scales with D_eff. TD7 (Boltzmann equation) → Navier-Stokes via moments. D2 (Feigenbaum) — turbulent cascades display universality.",
}),

("FM2", "Bernoulli's Principle", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "Along a streamline in steady, inviscid, incompressible flow, total mechanical energy per unit volume is conserved: P + ½ρv² + ρgh = const. "
        "Higher fluid velocity corresponds to lower pressure — this is the aerodynamic lift principle and explains venturi flow, aircraft wings, and cardiovascular pressure gradients. "
        "A direct application of energy conservation (TD2) to inviscid fluid flow."
    ),
    "Mathematical Form": "P + ½ρv² + ρgh = const  (along streamline)",
    "Constraint Category": "Geometric/Thermodynamic (Ge/Th): energy conservation along geometric streamlines.",
    "DS Cross-References": "Inviscid limit of FM1 (Navier-Stokes). X1 (vascular metabolic instantiation): Bernoulli governs pressure-flow in fractal vascular networks. A1 (Square-Cube): vascular scaling arises partly from pressure constraints.",
}),

("FM3", "Euler's Fluid Equations", "physics", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The inviscid (zero viscosity) form of the Navier-Stokes equations: ρ(∂u/∂t + u·∇u) = −∇P + f. "
        "Without viscosity, the equations are time-reversible. "
        "Euler flow develops singularities (vortex sheets) that viscosity regularizes in the full Navier-Stokes system. "
        "The transition from Euler to Navier-Stokes is a dissipation-switching transition — a regime change in the sense of H1."
    ),
    "Mathematical Form": "ρ(∂u/∂t + u·∇u) = −∇P + f  (no viscosity term)",
    "Constraint Category": "Geometric (Ge): inviscid — only geometric structure of flow, no dissipation.",
    "DS Cross-References": "Limiting case of FM1 (Navier-Stokes). H1 (Regime): the inviscid–viscous crossover is a regime transition. FM2 (Bernoulli) derives from Euler along streamlines.",
}),

("FM4", "Poiseuille's Law", "physics · biology", "organismal", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The volumetric flow rate through a cylindrical pipe is Q = πr⁴ΔP / (8ηL). "
        "The r⁴ dependence is a strong geometric scaling — doubling radius increases flow 16-fold. "
        "This is the foundational law of vascular hydraulics: blood flow, respiratory flow, and microfluidics all operate under Poiseuille constraints."
    ),
    "Mathematical Form": "Q = πr⁴ΔP / (8ηL)  (η = dynamic viscosity, L = pipe length)",
    "Constraint Category": "Geometric (Th/Ge): the r⁴ exponent is a D=3 geometric consequence of parabolic velocity profile + cylindrical geometry.",
    "DS Cross-References": "Critical for C1 (Metabolic Scaling/Kleiber): vascular geometry drives the ¾ exponent. X1 (Vascular/Metabolic instantiation): Poiseuille is the microscopic law. A1 (Square-Cube): vascular branching optimizes under Poiseuille + geometric constraints.",
}),

("FM5", "Stokes' Law", "physics", "organismal", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "At low Reynolds number (viscosity-dominated flow), the drag force on a sphere of radius r moving at velocity v in a fluid of viscosity η is F = 6πηrv. "
        "Linear in velocity — no turbulence. "
        "Stokes' law governs the motion of cells, bacteria, colloidal particles, and any slow-moving organism in fluid."
    ),
    "Mathematical Form": "F_drag = 6πηrv  (Stokes drag, low Reynolds number)",
    "Constraint Category": "Geometric (Ge): drag proportional to radius (not area or volume) — a D=3 geometric consequence of creeping flow.",
    "DS Cross-References": "FM1 (Navier-Stokes): Stokes' law is the linearized, low-Re limit. X1 (Vascular/Metabolic): governs cellular-scale transport within tissues. A1 (Square-Cube): at small scales, drag/weight ratios favor viscous over inertial regimes.",
}),

("FM6", "Faxén's Law", "physics", "molecular", "established", "Tier 2", "Ge", {
    "What It Claims": (
        "A generalization of Stokes' law that accounts for higher-order corrections when a particle is in a non-uniform flow field. "
        "The drag force includes terms proportional to the gradient of the undisturbed flow velocity at the particle center. "
        "Important in microfluidics, colloidal dynamics, and biological cell mechanics."
    ),
    "Mathematical Form": "F = 6πηr(u_∞ + (r²/6)∇²u_∞ − v_particle)",
    "Constraint Category": "Geometric (Ge): higher-order correction to Stokes — gradient coupling between particle and flow field.",
    "DS Cross-References": "Extension of FM5 (Stokes' law). Relevant for X1 (vascular) at the cellular level.",
}),

# ==========================================================================
# X. CHEMISTRY — KINETICS & EQUILIBRIUM  (KC1–KC10)
# ==========================================================================

("KC1", "Le Chatelier's Principle", "chemistry · physics", "cross-scale", "established", "Tier 1", "Th", {
    "What It Claims": (
        "If an external stress is applied to a system in chemical equilibrium, the system will shift in the direction that partially counteracts the stress. "
        "Increase pressure → equilibrium shifts to fewer moles of gas. Add heat → equilibrium shifts endothermically. "
        "It is the thermodynamic principle of homeostasis — every equilibrium system resists perturbation. "
        "EM8 (Lenz's law) is the electromagnetic analog; F4 (Saturation Dynamics) generalizes it to kinetic saturation."
    ),
    "Mathematical Form": "dG = 0 at equilibrium; perturbation → sign(dG) < 0 restoring shift",
    "Constraint Category": "Thermodynamic (Th): equilibrium restoration — the system minimizes Gibbs free energy against perturbation.",
    "DS Cross-References": "EM8 (Lenz's law): electromagnetic analog. F4 (Saturation Dynamics): KC1 is the equilibrium case; F4 is the kinetic-saturation generalization. F2 (Liebig): KC1 at the single-limiting-resource level.",
}),

("KC2", "Law of Microscopic Reversibility", "chemistry · physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "At equilibrium, the rate of every elementary process is exactly balanced by its reverse (detailed balance). "
        "No microscopic pathway can have a net flux at equilibrium. "
        "This follows from time-reversal symmetry in microscopic dynamics and is the molecular foundation of TD6 (Onsager reciprocal relations)."
    ),
    "Mathematical Form": "k_forward [A][B] = k_reverse [C][D]  at equilibrium  (for A + B ⇌ C + D)",
    "Constraint Category": "Thermodynamic (Th): time-reversal symmetry of microscopic dynamics → no net circulation at equilibrium.",
    "DS Cross-References": "Foundation for TD6 (Onsager reciprocal relations). AM5 (Noether): time-reversal is a discrete symmetry → detailed balance. Connects to H1 (Regime): breakdown of detailed balance signals a non-equilibrium regime transition.",
}),

("KC3", "Hammond–Leffler Postulate", "chemistry", "molecular", "established", "Tier 2", "Th", {
    "What It Claims": (
        "The transition state of a reaction resembles the species (reactant or product) that is closest to it in free energy. "
        "For exothermic reactions, the transition state is reactant-like; for endothermic, product-like. "
        "An empirical rule relating reaction mechanism to thermodynamics — the geometry of the energy landscape."
    ),
    "Mathematical Form": "δ‡ ≈ 0 for exothermic (early TS) | δ‡ ≈ 1 for endothermic (late TS)",
    "Constraint Category": "Thermodynamic (Th): relates transition state geometry to energy landscape topology.",
    "DS Cross-References": "B2 (Arrhenius): the barrier height and position determine the Arrhenius rate. KC1 (Le Chatelier): exo/endothermic direction and transition state geometry both depend on thermodynamic driving force.",
}),

("KC4", "Hess's Law", "chemistry", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The total enthalpy change of a reaction is independent of the path taken — it depends only on the initial and final states. "
        "This is a direct consequence of energy conservation (TD2): enthalpy H is a state function. "
        "Hess's law allows calculation of reaction enthalpies from tabulated values without direct measurement."
    ),
    "Mathematical Form": "ΔH_total = Σ ΔH_steps  (path-independent)",
    "Constraint Category": "Thermodynamic (Th): enthalpy is a state function — Th consequence of energy conservation.",
    "DS Cross-References": "Consequence of TD2 (first law: energy conservation). AM1 (least action): Hess's law is a thermodynamic path-independence principle — same logical structure as action stationarity.",
}),

("KC5", "Gibbs–Helmholtz Equation", "chemistry · physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "Relates the temperature dependence of Gibbs free energy to enthalpy: (∂(G/T)/∂T)_P = −H/T². "
        "Equivalently, ΔG = ΔH − TΔS sets the criterion for spontaneous processes (ΔG < 0). "
        "Free energy is the thermodynamic potential that determines chemical equilibrium and spontaneity at constant T and P."
    ),
    "Mathematical Form": "(∂(ΔG/T)/∂T)_P = −ΔH/T²  |  ΔG = ΔH − TΔS",
    "Constraint Category": "Thermodynamic (Th): free energy criterion for spontaneity — the master thermodynamic potential at constant T, P.",
    "DS Cross-References": "Derived from TD5 (fundamental thermodynamic relation). KC1 (Le Chatelier): equilibrium is the minimum of G. The ΔG = ΔH − TΔS structure is the thermodynamic analog of a constrained optimization (M1: KKT conditions).",
}),

("KC6", "Raoult's Law", "chemistry", "molecular", "established", "Tier 2", "Th", {
    "What It Claims": (
        "The vapor pressure of an ideal solution component is proportional to its mole fraction: P_A = x_A P°_A. "
        "Deviations from Raoult's law signal non-ideal behavior (intermolecular interactions). "
        "An additive mixing rule — the simplest thermodynamic model of solution behavior."
    ),
    "Mathematical Form": "P_A = x_A · P°_A  (x_A = mole fraction of A, P°_A = pure vapor pressure)",
    "Constraint Category": "Thermodynamic (Th): ideal mixing — no interaction between components changes the entropy of mixing.",
    "DS Cross-References": "Connects to KC5 (Gibbs-Helmholtz): deviations from Raoult's law appear in ΔG_mix. Structural analog to F2 (Liebig): both describe resource availability constraints in mixture systems.",
}),

("KC7", "Henry's Law", "chemistry", "molecular", "established", "Tier 2", "Th", {
    "What It Claims": (
        "The amount of gas dissolved in a liquid is proportional to the partial pressure of that gas above the liquid: C = k_H · P. "
        "Henry's law governs blood gas exchange in physiology, carbonation in beverages, and ocean CO₂ absorption. "
        "Breaks down at high concentrations — a saturation effect analogous to F4."
    ),
    "Mathematical Form": "C = k_H · P  (C = dissolved concentration, P = partial pressure)",
    "Constraint Category": "Thermodynamic (Th): linear equilibrium partition between phases — saturation at high P breaks linearity.",
    "DS Cross-References": "F4 (Saturation Dynamics): Henry's law is the linear regime; F4 is the Michaelis-Menten saturation generalization. F5 (Oxygen Viability Corridor): Henry's law governs O₂ solubility that sets the corridor bounds.",
}),

("KC8", "Law of Definite Composition", "chemistry", "molecular", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "A chemical compound always contains the same elements in the same mass ratio, regardless of its source or preparation. "
        "This is the empirical foundation of atomic theory — discrete atoms combine in fixed integer ratios. "
        "It implies that matter has a discrete, not continuous, structure."
    ),
    "Mathematical Form": "Mass fraction of element i = constant for any sample of compound C",
    "Constraint Category": "Geometric (Ge): fixed stoichiometry reflects discrete atomic combining geometry.",
    "DS Cross-References": "Foundation for QM3 (Pauli exclusion) and atomic structure. Discrete combining ratios are an early signal of the quantization that QM1 (Schrödinger) formalizes.",
}),

("KC9", "Dalton's Law of Multiple Proportions", "chemistry", "molecular", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "When two elements form more than one compound, the masses of one element that combine with a fixed mass of the other are in small integer ratios. "
        "This is direct evidence that atoms combine in discrete packets — a precursor to quantum discretization."
    ),
    "Mathematical Form": "m_A : m_A' = small integer ratio  (for two different compounds of A and B)",
    "Constraint Category": "Geometric (Ge): integer ratios from discrete atomic combining geometry.",
    "DS Cross-References": "Connects to KC8 (definite composition). Both point toward the atomic/quantum discretization formalized by QM1, QM3.",
}),

("KC10", "Law of Reciprocal Proportions", "chemistry", "molecular", "established", "Tier 1", "Ge", {
    "What It Claims": (
        "The ratio in which two elements A and B each combine with a fixed mass of a third element C is either the same as, or a simple multiple of, the ratio in which A and B combine with each other. "
        "Together with KC8 and KC9, this defines the stoichiometric consistency of all chemical reactions."
    ),
    "Mathematical Form": "Ratio of combining weights of A and B with C = simple multiple of ratio of A and B with each other",
    "Constraint Category": "Geometric (Ge): combinatorial consistency of discrete atomic combining ratios.",
    "DS Cross-References": "Completes the stoichiometric laws with KC8 and KC9. All three reflect the discrete, combinatorial geometry of atomic bonding.",
}),

# ==========================================================================
# XI. DIFFUSION & MASS TRANSPORT  (DM1–DM4)
# ==========================================================================

("DM1", "Fick's Laws of Diffusion", "chemistry · physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "First law: the diffusion flux J is proportional to the negative concentration gradient: J = −D∇c. "
        "Second law: the concentration evolves as ∂c/∂t = D∇²c (the diffusion equation). "
        "Fick's laws have identical mathematical form to TD10 (Fourier's law): both are gradient-driven transport laws. "
        "They govern transport in biology (oxygen diffusion in tissue), geology (isotope migration), and chemical engineering."
    ),
    "Mathematical Form": "J = −D∇c  (Fick's 1st)  |  ∂c/∂t = D∇²c  (Fick's 2nd / diffusion equation)",
    "Constraint Category": "Thermodynamic (Th): driven by concentration gradient (chemical potential gradient); produces entropy.",
    "DS Cross-References": "Structural pair with TD10 (Fourier's law): same ∇-proportional flux equation. X1 (vascular): tissue O₂ diffusion follows Fick. F5 (Oxygen Viability Corridor): diffusion limits set the corridor boundaries. DM2 (Graham's law) is the kinetic-theory derivation.",
}),

("DM2", "Graham's Law", "chemistry · physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The rate of diffusion or effusion of a gas is inversely proportional to the square root of its molar mass: r ∝ 1/√M. "
        "This follows from kinetic theory — at the same temperature, all gases have the same average kinetic energy (½Mv² = const), so lighter gases move faster. "
        "It quantifies the mass-dependent separation of isotopes and gases."
    ),
    "Mathematical Form": "r₁/r₂ = √(M₂/M₁)",
    "Constraint Category": "Thermodynamic (Th): kinetic energy equipartition → velocity inversely proportional to √mass.",
    "DS Cross-References": "Kinetic-theory basis for DM1 (Fick's laws). GL1 (Ideal gas law): same kinetic energy equipartition argument. Connects to TD12 (Dulong-Petit: equipartition again).",
}),

("DM3", "Lamm Equation", "chemistry", "molecular", "established", "Tier 2", "Th", {
    "What It Claims": (
        "Describes the sedimentation and diffusion of macromolecules in a centrifugal field: ∂c/∂t = D(∂²c/∂r²) − sω²r(∂c/∂r) + D(∂c/∂r)/r. "
        "The Lamm equation governs analytical ultracentrifugation — the technique used to determine molecular weights and shapes of proteins, nucleic acids, and polymers. "
        "A generalization of Fick's laws to non-uniform body-force fields."
    ),
    "Mathematical Form": "∂c/∂t = D(∂²c/∂r²) + (1/r − sω²r)D(∂c/∂r)",
    "Constraint Category": "Thermodynamic/Geometric (Th/Ge): diffusion + centrifugal sedimentation in cylindrical geometry.",
    "DS Cross-References": "Generalization of DM1 (Fick) to body-force fields. Relevant to X2 (Information Geometry): the Fisher information metric on statistical manifolds has a Lamm-like evolution equation.",
}),

("DM4", "Dalton's Law of Partial Pressures", "chemistry · physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "The total pressure of a mixture of non-reacting ideal gases equals the sum of the partial pressures of each component: P_total = Σ P_i. "
        "Each gas behaves independently, contributing pressure proportional to its mole fraction. "
        "A superposition principle for ideal gas mixtures."
    ),
    "Mathematical Form": "P_total = P₁ + P₂ + ... + Pₙ  |  Pᵢ = xᵢ · P_total",
    "Constraint Category": "Thermodynamic (Th): additivity of ideal gas pressure — no interaction between components.",
    "DS Cross-References": "Derives from GL1 (Ideal Gas Law) applied to mixtures. F5 (Oxygen Viability Corridor): partial pressure of O₂ in air vs. inside cell is the gradient driving the corridor.",
}),

# ==========================================================================
# XII. GAS LAWS  (GL1–GL5)
# ==========================================================================

("GL1", "Ideal Gas Law", "physics · chemistry", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": (
        "For an ideal gas (no intermolecular forces, point particles), pressure, volume, temperature, and amount are related by PV = nRT. "
        "This unifies Boyle's law (GL2), Charles's law (GL3), Gay-Lussac's law (GL4), and Avogadro's law (GL5) into a single equation. "
        "The ideal gas is the reference state for all real-gas thermodynamics — deviations from it signal intermolecular interactions."
    ),
    "Mathematical Form": "PV = nRT  (R ≈ 8.314 J·mol⁻¹·K⁻¹)",
    "Constraint Category": "Thermodynamic (Th): equation of state relating all thermodynamic variables of an ideal gas.",
    "DS Cross-References": "Foundation for TD7 (Boltzmann equation: microscopic basis of PV = nRT). DM4 (Dalton's law) applies this to mixtures. At high density, van der Waals corrections introduce the saturation signature of F4.",
}),

("GL2", "Boyle's Law", "physics · chemistry", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": "At constant temperature, the pressure of an ideal gas is inversely proportional to its volume: PV = const. Discovered empirically and now a special case of GL1 (ideal gas law).",
    "Mathematical Form": "P₁V₁ = P₂V₂  (isothermal)",
    "Constraint Category": "Thermodynamic (Th): isothermal constraint on ideal gas.",
    "DS Cross-References": "Special case of GL1 at constant T. Historical precursor to the unified ideal gas framework.",
}),

("GL3", "Charles's Law", "physics · chemistry", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": "At constant pressure, the volume of an ideal gas is proportional to its absolute temperature: V/T = const. A direct consequence of kinetic energy increasing with temperature.",
    "Mathematical Form": "V₁/T₁ = V₂/T₂  (isobaric)",
    "Constraint Category": "Thermodynamic (Th): isobaric constraint on ideal gas; defines absolute temperature via volume.",
    "DS Cross-References": "Special case of GL1 at constant P. Charles's law historically defined absolute zero as the temperature at which V → 0.",
}),

("GL4", "Gay-Lussac's Law", "physics · chemistry", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": "At constant volume, the pressure of an ideal gas is proportional to its absolute temperature: P/T = const. Heating a gas in a rigid container increases pressure proportionally.",
    "Mathematical Form": "P₁/T₁ = P₂/T₂  (isochoric)",
    "Constraint Category": "Thermodynamic (Th): isochoric constraint on ideal gas.",
    "DS Cross-References": "Special case of GL1 at constant V. Also applies to the combining volumes of gases in reactions — a bridge to KC8 (definite composition).",
}),

("GL5", "Avogadro's Law", "chemistry · physics", "molecular", "established", "Tier 1", "Th", {
    "What It Claims": "Equal volumes of all ideal gases at the same temperature and pressure contain equal numbers of molecules: V ∝ n at fixed T, P. This established that molecular count — not molecular type — determines volume, a profound insight into the nature of matter.",
    "Mathematical Form": "V/n = RT/P = const  (at fixed T, P)",
    "Constraint Category": "Thermodynamic (Th): molecular count determines volume regardless of molecular identity — an equipartition principle.",
    "DS Cross-References": "Part of GL1 (ideal gas law). Avogadro's number N_A = 6.022×10²³ mol⁻¹ connects molar (macroscopic) and molecular (microscopic) scales — a D_eff transition in scale.",
}),

# ==========================================================================
# XIII. INFORMATION THEORY (Landauer B5, Ashby F1 already exist — 0 new entries)
# ==========================================================================

# ==========================================================================
# XIV. SCALING & POWER LAWS (all existing — 0 new entries)
# ==========================================================================

# ==========================================================================
# XV. BIOLOGY — ECOLOGY & GENETICS  (BIO1–BIO3; F2, F3, F4 exist)
# ==========================================================================

("BIO1", "Mendelian Laws of Inheritance", "biology", "organismal", "established", "Tier 1", "In", {
    "What It Claims": (
        "Mendel's three laws govern the transmission of discrete heritable traits: "
        "(1) Segregation: each organism carries two alleles per gene; these separate during gamete formation so each gamete carries one. "
        "(2) Independent Assortment: genes on different chromosomes segregate independently. "
        "(3) Dominance: in a hybrid, one allele may mask the other. "
        "These discrete combinatorial rules are the genetic analog of KC8-KC9 (law of definite composition): information transmits in quanta."
    ),
    "Mathematical Form": "P(offspring genotype) from Punnett square | ratio 3:1 dominant:recessive in F2",
    "Constraint Category": "Informatic/Coordination (In/Co): discrete information packets (alleles) transmitted combinatorially — informatic conservation law.",
    "DS Cross-References": "BIO2 (Hardy-Weinberg) is the population-level consequence. QM3 (Pauli exclusion) has structural analogy: discrete states, combinatorial counting. KC8 (definite composition): both are discrete-ratio laws.",
}),

("BIO2", "Hardy–Weinberg Principle", "biology", "population", "established", "Tier 1", "Co", {
    "What It Claims": (
        "In an infinitely large, randomly mating population with no selection, mutation, migration, or genetic drift, "
        "allele and genotype frequencies remain constant across generations. "
        "The Hardy-Weinberg equilibrium (p² + 2pq + q² = 1 for two alleles) is the population genetic null model — "
        "deviations signal the forces of evolution. It is the genetic analog of chemical equilibrium (KC1 Le Chatelier): the baseline from which perturbations are measured."
    ),
    "Mathematical Form": "p² + 2pq + q² = 1  (p + q = 1 = allele frequencies)",
    "Constraint Category": "Coordination (Co): multi-agent equilibrium with no selection; random mating = mean-field coordination.",
    "DS Cross-References": "BIO1 (Mendel): Hardy-Weinberg is the large-population limit. KC1 (Le Chatelier): both describe equilibrium baselines and their perturbations. BIO3 (Natural Selection): deviations from HWE are caused by natural selection, drift, etc.",
}),

("BIO3", "Natural Selection — Fisher's Fundamental Theorem", "biology", "population", "established", "Tier 1", "In", {
    "What It Claims": (
        "Darwin's natural selection states that heritable variation in fitness leads to the differential reproduction of fitter variants, changing population composition over time. "
        "Fisher's fundamental theorem formalizes this: the rate of increase in mean fitness equals the additive genetic variance in fitness. "
        "The deep structural bridge: additive genetic variance in fitness IS the Fisher information of the population about its environment. "
        "Natural selection is Fisher information maximization."
    ),
    "Mathematical Form": "dW̄/dt = Var_A(w)  (Fisher's fundamental theorem, W̄ = mean fitness)",
    "Constraint Category": "Informatic/Coordination (In/Co): fitness = information content; selection = information gradient ascent.",
    "DS Cross-References": (
        "M6 (Fisher Information Rank): the metric of the DS information geometry is Fisher information — same as fitness in biological evolution. "
        "The structural bridge: maximizing Fisher information (M6) = maximizing fitness (BIO3). "
        "F3 (Gause competitive exclusion): a consequence of natural selection at the ecological level. "
        "Ax1 (Information Primacy): natural selection as information-theoretic optimization."
    ),
}),

# ==========================================================================
# XVI. EARTH SCIENCES & GEOGRAPHY  (ES1–ES14)
# ==========================================================================

("ES1", "Tobler's First Law of Geography", "earth sciences · networks", "population", "established", "Tier 1", "Co", {
    "What It Claims": (
        "\"Everything is related to everything else, but near things are more related than distant things.\" "
        "Spatial autocorrelation: the correlation between variables at two locations decays with their geographic separation. "
        "The decay rate encodes the effective dimensionality of the network substrate — a slower decay suggests higher-dimensional connectivity. "
        "The law formalizes the intuition that proximity implies similarity."
    ),
    "Mathematical Form": "Corr(X_i, X_j) = f(d_ij)  with f decreasing in distance d_ij",
    "Constraint Category": "Coordination/Geometric (Co/Ge): spatial correlation decay — a network geometry constraint.",
    "DS Cross-References": "Spatial correlation decay encodes D_eff of the geographic network substrate — directly testable with Ax2. C2 (Urban Scaling): city network topology produces superlinear scaling; Tobler's law is the spatial correlation foundation. X5 (Ecological Networks): species interaction strength decays with spatial separation.",
}),

("ES2", "Arbia's Law of Geography", "earth sciences", "population", "established", "Tier 2", "Co", {
    "What It Claims": "Aggregating spatial data to coarser geographic units inflates apparent statistical correlations. The modifiable areal unit problem (MAUP): spatial statistics depend on the scale of observation. This is a methodological statement about how coarse-graining (scale change) affects correlation structure.",
    "Mathematical Form": "Apparent correlation increases as spatial aggregation scale increases",
    "Constraint Category": "Coordination/Dimensional (Co/Di): scale-dependent correlation — a spatial analog of D_eff scale-dependence.",
    "DS Cross-References": "Directly relevant to Ax2 (D_eff is scale-dependent: the observer's resolution changes measured correlations). ES1 (Tobler): Arbia's law quantifies how Tobler's correlation changes with aggregation scale.",
}),

("ES3", "Archie's Law", "earth sciences", "molecular", "established", "Tier 2", "Ge", {
    "What It Claims": "Empirical law relating electrical resistivity of a saturated porous rock to its porosity φ and water resistivity: ρ_rock = a·ρ_water·φ^(−m)·S_w^(−n). The exponent m (cementation factor) encodes the geometric complexity of the pore network — a fractal-dimension signature.",
    "Mathematical Form": "ρ_rock = a · ρ_water · φ^(−m) · S_w^(−n)",
    "Constraint Category": "Geometric (Ge): pore network geometry determines conductivity — exponent m encodes network fractal dimension.",
    "DS Cross-References": "H2 (Fractal Dimension d_f): Archie's cementation exponent m is a proxy for pore network fractal dimension. C3 (Heavy-Tailed Distributions): pore size distributions in many rocks follow power laws.",
}),

("ES4", "Buys Ballot's Law", "earth sciences", "cross-scale", "established", "Tier 2", "Ge", {
    "What It Claims": "In the Northern Hemisphere, if you stand with your back to the wind, low pressure is to your left and high pressure to your right (reversed in Southern Hemisphere). Formalizes how the Coriolis force (rotating-frame geometry) deflects winds around pressure centers.",
    "Mathematical Form": "Wind direction rotated 90° from pressure gradient by Coriolis force: f×v adds perpendicular component",
    "Constraint Category": "Geometric (Ge): Coriolis deflection is a D=3 rotating-frame geometric effect.",
    "DS Cross-References": "Coriolis force is a rotating-frame effect that appears only in D=3 (cross-product structure). CM1 (Newton's laws in rotating frame). Connects to FM1 (Navier-Stokes) — the geostrophic wind balance is FM1 with Coriolis.",
}),

("ES5", "Birch's Law", "earth sciences", "molecular", "established", "Tier 2", "Ge", {
    "What It Claims": "Compressional seismic velocity in rocks is linearly related to mean atomic weight at constant density: V_P ≈ a + b·M̄. An empirical law that allows seismic measurements to constrain the chemical composition of the Earth's interior inaccessible to direct sampling.",
    "Mathematical Form": "V_P = a + b·M̄  (a, b empirical constants; M̄ = mean atomic weight)",
    "Constraint Category": "Geometric (Ge): velocity-density-composition geometric relationship in minerals.",
    "DS Cross-References": "Empirical scaling law with domain-specific exponents. Connects to D1 (Stevens' Power Law): both are empirical power-law relations between observable quantities in complex materials.",
}),

("ES6", "Byerlee's Law", "earth sciences", "organismal", "established", "Tier 2", "Th", {
    "What It Claims": "The shear stress required to cause sliding on a fault is approximately: τ ≈ 0.85σₙ for σₙ < 200 MPa, and τ ≈ 50 + 0.6σₙ for higher pressures (τ = shear stress, σₙ = normal stress). A near-universal empirical law independent of rock type — the frictional strength of the crust.",
    "Mathematical Form": "τ ≈ 0.85σₙ  (low pressure)  |  τ ≈ 50 MPa + 0.6σₙ  (high pressure)",
    "Constraint Category": "Thermodynamic (Th): frictional dissipation limit — a Th ceiling on fault stability.",
    "DS Cross-References": "Empirical constraint analogous to F2 (Liebig: limiting resource constraint). The bilinear form suggests a regime transition at σₙ ≈ 200 MPa — H1 (Regime mechanism).",
}),

("ES7", "Titius–Bode Law", "astronomy", "cosmological", "contested", "Tier 2", "Ge", {
    "What It Claims": "The distances of planets from the Sun follow an approximate exponential sequence: a ≈ 0.4 + 0.3×2ⁿ AU (n = −∞, 0, 1, 2, ...). Originally used to predict the existence of the asteroid belt and Neptune. No established physical derivation — may reflect resonance conditions in protoplanetary disk formation.",
    "Mathematical Form": "a_n ≈ 0.4 + 0.3 × 2ⁿ  AU",
    "Constraint Category": "Geometric (Ge): exponential spacing — potential resonance geometry of orbital mechanics.",
    "DS Cross-References": "The geometric spacing pattern connects to D2 (Feigenbaum universality): period-doubling cascades produce geometric sequences. C2 (Urban Scaling): hierarchical geometric patterns in orbital spacing may reflect network topology. Status: contested — not derivable from first principles.",
}),

("ES8", "Steno's Law of Superposition", "earth sciences", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": "In any sequence of undisturbed sedimentary rock layers, the oldest layers are at the bottom and the youngest at the top. A direct consequence of gravity and sequential deposition — the vertical axis encodes time in stratigraphic context.",
    "Mathematical Form": "Age(layer_i) > Age(layer_j) if depth(i) > depth(j)  (undeformed strata)",
    "Constraint Category": "Geometric (Ge): gravitational constraint on deposition order — a temporal ordering principle from spatial geometry.",
    "DS Cross-References": "Geometric constraint from gravity (CM2). The principle of temporal ordering from spatial position is structurally analogous to the topological ordering in directed networks (related to H4: topological obstruction).",
}),

("ES9", "Principle of Original Horizontality", "earth sciences", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": "Sedimentary layers are originally deposited horizontally. Tilted or folded strata have been deformed after deposition. Gravity + fluid mechanics of deposition enforce horizontal bedding as the minimum energy configuration.",
    "Mathematical Form": "Initial deposition plane ⊥ gravity vector  (minimum potential energy state)",
    "Constraint Category": "Geometric (Ge): gravitational potential energy minimization determines deposition geometry.",
    "DS Cross-References": "Gravity (CM2) + TD2 (energy conservation): horizontal deposition minimizes potential energy. AM1 (least action): natural systems take the path/configuration of minimum action.",
}),

("ES10", "Principle of Lateral Continuity", "earth sciences", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": "A sedimentary layer, when originally deposited, extends laterally in all directions until it either thins and disappears or reaches the edge of the depositional basin. Allows correlation of rock layers across distances where physical continuity cannot be directly observed.",
    "Mathematical Form": "Spatial extent of layer at deposition: connected across basin boundary conditions",
    "Constraint Category": "Geometric (Ge): spatial continuity of deposition — a topological connectivity constraint.",
    "DS Cross-References": "Topological connectivity of strata connects to H4 (topological obstruction χ_eff) and Q1 (fractal dimension from power-law exponents in spatial distributions).",
}),

("ES11", "Principle of Cross-Cutting Relationships", "earth sciences", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": "A geological feature (fault, igneous intrusion, vein) that cuts across another feature must be younger than the feature it cuts. Provides relative age dating through geometric intersection analysis.",
    "Mathematical Form": "If feature A intersects/cuts feature B: Age(A) < Age(B)",
    "Constraint Category": "Geometric (Ge): temporal ordering from geometric intersection — topology encodes time.",
    "DS Cross-References": "Topological argument: intersection implies temporal sequence. Similar to the topological ordering in H4 (χ_eff) and directed graph analysis in the DS connection network.",
}),

("ES12", "Principle of Faunal Succession", "earth sciences · biology", "cross-scale", "established", "Tier 1", "Co", {
    "What It Claims": "Fossil assemblages succeed one another in a definite, recognizable order — the same fossil sequence appears in rock layers worldwide. This allows stratigraphic correlation across continental distances and provides the primary evidence for evolution as a historical process.",
    "Mathematical Form": "Fossil assemblage sequence is globally consistent and irreversible",
    "Constraint Category": "Coordination (Co): global biological coordination through evolutionary history — irreversible temporal ordering.",
    "DS Cross-References": "BIO3 (Natural Selection): faunal succession is the geological record of evolutionary selection. ES8 (Superposition) + ES11 (Cross-cutting): together these provide the complete relative dating framework. Irreversible change connects to TD3 (2nd law).",
}),

("ES13", "Principle of Inclusions and Components", "earth sciences", "cross-scale", "established", "Tier 1", "Ge", {
    "What It Claims": "Any rock fragment (clast or inclusion) included within another rock must be older than the host rock. If rock A contains pieces of rock B, then B was solid before A formed around it.",
    "Mathematical Form": "If fragment B ⊂ rock A: Age(B) > Age(A)",
    "Constraint Category": "Geometric (Ge): containment implies prior existence — geometric enclosure encodes temporal order.",
    "DS Cross-References": "Same geometric-temporal reasoning as ES11 (cross-cutting). Topological containment argument.",
}),

("ES14", "Walther's Law of Facies", "earth sciences", "cross-scale", "established", "Tier 1", "Co", {
    "What It Claims": "Sedimentary environments (facies) that are laterally adjacent in space will appear vertically adjacent in the stratigraphic record — if no major unconformity separates them. Lateral spatial gradients translate directly into vertical temporal sequences during transgression/regression.",
    "Mathematical Form": "Lateral facies sequence ↔ vertical facies sequence  (under conformable deposition)",
    "Constraint Category": "Coordination/Geometric (Co/Ge): spatial-temporal transformation law — lateral position maps to vertical (temporal) position.",
    "DS Cross-References": "A space-time translation symmetry: the horizontal axis (space) maps to the vertical axis (time). Connects structurally to the DS framework's D_eff as a scale-dependent coordinate system, where spatial and temporal scales interconvert.",
}),

]  # end ENTRIES list

# ---------------------------------------------------------------------------
# Insertion logic
# ---------------------------------------------------------------------------

def normalize_filename(entry_id: str, title: str) -> str:
    """Generate a slug filename from id + title."""
    slug = title.lower()
    for ch in "()[]{}!@#$%^&*=+|\\;:'\",.<>?/`~":
        slug = slug.replace(ch, "")
    slug = slug.replace(" ", "_").replace("–", "-").replace("—", "-")
    while "__" in slug:
        slug = slug.replace("__", "_")
    slug = slug[:60].rstrip("_")
    return f"{entry_id}_{slug}.md"


def insert_entries(db_path: str, entries: list, dry_run: bool = False):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    inserted = 0
    skipped = 0
    errors = []

    for row in entries:
        entry_id, title, domain, scale, status, confidence, constraint, sections = row

        # Check for id conflict
        existing = cur.execute("SELECT id FROM entries WHERE id=?", (entry_id,)).fetchone()
        if existing:
            print(f"  SKIP (exists): {entry_id} — {title}")
            skipped += 1
            continue

        filename = normalize_filename(entry_id, title)

        try:
            cur.execute("""
                INSERT INTO entries (id, title, filename, entry_type, scale, domain, status, confidence, type_group)
                VALUES (?, ?, ?, 'reference_law', ?, ?, ?, ?, 'RL')
            """, (entry_id, title, filename, scale, domain, status, confidence))

            for order, (section_name, content) in enumerate(sections.items()):
                cur.execute("""
                    INSERT INTO sections (entry_id, section_name, section_order, content)
                    VALUES (?, ?, ?, ?)
                """, (entry_id, section_name, order, content))

            # Store constraint category as an entry property
            cur.execute("""
                INSERT INTO entry_properties (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?, 'DS Facets', 'Constraint Category', ?, 0)
            """, (entry_id, constraint))

            inserted += 1
            if not dry_run:
                print(f"  + {entry_id}: {title}")

        except Exception as e:
            errors.append((entry_id, str(e)))
            print(f"  ERROR {entry_id}: {e}")

    if not dry_run:
        conn.commit()
        print(f"\nCommitted: {inserted} inserted, {skipped} skipped, {len(errors)} errors")
    else:
        print(f"\nDRY RUN: would insert {inserted}, skip {skipped}, {len(errors)} errors")
        conn.rollback()

    conn.close()
    return inserted, skipped, errors


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing")
    args = parser.parse_args()

    print(f"Target DB: {SOURCE_DB}")
    print(f"Total entries to insert: {len(ENTRIES)}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE INSERT'}\n")

    inserted, skipped, errors = insert_entries(str(SOURCE_DB), ENTRIES, dry_run=args.dry_run)

    if errors:
        print("\nErrors:")
        for eid, err in errors:
            print(f"  {eid}: {err}")
        sys.exit(1)

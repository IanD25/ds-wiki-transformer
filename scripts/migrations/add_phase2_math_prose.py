"""
add_phase2_math_prose.py  — Phase 2: "What The Math Says"

Adds a "What The Math Says" section to every entry that has a mathematical
form.  The prose translates equations into natural language that the embedding
model (BGE-Small-EN-v1.5) can cluster meaningfully.

Why this matters:
  LaTeX strings like ∇·E = ρ/ε₀ tokenise to sub-word noise.
  The sentence "charge density is the divergence of the electric field, meaning
  charges are the sources and sinks of field lines" carries rich semantic signal.

Strategy:
  - 3-6 sentences per entry
  - Name each variable and what it represents
  - Describe qualitative behaviour (monotonic, inverse, exponential…)
  - Connect to physical / conceptual meaning
  - Reference DS framework context where relevant (DS-native entries only)

Run: .venv/bin/python scripts/add_phase2_math_prose.py [--dry-run]
"""

import sqlite3, sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import SOURCE_DB

# ===========================================================================
# PROSE DATA — keyed by entry_id
# ===========================================================================
# Each value is the "What The Math Says" section text (plain prose, no LaTeX).
# Entries without a Mathematical Form / Formula section are omitted.

PROSE: dict[str, str] = {

# ---------------------------------------------------------------------------
# DS-NATIVE: THEOREMS / LAWS / CONSTRAINTS / AXIOMS
# ---------------------------------------------------------------------------

"A1": (
    "When a shape is scaled by factor k, its surface area grows as k-squared and its volume "
    "as k-cubed. As objects grow larger, their volume grows faster than their surface — the "
    "surface-to-volume ratio shrinks as 1/k, so large animals have proportionally less skin "
    "relative to their mass than small ones. In D effective dimensions the gap persists but "
    "shifts: area scales as L to the power (D minus 1) and volume as L to the power D, so "
    "the exponent difference is always exactly one regardless of dimension. This asymmetry "
    "drives thermoregulation, nutrient transport, and structural constraints across all "
    "biological and physical systems."
),

"A2": (
    "The measured length of a fractal curve depends on the ruler size used: L of epsilon "
    "equals C times epsilon raised to the power (1 minus D_f), where epsilon is ruler size "
    "and D_f is the fractal (Hausdorff) dimension between 1 and 2. As the ruler shrinks the "
    "measured length grows without bound — there is no unique length for a fractal coastline. "
    "The fractal dimension D_f quantifies how fast length grows with finer measurement: D_f "
    "near 1 means a nearly smooth curve, D_f near 2 means an extremely crinkled surface-filling "
    "path. Equivalently D_f equals the negative slope of log(L) versus log(epsilon), directly "
    "readable from a log-log plot of measured length against ruler size."
),

"B1": (
    "The radioactive decay constant lambda equals an attempt frequency f multiplied by the "
    "quantum tunneling probability through the nuclear potential barrier. The tunneling probability "
    "is the exponential of minus twice the integral of imaginary momentum across the barrier — "
    "a wider or taller barrier makes this integral larger and the probability exponentially "
    "smaller. A nucleus attempts the barrier at its natural vibration frequency (roughly 10 to "
    "the 21 per second) but succeeds only an exponentially small fraction of attempts. The WKB "
    "approximation gives an exact exponential dependence rather than just an order-of-magnitude "
    "estimate, and the resulting decay constant lambda directly gives the half-life as ln(2) "
    "divided by lambda."
),

"B2": (
    "The reaction rate constant k equals a pre-exponential factor A (the attempt or collision "
    "frequency) multiplied by the Boltzmann factor exp(minus E_a divided by k_B T). The activation "
    "energy E_a is the energy barrier height; temperature T sets how much thermal energy is "
    "available to surmount it; k_B is Boltzmann's constant. Doubling the temperature does not "
    "double the rate — instead it shifts the exponential argument, so rates can increase by "
    "orders of magnitude over modest temperature ranges. The pre-exponential A captures both "
    "the frequency of collision attempts and geometric or orientation factors. Plotting ln(k) "
    "against inverse temperature gives the Arrhenius plot, a straight line with slope minus "
    "E_a divided by k_B."
),

"B3": (
    "The peak emission wavelength lambda_max of a blackbody is inversely proportional to its "
    "absolute temperature T, with proportionality constant b approximately 2.898 times 10 to "
    "the minus 3 meter-kelvin. Hotter objects emit at shorter (bluer) wavelengths; cooler "
    "objects emit at longer (redder) wavelengths. This is a direct consequence of the Planck "
    "distribution shifting and compressing toward shorter wavelengths as temperature increases. "
    "The sun (T around 5778 K) peaks in visible green; a human body (T around 310 K) peaks "
    "in the mid-infrared around 9 micrometers; a very hot star (T around 30000 K) peaks in "
    "the ultraviolet."
),

"B4": (
    "The Rayleigh scattering cross-section sigma scales as d to the sixth power divided by "
    "wavelength lambda to the fourth power, where d is particle diameter. The inverse fourth-power "
    "wavelength dependence means short wavelengths (blue, violet) scatter far more strongly "
    "than long wavelengths (red, infrared). Doubling particle diameter increases scattering "
    "64-fold (2 to the 6th). The sky is blue because molecules in the atmosphere scatter "
    "blue sunlight far more than red; sunsets are red because the long atmospheric path "
    "removes blue light, leaving only the long-wavelength red end. The law applies when "
    "particle diameter is much smaller than the wavelength."
),

"B5": (
    "The minimum energy dissipated per bit of information erased is k_B times T times ln(2), "
    "where k_B is Boltzmann's constant and T is temperature. Erasing information is a "
    "logically irreversible operation — it maps two distinguishable states to one — and the "
    "second law of thermodynamics requires that this irreversibility generate at least k_B T "
    "ln(2) of heat. Reversible computation (quantum computing in principle) can avoid this "
    "cost entirely. At room temperature the Landauer limit is approximately 3 times 10 to "
    "the minus 21 joules per bit — far below current processor dissipation (~10 to the minus "
    "15 joules per operation) but a fundamental thermodynamic floor."
),

"C1": (
    "Metabolic rate B scales as body mass M raised to exponent alpha approximately 0.75, with "
    "B_0 a species-specific normalization constant. In the DS framework, alpha equals D_eff "
    "divided by (D_eff plus 1), where D_eff is the fractal dimensionality of the vascular "
    "distribution network. A space-filling network in three dimensions with fractal surface "
    "has D_eff equal to 3, giving alpha of 3/4 exactly. The exponent is not fixed biology — "
    "organisms with different vascular geometries (higher or lower D_eff) should have different "
    "metabolic exponents, and this prediction is experimentally testable by comparing alpha "
    "measured from oxygen consumption data against D_eff measured by micro-CT box-counting."
),

"C2": (
    "Urban output Y scales as city population N raised to power beta, with Y_0 a normalization. "
    "Socioeconomic outputs (GDP, patents, crime, innovation) scale superlinearly with beta "
    "approximately 1.15 — doubling population yields 15 percent more output per person. "
    "Infrastructure (roads, pipes, electrical grid) scales sublinearly with beta approximately "
    "0.85 — larger cities need less infrastructure per person, giving economies of scale. "
    "Basic biological needs (food, water consumption) scale linearly with beta approximately "
    "1.0 — cities provide no biological advantage. The 15-percent rule captures how denser "
    "human interaction in larger cities concentrates social and economic processes."
),

"C3": (
    "Heavy-tailed distributions have survival probability P(X greater than x) proportional to "
    "x to the minus alpha, a power-law tail. Unlike exponential distributions that vanish "
    "rapidly, power laws assign substantial probability to extreme events: when alpha is 1 "
    "the mean is infinite; when alpha is 2 the variance is infinite. The same distribution "
    "appears in three equivalent forms: the Pareto tail (survival function), the Zipf rank "
    "law (frequency of the r-th ranked item proportional to r to the minus 1/alpha), and the "
    "probability density (proportional to x to the minus alpha plus 1). Heavy tails arise "
    "from multiplicative processes, preferential attachment, or cascading threshold crossings."
),

"D1": (
    "Perceived intensity psi scales as physical stimulus intensity I raised to exponent n, "
    "times a modality constant k. Different senses have different exponents: electric shock "
    "has n approximately 3.5 (supralinear — small physical increases feel large), apparent "
    "brightness has n approximately 0.33 (compressive — large physical increases feel small), "
    "and loudness has n approximately 0.6 (moderately compressive). The power law replaces "
    "the older logarithmic Fechner law, which underestimated sensitivity at intensity extremes. "
    "The exponent n reflects how aggressively the sensory system compresses or expands the "
    "physical signal, and can be interpreted as the system's information-maximizing strategy "
    "given its finite dynamic range."
),

"D2": (
    "As a nonlinear map's control parameter increases, the system undergoes successive "
    "period-doubling bifurcations at parameter values a_n. The ratio of consecutive bifurcation "
    "intervals converges to delta approximately 4.669 — the Feigenbaum constant — universally, "
    "regardless of the map's specific functional form. Similarly the branch widths shrink by "
    "a factor alpha approximately 2.503 per bifurcation. Both constants are the same for any "
    "smooth one-dimensional map with a single quadratic maximum, making them universal "
    "numbers analogous to critical exponents at phase transitions. This universality means "
    "all such maps approach chaos at the same geometric rate, determined by the topology of "
    "the period-doubling cascade rather than any particular equation."
),

"E1": (
    "Transistor count N doubles approximately every two years, following an exponential growth "
    "law N(t) equals N_0 times 2 to the power (t divided by tau) where tau is approximately "
    "2 years. The growth is driven by coordinated industrial investment, miniaturization "
    "techniques, and manufacturing improvements rather than a single physical law. Moore's law "
    "is empirical and describes a technological trajectory sustained by economic incentives. "
    "It held from 1965 to approximately 2016 before physical limits — quantum tunneling "
    "through gate oxides and heat dissipation per unit area — slowed areal density growth, "
    "shifting progress toward multicore architectures and 3D chip stacking."
),

"E2": (
    "Computational efficiency eta (computations per joule) doubles approximately every 1.57 "
    "years, following eta(t) equals eta_0 times 2 to the power (t divided by tau_K). This "
    "tracks the energy dimension of Moore's law — not just more transistors, but more "
    "efficient transistors. The doubling period of approximately 1.57 years has been consistent "
    "since the 1950s across vacuum tubes, discrete transistors, and integrated circuits. The "
    "law suggests that fundamental limits on energy efficiency (approaching the Landauer limit "
    "from above) will ultimately constrain computational efficiency more stringently than "
    "transistor density."
),

"F1": (
    "A control system must have at least as many distinguishable states (variety, measured "
    "in bits) as the system it regulates, reduced by whatever the communication channel can "
    "absorb: V_controller is greater than or equal to V_system minus V_channel. Variety is "
    "the log base 2 of the number of distinguishable states — a thermostat with two states "
    "has 1 bit of variety. If the environment can be in 1024 states (10 bits) and the channel "
    "can resolve 512 states (9 bits), the controller needs at least 1 bit of variety. The "
    "law formalizes 'only variety can destroy variety' — a controller too simple to match "
    "system complexity cannot maintain control."
),

"F2": (
    "System output Y is determined by the single scarcest resource, not by the total or "
    "average: Y equals the minimum over all resources of (available R_i divided by requirement "
    "k_i per unit output). Adding more of any non-limiting resource has zero marginal effect. "
    "Only when the binding constraint changes — because the bottleneck resource is resupplied "
    "or another becomes scarcer — does a different resource become limiting. This non-linearity "
    "means interventions must target the binding constraint to improve output, and the binding "
    "constraint can shift dynamically as conditions change."
),

"F3": (
    "Two competing species each follow logistic growth reduced by competition from the other. "
    "Species i grows at rate r_i N_i (1 minus (N_i plus alpha_ij N_j) divided by K_i), where "
    "K_i is carrying capacity and alpha_ij is the competitive effect of species j on species i. "
    "Stable coexistence requires intraspecific competition to exceed interspecific competition "
    "for both species simultaneously — each species must limit itself more than it limits the "
    "other. When this condition fails, whichever species has the competitive advantage drives "
    "the other to extinction. The principle states that two species competing for a single "
    "limiting resource cannot stably coexist."
),

"F4": (
    "Three equivalent forms describe approach to a finite ceiling: Michaelis-Menten kinetics "
    "(enzyme rate v approaches maximum V_max as substrate concentration S increases, with "
    "half-maximum at K_m); logistic growth (population N approaches carrying capacity K via "
    "an S-shaped sigmoid with inflection at t_0); and asymptotic growth (output Y approaches "
    "Y_max exponentially with rate k). All three arise from differential equations of the form "
    "dy/dt proportional to y times (1 minus y/ceiling). The shared signature is deceleration "
    "near the ceiling and linear growth near the origin — a natural consequence of negative "
    "feedback from a finite resource."
),

"F5": (
    "The viable oxygen partial pressure window is defined by four simultaneously binding "
    "constraints: thermodynamic feasibility of the ferrous-to-oxidized electron transfer step "
    "(requires minimum membrane potential delta-psi); substrate delivery rate (cytochrome c "
    "concentration relative to its Michaelis constant K_m); proton backpressure suppression "
    "(high delta-psi above 180 mV inhibits turnover); and ROS ceiling (reactive oxygen species "
    "production cannot exceed antioxidant detoxification capacity). The viable oxygen corridor "
    "is the intersection of all four constraint sets simultaneously, not the weakest of them "
    "individually. Violating any single constraint breaks mitochondrial function regardless "
    "of whether the others are satisfied."
),

"G1": (
    "Apparent cosmological redshift z accumulates as light travels through regions where effective "
    "dimensionality D_eff(r) varies with distance r. The integral of (1/D_eff) times (d D_eff/dr) "
    "measures the total fractional change in D_eff along the light path. Where D_eff decreases "
    "(more structure, higher effective dimensionality locally) the integrand is negative, "
    "contributing a blueshift component; where D_eff increases the contribution is redshift. "
    "The effective Hubble parameter H_eff at any point equals (c/D_eff) times (dD_eff/dr) — "
    "generalizing the cosmological expansion parameter to local dimensional gradients. This "
    "predicts that lines of sight through dense cosmic structure should show systematic "
    "redshift residuals correlating with foreground dimensional geometry."
),

"G3": (
    "Reconstructing the bulk (interior volume) gravitational field from boundary (surface) "
    "data requires computational complexity at least exponential in the boundary system size n. "
    "This holographic computational bound parallels the information-theoretic Bekenstein bound: "
    "entropy S of a region is at most A divided by (4 times l_P squared), where A is the "
    "boundary area and l_P is the Planck length. Maximum entropy scales with surface area, not "
    "volume — the interior is holographically encoded on the boundary. But reading that encoding "
    "back requires exponential computation, meaning the holographic representation is highly "
    "compressed: easy to write, hard to read back."
),

"H5": (
    "The unified scaling exponent beta interpolates linearly between two limits based on "
    "phase coherence lambda. When lambda equals 1 (full fractal coherence), beta equals "
    "d_f divided by (d_f plus 1) — the Kleiber-type metabolic exponent characteristic of "
    "fractal networks. When lambda equals 0 (no fractal coherence), beta equals 1 — linear "
    "scaling characteristic of integer-dimensional systems. Intermediate lambda blends these "
    "proportionally: beta equals lambda times d_f/(d_f+1) plus (1 minus lambda). Both fractal "
    "dimension d_f (which sets the fractal limit) and phase coherence lambda (which sets how "
    "fractal the system actually is) must be independently measured, making the formula a "
    "two-parameter prediction testable against observed scaling exponents."
),

"M1": (
    "KKT complementary slackness requires that for each inequality constraint g_i(x), either "
    "the constraint is exactly binding (g_i of x-star equals zero) or its shadow price mu_i "
    "is zero — never both nonzero. A binding constraint means the optimum is being pushed "
    "against a hard limit; the shadow price mu_i then measures how much the objective improves "
    "per unit relaxation of that constraint. A slack constraint means the system operates "
    "freely below the limit; relaxing it further has no value. The condition encodes resource "
    "scarcity: binding constraints correspond to scarce resources driving the optimum, while "
    "slack constraints correspond to abundant resources that are not limiting."
),

"M2": (
    "The system evolves under one of two distinct linear rational-expectations equation "
    "systems depending on which regime is active. In the reference regime (constraint slack), "
    "matrices A, B, C govern dynamics. In the alternative regime (constraint binding), "
    "different matrices A-star, B-star, C-star apply, plus a constant term D-star encoding "
    "the constraint pressure. The matrices switch discontinuously when the constraint "
    "threshold is crossed. For each regime, the Blanchard-Kahn eigenvalue condition must "
    "independently hold to ensure a unique bounded solution. The two-regime structure means "
    "linear perturbation analysis of one regime does not capture the nonlinear effects of "
    "regime switching."
),

"M3": (
    "The Preisach model represents any hysteretic system as a superposition of elementary "
    "relay operators, each of which switches from off to on at threshold alpha and from on "
    "to off at threshold beta (with beta less than alpha). The Preisach density mu(alpha, beta) "
    "is a probability distribution over the plane of all possible threshold pairs. The output "
    "f(u) is the integral of all relay states weighted by their density — effectively a "
    "spectral decomposition of hysteresis over the simplest possible hysteretic units. This "
    "framework is powerful because any complex hysteresis can be expressed as a specific "
    "choice of density function mu, and the model handles memory, branching, and saturation "
    "within a single mathematical structure."
),

"M4": (
    "The Mori-Zwanzig equation of motion for observable variable A_i has three components. "
    "The Markovian term Omega_ij times delta A_j captures the instantaneous response to the "
    "current state, analogous to a friction coefficient in the Langevin equation. The memory "
    "integral integrates the kernel K(t,s) times past states delta A_j(s) — past states "
    "continue to influence present dynamics with influence decaying as described by K. The "
    "orthogonal noise F_i(t) represents fluctuations from all unresolved degrees of freedom. "
    "As the separation between resolved and unresolved time scales grows, the memory kernel "
    "approaches a delta function and the dynamics become Markovian. The projection formally "
    "eliminates bath variables while capturing their statistical effect through memory and noise."
),

"M5": (
    "For a linear rational-expectations system with n_1 predetermined (state) variables and "
    "n_2 jump (expectational) variables, the Blanchard-Kahn condition requires exactly n_2 "
    "eigenvalues of the system matrix to lie outside the unit circle. Too few unstable "
    "eigenvalues allow indeterminate solutions (sunspot equilibria); too many cause explosive "
    "paths with no bounded solution. The correct eigenvalue count makes the stable manifold "
    "exactly n_1 dimensional — exactly enough dimensions to pin down the initial conditions "
    "of predetermined variables while allowing jump variables to be set by forward-looking "
    "expectations. The condition is the saddle-path stability requirement for recursive "
    "backward induction in dynamic programming."
),

"M6": (
    "The Fisher information matrix F_ij at observation scale ell captures how much information "
    "the data carry about each pair of parameters theta_i and theta_j. Its elements are the "
    "expected products of score functions — measuring the statistical curvature of the "
    "log-likelihood surface. The rank of F equals the effective dimensionality D_eff: a "
    "rank-k matrix means only k independent parameter combinations can be distinguished from "
    "data at scale ell. As observation scale increases (coarser measurement), F loses rank — "
    "information is compressed and fewer parameter combinations remain distinguishable. The "
    "identification of D_eff with Fisher rank makes effective dimensionality a directly "
    "computable quantity from any statistical model."
),

"OmD": (
    "The dimensional scaling operator Omega_D equals ((D minus 2) divided by 2) raised to "
    "the power lambda. At D equals 4 (standard four-dimensional spacetime) Omega_D equals 1 "
    "for any lambda, ensuring all physical constants recover their standard values identically. "
    "At D equals 2 the argument is zero and Omega_D vanishes (a singular limit requiring "
    "regularization). For D between 2 and 4, Omega_D interpolates continuously. Different "
    "physical constants scale with their own exponents lambda_G (Newton's constant), lambda_h "
    "(Planck's constant), and lambda_m (effective mass), encoding how sensitive each quantity "
    "is to dimensional change. The operator is the central mechanism by which the DS framework "
    "modifies all physical laws when effective dimensionality departs from four."
),

"T1": (
    "Effective dimensionality D_eff at observation scale ell equals the rank of the Fisher "
    "information matrix F(ell). The theorem states this rank can only decrease or stay "
    "constant as ell increases — D_eff(ell-prime) is less than or equal to D_eff(ell) for "
    "all ell-prime greater than ell. This is a consequence of the Data Processing Inequality: "
    "coarse-graining cannot create new parameter distinguishability. At fine scales the Fisher "
    "matrix has more nonzero eigenvalues (more independent observable dimensions); at coarser "
    "scales eigenvalues merge toward zero as information is compressed. The theorem provides "
    "the formal foundation for the DS claim that effective dimensionality is scale-dependent "
    "and always decreases under coarse-graining."
),

"T2": (
    "The metabolic scaling exponent alpha equals D_eff divided by (D_eff plus 1), directly "
    "linking a biological power-law exponent to an independently measurable geometric property "
    "of the vascular network. For D_eff equal to 3 (volume-filling branching network), alpha "
    "equals 3/4 — matching the empirically observed Kleiber exponent. For D_eff equal to 2 "
    "(surface-filling network), alpha equals 2/3. The theorem is empirically testable: measure "
    "alpha from metabolic oxygen consumption data and D_eff from micro-CT imaging and "
    "box-counting on the same organism, then check whether alpha equals D_eff over (D_eff "
    "plus 1). Agreement would constitute direct evidence that metabolic scaling exponents "
    "are geometric signatures of vascular network dimensionality."
),

"T3": (
    "The Omega_D unit consistency audit verifies two requirements: first, that Omega_D raised "
    "to any power lambda is dimensionless; second, that all DS-modified physical equations "
    "recover correct SI units when D equals 4. The operator ((D minus 2)/2) to the power "
    "lambda is dimensionless by construction since it is a pure ratio raised to a pure "
    "exponent. The recovery check at D equals 4 confirms Omega_4 equals 1, so modified "
    "equations reduce to their standard forms exactly. At D equals 2, Omega_D equals zero — "
    "a singular limit that signals breakdown of the operator's applicability at this "
    "dimensional extreme and may require regularization."
),

"T4": (
    "The redshift-structure correlation test compares predicted redshift residuals from the "
    "DS dimensional redshift formula against observed Hubble law residuals along the same "
    "line of sight. The DS formula predicts z(r) equals the exponential of the integral of "
    "(1/D_eff) times (dD_eff/dr) minus 1 — a redshift contribution from dimensional gradients "
    "along the path. Lines of sight through high-structure regions (galaxy clusters, cosmic "
    "filaments) should show systematic residuals Delta-z correlating with independently "
    "mapped dimensional structure. The null hypothesis is no such correlation. A positive "
    "result would be the first observational evidence for dimensional gradients contributing "
    "to apparent cosmological redshift."
),

"T5": (
    "Standard universality classes of phase transitions (Ising, XY, Heisenberg) assign discrete "
    "critical exponents determined by integer spatial dimensionality and order parameter "
    "components. The DS prediction is that when effective dimensionality D_eff is non-integer, "
    "critical exponents beta, gamma, and nu interpolate continuously between the values of "
    "the nearest integer universality classes. A system with D_eff equal to 2.7 should have "
    "exponents proportional to (D_eff minus 2), interpolating between d=2 and d=3 values. "
    "The test asks whether real physical systems (thin films, porous media, fractally confined "
    "materials) show the predicted continuous exponent variation as D_eff is tuned, or whether "
    "universality class membership remains discrete."
),

"T6": (
    "The holographic reconstruction complexity gate triggers if a proof establishes that "
    "recovering bulk (interior) information from boundary data requires computation at least "
    "exponential in boundary system size n. The claimed bound is C(bulk reconstruction) "
    "greater than or equal to 2 to the Omega(n), where the big-Omega notation means at least "
    "exponential growth. This would formalize the holographic principle as a computational "
    "complexity statement: not only is boundary entropy bounded by area, but reconstructing "
    "the bulk from the boundary is computationally hard. The gate opens a bridge between "
    "complexity theory and holographic duality that would have implications for quantum gravity."
),

"T7": (
    "If effective dimensionality D_eff differs from 4, the effective Planck constant h_eff "
    "scales as Omega_D to the power lambda_h times the standard h. Since hadron charge radii "
    "depend on h through QCD confinement and quark dynamics, non-standard D_eff would shift "
    "predicted radii by a factor determined by Omega_D raised to lambda_h. The test compares "
    "DS-framework predictions against standard QCD lattice calculations for proton and neutron "
    "charge radii. A positive signal (significant deviation in the predicted direction) would "
    "require D_eff different from 4 at hadronic scales of approximately 1 femtometer — "
    "suggesting dimensional deviation at nuclear length scales far smaller than any currently "
    "known structure."
),

# ---------------------------------------------------------------------------
# REFERENCE LAWS — ANALYTICAL MECHANICS (AM)
# ---------------------------------------------------------------------------

"AM1": (
    "The action S equals the time integral of the Lagrangian L (kinetic energy minus potential "
    "energy). The principle of least action states that the actual path a system follows "
    "between two configurations is the one for which the variation delta-S of the action "
    "is zero. Setting the first variation to zero yields the Euler-Lagrange equations as "
    "necessary conditions, which are equivalent to Newton's second law but expressed in "
    "generalized coordinates without needing to enumerate constraint forces explicitly. The "
    "principle extends naturally from classical mechanics to field theory, special and general "
    "relativity, and quantum mechanics via the path integral, making it the most universal "
    "formulation of dynamics across all of physics."
),

"AM2": (
    "For each generalized coordinate q_i, the Euler-Lagrange equation states that the time "
    "derivative of the generalized momentum p_i equals the partial derivative of the Lagrangian "
    "with respect to q_i. The generalized momentum p_i equals partial L divided by partial "
    "q-dot_i — the momentum conjugate to coordinate q_i, which may be angular momentum, "
    "linear momentum, or another conserved quantity depending on the coordinate choice. In "
    "Cartesian coordinates the equation reduces directly to Newton F equals ma. In curvilinear "
    "coordinates or with holonomic constraints eliminated, the same equation applies but "
    "automatically accounts for constraint forces that Newton's approach would require computing "
    "separately. The power of Lagrangian mechanics is the coordinate freedom — generalized "
    "coordinates absorb constraints and reduce the number of equations."
),

"AM3": (
    "Hamilton's equations split each degree of freedom into two coupled first-order equations: "
    "the time derivative of momentum p equals minus the partial derivative of the Hamiltonian H "
    "with respect to position q (momentum is driven by the negative gradient of H); and the "
    "time derivative of position q equals the partial derivative of H with respect to momentum "
    "p (position evolves in the direction of increasing H in momentum space). The Hamiltonian H "
    "is typically the total energy T plus V, expressed in terms of positions and momenta rather "
    "than velocities. This phase-space formulation reveals the geometric structure of mechanics: "
    "trajectories flow incompressibly in (q, p) space (Liouville's theorem), and H generates "
    "the flow via Poisson brackets."
),

"AM4": (
    "The Hamilton-Jacobi equation H(q, partial S / partial q, t) equals minus partial S / "
    "partial t defines the action S as a function of position and time (called Hamilton's "
    "principal function). When H does not depend on time explicitly, S separates: S equals "
    "W(q) minus E times t, where W satisfies H(q, partial W / partial q) equals E. Finding "
    "the complete solution S fully solves the mechanical problem — trajectories follow the "
    "gradient of W in configuration space. The equation bridges classical and quantum mechanics: "
    "Schrödinger's equation reduces exactly to Hamilton-Jacobi in the classical limit h-bar "
    "tends to zero, when the quantum phase S divided by h-bar is identified with the classical "
    "principal function."
),

"AM5": (
    "Noether's theorem states that every continuous symmetry of the action corresponds to a "
    "conserved Noether current J-mu satisfying the divergence condition partial_mu J-mu equals "
    "zero. Time translation symmetry (H unchanged under t shifted to t plus epsilon) gives "
    "energy conservation; spatial translation symmetry gives momentum conservation; rotation "
    "symmetry gives angular momentum conservation; U(1) phase symmetry gives electric charge "
    "conservation. The theorem is constructive — given any infinitesimal transformation that "
    "leaves the action invariant, the conserved current can be built explicitly from the "
    "variation. Noether's theorem explains why conservation laws exist (they reflect symmetries) "
    "and predicts new conserved quantities whenever new symmetries are discovered."
),

# ---------------------------------------------------------------------------
# BIOLOGY (BIO)
# ---------------------------------------------------------------------------

"BIO1": (
    "Mendelian genetics predicts offspring genotype frequencies from the Punnett square "
    "combination of parental alleles. For a single gene with dominant allele D and recessive "
    "allele r, crossing two heterozygotes (Dr times Dr) yields genotype ratios 1 DD : 2 Dr : "
    "1 rr, and phenotype ratio 3 dominant : 1 recessive in the F2 generation. The 3:1 ratio "
    "is the direct consequence of alleles segregating independently during gamete formation. "
    "When two genes are on different chromosomes, they assort independently and ratios "
    "multiply: the 9:3:3:1 dihybrid ratio in F2 is the product of two 3:1 ratios. Mendel's "
    "laws are exact for independently assorting unlinked loci with no fitness differences."
),

"BIO2": (
    "The Hardy-Weinberg principle states that under random mating with no selection, mutation, "
    "migration, or genetic drift, allele frequencies remain constant across generations. If "
    "allele A has frequency p and allele a has frequency q (with p plus q equals 1), genotype "
    "frequencies are p-squared for AA, 2pq for Aa, and q-squared for aa, and these frequencies "
    "are restored in one generation of random mating. The principle provides the null model "
    "for population genetics: any departure from Hardy-Weinberg equilibrium signals the action "
    "of one or more evolutionary forces. It is equivalent to a statistical statement that "
    "alleles at a diploid locus combine like independent draws from an urn."
),

"BIO3": (
    "Fisher's fundamental theorem of natural selection states that the rate of increase in "
    "mean fitness W-bar equals the additive genetic variance in fitness Var_A(w). Mean fitness "
    "always increases over time at a rate proportional to how much heritable variation in "
    "fitness exists — more variation means faster adaptation. The theorem assumes constant "
    "environment; in a changing environment the term that subtracts changing environment "
    "effects must be included. Fisher interpreted this as a biological analogue of the second "
    "law of thermodynamics, with fitness playing the role of entropy's inverse, always "
    "increasing under selection."
),

# ---------------------------------------------------------------------------
# CLASSICAL MECHANICS (CM)
# ---------------------------------------------------------------------------

"CM1": (
    "Newton's three laws cover inertia, force, and reaction. First: a body with zero net force "
    "moves at constant velocity in a straight line — velocity is the natural state, not rest. "
    "Second: net force F equals mass m times acceleration a (equivalently, F equals rate of "
    "change of momentum dp/dt) — force causes acceleration proportional to force and inversely "
    "proportional to mass. Third: forces always come in equal and opposite pairs acting on "
    "different bodies — the earth pulls the apple down with the same force the apple pulls "
    "the earth up. In the Lagrangian formulation, all three laws derive from extremizing the "
    "action for kinetic Lagrangian L equals T minus V."
),

"CM2": (
    "The gravitational force between masses m_1 and m_2 separated by distance r is F equals "
    "G times m_1 times m_2 divided by r-squared, where G approximately 6.674 times 10 to "
    "the minus 11 N·m²·kg⁻² is Newton's gravitational constant. Doubling the distance reduces "
    "force to one-quarter; tripling distance reduces it to one-ninth. The inverse-square "
    "dependence is a geometric consequence of D equals 3: gravitational flux spreads over a "
    "sphere of area 4 pi r-squared, so field strength falls as r to the minus 2. In D spatial "
    "dimensions the exponent would be minus (D minus 1), making the inverse-square law a "
    "direct signature of three-dimensional space."
),

"CM3": (
    "Planetary orbits are conic sections with the gravitating body at one focus. The orbit "
    "equation r equals ell divided by (1 plus e times cosine theta) describes the radial "
    "distance r as a function of orbital angle theta. The semi-latus rectum ell sets the "
    "overall size; eccentricity e determines the shape: e equals 0 gives a circle, e between "
    "0 and 1 gives an ellipse, e equals 1 gives a parabola, e greater than 1 gives a hyperbola. "
    "The gravitating body sits at one focus, not the center — so perihelion (closest approach) "
    "occurs at theta equals 0 and aphelion (furthest point) at theta equals pi. This result "
    "follows directly from the 1/r-squared force law."
),

"CM4": (
    "The rate at which a planet's radius vector sweeps out area, dA/dt equals the magnitude "
    "of angular momentum L divided by twice the planetary mass m, is constant throughout the "
    "orbit. This constancy is equivalent to conservation of angular momentum: the gravitational "
    "force is purely central (directed toward the sun), so it exerts no torque and cannot "
    "change L. The planet moves faster when close to the sun (small r requires larger angular "
    "velocity to maintain r-squared times d-theta/dt equals L/m constant) and slower when "
    "far away. The law holds for any central force, not just gravity, and was the first "
    "quantitative statement of angular momentum conservation."
),

"CM5": (
    "The square of orbital period T equals (4 pi squared divided by G times the total system "
    "mass m plus M) times the cube of the semi-major axis a. For planets much less massive "
    "than their star (m much less than M), the total mass is approximately M and T-squared "
    "is proportional to a-cubed with the star's mass setting the constant of proportionality. "
    "A planet twice as far from its star takes 2 to the 3/2 power (approximately 2.83) times "
    "as long to orbit. The law emerges from the inverse-square nature of gravity — a different "
    "force law would give a different period-distance exponent, so Kepler's third law provides "
    "evidence for the 1/r-squared form of gravity."
),

"CM6": (
    "Newton's second law extends to rigid bodies as two separate equations. The translational "
    "equation F equals dp/dt governs the motion of the center of mass: net external force "
    "equals rate of change of total linear momentum. The rotational equation tau equals dL/dt "
    "governs rotation about the center of mass: net external torque equals rate of change of "
    "angular momentum. Internal forces cancel in the first equation (Newton's third law) and "
    "contribute zero net torque about the center of mass for symmetric distributions. Together "
    "the two equations provide six coupled scalar equations fully determining rigid body "
    "trajectories in three dimensions."
),

"CM7": (
    "The buoyant force on a submerged or partially submerged object equals the weight of the "
    "fluid displaced: F_buoy equals rho_fluid times g times V_displaced. An object floats "
    "when the weight of displaced fluid exactly equals the object's weight — equivalently "
    "when the object's average density equals the fluid density. For partial submersion, only "
    "the submerged volume V_displaced contributes. The principle follows from the pressure "
    "distribution in the fluid: pressure increases with depth, so the upward pressure force "
    "on the bottom of a submerged object exceeds the downward pressure on the top, giving a "
    "net upward force equal to the displaced fluid's weight."
),

"CM8": (
    "The electromagnetic force on a charge q moving with velocity v in electric field E and "
    "magnetic field B is F equals q times (E plus v cross B). The electric component qE acts "
    "along the field direction and accelerates the charge; the magnetic component q(v cross B) "
    "is perpendicular to both velocity and field, deflecting the path without doing work. "
    "The cross product means the magnetic force is zero when v is parallel to B and maximum "
    "when perpendicular. Magnetic fields alone curve charged particle trajectories into circles "
    "or helices but cannot change particle speed. The law unifies the separate electric and "
    "magnetic forces that appear in different inertial frames as aspects of one electromagnetic "
    "interaction."
),

# ---------------------------------------------------------------------------
# DIFFUSION AND TRANSPORT (DM)
# ---------------------------------------------------------------------------

"DM1": (
    "Fick's first law states that diffusion flux J equals minus D times the gradient of "
    "concentration c: matter flows from regions of high concentration to low, with a rate "
    "proportional to the concentration slope and the diffusion coefficient D. The minus sign "
    "means flux opposes the gradient — downhill diffusion. Fick's second law (the diffusion "
    "equation) states that concentration changes in time as partial c / partial t equals D "
    "times the Laplacian of c: without sources or sinks, concentration evolves to eliminate "
    "gradients, approaching uniform distribution exponentially. Together these laws describe "
    "thermal random walks: D is related to step size and frequency by D equals (step squared) "
    "divided by (2 times time)."
),

"DM2": (
    "Graham's law of effusion states that the rate of effusion (flow of gas through a tiny "
    "hole) for gas 1 relative to gas 2 is inversely proportional to the square root of the "
    "ratio of their molar masses M_1 and M_2: r_1 divided by r_2 equals the square root of "
    "M_2 divided by M_1. Heavier gases effuse more slowly because at the same temperature "
    "they have the same average kinetic energy (1/2 M v-squared equals 3/2 k_B T) but lower "
    "average speed (v proportional to 1 over square root of M). Graham's law was used by "
    "the Manhattan Project to separate uranium isotopes U-235 and U-238 via gaseous diffusion "
    "of UF_6 — the slight mass difference (349 vs 352 g/mol) gives a separation factor of "
    "approximately 1.004 per stage."
),

"DM3": (
    "The Lamm equation describes sedimentation and diffusion of a macromolecule in an "
    "ultracentrifuge. The concentration c changes in time due to diffusion (proportional to "
    "D times the second spatial derivative of c) and sedimentation (the centrifugal force "
    "term proportional to s times omega-squared times r times dc/dr, where s is the "
    "sedimentation coefficient, omega is angular velocity, and r is radial distance from "
    "the rotation axis). At steady state, diffusion balances sedimentation and the "
    "concentration profile gives both s and D, from which molecular weight and shape can "
    "be inferred. The equation is fundamental to analytical ultracentrifugation for "
    "characterizing macromolecules."
),

"DM4": (
    "Dalton's law of partial pressures states that the total pressure of a gas mixture equals "
    "the sum of the partial pressures of each component gas: P_total equals P_1 plus P_2 "
    "plus up to P_n. Each partial pressure P_i equals the mole fraction x_i times the total "
    "pressure — each gas contributes as if it alone occupied the full volume. The law follows "
    "from the ideal gas assumption that molecules do not interact with each other between "
    "collisions. Dalton's law allows the partial pressure of any component to be computed "
    "from its mole fraction, which is essential for calculating equilibrium constants, "
    "solubilities, and vapor pressures of mixtures."
),

# ---------------------------------------------------------------------------
# ELECTROMAGNETISM (EM)
# ---------------------------------------------------------------------------

"EM1": (
    "The divergence of the electric field E at any point equals the local free charge density "
    "rho divided by the permittivity of free space epsilon_0. In integral form, the total "
    "electric flux through any closed surface equals the total enclosed charge divided by "
    "epsilon_0. This means electric field lines originate on positive charges and terminate "
    "on negative charges: charges are the sources and sinks of the electric field. In empty "
    "space with no charge, the electric field is divergence-free. The equation is the "
    "electromagnetic equivalent of Gauss's law for gravity and confirms that electric field "
    "lines are continuous except at charges."
),

"EM2": (
    "The divergence of the magnetic field B is zero everywhere: there are no magnetic "
    "monopoles, no magnetic sources or sinks. In integral form, every magnetic field line "
    "that enters any closed surface must exit it — magnetic flux through any closed surface "
    "is exactly zero. Magnetic field lines always form closed loops, never beginning or "
    "ending. This law would be modified to nabla-dot-B equals mu_0 times rho_m if magnetic "
    "monopoles were discovered, analogous to Gauss's electric law. The absence of monopoles "
    "is one of the empirically confirmed pillars of classical electrodynamics."
),

"EM3": (
    "The curl of the electric field E equals the negative time derivative of the magnetic "
    "field B: a changing magnetic field induces a circulating electric field in the surrounding "
    "space, even in the absence of any conductor. In integral form (Faraday's law), the "
    "electromotive force around a closed loop equals the negative rate of change of magnetic "
    "flux through it. The minus sign (Lenz's law) means the induced current creates a magnetic "
    "field opposing the change: a decreasing B induces current that tries to maintain B, "
    "and an increasing B induces opposing current. Electromagnetic induction is the operating "
    "principle of generators, transformers, and induction motors."
),

"EM4": (
    "The curl of the magnetic field B equals mu_0 times current density J plus (1/c-squared) "
    "times partial E / partial t. Maxwell added the displacement current term (1/c-squared) "
    "partial E / partial t to the original Ampere's law, where c equals 1 divided by the "
    "square root of mu_0 times epsilon_0. Without this term, the equation's divergence would "
    "violate charge conservation when the electric field changes in time. The displacement "
    "current allowed Maxwell to predict electromagnetic waves propagating at exactly the speed "
    "of light c, revealing that light is an electromagnetic wave. This single term unified "
    "optics and electromagnetism."
),

"EM5": (
    "The continuity equation for electric charge states that the rate of change of charge "
    "density rho at any point equals minus the divergence of current density J. Where "
    "current flows out of a volume (positive divergence of J), charge density decreases; "
    "where current flows in (negative divergence), charge density increases. This is the "
    "mathematical statement of local charge conservation: charge cannot disappear in one "
    "place and reappear elsewhere — it must flow continuously. The equation is the "
    "electromagnetic analog of mass conservation in fluid mechanics and holds exactly in "
    "classical and quantum electrodynamics."
),

"EM6": (
    "Coulomb's law gives the electrostatic force between two point charges q_1 and q_2 "
    "separated by distance r: F equals k times q_1 times q_2 divided by r-squared, where "
    "k equals 1 over (4 pi epsilon_0) approximately 8.99 times 10 to the 9 N·m²·C⁻². Like "
    "charges repel; opposite charges attract. The inverse-square dependence is a geometric "
    "consequence of D equals 3: the field from a point charge spreads over a sphere of area "
    "4 pi r-squared, so field strength falls as 1/r-squared. In quantum electrodynamics, "
    "Coulomb's law is the tree-level amplitude of massless photon exchange between charged "
    "particles. Deviations from the inverse-square law would signal massive photons or extra "
    "spatial dimensions."
),

"EM7": (
    "The magnetic field contribution dB from a small current element I times dl at distance "
    "r is proportional to (I times dl cross r-hat) divided by r-squared, where the cross "
    "product means the field circles around the current direction. Field lines form closed "
    "rings centered on the current; no field exists along the current axis. The total field "
    "is the integral of contributions from all current elements along the conductor. For an "
    "infinite straight wire, integrating over all elements gives B equals mu_0 I divided by "
    "(2 pi r) — field falling as 1/r, not 1/r-squared, because integrating a 1/r-squared "
    "source over an infinite line yields 1/r by geometric cancellation."
),

"EM8": (
    "An induced EMF (electromotive force) in a circuit always acts to oppose the change in "
    "magnetic flux that produced it. If flux is increasing, the induced current creates a "
    "magnetic field opposing the increase; if flux is decreasing, the induced current creates "
    "a field trying to maintain the original flux. Lenz's law is the statement of the minus "
    "sign in Faraday's law and is required by energy conservation: if induced currents "
    "reinforced flux changes, a small initial perturbation would grow without limit, generating "
    "energy from nothing. The law governs eddy current braking, inductive loading of generators, "
    "and the back-EMF of motors."
),

"EM9": (
    "Ohm's law states that current I through a conductor is proportional to voltage V across "
    "it: V equals I times R, where R is resistance. In microscopic form, current density J "
    "equals conductivity sigma times electric field E. Ohm's law holds for linear ohmic "
    "conductors (metals at moderate temperatures, many electrolytes) but fails for "
    "semiconductors, plasmas, and nonlinear devices. Microscopically, it follows from the "
    "Drude model: electrons are accelerated by E but scatter randomly from lattice atoms, "
    "reaching a drift velocity proportional to E. Resistance R depends on material "
    "resistivity rho, length L, and cross-sectional area A through R equals rho L divided by A."
),

"EM10": (
    "Kirchhoff's current law (KCL) states that the sum of currents entering any junction "
    "equals the sum leaving: charge is conserved locally, with no accumulation at nodes in "
    "steady state. Kirchhoff's voltage law (KVL) states that the sum of voltage drops around "
    "any closed loop is zero: voltage is a state function and any path between two points "
    "gives the same voltage difference. Together KCL and KVL provide a complete algebraic "
    "system for analyzing any linear circuit: N nodes give N minus 1 independent KCL "
    "equations, and L independent loops give L KVL equations, sufficient to solve for all "
    "branch currents and voltages."
),

"EM11": (
    "Joule's law states that electrical power dissipated as heat in a resistor equals I-squared "
    "times R (or V-squared divided by R, or V times I). The quadratic dependence on current "
    "means doubling the current quadruples heating — power transmission lines use high voltage "
    "and low current to minimize resistive losses over long distances. Joule heating is always "
    "positive regardless of current direction, making it an irreversible process: it converts "
    "ordered electrical energy into disordered thermal energy, increasing entropy. The effect "
    "is the microscopic mechanism of resistance: electrons transfer their drift kinetic energy "
    "to the lattice in collisions."
),

# ---------------------------------------------------------------------------
# EARTH SCIENCES (ES)
# ---------------------------------------------------------------------------

"ES1": (
    "Tobler's first law states that the correlation between attributes at two locations "
    "decreases as the distance d_ij between them increases. The correlation function Corr(X_i, "
    "X_j) equals f(d_ij) where f is a decreasing function of distance — nearby locations "
    "are more similar than distant ones in virtually every geographic variable. This spatial "
    "autocorrelation is the empirical foundation of geostatistics, spatial interpolation "
    "(kriging), and geographic information systems. It reflects the physical processes that "
    "produce geographic patterns: diffusion, advection, and proximity-based interaction all "
    "create correlation that decays with distance."
),

"ES2": (
    "Arbia's law states that apparent spatial correlation increases as the areal units used "
    "for aggregation get larger — larger spatial units show stronger correlation because "
    "within-unit variation is averaged away. This is the geographic manifestation of the "
    "modifiable areal unit problem: statistics computed at the county level will show different "
    "patterns than the same data at the tract, state, or national level. Apparent correlations "
    "at large scales can be artifacts of aggregation rather than reflecting genuine large-scale "
    "processes. The law warns against using spatially aggregated data to infer fine-scale "
    "relationships."
),

"ES3": (
    "Archie's law relates the bulk electrical resistivity of a porous rock to its water "
    "content: rho_rock equals a times rho_water times porosity phi to the minus m times "
    "water saturation S_w to the minus n, where a, m, and n are empirical constants. Higher "
    "porosity means more conductive pathways and lower resistivity; lower water saturation "
    "means fewer conductive pathways and higher resistivity. The law is purely empirical "
    "but remarkably consistent across rock types. It is the primary tool for estimating "
    "hydrocarbon saturation from electrical resistivity logs in oil and gas exploration — "
    "oil is resistive, water is conductive, so high resistivity in a porous formation "
    "signals oil."
),

"ES4": (
    "Buys Ballot's law describes the effect of Earth's rotation on wind direction. The Coriolis "
    "force f times v (where f is the Coriolis parameter and v is wind speed) adds a "
    "perpendicular component to the pressure-gradient force, rotating wind direction approximately "
    "90 degrees from what pure pressure gradient would predict. In the Northern Hemisphere "
    "wind curves right; in the Southern Hemisphere it curves left. At large scales (synoptic "
    "weather systems) this rotation is nearly complete and winds blow approximately along "
    "isobars rather than across them. The rule of thumb: in the Northern Hemisphere, stand "
    "with the wind at your back and low pressure is to your left."
),

"ES5": (
    "Birch's law states that the compressional seismic wave velocity V_P in a mineral is "
    "approximately linear in mean atomic weight M-bar: V_P equals a plus b times M-bar, "
    "where a and b are empirical constants. Heavier elements slow seismic waves through "
    "their greater mass density; the relationship is remarkably linear across a wide range "
    "of minerals and pressures. Birch's law allows seismologists to infer the composition "
    "of Earth's deep interior — which cannot be directly sampled — from seismic velocity "
    "profiles. It is the primary constraint on the composition of Earth's lower mantle "
    "and core."
),

"ES6": (
    "Byerlee's law gives the shear stress tau required to cause frictional sliding on a rock "
    "fault: at normal stresses below approximately 200 MPa, tau approximately equals 0.85 "
    "times normal stress sigma_n; at higher normal stresses, tau approximately equals 50 MPa "
    "plus 0.6 times sigma_n. The law is remarkably similar across rock types — most rocks "
    "have nearly the same coefficient of friction. The pressure-dependent form at higher "
    "pressures reflects the Byerlee effect: once confining pressure is high enough, sliding "
    "resistance saturates. Byerlee's law governs fault mechanics, earthquake nucleation, and "
    "the depth profile of seismicity in Earth's crust."
),

"ES7": (
    "The Titius-Bode law gives approximate orbital semi-major axes of planets: a_n approximately "
    "equals 0.4 plus 0.3 times 2 to the n, in astronomical units, where n is minus infinity "
    "for Mercury, 0 for Venus, 1 for Earth, 2 for Mars, and so on. The law predicted the "
    "existence of a planet between Mars and Jupiter (where the asteroid belt is found) and "
    "matched Uranus when discovered in 1781. It fails for Neptune. The law has no established "
    "physical derivation — it may reflect gravitational resonance conditions during planetary "
    "formation or may be partly coincidental. It remains a numerological curiosity rather "
    "than a fundamental physical law."
),

"ES8": (
    "Steno's law of superposition states that in an undisturbed sedimentary sequence, lower "
    "layers are older than upper ones: age of layer i is greater than age of layer j when "
    "depth of i is greater than depth of j. This is the foundational principle of stratigraphy "
    "and relative geochronology. Exceptions occur where tectonic deformation has overturned "
    "strata, thrust older rock over younger, or produced unconformities. Superposition allows "
    "geologists to determine the relative sequence of geological events from rock exposures "
    "without any absolute age measurement."
),

"ES9": (
    "The principle of original horizontality states that sedimentary layers are deposited "
    "approximately horizontally, perpendicular to the gravity vector, because this minimizes "
    "gravitational potential energy during deposition. Consequently, any tilting, folding, "
    "or dipping of strata from the horizontal reflects post-depositional tectonic deformation. "
    "The principle allows geologists to infer the direction and magnitude of deformation from "
    "the current orientation of originally horizontal beds. It was first stated by Nicolaus "
    "Steno in 1669 and remains the basis for structural geology's interpretation of deformed "
    "rock sequences."
),

"ES10": (
    "The principle of lateral continuity states that a sedimentary layer extends laterally "
    "in all directions across a depositional basin, thinning or changing facies at the basin "
    "margins. The spatial extent of a layer at deposition is bounded by the basin edges — "
    "where sediment supply ends or water depth changes to zero. If the same layer is found "
    "on both sides of a valley or canyon, the layer originally connected across the gap "
    "before erosion removed the middle portion. This principle allows correlation of rock "
    "units across geographical distances, forming the basis of stratigraphic mapping."
),

"ES11": (
    "The principle of cross-cutting relationships states that any geological feature that "
    "cuts across or intrudes into another feature is younger than what it cuts: if feature "
    "A intersects or transects feature B, then A is younger than B. This applies to faults "
    "cutting through rock layers (the fault is younger than the layers), dikes intruding "
    "into country rock (the dike is younger), and erosional unconformities cutting across "
    "tilted strata. The principle provides a way to establish relative ages of geological "
    "events from field observations of geometric relationships, independent of absolute "
    "radiometric dating."
),

"ES12": (
    "The principle of faunal succession states that fossil assemblages succeed one another "
    "in a definite and deterministic order through time, with the sequence reproducible "
    "globally and irreversible: once a species disappears from the fossil record it does "
    "not reappear in younger rocks. Each time interval (period, epoch) is characterized by "
    "a unique assemblage of index fossils — species with short stratigraphic ranges and wide "
    "geographic distribution. This allows correlation of rock units across continents by "
    "matching fossil assemblages even when the physical rock types differ completely. The "
    "principle is the foundation of biostratigraphy."
),

"ES13": (
    "The principle of inclusions states that if a fragment or xenolith of rock B is included "
    "within rock A, then B is older than A. The fragment had to exist before it could be "
    "incorporated. Granite xenoliths in basalt are older than the basalt; pebbles of "
    "quartzite in conglomerate are older than the conglomerate. This principle establishes "
    "the temporal priority of the incorporated material over the matrix rock and allows "
    "relative dating of plutonic and sedimentary sequences by identifying incorporated "
    "fragments."
),

"ES14": (
    "Walther's law of facies states that vertical sequences of sedimentary facies in a "
    "conformable succession correspond to lateral facies sequences in the modern environment "
    "during the same time of deposition. If facies A is on top of facies B in a vertical "
    "section, then facies A's environment was laterally adjacent to facies B's environment "
    "during deposition — later sea level or shoreline migration stacked them vertically. "
    "The law connects space and time in sedimentary systems, allowing past lateral geography "
    "to be reconstructed from vertical sedimentary sequences."
),

# ---------------------------------------------------------------------------
# FLUID MECHANICS (FM)
# ---------------------------------------------------------------------------

"FM1": (
    "The Navier-Stokes equation states that mass times acceleration (left side: rho times "
    "partial u / partial t plus u dot gradient u) equals the sum of pressure gradient force "
    "minus nabla P, viscous diffusion mu times the Laplacian of u, and body forces f. The "
    "nonlinear convective acceleration term u dot nabla u makes the equations extremely "
    "difficult to solve analytically and is the source of turbulence. The incompressibility "
    "condition nabla dot u equals zero closes the system. Whether smooth solutions always "
    "exist in three dimensions for all initial conditions is one of the seven Millennium "
    "Prize Problems — worth one million dollars and unsolved as of 2024."
),

"FM2": (
    "Bernoulli's principle states that for an ideal (inviscid, incompressible, steady) fluid "
    "flowing along a streamline, the sum of static pressure P, dynamic pressure one-half rho "
    "v-squared, and hydrostatic pressure rho g h is constant. Higher velocity means lower "
    "static pressure — faster flow creates lower lateral pressure. This explains aerodynamic "
    "lift (faster airflow over a wing's upper surface creates lower pressure, net upward "
    "force), Venturi meters (flow accelerates through a constriction, pressure drops), and "
    "the Bernoulli effect in atomizers. The principle is an energy conservation statement: "
    "kinetic, pressure, and gravitational potential energies trade off along the streamline."
),

"FM3": (
    "Euler's fluid equations are the Navier-Stokes equations without the viscous term: rho "
    "times (partial u / partial t plus u dot nabla u) equals minus nabla P plus body force f. "
    "They describe inviscid (zero viscosity) fluid flow and are valid where viscous effects "
    "are negligible — far from boundaries and at high Reynolds numbers. Euler's equations "
    "conserve kinetic and pressure energy but allow shock waves (discontinuities) because "
    "without viscosity there is no mechanism to smooth them. They are the foundation of "
    "inviscid aerodynamics and acoustic propagation."
),

"FM4": (
    "The volumetric flow rate Q through a circular pipe of radius r and length L under "
    "pressure difference delta-P equals pi times r to the fourth times delta-P divided by "
    "(8 times dynamic viscosity eta times L). The dramatic r-to-the-fourth dependence means "
    "halving the pipe radius reduces flow 16-fold at the same pressure. This is why "
    "arteriosclerotic narrowing of arteries is so catastrophically effective at reducing "
    "blood flow — a 50 percent radius reduction gives only 6 percent of original flow. "
    "Poiseuille's law assumes laminar (non-turbulent) flow, Newtonian fluid, no-slip "
    "boundary conditions, and fully developed steady flow — conditions approximately met "
    "in small blood vessels but violated in large arteries."
),

"FM5": (
    "Stokes' drag law gives the viscous drag force on a sphere of radius r moving at velocity "
    "v through a fluid of dynamic viscosity eta: F_drag equals 6 pi eta r v. The linear "
    "velocity dependence (as opposed to v-squared for turbulent drag) holds at low Reynolds "
    "numbers Re equals rho v r / eta much less than 1, where viscous forces dominate inertia. "
    "This regime applies to small particles, microorganisms, and slow settling in viscous "
    "media. Terminal settling velocity of a sphere is v_t equals 2 r-squared times (rho_particle "
    "minus rho_fluid) times g divided by (9 eta), obtained by balancing Stokes drag against "
    "gravitational force minus buoyancy."
),

"FM6": (
    "Faxén's law extends Stokes' drag to non-uniform flow fields. The force on a sphere "
    "in background flow u_infinity is F equals 6 pi eta r times (u_infinity plus r-squared "
    "over 6 times the Laplacian of u_infinity, minus the particle velocity v_particle). The "
    "Laplacian correction accounts for the curvature of the velocity field — the sphere "
    "responds not just to the local background velocity but to the average of the background "
    "velocity over a sphere of radius r. This matters when velocity gradients are comparable "
    "to particle size, such as particles in shear flows, near walls, or in focused microfluidic "
    "channels."
),

# ---------------------------------------------------------------------------
# GAS LAWS (GL)
# ---------------------------------------------------------------------------

"GL1": (
    "The ideal gas law PV equals nRT relates pressure P, volume V, moles n, and temperature "
    "T through the universal gas constant R approximately 8.314 joules per mole per kelvin. "
    "At fixed T and n, pressure and volume are inversely proportional (Boyle's law). At fixed "
    "P and n, volume is proportional to temperature (Charles's law). At fixed V and n, "
    "pressure is proportional to temperature (Gay-Lussac's law). The law assumes molecules "
    "occupy zero volume and exert no intermolecular forces — good approximations for real "
    "gases at low pressure and high temperature, failing near phase transitions or at high "
    "densities."
),

"GL2": (
    "Boyle's law states that at constant temperature and fixed amount of gas, pressure and "
    "volume are inversely proportional: P_1 V_1 equals P_2 V_2. Doubling pressure halves "
    "volume; halving pressure doubles volume. This follows from the ideal gas assumption: "
    "molecules exert no intermolecular attractions, so compression increases their collision "
    "rate with the walls proportionally. Deviations from Boyle's law at high pressure signal "
    "significant intermolecular interactions or finite molecular volume, captured by the "
    "van der Waals equation."
),

"GL3": (
    "Charles's law states that at constant pressure and fixed amount of gas, volume is "
    "proportional to absolute temperature: V_1 divided by T_1 equals V_2 divided by T_2. "
    "Heating a gas at constant pressure makes it expand; cooling makes it contract. At "
    "absolute zero the extrapolated volume reaches zero — defining the Kelvin temperature "
    "scale's zero point. The law follows from kinetic theory: higher temperature means higher "
    "average molecular speed and more frequent wall collisions, requiring more volume at "
    "constant pressure to maintain the same force per area."
),

"GL4": (
    "Gay-Lussac's law states that at constant volume and fixed amount of gas, pressure is "
    "proportional to absolute temperature: P_1 divided by T_1 equals P_2 divided by T_2. "
    "Heating a sealed container increases pressure proportionally; cooling decreases it. "
    "The law explains why aerosol cans warn against high temperatures — sealed volume combined "
    "with temperature increase raises pressure, risking rupture. It follows directly from the "
    "kinetic theory: higher temperature means molecules hit the walls faster and more "
    "frequently, increasing pressure at fixed volume."
),

"GL5": (
    "Avogadro's law states that at constant temperature and pressure, equal volumes of "
    "different ideal gases contain equal numbers of molecules: V divided by n equals R T "
    "divided by P equals constant. One mole of any ideal gas at standard temperature and "
    "pressure occupies approximately 22.4 liters. The law implies that gas volume directly "
    "measures the number of moles, making it the experimental basis for determining molar "
    "masses from gas density measurements. Avogadro's hypothesis was crucial for reconciling "
    "Dalton's atomic theory with Gay-Lussac's experimental observations on combining volumes "
    "of gases in reactions."
),

# ---------------------------------------------------------------------------
# GRAVITATION (GV)
# ---------------------------------------------------------------------------

"GV1": (
    "The Einstein field equations equate the curvature of spacetime (left side) to the "
    "energy-momentum content of matter and radiation (right side). The Ricci curvature tensor "
    "R-mu-nu captures how much volume changes in curved space; the metric tensor g-mu-nu "
    "encodes distances and time intervals; R is the Ricci scalar (trace of curvature); "
    "Lambda is the cosmological constant representing dark energy's contribution; and T-mu-nu "
    "is the stress-energy tensor containing energy density, pressure, and momentum flux. "
    "The coefficient 8 pi G divided by c-to-the-fourth converts between geometrical curvature "
    "units and energy-momentum units. The equations are ten coupled nonlinear partial "
    "differential equations — vastly more complex than Newton's single scalar equation."
),

"GV2": (
    "In the weak-field, slow-motion limit of general relativity, the gravitational field "
    "equations take a Maxwell-like form. The gravitoelectric law (nabla dot g equals minus "
    "4 pi G rho) parallels Gauss's electric law but with a minus sign reflecting gravity's "
    "purely attractive nature — all mass has the same sign, unlike electric charges. The "
    "gravitomagnetic component (nabla cross B_g) describes frame-dragging effects around "
    "rotating masses. GEM equations predict the Lense-Thirring effect (gyroscope precession "
    "near rotating bodies), which was confirmed by Gravity Probe B in 2011. GEM is valid "
    "only in the weak-field approximation and breaks down in strong gravitational fields."
),

"GV3": (
    "Newtonian gravitational Gauss's law states that the divergence of the gravitational "
    "acceleration field g equals minus 4 pi G times mass density rho. In integral form, the "
    "total gravitational flux through a closed surface equals minus 4 pi G times the total "
    "mass enclosed. The minus sign reflects that gravity is attractive — field lines point "
    "inward toward mass. For spherically symmetric mass distributions, the field outside "
    "depends only on the total enclosed mass, not on its internal distribution. This shell "
    "theorem (a uniform spherical shell exerts no interior force) follows directly from "
    "Gauss's law and makes planetary orbit calculations tractable."
),

# ---------------------------------------------------------------------------
# CHEMISTRY / KINETICS (KC)
# ---------------------------------------------------------------------------

"KC1": (
    "Le Chatelier's principle states that a system at chemical equilibrium (where Gibbs free "
    "energy G is at a minimum and dG equals zero) responds to any perturbation by shifting "
    "in the direction that partially opposes the perturbation. Adding reactants shifts the "
    "equilibrium toward products; increasing pressure for a gas-phase reaction shifts toward "
    "the side with fewer moles; increasing temperature shifts in the endothermic direction "
    "because that direction absorbs heat and partly counteracts the temperature increase. "
    "The principle is qualitative — it predicts the direction of shift but not the magnitude. "
    "It follows from the thermodynamic requirement that G is minimized at equilibrium."
),

"KC2": (
    "The principle of microscopic reversibility states that at equilibrium, the forward rate "
    "of each elementary reaction step exactly equals its reverse rate: k_forward times "
    "[A][B] equals k_reverse times [C][D] for elementary reaction A plus B ⇌ C plus D. "
    "This detailed balance condition prevents equilibrium from being sustained by a cyclic "
    "sequence of irreversible steps — a mechanism that would constitute a perpetual motion "
    "machine. The principle follows from the time-reversal symmetry of the underlying "
    "microscopic equations of motion and is equivalent to the thermodynamic requirement that "
    "the equilibrium constant K equals k_forward divided by k_reverse."
),

"KC3": (
    "The Hammond-Leffler postulate relates transition state structure to reaction "
    "thermodynamics: for an exothermic reaction the transition state resembles the reactants "
    "(early transition state, delta-dagger approximately 0) while for an endothermic reaction "
    "it resembles the products (late transition state, delta-dagger approximately 1). This "
    "means substituents that stabilize products also lower the activation energy for "
    "endothermic reactions, but have little effect on exothermic ones. The postulate "
    "connects thermodynamics (delta-H) to kinetics (activation energy E_a) and allows "
    "prediction of how structural changes affect reaction rates by assessing their effect "
    "on overall thermodynamics."
),

"KC4": (
    "Hess's law states that the total enthalpy change for a chemical reaction is the sum "
    "of enthalpy changes for any sequence of steps connecting the same initial and final "
    "states: delta-H_total equals the sum of delta-H for each step. Enthalpy is a state "
    "function — it depends only on the initial and final states, not on the path. This "
    "allows the enthalpy of reactions that are difficult or impossible to measure directly "
    "(decomposition of diamond, formation of very reactive species) to be calculated "
    "algebraically from easily measured reactions. Standard enthalpies of formation are "
    "tabulated precisely because Hess's law lets them be combined to predict any reaction "
    "enthalpy."
),

"KC5": (
    "The Gibbs-Helmholtz equation relates the temperature dependence of Gibbs free energy G "
    "to enthalpy H: the partial derivative of (delta-G divided by T) with respect to T at "
    "constant pressure equals minus delta-H divided by T-squared. This connects the "
    "temperature sensitivity of thermodynamic spontaneity (dG) to the heat of reaction (H). "
    "For exothermic reactions (H negative), G decreases as temperature increases — the "
    "reaction becomes less favorable with heat. For endothermic reactions (H positive), G "
    "decreases as temperature increases — heating favors the reaction. Integration gives the "
    "van't Hoff equation for how equilibrium constants change with temperature."
),

"KC6": (
    "Raoult's law states that the partial vapor pressure P_A of component A above an ideal "
    "solution equals its mole fraction x_A times its pure-component vapor pressure P-zero_A: "
    "P_A equals x_A times P-zero_A. A component diluted to half its mole fraction contributes "
    "half the vapor pressure. Raoult's law defines an ideal solution and holds when the "
    "interactions between unlike molecules equal those between like molecules. Deviations "
    "from Raoult's law — positive (actual P higher than predicted, weaker unlike interactions) "
    "or negative (actual P lower, stronger unlike interactions) — reveal intermolecular "
    "interaction asymmetries. The law is the basis for calculating boiling point elevation "
    "and freezing point depression."
),

"KC7": (
    "Henry's law states that the dissolved concentration C of a gas in a liquid is "
    "proportional to the partial pressure P of that gas above the liquid: C equals k_H "
    "times P, where k_H is the Henry's law constant (units of mol/L/atm or similar). Higher "
    "gas pressure forces more gas into solution; the dissolved concentration rises proportionally. "
    "This explains why carbonated drinks release CO_2 when the cap is removed (pressure drops, "
    "dissolved CO_2 exceeds saturation), why divers must ascend slowly (N_2 dissolved under "
    "high pressure must leave solution gradually to avoid bubbles), and why oxygen delivery "
    "to tissues scales with partial pressure."
),

"KC8": (
    "The law of definite composition (constant composition) states that every sample of a "
    "pure chemical compound contains the same elements combined in the same fixed mass "
    "fractions, regardless of the compound's origin or method of preparation. Water always "
    "contains 8 grams of oxygen for every 1 gram of hydrogen by mass. This fixed mass "
    "fraction is the consequence of atoms combining in fixed small-integer mole ratios "
    "determined by the molecular formula. The law distinguished pure compounds from mixtures "
    "(which have variable composition) and was the empirical foundation for Dalton's atomic "
    "theory of matter."
),

"KC9": (
    "Dalton's law of multiple proportions states that when two elements form more than one "
    "compound, the masses of one element that combine with a fixed mass of the other are in "
    "simple integer ratios. Carbon monoxide and carbon dioxide both contain carbon and oxygen: "
    "in CO the ratio is 12:16 and in CO_2 it is 12:32, so the oxygen masses are in ratio "
    "1:2 for the same mass of carbon. These integer ratios imply that atoms combine in "
    "whole-number ratios, providing strong evidence for the existence of discrete atomic "
    "units. The law distinguishes compounds from mixtures and was key evidence for Dalton's "
    "atomic theory."
),

"KC10": (
    "The law of reciprocal proportions states that if element A combines separately with "
    "both element B and element C, then B and C will combine with each other in masses that "
    "are simple multiples of the masses in which they individually combine with A. The "
    "principle interconnects the combining weights of all elements in a network of reactions, "
    "making the entire system of equivalent weights consistent. It was essential to the "
    "establishment of a consistent atomic mass scale in the early nineteenth century by "
    "allowing atomic masses to be triangulated across multiple pairs of reacting elements."
),

# ---------------------------------------------------------------------------
# OPTICS (OP)
# ---------------------------------------------------------------------------

"OP1": (
    "Fermat's principle states that light travels between two points along the path that "
    "minimizes (or stationary-izes) the optical path length delta integral of n(r) ds, where "
    "n(r) is the refractive index and s is the path length. In a uniform medium where n is "
    "constant, the minimum path is a straight line. At an interface between media with "
    "different n, the minimum-time path requires bending at an angle described by Snell's "
    "law. Reflection also follows: the angle of incidence equals the angle of reflection "
    "because this gives the minimum round-trip path from source to mirror to receiver. "
    "Fermat's principle is the optical analog of Hamilton's principle of least action in "
    "mechanics."
),

"OP2": (
    "The law of reflection states that the angle of incidence theta_i equals the angle of "
    "reflection theta_r, both measured from the surface normal at the point of incidence, "
    "and that the incident ray, reflected ray, and surface normal are all coplanar. This "
    "holds for all wavelengths, all angles, and all reflecting surfaces (rough or smooth, "
    "metallic or dielectric). The law follows from the boundary condition that the tangential "
    "component of the wave vector is conserved upon reflection (no momentum transfer parallel "
    "to the surface), combined with the constraint that the reflected wave travels away "
    "from the surface."
),

"OP3": (
    "Snell's law states that the product of refractive index n and sine of the angle from "
    "the normal theta is conserved across an optical interface: n_1 sin(theta_1) equals n_2 "
    "sin(theta_2). Light bends toward the normal when entering a denser medium (n_2 greater "
    "than n_1) and away when entering a less dense medium. Total internal reflection occurs "
    "when n_1 sin(theta_1) equals or exceeds n_2 — no refracted ray can satisfy the equation "
    "and all light reflects. Fiber optic cables exploit total internal reflection to transmit "
    "light around bends. Snell's law follows from the requirement that the tangential "
    "component of the wave vector is continuous across the interface."
),

"OP4": (
    "Brewster's angle theta_B is the angle of incidence at which reflected light is completely "
    "s-polarized (no p-polarization reflected): tan(theta_B) equals n_2 divided by n_1. At "
    "this specific angle the reflected and refracted rays are perpendicular — p-polarized "
    "oscillations aligned with the reflected direction cannot radiate, so they all transmit "
    "rather than reflect. Polarizing sunglasses exploit this: glare from horizontal surfaces "
    "such as water or roads is predominantly s-polarized (vibrating horizontally), which "
    "the vertically oriented polarizer blocks. Brewster's angle is used in laser windows "
    "(Brewster windows) to minimize reflection losses for a specific polarization."
),

"OP5": (
    "Malus's law states that when plane-polarized light of intensity I_0 passes through a "
    "polarizer whose transmission axis makes angle theta with the polarization direction, "
    "the transmitted intensity is I_0 times cosine-squared of theta. At theta equals zero "
    "all light passes; at theta equals 90 degrees (crossed polarizers) no light passes. "
    "The cosine-squared dependence arises because the electric field amplitude transmitted "
    "is proportional to cos(theta) (projection of the field onto the transmission axis) "
    "and intensity is proportional to the square of the field amplitude. Inserting a third "
    "polarizer at 45 degrees between two crossed polarizers allows one-quarter of the "
    "original intensity through."
),

"OP6": (
    "The Beer-Lambert law states that the intensity of light transmitted through an absorbing "
    "medium of thickness l is I_0 times the exponential of minus alpha times l, where alpha "
    "is the absorption coefficient. In the Beer's law form for solutions, alpha equals molar "
    "absorptivity epsilon times concentration c. Absorbance A equals log(I_0 divided by I) "
    "is proportional to both c and l. This is the basis of spectrophotometry — measuring "
    "solute concentration from transmitted light intensity. The exponential form means each "
    "layer of the same thickness absorbs the same fraction of remaining light (not the same "
    "absolute amount). The law assumes each absorbing molecule acts independently, failing "
    "at high concentrations where molecular interactions modify absorption."
),

# ---------------------------------------------------------------------------
# RADIATION (RD)
# ---------------------------------------------------------------------------

"RD1": (
    "Planck's law gives the spectral energy density of blackbody radiation: u(nu, T) equals "
    "(8 pi h nu-cubed divided by c-cubed) times 1 divided by (exp(h nu divided by k_B T) "
    "minus 1). The exponential-minus-1 denominator is the Bose-Einstein distribution for "
    "photons — the quantum statistics of bosons. At low frequencies (h nu much less than "
    "k_B T), the denominator approximates h nu divided by k_B T and the spectrum reduces "
    "to the classical Rayleigh-Jeans law proportional to nu-squared times T. At high "
    "frequencies, the exponential denominator falls off rapidly (quantum cutoff), preventing "
    "the ultraviolet catastrophe. Integrating Planck's law over all frequencies gives the "
    "Stefan-Boltzmann law."
),

"RD2": (
    "The Stefan-Boltzmann law states that the total power radiated per unit area by a "
    "blackbody is sigma times T to the fourth power, where sigma approximately 5.67 times "
    "10 to the minus 8 W per m-squared per K-to-the-fourth. Total radiation increases as "
    "the fourth power of absolute temperature — doubling temperature increases total "
    "radiation 16-fold. This strong temperature dependence makes radiation the dominant "
    "heat transfer mechanism at high temperatures. The Stefan-Boltzmann constant sigma "
    "equals 2 pi to the fifth times k_B to the fourth divided by (15 h-cubed c-squared) — "
    "a combination of fundamental constants. Real surfaces radiate epsilon times sigma T-fourth "
    "where emissivity epsilon is less than or equal to 1."
),

"RD3": (
    "The Planck-Einstein relation states that the energy of a photon or quantum oscillator "
    "is E equals h times frequency nu equals h-bar times angular frequency omega, where h "
    "is Planck's constant approximately 6.626 times 10 to the minus 34 J·s and h-bar "
    "equals h divided by 2 pi. Higher-frequency light (ultraviolet, X-ray) carries more "
    "energy per photon; lower-frequency light (infrared, radio) carries less. This quantization "
    "was Planck's 1900 hypothesis to explain blackbody spectra and Einstein's 1905 explanation "
    "of the photoelectric effect — a photon below a threshold frequency cannot eject an "
    "electron regardless of beam intensity because individual photons lack the energy. "
    "The relation is the seed from which quantum mechanics grew."
),

# ---------------------------------------------------------------------------
# QUANTUM MECHANICS (QM)
# ---------------------------------------------------------------------------

"QM1": (
    "The Schrödinger equation governs the time evolution of a quantum state: i times h-bar "
    "times the time derivative of the state |psi> equals the Hamiltonian operator H-hat "
    "acting on |psi>. The equation is linear — superposition of solutions is a solution — "
    "encoding the quantum principle of superposition. In position space, the wavefunction "
    "psi(x, t) satisfies the equation and |psi|^2 gives the probability density. Energy "
    "eigenstates H-hat |n> equals E_n |n> are stationary — their probability distributions "
    "do not change in time. The equation is first-order in time (deterministic, reversible) "
    "until measurement collapses the wavefunction to an eigenstate."
),

"QM2": (
    "The Heisenberg uncertainty principle states that the product of standard deviations of "
    "position and momentum is at least h-bar divided by 2: delta-x times delta-p is greater "
    "than or equal to h-bar over 2. This is not a limitation of measurement precision but "
    "a fundamental property of wave-like objects: a sharply localized wavepacket (small "
    "delta-x) requires a wide spread of wavelengths (large delta-p equals h-bar times "
    "delta-k). The time-energy uncertainty delta-E times delta-t greater than or equal to "
    "h-bar over 2 has a different interpretation — a quantum state that lives for time delta-t "
    "has an energy spread of at least h-bar divided by delta-t, giving spectral linewidths. "
    "Both relations arise from the Fourier transform relationship between conjugate variables."
),

"QM3": (
    "The Pauli exclusion principle states that the wavefunction of a system of identical "
    "fermions (particles with half-integer spin) is antisymmetric under exchange of any "
    "two particles: psi(...r_i...r_j...) equals minus psi(...r_j...r_i...). Swapping two "
    "identical fermions negates the wavefunction; if any two are in the same state the "
    "wavefunction equals its own negative and must be zero — no two fermions can share the "
    "same quantum state. This explains atomic structure (electrons fill distinct energy "
    "levels and orbitals), the stability of ordinary matter (electrons cannot all collapse "
    "to the nucleus), the periodic table (shell filling from the exclusion principle), and "
    "the existence of neutron stars and white dwarfs (degeneracy pressure)."
),

"QM4": (
    "The de Broglie relation assigns a wavelength lambda equals h divided by momentum p to "
    "every particle: matter has wave properties with wavelength inversely proportional to "
    "momentum. Equivalently, momentum p equals h-bar times the wave vector k. For an electron "
    "with energy of a few electron-volts, lambda is on the order of an Angstrom — comparable "
    "to atomic spacings, enabling electron diffraction through crystals. For a macroscopic "
    "object (1 gram at 1 cm/s), lambda is approximately 7 times 10 to the minus 29 meters — "
    "utterly negligible. Wave-particle duality predicted by de Broglie was confirmed by the "
    "Davisson-Germer experiment (1927) showing electron diffraction through a nickel crystal."
),

"QM5": (
    "Einstein's two postulates — that the laws of physics are identical in all inertial "
    "reference frames, and that the speed of light c is the same in all inertial frames "
    "regardless of source or observer motion — require that space and time coordinates mix "
    "under changes of reference frame. The Lorentz transformation A-prime equals Lambda "
    "times A mixes time and space in a way that preserves c. Consequences include: time "
    "dilation (a moving clock runs slow by the Lorentz factor gamma equals 1 divided by "
    "square root of 1 minus v-squared over c-squared); length contraction (moving objects "
    "are shorter by a factor 1/gamma); and energy-momentum relation E-squared equals "
    "(pc)-squared plus (mc-squared)-squared, unifying energy and mass."
),

# ---------------------------------------------------------------------------
# THERMODYNAMICS (TD)
# ---------------------------------------------------------------------------

"TD1": (
    "The zeroth law states that thermal equilibrium is transitive: if body A is in thermal "
    "equilibrium with B, and B with C, then A is in thermal equilibrium with C. This "
    "seemingly obvious statement is the logical prerequisite for temperature to be a well- "
    "defined scalar quantity — it establishes that temperature is a consistent label that "
    "can be assigned to each state. Without transitivity, a thermometer could read differently "
    "when touching two bodies that are in equilibrium with each other. The zeroth law makes "
    "temperature a state function and justifies thermometry."
),

"TD2": (
    "The first law states that the internal energy U of a closed system changes by the "
    "difference between heat absorbed delta-Q and work done by the system delta-W: dU "
    "equals delta-Q minus delta-W. Energy is conserved — heat added goes either into "
    "changing internal energy (heating the system) or into work done by the system. For a "
    "gas, work done equals P times dV. The law implies perpetual motion machines of the "
    "first kind (creating energy from nothing) are impossible. For open systems, a chemical "
    "potential term sum of mu_i dN_i adds the energy carried by particles entering or leaving."
),

"TD3": (
    "The second law states that the total entropy S of an isolated system never decreases: "
    "delta-S is greater than or equal to zero, with equality for reversible processes. "
    "Boltzmann's entropy formula S equals k_B times ln(Omega), where Omega is the number "
    "of microscopic configurations consistent with the macroscopic state, connects entropy "
    "to statistical mechanics. Systems evolve toward states with more configurations because "
    "there are simply more ways to be disordered. The law establishes the arrow of time — "
    "entropy increase distinguishes the future from the past. Perpetual motion machines of "
    "the second kind (extracting work from a single temperature reservoir) are impossible."
),

"TD4": (
    "The third law states that as absolute temperature T approaches zero, the entropy S of "
    "a perfect crystal with a unique ground state approaches zero: S approaches 0 as T "
    "approaches 0. This establishes an absolute entropy scale rather than one defined only "
    "by differences. The law implies that absolute zero is unattainable in finite steps — "
    "each cooling step removes progressively less entropy and temperature approaches zero "
    "asymptotically. It also requires that heat capacities vanish as T tends to zero "
    "(otherwise integrating C/T to get entropy change would diverge)."
),

"TD5": (
    "The fundamental thermodynamic relation dU equals T dS minus P dV plus sum of mu_i dN_i "
    "combines the first and second laws into a single differential equation for internal "
    "energy U as a function of entropy S, volume V, and particle numbers N_i. The temperature "
    "T equals partial U / partial S at constant V and N (temperature is the entropy-based "
    "rate of energy change); pressure P equals minus partial U / partial V at constant S "
    "and N; chemical potential mu_i equals partial U / partial N_i at constant S, V. All "
    "thermodynamic potentials — Helmholtz, Gibbs, enthalpy — derive from this relation by "
    "Legendre transforms that swap which variable (S, V, or N) is held constant."
),

"TD6": (
    "Near thermodynamic equilibrium, fluxes J_i (heat current, electric current, diffusion "
    "flux) are linear combinations of all driving forces X_j (temperature gradient, voltage "
    "gradient, concentration gradient): J_i equals sum over j of L_ij times X_j. The "
    "Onsager reciprocal relations state that the coupling coefficient matrix L_ij is "
    "symmetric: L_ij equals L_ji. This symmetry means the coupling from thermal gradient "
    "to electric current (Seebeck coefficient) equals the coupling from electric potential "
    "gradient to heat current (Peltier coefficient). The relations follow from microscopic "
    "time-reversal symmetry and reduce the number of independent transport coefficients "
    "that must be measured."
),

"TD7": (
    "The Boltzmann transport equation describes the evolution of the phase-space distribution "
    "function f(r, p, t) — the probability density of finding a particle at position r with "
    "momentum p at time t. The left side combines streaming (free flight at velocity p/m) "
    "and external force terms. The right side is the collision integral C[f] — a functional "
    "of f that describes how collisions between particles relax f toward local equilibrium. "
    "In the relaxation time approximation, C[f] equals minus (f minus f_eq) divided by tau. "
    "The H-theorem shows the entropy functional H equals minus integral of f ln(f) dp "
    "never decreases, deriving the second law from kinetic theory."
),

"TD8": (
    "Carnot's theorem states that no heat engine operating between a hot reservoir at T_hot "
    "and a cold reservoir at T_cold can be more efficient than the reversible Carnot cycle: "
    "maximum efficiency eta equals 1 minus T_cold divided by T_hot. The Carnot cycle consists "
    "of two isothermal steps (absorbing and rejecting heat at fixed temperature) and two "
    "adiabatic steps (changing temperature without heat exchange), making it perfectly "
    "reversible. All real engines are irreversible and less efficient. The theorem establishes "
    "that thermodynamic temperature is the absolute scale — the ratio of heat absorbed to "
    "heat rejected by a Carnot engine equals the ratio of temperatures."
),

"TD9": (
    "Newton's law of cooling states that the rate of heat loss from a body is proportional "
    "to the temperature difference between the body and its surroundings: dT/dt equals "
    "minus k times (T minus T_environment), where k equals h A divided by (m c_p) for heat "
    "transfer coefficient h, surface area A, mass m, and specific heat c_p. The solution "
    "is exponential decay: T(t) minus T_env equals (T_0 minus T_env) times exp(minus k t). "
    "The law is an approximation valid for forced convection where h is roughly independent "
    "of temperature difference; for natural convection h increases with temperature difference "
    "and the decay is non-exponential."
),

"TD10": (
    "Fourier's law of heat conduction states that heat flux q (power per unit area) equals "
    "minus thermal conductivity k times the temperature gradient nabla-T: heat flows from "
    "hot to cold at a rate proportional to the steepness of the temperature gradient. The "
    "minus sign means heat flows downhill in temperature. The heat equation, derived by "
    "combining Fourier's law with energy conservation, states partial T / partial t equals "
    "thermal diffusivity alpha times the Laplacian of T. Solutions show temperature "
    "disturbances spreading diffusively — the characteristic diffusion distance grows as "
    "the square root of time, the same as particle diffusion but for thermal energy."
),

"TD11": (
    "Kopp's law states that the molar heat capacity at constant volume of a solid compound "
    "approximately equals the sum of the molar heat capacities of its constituent elements "
    "in their standard states. For a compound A_m B_n, the molar heat capacity C "
    "approximately equals m times C_A plus n times C_B. The additivity reflects the "
    "equipartition theorem applied independently to each atom: each atom contributes 3R to "
    "the heat capacity through its three vibrational modes (three kinetic plus three potential "
    "energy degrees of freedom). Kopp's law is approximate and breaks down for light elements "
    "(H, B, C) at moderate temperatures and for all elements at low temperatures where "
    "quantum effects suppress heat capacity below the equipartition limit."
),

"TD12": (
    "The Dulong-Petit law states that the molar heat capacity at constant volume of a "
    "monatomic solid approaches 3R approximately 24.9 joules per mol per kelvin at high "
    "temperatures, where R is the universal gas constant. The factor 3R comes from the "
    "equipartition theorem: each atom is a harmonic oscillator with three spatial dimensions, "
    "each contributing kB T / 2 to kinetic energy and kB T / 2 to potential energy, for "
    "total 3 kB T per atom equals 3R per mole. At low temperatures quantum effects cause "
    "heat capacity to fall well below 3R as vibrational modes (phonons) freeze out — the "
    "Einstein and Debye models correctly predict this quantum suppression."
),

"TD13": (
    "Carnot's theorem defines thermodynamic temperature via the heat exchange ratio of a "
    "reversible Carnot cycle: the ratio T_cold divided by T_hot equals Q_cold divided by "
    "Q_hot, where Q_cold is heat rejected to the cold reservoir and Q_hot is heat absorbed "
    "from the hot reservoir. This identifies absolute thermodynamic temperature as the "
    "variable whose ratio equals the heat exchange ratio for a reversible engine — making "
    "temperature an operationally defined thermodynamic quantity independent of any specific "
    "thermometric substance. The Carnot efficiency eta equals 1 minus T_cold over T_hot "
    "sets the maximum fraction of heat convertible to work and increases toward 1 as "
    "T_cold approaches 0."
),

}  # end PROSE dict


# ===========================================================================
# INSERT LOGIC
# ===========================================================================

SECTION_NAME = "What The Math Says"

def get_entries_with_math(conn: sqlite3.Connection) -> list[tuple[str, str]]:
    """Return (entry_id, section_name) for all entries that have a math section."""
    cur = conn.execute("""
        SELECT e.id, s.section_name
        FROM entries e
        JOIN sections s ON s.entry_id = e.id
        WHERE s.section_name IN ('Mathematical Form', 'Formula', 'Symbology')
        ORDER BY e.id
    """)
    return cur.fetchall()


def run(db_path: str, dry_run: bool = False):
    print(f"DB: {db_path}")
    conn = sqlite3.connect(db_path)

    entries_with_math = get_entries_with_math(conn)
    entry_ids_with_math = {eid for eid, _ in entries_with_math}

    # Check coverage
    covered = {eid for eid in entry_ids_with_math if eid in PROSE}
    missing = entry_ids_with_math - covered
    extra = set(PROSE.keys()) - entry_ids_with_math  # prose defined but no math section

    print(f"Entries with math sections : {len(entry_ids_with_math)}")
    print(f"Prose entries defined       : {len(PROSE)}")
    print(f"Covered (will insert)       : {len(covered)}")
    if missing:
        print(f"WARNING — no prose for {len(missing)} entries: {sorted(missing)}")
    if extra:
        print(f"NOTE    — prose defined but no math section for: {sorted(extra)}")

    # Get max section order per entry
    max_order_cur = conn.execute("""
        SELECT entry_id, MAX(section_order) FROM sections GROUP BY entry_id
    """)
    max_order = dict(max_order_cur.fetchall())

    # Build insert payload
    rows = []
    for entry_id in sorted(covered):
        prose_text = PROSE[entry_id]
        order = (max_order.get(entry_id) or 0) + 1
        rows.append((entry_id, SECTION_NAME, prose_text, order))

    print(f"\nSection rows to insert: {len(rows)}")

    if dry_run:
        print("\nDRY RUN — What The Math Says prose sections")
        print(f"  Would insert: {len(rows)} 'What The Math Says' sections")
        print(f"  Sample (first 3):")
        for eid, sname, text, order in rows[:3]:
            print(f"    [{eid}] {sname} (order {order}) — {text[:80]}...")
        conn.close()
        return

    # Live insert
    inserted = 0
    skipped = 0
    errors = 0
    cur = conn.cursor()

    for entry_id, section_name, content, order in rows:
        try:
            cur.execute("""
                INSERT OR IGNORE INTO sections
                    (entry_id, section_name, content, section_order)
                VALUES (?, ?, ?, ?)
            """, (entry_id, section_name, content, order))
            if cur.rowcount:
                inserted += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"ERROR [{entry_id}]: {e}")
            errors += 1

    conn.commit()
    conn.close()

    print(f"\nPhase 2 'What The Math Says' insertion complete")
    print(f"  Sections inserted : {inserted}")
    print(f"  Skipped (existed) : {skipped}")
    print(f"  Errors            : {errors}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 2: Add 'What The Math Says' prose sections")
    parser.add_argument("--dry-run", action="store_true", help="Preview without inserting")
    args = parser.parse_args()
    run(SOURCE_DB, dry_run=args.dry_run)

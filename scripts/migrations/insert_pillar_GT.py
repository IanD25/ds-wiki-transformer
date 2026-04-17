"""
Pillar Extension — Gravity from Thermodynamics (GT)
Inserts 7 new entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Skipped: GT07 (Einstein Field Equations = GV1 already exists)

Entries:
  GT01: Jacobson's Thermodynamic Derivation of Einstein Equations
  GT02: Verlinde Entropic Gravity
  GT03: Padmanabhan Holographic Equipartition
  GT04: Bianconi Gravity from Entropy
  GT05: Carney Spin Entropic Gravity
  GT06: Sakharov Induced Gravity
  GT08: Equivalence Principle
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── GRAVITY FROM THERMODYNAMICS ────────────────────────────────────────────

{
    "id": "GT01",
    "title": "Jacobson's Thermodynamic Derivation of Einstein Equations",
    "filename": "GT01_jacobson_derivation.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Jacobson showed that the Einstein field equations of general relativity can be derived from the proportionality of entropy to horizon area, combined with the Clausius relation δQ = TdS, applied to all local causal horizons (Jacobson, PRL 75, 1260, 1995). The derivation treats the Einstein equations not as fundamental laws of gravity but as an equation of state — a thermodynamic identity relating heat flow, temperature, and entropy at every point in spacetime. The key inputs are: (1) the Unruh temperature T = ℏa/2πck_B for accelerating observers near a local Rindler horizon, and (2) the entropy-area proportionality δS = ηδA where η = 1/4l_P². The heat flux δQ is identified with the energy flux of matter crossing the horizon via the Raychaudhuri equation. From these thermodynamic ingredients alone, the Einstein equations emerge as a consistency condition. This is the founding result of the gravity-from-thermodynamics programme: it shows that gravity may not be a fundamental force but rather an emergent thermodynamic phenomenon."),
        ("Mathematical Form", 1,
         "Clausius relation: δQ = T dS\n\nInputs:\n  T = ℏa/2πck_B  (Unruh temperature)\n  dS = η dA = (1/4l_P²) dA  (entropy-area proportionality)\n  δQ = T_ab k^a dΣ^b  (heat flux through horizon, via Raychaudhuri)\n\nOutput:\n  R_ab − ½g_ab R + Λg_ab = (8πG/c⁴) T_ab  (Einstein field equations)\n\nThe cosmological constant Λ appears as an integration constant."),
        ("Constraint Category", 2,
         "Thermodynamic-Geometric (Th-Gm): Jacobson's derivation reveals that the Einstein equations are a thermodynamic constraint — the geometric content (curvature) equals the thermodynamic content (entropy production) at every point. This is not an analogy: it is an exact mathematical derivation. The constraint has both thermodynamic content (entropy, temperature, heat) and geometric content (curvature, area, horizons)."),
        ("DS Cross-References", 3,
         "HB02 (Bekenstein-Hawking Entropy — the entropy-area relation S = A/4l_P² is the key input to Jacobson's derivation). HB05 (Unruh Effect — the Unruh temperature T = ℏa/2πck_B provides the local temperature for each accelerating observer). GV1 (Einstein Field Equations — the output of the derivation; Jacobson derives GV1 from thermodynamics). GT02 (Verlinde Entropic Gravity — Verlinde extends Jacobson's approach to derive Newton's law of gravity as an entropic force). GT04 (Bianconi Gravity from Entropy — Bianconi extends to quantum regime, using quantum relative entropy and Fisher information). TD3 (Second Law — the Clausius relation δQ = TdS is a consequence of the second law applied locally)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nJacobson's derivation is an optimization/consistency argument: the Einstein equations are the unique set of geometric equations consistent with the thermodynamic requirements δQ = TdS and S ∝ A at every local causal horizon. Gravity is not derived from an action principle but from a thermodynamic consistency condition — it is the equation of state of spacetime, just as the ideal gas law is the equation of state of a gas."),
        ("What The Math Says", 5,
         "Consider a small patch of any causal horizon in an arbitrary spacetime. Assign to it the Unruh temperature T equals h-bar a over 2 pi c k-B, where a is the acceleration of the horizon-generating null geodesics. Assign entropy proportional to area: dS equals eta times dA, with eta equals 1 over 4 l-P-squared. The heat flux delta-Q through the horizon patch equals the stress-energy tensor contracted with the null generator and the area element, computed via the Raychaudhuri equation which relates the expansion of the null generators to the Ricci tensor. Substituting into the Clausius relation delta-Q equals T dS and requiring the equation to hold for every local horizon at every point in spacetime yields the Einstein field equations R-ab minus half g-ab R plus Lambda g-ab equals 8 pi G over c-to-the-fourth times T-ab. The cosmological constant Lambda appears as an undetermined integration constant, exactly as in the standard derivation from the Einstein-Hilbert action."),
        ("Concept Tags", 6,
         "• Jacobson derivation\n• gravity from thermodynamics\n• equation of state of spacetime\n• Clausius relation\n• horizon thermodynamics\n• emergent gravity\n• Raychaudhuri equation\n• local causal horizon\n• entropy-area proportionality\n• thermodynamic consistency"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th-Gm", 0),
        ("entries", "concept_tags", "Jacobson derivation, gravity from thermodynamics, equation of state of spacetime, Clausius relation, horizon thermodynamics, emergent gravity, Raychaudhuri equation, local causal horizon, entropy-area proportionality, thermodynamic consistency", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "HB02", "Bekenstein-Hawking Entropy", "Jacobson uses S = A/4l_P² as input, combined with the Clausius relation, to derive the Einstein equations — gravity emerges from the entropy-area proportionality."),
        ("derives from", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "HB05", "Unruh Effect", "The Unruh temperature T = ℏa/2πck_B provides the local temperature at each horizon, the second key input to Jacobson's thermodynamic derivation."),
        ("predicts for", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "GV1", "General Relativity — Einstein Field Equations", "Jacobson derives the Einstein equations as a thermodynamic equation of state — GV1 is the output, not the input, of this derivation."),
    ],
},

{
    "id": "GT02",
    "title": "Verlinde Entropic Gravity",
    "filename": "GT02_verlinde_entropic_gravity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Verlinde's entropic gravity proposes that gravitational attraction is not a fundamental force but an entropic force — a macroscopic effect arising from the statistical tendency of a system to increase its entropy (Verlinde, JHEP 1104:029, 2011). Just as an elastic polymer recoils not because of a fundamental restoring force but because the coiled state has higher entropy than the stretched state, gravitational attraction arises because matter configurations at lower gravitational potential have higher entropy than those at higher potential. Verlinde derives Newton's law of gravity F = GmM/r² and Newton's second law F = ma from holographic and thermodynamic principles: the Bekenstein bound for information on holographic screens, the equipartition of energy E = ½NkT, and the Unruh temperature. The approach extends Jacobson's derivation by making the emergent nature of gravity explicit: gravity is not mediated by a graviton but is a macroscopic statistical effect of the underlying microscopic degrees of freedom on holographic screens."),
        ("Mathematical Form", 1,
         "Entropic force: F Δx = T ΔS\n\nDerivation of Newton's second law:\n  T = ℏa/2πck_B  (Unruh)\n  ΔS = 2πk_B mc Δx/ℏ  (Bekenstein, one bit per Compton wavelength)\n  → F = ma\n\nDerivation of Newton's gravity:\n  E = ½Nk_BT  (equipartition on holographic screen)\n  N = Ac³/Gℏ  (bits on screen of area A)\n  → F = GmM/r²"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): Verlinde's entropic gravity proposes that the gravitational force is a thermodynamic constraint — the gradient of entropy with respect to position. If correct, gravity is not a fundamental interaction but an emergent thermodynamic phenomenon, like osmotic pressure or polymer elasticity. The proposal remains contested: critics argue that entropic forces require thermal equilibrium, which is not present in vacuum gravity."),
        ("DS Cross-References", 3,
         "GT01 (Jacobson — Verlinde extends Jacobson's programme: where Jacobson derived the Einstein equations thermodynamically, Verlinde derives Newton's force law entropic-ally). HB05 (Unruh Effect — the Unruh temperature provides the entropic force's temperature). HB01 (Bekenstein Bound — the entropy change ΔS uses the Bekenstein bound to count bits on the holographic screen). GT03 (Padmanabhan — Padmanabhan's holographic equipartition extends Verlinde to cosmology, deriving the Friedmann equations). GT04 (Bianconi — Bianconi makes the framework quantum by using quantum relative entropy and Fisher information)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nEntropic gravity is an optimization argument: the system evolves to maximise entropy (equivalently, minimise free energy), and gravitational attraction is the gradient of this entropy landscape. The force law emerges from counting microstates on holographic screens — it is a statistical, not dynamical, derivation of gravity."),
        ("What The Math Says", 5,
         "The entropic force F is defined by F times displacement Delta-x equals temperature T times entropy change Delta-S. Verlinde derives Newton's second law by using the Unruh temperature T equals h-bar a over 2 pi c k-B and the Bekenstein entropy change Delta-S equals 2 pi k-B m c Delta-x over h-bar (representing one bit of information per Compton wavelength of displacement). The product T times Delta-S gives F equals m a. For Newton's gravitational law, Verlinde uses the equipartition theorem E equals half N k-B T on a holographic screen of area A equals 4 pi r-squared, where the number of degrees of freedom N equals A c-cubed over G h-bar. Setting the total energy E equals M c-squared (the mass enclosed by the screen) and solving for the force gives F equals G m M over r-squared — Newton's law of universal gravitation from purely thermodynamic and holographic arguments."),
        ("Concept Tags", 6,
         "• entropic gravity\n• Verlinde\n• entropic force\n• holographic screen\n• emergent gravity\n• equipartition\n• Newton's law from thermodynamics\n• information-based gravity\n• macroscopic entropy gradient\n• holographic degrees of freedom"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "entropic gravity, Verlinde, entropic force, holographic screen, emergent gravity, equipartition, Newton's law from thermodynamics, information-based gravity, macroscopic entropy gradient, holographic degrees of freedom", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT02", "Verlinde Entropic Gravity", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Verlinde extends Jacobson's programme from the Einstein equations to Newton's force law, making the entropic mechanism explicit."),
        ("derives from", "GT02", "Verlinde Entropic Gravity", "HB05", "Unruh Effect", "The Unruh temperature T = ℏa/2πck_B is the temperature of the entropic force in Verlinde's derivation."),
        ("derives from", "GT02", "Verlinde Entropic Gravity", "HB01", "Bekenstein Bound", "The entropy change ΔS = 2πk_Bmc Δx/ℏ in Verlinde's derivation uses the Bekenstein bound to count information bits displaced on the holographic screen."),
    ],
},

{
    "id": "GT03",
    "title": "Padmanabhan Holographic Equipartition",
    "filename": "GT03_padmanabhan_holographic_equipartition.md",
    "entry_type": "reference_law",
    "scale": "cosmological",
    "domain": "physics · information",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Padmanabhan's holographic equipartition principle states that the expansion of the universe is driven by the difference between the number of degrees of freedom on the boundary (holographic surface) and in the bulk: dV/dt = l_P²(N_sur − N_bulk), where N_sur is the number of degrees of freedom on the Hubble horizon and N_bulk is the number of bulk degrees of freedom within the horizon (Padmanabhan, arXiv:1206.4916, 2012). This derives the Friedmann equations of cosmology from a counting argument: space expands when the bulk has fewer degrees of freedom than the boundary can accommodate, and contracts when the bulk has more. The universe evolves toward holographic equipartition: a state where N_sur = N_bulk and expansion halts. This extends the Jacobson-Verlinde programme from local horizons to cosmological horizons, providing a thermodynamic/information-theoretic derivation of the expansion of the universe."),
        ("Mathematical Form", 1,
         "dV/dt = l_P² (N_sur − N_bulk)\n\nwhere:\n  V = Hubble volume\n  N_sur = A_H / l_P²  (surface degrees of freedom on Hubble horizon)\n  N_bulk = |E_Komar| / (½k_BT_H)  (bulk degrees of freedom, Komar energy / equipartition)\n  T_H = H/2π  (Gibbons-Hawking temperature of de Sitter horizon)\n  A_H = 4π/H²  (Hubble horizon area)\n\nThis yields the Friedmann equation:\n  H² + k/a² = 8πGρ/3"),
        ("Constraint Category", 2,
         "Thermodynamic-Geometric (Th-Gm): Padmanabhan's principle is a thermodynamic-geometric constraint: the rate of cosmological expansion (geometry) is determined by the information imbalance between surface and bulk degrees of freedom (thermodynamics/information). The Friedmann equations emerge as the equation of state governing this balance. Cosmological expansion is driven by information disequilibrium."),
        ("DS Cross-References", 3,
         "GT01 (Jacobson — Padmanabhan extends Jacobson's local derivation to the cosmological scale, deriving the Friedmann equations from horizon thermodynamics). GT02 (Verlinde — Padmanabhan builds on Verlinde's entropic force by applying it to the cosmological horizon). HB03 (Holographic Principle — the N_sur term counts holographic degrees of freedom on the boundary). RG04 (Zamolodchikov c-theorem — both describe the monotonic decrease of effective degrees of freedom under a flow: c decreases under RG, N_bulk approaches N_sur under cosmic expansion)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nHolographic equipartition is an equilibrium condition: the universe expands until N_sur = N_bulk, at which point the driving force vanishes. This is the cosmological equilibrium, analogous to thermal equilibrium where entropy is maximised. The approach to equilibrium (expansion) is driven by the information deficit of the bulk relative to the boundary — a counting argument, not a force law."),
        ("What The Math Says", 5,
         "The rate of change of the Hubble volume V is l-P-squared times the difference between N-sur and N-bulk. The surface degrees of freedom N-sur equal the Hubble horizon area A-H divided by the Planck area l-P-squared. The bulk degrees of freedom N-bulk equal the absolute value of the Komar energy divided by half k-B T-H, where T-H is the Gibbons-Hawking temperature H over 2 pi of the de Sitter horizon. When N-sur exceeds N-bulk — when the boundary can accommodate more information than the bulk contains — the volume increases: space expands. When N-sur equals N-bulk, expansion halts: holographic equipartition is achieved. This yields the standard Friedmann equation H-squared plus k over a-squared equals 8 pi G rho over 3. The cosmological constant Lambda corresponds to the final equilibrium state where N-sur equals N-bulk, explaining why the universe approaches de Sitter space."),
        ("Concept Tags", 6,
         "• holographic equipartition\n• Padmanabhan\n• cosmological expansion\n• degrees of freedom counting\n• Hubble horizon\n• Friedmann equations from information\n• surface-bulk imbalance\n• cosmic evolution\n• de Sitter equilibrium\n• information-driven expansion"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th-Gm", 0),
        ("entries", "concept_tags", "holographic equipartition, Padmanabhan, cosmological expansion, degrees of freedom counting, Hubble horizon, Friedmann equations from information, surface-bulk imbalance, cosmic evolution, de Sitter equilibrium, information-driven expansion", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT03", "Padmanabhan Holographic Equipartition", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Padmanabhan extends Jacobson's local horizon thermodynamics to the cosmological Hubble horizon, deriving the Friedmann equations."),
        ("derives from", "GT03", "Padmanabhan Holographic Equipartition", "HB03", "Holographic Principle", "The surface degrees of freedom N_sur are counted holographically: N_sur = A_H/l_P², applying the holographic principle to the Hubble horizon."),
        ("analogous to", "GT03", "Padmanabhan Holographic Equipartition", "RG04", "Zamolodchikov c-Theorem", "Both describe monotonic decrease of effective degrees of freedom under a flow: c decreases under RG flow in 2D; the bulk-surface imbalance drives cosmic expansion toward equipartition."),
    ],
},

{
    "id": "GT04",
    "title": "Bianconi Gravity from Entropy",
    "filename": "GT04_bianconi_gravity_from_entropy.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "physics · information · networks",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Bianconi's framework derives gravitational dynamics from quantum information geometry by treating spacetime as a network of quantum states whose geometry is determined by the quantum relative entropy and its associated Fisher information metric (Bianconi, PRD 111, 066001, 2025). The key insight is that the quantum relative entropy S(ρ||σ) between quantum states on a network defines a natural distance, and its Hessian — the quantum Fisher information matrix — defines a Riemannian metric on the space of quantum states. This metric generates curvature, and the curvature satisfies equations analogous to Einstein's field equations. Gravity is not a fundamental force but the geometric consequence of information-geometric structure on quantum state space. The framework extends the Jacobson-Verlinde-Padmanabhan programme from classical thermodynamics to quantum information geometry, using the Fisher-Rao metric as the bridge between information theory and spacetime geometry. Bianconi's approach is network-native: it works on discrete quantum networks, not just continuous manifolds."),
        ("Mathematical Form", 1,
         "Quantum relative entropy: S(ρ||σ) = Tr(ρ log ρ − ρ log σ)\n\nQuantum Fisher information metric:\n  g_ij^Q = −∂²S(ρ_θ||ρ_{θ₀})/∂θ^i ∂θ^j |_{θ=θ₀}\n\nEmergent curvature: R_ij ~ T_ij  (curvature from Fisher information\n  on the quantum network satisfies Einstein-like equations)\n\nKey structural equation:\n  Gravity = curvature of the Fisher-Rao metric on quantum state space"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): Bianconi's framework is an informatic-geometric programme: gravity (geometry) emerges from quantum information (Fisher information). The constraint structure is: quantum relative entropy → Fisher metric → curvature → Einstein equations. The geometric content (curvature, metric) is entirely derived from the informatic content (quantum states, distinguishability, Fisher information)."),
        ("DS Cross-References", 3,
         "IT04 (Quantum Relative Entropy — the quantum relative entropy S(ρ||σ) is the starting point of Bianconi's derivation). IT05 (Fisher Information — the quantum Fisher information matrix, the Hessian of QRE, provides the emergent metric). IT08 (Fisher-Rao Metric — the Fisher-Rao metric on quantum state space is the emergent spacetime metric in Bianconi's framework). GT01 (Jacobson — Bianconi extends Jacobson's classical thermodynamic derivation to the quantum information-geometric regime). GT05 (Carney — Carney's spin entropic gravity tests similar ideas at the microscopic scale). RG06 (Cotler-Rezchikov — both use the Fisher metric as the fundamental geometric object: Cotler-Rezchikov for RG flow, Bianconi for gravity)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nBianconi's programme derives geometry from information by optimising (extremising) an information-geometric functional. The Einstein equations emerge as the stationarity condition for an action built from the quantum Fisher information metric — gravity is the geometry that extremises the information-geometric action on quantum state space."),
        ("What The Math Says", 5,
         "Start with a network of quantum states, each described by a density matrix rho. The quantum relative entropy S of rho given sigma measures how distinguishable the two states are. The Hessian of S with respect to parameters theta at a reference point theta-zero gives the quantum Fisher information matrix g-ij-Q — a positive-definite matrix that defines a Riemannian metric on the space of quantum states. This metric has curvature. Bianconi shows that this curvature satisfies equations structurally analogous to the Einstein field equations: the Ricci curvature of the Fisher metric is determined by the quantum state configuration, just as the Ricci curvature of spacetime is determined by the stress-energy tensor. The network structure allows discrete formulation: the framework does not require a pre-existing smooth manifold. Spacetime geometry and its curvature emerge from quantum information geometry on the network."),
        ("Concept Tags", 6,
         "• Bianconi gravity\n• quantum information geometry\n• emergent spacetime\n• quantum relative entropy\n• quantum Fisher information\n• Fisher-Rao metric\n• network gravity\n• information-geometric gravity\n• quantum state space curvature\n• Einstein equations from information"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "Bianconi gravity, quantum information geometry, emergent spacetime, quantum relative entropy, quantum Fisher information, Fisher-Rao metric, network gravity, information-geometric gravity, quantum state space curvature, Einstein equations from information", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT04", "Bianconi Gravity from Entropy", "IT04", "Quantum Relative Entropy", "Bianconi's framework starts from the quantum relative entropy S(ρ||σ) — gravitational dynamics emerge from its geometric structure."),
        ("derives from", "GT04", "Bianconi Gravity from Entropy", "IT05", "Fisher Information", "The quantum Fisher information matrix — the Hessian of quantum relative entropy — provides the emergent Riemannian metric that becomes the spacetime metric."),
        ("generalizes", "GT04", "Bianconi Gravity from Entropy", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Bianconi extends Jacobson's classical thermodynamic derivation to the quantum information-geometric regime using Fisher information rather than the Clausius relation."),
    ],
},

{
    "id": "GT05",
    "title": "Carney Spin Entropic Gravity",
    "filename": "GT05_carney_spin_entropic_gravity.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "physics · information",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Carney's spin entropic gravity proposes a microscopic model where the gravitational interaction between two masses arises from the entanglement entropy of a quantum spin network connecting them (Carney, PRX 15, 031038, 2025). Each mass is surrounded by a cloud of spin-½ degrees of freedom on a lattice. The gravitational force emerges as an entropic force from the tendency of the spin system to maximise its entanglement entropy. Crucially, Carney derives testable predictions: the entanglement-mediated gravity produces a noise spectrum distinct from both quantum gravity (graviton exchange) and classical gravity. Optomechanical experiments could distinguish between these scenarios within the next decade. This makes Carney's framework the most experimentally accessible test of the gravity-from-information paradigm."),
        ("Mathematical Form", 1,
         "Entropic force: F = T ∂S_ent/∂r\n\nwhere:\n  S_ent = entanglement entropy of spin network between two masses\n  T = effective temperature of the spin degrees of freedom\n  r = separation between masses\n\nNoise prediction: S_FF(ω) ∝ ω^{-α}  (characteristic spectrum\n  distinguishable from quantum gravity and classical gravity)\n\nRecovery: in the large-N limit, F → GmM/r² (Newton's law)"),
        ("Constraint Category", 2,
         "Informatic (In): Carney's framework is fundamentally informatic: gravitational attraction is the entropic force arising from quantum entanglement between spin degrees of freedom. The constraint is that gravity is not mediated by a particle (graviton) but by the statistical mechanics of entanglement — making it a macroscopic quantum information effect."),
        ("DS Cross-References", 3,
         "GT01 (Jacobson — Carney provides a microscopic model for the thermodynamic derivation: the spin network is the microstructure whose entropy drives gravity). GT02 (Verlinde — Carney's entropic force mechanism is the microscopic realisation of Verlinde's macroscopic entropic gravity). GT04 (Bianconi — both use quantum information (entanglement, Fisher information) to derive gravity, but Carney focuses on testability while Bianconi focuses on geometric structure). IT02 (Von Neumann Entropy — the entanglement entropy driving the force is a von Neumann entropy of the spin system's reduced density matrix). BR01 (ER=EPR — Carney's spin entanglement mediating gravity is a microscopic instance of the ER=EPR conjecture: entanglement creates effective geometric connections)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nCarney's spin entropic gravity is an optimization/entropy-maximisation model: the spin system evolves to maximise its entanglement entropy, and the resulting entropic force reproduces Newtonian gravity. The experimentally testable noise spectrum distinguishes this optimisation-based mechanism from fundamental force mechanisms."),
        ("What The Math Says", 5,
         "Two masses are connected by a network of spin-half quantum degrees of freedom on a lattice. The entanglement entropy S-ent of the spin network depends on the separation r between the masses. The entropic force equals the temperature T times the derivative of S-ent with respect to r. In the limit of many spins (large N), this recovers Newton's gravitational force F equals G m M over r-squared. The key testable prediction is the noise power spectrum S-FF of omega: the force fluctuations produced by the spin network have a characteristic frequency dependence that differs from both quantum gravity (graviton exchange produces shot noise) and classical stochastic gravity (produces white noise). Optomechanical experiments measuring force noise between closely spaced masses could detect this signature. Carney estimates that current technology is within an order of magnitude of the required sensitivity."),
        ("Concept Tags", 6,
         "• spin entropic gravity\n• Carney\n• entanglement entropy\n• entropic force\n• spin network\n• testable quantum gravity\n• noise spectrum\n• optomechanical test\n• microscopic gravity model\n• quantum entanglement mediated gravity"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "spin entropic gravity, Carney, entanglement entropy, entropic force, spin network, testable quantum gravity, noise spectrum, optomechanical test, microscopic gravity model, quantum entanglement mediated gravity", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT05", "Carney Spin Entropic Gravity", "GT02", "Verlinde Entropic Gravity", "Carney provides the microscopic mechanism for Verlinde's entropic gravity: the spin network is the microstructure whose entanglement entropy generates the entropic force."),
        ("tests", "GT05", "Carney Spin Entropic Gravity", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Carney's noise spectrum predictions provide the first experimental test of the gravity-from-thermodynamics programme — distinguishing entropic from fundamental gravity."),
        ("couples to", "GT05", "Carney Spin Entropic Gravity", "IT02", "Von Neumann Entropy", "The entanglement entropy driving the gravitational force in Carney's model is a von Neumann entropy of the spin system's reduced density matrix."),
    ],
},

{
    "id": "GT06",
    "title": "Sakharov Induced Gravity",
    "filename": "GT06_sakharov_induced_gravity.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Sakharov's induced gravity proposes that the Einstein-Hilbert action of general relativity — and hence gravity itself — is not a fundamental interaction but is induced by quantum fluctuations of matter fields in curved spacetime (Sakharov, Soviet Physics Doklady 12, 1040, 1968). Just as the elasticity of a metal is not a fundamental property but emerges from the electromagnetic interactions between atoms, the curvature of spacetime is not fundamental but emerges from the quantum vacuum energy of matter fields. The gravitational constant G is determined by the ultraviolet cutoff of the quantum field theory — it is a derived quantity, not a free parameter. Sakharov's proposal is the earliest version of emergent gravity, predating Jacobson by 27 years and Verlinde by 43 years. Modern formulations connect it to the vacuum entanglement entropy: the induced gravitational action arises from the entanglement of quantum fields across any causal horizon."),
        ("Mathematical Form", 1,
         "Induced action: S_grav = (1/16πG_ind) ∫ R √(-g) d⁴x + ...\n\nwhere:\n  1/G_ind = (c³/ℏ) · Σ_s N_s ∫ (dk/16π²)  (sum over species s,\n    N_s = number of fields, k = momentum cutoff)\n\nModern (entanglement): G_ind determined by the entanglement entropy\n  of quantum fields across a horizon:\n  S_ent = (A/4G_ind) + finite terms"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): Sakharov's induced gravity treats the gravitational action as a thermodynamic free energy: the Einstein-Hilbert action arises as the leading term in the effective action of matter fields in curved spacetime. Gravity is an emergent elasticity of the vacuum, determined by the spectrum of quantum fields — a thermodynamic/statistical effect of the underlying quantum degrees of freedom."),
        ("DS Cross-References", 3,
         "GT01 (Jacobson — Jacobson's thermodynamic derivation is the modern formulation of Sakharov's idea: gravity emerges from the thermodynamic properties of horizons, which are themselves determined by quantum vacuum fluctuations). GT02 (Verlinde — Verlinde's entropic gravity is a descendant of Sakharov's induced gravity: both treat gravity as emergent from underlying microscopic physics). GV1 (Einstein Field Equations — the output of Sakharov's programme: the Einstein-Hilbert action is induced by quantum fluctuations). HB02 (Bekenstein-Hawking Entropy — the modern interpretation of induced gravity connects the gravitational constant to entanglement entropy, which equals BH entropy for horizons)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nSakharov's induced gravity derives the gravitational action as the effective action (free energy) of quantum matter fields in curved spacetime. The Einstein equations emerge from extremising this effective action — gravity is the stationarity condition for the vacuum free energy functional."),
        ("What The Math Says", 5,
         "The gravitational action S-grav with the familiar Einstein-Hilbert form (1 over 16 pi G) times the integral of the Ricci scalar R is not postulated but derived from the one-loop effective action of quantum matter fields propagating in curved spacetime. The induced gravitational constant G-ind is determined by a sum over all matter species, weighted by their spins and integrated up to an ultraviolet momentum cutoff k. The key insight is that the vacuum energy of quantum fields depends on spacetime curvature: in flat space the vacuum energy is a constant, but in curved space it acquires a term proportional to R, which is precisely the Einstein-Hilbert action. In modern language, the gravitational constant is determined by the entanglement entropy of quantum fields across a horizon: S-ent equals A over 4 G-ind plus finite corrections. This connects Sakharov's 1968 idea to the Bekenstein-Hawking entropy and to Jacobson's 1995 thermodynamic derivation."),
        ("Concept Tags", 6,
         "• Sakharov induced gravity\n• emergent gravity\n• vacuum elasticity\n• one-loop effective action\n• induced gravitational constant\n• quantum vacuum fluctuations\n• entanglement entropy\n• ultraviolet cutoff\n• effective field theory\n• vacuum energy and curvature"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Sakharov induced gravity, emergent gravity, vacuum elasticity, one-loop effective action, induced gravitational constant, quantum vacuum fluctuations, entanglement entropy, ultraviolet cutoff, effective field theory, vacuum energy and curvature", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT06", "Sakharov Induced Gravity", "GV1", "General Relativity — Einstein Field Equations", "Sakharov derives the Einstein-Hilbert action from quantum vacuum fluctuations — the Einstein equations are not fundamental but induced by matter field dynamics in curved spacetime."),
        ("analogous to", "GT06", "Sakharov Induced Gravity", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Both derive gravity from underlying microscopic physics: Sakharov from quantum vacuum fluctuations, Jacobson from horizon thermodynamics. The modern connection is through entanglement entropy."),
        ("couples to", "GT06", "Sakharov Induced Gravity", "HB02", "Bekenstein-Hawking Entropy", "The modern interpretation connects Sakharov's induced gravitational constant to entanglement entropy: G is determined by S_ent = A/4G, linking the gravitational constant to quantum entanglement."),
    ],
},

{
    "id": "GT08",
    "title": "Equivalence Principle",
    "filename": "GT08_equivalence_principle.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The equivalence principle states that inertial mass equals gravitational mass: the resistance of an object to acceleration (inertia) is exactly the same quantity that determines the strength of its gravitational interaction (Einstein, 1907). In its strong form, the principle states that the effects of gravity are locally indistinguishable from the effects of acceleration — an observer in a uniformly accelerating elevator cannot distinguish their situation from being at rest in a gravitational field. This equivalence is the foundation of general relativity: it implies that gravity is not a force but a geometric property of spacetime. For the gravity-from-thermodynamics programme, the equivalence principle has a deep information-theoretic interpretation: it means that the Unruh effect (thermal radiation seen by accelerating observers) and the Hawking effect (thermal radiation from gravitational horizons) are manifestations of the same underlying physics."),
        ("Mathematical Form", 1,
         "Weak: m_inertial = m_gravitational\n  F = m_i a = m_g g  →  a = g  (universality of free fall)\n\nStrong: In a sufficiently small region, the effects of gravity\n  are indistinguishable from uniform acceleration:\n  g_μν → η_μν + O(x²)  (locally flat coordinates exist)\n\nEinstein: g_μν at any point can be transformed to η_μν;\n  local physics is special-relativistic\n\nExperimental: |m_i − m_g|/m < 10⁻¹⁵  (Eötvös-type experiments)"),
        ("Constraint Category", 2,
         "Geometric (Gm): The equivalence principle is the foundational geometric constraint of general relativity: it requires that spacetime be a pseudo-Riemannian manifold with a metric that can be locally diagonalised to the Minkowski form. This geometric requirement completely determines the mathematical framework (differential geometry on manifolds) and constrains the possible dynamics (Einstein equations are the simplest second-order equations for the metric)."),
        ("DS Cross-References", 3,
         "GV1 (Einstein Field Equations — the equivalence principle is the physical postulate from which the Einstein equations are derived: gravity = geometry follows from the local equivalence of gravity and acceleration). HB05 (Unruh Effect — the Unruh effect is the quantum expression of the equivalence principle: acceleration and gravity produce identical thermal effects). GT01 (Jacobson — Jacobson's derivation relies on the equivalence principle: every point in spacetime has a local Rindler horizon with Unruh temperature). CM1 (Newton's Second Law — the equivalence principle generalises Newton's F = ma by identifying inertial and gravitational mass, leading from flat-space dynamics to curved-spacetime geometry)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe equivalence principle is a symmetry statement: the local equivalence of gravity and acceleration is a gauge symmetry (diffeomorphism invariance) of the gravitational field. Like other symmetries (Noether's theorem), it constrains the dynamics: the Einstein equations are the unique second-order field equations consistent with this symmetry (Lovelock's theorem)."),
        ("What The Math Says", 5,
         "The weak equivalence principle states that inertial mass m-i (which appears in Newton's second law F equals m-i a) equals gravitational mass m-g (which appears in the gravitational force F equals m-g g). This has been tested to parts in 10-to-the-15 by torsion balance experiments. The strong equivalence principle states that at any point in spacetime, coordinates can be chosen so that the metric g-mu-nu reduces to the Minkowski metric eta-mu-nu, with corrections of order x-squared — meaning the effects of gravity vanish locally. This is equivalent to requiring spacetime to be a pseudo-Riemannian manifold. Einstein's equivalence principle further requires that all non-gravitational physics in these local coordinates is identical to special relativity. Combined with general covariance, this leads uniquely to the Einstein field equations as the simplest dynamical equations for the metric."),
        ("Concept Tags", 6,
         "• equivalence principle\n• inertial mass\n• gravitational mass\n• universality of free fall\n• locally flat coordinates\n• general covariance\n• pseudo-Riemannian manifold\n• diffeomorphism invariance\n• Eötvös experiment\n• gravity as geometry"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Gm", 0),
        ("entries", "concept_tags", "equivalence principle, inertial mass, gravitational mass, universality of free fall, locally flat coordinates, general covariance, pseudo-Riemannian manifold, diffeomorphism invariance, Eötvös experiment, gravity as geometry", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GT08", "Equivalence Principle", "GV1", "General Relativity — Einstein Field Equations", "The equivalence principle is the physical postulate from which the Einstein field equations are derived — gravity as geometry follows from the equivalence of gravity and acceleration."),
        ("couples to", "GT08", "Equivalence Principle", "HB05", "Unruh Effect", "The Unruh effect is the quantum expression of the equivalence principle: acceleration and gravity produce identical thermal effects on quantum fields."),
        ("analogous to", "GT08", "Equivalence Principle", "CM1", "Newton's First and Second Laws of Motion", "The equivalence principle extends Newton's F = ma by identifying inertial and gravitational mass, generalising flat-space dynamics to curved spacetime."),
    ],
},

]  # end ENTRIES


def insert_entries(db_path, entries):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    inserted = skipped = 0

    for e in entries:
        cur.execute("""
            INSERT OR IGNORE INTO entries
                (id, title, filename, entry_type, scale, domain, status, confidence, type_group, authoring_status)
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (e["id"], e["title"], e["filename"], e["entry_type"], e["scale"],
              e["domain"], e["status"], e["confidence"], e["type_group"], None))

        if cur.rowcount == 0:
            print(f"  SKIP (exists): {e['id']}")
            skipped += 1
            continue

        for (sname, sorder, content) in e["sections"]:
            cur.execute("""
                INSERT INTO sections (entry_id, section_name, section_order, content)
                VALUES (?,?,?,?)
            """, (e["id"], sname, sorder, content))

        for (tname, pname, pvalue, porder) in e["properties"]:
            cur.execute("""
                INSERT INTO entry_properties
                    (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?,?,?,?,?)
            """, (e["id"], tname, pname, pvalue, porder))

        for (ltype, src, slabel, tgt, tlabel, desc) in e.get("links", []):
            cur.execute("""
                INSERT OR IGNORE INTO links
                    (link_type, source_id, source_label, target_id, target_label,
                     description, link_order, confidence_tier)
                VALUES (?,?,?,?,?,?,?,?)
            """, (ltype, src, slabel, tgt, tlabel, desc, 0, "1.5"))

        print(f"  INSERT: {e['id']} — {e['title']}")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone: {inserted} inserted, {skipped} skipped.")
    return inserted


if __name__ == "__main__":
    print(f"Inserting GT pillar ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)

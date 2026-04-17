"""
Pillar Extension — Cross-Pillar Bridge Entries (BR)
Inserts 5 new entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

These bridge entries explicitly connect pillars. They should be
inserted LAST, after all pillar entries exist.

Entries:
  BR01: ER = EPR Conjecture
  BR02: AdS/CFT Correspondence
  BR03: Van Raamsdonk: Entanglement Builds Spacetime
  BR04: Thermodynamic Geometry (Ruppeiner)
  BR05: Dimensional Flow in Quantum Gravity
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── CROSS-PILLAR BRIDGE ENTRIES ────────────────────────────────────────────

{
    "id": "BR01",
    "title": "ER = EPR Conjecture",
    "filename": "BR01_er_epr_conjecture.md",
    "entry_type": "open_question",
    "scale": "quantum · cosmological",
    "domain": "physics · information",
    "status": "conjectured",
    "confidence": "Tier 3 ‡",
    "type_group": "Q",
    "sections": [
        ("What It Claims", 0,
         "The ER = EPR conjecture proposes that every Einstein-Rosen bridge (wormhole, ER) is created by and equivalent to quantum entanglement (Einstein-Podolsky-Rosen, EPR) between the systems on either side (Maldacena & Susskind, 2013). Two entangled black holes are connected by a non-traversable wormhole; conversely, every wormhole corresponds to an entangled pair. The conjecture bridges holographic bounds and quantum information theory by identifying a geometric object (wormhole) with an information-theoretic relation (entanglement). If correct, ER = EPR implies that the connectivity of spacetime is built from quantum entanglement — removing entanglement disconnects the geometry. This bridges HB (holographic bounds) and IT (information theory): geometric connections between spacetime regions ARE quantum information correlations. The conjecture is the strongest form of the 'it from qubit' programme — spacetime geometry is emergent from quantum information."),
        ("Mathematical Form", 1,
         "Conjecture: ER bridge (wormhole) ≡ EPR pair (entanglement)\n\nFor two entangled black holes:\n  |ψ⟩ = Σ_n e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R  (thermofield double state)\n  ↔  two-sided AdS black hole connected by ER bridge\n\nEntanglement entropy: S_ent = S_BH = A/4G_N\n  (entanglement entropy equals geometric area)\n\nDisconnecting limit: S_ent → 0  ↔  wormhole length → ∞"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): ER = EPR is the most radical bridge between information (entanglement, qubits) and geometry (wormholes, spacetime connectivity). It proposes that every geometric connection is an information correlation, and every information correlation is a geometric connection. This would make information the fundamental substance from which spacetime is constructed."),
        ("DS Cross-References", 3,
         "HB02 (Bekenstein-Hawking Entropy — the entanglement entropy of ER = EPR equals the BH entropy, connecting information to horizon area). IT02 (Von Neumann Entropy — the entanglement in ER = EPR is measured by von Neumann entropy of the reduced state). HB07 (Ryu-Takayanagi — RT computes entanglement entropy as geometric area; ER = EPR identifies the geometric surfaces with entanglement connections). BR03 (Van Raamsdonk — Van Raamsdonk's argument that removing entanglement disconnects spacetime is a direct consequence of ER = EPR). BR02 (AdS/CFT — ER = EPR is formulated within AdS/CFT, where the thermofield double state in the boundary CFT corresponds to the two-sided black hole in the bulk). GT05 (Carney — Carney's spin entanglement mediating gravity is a microscopic realisation of ER = EPR at laboratory scales)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nER = EPR is an identity/duality: it equates two seemingly different objects (geometric connections and quantum correlations). The conservation-like structure is that geometric connectivity IS entanglement — neither can exist without the other, and the amount of each is conserved in the equivalence."),
        ("What The Math Says", 5,
         "The thermofield double state psi equals the sum over n of e-to-the-minus-beta-E-n-over-2 times the tensor product of state n on the left and state n on the right is a maximally entangled state between two copies of a quantum system. In AdS/CFT, this state corresponds to a two-sided eternal black hole where the left and right boundaries are connected by an Einstein-Rosen bridge (wormhole) in the bulk. The entanglement entropy of the left system equals the Bekenstein-Hawking entropy S-BH equals A over 4 G-N, where A is the area of the wormhole's minimal cross-section. Reducing the entanglement (for example by acting with many local operators on one side) stretches the wormhole, increasing its length. In the limit of zero entanglement, the wormhole becomes infinitely long — the geometry disconnects. The ER equals EPR conjecture generalises this to all entangled quantum systems: any entangled pair is connected by a (possibly microscopic, Planck-scale) wormhole."),
        ("Concept Tags", 6,
         "• ER = EPR\n• Einstein-Rosen bridge\n• wormhole\n• quantum entanglement\n• spacetime connectivity\n• thermofield double\n• it from qubit\n• geometry from information\n• Maldacena-Susskind\n• holographic entanglement"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "ER = EPR, Einstein-Rosen bridge, wormhole, quantum entanglement, spacetime connectivity, thermofield double, it from qubit, geometry from information, Maldacena-Susskind, holographic entanglement", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "BR01", "ER = EPR Conjecture", "HB02", "Bekenstein-Hawking Entropy", "In ER = EPR, the entanglement entropy between the two sides equals the Bekenstein-Hawking entropy S = A/4G — the bridge area IS the entanglement measure."),
        ("couples to", "BR01", "ER = EPR Conjecture", "IT02", "Von Neumann Entropy", "The entanglement in ER = EPR is quantified by the von Neumann entropy of the reduced density matrix — the information-theoretic side of the geometry-information bridge."),
        ("couples to", "BR01", "ER = EPR Conjecture", "BR03", "Van Raamsdonk: Entanglement Builds Spacetime", "Van Raamsdonk's argument (removing entanglement disconnects spacetime) is a direct consequence of ER = EPR: no entanglement → no geometric connection."),
    ],
},

{
    "id": "BR02",
    "title": "AdS/CFT Correspondence",
    "filename": "BR02_ads_cft_correspondence.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The AdS/CFT correspondence (anti-de Sitter/conformal field theory correspondence) states that a gravitational theory in (d+1)-dimensional anti-de Sitter spacetime is exactly equivalent to a non-gravitational conformal field theory living on the d-dimensional boundary of that spacetime (Maldacena, 1997). This is the most concrete realisation of the holographic principle: the entire content of a gravitational bulk theory — including black holes, gravitational waves, and spacetime geometry — is encoded in a lower-dimensional boundary theory without gravity. AdS/CFT bridges holographic bounds (HB) and renormalisation group (RG) physics: the extra radial dimension of AdS corresponds to the energy scale of the boundary CFT, making the bulk geometry a geometric picture of the renormalisation group flow. The correspondence connects information theory to gravity through the holographic dictionary: boundary entanglement entropy equals bulk geometric area (Ryu-Takayanagi), boundary conformal symmetry maps to bulk isometries, and boundary RG flow corresponds to bulk radial evolution."),
        ("Mathematical Form", 1,
         "Duality: gravity in AdS_{d+1}  ⟺  CFT_d on boundary\n\nPartition functions: Z_gravity[φ₀] = ⟨exp(∫ φ₀ O)⟩_CFT\n\nRadial/energy correspondence:\n  r_bulk ↔ μ_boundary  (bulk radial coordinate = boundary energy scale)\n\nHolographic dictionary:\n  Boundary S_ent(A) = Bulk Area(γ_A)/4G_N  (Ryu-Takayanagi)\n  Boundary T_μν = Bulk metric g_μν  (stress-energy = geometry)\n  Boundary RG flow = Bulk radial evolution\n\nStrong/weak duality: strong boundary coupling ↔ weak bulk coupling"),
        ("Constraint Category", 2,
         "Geometric-Informatic (Gm-In): AdS/CFT is a duality constraint: it requires that two superficially different theories — a gravitational bulk theory and a non-gravitational boundary theory — contain exactly the same information. The constraint is that all bulk geometric information (spacetime, horizons, curvature) is equivalently encoded in boundary informatic quantities (correlation functions, entanglement, conformal data)."),
        ("DS Cross-References", 3,
         "HB03 (Holographic Principle — AdS/CFT is the precise mathematical realisation of the holographic principle: (d+1)-dimensional gravity is encoded on a d-dimensional boundary). HB07 (Ryu-Takayanagi — RT is a consequence of AdS/CFT: boundary entanglement entropy equals bulk minimal surface area). RG01 (Wilson RG — the extra radial dimension of AdS geometrises the RG: moving radially inward in the bulk corresponds to flowing to lower energies on the boundary). RG04 (c-theorem — the c-theorem's monotonicity is geometrised in AdS/CFT: the c-function corresponds to a geometric quantity that decreases along the radial direction). BR01 (ER = EPR — ER = EPR is formulated within AdS/CFT: the thermofield double state on the boundary corresponds to the two-sided black hole in the bulk)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nAdS/CFT is a duality: it establishes a one-to-one map between two complete theories, conserving all information between the bulk and boundary descriptions. The conservation is exact — every bulk observable has a unique boundary counterpart and vice versa. This makes AdS/CFT the most powerful structural constraint in theoretical physics: any result in one description must have a counterpart in the other."),
        ("What The Math Says", 5,
         "The Maldacena correspondence equates the partition function of quantum gravity in anti-de Sitter space (a negatively curved spacetime) with the partition function of a conformal field theory on its flat boundary. The boundary values of bulk fields phi-zero act as sources for boundary operators O: the bulk partition function Z-gravity of phi-zero equals the expectation value of exp of the integral of phi-zero times O in the CFT. The key structural insight is the radial-energy correspondence: the radial coordinate r in the bulk maps to the energy scale mu on the boundary. Moving radially inward corresponds to flowing to lower energies — the bulk geometry IS a geometric picture of the renormalisation group. Strong coupling on the boundary (where the CFT is hard to solve) maps to weak coupling in the bulk (where gravity is classical and tractable), making AdS/CFT a powerful computational tool: hard quantum field theory problems become easy classical gravity problems."),
        ("Concept Tags", 6,
         "• AdS/CFT correspondence\n• holographic duality\n• Maldacena conjecture\n• bulk-boundary duality\n• anti-de Sitter space\n• conformal field theory\n• strong-weak duality\n• holographic dictionary\n• geometric RG\n• radial-energy correspondence"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Gm-In", 0),
        ("entries", "concept_tags", "AdS/CFT correspondence, holographic duality, Maldacena conjecture, bulk-boundary duality, anti-de Sitter space, conformal field theory, strong-weak duality, holographic dictionary, geometric RG, radial-energy correspondence", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "BR02", "AdS/CFT Correspondence", "HB03", "Holographic Principle", "AdS/CFT is the precise mathematical realisation of the holographic principle: (d+1)-dimensional bulk gravity is exactly encoded on the d-dimensional boundary."),
        ("couples to", "BR02", "AdS/CFT Correspondence", "RG01", "Wilson's Renormalisation Group", "AdS/CFT geometrises the RG: the extra radial dimension of AdS IS the RG scale, making bulk geometry a picture of scale-dependent physics."),
        ("couples to", "BR02", "AdS/CFT Correspondence", "HB07", "Ryu-Takayanagi Formula", "The RT formula S_A = Area(γ_A)/4G_N is a consequence of AdS/CFT — it computes boundary entanglement entropy using bulk geometry."),
    ],
},

{
    "id": "BR03",
    "title": "Van Raamsdonk: Entanglement Builds Spacetime",
    "filename": "BR03_van_raamsdonk_entanglement_spacetime.md",
    "entry_type": "reference_law",
    "scale": "quantum · cosmological",
    "domain": "physics · information",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Van Raamsdonk showed that in the AdS/CFT correspondence, reducing the quantum entanglement between two halves of the boundary CFT causes the dual bulk spacetime to pinch off and disconnect — entanglement is the glue that holds spacetime together (Van Raamsdonk, Gen. Rel. Grav. 42, 2323, 2010). Starting from a thermofield double state (maximally entangled), the dual geometry is a connected two-sided black hole. As entanglement is reduced, the Ryu-Takayanagi surface grows, corresponding to the wormhole throat stretching. At zero entanglement, the geometry disconnects into two separate spacetimes. This result bridges holographic bounds (HB) and information theory (IT) directly: spacetime connectivity IS quantum entanglement. The geometric structure of the bulk is not fundamental but emergent from the pattern of entanglement in the boundary quantum state. This is the most concrete evidence for the 'it from qubit' programme: geometry (spacetime) is derived from information (entanglement)."),
        ("Mathematical Form", 1,
         "Thermofield double: |TFD⟩ = Σ_n e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R\n  ↔  connected two-sided black hole\n\nEntanglement entropy: S_ent = S_BH = A(throat)/4G_N\n\nReduce entanglement: S_ent → 0\n  ↔  A(throat) → 0  (wormhole pinches off)\n  ↔  geometry disconnects\n\nProduct state: |ψ⟩_L ⊗ |φ⟩_R  (zero entanglement)\n  ↔  two disconnected AdS spacetimes\n\nKey identity: spacetime connectivity ≡ quantum entanglement"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): Van Raamsdonk's result is the sharpest bridge between information and geometry: the connectivity of spacetime (a geometric property) is determined by the entanglement structure of the quantum state (an informatic property). Reducing entanglement disconnects geometry — information IS geometry."),
        ("DS Cross-References", 3,
         "HB07 (Ryu-Takayanagi — the RT surface area grows as entanglement decreases, quantifying the wormhole stretching until disconnection). IT02 (Von Neumann Entropy — the entanglement is measured by the von Neumann entropy of the reduced state; zero von Neumann entropy implies disconnected geometry). BR01 (ER = EPR — Van Raamsdonk's result is the key evidence for ER = EPR: entanglement (EPR) creates geometric connections (ER)). BR02 (AdS/CFT — Van Raamsdonk works within AdS/CFT, using the boundary entanglement to control bulk geometry). GT04 (Bianconi — Bianconi's network gravity is consistent with Van Raamsdonk: the Fisher metric on quantum states generates the geometric structure that Van Raamsdonk shows is entanglement-dependent)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: threshold-transition\n\nVan Raamsdonk's disconnection is a topological transition: as entanglement decreases through a critical value, the spacetime topology changes from connected to disconnected. This is a geometric phase transition driven by information content — the most dramatic example of information controlling geometry."),
        ("What The Math Says", 5,
         "Start with the thermofield double state: a maximally entangled state between two copies of a CFT, with entanglement entropy equal to the Bekenstein-Hawking entropy S-BH equals A of the throat divided by 4 G-N. In the dual bulk description, this is a two-sided eternal black hole connected by an Einstein-Rosen bridge. Now gradually reduce the entanglement by acting with local unitaries or partial projections. As entanglement entropy decreases, the Ryu-Takayanagi surface area grows — the wormhole throat elongates. The geometric distance between the two sides increases as entanglement decreases. In the limit of zero entanglement (product state: psi-L tensor phi-R), the throat area shrinks to zero, the wormhole pinches off, and the geometry disconnects into two separate AdS spacetimes with no geometric connection. The conclusion is that spacetime connectivity requires entanglement: unentangled systems occupy disconnected spacetimes. Geometry is not fundamental — it is built from the entanglement pattern of the quantum state."),
        ("Concept Tags", 6,
         "• Van Raamsdonk\n• entanglement builds spacetime\n• spacetime connectivity\n• it from qubit\n• geometric disconnection\n• wormhole pinch-off\n• emergent geometry\n• thermofield double\n• entanglement as glue\n• topology change from information"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "Van Raamsdonk, entanglement builds spacetime, spacetime connectivity, it from qubit, geometric disconnection, wormhole pinch-off, emergent geometry, thermofield double, entanglement as glue, topology change from information", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "BR03", "Van Raamsdonk: Entanglement Builds Spacetime", "HB07", "Ryu-Takayanagi Formula", "RT quantifies the Van Raamsdonk mechanism: as boundary entanglement decreases, the RT minimal surface area grows until the geometry disconnects."),
        ("couples to", "BR03", "Van Raamsdonk: Entanglement Builds Spacetime", "IT02", "Von Neumann Entropy", "The entanglement that builds spacetime is measured by the von Neumann entropy of the boundary quantum state — zero von Neumann entropy means disconnected geometry."),
        ("derives from", "BR03", "Van Raamsdonk: Entanglement Builds Spacetime", "BR02", "AdS/CFT Correspondence", "Van Raamsdonk's argument works within AdS/CFT: the boundary entanglement controls the bulk geometry through the holographic dictionary."),
    ],
},

{
    "id": "BR04",
    "title": "Thermodynamic Geometry (Ruppeiner Metric)",
    "filename": "BR04_thermodynamic_geometry_ruppeiner.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Ruppeiner's thermodynamic geometry defines a Riemannian metric on thermodynamic state space as the negative Hessian of the entropy: g_ij = −∂²S/∂X^i ∂X^j, where the X^i are extensive variables (energy, volume, particle number) (Ruppeiner, Rev. Mod. Phys. 67, 605, 1995). The geodesic distance in this metric measures the thermodynamic distinguishability between states — how far apart two states are in terms of their fluctuation properties. The Ruppeiner metric IS the Fisher-Rao metric applied to the canonical Gibbs ensemble: thermodynamic geometry and information geometry are the same geometry. The curvature of the Ruppeiner metric has physical meaning: it diverges at phase transitions (where fluctuations diverge) and its sign indicates whether microscopic interactions are attractive (negative curvature) or repulsive (positive curvature). This result bridges information theory (IT) and gravity-thermodynamics (GT) by showing that the Fisher-Rao metric — the fundamental object of information geometry — appears naturally in thermodynamic state space and, through Jacobson's and Bianconi's frameworks, in spacetime geometry."),
        ("Mathematical Form", 1,
         "Ruppeiner metric: g_ij^R = −∂²S/∂X^i ∂X^j\n  (negative Hessian of entropy w.r.t. extensive variables)\n\nWeinhold metric: g_ij^W = ∂²U/∂S^i ∂S^j\n  (Hessian of internal energy w.r.t. entropy + extensive variables)\n\nRelation: ds²_R = (1/T) ds²_W\n\nIdentity with Fisher-Rao:\n  g_ij^R = g_ij^{FR}(Gibbs)  for the canonical ensemble\n  p(x|θ) = (1/Z) exp(−βH(x))\n  →  g_ij^{FR} = −∂²S/∂X^i ∂X^j = g_ij^R\n\nCurvature: R → ∞ at phase transitions;\n  R < 0 attractive, R > 0 repulsive, R = 0 ideal gas"),
        ("Constraint Category", 2,
         "Geometric (Gm): The Ruppeiner metric is a geometric constraint on thermodynamic state space: it determines the natural distance between thermodynamic states, the geodesics (optimal thermodynamic paths), and the curvature (phase transition signatures). The identity with the Fisher-Rao metric makes this simultaneously a geometric and information-theoretic constraint."),
        ("DS Cross-References", 3,
         "IT08 (Fisher-Rao Metric — the Ruppeiner metric IS the Fisher-Rao metric on the Gibbs canonical ensemble; thermodynamic geometry and information geometry are identical). IT05 (Fisher Information — the Ruppeiner metric tensor is the Fisher information matrix for the canonical distribution, connecting thermodynamic fluctuations to statistical estimation). IT03 (KL Divergence — the Ruppeiner metric is the Hessian of entropy, which is the Legendre transform of the Hessian of KL divergence — the two are connected by the Legendre structure of thermodynamics). GT01 (Jacobson — Jacobson's thermodynamic derivation of gravity, combined with Ruppeiner's identification of thermodynamic and information geometry, suggests that spacetime geometry is ultimately information geometry). GT04 (Bianconi — Bianconi's framework uses the Fisher metric on quantum states to derive gravity; Ruppeiner shows this same metric naturally appears in thermodynamic state space)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe Ruppeiner metric defines optimal paths through thermodynamic state space: geodesics are the most efficient thermodynamic processes. The curvature measures the cost of deviating from optimal paths and diverges at phase transitions where the system becomes infinitely sensitive to perturbations. The metric bridges information theory and thermodynamics through the Fisher-Rao identification."),
        ("What The Math Says", 5,
         "The Ruppeiner metric g-ij-R is the negative Hessian of entropy S with respect to extensive variables X-i and X-j. For a system described by the canonical Gibbs distribution p of x given theta equals 1 over Z times exp of minus beta H of x, the Fisher information matrix g-ij-FR equals the expected value of the product of score functions, which evaluates to minus the second derivative of entropy with respect to extensive variables — exactly the Ruppeiner metric. This proves the identity: thermodynamic geometry IS information geometry for thermal systems. The curvature scalar R of the Ruppeiner metric diverges at second-order phase transitions because thermodynamic fluctuations diverge there — the correlation length goes to infinity, and the metric cannot distinguish nearby states. The sign of R indicates the nature of microscopic interactions: negative curvature for attractive interactions (like in a van der Waals gas below the critical point), positive for repulsive, and zero for ideal (non-interacting) systems."),
        ("Concept Tags", 6,
         "• Ruppeiner metric\n• thermodynamic geometry\n• Hessian of entropy\n• Fisher-Rao identity\n• phase transition curvature\n• Weinhold metric\n• thermodynamic distance\n• information geometry of thermodynamics\n• geodesic thermodynamic path\n• fluctuation geometry"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Gm", 0),
        ("entries", "concept_tags", "Ruppeiner metric, thermodynamic geometry, Hessian of entropy, Fisher-Rao identity, phase transition curvature, Weinhold metric, thermodynamic distance, information geometry of thermodynamics, geodesic thermodynamic path, fluctuation geometry", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "BR04", "Thermodynamic Geometry (Ruppeiner Metric)", "IT08", "Fisher-Rao Metric", "The Ruppeiner metric IS the Fisher-Rao metric on the canonical Gibbs ensemble — they are mathematically identical, proving that thermodynamic geometry is information geometry."),
        ("derives from", "BR04", "Thermodynamic Geometry (Ruppeiner Metric)", "IT05", "Fisher Information", "The Ruppeiner metric tensor is the Fisher information matrix for the canonical distribution — thermodynamic fluctuations are quantified by Fisher information."),
        ("couples to", "BR04", "Thermodynamic Geometry (Ruppeiner Metric)", "GT04", "Bianconi Gravity from Entropy", "Ruppeiner shows the Fisher metric appears naturally in thermodynamic state space; Bianconi shows it generates gravitational dynamics on quantum state space — the same geometric object bridges thermodynamics and gravity."),
    ],
},

{
    "id": "BR05",
    "title": "Dimensional Flow in Quantum Gravity",
    "filename": "BR05_dimensional_flow_quantum_gravity.md",
    "entry_type": "reference_law",
    "scale": "quantum · cosmological",
    "domain": "physics · mathematics",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Dimensional flow (also called dimensional reduction) is the phenomenon where the effective (spectral) dimension of spacetime changes with the scale of observation, flowing from d_spectral ≈ 2 at the Planck scale to d_spectral = 4 at macroscopic scales (Lauscher & Reuter, 2005; Carlip, 2017). This has been observed independently in multiple approaches to quantum gravity — causal dynamical triangulations, asymptotic safety, loop quantum gravity, Horava-Lifshitz gravity, and non-commutative geometry — suggesting it is a universal feature of quantum gravity, not an artifact of any particular formulation. Dimensional flow bridges renormalisation group physics (RG) and gravity-thermodynamics (GT) directly: the spectral dimension runs under a renormalisation group flow, decreasing from 4 to 2 as one probes shorter distances. The value d_spectral ≈ 2 at the Planck scale is significant because in 2 dimensions, the gravitational coupling is dimensionless and gravity is topological — the theory becomes scale-invariant (a UV fixed point of the gravitational RG flow). This connects to the holographic principle: the reduction to 2 effective dimensions at the Planck scale is consistent with the holographic bound S ∝ A, since area is a 2-dimensional quantity."),
        ("Mathematical Form", 1,
         "Spectral dimension: d_s(σ) = −2 d log P(σ)/d log σ\n\nwhere:\n  P(σ) = return probability of a random walk in time σ\n  σ = diffusion time (probing scale)\n\nFlow:\n  d_s(σ → 0) ≈ 2  (Planck scale / UV)\n  d_s(σ → ∞) = 4  (macroscopic / IR)\n\nConnections:\n  d_s = 2 at UV: gravitational coupling G is dimensionless\n  d_s = 2: consistent with S ∝ A (holographic bound)\n  d_s flow: spectral dimension runs under gravitational RG flow"),
        ("Constraint Category", 2,
         "Geometric-Dynamical (Gm-Di): Dimensional flow is a geometric constraint that varies dynamically with scale. The effective dimension of spacetime is not fixed but runs — it is a scale-dependent geometric property. This dynamical geometry connects to the RG (scale dependence) and to holography (area-entropy scaling at d_s = 2)."),
        ("DS Cross-References", 3,
         "RG01 (Wilson RG — dimensional flow is a gravitational RG phenomenon: the spectral dimension runs under the gravitational RG flow from 4 in the IR to 2 in the UV). RG02 (Beta Function — the running of the spectral dimension is governed by the gravitational beta function; d_s = 2 at the UV fixed point where the gravitational coupling is marginal). HB03 (Holographic Principle — d_s ≈ 2 at the Planck scale is consistent with holography: the effective degrees of freedom are 2-dimensional at the smallest scales, matching the area-entropy scaling S ∝ A). GV1 (Einstein Field Equations — dimensional flow modifies the Einstein equations at short distances: the effective theory changes character as the spectral dimension flows from 4 to 2). GT01 (Jacobson — Jacobson's derivation uses 4-dimensional geometry; dimensional flow suggests the derivation must be modified at the Planck scale where d_s ≈ 2)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: dimensional-scaling\n\nDimensional flow is the ultimate dimensional scaling law: the dimension itself is a running quantity, varying with the observation scale. At macroscopic scales, d_s = 4 (standard physics); at the Planck scale, d_s ≈ 2 (holographic, scale-invariant physics). The transition between these regimes is the gravitational RG flow connecting the UV and IR fixed points."),
        ("What The Math Says", 5,
         "The spectral dimension d-s at diffusion scale sigma equals minus 2 times the derivative of the log of the return probability P of sigma with respect to log sigma. On a smooth d-dimensional manifold, P of sigma scales as sigma-to-the-minus-d-over-2, giving d-s equals d (the topological dimension). In quantum gravity, the effective geometry fluctuates, modifying the return probability. Numerical simulations in causal dynamical triangulations show that P of sigma transitions from sigma-to-the-minus-1 (d-s equals 2) at short diffusion times to sigma-to-the-minus-2 (d-s equals 4) at long diffusion times. This flow from 2 to 4 is also obtained analytically in asymptotic safety (where the gravitational coupling has a non-trivial UV fixed point with d-s equals 2), in loop quantum gravity (from the discrete area spectrum), and in Horava-Lifshitz gravity (from the anisotropic scaling). The universality across approaches suggests dimensional flow is a robust feature of quantum gravity, not an artifact. The UV value d-s equals 2 means gravity becomes topological at the Planck scale — a dramatic simplification that may make quantum gravity tractable."),
        ("Concept Tags", 6,
         "• dimensional flow\n• spectral dimension\n• dimensional reduction\n• quantum gravity\n• UV fixed point\n• asymptotic safety\n• causal dynamical triangulations\n• Planck scale\n• running dimension\n• scale-dependent geometry"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Gm-Di", 0),
        ("entries", "concept_tags", "dimensional flow, spectral dimension, dimensional reduction, quantum gravity, UV fixed point, asymptotic safety, causal dynamical triangulations, Planck scale, running dimension, scale-dependent geometry", 0),
        ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "BR05", "Dimensional Flow in Quantum Gravity", "RG01", "Wilson's Renormalisation Group", "Dimensional flow is a gravitational RG phenomenon: the spectral dimension runs under the gravitational renormalisation group flow."),
        ("couples to", "BR05", "Dimensional Flow in Quantum Gravity", "HB03", "Holographic Principle", "The reduction to d_s ≈ 2 at the Planck scale is consistent with holography: 2D effective degrees of freedom match the area-entropy scaling."),
        ("couples to", "BR05", "Dimensional Flow in Quantum Gravity", "GV1", "General Relativity — Einstein Field Equations", "Dimensional flow modifies the Einstein equations at short distances: at d_s ≈ 2, the gravitational coupling becomes dimensionless and gravity becomes topological."),
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
    print(f"Inserting BR pillar ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)

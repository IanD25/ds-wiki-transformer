"""
Pillar Extension — Holographic & Entropy Bounds (HB)
Inserts 8 new reference_law entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Entries:
  HB01: Bekenstein Bound
  HB02: Bekenstein-Hawking Entropy
  HB03: Holographic Principle
  HB04: Hawking Radiation
  HB05: Unruh Effect
  HB06: Black Hole Area Theorem
  HB07: Ryu-Takayanagi Formula
  HB08: Bousso Covariant Entropy Bound
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── HOLOGRAPHIC & ENTROPY BOUNDS ───────────────────────────────────────────

{
    "id": "HB01",
    "title": "Bekenstein Bound",
    "filename": "HB01_bekenstein_bound.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Bekenstein bound S ≤ 2πER/ℏc states that the maximum entropy (equivalently, the maximum information content) of any physical system contained within a sphere of radius R and total energy E is finite and proportional to the product of energy and size (Bekenstein, 1981). This is not merely a limit on our ability to measure — it is a fundamental bound on the number of distinguishable quantum states a region of spacetime can contain. The bound implies that nature has a finite information density: there is a maximum number of bits per unit volume, set by the Planck scale. This connects information theory directly to gravitational physics: the bound arises from requiring that the system not form a black hole, which would have Bekenstein-Hawking entropy proportional to its horizon area."),
        ("Mathematical Form", 1,
         "S ≤ 2πER / ℏc  (in natural units: S ≤ 2πER)\n\nwhere:\n  S = entropy (in nats; divide by ln 2 for bits)\n  E = total energy of the system\n  R = radius of the smallest enclosing sphere\n  ℏ = reduced Planck constant\n  c = speed of light\n\nEquivalently: number of bits ≤ 2πER / (ℏc ln 2)"),
        ("Constraint Category", 2,
         "Thermodynamic-Informatic (Th-In): The Bekenstein bound is simultaneously a thermodynamic constraint (it limits entropy) and an informatic constraint (it limits information content). It is the tightest universal bound on information density in physics, bridging the gap between information theory and general relativity. The bound is saturated by black holes, which are the densest information storage devices allowed by physics."),
        ("DS Cross-References", 3,
         "HB02 (Bekenstein-Hawking Entropy — the BH entropy S = A/4l_P² saturates the Bekenstein bound for black holes; BH entropy is the maximum entropy for a given boundary area). HB03 (Holographic Principle — the Bekenstein bound implies holography: maximal information scales with area, not volume). INFO1 (Shannon Entropy — the Bekenstein bound limits the Shannon entropy of any physical information storage system). TD3 (Second Law — the Bekenstein bound ensures the second law holds even when matter falls into black holes: the total generalised entropy never decreases)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nThe Bekenstein bound is the prototype of an information-theoretic bound arising from gravitational physics. It states that the information content of a physical system is bounded above by a quantity proportional to its energy and linear size. This is the first result showing that spacetime geometry constrains information capacity — the foundational insight that leads to holography and eventually to gravity-from-information programmes."),
        ("What The Math Says", 5,
         "The maximum entropy S of a system with total energy E enclosed in a sphere of radius R is at most 2 pi times E times R divided by h-bar times c. In natural units where h-bar equals c equals 1, this is simply 2 pi E R. The bound counts the maximum number of distinguishable quantum states: converting to bits by dividing by ln 2, you get at most 2 pi E R over h-bar c ln 2 bits. For a 1 kilogram object of radius 1 metre, this gives roughly 10 to the 43 bits — vastly more than any human technology uses, but finite. The bound is saturated by black holes: a black hole of energy E and Schwarzschild radius R = 2GE/c⁴ has entropy exactly equal to the Bekenstein bound. Any attempt to pack more information into the region would cause gravitational collapse to a black hole."),
        ("Concept Tags", 6,
         "• Bekenstein bound\n• information density limit\n• entropy bound\n• holographic limit\n• Planck-scale information\n• black hole saturation\n• information-energy bound\n• maximum entropy\n• quantum states\n• gravitational information bound"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th-In", 0),
        ("entries", "concept_tags", "Bekenstein bound, information density limit, entropy bound, holographic limit, Planck-scale information, black hole saturation, information-energy bound, maximum entropy, quantum states, gravitational information bound", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("constrains", "HB01", "Bekenstein Bound", "INFO1", "Shannon Entropy", "The Bekenstein bound places a finite upper limit on the Shannon entropy (information content) of any physical system — nature has a maximum information density."),
        ("derives from", "HB01", "Bekenstein Bound", "HB02", "Bekenstein-Hawking Entropy", "The Bekenstein bound is derived from requiring consistency with black hole thermodynamics: any system exceeding the bound would form a black hole with higher entropy, violating the second law."),
        ("derives from", "HB01", "Bekenstein Bound", "HB03", "Holographic Principle", "The Bekenstein bound implies holography: since entropy scales as area (E·R ~ R²) rather than volume (R³), the information content of a volume is encoded on its boundary."),
    ],
},

{
    "id": "HB02",
    "title": "Bekenstein-Hawking Entropy",
    "filename": "HB02_bekenstein_hawking_entropy.md",
    "entry_type": "reference_law",
    "scale": "cosmological",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Bekenstein-Hawking entropy S_BH = A/4l_P² = Ak_Bc³/4Gℏ states that the entropy of a black hole is proportional to the area of its event horizon measured in Planck units, not its volume (Bekenstein, 1973; Hawking, 1975). This is the most remarkable formula in theoretical physics because it contains all four fundamental constants (c, G, ℏ, k_B), uniting general relativity, quantum mechanics, and thermodynamics in a single equation. The entropy counts the number of microscopic quantum states consistent with the macroscopic black hole — but the area-proportionality means these states live on the two-dimensional boundary, not in the three-dimensional interior. This is the origin of the holographic principle. The Bekenstein-Hawking entropy has been reproduced by string theory microstate counting (Strominger & Vafa, 1996) and is now understood to equal the entanglement entropy of quantum fields across the event horizon."),
        ("Mathematical Form", 1,
         "S_BH = A / 4l_P²  =  Ak_Bc³ / 4Gℏ\n\nwhere:\n  A = area of the event horizon\n  l_P = √(ℏG/c³) ≈ 1.616 × 10⁻³⁵ m  (Planck length)\n  G = Newton's gravitational constant\n  k_B = Boltzmann constant\n\nFor a Schwarzschild black hole of mass M:\n  A = 16πG²M²/c⁴\n  S_BH = 4πGM²k_B / ℏc"),
        ("Constraint Category", 2,
         "Thermodynamic-Geometric (Th-Gm): The BH entropy is simultaneously a thermodynamic quantity (it obeys the laws of black hole thermodynamics) and a geometric quantity (it equals the horizon area in Planck units). This dual nature is the deepest clue that thermodynamics and geometry are fundamentally related — the central insight of the gravity-from-thermodynamics programme."),
        ("DS Cross-References", 3,
         "IT02 (Von Neumann Entropy — BH entropy equals the entanglement entropy of quantum fields across the horizon; the von Neumann entropy of the exterior state). HB01 (Bekenstein Bound — BH entropy saturates the Bekenstein bound; black holes are maximally entropic). HB04 (Hawking Radiation — Hawking radiation carries entropy away from the black hole at temperature T = ℏc³/8πGMk_B). HB06 (Black Hole Area Theorem — the area theorem dA/dt ≥ 0 is the second law for black holes). GT01 (Jacobson's Derivation — Jacobson showed that Einstein's equations follow from requiring the entropy-area proportionality to hold for all local causal horizons). HB07 (Ryu-Takayanagi — generalises BH entropy to holographic entanglement entropy in AdS/CFT)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nBekenstein-Hawking entropy is the prototype of a geometric entropy: a thermodynamic quantity that equals a geometric measure (area in Planck units). It bounds the information content of any region from above (holography), and its area-proportionality — rather than volume-proportionality — is the defining signature of holographic physics. Every gravity-from-information programme ultimately traces back to explaining why S = A/4l_P²."),
        ("What The Math Says", 5,
         "The entropy of a black hole equals the area of its event horizon A divided by 4 times the Planck length squared l-P-squared. The Planck length l-P equals the square root of h-bar times G over c-cubed, approximately 1.6 times 10-to-the-minus-35 metres. For a Schwarzschild black hole of mass M, the area is 16 pi G-squared M-squared over c-to-the-fourth, giving entropy 4 pi G M-squared k-B over h-bar c. This entropy is enormous: a solar-mass black hole has entropy roughly 10-to-the-77 in units of k-B, far exceeding the entropy of the pre-collapse star. The formula contains all four fundamental constants: c from relativity, G from gravity, h-bar from quantum mechanics, and k-B from thermodynamics — it is the unique meeting point of all four pillars of physics."),
        ("Concept Tags", 6,
         "• Bekenstein-Hawking entropy\n• black hole entropy\n• area-entropy proportionality\n• holographic entropy\n• Planck area\n• event horizon\n• entanglement entropy\n• four fundamental constants\n• microstate counting\n• geometric entropy"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th-Gm", 0),
        ("entries", "concept_tags", "Bekenstein-Hawking entropy, black hole entropy, area-entropy proportionality, holographic entropy, Planck area, event horizon, entanglement entropy, four fundamental constants, microstate counting, geometric entropy", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("analogous to", "HB02", "Bekenstein-Hawking Entropy", "IT02", "Von Neumann Entropy", "BH entropy equals the entanglement entropy (von Neumann entropy of the reduced state) of quantum fields across the event horizon — the gravitational and quantum information descriptions are identical."),
        ("derives from", "HB02", "Bekenstein-Hawking Entropy", "HB06", "Black Hole Area Theorem", "The area theorem dA/dt ≥ 0 becomes the second law dS/dt ≥ 0 when entropy is proportional to area — Bekenstein's original insight."),
        ("couples to", "HB02", "Bekenstein-Hawking Entropy", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Jacobson reversed the logic: assuming S = A/4l_P² for all local Rindler horizons, he derived the Einstein field equations as the equation of state of spacetime."),
    ],
},

{
    "id": "HB03",
    "title": "Holographic Principle",
    "filename": "HB03_holographic_principle.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The holographic principle states that the maximum entropy — hence maximum information content — of any region of space is proportional to the area of its boundary, not its volume (t'Hooft, 1993; Susskind, 1995). A three-dimensional volume can contain at most one bit per Planck area (l_P² ≈ 2.6 × 10⁻⁷⁰ m²) of its enclosing surface. This implies that the fundamental degrees of freedom of a gravitational theory are two-dimensional, not three-dimensional — the bulk physics is a holographic projection of boundary data. The holographic principle is realised concretely in the AdS/CFT correspondence, where a gravitational theory in (d+1)-dimensional anti-de Sitter space is exactly dual to a non-gravitational conformal field theory on its d-dimensional boundary."),
        ("Mathematical Form", 1,
         "S_max(V) ≤ A(∂V) / 4l_P²\n\nwhere:\n  S_max = maximum entropy of region V\n  A(∂V) = area of the boundary ∂V\n  l_P² = ℏG/c³  (Planck area)\n\nInformation capacity: I_max ≤ A / (4l_P² ln 2)  bits\n\nDimensional reduction: d+1 bulk dimensions ↔ d boundary dimensions"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): The holographic principle is both an information bound (maximum entropy scales as area) and a geometric principle (the degrees of freedom are lower-dimensional than the space they describe). It is the most radical constraint on information in physics: the apparent three-dimensionality of space is emergent from two-dimensional boundary information."),
        ("DS Cross-References", 3,
         "HB01 (Bekenstein Bound — the holographic principle follows from the Bekenstein bound: the energy-radius scaling implies area-proportional information content). HB02 (Bekenstein-Hawking Entropy — BH entropy is the prototype holographic entropy: area-proportional, not volume-proportional). BR02 (AdS/CFT Correspondence — the concrete realisation of holography: a gravitational bulk is exactly dual to a non-gravitational boundary theory). HB07 (Ryu-Takayanagi — computes entanglement entropy holographically as a minimal surface area in the bulk). BR03 (Van Raamsdonk — spacetime connectivity is built from entanglement, the mechanism underlying holographic encoding)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: dimensional-scaling\n\nThe holographic principle is a dimensional scaling law: information scales as L^(d-1) (area) rather than L^d (volume) where d is the spatial dimension. This anomalous scaling is the signature of gravitational systems and distinguishes them from ordinary quantum systems where entropy is extensive (volume-scaling). The dimensional reduction is the deepest known constraint on the structure of quantum gravity."),
        ("What The Math Says", 5,
         "The maximum entropy of a spatial region V is at most the area A of its boundary divided by 4 times the Planck area l-P-squared, where the Planck area equals h-bar times G over c-cubed, roughly 2.6 times 10-to-the-minus-70 square metres. Converting to bits by dividing by ln 2, the maximum information content is about 1.4 times 10-to-the-69 bits per square metre of boundary. For a room-sized volume of 10 cubic metres, the holographic limit is roughly 10-to-the-70 bits — encoded on the walls, not in the interior. The dimensional reduction from d+1 bulk dimensions to d boundary dimensions means that the true degrees of freedom of a gravitational theory live on the boundary: the interior is a holographic projection."),
        ("Concept Tags", 6,
         "• holographic principle\n• area-entropy scaling\n• information bound\n• dimensional reduction\n• boundary degrees of freedom\n• Planck area\n• AdS/CFT\n• holographic encoding\n• bulk-boundary duality\n• emergent dimensionality"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "holographic principle, area-entropy scaling, information bound, dimensional reduction, boundary degrees of freedom, Planck area, AdS/CFT, holographic encoding, bulk-boundary duality, emergent dimensionality", 0),
        ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "HB03", "Holographic Principle", "HB02", "Bekenstein-Hawking Entropy", "The holographic principle generalises the BH area-entropy relation from black holes to all bounded regions of space — the area-entropy proportionality is universal."),
        ("constrains", "HB03", "Holographic Principle", "INFO1", "Shannon Entropy", "The holographic principle places a geometric upper bound on the Shannon entropy of any physical system: information capacity is proportional to boundary area, not enclosed volume."),
        ("couples to", "HB03", "Holographic Principle", "BR02", "AdS/CFT Correspondence", "AdS/CFT is the concrete, mathematically precise realisation of the holographic principle: a gravitational bulk theory is exactly dual to a boundary conformal field theory."),
    ],
},

{
    "id": "HB04",
    "title": "Hawking Radiation",
    "filename": "HB04_hawking_radiation.md",
    "entry_type": "reference_law",
    "scale": "quantum · cosmological",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Hawking radiation is the thermal radiation predicted to be emitted by black holes due to quantum effects near the event horizon, at a temperature T_H = ℏc³/8πGMk_B (Hawking, 1974, 1975). The radiation arises because the vacuum state of quantum fields in the presence of a horizon contains particle pairs: one particle escapes to infinity while its partner falls behind the horizon. The outgoing radiation is exactly thermal (Planckian) with temperature inversely proportional to the black hole mass. Hawking radiation is fundamentally an information-theoretic phenomenon: it demonstrates that horizons convert quantum vacuum fluctuations into real particles, transferring information from behind the horizon to the exterior. The information paradox — whether the radiation is truly thermal (information-destroying) or subtly encodes the black hole's quantum state — remains one of the deepest open problems in theoretical physics."),
        ("Mathematical Form", 1,
         "T_H = ℏc³ / 8πGMk_B\n\nLuminosity: L = ℏc⁶ / (15360π G²M²)\n\nEvaporation time: t_evap = 5120πG²M³ / ℏc⁴\n\nEntropy: S = A/4l_P² = 4πGM²k_B/ℏc\n\nSpectrum: thermal (Planckian) at temperature T_H"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): Hawking radiation establishes black holes as thermodynamic objects with a well-defined temperature, entropy, and luminosity. The temperature is inversely proportional to mass, so smaller black holes are hotter and radiate faster — leading to eventual evaporation. This connects quantum field theory, general relativity, and thermodynamics in a single physical process."),
        ("DS Cross-References", 3,
         "HB02 (Bekenstein-Hawking Entropy — Hawking radiation carries entropy at temperature T_H, validating the BH entropy formula). HB05 (Unruh Effect — the Unruh effect is the flat-spacetime analog of Hawking radiation: an accelerating observer sees thermal radiation at temperature T = ℏa/2πck_B). TD3 (Second Law — black hole evaporation via Hawking radiation tests the generalised second law: total entropy including radiation must increase). RD1 (Planck's Law — Hawking radiation has a Planckian spectrum, connecting black hole physics to quantum statistical mechanics)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nHawking radiation establishes a fundamental link between horizons and thermal physics: any event horizon radiates thermally. The temperature T_H sets the energy scale at which quantum and gravitational effects become equally important for a black hole of mass M. The inverse mass-temperature relation T ∝ 1/M means the radiation is a runaway process (negative specific heat), ultimately ending in complete evaporation — a unique thermodynamic behaviour not seen in ordinary matter."),
        ("What The Math Says", 5,
         "The Hawking temperature of a black hole of mass M is h-bar times c-cubed divided by 8 pi G M k-B. For a solar-mass black hole this gives roughly 60 nanokelvins — far below the cosmic microwave background temperature, so solar-mass black holes absorb more than they emit. The luminosity scales as 1 over M-squared, meaning the black hole radiates faster as it loses mass, leading to a runaway evaporation. The evaporation time scales as M-cubed: a solar-mass black hole takes roughly 10-to-the-67 years to evaporate, but a mountain-mass black hole (10-to-the-12 kg) would evaporate in the age of the universe. The spectrum is exactly Planckian — a perfect blackbody — which is the origin of the information paradox: a thermal spectrum contains no information about the initial state that formed the black hole."),
        ("Concept Tags", 6,
         "• Hawking radiation\n• black hole temperature\n• Hawking temperature\n• quantum vacuum fluctuations\n• event horizon\n• information paradox\n• black hole evaporation\n• thermal radiation\n• negative specific heat\n• Planckian spectrum"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Hawking radiation, black hole temperature, Hawking temperature, quantum vacuum fluctuations, event horizon, information paradox, black hole evaporation, thermal radiation, negative specific heat, Planckian spectrum", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "HB04", "Hawking Radiation", "HB02", "Bekenstein-Hawking Entropy", "Hawking radiation validates the BH entropy formula by providing the thermodynamic temperature T_H, completing the analogy between black hole mechanics and thermodynamics."),
        ("analogous to", "HB04", "Hawking Radiation", "HB05", "Unruh Effect", "The Unruh effect is the flat-spacetime analog: an accelerating observer sees thermal radiation at T = ℏa/2πck_B, structurally identical to Hawking radiation via the equivalence principle."),
        ("analogous to", "HB04", "Hawking Radiation", "RD1", "Planck's Radiation Law", "Hawking radiation has a perfect Planckian spectrum — the black hole is an ideal blackbody, connecting gravitational quantum effects to the foundational law of quantum statistical mechanics."),
    ],
},

{
    "id": "HB05",
    "title": "Unruh Effect",
    "filename": "HB05_unruh_effect.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Unruh effect states that a uniformly accelerating observer in flat Minkowski spacetime perceives the vacuum state of quantum fields as a thermal bath at temperature T = ℏa/2πck_B, where a is the proper acceleration (Unruh, 1976). An inertial observer sees empty space; an accelerating observer sees thermal particles. This effect reveals that the particle concept in quantum field theory is observer-dependent — the notion of a vacuum depends on the observer's state of motion. The Unruh effect is the flat-spacetime version of Hawking radiation: through the equivalence principle, acceleration in flat spacetime is locally equivalent to a gravitational field, and both produce thermal spectra. The Unruh temperature is the key ingredient in Jacobson's thermodynamic derivation of general relativity and in Verlinde's entropic gravity."),
        ("Mathematical Form", 1,
         "T_U = ℏa / 2πck_B\n\nwhere:\n  a = proper acceleration (m/s²)\n  T_U = Unruh temperature (K)\n\nFor a = 1 m/s²: T_U ≈ 4 × 10⁻²¹ K (experimentally inaccessible)\nFor a = g ≈ 10 m/s²: T_U ≈ 4 × 10⁻²⁰ K\n\nThe Minkowski vacuum |0⟩_M expressed in Rindler modes:\n  |0⟩_M = Π_k (1/cosh r_k) Σ_n (tanh r_k)^n |n⟩_L ⊗ |n⟩_R  (thermofield double)"),
        ("Constraint Category", 2,
         "Thermodynamic-Geometric (Th-Gm): The Unruh effect is a geometric-thermodynamic constraint: acceleration creates an effective horizon (the Rindler horizon), and horizons produce thermal radiation. The temperature is fixed by geometry — the acceleration — with no free parameters. This observer-dependence of vacuum and temperature is a geometric constraint on the structure of quantum field theory."),
        ("DS Cross-References", 3,
         "HB04 (Hawking Radiation — Hawking radiation is the curved-spacetime analog; both are instances of the principle that horizons radiate thermally). GT01 (Jacobson's Derivation — Jacobson uses the Unruh temperature as input: the local temperature seen by accelerating observers near any causal horizon determines the Einstein equations). GT02 (Verlinde Entropic Gravity — Verlinde's entropic force uses the Unruh temperature T = ℏa/2πck_B as the temperature associated with gravitational acceleration). GT08 (Equivalence Principle — the Unruh effect is the quantum manifestation of the equivalence principle: acceleration and gravity produce equivalent thermal effects)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nThe Unruh effect establishes a universal temperature-acceleration correspondence: every acceleration defines a temperature, and every horizon radiates. The temperature is set by geometry (acceleration) with no material properties involved — it is a pure spacetime effect. This universality makes it a cornerstone of the gravity-thermodynamics programme."),
        ("What The Math Says", 5,
         "The Unruh temperature equals h-bar times the proper acceleration a divided by 2 pi times c times k-B. For an acceleration of 1 metre per second squared, this gives roughly 4 times 10-to-the-minus-21 kelvin — extraordinarily small and far below experimental detection. The deep mathematical content is in the thermofield double structure: the Minkowski vacuum expressed in Rindler coordinates (natural for the accelerating observer) is an entangled state where each mode with Rindler frequency omega-k appears as a pair with equal occupation number on both sides of the Rindler horizon. Tracing over the modes behind the horizon produces a thermal density matrix at the Unruh temperature. The observer-dependence of the vacuum means that particles and temperature are not absolute concepts but depend on the observer's causal structure."),
        ("Concept Tags", 6,
         "• Unruh effect\n• Unruh temperature\n• accelerating observer\n• Rindler horizon\n• observer-dependent vacuum\n• thermofield double\n• thermal bath\n• equivalence principle\n• horizon temperature\n• Rindler modes"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th-Gm", 0),
        ("entries", "concept_tags", "Unruh effect, Unruh temperature, accelerating observer, Rindler horizon, observer-dependent vacuum, thermofield double, thermal bath, equivalence principle, horizon temperature, Rindler modes", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("analogous to", "HB05", "Unruh Effect", "HB04", "Hawking Radiation", "Hawking radiation and the Unruh effect are the curved and flat spacetime instances of the same phenomenon: horizons radiate thermally. Related by the equivalence principle."),
        ("couples to", "HB05", "Unruh Effect", "GT01", "Jacobson's Thermodynamic Derivation of Einstein Equations", "Jacobson uses the Unruh temperature as the local temperature of accelerating observers near causal horizons — this input, combined with the entropy-area relation, yields Einstein's equations."),
        ("couples to", "HB05", "Unruh Effect", "GT08", "Equivalence Principle", "The Unruh effect is the quantum expression of the equivalence principle: acceleration and gravity produce identical thermal effects, linking quantum field theory to gravitational physics."),
    ],
},

{
    "id": "HB06",
    "title": "Black Hole Area Theorem",
    "filename": "HB06_black_hole_area_theorem.md",
    "entry_type": "reference_law",
    "scale": "cosmological",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Hawking's area theorem states that the total area of black hole event horizons can never decrease in any classical process: dA/dt ≥ 0, assuming the null energy condition holds (Hawking, 1971). When two black holes merge, the area of the final black hole is at least as large as the sum of the initial areas. This is the gravitational analog of the second law of thermodynamics: if entropy is proportional to area (Bekenstein-Hawking), then the area theorem IS the second law for black holes. The theorem established the first formal connection between black hole mechanics and thermodynamics. Quantum effects (Hawking radiation) violate the classical area theorem, but the generalised second law — total area plus matter entropy — remains valid."),
        ("Mathematical Form", 1,
         "dA/dt ≥ 0  (classical, assuming null energy condition)\n\nMerger bound: A_final ≥ A_1 + A_2\n\nGeneralised second law: d(A/4l_P² + S_outside)/dt ≥ 0\n  (Bekenstein, 1972 — holds even with quantum effects)\n\nFour laws of black hole mechanics:\n  0th: surface gravity κ is constant (↔ zeroth law, T constant)\n  1st: dM = (κ/8πG)dA + ΩdJ + ΦdQ  (↔ dE = TdS + work)\n  2nd: dA ≥ 0  (↔ dS ≥ 0)\n  3rd: κ → 0 unattainable  (↔ T → 0 unattainable)"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): The area theorem is the gravitational second law — it constrains the direction of gravitational processes just as the second law constrains thermodynamic processes. The monotonicity of area is the monotonicity of gravitational entropy. Combined with the four laws of black hole mechanics, it establishes a complete formal analogy between black hole physics and thermodynamics."),
        ("DS Cross-References", 3,
         "TD3 (Second Law of Thermodynamics — the area theorem is the gravitational version of the second law: area plays the role of entropy, surface gravity plays the role of temperature). HB02 (Bekenstein-Hawking Entropy — the area theorem becomes the second law when S = A/4l_P²). INFO4 (Data Processing Inequality — the DPI states that information processing can only destroy information; the area theorem states that gravitational processes can only increase entropy; both are monotonicity/irreversibility statements). NE03 (Jarzynski Equality — Jarzynski extends the second law to fluctuating systems; the area theorem is the gravitational analog awaiting a fluctuation-theorem generalisation)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe area theorem is a monotonicity law rather than a strict conservation law — area can increase but never decrease. It is analogous to entropy in thermodynamics and mutual information loss in information processing. The monotonicity structure (irreversibility) is the common thread linking the second law, the data processing inequality, and the c-theorem in renormalisation group flow."),
        ("What The Math Says", 5,
         "The area of a black hole event horizon A is a non-decreasing function of time: dA over dt is greater than or equal to zero, provided the null energy condition holds (meaning matter has non-negative energy as seen by any light ray). When two black holes with areas A-1 and A-2 merge, the resulting black hole has area at least A-1 plus A-2. The four laws of black hole mechanics parallel the four laws of thermodynamics exactly: constant surface gravity parallels constant temperature (zeroth law); the first law dM equals kappa over 8 pi G times dA plus work terms parallels dE equals T dS plus work; the area theorem parallels the second law; and the unattainability of zero surface gravity parallels the third law. The generalised second law adds the entropy of matter outside the black hole: the total d of A over 4 l-P-squared plus S-outside over dt is non-negative, even when Hawking radiation causes the area to decrease."),
        ("Concept Tags", 6,
         "• area theorem\n• black hole mechanics\n• gravitational second law\n• monotonicity\n• null energy condition\n• generalised second law\n• surface gravity\n• irreversibility\n• entropy increase\n• four laws of black hole mechanics"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "area theorem, black hole mechanics, gravitational second law, monotonicity, null energy condition, generalised second law, surface gravity, irreversibility, entropy increase, four laws of black hole mechanics", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("analogous to", "HB06", "Black Hole Area Theorem", "TD3", "Second Law of Thermodynamics", "The area theorem is the gravitational second law: horizon area plays the role of entropy, surface gravity plays the role of temperature. The formal analogy is exact."),
        ("derives from", "HB06", "Black Hole Area Theorem", "HB02", "Bekenstein-Hawking Entropy", "The area theorem dA/dt ≥ 0 becomes the second law dS/dt ≥ 0 when S = A/4l_P² — the area theorem motivated Bekenstein's entropy proposal."),
        ("analogous to", "HB06", "Black Hole Area Theorem", "INFO4", "Mutual Information and Data Processing Inequality", "Both are monotonicity/irreversibility statements: the DPI says information processing only destroys information; the area theorem says gravitational processes only increase entropy."),
    ],
},

{
    "id": "HB07",
    "title": "Ryu-Takayanagi Formula",
    "filename": "HB07_ryu_takayanagi_formula.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Ryu-Takayanagi (RT) formula S_A = Area(γ_A)/4G_N states that the entanglement entropy of a boundary region A in the AdS/CFT correspondence equals the area of the minimal surface γ_A in the bulk that is homologous to A, divided by 4G_N (Ryu & Takayanagi, 2006). This is a holographic formula: it computes a quantum information quantity (entanglement entropy) using a geometric quantity (minimal surface area). The RT formula generalises the Bekenstein-Hawking entropy from black hole horizons to arbitrary boundary subregions in holographic theories. Its quantum correction (the Faulkner-Lewkowycz-Maldacena generalisation) adds the bulk entanglement entropy across the minimal surface. The RT formula has been proven from first principles in AdS/CFT (Lewkowycz & Maldacena, 2013) and is the most concrete realisation of the idea that geometry encodes quantum information."),
        ("Mathematical Form", 1,
         "S_A = Area(γ_A) / 4G_N\n\nwhere:\n  S_A = entanglement entropy of boundary region A\n  γ_A = minimal area surface in the bulk homologous to A\n  G_N = Newton's constant in the bulk\n\nQuantum-corrected (FLM):\n  S_A = Area(γ_A)/4G_N + S_bulk(Σ_A) + O(G_N)\n\nwhere S_bulk(Σ_A) is the von Neumann entropy of bulk fields on\nthe entanglement wedge Σ_A bounded by A ∪ γ_A"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): The RT formula is a geometric-informatic identity: it equates an information-theoretic quantity (entanglement entropy, defined via von Neumann entropy) with a geometric quantity (minimal surface area, defined via Riemannian geometry). It satisfies strong subadditivity as a geometric consequence, and the monogamy of entanglement becomes a geometric nesting property of minimal surfaces."),
        ("DS Cross-References", 3,
         "HB02 (Bekenstein-Hawking Entropy — RT generalises BH entropy: for a boundary region equal to the entire boundary, γ_A is the black hole horizon and S_A = S_BH). IT02 (Von Neumann Entropy — the entanglement entropy S_A is a von Neumann entropy: S_A = −Tr(ρ_A log ρ_A) where ρ_A is the reduced density matrix of region A). BR02 (AdS/CFT Correspondence — RT lives within AdS/CFT: it computes boundary entanglement using bulk geometry). BR03 (Van Raamsdonk — RT motivates Van Raamsdonk's conjecture that entanglement builds spacetime: removing entanglement causes the minimal surface to grow, eventually disconnecting the geometry)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe RT formula involves a minimisation: find the bulk surface with smallest area that is homologous to the boundary region A. This extremal surface prescription is an optimization principle that connects the variational structure of geometry (minimal surfaces, geodesics) to the information-theoretic structure of entanglement (entropy maximisation). The surface is both a geometric extremum and an information-theoretic saddle point."),
        ("What The Math Says", 5,
         "The entanglement entropy of a boundary region A in the holographic CFT equals the area of the minimal-area bulk surface gamma-A that ends on the boundary of A, divided by 4 times Newton's constant G-N. The surface gamma-A must be homologous to A: there must be a bulk region whose boundary is A union gamma-A. This is a holographic dictionary entry: a quantum quantity on the boundary (entanglement entropy) equals a classical quantity in the bulk (area). The quantum-corrected FLM formula adds the von Neumann entropy of bulk quantum fields on the entanglement wedge — the bulk region between A and gamma-A. The RT formula satisfies strong subadditivity geometrically: the minimal surface for A union B has area at most the sum of areas for A and B separately, which is the content of S(AB) at most S(A) plus S(B)."),
        ("Concept Tags", 6,
         "• Ryu-Takayanagi formula\n• holographic entanglement entropy\n• minimal surface\n• AdS/CFT\n• entanglement wedge\n• FLM correction\n• boundary-bulk duality\n• geometric entanglement\n• holographic dictionary\n• strong subadditivity"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "Ryu-Takayanagi formula, holographic entanglement entropy, minimal surface, AdS/CFT, entanglement wedge, FLM correction, boundary-bulk duality, geometric entanglement, holographic dictionary, strong subadditivity", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "HB07", "Ryu-Takayanagi Formula", "HB02", "Bekenstein-Hawking Entropy", "RT generalises BH entropy to arbitrary boundary subregions in holographic theories — for the full boundary, the RT surface is the black hole horizon."),
        ("couples to", "HB07", "Ryu-Takayanagi Formula", "IT02", "Von Neumann Entropy", "The entanglement entropy S_A computed by RT is a von Neumann entropy: S_A = −Tr(ρ_A log ρ_A) — RT provides the geometric dual of this quantum information quantity."),
        ("derives from", "HB07", "Ryu-Takayanagi Formula", "BR02", "AdS/CFT Correspondence", "The RT formula is derived within AdS/CFT — it is a consequence of the holographic duality applied to entanglement entropy computation."),
    ],
},

{
    "id": "HB08",
    "title": "Bousso Covariant Entropy Bound",
    "filename": "HB08_bousso_covariant_entropy_bound.md",
    "entry_type": "reference_law",
    "scale": "cosmological",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Bousso bound (covariant entropy bound) states that the entropy passing through any light sheet L(B) — a null hypersurface generated by non-expanding light rays orthogonal to a codimension-2 surface B — is bounded by the area of B divided by 4G_N: S[L(B)] ≤ A(B)/4G_N (Bousso, 1999). This is the covariant generalisation of the holographic principle. Unlike the Bekenstein bound, which applies to spatial regions and can fail in cosmological contexts, the Bousso bound is valid in all spacetimes including expanding universes, black hole interiors, and cosmological horizons. It is the most general formulation of holography: the entropy flowing through any light sheet is bounded by the area of the surface that generates it."),
        ("Mathematical Form", 1,
         "S[L(B)] ≤ A(B) / 4G_N\n\nwhere:\n  B = codimension-2 spacelike surface\n  L(B) = light sheet: null hypersurface generated by\n         non-expanding orthogonal null geodesics from B\n  S[L(B)] = total entropy passing through L(B)\n  A(B) = area of B\n\nLight sheet condition: θ ≤ 0  (null expansion is non-positive)"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): The Bousso bound is a covariant information-geometric constraint: it bounds information content using null geometry (light sheets). It is formulated covariantly — no preferred time slicing needed — making it valid in arbitrary curved spacetimes. The bound connects the causal structure of spacetime (light rays) to its information content (entropy), showing that geometry constrains information flow."),
        ("DS Cross-References", 3,
         "HB01 (Bekenstein Bound — Bousso generalises Bekenstein to arbitrary spacetimes; the Bekenstein bound is the special case for nearly flat space). HB03 (Holographic Principle — the Bousso bound is the covariant, rigorous version of the holographic principle that applies to all spacetimes). HB02 (Bekenstein-Hawking Entropy — BH entropy saturates the Bousso bound on the black hole horizon's light sheet). GV1 (Einstein Field Equations — the Bousso bound uses the Raychaudhuri equation, which is derived from Einstein's equations, to construct light sheets)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nThe Bousso bound is the most general entropy bound in physics — it subsumes the Bekenstein bound and the holographic principle as special cases. Its covariance (independence of observer or time slicing) makes it the natural information-theoretic constraint compatible with general relativity. The light sheet construction connects information bounds to the causal structure of spacetime."),
        ("What The Math Says", 5,
         "Given any codimension-2 spacelike surface B, construct a light sheet L of B by sending null geodesics orthogonal to B in a direction where the null expansion theta is non-positive (meaning the light rays are not diverging). The total entropy S passing through this light sheet is at most the area of B divided by 4 G-N. The condition theta less than or equal to zero selects the correct direction of the light sheet and ensures the bound is not trivially violated by choosing diverging light rays. In flat spacetime, the Bousso bound reduces to the Bekenstein bound. In cosmological spacetimes where the Bekenstein bound fails (because arbitrarily large entropy can exist in large volumes), the Bousso bound remains valid because the light sheet captures only the entropy that flows through the null surface. For a black hole horizon, the light sheet is the ingoing future null surface, and the bound is saturated — the entropy passing through is exactly A over 4 G-N."),
        ("Concept Tags", 6,
         "• Bousso bound\n• covariant entropy bound\n• light sheet\n• null hypersurface\n• null expansion\n• covariant holography\n• entropy flow\n• causal structure\n• Raychaudhuri equation\n• spacetime information bound"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "Bousso bound, covariant entropy bound, light sheet, null hypersurface, null expansion, covariant holography, entropy flow, causal structure, Raychaudhuri equation, spacetime information bound", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "HB08", "Bousso Covariant Entropy Bound", "HB01", "Bekenstein Bound", "The Bousso bound generalises the Bekenstein bound to arbitrary spacetimes using covariant light sheet construction — Bekenstein is the flat-space special case."),
        ("generalizes", "HB08", "Bousso Covariant Entropy Bound", "HB03", "Holographic Principle", "The Bousso bound is the rigorous covariant formulation of the holographic principle — it provides the precise statement of how area bounds entropy in all spacetimes."),
        ("couples to", "HB08", "Bousso Covariant Entropy Bound", "GV1", "General Relativity — Einstein Field Equations", "The Bousso bound uses the Raychaudhuri equation (derived from Einstein's equations) to define light sheets — it is a general-relativistic information bound."),
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
    print(f"Inserting HB pillar ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)

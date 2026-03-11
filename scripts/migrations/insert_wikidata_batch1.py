"""
insert_wikidata_batch1.py — 10 high-priority entries seeded from Wikidata physical laws.

New entries:
  CM9   Hooke's Law
  CM10  Conservation of Momentum
  CM11  Conservation of Energy
  EM12  Ampère's Circuital Law
  EM13  Wiedemann–Franz Law
  TD14  van der Waals Equation
  GV4   Hubble–Lemaître Law
  FM7   Darcy's Law
  CR1   Bragg's Law              [new cluster: crystallography/scattering]
  MS1   Young's Modulus          [new cluster: materials science]

Wikidata QIDs:  Q170282, Q2305665, Q11382, Q51500, Q944030,
                Q254329, Q179916, Q392416, Q847354, Q2091584

Safe to re-run — INSERT OR IGNORE guards.
Run from project root:
    python3 scripts/insert_wikidata_batch1.py
"""
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── CLASSICAL MECHANICS ───────────────────────────────────────────────────────

{
    "id": "CM9",
    "title": "Hooke's Law",
    "filename": "CM9_hookes_law.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Within the elastic limit, the restoring force exerted by a spring or elastic material is proportional to the displacement from equilibrium and directed against it (Hooke, 1678). The constant of proportionality k encodes the stiffness of the system. Beyond the elastic limit the proportionality breaks down and the material yields or fractures. Hooke's Law is the linearisation of virtually all restoring-force physics around a stable equilibrium point."),
        ("Mathematical Form", 1,
         "F = −kx\n\nFor materials (uniaxial stress):\n  σ = E ε   (Young's modulus form)\n  where σ = F/A (stress, Pa), ε = ΔL/L (dimensionless strain), E = Young's modulus (Pa)\n\nElastic potential energy: U = ½kx²"),
        ("Constraint Category", 2,
         "Geometric/Thermodynamic (Ge/Th): the linear restoring force is the leading-order term in a Taylor expansion of any potential energy around a stable minimum — a geometric consequence of differentiability. The elastic energy U=½kx² is the minimal non-trivial potential. D-sensitive: k scales with material cross-section and length (k = EA/L for a rod)."),
        ("DS Cross-References", 3,
         "CM1 (Newton's Laws — Hooke's force F=−kx enters Newton's F=ma to give the harmonic oscillator ẍ+ω²x=0, ω=√(k/m)). AM1/AM2 (Principle of Least Action / Euler–Lagrange — the harmonic oscillator Lagrangian L=½mẋ²−½kx² is the canonical Euler–Lagrange example). TD5 (Fundamental Thermodynamic Relation — elastic energy U=½kx² contributes to the internal energy of a deformed solid). MS1 (Young's Modulus — the three-dimensional uniaxial generalisation of Hooke's Law)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nHooke's Law is the archetype of all linear response: output (force) is proportional to input (displacement). It defines the harmonic oscillator — the universal linearisation of any potential near a minimum. Every oscillatory system in the DS framework that is operating near equilibrium implicitly invokes Hooke's Law as its lowest-order approximation."),
        ("What The Math Says", 5,
         "The force F equals minus k times displacement x: the minus sign ensures the force opposes displacement, creating a stable equilibrium at x equals zero. The spring constant k has units of newtons per metre and encodes both material stiffness and geometry. For a rod of cross-section A, length L, and Young's modulus E, k equals EA over L. The elastic potential energy stored is one-half k x squared, recoverable on release. The harmonic oscillator equation m times x-double-dot plus k times x equals zero has the solution x of t equals A cosine of omega t plus phi, where omega equals the square root of k over m — the natural frequency. Any system expanded around a stable potential minimum to leading order behaves as a Hooke's Law oscillator."),
        ("Concept Tags", 6,
         "• Hooke's Law\n• spring constant\n• elastic restoring force\n• harmonic oscillator\n• elastic limit\n• Young's modulus\n• linear response\n• elastic potential energy\n• constitutive relation\n• stiffness"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Hooke's Law, spring constant, elastic restoring force, harmonic oscillator, elastic limit, Young's modulus, linear response, elastic potential energy, constitutive relation, stiffness", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "CM9", "Hooke's Law", "CM1", "Newton's Laws of Motion",
         "Hooke's restoring force F=−kx enters Newton's second law to give the harmonic oscillator equation mẍ=−kx; Hooke's Law is a constitutive force law consistent with Newton's framework."),
        ("analogous to", "CM9", "Hooke's Law", "DM1", "Fick's Laws of Diffusion",
         "Both are linear response laws: Fick's J=−D∇c and Hooke's F=−kx both express flux (or force) proportional to a gradient (or displacement) — the same mathematical structure underlying all Fickian/Hookean transport."),
        ("analogous to", "CM9", "Hooke's Law", "TD10", "Fourier's Law of Heat Conduction",
         "Fourier's q=−k∇T and Hooke's F=−kx are both linear constitutive relations mapping a gradient to a flux or force; all three (Hooke, Fick, Fourier) are members of the linear-response family."),
    ],
},

{
    "id": "CM10",
    "title": "Conservation of Momentum",
    "filename": "CM10_conservation_momentum.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The total linear momentum of an isolated system is constant in time. Equivalently, momentum can only change if an external net force acts on the system (Newton's 2nd Law: F = dp/dt). By Noether's Theorem, momentum conservation is the direct consequence of spatial translation symmetry: if the laws of physics are the same at every location in space, momentum is conserved. It is violated in non-inertial frames and modified in relativistic and quantum regimes."),
        ("Mathematical Form", 1,
         "p_total = Σ mᵢvᵢ = const  (isolated system)\n\nDifferential form: dp/dt = F_ext\n\nFor collisions:  Σ p_before = Σ p_after\n\nRelativistic:  p = γmv,   γ = 1/√(1−v²/c²)\n\nQuantum:  ⟨p⟩ conserved when [H, p] = 0  (space-translation symmetry of Hamiltonian)"),
        ("Constraint Category", 2,
         "Symmetry/Conservation (Sy/Co): momentum conservation is the Noether charge of continuous spatial translation symmetry. It constrains all collision, explosion, and flow problems without requiring knowledge of internal forces. In D dimensions, momentum is a D-component vector; spatial isotropy (in D=3) extends to three independent conservation laws (px, py, pz)."),
        ("DS Cross-References", 3,
         "CM1 (Newton's Laws — Newton's 3rd Law implies momentum conservation: internal forces cancel pairwise, net momentum change = external forces only). AM5 (Noether's Theorem — spatial translation symmetry of the Lagrangian L generates momentum as the conserved Noether charge). CM11 (Conservation of Energy — energy and momentum are jointly conserved; in relativistic mechanics they form the 4-momentum conservation law E²/c²−p²=m²c²). QM5 (Special Relativity — relativistic momentum p=γmv replaces classical p=mv; the 4-momentum conservation unifies energy and momentum)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nMomentum conservation is the vector prototype of conservation laws: it is additive, extensive, and frame-dependent (unlike energy which is scalar). In continuum mechanics, it becomes ∂ρv/∂t = −∇·(ρvv + P) — the Euler/Navier-Stokes momentum flux equation. The conservation law structure means momentum can be tracked as a ledger: whatever leaves one subsystem enters another."),
        ("What The Math Says", 5,
         "The total momentum p-total is the sum of mass times velocity for each particle. For an isolated system with no external forces, dp-total over dt equals zero, so p-total is constant. For a collision, the sum of momenta before equals the sum after, regardless of the internal forces during impact. In the relativistic case, mass m is augmented by the Lorentz factor gamma equals one over the square root of one minus v-squared over c-squared, and the 4-momentum (E/c, p) is conserved as a four-vector. In quantum mechanics, momentum is conserved when the Hamiltonian commutes with the momentum operator, which occurs precisely when the system has spatial translation symmetry — the operator form of Noether's Theorem."),
        ("Concept Tags", 6,
         "• conservation of momentum\n• linear momentum\n• Newton's third law\n• Noether's theorem\n• spatial translation symmetry\n• collision\n• impulse\n• relativistic momentum\n• 4-momentum\n• isolated system"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Sy", 0),
        ("entries", "concept_tags", "conservation of momentum, linear momentum, Newton's third law, Noether's theorem, spatial translation symmetry, collision, impulse, relativistic momentum, 4-momentum, isolated system", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "CM10", "Conservation of Momentum", "CM1", "Newton's Laws of Motion",
         "Newton's 3rd Law (equal and opposite reaction) implies that internal forces cancel pairwise, leaving net momentum change equal to external forces only — the direct derivation of momentum conservation."),
        ("derives from", "CM10", "Conservation of Momentum", "AM5", "Noether's Theorem",
         "Spatial translation symmetry of the Lagrangian generates momentum as its Noether conserved charge: invariance under x→x+ε gives d/dt(∂L/∂ẋ)=0, i.e., dp/dt=0."),
        ("couples to", "CM10", "Conservation of Momentum", "CM11", "Conservation of Energy",
         "Momentum and energy are the two paired Noether conservation laws of classical mechanics (spatial and time translation symmetry respectively); in special relativity they unite into 4-momentum conservation."),
    ],
},

{
    "id": "CM11",
    "title": "Conservation of Energy",
    "filename": "CM11_conservation_energy.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The total energy of an isolated system — summed across all forms (kinetic, potential, rest-mass, thermal, electromagnetic, etc.) — is constant in time. Energy can be transformed between forms but cannot be created or destroyed. By Noether's Theorem, this is the consequence of time-translation symmetry: physical laws that do not change with time imply energy conservation. The First Law of Thermodynamics (TD2) is the thermodynamic form; Einstein's E=mc² extends it to include rest-mass energy."),
        ("Mathematical Form", 1,
         "E_total = KE + PE + E_internal + ... = const  (isolated system)\n\ndE/dt = P_ext  (power from external sources)\n\nMechanics:     E = ½mv² + V(x)\nThermodynamics: ΔU = Q − W          (TD2)\nRelativity:    E² = (pc)² + (mc²)²  (rest-mass included)\nQuantum:       d⟨H⟩/dt = 0  when ∂H/∂t = 0"),
        ("Constraint Category", 2,
         "Symmetry/Conservation (Sy/Co): energy conservation is the Noether charge of time-translation symmetry. It is the master scalar constraint on all physical processes — the ledger that no interaction can violate. D-invariant: energy conservation holds in any number of spatial dimensions as long as the Lagrangian has no explicit time dependence."),
        ("DS Cross-References", 3,
         "TD2 (First Law of Thermodynamics — the thermodynamic specialisation of energy conservation: ΔU=Q−W, where Q is heat and W is mechanical work done by the system). AM5 (Noether's Theorem — time-translation symmetry of the Lagrangian generates the Hamiltonian H as the conserved Noether charge; dH/dt=0 when ∂L/∂t=0). CM10 (Conservation of Momentum — the partner conservation law; together energy and momentum conservation constrain all collision and decay kinematics). TD3 (Second Law — while total energy is conserved, available work (exergy) decreases irreversibly; energy quality degrades even as quantity is preserved)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nConservation of Energy is the scalar conservation law: it is the unique Noether charge associated with time-homogeneity. Unlike momentum (a vector), energy is frame-independent in the non-relativistic limit. The conservation structure allows bookkeeping across arbitrary transformations: kinetic ↔ potential ↔ thermal ↔ electromagnetic, with no net change in the total. In the DS framework it is the root constraint above all thermodynamic bounds."),
        ("What The Math Says", 5,
         "The total mechanical energy E equals kinetic energy one-half m v-squared plus potential energy V of x, and is constant along any trajectory in the absence of dissipation. When external agents do work at rate P-ext, energy changes as dE over dt equals P-ext. In thermodynamics, the change in internal energy ΔU equals heat added Q minus work done by the system W — this is TD2. In special relativity, total energy squared equals momentum squared times c-squared plus rest mass energy squared (mc-squared squared), so even a particle at rest has energy mc-squared. In quantum mechanics, the expectation value of the Hamiltonian H is constant whenever H has no explicit time dependence — Ehrenfest's theorem. All of these are specialisations of the same Noether charge under time-translation symmetry."),
        ("Concept Tags", 6,
         "• conservation of energy\n• Noether's theorem\n• time-translation symmetry\n• Hamiltonian\n• kinetic energy\n• potential energy\n• first law of thermodynamics\n• E=mc²\n• rest-mass energy\n• exergy"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Sy", 0),
        ("entries", "concept_tags", "conservation of energy, Noether's theorem, time-translation symmetry, Hamiltonian, kinetic energy, potential energy, first law of thermodynamics, E=mc², rest-mass energy, exergy", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "CM11", "Conservation of Energy", "TD2", "First Law of Thermodynamics",
         "The First Law (ΔU=Q−W) is the thermodynamic form of energy conservation, restricted to heat and mechanical work. Conservation of Energy is the more general statement covering kinetic, potential, electromagnetic, and rest-mass energy."),
        ("derives from", "CM11", "Conservation of Energy", "AM5", "Noether's Theorem",
         "Time-translation symmetry of the Lagrangian (∂L/∂t=0) generates the Hamiltonian as the conserved Noether charge: dH/dt=0 is exactly energy conservation."),
        ("couples to", "CM11", "Conservation of Energy", "CM10", "Conservation of Momentum",
         "Energy and momentum are the paired Noether conservation laws from time- and space-translation symmetry; in special relativity they unify into the 4-momentum (E/c, p) conservation law."),
    ],
},

# ── ELECTROMAGNETISM ──────────────────────────────────────────────────────────

{
    "id": "EM12",
    "title": "Ampère's Circuital Law",
    "filename": "EM12_ampere_circuital.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The line integral of the magnetic field B around any closed loop equals μ₀ times the total current enclosed by that loop (Ampère, 1826). This is the static (magnetostatic) form; it applies when the electric field is not changing in time. Maxwell extended it by adding the displacement current term (EM4), which is essential for electromagnetic wave propagation. Ampère's circuital law enables calculation of magnetic fields for symmetric current configurations without integrating over source elements."),
        ("Mathematical Form", 1,
         "∮ B · dl = μ₀ I_enc          (magnetostatic form)\n\nDifferential form: ∇ × B = μ₀ J   (static)\n\nFor an infinite straight wire: B = μ₀I / 2πr\nFor a solenoid (n turns/length): B = μ₀nI (inside)\nFor a toroid: B = μ₀NI / 2πr"),
        ("Constraint Category", 2,
         "Geometric (Ge): the integral form applies Stokes' theorem to the magnetic curl equation in 3D; the result is path-independent in the sense that any loop enclosing the same current gives the same magnetomotive force. D-sensitive in the sense that the geometry of the Amperian loop must match the symmetry of the current distribution to be analytically tractable."),
        ("DS Cross-References", 3,
         "EM4 (Ampère–Maxwell Law — EM12 is the static limit of EM4: setting ∂E/∂t=0 recovers Ampère's original circuital law; Maxwell's displacement current is the extension for time-varying fields). EM7 (Biot–Savart Law — equivalent alternative for static fields: Biot-Savart integrates over current elements dB=μ₀Idl×r̂/4πr²; Ampère's law integrates around a loop; both give the same B for magnetostatics). MATH8 (Generalized Stokes' Theorem — Ampère's circuital law is the physical application of Stokes' theorem ∮B·dl=∬(∇×B)·dA to the static Maxwell curl equation). EM3 (Faraday's Law — together Faraday and Ampère are the two curl Maxwell equations governing EM wave propagation)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nAmpère's Circuital Law is the integral form of the magnetic flux-current relationship: the magnetomotive force ∮B·dl depends only on the total enclosed current, not on the current distribution. This is a topological conservation statement — the curl integral is invariant to loop deformation as long as enclosed current is unchanged. It is the magnetic analog of Gauss's Law (EM1): flux integral for sources vs. circulation integral for vortices."),
        ("What The Math Says", 5,
         "The line integral of B dotted with the path element dl around a closed Amperian loop equals mu-zero times the current I-enc passing through any surface bounded by that loop. The choice of loop is free — any shape enclosing the same current gives the same result. For an infinite straight wire, choosing a circular loop of radius r gives B times two pi r equals mu-zero I, so B equals mu-zero I over two pi r: the field circles the wire and decays as 1 over r. For a solenoid with n turns per unit length carrying current I, choosing a rectangular loop through the interior and exterior gives B equals mu-zero n I inside and zero outside (ideal solenoid). The differential form nabla cross B equals mu-zero J is the point-wise version, recovered by shrinking the loop to a point and applying Stokes' theorem."),
        ("Concept Tags", 6,
         "• Ampère's law\n• magnetomotive force\n• magnetic circulation\n• solenoid\n• Stokes' theorem\n• magnetostatics\n• Amperian loop\n• magnetic field\n• current density\n• Maxwell equations"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Ampère's law, magnetomotive force, magnetic circulation, solenoid, Stokes' theorem, magnetostatics, Amperian loop, magnetic field, current density, Maxwell equations", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "EM12", "Ampère's Circuital Law", "EM4", "Ampère–Maxwell Law",
         "Setting the displacement current term ∂E/∂t=0 in the Ampère–Maxwell Law (EM4) recovers Ampère's Circuital Law exactly; EM12 is the static limit of EM4."),
        ("analogous to", "EM12", "Ampère's Circuital Law", "EM7", "Biot–Savart Law",
         "Ampère's Circuital Law (integral over a closed loop) and Biot–Savart Law (integration over current elements) are equivalent descriptions of magnetostatic fields; Ampère's law is preferred for symmetric geometries."),
        ("derives from", "EM12", "Ampère's Circuital Law", "MATH8", "Generalized Stokes' Theorem",
         "The circuital form ∮B·dl=μ₀I_enc is Stokes' theorem (∮B·dl=∬(∇×B)·dA) applied to the static Maxwell curl equation ∇×B=μ₀J."),
    ],
},

{
    "id": "EM13",
    "title": "Wiedemann–Franz Law",
    "filename": "EM13_wiedemann_franz.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "In metals, the ratio of thermal conductivity κ to electrical conductivity σ is proportional to temperature T, with a nearly universal proportionality constant L called the Lorenz number (Wiedemann & Franz, 1853; Drude, 1900; Sommerfeld, 1927). This universality arises because both thermal and electrical transport in metals are dominated by the same charge carriers — conduction electrons — governed by Fermi-Dirac statistics. Significant deviations signal strongly correlated electron physics."),
        ("Mathematical Form", 1,
         "κ / σ = L · T\n\nLorenz number (Sommerfeld):  L = π²kB² / 3e²  ≈  2.44 × 10⁻⁸  W·Ω·K⁻²\n\nFor comparison:\n  Copper at 300 K:  κ ≈ 400 W/m·K,  σ ≈ 6×10⁷ Ω⁻¹m⁻¹  →  L ≈ 2.2×10⁻⁸ W·Ω·K⁻²\n  Gold at 300 K:   L ≈ 2.3×10⁻⁸ W·Ω·K⁻²"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): both κ and σ are linear response transport coefficients (Onsager regime); their ratio is fixed by the universal Fermi-Dirac statistics of electrons rather than material-specific band structure details. Violations of the Wiedemann–Franz Law signal non-Fermi-liquid behaviour (strongly correlated electrons, phonon drag, Mott insulators) — making it a diagnostic for exotic metallic states."),
        ("DS Cross-References", 3,
         "EM9 (Ohm's Law — electrical conductivity σ in the Wiedemann–Franz ratio is the same σ as Ohm's law J=σE; the law links the two transport properties through the same carrier population). TD10 (Fourier's Law of Heat Conduction — thermal conductivity κ is the coefficient in Fourier's q=−κ∇T; the Wiedemann–Franz law constrains κ for metals once σ is known). TD6 (Onsager Reciprocal Relations — κ and σ are both diagonal Onsager transport coefficients; the Wiedemann–Franz Law is a further constraint beyond Onsager symmetry that emerges from Fermi-Dirac statistics). QM3 (Pauli Exclusion Principle — the Fermi-Dirac distribution underlying the Sommerfeld derivation is a direct consequence of the Pauli exclusion principle for electrons)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nThe Wiedemann–Franz Law is a linear proportionality between two transport coefficients mediated by temperature. Its universality reflects that the Lorenz number L=π²kB²/3e² is expressed entirely in terms of fundamental constants — it is a ratio fixed by quantum statistics, not by material parameters. This universality class structure (same L across metals) is the hallmark of Fermi liquid theory."),
        ("What The Math Says", 5,
         "The ratio of thermal conductivity kappa to electrical conductivity sigma equals the Lorenz number L times temperature T. The Sommerfeld derivation gives L equals pi-squared times k-B-squared over 3 e-squared, approximately 2.44 times 10 to the minus 8 watts ohms per kelvin squared. This value is universal across conventional metals because both heat and charge are carried by the same electron population obeying Fermi-Dirac statistics: only electrons within k-B T of the Fermi level contribute to transport. The thermal conductivity scales as T because the number of thermally activated carriers scales linearly with T near absolute zero. The electrical conductivity is temperature-independent in the Drude-Sommerfeld model at low T. Deviations from the Wiedemann-Franz Law at low temperature indicate that phonon scattering, electron-electron interactions, or magnetic fluctuations break the universal ratio."),
        ("Concept Tags", 6,
         "• Wiedemann–Franz Law\n• Lorenz number\n• thermal conductivity\n• electrical conductivity\n• Fermi-Dirac statistics\n• free electron model\n• Sommerfeld theory\n• non-Fermi liquid\n• transport coefficient\n• condensed matter"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Wiedemann-Franz Law, Lorenz number, thermal conductivity, electrical conductivity, Fermi-Dirac statistics, free electron model, Sommerfeld theory, non-Fermi liquid, transport coefficient, condensed matter", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "EM13", "Wiedemann–Franz Law", "EM9", "Ohm's Law",
         "Electrical conductivity σ in the Wiedemann–Franz ratio κ/σ=LT is the same σ as in Ohm's Law J=σE; the Wiedemann–Franz Law directly constrains σ's thermal partner κ through the same electron population."),
        ("couples to", "EM13", "Wiedemann–Franz Law", "TD10", "Fourier's Law of Heat Conduction",
         "Thermal conductivity κ is the coefficient in Fourier's Law q=−κ∇T; for metals, the Wiedemann–Franz Law determines κ=LTσ once σ is known from Ohm's Law, connecting the two transport laws."),
        ("derives from", "EM13", "Wiedemann–Franz Law", "QM3", "Pauli Exclusion Principle",
         "The Sommerfeld derivation of L=π²kB²/3e² relies on Fermi-Dirac statistics, which are the direct consequence of the Pauli exclusion principle applied to electron gases."),
    ],
},

# ── THERMODYNAMICS ────────────────────────────────────────────────────────────

{
    "id": "TD14",
    "title": "van der Waals Equation",
    "filename": "TD14_van_der_waals.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · chemistry",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Real gases deviate from ideal behaviour because molecules have finite volume and exert attractive forces on each other. Van der Waals (1873) corrected the Ideal Gas Law by subtracting the excluded volume (b per mole) and adding a pressure correction for intermolecular attraction (a/V²). The equation predicts gas-liquid phase transitions and the critical point (Tc, Pc, Vc) — phenomena entirely absent from the Ideal Gas Law. At low density (a→0, b→0), it reduces exactly to PV=nRT."),
        ("Mathematical Form", 1,
         "(P + n²a/V²)(V − nb) = nRT\n\nPer-mole form:  (P + a/Vm²)(Vm − b) = RT\n\nCritical point:  Tc = 8a/27Rb,   Pc = a/27b²,   Vc = 3nb\nReduced variables:  Pr = P/Pc,  Tr = T/Tc,  Vr = V/Vc\nLaw of Corresponding States:  (Pr + 3/Vr²)(3Vr − 1) = 8Tr"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): the equation of state constrains P, V, T relationships for real gases and predicts the liquid–gas phase boundary and critical point. The van der Waals constants a (J·m³/mol²) and b (m³/mol) are substance-specific — D-sensitive. The Law of Corresponding States (reduced variables) is D-invariant in functional form, applying universally across all van der Waals fluids."),
        ("DS Cross-References", 3,
         "GL1 (Ideal Gas Law — van der Waals reduces to PV=nRT in the limit a→0, b→0; the Ideal Gas Law is the zeroth-order approximation that van der Waals corrects). TD5 (Fundamental Thermodynamic Relation — the van der Waals equation is an equation of state, a specialisation of the relationship among P, V, T derivable from the Helmholtz free energy F=−NkBT[ln(V−Nb)/N + 3/2 ln(2πmkBT/h²)] − aN²/V). TD3 (Second Law — the Maxwell construction (equal-area rule) resolves the unphysical van der Waals isotherm in the two-phase region, enforcing Gibbs free energy equality between phases). KC2 (Law of Microscopic Reversibility — the van der Waals constants arise from pairwise intermolecular potentials; KC2 constrains the symmetry of these collision processes)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nThe van der Waals equation defines an equilibrium surface in (P, V, T) space that generalises the ideal gas manifold. Its cubic form in V admits three real roots in the coexistence region (liquid, spinodal, gas solutions) — the hallmark of a first-order phase transition. The critical point is where the three roots merge: (∂P/∂V)_T = (∂²P/∂V²)_T = 0. The reduced equation (Law of Corresponding States) is the universal normal form of van der Waals-class fluids."),
        ("What The Math Says", 5,
         "The pressure P plus n-squared a over V-squared, times V minus n b, equals n R T. The term n-squared a over V-squared corrects for attractive intermolecular forces: they reduce the effective pressure below the ideal value because molecules near the wall are pulled back by neighbours. The term V minus n b corrects for excluded volume: the space available to each molecule is reduced by the volume nb already occupied by the others. At the critical point, the three solutions for V at fixed T and P merge into one: Tc equals 8a over 27Rb, Pc equals a over 27b-squared, and Vc equals 3nb. In reduced variables Pr, Tr, Vr, the equation becomes the universal form Pr plus 3 over Vr-squared times 3Vr minus 1 equals 8Tr — valid for all van der Waals fluids regardless of the specific values of a and b."),
        ("Concept Tags", 6,
         "• van der Waals equation\n• real gas\n• intermolecular forces\n• excluded volume\n• critical point\n• phase transition\n• law of corresponding states\n• equation of state\n• van der Waals constants\n• gas-liquid coexistence"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "van der Waals equation, real gas, intermolecular forces, excluded volume, critical point, phase transition, law of corresponding states, equation of state, van der Waals constants, gas-liquid coexistence", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "TD14", "van der Waals Equation", "GL1", "Ideal Gas Law",
         "Setting a=0 and b=0 in the van der Waals equation recovers PV=nRT exactly; the Ideal Gas Law is the zero-interaction, zero-volume limit of the van der Waals equation."),
        ("derives from", "TD14", "van der Waals Equation", "TD5", "Fundamental Thermodynamic Relation",
         "The van der Waals equation of state is derived from the Helmholtz free energy F via P=−(∂F/∂V)_T; it is a specific implementation of the equation-of-state constraint implicit in TD5."),
        ("couples to", "TD14", "van der Waals Equation", "TD3", "Second Law of Thermodynamics",
         "The Maxwell equal-area construction — which resolves the unphysical van der Waals S-curve in the two-phase region — enforces equal Gibbs free energy between coexisting phases, a direct requirement of the Second Law."),
    ],
},

# ── GRAVITY / COSMOLOGY ───────────────────────────────────────────────────────

{
    "id": "GV4",
    "title": "Hubble–Lemaître Law",
    "filename": "GV4_hubble_lemaitre.md",
    "entry_type": "reference_law",
    "scale": "cosmological",
    "domain": "physics · cosmology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The recession velocity of a distant galaxy is proportional to its distance from the observer (Lemaître, 1927; Hubble, 1929). The proportionality constant H₀ (Hubble constant, ~70 km/s/Mpc) is the present-day rate of cosmic expansion. The law follows directly from the FLRW metric of General Relativity applied to a homogeneous, isotropic expanding universe. It constitutes the primary observational evidence for the Big Bang and cosmic expansion. At cosmological distances, peculiar velocities and redshift corrections apply."),
        ("Mathematical Form", 1,
         "v = H₀ · d          (Hubble–Lemaître Law)\n\nH₀ ≈ 67–73 km/s/Mpc  (current observational range; 'Hubble tension')\n\nGeneral FLRW form:  H(t) = ȧ(t)/a(t)   (Hubble parameter at cosmic time t)\nScale factor:        d(t) = a(t) · d_comoving\nRedshift:            1 + z = a(t₀)/a(t_emit)"),
        ("Constraint Category", 2,
         "Geometric (Ge): the linear velocity-distance relation is a geometric consequence of uniform expansion — every point recedes from every other at a rate proportional to separation, with no preferred centre. D-sensitive: H₀ is an empirically measured cosmological parameter with current precision ~1–2% but subject to the Hubble tension (local vs. CMB-based measurements disagree at ~5σ)."),
        ("DS Cross-References", 3,
         "GV1 (General Relativity — the Hubble–Lemaître Law is derived from the FLRW metric, which is the exact solution to Einstein's field equations for a homogeneous, isotropic universe; the Friedmann equations govern a(t)). GV2 (Gravitoelectromagnetism — the weak-field regime of GR that yields GEM also underlies the Newtonian approximation to expansion, where H₀d gives recessional velocity). CM2 (Newton's Law of Universal Gravitation — a Newtonian derivation of the Friedmann equations gives the same expansion law: gravity decelerates expansion while dark energy accelerates it). RD2 (Stefan–Boltzmann Law — the CMB temperature T∝1/a(t) follows from Stefan-Boltzmann applied to the photon gas; CMB measurements are the primary route to H₀ from early-universe data)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nThe Hubble-Lemaître Law is linear in d at fixed cosmic time: v=H₀d. This linearity is not a coincidence but a geometric necessity — uniform expansion of a homogeneous medium produces a linear velocity field. It is the cosmological instance of the linear scaling archetype: any two points in a uniformly expanding medium satisfy v∝d regardless of scale. Deviations from linearity encode the matter/energy content of the universe through the deceleration parameter q₀."),
        ("What The Math Says", 5,
         "The recession velocity v of a galaxy equals H-zero times its distance d. H-zero has units of inverse time (approximately 2.3 times 10 to the minus 18 per second, or equivalently 70 km/s per megaparsec). The general FLRW form replaces H-zero with the time-dependent Hubble parameter H of t equals a-dot over a, where a of t is the cosmic scale factor normalised to 1 today. Redshift z relates to the scale factor by 1 plus z equals a of t-zero over a of t-emit: light emitted when the universe was smaller arrives stretched by the factor by which the universe has expanded since emission. The Friedmann equations from GR give a-dot squared over a squared equals 8 pi G rho over 3 minus kc squared over a squared plus Lambda over 3, where rho is energy density, k is spatial curvature, and Lambda is the cosmological constant. The Hubble tension — a 5-sigma disagreement between H-zero derived from the early universe (CMB, ~67 km/s/Mpc) and from late-universe standard candles (~73 km/s/Mpc) — is a current open problem in cosmology."),
        ("Concept Tags", 6,
         "• Hubble–Lemaître Law\n• Hubble constant\n• cosmic expansion\n• FLRW metric\n• scale factor\n• redshift\n• Big Bang\n• Hubble tension\n• Friedmann equations\n• cosmological distance"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Hubble-Lemaître Law, Hubble constant, cosmic expansion, FLRW metric, scale factor, redshift, Big Bang, Hubble tension, Friedmann equations, cosmological distance", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "GV4", "Hubble–Lemaître Law", "GV1", "General Relativity — Einstein Field Equations",
         "The Hubble–Lemaître Law follows from the Friedmann equations, which are the GR field equations specialised to a homogeneous, isotropic (FLRW) universe; ȧ/a=H is the direct observable of the GR expansion."),
        ("couples to", "GV4", "Hubble–Lemaître Law", "CM2", "Newton's Law of Universal Gravitation",
         "A Newtonian derivation of expansion treats each shell of matter as a test particle; gravity decelerates expansion while dark energy (Λ) accelerates it — the competition between CM2 and the cosmological constant determines the fate of the universe."),
        ("couples to", "GV4", "Hubble–Lemaître Law", "RD2", "Stefan–Boltzmann Law",
         "CMB photon temperature scales as T∝1/a(t) (a photon-gas cooling law derivable from Stefan-Boltzmann); the CMB provides the primary early-universe measurement of H₀ that drives the Hubble tension."),
    ],
},

# ── FLUID MECHANICS ───────────────────────────────────────────────────────────

{
    "id": "FM7",
    "title": "Darcy's Law",
    "filename": "FM7_darcys_law.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The volumetric flow rate of a fluid through a porous medium is proportional to the cross-sectional area and the pressure gradient, and inversely proportional to fluid viscosity (Darcy, 1856). The permeability k characterises the medium's resistance to flow — a purely geometric property of the pore structure, independent of the fluid. Darcy's Law is the porous-media analog of Ohm's Law and holds in the low-Reynolds-number (viscous-dominated) regime where inertial effects are negligible."),
        ("Mathematical Form", 1,
         "Q = −(k A / μ) · (ΔP / L)    (1D form)\n\nVector form:  v = −(k/μ) · ∇P    (Darcy velocity / flux)\n\nWith gravity:  v = −(k/μ) · (∇P − ρg)   (hydrogeology form)\n\nk = permeability (m², Darcy: 1 D ≈ 10⁻¹² m²)\nμ = dynamic viscosity (Pa·s)\nQ = volumetric flux (m³/s)\nRe_Darcy < 1  for validity"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): linear dissipative transport — pressure gradient drives viscous flow through a medium whose pore geometry fixes the permeability k. Same mathematical class as Ohm's Law (J=σE), Fourier's Law (q=−κ∇T), and Fick's Law (J=−D∇c). D-sensitive: k depends entirely on pore geometry and is independent of the fluid; μ depends on the fluid and temperature."),
        ("DS Cross-References", 3,
         "DM1 (Fick's Laws of Diffusion — Fick's J=−D∇c and Darcy's v=−(k/μ)∇P are the same linear transport archetype: flux proportional to gradient; D↔k/μ, concentration gradient↔pressure gradient). TD10 (Fourier's Law of Heat Conduction — Fourier's q=−κ∇T is the thermal member of the same linear transport family; all three (Fick, Darcy, Fourier) are Fickian transport laws differing only in the transported quantity). FM5 (Stokes' Law — both describe viscous, inertia-free flow at low Reynolds number; Darcy's Law is the continuum-porous-medium version of Stokes flow at the pore scale). FM1 (Navier–Stokes Equations — Darcy's Law is derivable from volume-averaging the Stokes limit of NS over the pore geometry: ⟨v⟩ = −(k/μ)∇P by homogenisation theory)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nDarcy's Law is the porous-media instance of the universal Fickian transport archetype: flux = −conductivity × gradient. The permeability k/μ plays the role of diffusivity D in Fick's Law, thermal conductivity κ in Fourier's Law, and electrical conductivity σ in Ohm's Law. All four are zero-inertia (Stokes regime) linear responses that become nonlinear at high Reynolds or Péclet number."),
        ("What The Math Says", 5,
         "The Darcy velocity v equals minus k over mu times the gradient of pressure P, where k is the intrinsic permeability of the medium in metres squared and mu is the dynamic viscosity of the fluid in pascal-seconds. The negative sign means flow goes from high to low pressure. Permeability k is a tensor in anisotropic media — rock with aligned fractures conducts differently in different directions. For horizontal 1D flow of length L across area A with pressure drop delta-P, the volumetric flow rate Q equals k A delta-P over mu L. In hydrogeology, the gravitational term rho g is added to pressure to give hydraulic head. The Darcy velocity v (superficial velocity) differs from the pore velocity v-pore by a factor of porosity phi: v-pore equals v over phi. Darcy's Law breaks down when the Darcy Reynolds number Re equals rho v d-pore over mu exceeds approximately 1 — inertial effects then require the Forchheimer equation: minus dP/dx equals mu v / k plus rho beta v squared."),
        ("Concept Tags", 6,
         "• Darcy's Law\n• porous media\n• permeability\n• viscous flow\n• hydraulic conductivity\n• pressure gradient\n• Darcy velocity\n• groundwater\n• low Reynolds number\n• Fickian transport"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Darcy's Law, porous media, permeability, viscous flow, hydraulic conductivity, pressure gradient, Darcy velocity, groundwater, low Reynolds number, Fickian transport", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("analogous to", "FM7", "Darcy's Law", "DM1", "Fick's Laws of Diffusion",
         "Darcy's v=−(k/μ)∇P and Fick's J=−D∇c are the same linear transport law — flux proportional to driving gradient — in different physical settings: porous-media pressure vs. concentration diffusion."),
        ("analogous to", "FM7", "Darcy's Law", "EM9", "Ohm's Law",
         "Darcy's Law (v=−(k/μ)∇P), Ohm's Law (J=σE), Fourier's Law, and Fick's Law are all members of the Fickian linear-response family: all map a potential gradient to a flux with a medium-specific conductivity coefficient."),
        ("derives from", "FM7", "Darcy's Law", "FM1", "Navier–Stokes Equations",
         "Darcy's Law is derived by volume-averaging the Stokes limit of the Navier–Stokes equations over a representative pore volume; the permeability k emerges from the homogenisation of the pore geometry."),
    ],
},

# ── CRYSTALLOGRAPHY / SCATTERING ──────────────────────────────────────────────

{
    "id": "CR1",
    "title": "Bragg's Law",
    "filename": "CR1_braggs_law.md",
    "entry_type": "reference_law",
    "scale": "atomic · molecular",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "When X-rays, neutrons, or electrons scatter from parallel crystal planes separated by interplanar spacing d, constructive interference occurs only at discrete glancing angles θ satisfying the Bragg condition (W.L. Bragg & W.H. Bragg, 1913). The integer n is the diffraction order. The law is the basis of X-ray crystallography, enabling determination of atomic structure from diffraction patterns. The same condition governs neutron and electron diffraction via de Broglie wavelengths."),
        ("Mathematical Form", 1,
         "nλ = 2d sinθ\n\nn = integer order (1, 2, 3, ...)\nλ = wavelength of radiation (X-ray: ~0.1 nm; neutron: ~0.1–1 nm)\nd = interplanar spacing (Ångströms; Miller indices hkl)\nθ = glancing angle from the crystal plane surface\n\nFor cubic crystals: d_hkl = a / √(h² + k² + l²)\nBragg peaks at: sinθ = nλ/2d"),
        ("Constraint Category", 2,
         "Geometric (Ge): Bragg's Law is a path-difference geometry condition — constructive interference occurs when the extra path 2d sinθ is an integer multiple of λ. It is purely kinematic (no dynamical diffraction effects) and exact in the single-scattering (Born) approximation. D-sensitive in the sense that d is crystal-specific and λ must be chosen to be comparable to d (λ ~ 10⁻¹⁰ m for X-ray crystallography of atomic spacings)."),
        ("DS Cross-References", 3,
         "OP2 (Law of Reflection — the Bragg reflection geometry is specular reflection from each crystal plane; the constructive-interference condition selects the angles where in-phase specular reflections add coherently). QM4 (de Broglie Wavelength — de Broglie's λ=h/p extends Bragg's Law from X-ray photons to electrons and neutrons: electron diffraction uses λ=h/√(2meV) and neutron diffraction uses λ=h/mv, enabling structure determination with different probe-matter interactions). RD3 (Planck–Einstein Relation — X-ray photon energy E=hc/λ connects Bragg's diffraction angle to photon energy; energy-dispersive X-ray diffraction uses a fixed θ and varies λ via polychromatic radiation). EM1 (Gauss's Law for Electricity — X-rays are electromagnetic radiation; their interaction with electron density in the crystal determines the diffraction structure factors F_hkl = Σ fⱼ e^{2πi(hxⱼ+kyⱼ+lzⱼ})."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: oscillatory\n\nBragg's Law is an interference condition: constructive superposition of waves (oscillatory archetype) reflected from periodic planes. It is the discrete Fourier condition for a periodic lattice: the reciprocal lattice vectors G_hkl satisfying |G|=2sinθ/λ are the Bragg peaks. X-ray crystallography is fundamentally Fourier analysis of matter — measuring intensities |F_hkl|² at Bragg peaks and inverting to recover the real-space electron density."),
        ("What The Math Says", 5,
         "The condition n lambda equals 2d sin theta states that the path difference between waves reflecting from adjacent crystal planes — equal to 2d times sin theta, where theta is the glancing angle from the plane surface — must be an integer number n of wavelengths for constructive interference. For X-rays with lambda approximately 0.15 nm interacting with crystal planes of spacing d approximately 0.2 nm, the Bragg angle theta falls in the range 10 to 80 degrees — accessible with laboratory diffractometers. For a cubic crystal with lattice parameter a, the interplanar spacing for Miller indices h, k, l is d-hkl equals a over the square root of h-squared plus k-squared plus l-squared. The complete diffraction pattern is the square modulus of the structure factor F-hkl, summed over all atoms j with scattering factors f-j at fractional coordinates (x-j, y-j, z-j). Phase retrieval — recovering the phases of F-hkl from intensities alone — is the central computational challenge of crystallography."),
        ("Concept Tags", 6,
         "• Bragg's Law\n• X-ray crystallography\n• diffraction\n• interplanar spacing\n• Miller indices\n• neutron diffraction\n• electron diffraction\n• constructive interference\n• reciprocal lattice\n• structure factor"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Bragg's Law, X-ray crystallography, diffraction, interplanar spacing, Miller indices, neutron diffraction, electron diffraction, constructive interference, reciprocal lattice, structure factor", 0),
        ("DS Facets", "mathematical_archetype", "oscillatory", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "CR1", "Bragg's Law", "OP2", "Law of Reflection",
         "The Bragg geometry is specular reflection from each crystal plane; Bragg's Law adds the coherence condition (path difference = nλ) to select the angles at which reflections from successive planes interfere constructively."),
        ("couples to", "CR1", "Bragg's Law", "QM4", "de Broglie Wavelength",
         "de Broglie's λ=h/p extends Bragg's Law from X-ray photons to electrons and neutrons; the same nλ=2d sinθ condition governs electron and neutron diffraction using de Broglie wavelengths."),
        ("couples to", "CR1", "Bragg's Law", "RD3", "Planck–Einstein Relation",
         "X-ray photon energy E=hc/λ from the Planck–Einstein Relation connects the Bragg diffraction angle θ to photon energy; energy-dispersive X-ray diffraction varies λ at fixed θ to sweep through Bragg peaks."),
    ],
},

# ── MATERIALS SCIENCE ─────────────────────────────────────────────────────────

{
    "id": "MS1",
    "title": "Young's Modulus",
    "filename": "MS1_youngs_modulus.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "For a linearly elastic material under uniaxial stress, engineering strain is proportional to stress, with Young's modulus E as the constant of proportionality (Young, 1807). E encodes the stiffness of a material against stretching or compression along one axis and is a fundamental material property determined by atomic bonding strength. Young's Modulus is the tensorial component C₁₁₁₁ of the full elasticity tensor for isotropic materials, and the three-dimensional material-level form of Hooke's Law."),
        ("Mathematical Form", 1,
         "σ = E ε       (uniaxial stress-strain)\n\nσ = F / A      (stress, Pa)\nε = ΔL / L₀   (engineering strain, dimensionless)\n\nRepresentative values:\n  Diamond:     E ≈ 1,000 GPa\n  Steel:       E ≈ 200 GPa\n  Bone:        E ≈ 20 GPa\n  Rubber:      E ≈ 0.01 GPa\n\nPoisson's ratio: ν = −ε_transverse / ε_axial  (lateral contraction)\nShear modulus:   G = E / 2(1+ν)\nBulk modulus:    K = E / 3(1−2ν)"),
        ("Constraint Category", 2,
         "Geometric/Thermodynamic (Ge/Th): Young's Modulus is a geometric material property (linear elastic response within the infinitesimal strain limit) and a thermodynamic one (E is the second derivative of free energy density with respect to strain: E = ∂²F/∂ε²). D-sensitive: E values span five orders of magnitude across materials; dimensionally, it is a pressure (Pa = N/m²) and scales with interatomic bond stiffness."),
        ("DS Cross-References", 3,
         "CM9 (Hooke's Law — Young's Modulus is Hooke's spring constant k generalised to a material: σ=Eε is the continuum form of F=−kx, with E=kL₀/A for a rod of initial length L₀ and area A). FM1 (Navier–Stokes Equations — the elastic stress tensor σ=Eε enters continuum mechanics alongside the viscous stress tensor in the full Cauchy momentum equation; solid mechanics and fluid mechanics share the same momentum conservation framework). EM9 (Ohm's Law — both Young's Modulus (σ=Eε) and Ohm's Law (J=σE) are linear constitutive relations mapping a driving quantity to a response: stress→strain :: electric field→current density). DM1 (Fick's Laws — all three (Hooke/Young, Ohm, Fick, Darcy, Fourier) are members of the Fickian linear-response family: response proportional to driving gradient, with a material-specific coefficient)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: linear-proportionality\n\nYoung's Modulus instantiates the linear-response archetype for mechanical deformation: stress (force per area) is proportional to strain (fractional elongation). It is the second derivative of the elastic strain energy density U=½Eε² with respect to strain — the mechanical analog of the capacitive energy ½CV² in electrostatics or the spring energy ½kx². The full elasticity tensor C_ijkl generalises E to anisotropic materials with up to 21 independent components (reduced to 2 for isotropic: E and ν)."),
        ("What The Math Says", 5,
         "Stress sigma equals Young's modulus E times strain epsilon: sigma equals force F over area A, and epsilon equals change in length delta-L over original length L-zero. Young's modulus E has units of pascals (newtons per metre squared) and spans five orders of magnitude: from rubber at approximately 10 megapascals to diamond at approximately 1 terepascal. For a cylindrical rod of length L-zero, area A, and Young's modulus E, the spring constant is k equals E A over L-zero, making the connection to Hooke's law explicit: F equals k times delta-L. Poisson's ratio nu gives the transverse contraction per unit axial extension: a steel rod stretched by 0.1% contracts laterally by approximately 0.03% (nu approximately 0.3 for steel). For an isotropic material, the full stress-strain relation requires only two constants: E and nu, from which shear modulus G and bulk modulus K follow. The elastic strain energy density stored per unit volume is one-half E times epsilon-squared — fully recoverable on unloading, unlike plastic deformation."),
        ("Concept Tags", 6,
         "• Young's modulus\n• stress-strain\n• linear elasticity\n• Hooke's Law\n• Poisson's ratio\n• elastic modulus\n• stiffness\n• shear modulus\n• bulk modulus\n• constitutive relation"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Young's modulus, stress-strain, linear elasticity, Hooke's Law, Poisson's ratio, elastic modulus, stiffness, shear modulus, bulk modulus, constitutive relation", 0),
        ("DS Facets", "mathematical_archetype", "linear-proportionality", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "MS1", "Young's Modulus", "CM9", "Hooke's Law",
         "Young's Modulus is Hooke's Law (F=−kx) expressed per unit geometry: σ=Eε, with E=kL₀/A for a rod. Young's Modulus generalises the spring constant k to a material property independent of sample dimensions."),
        ("analogous to", "MS1", "Young's Modulus", "EM9", "Ohm's Law",
         "Young's Modulus (σ=Eε: stress∝strain) and Ohm's Law (J=σE: current density∝field) are both linear constitutive relations that map a driving quantity to a material response; E and σ are the material-specific proportionality constants."),
        ("analogous to", "MS1", "Young's Modulus", "DM1", "Fick's Laws of Diffusion",
         "Young's Modulus (σ=Eε), Ohm's Law, Fick's Law (J=−D∇c), and Darcy's Law (v=−(k/μ)∇P) are all Fickian linear-response laws: response ∝ driving gradient, with a material-specific coefficient (E, σ, D, k/μ)."),
    ],
},

]


def insert_entries(db_path, entries):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    for e in entries:
        # 1. Insert entry
        cur.execute("""
            INSERT OR IGNORE INTO entries
              (id, title, filename, entry_type, scale, domain, status, confidence, type_group)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (e["id"], e["title"], e["filename"], e["entry_type"], e["scale"],
              e["domain"], e["status"], e["confidence"], e["type_group"]))

        # 2. Insert sections
        for (sname, sorder, content) in e["sections"]:
            cur.execute("""
                INSERT OR IGNORE INTO sections (entry_id, section_name, section_order, content)
                VALUES (?, ?, ?, ?)
            """, (e["id"], sname, sorder, content))

        # 3. Insert properties
        for (tname, pname, pval, porder) in e["properties"]:
            cur.execute("""
                INSERT OR IGNORE INTO entry_properties
                  (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?, ?, ?, ?, ?)
            """, (e["id"], tname, pname, pval, porder))

        # 4. Insert links
        for (ltype, src, slabel, tgt, tlabel, desc) in e.get("links", []):
            cur.execute("""
                INSERT OR IGNORE INTO links
                  (link_type, source_id, source_label, target_id,
                   target_label, description, link_order, confidence_tier)
                VALUES (?, ?, ?, ?, ?, ?, 0, '1.5')
            """, (ltype, src, slabel, tgt, tlabel, desc))

        print(f"  INSERT: {e['id']} — {e['title']}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    print(f"Inserting {len(ENTRIES)} entries into {SOURCE_DB}")
    print("─" * 70)
    insert_entries(SOURCE_DB, ENTRIES)
    print(f"\nDone. {len(ENTRIES)} entries inserted.")
    link_count = sum(len(e.get("links", [])) for e in ENTRIES)
    print(f"       {link_count} new links added.")

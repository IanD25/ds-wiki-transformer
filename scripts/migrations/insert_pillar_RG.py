"""
Pillar Extension — Renormalisation & Scale Dependence (RG)
Inserts 6 new reference_law entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Entries:
  RG01: Wilson's Renormalisation Group
  RG02: Beta Function
  RG03: Kadanoff Block Spin
  RG04: Zamolodchikov c-Theorem
  RG05: a-Theorem (4D)
  RG06: Cotler-Rezchikov RG = Optimal Transport
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── RENORMALISATION & SCALE DEPENDENCE ─────────────────────────────────────

{
    "id": "RG01",
    "title": "Wilson's Renormalisation Group",
    "filename": "RG01_wilson_renormalisation_group.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Wilson's renormalisation group (RG) provides a systematic framework for understanding how physical theories change as one varies the scale of observation — coarse-graining from microscopic to macroscopic descriptions (Wilson, Rev. Mod. Phys. 47, 773, 1975; Nobel Prize 1982). The key insight is that physics at different scales is described by different effective theories, connected by RG transformations that integrate out high-energy (short-distance) degrees of freedom. The RG flow is a trajectory in the space of all possible theories, and fixed points of this flow correspond to scale-invariant theories (conformal field theories at criticality). Wilson's RG explains universality: why systems with completely different microscopic physics exhibit identical behaviour at phase transitions — they flow to the same fixed point. The RG is fundamentally a counting procedure: it tracks how the number of effective degrees of freedom changes with scale, connecting to the c-theorem and the data processing inequality."),
        ("Mathematical Form", 1,
         "RG transformation: Z' = ∫ Dφ_> exp(-S[φ_<, φ_>])\n  (integrate out modes φ_> above cutoff Λ/b)\n\nEffective action: S_eff[φ_<; Λ/b] from S[φ; Λ]\n\nCoupling flow: g_i(μ) = g_i(μ₀) + β_i(g) ln(μ/μ₀) + ...\n\nFixed points: β_i(g*) = 0  (scale-invariant theories)\n\nCritical exponents: eigenvalues of ∂β_i/∂g_j at g*"),
        ("Constraint Category", 2,
         "Dynamical (Di): The RG is a dynamical flow in theory space — it describes how effective theories evolve under scale changes. The flow has fixed points (scale-invariant theories), basins of attraction (universality classes), and irrelevant/relevant directions that determine critical exponents. The RG is the fundamental framework for understanding why different microscopic theories produce the same macroscopic physics: universality."),
        ("DS Cross-References", 3,
         "RG02 (Beta Function — the beta function is the velocity field of the RG flow: it specifies how each coupling changes with scale). RG03 (Kadanoff Block Spin — Kadanoff's block spin is the real-space version of Wilson's momentum-space RG: coarse-graining by spatially averaging). RG04 (Zamolodchikov c-theorem — the c-theorem constrains RG flow: in 2D, a quantity c monotonically decreases along the flow, proving irreversibility). INFO4 (Data Processing Inequality — RG coarse-graining is a form of data processing: integrating out degrees of freedom is information loss, so the DPI constrains RG flow). MATH2 (Central Limit Theorem — the CLT is an RG fixed-point result: the Gaussian is the attractor of the sum-of-random-variables RG flow)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe RG is an optimization over scales: at each scale, the effective theory retains only the relevant degrees of freedom, discarding (integrating out) irrelevant high-energy modes. Fixed points are optimal theories — scale-invariant, with no preferred scale. The flow toward fixed points explains universality: different microscopic starting points converge to the same optimal macroscopic description."),
        ("What The Math Says", 5,
         "Start with a theory defined at a high-energy cutoff Lambda with an action S containing many coupling constants g-i. The RG transformation integrates out degrees of freedom with momenta between Lambda and Lambda over b (where b is the scale factor), producing a new effective action S-eff with modified couplings g-i-prime. Repeating this generates a flow in the space of couplings. The beta function beta-i of g gives the rate of change of coupling g-i with scale: d g-i over d log mu equals beta-i of g. Fixed points where all beta functions vanish are scale-invariant theories — conformal field theories. Near a fixed point, the beta function can be linearised: the eigenvalues of the Jacobian matrix partial beta-i over partial g-j determine the critical exponents that govern power-law behaviour at phase transitions. Positive eigenvalues correspond to relevant operators (important at large scales); negative eigenvalues correspond to irrelevant operators (vanish at large scales). Universality arises because different microscopic theories flow to the same fixed point."),
        ("Concept Tags", 6,
         "• renormalisation group\n• Wilson RG\n• coarse-graining\n• effective theory\n• scale dependence\n• universality\n• fixed point\n• critical phenomena\n• degrees of freedom\n• theory space flow"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "renormalisation group, Wilson RG, coarse-graining, effective theory, scale dependence, universality, fixed point, critical phenomena, degrees of freedom, theory space flow", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "RG01", "Wilson's Renormalisation Group", "RG02", "Beta Function", "The beta function is the velocity field of the RG flow — it specifies how each coupling constant evolves under scale changes."),
        ("generalizes", "RG01", "Wilson's Renormalisation Group", "RG03", "Kadanoff Block Spin", "Wilson's momentum-space RG generalises Kadanoff's real-space block spin procedure to a systematic framework applicable to all field theories."),
        ("analogous to", "RG01", "Wilson's Renormalisation Group", "INFO4", "Mutual Information and Data Processing Inequality", "RG coarse-graining is information-processing: integrating out degrees of freedom is data processing that can only lose information (DPI). The RG flow IS a data-processing flow."),
    ],
},

{
    "id": "RG02",
    "title": "Beta Function",
    "filename": "RG02_beta_function.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The beta function β(g) = dg/d(log μ) describes how a coupling constant g changes with the energy scale μ in a quantum field theory under the renormalisation group flow (Callan, 1970; Symanzik, 1970). Zeros of the beta function correspond to fixed points of the RG: scale-invariant theories where the coupling does not run. Asymptotic freedom (β < 0 at weak coupling) means the coupling decreases at high energies — the theory becomes free in the ultraviolet. Infrared slavery (β > 0 at weak coupling) means the coupling increases at low energies — the theory becomes strongly coupled in the infrared. The beta function encodes the running of all physical observables with scale and determines the phase structure of quantum field theories."),
        ("Mathematical Form", 1,
         "β(g) = μ dg/dμ = dg/d(log μ)\n\nPerturbative expansion:\n  β(g) = −b₀ g³ − b₁ g⁵ − ...  (for gauge theories)\n\nQCD: β(g_s) = −(33 − 2N_f)g_s³/(48π²) + ...  (asymptotic freedom for N_f < 16.5)\n\nQED: β(e) = +e³/(12π²) + ...  (infrared freedom)\n\nFixed points: β(g*) = 0  →  g* is scale-invariant"),
        ("Constraint Category", 2,
         "Dynamical (Di): The beta function is the dynamical law governing scale evolution of coupling constants. It constrains which theories are self-consistent at all scales (those reaching a UV fixed point) and which require completion (those with Landau poles). The running of couplings with scale is the most direct manifestation of the non-trivial quantum structure of field theories."),
        ("DS Cross-References", 3,
         "RG01 (Wilson RG — the beta function is the velocity field of Wilson's RG flow; β(g) = 0 identifies the fixed points). RG04 (Zamolodchikov c-theorem — the c-theorem constrains the beta function: it proves that RG flow is irreversible in 2D, meaning the flow has a Lyapunov function c that decreases monotonically). EM14 (Fine Structure Constant — the fine structure constant α runs with energy scale according to the QED beta function). RG03 (Kadanoff Block Spin — Kadanoff's real-space RG generates discrete beta functions describing how effective couplings change under block-spin transformations)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe beta function defines a gradient-like flow in coupling space. In 2D, the Zamolodchikov c-function proves this flow is a true gradient flow (irreversible). The fixed points β = 0 are the optimal (scale-invariant) theories. The sign of β determines whether a coupling is asymptotically free (relevant in UV), infrared free (relevant in IR), or marginal (exactly scale-invariant)."),
        ("What The Math Says", 5,
         "The beta function of a coupling g is the derivative of g with respect to the logarithm of the energy scale mu: beta of g equals mu times dg over d-mu. When beta is negative, the coupling decreases at higher energies — this is asymptotic freedom, discovered in QCD where the leading coefficient minus b-zero is negative for fewer than 16.5 quark flavours. When beta is positive, the coupling increases at higher energies and eventually hits a Landau pole — this is QED, where the electromagnetic coupling increases logarithmically with energy. When beta is zero, the coupling is scale-invariant: this is a fixed point of the RG flow. In the perturbative expansion, beta equals minus b-zero times g-cubed minus b-one times g-to-the-fifth, where the coefficients b-zero and b-one are determined by the field content of the theory. The universality of the first two coefficients b-zero and b-one (scheme-independent) means that the qualitative behaviour of the flow is a physical prediction, not an artifact of the calculation method."),
        ("Concept Tags", 6,
         "• beta function\n• coupling constant running\n• renormalisation group flow\n• asymptotic freedom\n• Landau pole\n• fixed point\n• scale invariance\n• Callan-Symanzik equation\n• perturbative QFT\n• infrared slavery"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "beta function, coupling constant running, renormalisation group flow, asymptotic freedom, Landau pole, fixed point, scale invariance, Callan-Symanzik equation, perturbative QFT, infrared slavery", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "RG02", "Beta Function", "RG01", "Wilson's Renormalisation Group", "The beta function is the infinitesimal generator of Wilson's RG flow — it specifies the velocity in coupling space."),
        ("couples to", "RG02", "Beta Function", "RG04", "Zamolodchikov c-Theorem", "The c-theorem constrains beta functions in 2D: the flow defined by β must be irreversible (c must decrease), restricting the possible RG trajectories."),
        ("couples to", "RG02", "Beta Function", "EM14", "Fine Structure Constant (α)", "The electromagnetic fine structure constant α runs with energy scale according to the QED beta function: α increases logarithmically at higher energies."),
    ],
},

{
    "id": "RG03",
    "title": "Kadanoff Block Spin Transformation",
    "filename": "RG03_kadanoff_block_spin.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Kadanoff block spin transformation is the real-space implementation of the renormalisation group: it coarse-grains a lattice spin system by grouping adjacent spins into blocks and replacing each block by a single effective spin (Kadanoff, Physics 2, 263, 1966). The block spin has effective coupling constants that differ from the original — the RG transformation maps old couplings to new couplings. This procedure can be iterated, generating an RG flow in coupling space. At a critical point, the system is scale-invariant: the block-spin transformation maps the system to itself, with the same coupling constants. Kadanoff's procedure makes the connection between coarse-graining and information processing explicit: replacing many spins by one block spin is a lossy compression of the microscopic state, directly analogous to data processing. The information lost in each coarse-graining step is bounded by the data processing inequality."),
        ("Mathematical Form", 1,
         "Block spin: s'_I = sign(Σ_{i∈block I} s_i)  (majority rule)\n\nRG map: K' = R(K)  where K = {coupling constants}\n\nFixed point: K* = R(K*)  (critical point)\n\nCorrelation length: ξ → ξ/b after block-spin with scale factor b\n  At criticality: ξ = ∞  →  ξ/b = ∞  (self-similar)\n\nCritical exponents from linearisation:\n  R(K* + δK) ≈ K* + L·δK\n  Eigenvalues of L determine critical exponents"),
        ("Constraint Category", 2,
         "Dynamical (Di): The block spin transformation defines a discrete RG dynamics: each application removes one layer of microscopic detail, flowing toward an effective macroscopic description. The procedure is irreversible — information about the microscopic spin configuration is lost at each step — making it a physical implementation of the data processing inequality."),
        ("DS Cross-References", 3,
         "RG01 (Wilson RG — Kadanoff's block spin is the real-space predecessor of Wilson's momentum-space RG; Wilson generalised and systematised Kadanoff's ideas). INFO4 (Data Processing Inequality — block-spin coarse-graining is a data-processing channel: replacing many spins by one block spin loses information, bounded by the DPI). RG04 (c-theorem — the c-theorem formalises the irreversibility of Kadanoff's procedure: information is lost at each step, and the c-function counts the remaining degrees of freedom). TD3 (Second Law — block-spin coarse-graining is an entropy-increasing process: the block spin system has higher entropy than the original, connecting RG to the second law)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe block spin transformation is an optimal compression: it retains the long-range (relevant) correlations while discarding short-range (irrelevant) details. The fixed point of the transformation is the optimal description — a scale-invariant theory with no preferred scale. The loss of information at each step connects RG to information theory through the data processing inequality."),
        ("What The Math Says", 5,
         "Take a square lattice of Ising spins s-i equals plus or minus 1. Group adjacent spins into blocks of b-by-b spins. Define the block spin s-prime-I as the sign of the sum of spins in block I (majority rule). The partition function is preserved but the effective Hamiltonian changes: the coupling constants K transform to K-prime equals R of K. The correlation length xi transforms to xi over b because the lattice spacing has been scaled by b. At the critical point, xi is infinite, so xi over b is still infinite — the system maps to itself. This is the fixed point K-star where K-star equals R of K-star. Near the fixed point, linearising the RG map gives K-star plus delta-K maps to K-star plus L times delta-K, where L is the linearised RG matrix. The eigenvalues of L determine the critical exponents: an eigenvalue lambda greater than 1 corresponds to a relevant perturbation with critical exponent y equals log lambda over log b. The universality of critical exponents follows from the existence of common fixed points."),
        ("Concept Tags", 6,
         "• block spin\n• Kadanoff\n• real-space RG\n• coarse-graining\n• lattice spin system\n• critical point\n• scale invariance\n• Ising model\n• information compression\n• universality class"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "block spin, Kadanoff, real-space RG, coarse-graining, lattice spin system, critical point, scale invariance, Ising model, information compression, universality class", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "RG03", "Kadanoff Block Spin Transformation", "RG01", "Wilson's Renormalisation Group", "Kadanoff's block spin is the real-space precursor to Wilson's general RG framework — Wilson formalised and extended Kadanoff's physical intuition."),
        ("analogous to", "RG03", "Kadanoff Block Spin Transformation", "INFO4", "Mutual Information and Data Processing Inequality", "Block-spin coarse-graining is a data-processing channel: each step is information-lossy, bounded by the DPI. The RG flow IS data processing on the spin configuration."),
        ("couples to", "RG03", "Kadanoff Block Spin Transformation", "TD3", "Second Law of Thermodynamics", "Block-spin coarse-graining increases entropy — the effective description has fewer degrees of freedom and higher entropy than the original — connecting RG irreversibility to the second law."),
    ],
},

{
    "id": "RG04",
    "title": "Zamolodchikov c-Theorem",
    "filename": "RG04_zamolodchikov_c_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Zamolodchikov c-theorem states that in two-dimensional quantum field theory, there exists a function c(g) of the coupling constants that is monotonically non-increasing along renormalisation group flow: dc/dt ≤ 0 where t parametrises the RG flow from UV to IR (Zamolodchikov, JETP Lett. 43, 730, 1986). At RG fixed points, c equals the central charge of the conformal field theory, which counts the effective number of degrees of freedom. The c-theorem therefore proves that RG flow is irreversible in 2D: the number of effective degrees of freedom can only decrease as one coarse-grains from small scales to large scales. This is the field-theoretic version of the second law of thermodynamics and the information-theoretic data processing inequality: coarse-graining can only lose information, never gain it. The c-theorem was the first rigorous proof that RG flow has a preferred direction — from many degrees of freedom (UV) to few (IR)."),
        ("Mathematical Form", 1,
         "c-function: c(g) is a function of couplings that satisfies:\n  1. dc/dt ≤ 0  along RG flow (t: UV → IR)\n  2. c(g*) = central charge at fixed points g*\n  3. c is stationary at fixed points: ∂c/∂g_i|_{g*} = 0\n\nFor 2D CFT: c = central charge of Virasoro algebra\n\nMonotonicity: c_UV ≥ c_IR  (strict inequality for non-trivial flow)\n\nStrong version: c(g) = C₂(r) + 2r·C₁(r) − ¼r²·C₀(r)\n  where C_n are 2-point function components at scale r"),
        ("Constraint Category", 2,
         "Informatic-Dynamical (In-Di): The c-theorem is an information-theoretic constraint on the dynamics of scale evolution: it proves that RG flow is irreversible. The c-function counts effective degrees of freedom, and its monotonic decrease under RG flow is the field-theoretic analog of entropy increase (second law) and information loss (data processing inequality). The constraint is both informatic (counting degrees of freedom) and dynamical (governing the direction of flow)."),
        ("DS Cross-References", 3,
         "RG01 (Wilson RG — the c-theorem constrains Wilson's RG flow: the flow must decrease the c-function, proving irreversibility). RG05 (a-theorem — the a-theorem is the 4D generalisation: in four dimensions, the a-anomaly coefficient decreases along RG flow). INFO4 (Data Processing Inequality — the c-theorem is the field-theoretic version of the DPI: both say that processing (coarse-graining) can only lose information). HB06 (Area Theorem — both are monotonicity/irreversibility statements: area increases in black hole processes, c decreases in RG flow). TD3 (Second Law — the c-theorem is the field-theoretic second law: entropy (in the form of lost degrees of freedom) can only increase under RG flow). GT03 (Padmanabhan — both describe monotonic decrease of degrees of freedom under a flow: c decreases under RG, N_bulk approaches N_sur under cosmic expansion)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe c-theorem is a monotonicity law (not a conservation law): c can decrease but never increase along RG flow. It is the field-theoretic analog of the second law and the data processing inequality. The monotonicity structure connects three domains: thermodynamics (entropy increase), information theory (information loss), and quantum field theory (degrees of freedom decrease). All three are manifestations of the same underlying principle: coarse-graining is irreversible."),
        ("What The Math Says", 5,
         "In any two-dimensional quantum field theory, there exists a function c of the coupling constants g that satisfies three properties: first, c is non-increasing along the RG flow from UV to IR, dc over dt is at most zero. Second, at any fixed point g-star of the RG, c of g-star equals the central charge of the corresponding conformal field theory. Third, c is stationary at fixed points, meaning its gradient vanishes there. The central charge c counts the effective degrees of freedom of the CFT: a free boson has c equals 1, a free fermion has c equals one-half. The c-theorem proves that c-UV is at least c-IR: the UV theory always has more degrees of freedom than the IR theory. This is strict for non-trivial flow: if the theory actually changes between UV and IR, degrees of freedom are genuinely lost. Zamolodchikov proved this by constructing c explicitly from the two-point correlation functions of the stress-energy tensor at scale r."),
        ("Concept Tags", 6,
         "• c-theorem\n• Zamolodchikov\n• central charge\n• RG irreversibility\n• monotonicity\n• degrees of freedom counting\n• conformal field theory\n• Virasoro algebra\n• field-theoretic second law\n• UV-IR flow"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Di", 0),
        ("entries", "concept_tags", "c-theorem, Zamolodchikov, central charge, RG irreversibility, monotonicity, degrees of freedom counting, conformal field theory, Virasoro algebra, field-theoretic second law, UV-IR flow", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("constrains", "RG04", "Zamolodchikov c-Theorem", "RG01", "Wilson's Renormalisation Group", "The c-theorem proves that Wilson's RG flow is irreversible in 2D: the c-function provides a Lyapunov function that monotonically decreases along the flow."),
        ("analogous to", "RG04", "Zamolodchikov c-Theorem", "INFO4", "Mutual Information and Data Processing Inequality", "Both are irreversibility/monotonicity theorems: the DPI says data processing cannot increase mutual information; the c-theorem says RG coarse-graining cannot increase degrees of freedom."),
        ("analogous to", "RG04", "Zamolodchikov c-Theorem", "HB06", "Black Hole Area Theorem", "Both are monotonicity theorems: black hole area can only increase, central charge can only decrease. Both express irreversibility — of gravitational processes and of scale coarse-graining respectively."),
    ],
},

{
    "id": "RG05",
    "title": "a-Theorem (4D)",
    "filename": "RG05_a_theorem_4d.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The a-theorem states that in four-dimensional quantum field theory, the a-anomaly coefficient of the trace anomaly monotonically decreases along renormalisation group flow: a_UV ≥ a_IR (Komargodski & Schwimmer, JHEP 1112:099, 2011; conjectured by Cardy, 1988). The a-coefficient is the four-dimensional analog of the central charge c in two dimensions — it counts the effective number of degrees of freedom. The a-theorem is the four-dimensional generalisation of Zamolodchikov's c-theorem, proving that RG flow is irreversible in the physical spacetime dimension d = 4. Like the c-theorem, the a-theorem is a deep constraint connecting information theory (irreversibility of coarse-graining) to quantum field theory (degrees of freedom decrease) to thermodynamics (entropy increase under lossy compression)."),
        ("Mathematical Form", 1,
         "a-anomaly coefficient: appears in the trace anomaly\n  ⟨T^μ_μ⟩ = a E₄ − c W²_{μνρσ} + ...\n\nwhere:\n  E₄ = Euler density in 4D\n  W_{μνρσ} = Weyl tensor\n\nMonotonicity: a_UV ≥ a_IR  (strict for non-trivial flow)\n\nFree field values:\n  Real scalar: a = 1/360  (per field)\n  Weyl fermion: a = 11/720  (per field)\n  Vector: a = 31/180  (per field)"),
        ("Constraint Category", 2,
         "Informatic-Dynamical (In-Di): The a-theorem constrains the RG dynamics in four dimensions: the a-coefficient is an irreversibility function, monotonically decreasing under RG flow. It counts degrees of freedom in the same sense as the central charge does in 2D — coarse-graining can only reduce the number of effective degrees of freedom."),
        ("DS Cross-References", 3,
         "RG04 (Zamolodchikov c-theorem — the a-theorem is the 4D extension of the c-theorem; both prove RG irreversibility by showing a monotonic function of couplings decreases along the flow). RG01 (Wilson RG — the a-theorem constrains the flow of Wilson's RG in 4D: the flow must decrease the a-coefficient). INFO4 (Data Processing Inequality — the a-theorem, like the DPI, proves that coarse-graining (data processing) is irreversible: degrees of freedom (information) can only be lost). TD3 (Second Law — the a-theorem is the second law for RG flow in 4D: the a-function is the entropy-like quantity that can only decrease)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe a-theorem is a monotonicity law: a can decrease but never increase along RG flow. It is the 4D version of the field-theoretic second law. The proof by Komargodski and Schwimmer uses the dilaton effective action — the dilaton is a Goldstone boson of broken conformal symmetry, and its scattering amplitude encodes the a-coefficient."),
        ("What The Math Says", 5,
         "In four-dimensional quantum field theories, the trace of the stress-energy tensor in a curved background contains two anomaly coefficients: a (multiplying the Euler density E-4) and c (multiplying the square of the Weyl tensor). The a-coefficient counts degrees of freedom: for a free real scalar it is 1/360, for a Weyl fermion 11/720, for a vector boson 31/180. The a-theorem states that a-UV is at least a-IR for any RG flow connecting a UV conformal field theory to an IR conformal field theory. Komargodski and Schwimmer proved this in 2011 by considering the effective action for a dilaton field — the Goldstone boson of spontaneously broken conformal symmetry. The forward scattering amplitude of four dilatons at low energy is proportional to a-UV minus a-IR, and unitarity (positivity of the spectral density) requires this to be non-negative. The proof is non-perturbative and holds for all four-dimensional quantum field theories."),
        ("Concept Tags", 6,
         "• a-theorem\n• trace anomaly\n• Euler density\n• RG irreversibility\n• four dimensions\n• Komargodski-Schwimmer\n• Cardy conjecture\n• degrees of freedom counting\n• dilaton effective action\n• conformal anomaly"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Di", 0),
        ("entries", "concept_tags", "a-theorem, trace anomaly, Euler density, RG irreversibility, four dimensions, Komargodski-Schwimmer, Cardy conjecture, degrees of freedom counting, dilaton effective action, conformal anomaly", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "RG05", "a-Theorem (4D)", "RG04", "Zamolodchikov c-Theorem", "The a-theorem extends the c-theorem from 2D to 4D — both prove RG irreversibility by exhibiting a monotonically decreasing function along the RG flow."),
        ("constrains", "RG05", "a-Theorem (4D)", "RG01", "Wilson's Renormalisation Group", "The a-theorem constrains Wilson's RG flow in 4D: any RG flow must decrease the a-anomaly coefficient."),
        ("analogous to", "RG05", "a-Theorem (4D)", "TD3", "Second Law of Thermodynamics", "Both are irreversibility statements: the second law says entropy increases in thermodynamic processes; the a-theorem says the a-function decreases (degrees of freedom are lost) in RG flow."),
    ],
},

{
    "id": "RG06",
    "title": "Cotler-Rezchikov: RG as Optimal Transport with Fisher Metric",
    "filename": "RG06_cotler_rezchikov_rg_optimal_transport.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · mathematics · information",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Cotler and Rezchikov showed that renormalisation group flow can be understood as Wasserstein gradient flow — optimal transport — on the space of probability distributions, with the Fisher-Rao metric providing the natural geometry (Cotler & Rezchikov, 2022). The key insight is that the RG flow of a statistical field theory is equivalent to the flow that minimises the Wasserstein distance (earth mover's distance) from a reference measure, where the cost function is determined by the Fisher information metric on the space of field configurations. This establishes an explicit mathematical bridge between three domains: renormalisation group physics (scale dependence), optimal transport theory (Wasserstein geometry), and information geometry (Fisher-Rao metric). The Fisher metric IS the infinitesimal geometry of RG flow — connecting scale dependence directly to the curvature of probability space, and through Bianconi's framework, to gravitational dynamics."),
        ("Mathematical Form", 1,
         "RG flow as Wasserstein gradient flow:\n  ∂ρ/∂t = ∇ · (ρ ∇(δF/δρ))  (continuity equation)\n\nwhere:\n  ρ = probability distribution on field configuration space\n  F[ρ] = free energy functional\n  t = RG scale parameter\n\nFisher-Rao metric on configuration space:\n  g_ij = E_ρ[∂_i log ρ · ∂_j log ρ]\n\nWasserstein-2 distance:\n  W₂²(μ,ν) = inf_{γ∈Γ(μ,ν)} ∫ d(x,y)² dγ(x,y)"),
        ("Constraint Category", 2,
         "Informatic-Geometric (In-Gm): The Cotler-Rezchikov result is an informatic-geometric bridge: it shows that the geometry of RG flow (scale dependence) is the Fisher-Rao metric (information geometry). The constraint is that RG flow is not arbitrary but follows the Wasserstein gradient — the most efficient path of scale evolution as measured by the Fisher metric on probability space."),
        ("DS Cross-References", 3,
         "IT05 (Fisher Information — the Fisher information matrix provides the Riemannian metric that governs the geometry of RG flow in the Cotler-Rezchikov framework). IT08 (Fisher-Rao Metric — the Fisher-Rao metric IS the metric of RG flow: Cotler-Rezchikov makes this identification explicit). RG01 (Wilson RG — the Cotler-Rezchikov result gives Wilson's RG flow an information-geometric interpretation: it is Wasserstein gradient flow with Fisher metric). GT04 (Bianconi — both use the Fisher metric as the fundamental geometric object: Cotler-Rezchikov for RG flow, Bianconi for gravity. The Fisher metric connects scale dependence to gravitational dynamics). RG04 (c-theorem — the c-theorem's irreversibility is a consequence of the Wasserstein gradient flow structure: gradient flows have built-in monotonicity)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe Cotler-Rezchikov result shows that RG flow is an optimisation: it is the gradient flow that minimises free energy along the Wasserstein metric. This is optimal transport: the RG moves probability mass on configuration space along the most efficient routes as measured by the Fisher-Rao distance. The gradient flow structure automatically implies monotonicity (connecting to the c-theorem) and provides the geometric framework connecting RG to gravity."),
        ("What The Math Says", 5,
         "The distribution rho on field configuration space evolves under RG flow according to a continuity equation: partial rho over partial t equals the divergence of rho times the gradient of the functional derivative of the free energy F with respect to rho. This is the standard form of Wasserstein gradient flow — the flow that decreases the free energy as efficiently as possible with respect to the Wasserstein-2 distance. The Wasserstein-2 distance W-2-squared between two distributions mu and nu is the minimum cost of transporting mu to nu, where the cost is the squared geodesic distance in the underlying space. Cotler and Rezchikov show that the natural metric on the underlying field configuration space is the Fisher-Rao metric g-ij equals the expected product of score functions. The Fisher-Rao metric is the unique Riemannian metric on probability space invariant under sufficient statistics (Chentsov). This means the geometry governing RG flow is determined by information theory: the Fisher-Rao metric encodes how distinguishable nearby theories are, and the RG flow follows the path of least informational cost."),
        ("Concept Tags", 6,
         "• Cotler-Rezchikov\n• RG as optimal transport\n• Wasserstein gradient flow\n• Fisher-Rao metric\n• information geometry of RG\n• earth mover distance\n• free energy minimisation\n• scale-dependent geometry\n• Fisher metric\n• optimal transport theory"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "Cotler-Rezchikov, RG as optimal transport, Wasserstein gradient flow, Fisher-Rao metric, information geometry of RG, earth mover distance, free energy minimisation, scale-dependent geometry, Fisher metric, optimal transport theory", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("couples to", "RG06", "Cotler-Rezchikov: RG as Optimal Transport with Fisher Metric", "IT08", "Fisher-Rao Metric", "Cotler-Rezchikov show that the Fisher-Rao metric IS the natural geometry of RG flow — RG is Wasserstein gradient flow with Fisher-Rao as the transport cost metric."),
        ("derives from", "RG06", "Cotler-Rezchikov: RG as Optimal Transport with Fisher Metric", "RG01", "Wilson's Renormalisation Group", "Cotler-Rezchikov give Wilson's RG an information-geometric interpretation: the flow is Wasserstein gradient descent on the Fisher-Rao manifold."),
        ("analogous to", "RG06", "Cotler-Rezchikov: RG as Optimal Transport with Fisher Metric", "GT04", "Bianconi Gravity from Entropy", "Both use the Fisher metric as the fundamental geometric object: Cotler-Rezchikov for RG flow, Bianconi for gravity. The Fisher metric is the common bridge connecting scale dependence to spacetime geometry."),
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
    print(f"Inserting RG pillar ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)

"""
Pillar Extension — Information Theory (IT)
Inserts 5 new reference_law entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Skipped (already exist):
  INFO1 = Shannon Entropy (≡ spec IT01)
  INFO4 = Mutual Information & DPI (≡ spec IT06 + IT07)

New entries:
  IT02: Von Neumann Entropy
  IT03: KL Divergence
  IT04: Quantum Relative Entropy
  IT05: Fisher Information
  IT08: Fisher-Rao Metric
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── INFORMATION THEORY ─────────────────────────────────────────────────────

{
    "id": "IT02",
    "title": "Von Neumann Entropy",
    "filename": "IT02_von_neumann_entropy.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "information · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The von Neumann entropy S(ρ) = −Tr(ρ log ρ) is the quantum generalisation of Shannon entropy, measuring the information content — equivalently the degree of mixedness — of a quantum state described by a density matrix ρ (von Neumann, 1932). For a pure state, S = 0; for a maximally mixed state of dimension d, S = log d. Von Neumann entropy quantifies entanglement: the entropy of a subsystem's reduced density matrix equals the entanglement entropy between subsystem and environment. This makes it the bridge between quantum information theory and black hole thermodynamics, where the Bekenstein-Hawking entropy of a black hole equals the entanglement entropy across the event horizon."),
        ("Mathematical Form", 1,
         "S(ρ) = −Tr(ρ log ρ) = −Σ_i λ_i log λ_i\n\nwhere {λ_i} are eigenvalues of the density matrix ρ\n\nFor a bipartite pure state |ψ⟩_AB:\n  S(ρ_A) = S(ρ_B)  (Schmidt decomposition symmetry)\n\nSubadditivity: S(ρ_AB) ≤ S(ρ_A) + S(ρ_B)\nStrong subadditivity: S(ρ_ABC) + S(ρ_B) ≤ S(ρ_AB) + S(ρ_BC)  (Lieb-Ruskai, 1973)"),
        ("Constraint Category", 2,
         "Informatic (In): Von Neumann entropy is the unique measure of quantum uncertainty satisfying continuity, additivity for product states, and subadditivity. Strong subadditivity — the deepest inequality in quantum information theory — constrains how quantum correlations can be distributed across subsystems. It is the quantum analog of the second law: under any completely positive trace-preserving map (quantum channel), entropy cannot decrease."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — von Neumann entropy reduces to Shannon entropy for diagonal density matrices; the quantum-classical bridge). HB02 (Bekenstein-Hawking Entropy — BH entropy equals entanglement entropy across the horizon, connecting quantum information to gravitational thermodynamics). IT04 (Quantum Relative Entropy — S(ρ||σ) = Tr(ρ log ρ − ρ log σ) generalises KL divergence to quantum states; von Neumann entropy is S(ρ||I/d) up to a constant). TD3 (Second Law — strong subadditivity is the quantum version of the second law of thermodynamics)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nVon Neumann entropy is bounded: 0 ≤ S(ρ) ≤ log d. The lower bound is saturated by pure states (zero uncertainty), the upper bound by maximally mixed states (maximum uncertainty). Strong subadditivity constrains the distribution of quantum correlations exactly as the second law constrains thermodynamic processes — both are monotonicity statements about information processing."),
        ("What The Math Says", 5,
         "The von Neumann entropy of a quantum state described by density matrix rho equals minus the trace of rho times log rho, which equals minus the sum of eigenvalues lambda-i times log lambda-i. For a pure state (single eigenvalue 1), the entropy is zero — there is no uncertainty. For a maximally mixed state of d dimensions (all eigenvalues 1/d), the entropy is log d — maximum uncertainty. For a bipartite pure state, the entanglement entropy of subsystem A equals that of subsystem B — entanglement is symmetric. Subadditivity says the entropy of a joint system AB is at most the sum of entropies of A and B separately. Strong subadditivity adds a third system C and says S(ABC) + S(B) is at most S(AB) + S(BC) — this is the deepest constraint on quantum information and was proved by Lieb and Ruskai in 1973."),
        ("Concept Tags", 6,
         "• von Neumann entropy\n• density matrix\n• quantum information\n• entanglement entropy\n• strong subadditivity\n• reduced density matrix\n• quantum channel\n• mixedness\n• Schmidt decomposition\n• quantum-classical bridge"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "von Neumann entropy, density matrix, quantum information, entanglement entropy, strong subadditivity, reduced density matrix, quantum channel, mixedness, Schmidt decomposition, quantum-classical bridge", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "IT02", "Von Neumann Entropy", "INFO1", "Shannon Entropy", "Von Neumann entropy reduces to Shannon entropy for diagonal density matrices (classical probability distributions); it is the unique quantum extension."),
        ("analogous to", "IT02", "Von Neumann Entropy", "TD3", "Second Law of Thermodynamics", "Strong subadditivity of von Neumann entropy is the quantum version of the second law — entropy cannot decrease under quantum channels, just as thermodynamic entropy cannot decrease in isolated systems."),
        ("couples to", "IT02", "Von Neumann Entropy", "HB02", "Bekenstein-Hawking Entropy", "Bekenstein-Hawking entropy equals the entanglement entropy (von Neumann entropy of the reduced state) across the event horizon — the direct bridge between quantum information and black hole thermodynamics."),
    ],
},

{
    "id": "IT03",
    "title": "Kullback-Leibler Divergence",
    "filename": "IT03_kl_divergence.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Kullback-Leibler divergence D_KL(P||Q) = Σ p_i log(p_i/q_i) measures the information lost when distribution Q is used to approximate distribution P (Kullback & Leibler, 1951). It is not a distance (it is asymmetric and does not satisfy the triangle inequality), but it is the fundamental measure of statistical distinguishability between probability distributions. KL divergence connects information theory to thermodynamics: the free energy difference between two thermal states equals kT times their KL divergence. It connects to geometry: the Hessian (second derivative) of KL divergence with respect to parameters defines the Fisher information metric on the space of probability distributions, making it the infinitesimal generator of information geometry."),
        ("Mathematical Form", 1,
         "D_KL(P||Q) = Σ_i p_i log(p_i / q_i) = E_P[log(P/Q)]\n\nContinuous: D_KL(p||q) = ∫ p(x) log[p(x)/q(x)] dx\n\nProperties:\n  D_KL(P||Q) ≥ 0  (Gibbs' inequality)\n  D_KL(P||Q) = 0  iff P = Q\n  D_KL(P||Q) ≠ D_KL(Q||P)  in general (asymmetric)\n\nHessian: ∂²D_KL(p_θ||p_{θ₀}) / ∂θ^i∂θ^j |_{θ=θ₀} = g_ij(θ₀)  (Fisher metric)"),
        ("Constraint Category", 2,
         "Informatic (In): KL divergence is non-negative (Gibbs' inequality), which is equivalent to the second law of thermodynamics in the information-theoretic formulation. The non-negativity encodes the irreversibility of information processing: once you coarse-grain (replace P by Q), the information loss D_KL(P||Q) is always positive. This makes KL divergence the master inequality from which both the second law and the data processing inequality follow."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — KL divergence D_KL(P||U) from any distribution to the uniform distribution equals log N minus the Shannon entropy H(P); entropy measures distance from maximum uncertainty). IT04 (Quantum Relative Entropy — S(ρ||σ) = Tr(ρ log ρ − ρ log σ) is the quantum generalisation of KL divergence). IT05 (Fisher Information — the Fisher metric is the Hessian of KL divergence; Fisher information is the infinitesimal version of KL divergence). TD3 (Second Law — the second law is equivalent to D_KL(P_t||P_eq) being non-increasing under equilibration). B5 (Landauer's Principle — the energy cost of erasing one bit is kT ln 2, which equals kT times the KL divergence between the initial and erased states)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nKL divergence is the master bound of information theory: it is non-negative, zero only at the optimum (P = Q), and its Taylor expansion yields the Fisher metric. It governs the rate of statistical learning (Sanov's theorem), the efficiency of coding (Shannon's source coding theorem), and the direction of thermodynamic evolution (free energy minimisation). Every irreversibility statement in information theory can be traced back to the non-negativity of KL divergence."),
        ("What The Math Says", 5,
         "The KL divergence from P to Q sums over all outcomes i the probability p-i times the log ratio of p-i to q-i. It measures the expected number of extra bits (or nats) needed to encode samples from P using a code optimised for Q. It is always non-negative by Gibbs' inequality, and equals zero only when P equals Q everywhere. The asymmetry means D-KL of P given Q generally differs from D-KL of Q given P. The continuous version integrates p of x times log of p of x over q of x. The second derivative of KL divergence at theta equals theta-zero gives the Fisher information matrix g-ij — this is the key bridge to information geometry, showing that the Fisher-Rao metric is the infinitesimal structure of statistical divergence."),
        ("Concept Tags", 6,
         "• KL divergence\n• relative entropy\n• information divergence\n• Gibbs inequality\n• statistical distinguishability\n• free energy\n• Fisher information\n• information geometry\n• asymmetric divergence\n• Sanov theorem"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "KL divergence, relative entropy, information divergence, Gibbs inequality, statistical distinguishability, free energy, Fisher information, information geometry, asymmetric divergence, Sanov theorem", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "IT03", "Kullback-Leibler Divergence", "INFO1", "Shannon Entropy", "Shannon entropy H(P) = log N − D_KL(P||U); entropy is the complement of KL divergence from the uniform distribution, making KL the more fundamental quantity."),
        ("couples to", "IT03", "Kullback-Leibler Divergence", "TD3", "Second Law of Thermodynamics", "The second law in its information-theoretic form states that D_KL(P_t||P_eq) is non-increasing: systems evolve to minimise their KL divergence from equilibrium, which equals free energy minimisation."),
        ("derives from", "IT03", "Kullback-Leibler Divergence", "IT05", "Fisher Information", "The Fisher information metric is the Hessian of KL divergence: g_ij = ∂²D_KL/∂θ^i∂θ^j. Fisher information is the infinitesimal, local version of KL divergence."),
    ],
},

{
    "id": "IT04",
    "title": "Quantum Relative Entropy",
    "filename": "IT04_quantum_relative_entropy.md",
    "entry_type": "reference_law",
    "scale": "quantum",
    "domain": "information · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Quantum relative entropy S(ρ||σ) = Tr(ρ log ρ − ρ log σ) is the quantum generalisation of Kullback-Leibler divergence, measuring the distinguishability between two quantum states ρ and σ (Umegaki, 1962). Like its classical counterpart, it is non-negative (Klein's inequality: S(ρ||σ) ≥ 0) and equals zero only when ρ = σ. It is monotonically non-increasing under completely positive trace-preserving maps — the quantum data processing inequality. This monotonicity is the deepest formulation of the second law of quantum thermodynamics: quantum operations can only destroy the distinguishability between states. The quantum Fisher information emerges as the Hessian of quantum relative entropy, linking quantum information geometry to gravitational dynamics in frameworks such as Bianconi's."),
        ("Mathematical Form", 1,
         "S(ρ||σ) = Tr(ρ log ρ − ρ log σ)\n\nProperties:\n  S(ρ||σ) ≥ 0  (Klein's inequality)\n  S(ρ||σ) = 0  iff ρ = σ\n  S(Φ(ρ)||Φ(σ)) ≤ S(ρ||σ)  (monotonicity under CPTP maps)\n\nPinsker's inequality: ||ρ − σ||₁² ≤ 2 S(ρ||σ)\n\nQuantum Fisher information: g_ij^Q = −∂²S(ρ_θ||ρ_{θ₀})/∂θ^i∂θ^j |_{θ=θ₀}"),
        ("Constraint Category", 2,
         "Informatic (In): The monotonicity of quantum relative entropy under quantum channels (CPTP maps) is the master inequality of quantum information theory. It implies strong subadditivity of von Neumann entropy, the quantum data processing inequality, and the second law of quantum thermodynamics. Every irreversibility result in quantum theory can be derived from this single property."),
        ("DS Cross-References", 3,
         "IT03 (KL Divergence — quantum relative entropy generalises KL divergence to non-commutative quantum states; reduces to KL for simultaneously diagonalisable density matrices). IT02 (Von Neumann Entropy — S(ρ) = −S(ρ||I/d) + log d; von Neumann entropy is related to quantum relative entropy against the maximally mixed state). IT05 (Fisher Information — quantum Fisher information is the Hessian of quantum relative entropy, the infinitesimal geometry of quantum state space). GT04 (Bianconi Gravity from Entropy — Bianconi's framework uses quantum relative entropy and its Fisher information to derive gravitational dynamics from information geometry)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nQuantum relative entropy is the quantum master bound: non-negative, monotone under physical operations, and generating the quantum Fisher metric as its infinitesimal structure. It unifies the second law (irreversibility), the data processing inequality (information loss), and information geometry (curvature of state space) into a single mathematical object."),
        ("What The Math Says", 5,
         "Quantum relative entropy of rho with respect to sigma equals the trace of rho times log rho minus rho times log sigma. Klein's inequality guarantees this is non-negative, equalling zero only when the two states are identical. The key property is monotonicity: applying any quantum channel Phi to both states cannot increase their relative entropy, meaning S of Phi-rho given Phi-sigma is at most S of rho given sigma. Pinsker's inequality bounds the trace distance between two states by the square root of twice their relative entropy. The quantum Fisher information matrix g-ij-Q is the negative Hessian of quantum relative entropy, making it the natural Riemannian metric on the space of quantum states — the quantum version of the Fisher-Rao metric."),
        ("Concept Tags", 6,
         "• quantum relative entropy\n• Umegaki relative entropy\n• Klein inequality\n• quantum data processing inequality\n• CPTP monotonicity\n• quantum Fisher information\n• quantum second law\n• Pinsker inequality\n• quantum state distinguishability\n• information geometry"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "quantum relative entropy, Umegaki relative entropy, Klein inequality, quantum data processing inequality, CPTP monotonicity, quantum Fisher information, quantum second law, Pinsker inequality, quantum state distinguishability, information geometry", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "IT04", "Quantum Relative Entropy", "IT03", "Kullback-Leibler Divergence", "Quantum relative entropy reduces to classical KL divergence when both density matrices are diagonal — it is the unique quantum extension preserving monotonicity under physical operations."),
        ("derives from", "IT04", "Quantum Relative Entropy", "IT02", "Von Neumann Entropy", "Von Neumann entropy S(ρ) = log d − S(ρ||I/d); the von Neumann entropy is determined by the quantum relative entropy to the maximally mixed state."),
        ("couples to", "IT04", "Quantum Relative Entropy", "GT04", "Bianconi Gravity from Entropy", "Bianconi's framework derives gravitational dynamics from the quantum relative entropy and its Fisher information metric on quantum state space — gravity emerges from quantum information geometry."),
    ],
},

{
    "id": "IT05",
    "title": "Fisher Information",
    "filename": "IT05_fisher_information.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Fisher information I(θ) = E[(∂/∂θ log f(x;θ))²] measures the amount of information that an observable random variable X carries about an unknown parameter θ of the distribution f(x;θ) (Fisher, 1925). It is the expected curvature (second derivative) of the log-likelihood function, quantifying how sensitively the probability distribution responds to changes in the parameter. Fisher information is the Hessian of KL divergence: the infinitesimal version of statistical distinguishability. The Fisher information matrix g_ij = E[∂_i log f · ∂_j log f] defines a Riemannian metric on the space of probability distributions — the Fisher-Rao metric — making parameter estimation a problem of differential geometry. This geometric interpretation connects statistical inference to general relativity (Ruppeiner geometry), renormalisation group flow (Cotler-Rezchikov), and emergent gravity (Bianconi)."),
        ("Mathematical Form", 1,
         "Scalar: I(θ) = E[(∂/∂θ log f(x;θ))²] = −E[∂²/∂θ² log f(x;θ)]\n\nMatrix (multiparameter):\n  g_ij(θ) = E[∂_i log f(x;θ) · ∂_j log f(x;θ)]\n         = −E[∂_i ∂_j log f(x;θ)]\n\nCramér-Rao bound: Var(θ̂) ≥ 1/I(θ)\n\nRelation to KL: g_ij(θ₀) = ∂²D_KL(p_θ||p_{θ₀})/∂θ^i∂θ^j |_{θ=θ₀}"),
        ("Constraint Category", 2,
         "Informatic (In): The Cramér-Rao bound is the fundamental precision limit of statistical estimation: no unbiased estimator can have variance smaller than the inverse Fisher information. This is the information-theoretic analog of the uncertainty principle — both state that precision is bounded by the curvature of the underlying probability/wavefunction space. Fisher information also decreases under sufficient statistics (the information processing inequality at the infinitesimal level)."),
        ("DS Cross-References", 3,
         "IT03 (KL Divergence — Fisher information is the Hessian of KL divergence; the local curvature of the divergence surface at its minimum). IT08 (Fisher-Rao Metric — the Fisher information matrix IS the metric tensor of the Fisher-Rao Riemannian metric on statistical manifolds). BR04 (Thermodynamic Geometry — Ruppeiner's thermodynamic metric is Fisher-Rao applied to Gibbs/Boltzmann distributions, connecting statistical inference to thermodynamic geometry). RG06 (Cotler-Rezchikov — RG flow is Wasserstein gradient flow with Fisher metric, connecting information geometry to scale dependence). INFO4 (Data Processing Inequality — Fisher information decreases under data processing; the infinitesimal version of the DPI)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nFisher information defines the optimal precision of parameter estimation (Cramér-Rao), the natural geometry of statistical models (Fisher-Rao), and the local structure of information divergence (Hessian of KL). It is the bridge between information theory and differential geometry: wherever a probability distribution depends on parameters, Fisher information supplies the natural metric for comparing nearby distributions."),
        ("What The Math Says", 5,
         "The Fisher information of a distribution f parameterised by theta is the expected value of the squared score function: the square of the partial derivative of log f with respect to theta. Equivalently, it is minus the expected second derivative of the log-likelihood — the curvature at the peak. Higher curvature means the likelihood is more peaked, the data is more informative, and parameters can be estimated more precisely. The Cramer-Rao bound states that the variance of any unbiased estimator of theta is at least 1 over I of theta. In the multiparameter case, the Fisher information matrix g-ij has entries equal to the expected product of score functions partial-i log f times partial-j log f. This matrix is the Riemannian metric tensor on the manifold of probability distributions — the Fisher-Rao metric. The key bridge identity: g-ij at theta-zero equals the Hessian of KL divergence D-KL of p-theta given p-theta-zero, evaluated at theta equals theta-zero."),
        ("Concept Tags", 6,
         "• Fisher information\n• Fisher information matrix\n• Cramér-Rao bound\n• score function\n• log-likelihood curvature\n• information geometry\n• statistical estimation\n• Riemannian metric\n• parameter sensitivity\n• Hessian of KL divergence"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Fisher information, Fisher information matrix, Cramér-Rao bound, score function, log-likelihood curvature, information geometry, statistical estimation, Riemannian metric, parameter sensitivity, Hessian of KL divergence", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "IT05", "Fisher Information", "IT03", "Kullback-Leibler Divergence", "Fisher information is the Hessian of KL divergence: I(θ) = ∂²D_KL(p_θ||p_{θ₀})/∂θ² — the infinitesimal measure of statistical distinguishability."),
        ("couples to", "IT05", "Fisher Information", "INFO4", "Mutual Information and Data Processing Inequality", "Fisher information decreases under sufficient statistics and data processing — the infinitesimal version of the Data Processing Inequality for mutual information."),
        ("couples to", "IT05", "Fisher Information", "IT08", "Fisher-Rao Metric", "The Fisher information matrix g_ij is the metric tensor of the Fisher-Rao Riemannian geometry on statistical manifolds."),
    ],
},

{
    "id": "IT08",
    "title": "Fisher-Rao Metric",
    "filename": "IT08_fisher_rao_metric.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Fisher-Rao metric ds² = g_ij dθ^i dθ^j, where g_ij = E[∂_i log f · ∂_j log f], is the unique Riemannian metric on the space of probability distributions that is invariant under sufficient statistics (Chentsov's theorem, 1972). It endows the manifold of parametric probability distributions with a natural geometry where geodesic distance measures statistical distinguishability. This is the foundational object of information geometry (Amari, 1985). The Fisher-Rao metric on thermodynamic state space IS the Ruppeiner metric, connecting information geometry to thermodynamic geometry. The Fisher-Rao metric on quantum state space IS the Fubini-Study metric (for pure states) or the Bures metric (for mixed states), connecting information geometry to quantum mechanics. These bridges make the Fisher-Rao metric the geometric unifier of statistics, thermodynamics, and quantum theory."),
        ("Mathematical Form", 1,
         "ds² = g_ij(θ) dθ^i dθ^j\n\nwhere g_ij(θ) = E[∂_i log f(x;θ) · ∂_j log f(x;θ)] = ∫ (∂_i log f)(∂_j log f) f dx\n\nChentsov uniqueness: g_ij is the ONLY Riemannian metric invariant under\nMarkov morphisms (sufficient statistics)\n\nGeodesic distance: d(p,q) = arccos(∫ √(p(x)q(x)) dx)  (for statistical manifolds)\n\nRuppeiner metric: ds² = −∂²S/∂X^i∂X^j dX^i dX^j  (Hessian of entropy)"),
        ("Constraint Category", 2,
         "Geometric (Gm): The Fisher-Rao metric is a geometric constraint — Chentsov's theorem shows it is the unique Riemannian structure compatible with the category of statistical models. Just as general relativity has a unique metric (up to diffeomorphisms) satisfying the Einstein equations, information geometry has a unique metric satisfying invariance under sufficient statistics. This uniqueness is why the same metric appears in thermodynamics (Ruppeiner), quantum mechanics (Bures/Fubini-Study), and gravity (Bianconi)."),
        ("DS Cross-References", 3,
         "IT05 (Fisher Information — the Fisher information matrix IS the metric tensor of the Fisher-Rao metric; the metric is the global geometric structure built from the local curvature of KL divergence). IT03 (KL Divergence — the Fisher-Rao metric is the infinitesimal structure of KL divergence; ds² approximates 2·D_KL for nearby distributions). BR04 (Thermodynamic Geometry — Ruppeiner metric on thermodynamic state space is Fisher-Rao applied to the canonical Gibbs ensemble; the Hessian of entropy IS the Fisher metric). RG06 (Cotler-Rezchikov — RG flow is gradient flow with respect to the Fisher-Rao metric, connecting scale dependence to information geometry). GT04 (Bianconi — derives gravitational dynamics from the Fisher-Rao geometry on quantum state space)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nThe Fisher-Rao metric is the unique natural geometry on probability space, the optimization landscape for statistical inference. Geodesics are the shortest paths between distributions, and the curvature tensor encodes the intrinsic difficulty of statistical estimation. The Cramér-Rao bound is a consequence of this geometry: the minimum variance of an estimator equals the inverse of the metric component, which is the geodesic distance squared in the parameter direction."),
        ("What The Math Says", 5,
         "The Fisher-Rao line element ds-squared equals g-ij times d-theta-i times d-theta-j, where the metric tensor g-ij is the expected product of the partial derivatives of log f with respect to parameters theta-i and theta-j. Chentsov proved in 1972 that this is the only Riemannian metric on the space of probability distributions that is invariant under sufficient statistics — meaning it does not depend on how the data is represented, only on its information content. The geodesic distance between distributions p and q is the arccosine of the Bhattacharyya coefficient, which equals the integral of the square root of p times q. On thermodynamic state space, the Fisher-Rao metric becomes the Ruppeiner metric: minus the Hessian of entropy with respect to extensive variables. On quantum state space for pure states, it becomes the Fubini-Study metric. For mixed quantum states, it becomes the Bures metric. This universality makes Fisher-Rao the geometric bridge between information theory, thermodynamics, and quantum mechanics."),
        ("Concept Tags", 6,
         "• Fisher-Rao metric\n• information geometry\n• Chentsov theorem\n• statistical manifold\n• Riemannian metric\n• Ruppeiner metric\n• Fubini-Study metric\n• Bures metric\n• geodesic distance\n• natural geometry of probability"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Gm", 0),
        ("entries", "concept_tags", "Fisher-Rao metric, information geometry, Chentsov theorem, statistical manifold, Riemannian metric, Ruppeiner metric, Fubini-Study metric, Bures metric, geodesic distance, natural geometry of probability", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "IT08", "Fisher-Rao Metric", "IT05", "Fisher Information", "The Fisher-Rao metric is the global Riemannian geometry whose metric tensor at each point is the Fisher information matrix — the metric is the geometric integration of local Fisher information."),
        ("analogous to", "IT08", "Fisher-Rao Metric", "GV1", "General Relativity — Einstein Field Equations", "Both are unique Riemannian metrics: Fisher-Rao is the unique metric on probability space (Chentsov); the Einstein metric is the unique dynamics on spacetime (Lovelock). The structural parallel deepens in Bianconi's framework where gravity emerges from Fisher-Rao geometry."),
        ("couples to", "IT08", "Fisher-Rao Metric", "BR04", "Thermodynamic Geometry (Ruppeiner)", "The Ruppeiner thermodynamic metric IS the Fisher-Rao metric applied to the Gibbs canonical ensemble — information geometry and thermodynamic geometry are the same geometry."),
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
    print(f"Inserting IT pillar ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)

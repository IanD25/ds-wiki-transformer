"""
Option E — Chunk 2: Mathematics + Information Theory + Statistics
Inserts 15 new reference_law entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Entries:
  MATH1: Bayes' Theorem
  MATH2: Central Limit Theorem
  MATH3: Law of Large Numbers
  MATH4: Gödel's Incompleteness Theorems
  MATH5: Fundamental Theorem of Calculus
  MATH6: Prime Number Theorem
  MATH7: Euler's Identity
  MATH8: Generalized Stokes' Theorem
  INFO1: Shannon Entropy
  INFO2: Shannon Source Coding Theorem
  INFO3: Shannon Noisy-Channel Coding Theorem
  INFO4: Mutual Information & Data Processing Inequality
  INFO5: Kolmogorov Complexity
  STAT1: Maximum Entropy Principle (Jaynes)
  STAT2: Ergodic Theorem (Birkhoff)
"""

import sqlite3

SOURCE_DB = "/Users/iandarling/Library/Mobile Documents/com~apple~CloudDocs/Primary Work Outputs/wiki build/ds-wiki-repo/ds_wiki.db"

ENTRIES = [

# ── MATHEMATICS ────────────────────────────────────────────────────────────

{
    "id": "MATH1",
    "title": "Bayes' Theorem",
    "filename": "MATH1_bayes_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The posterior probability of a hypothesis given evidence equals the likelihood of the evidence given the hypothesis times the prior probability of the hypothesis, divided by the marginal probability of the evidence (Bayes, 1763; Laplace, 1812). Bayes' theorem is the unique consistent rule for updating beliefs in light of new information. It formalises rational inference: how prior knowledge is revised by data."),
        ("Mathematical Form", 1,
         "P(H|E) = P(E|H) · P(H) / P(E)\n\nwhere P(E) = Σ_i P(E|H_i) · P(H_i)  (law of total probability)\n\nLog-odds form: log[P(H|E)/P(¬H|E)] = log[P(E|H)/P(E|¬H)] + log[P(H)/P(¬H)]"),
        ("Constraint Category", 2,
         "Informatic (In): Bayes' theorem is the unique probability update rule consistent with the axioms of probability theory (Cox's theorem). The theorem is not optional — any other update rule violates either coherence or consistency. It quantifies the information content of evidence as the log likelihood ratio log[P(E|H)/P(E|¬H)]."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — Bayesian updating minimises expected posterior entropy; the KL divergence D_KL(posterior||prior) measures information gained). M6 (Fisher Information — Fisher information is the curvature of the log-likelihood; Bayes and Fisher are the two foundations of statistical inference). BIO8 (Neutral Theory — phylogenetic Bayesian inference applies Bayes' theorem to molecular evolution). STAT1 (Maximum Entropy Principle — MaxEnt provides the least-informative prior; Bayes provides the update rule)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: statistical-distribution\n\nBayes' theorem describes the transformation of one probability distribution (prior) into another (posterior) through the likelihood function. The posterior is the Bayes-optimal belief state given the prior and evidence. In the limit of many observations, the posterior concentrates on the true parameter value regardless of the prior — Bayesian consistency."),
        ("What The Math Says", 5,
         "The probability of hypothesis H given evidence E equals the probability of E given H times the prior probability of H, divided by the total probability of E. The total probability of E sums over all hypotheses: each hypothesis H-i contributes P(E|H-i) times P(H-i). In log-odds form, the posterior log-odds equal the prior log-odds plus the log likelihood ratio — this shows that evidence adds information multiplicatively to prior belief. The log likelihood ratio log[P(E|H)/P(E|not-H)] is the information content of the evidence in bits when using log base 2, and equals zero for completely uninformative evidence."),
        ("Concept Tags", 6,
         "• Bayes theorem\n• posterior probability\n• prior probability\n• likelihood function\n• Bayesian inference\n• belief updating\n• conditional probability\n• log-odds\n• Cox theorem\n• Bayesian consistency"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Bayes theorem, posterior probability, prior probability, likelihood function, Bayesian inference, belief updating, conditional probability, log-odds, Cox theorem, Bayesian consistency", 0),
        ("DS Facets", "mathematical_archetype", "statistical-distribution", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "MATH1", "Bayes' Theorem", "INFO1", "Shannon Entropy", "Bayesian updating minimises expected posterior entropy; the information gained equals the KL divergence from prior to posterior."),
        ("couples to", "MATH1", "Bayes' Theorem", "M6", "M6: Fisher Information Rank", "Fisher information is the expected curvature of the log-likelihood — the local metric on the manifold of distributions that Bayes' theorem navigates."),
        ("implements", "MATH1", "Bayes' Theorem", "STAT1", "Maximum Entropy Principle", "The maximum entropy prior (Jaynes) provides the least-informative starting point; Bayes' theorem then specifies the rational update when evidence arrives."),
    ],
},

{
    "id": "MATH2",
    "title": "Central Limit Theorem",
    "filename": "MATH2_central_limit_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The normalised sum of a large number of independent, identically distributed random variables with finite mean and variance converges in distribution to a Gaussian (normal) distribution, regardless of the original distribution's shape (Laplace, 1812; Lyapunov, 1901; Lindeberg, 1922). The Gaussian is the universal attractor for sums of weakly-correlated random variables. This explains the ubiquity of bell curves in nature."),
        ("Mathematical Form", 1,
         "Z_n = (X̄_n − μ) / (σ/√n)  →  N(0,1)  as n → ∞\n\nwhere X̄_n = (1/n)Σ X_i,  μ = E[X_i],  σ² = Var(X_i) < ∞\n\nConvergence rate: |F_n(x) − Φ(x)| ≤ C · ρ / (σ³√n)  (Berry-Esseen bound, ρ = E[|X|³])"),
        ("Constraint Category", 2,
         "Dynamical (Di): the CLT describes convergence in distribution — a dynamical limit of the empirical distribution. The Gaussian N(0,1) is a fixed point of the normalisation-and-convolution operation: convolution of two Gaussians is Gaussian. This fixed-point property makes the Gaussian the attractor of the renormalisation group for sums of random variables."),
        ("DS Cross-References", 3,
         "C3 (Heavy-Tailed Distributions — the CLT breaks down when variance is infinite; Lévy-stable distributions are the attractors for heavy-tailed summands, generalising the Gaussian). BIO3 (Fisher's Fundamental Theorem — CLT underlies the Gaussian approximation to the distribution of additive genetic effects). INFO1 (Shannon Entropy — the Gaussian maximises entropy for fixed mean and variance; the CLT is why maximum-entropy distributions arise so naturally). TD7 (Boltzmann Equation — the Maxwell-Boltzmann velocity distribution is a CLT consequence for molecular velocities)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: statistical-distribution\n\nThe Gaussian N(μ, σ²) is the universal attractor under the CLT renormalisation flow: rescaled sums converge to N(0,1) as a fixed point. This is the probabilistic analog of a phase transition — many microscopic distributions flow to the same macroscopic form. The CLT identifies the universality class (finite variance) for which the Gaussian is the basin of attraction."),
        ("What The Math Says", 5,
         "Take n independent draws from any distribution with mean mu and finite variance sigma-squared. The sample mean X-bar-n converges in probability to mu (law of large numbers). The standardised deviation Z-n equals the difference between X-bar-n and mu, divided by sigma over root-n. As n grows, the distribution of Z-n converges to the standard normal N(0,1). The Berry-Esseen theorem quantifies the convergence rate: the maximum error in the CDF is bounded by C times the third absolute moment divided by sigma-cubed times root-n. For heavy-tailed distributions where the variance is infinite, the CLT fails and the attractor is instead a Lévy-stable distribution with a power-law tail."),
        ("Concept Tags", 6,
         "• central limit theorem\n• Gaussian distribution\n• normal distribution\n• convergence in distribution\n• sum of random variables\n• Berry-Esseen bound\n• renormalisation group\n• universality class\n• Lindeberg condition\n• additive noise"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "central limit theorem, Gaussian distribution, normal distribution, convergence in distribution, sum of random variables, Berry-Esseen bound, renormalisation group, universality class, Lindeberg condition, additive noise", 0),
        ("DS Facets", "mathematical_archetype", "statistical-distribution", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("tensions with", "MATH2", "Central Limit Theorem", "C3", "C3: Heavy-Tailed Distributions (Unified)", "The CLT requires finite variance; C3's heavy-tailed (Lévy-stable) distributions lie outside the CLT basin — they are the attractor for infinite-variance summands, the regime where CLT fails."),
        ("implements", "MATH2", "Central Limit Theorem", "INFO1", "Shannon Entropy", "The Gaussian maximises Shannon entropy subject to fixed mean and variance; the CLT shows why maximum-entropy distributions emerge naturally from sums of random variables."),
        ("couples to", "MATH2", "Central Limit Theorem", "STAT2", "Ergodic Theorem", "The ergodic theorem is the dynamical version of the LLN; the CLT provides the fluctuation corrections — both describe convergence of time/ensemble averages."),
    ],
},

{
    "id": "MATH3",
    "title": "Law of Large Numbers",
    "filename": "MATH3_law_of_large_numbers.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The sample mean of n independent, identically distributed random variables with finite expectation μ converges to μ as n → ∞. Weak LLN (Bernoulli, 1713; Chebyshev, 1867): convergence in probability. Strong LLN (Kolmogorov, 1930): almost sure convergence. The LLN justifies the frequentist interpretation of probability as the long-run relative frequency of an event."),
        ("Mathematical Form", 1,
         "Weak LLN:  X̄_n →^P μ  (for any ε > 0: P(|X̄_n − μ| > ε) → 0 as n → ∞)\nStrong LLN: X̄_n →^{a.s.} μ  (P(lim_{n→∞} X̄_n = μ) = 1)\nCondition: E[|X|] < ∞  (Kolmogorov's condition for strong LLN)"),
        ("Constraint Category", 2,
         "Informatic/Coordination (In): the LLN establishes that probability is not merely a formal construct but a quantity empirically measurable as limiting frequency. It coordinates the formal (axiomatic) and empirical (frequentist) interpretations of probability. The strong form makes a statement about individual realisations; the weak form about the distribution of sample means."),
        ("DS Cross-References", 3,
         "MATH2 (Central Limit Theorem — the CLT is the quantitative refinement of the LLN: the LLN gives the limit, the CLT gives the fluctuations around it). STAT2 (Ergodic Theorem — ergodicity is the dynamical extension of the LLN: time averages converge to ensemble averages). BIO8 (Neutral Theory — the molecular clock rate k = μ_n is established via LLN: observed substitution frequencies converge to the neutral rate). MATH1 (Bayes' Theorem — Bayesian posterior concentrates on true parameter via LLN for likelihoods)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe LLN is a conservation law for probability: the long-run frequency is conserved at the true probability value regardless of the finite-sample fluctuations. The strong LLN states that with probability one, the sample path eventually stays within any ε-tube around μ — an almost-sure conservation of the mean."),
        ("What The Math Says", 5,
         "Let X-1, X-2, ... be independent and identically distributed with mean mu. The sample mean X-bar-n equals the sum divided by n. The weak law states that for any small positive epsilon, the probability that X-bar-n differs from mu by more than epsilon goes to zero as n goes to infinity. The strong law strengthens this: the probability that X-bar-n converges exactly to mu as n goes to infinity is one — almost every sequence of outcomes has a sample mean converging to the true mean. The key condition is that the expected absolute value of X must be finite. When this fails (infinite mean, as in some heavy-tailed distributions), the LLN breaks down and there is no stable long-run average."),
        ("Concept Tags", 6,
         "• law of large numbers\n• sample mean convergence\n• frequentist probability\n• almost sure convergence\n• Kolmogorov\n• Bernoulli\n• strong LLN\n• weak LLN\n• empirical frequency\n• finite expectation"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "law of large numbers, sample mean convergence, frequentist probability, almost sure convergence, Kolmogorov, Bernoulli, strong LLN, weak LLN, empirical frequency, finite expectation", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "MATH3", "Law of Large Numbers", "MATH2", "Central Limit Theorem", "The LLN gives the limiting value; the CLT gives the rate of convergence and the fluctuation distribution. The CLT is the quantitative completion of the LLN."),
        ("implements", "MATH3", "Law of Large Numbers", "STAT2", "Ergodic Theorem", "The ergodic theorem is the dynamical generalisation of the LLN: for ergodic systems, time averages along a single trajectory converge to the ensemble mean, extending LLN to dependent sequences."),
        ("couples to", "MATH3", "Law of Large Numbers", "BIO8", "Neutral Theory of Molecular Evolution", "The molecular clock rate k = μ_n is empirically established via LLN: the observed substitution frequency in long sequences converges to the true neutral mutation rate."),
    ],
},

{
    "id": "MATH4",
    "title": "Gödel's Incompleteness Theorems",
    "filename": "MATH4_godel_incompleteness.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "First theorem: Any consistent formal system F capable of expressing elementary arithmetic contains statements that are true but unprovable within F (Gödel, 1931). Second theorem: Such a system F cannot prove its own consistency. These theorems establish an absolute ceiling on formal knowledge: no finite set of axioms can capture all mathematical truth, and no sufficiently powerful system can bootstrap its own validation. The proofs use diagonalisation — a self-referential construction that encodes 'this statement is unprovable'."),
        ("Mathematical Form", 1,
         "Gödel sentence G_F: 'This statement is not provable in F'\nIf F is consistent: F ⊬ G_F  and  F ⊬ ¬G_F  (G_F is undecidable in F)\nIf F is ω-consistent: F ⊬ ¬G_F  (the negation is also unprovable)\nSecond theorem: Con(F) ⊬_F Con(F)  (F cannot prove its own consistency)"),
        ("Constraint Category", 2,
         "Informatic (In): the incompleteness theorems are information-theoretic limits on formal systems. Chaitin's formulation makes this explicit: no formal system of complexity K can prove that a string has Kolmogorov complexity greater than K. The theorems establish that mathematical truth is not fully capturable by any finite description — there is always a gap between provable and true."),
        ("DS Cross-References", 3,
         "INFO5 (Kolmogorov Complexity — Chaitin's incompleteness theorem states that no formal system of complexity K can prove K(x) > K for any x; this is the algorithmic information version of Gödel). B5 (Landauer's Principle — both establish physical/logical floors: Landauer gives the thermodynamic cost of logical operations; Gödel gives the logical limit of formal deduction). MATH3 (Law of Large Numbers — both have impossibility/limit character: LLN constrains what frequencies can do, Gödel constrains what proofs can do)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe incompleteness is a conserved limit: no extension of F by finitely many new axioms eliminates the incompleteness — G_{F'} is a new undecidable statement in the extended system F'. The gap between provable and true is invariant under any finite axiomatic extension. This is the logical analog of a conservation law: the incompleteness cannot be removed, only deferred."),
        ("What The Math Says", 5,
         "Gödel constructed a sentence G-F in the language of arithmetic that, when interpreted, says 'I am not provable in F'. If F is consistent and can express basic arithmetic, then G-F is true (since if it were false, F would prove a falsehood) but not provable in F. Adding G-F as a new axiom gives a stronger system F-prime, but F-prime has its own Gödel sentence G-F-prime that is unprovable in F-prime. The process never terminates: formal systems cannot catch their own truth. The proof uses Gödel numbering — encoding formulas as integers — and the diagonal lemma to construct self-referential statements. The second theorem follows: a system strong enough to prove its own consistency would be strong enough to prove G-F, contradicting the first theorem."),
        ("Concept Tags", 6,
         "• Gödel incompleteness\n• undecidable statement\n• formal system limits\n• self-reference\n• diagonalisation\n• consistency unprovable\n• arithmetic truth\n• Gödel numbering\n• Chaitin incompleteness\n• axiomatic limits"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Gödel incompleteness, undecidable statement, formal system limits, self-reference, diagonalisation, consistency unprovable, arithmetic truth, Gödel numbering, Chaitin incompleteness, axiomatic limits", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "MATH4", "Gödel's Incompleteness Theorems", "INFO5", "Kolmogorov Complexity", "Chaitin's incompleteness — no system of complexity K can prove K(x) > K — is the algorithmic information reformulation of Gödel, connecting incompleteness directly to information content."),
        ("couples to", "MATH4", "Gödel's Incompleteness Theorems", "B5", "B5: Landauer's Principle", "Both establish fundamental physical/logical limits: Landauer gives the minimum thermodynamic cost of irreversible computation; Gödel gives the logical limit of what finite formal systems can prove."),
        ("analogous to", "MATH4", "Gödel's Incompleteness Theorems", "QM2", "Heisenberg Uncertainty Principle", "Both are irreducible limits arising from self-referential structure: Heisenberg's uncertainty arises from the measurement disturbing the system; Gödel's undecidability arises from the system encoding statements about itself."),
    ],
},

{
    "id": "MATH5",
    "title": "Fundamental Theorem of Calculus",
    "filename": "MATH5_fundamental_theorem_calculus.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Differentiation and integration are inverse operations (Newton, Leibniz, 17th century). Part 1: if f is continuous on [a,b], then F(x) = ∫_a^x f(t)dt is differentiable and F'(x) = f(x). Part 2: ∫_a^b f(x)dx = F(b) − F(a) for any antiderivative F of f. This theorem unifies two apparently distinct operations — instantaneous rate of change and accumulated area — as a single duality, founding all of analysis."),
        ("Mathematical Form", 1,
         "Part 1: d/dx ∫_a^x f(t) dt = f(x)  (derivative of integral recovers integrand)\nPart 2: ∫_a^b f'(x) dx = f(b) − f(a)  (integral of derivative is net change)\nGeneralisation (Stokes): ∫_∂Ω ω = ∫_Ω dω  (FTC is the 1D case of Stokes' theorem)"),
        ("Constraint Category", 2,
         "Geometric (Ge): integration measures accumulated area (a geometric quantity); differentiation measures local slope (a geometric tangent). The FTC states these are inverses: local geometry (tangent) and global geometry (area) are dual. This duality is extended to all dimensions by the Generalized Stokes' Theorem."),
        ("DS Cross-References", 3,
         "AM1 (Principle of Least Action — the action S = ∫L dt uses the FTC to convert the variational condition δS = 0 into the Euler-Lagrange differential equations). AM2 (Euler-Lagrange — the E-L equations are obtained by differentiating the action integral; FTC is implicit). MATH8 (Stokes' Theorem — the FTC is the 1D special case of the Generalized Stokes' Theorem on manifolds). TD2 (First Law of Thermodynamics — dU = δQ − δW integrates to ΔU = Q − W via FTC; thermodynamic work is defined by integration)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: symmetry-conservation\n\nThe FTC expresses a deep symmetry: the operations of differentiation (local, instantaneous) and integration (global, cumulative) are exact inverses of each other. This symmetry is a conservation law in the space of functions: the information content of a function is conserved under the differential-integral round trip. The FTC is the reason differential equations and integral equations are two sides of the same coin."),
        ("What The Math Says", 5,
         "Part 1 says that if you accumulate a continuous function f from a to x and then differentiate with respect to x, you get f back — the derivative of the area function is the original function. Part 2 says that to integrate f from a to b, it suffices to find any antiderivative F of f and evaluate it at the endpoints: the integral equals F(b) minus F(a). Together these mean: integration and differentiation are inverse operations, up to a constant. The practical power is enormous — computing integrals by finding antiderivatives is vastly simpler than computing limits of Riemann sums. The Generalized Stokes theorem ∫ over the boundary of omega of omega equals ∫ over omega of d-omega extends this to differential forms on manifolds in arbitrary dimensions."),
        ("Concept Tags", 6,
         "• fundamental theorem of calculus\n• differentiation integration duality\n• antiderivative\n• Riemann integral\n• Newton Leibniz\n• area under curve\n• net change theorem\n• differential forms\n• analysis foundation\n• inverse operations"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "fundamental theorem of calculus, differentiation integration duality, antiderivative, Riemann integral, Newton Leibniz, area under curve, net change theorem, differential forms, analysis foundation, inverse operations", 0),
        ("DS Facets", "mathematical_archetype", "symmetry-conservation", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "MATH5", "Fundamental Theorem of Calculus", "AM1", "Principle of Least Action", "The action S = ∫L dt is defined by integration; varying S and applying the FTC converts the integral condition δS = 0 into the differential Euler-Lagrange equations."),
        ("derives from", "MATH5", "Fundamental Theorem of Calculus", "MATH8", "Generalized Stokes' Theorem", "The FTC is the one-dimensional special case of the Generalized Stokes' Theorem: ∫_a^b f'dx = f(b)−f(a) is ∫_∂[a,b] f = ∫_[a,b] df."),
        ("couples to", "MATH5", "Fundamental Theorem of Calculus", "TD2", "First Law of Thermodynamics", "The First Law ΔU = Q − W is obtained by integrating the differential form dU = δQ − δW; the FTC connects the infinitesimal and macroscopic statements of energy conservation."),
    ],
},

{
    "id": "MATH6",
    "title": "Prime Number Theorem",
    "filename": "MATH6_prime_number_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The number of prime numbers up to x, denoted π(x), is asymptotically equal to x/ln(x) as x → ∞ (proved independently by Hadamard and de la Vallée Poussin, 1896). Equivalently, the n-th prime p_n ~ n·ln(n) and the average gap between primes near x is ~ ln(x). The primes, despite their apparent irregularity, obey a precise statistical law at large scales. The Riemann Hypothesis (if true) gives sharp error bounds: |π(x) − Li(x)| = O(√x · ln x)."),
        ("Mathematical Form", 1,
         "π(x) ~ x / ln(x)  as x → ∞\nEquivalently: π(x) ~ Li(x) = ∫_2^x dt/ln(t)  (logarithmic integral, sharper)\np_n ~ n · ln(n)  (n-th prime)\nPrime gap near x: ~ ln(x)  (average gap between consecutive primes)"),
        ("Constraint Category", 2,
         "Geometric (Ge): the PNT is a statement about the density of primes in the number line — a one-dimensional geometric distribution problem. The proof uses complex analysis (the Riemann zeta function ζ(s) has no zeros on the line Re(s) = 1), connecting number theory to the geometry of the complex plane."),
        ("DS Cross-References", 3,
         "C3 (Heavy-Tailed Distributions — prime gaps have a nearly-exponential distribution at small scales but long tails; the gap distribution is a form of memoryless spacing). INFO5 (Kolmogorov Complexity — primes have high algorithmic information content: there is no known short program that generates all primes faster than trial division; the PNT is the best macroscopic description). MATH7 (Euler's Identity — the Euler product ζ(s) = Π(1−p^{-s})^{-1} connects the Riemann zeta function (key to PNT proof) to the complex exponential geometry of Euler's formula)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: logarithmic-growth\n\nThe number of primes up to x grows as x/ln(x) — slower than linear but faster than any fixed power of x. The logarithmic density of primes at x is 1/ln(x): a randomly chosen integer near x is prime with probability ~1/ln(x). This is logarithmic attenuation of density with scale, the hallmark of logarithmic growth."),
        ("What The Math Says", 5,
         "The prime counting function pi(x) counts the number of primes less than or equal to x. The PNT states that pi(x) divided by x over ln(x) approaches 1 as x grows without bound. More precisely, pi(x) is well approximated by the logarithmic integral Li(x) = integral from 2 to x of 1 over ln(t) dt. The average gap between consecutive primes near x is approximately ln(x): near x = 10 to the 6, gaps average about 14; near x = 10 to the 12, gaps average about 28. The proof by Hadamard and de la Vallée Poussin uses the fact that the Riemann zeta function has no zeros on the vertical line where the real part of s equals 1. The Riemann Hypothesis would sharpen the error: the deviation of pi(x) from Li(x) is at most of order root-x times ln(x)."),
        ("Concept Tags", 6,
         "• prime number theorem\n• prime counting function\n• logarithmic integral\n• Riemann hypothesis\n• prime density\n• prime gaps\n• Hadamard\n• Riemann zeta function\n• analytic number theory\n• asymptotic distribution"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "prime number theorem, prime counting function, logarithmic integral, Riemann hypothesis, prime density, prime gaps, Hadamard, Riemann zeta function, analytic number theory, asymptotic distribution", 0),
        ("DS Facets", "mathematical_archetype", "logarithmic-growth", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "MATH6", "Prime Number Theorem", "C3", "C3: Heavy-Tailed Distributions (Unified)", "Both describe macroscopic regularity emerging from seemingly irregular microscopic patterns: C3 for network degree distributions, PNT for prime distributions on the number line."),
        ("couples to", "MATH6", "Prime Number Theorem", "MATH7", "Euler's Identity", "The Euler product formula ζ(s) = Π(1−p^{-s})^{-1} connects all primes to the Riemann zeta function, whose zeros (via Euler's complex exponential geometry) control the error term in the PNT."),
        ("couples to", "MATH6", "Prime Number Theorem", "INFO5", "Kolmogorov Complexity", "The PNT gives the best known macroscopic description of prime distribution; Kolmogorov complexity characterises the irreducible information content of the prime sequence — no known short program captures all prime structure."),
    ],
},

{
    "id": "MATH7",
    "title": "Euler's Identity and Formula",
    "filename": "MATH7_euler_identity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Euler's formula: e^{iθ} = cos θ + i sin θ for all real θ. This connects the complex exponential to circular motion in the plane. The special case θ = π gives Euler's identity: e^{iπ} + 1 = 0, relating the five most fundamental constants of mathematics (e, i, π, 1, 0). Euler's formula is not merely a curiosity — it is the foundation of Fourier analysis, wave mechanics, quantum theory, signal processing, and all of complex analysis."),
        ("Mathematical Form", 1,
         "e^{iθ} = cos θ + i sin θ  (Euler's formula)\ne^{iπ} + 1 = 0  (Euler's identity, θ = π)\ne^{i2π} = 1  (unit circle: period 2π)\nFourier: f(t) = Σ_n c_n e^{inωt}  (decomposition into complex exponentials)\nQuantum: ψ(x,t) = A · e^{i(kx − ωt)}  (plane wave = complex exponential)"),
        ("Constraint Category", 2,
         "Geometric (Ge): e^{iθ} describes rotation by angle θ in the complex plane — it is the unit circle parameterised by arc length. The formula unifies exponential growth (real axis) and circular motion (imaginary axis) into a single geometric object: the complex exponential maps the real line to the unit circle. Multiplication by e^{iθ} is a rotation operator."),
        ("DS Cross-References", 3,
         "QM1 (Schrödinger Equation — quantum wavefunctions are complex exponentials e^{i(kx−ωt)}; the Schrödinger equation is the wave equation in complex exponential form). OP1 (Fermat's Principle — wave optics uses the complex exponential to represent phase; interference and diffraction are phase differences in e^{iφ}). AM1 (Least Action — path integrals weight each path by e^{iS/ℏ}; quantum mechanics is the complex-exponential generalisation of least action). MATH8 (Stokes' Theorem — complex analysis uses differential forms; the residue theorem is an application of Stokes' theorem using complex exponential geometry)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: symmetry-conservation\n\nEuler's formula reveals a deep symmetry: e^{iθ} has unit modulus for all real θ — rotation in the complex plane is an isometry (distance-preserving). The group of rotations U(1) = {e^{iθ} : θ ∈ ℝ} is the simplest continuous symmetry group. Noether's theorem (AM5) links this U(1) symmetry to conservation of a quantity — in electromagnetism, U(1) gauge symmetry is the source of charge conservation."),
        ("What The Math Says", 5,
         "Euler's formula states that e raised to the power i-theta equals cosine theta plus i times sine theta for any real angle theta. This is proved by comparing the Taylor series of e-to-the-i-theta with the Taylor series of cosine and sine: the even terms give cosine and the odd terms (multiplied by i) give sine. Setting theta equal to pi gives Euler's identity: e to the i-pi equals minus 1, so e to the i-pi plus 1 equals 0. The formula means that multiplication by e-to-the-i-theta rotates any complex number by angle theta — it is a rotation operator. In Fourier analysis, any periodic function decomposes into a sum of complex exponentials e to the i-n-omega-t, each representing a pure frequency component. In quantum mechanics, the free-particle wavefunction is e to the i(kx minus omega-t), a complex exponential propagating in space and time."),
        ("Concept Tags", 6,
         "• Euler's formula\n• Euler's identity\n• complex exponential\n• unit circle\n• rotation operator\n• Fourier analysis\n• wave mechanics\n• U(1) symmetry\n• complex plane\n• phase"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Euler's formula, Euler's identity, complex exponential, unit circle, rotation operator, Fourier analysis, wave mechanics, U(1) symmetry, complex plane, phase", 0),
        ("DS Facets", "mathematical_archetype", "symmetry-conservation", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "MATH7", "Euler's Identity and Formula", "QM1", "Schrödinger Equation", "Quantum wavefunctions are complex exponentials e^{i(kx−ωt)}; the Schrödinger equation is precisely the wave equation expressed in Euler's complex exponential language."),
        ("implements", "MATH7", "Euler's Identity and Formula", "AM1", "Principle of Least Action", "The Feynman path integral weights each classical path by e^{iS/ℏ}, where S is the action; quantum mechanics is the complex-exponential extension of classical least action via Euler's formula."),
        ("derives from", "MATH7", "Euler's Identity and Formula", "AM5", "Noether's Theorem", "The U(1) rotation symmetry e^{iθ} is the gauge group of electromagnetism; Noether's theorem applied to this U(1) symmetry yields conservation of electric charge."),
    ],
},

{
    "id": "MATH8",
    "title": "Generalized Stokes' Theorem",
    "filename": "MATH8_stokes_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The integral of a differential form ω over the boundary ∂Ω of an oriented manifold Ω equals the integral of its exterior derivative dω over Ω itself (Cartan, early 20th century). This single theorem subsumes four classical theorems: the Fundamental Theorem of Calculus (1D), Green's theorem (2D), the classical Stokes' theorem (surface in 3D), and the Divergence theorem (3D volume). It unifies all of vector calculus into a single statement about differential forms."),
        ("Mathematical Form", 1,
         "∫_∂Ω ω = ∫_Ω dω\n\nSpecial cases:\n  FTC:       ∫_a^b f'(x)dx = f(b) − f(a)\n  Green:     ∮_C (P dx + Q dy) = ∬_D (∂Q/∂x − ∂P/∂y) dA\n  Stokes:    ∮_∂S F·dr = ∬_S (∇×F)·dS\n  Divergence: ∯_∂V F·dS = ∭_V (∇·F) dV"),
        ("Constraint Category", 2,
         "Geometric (Ge): the theorem is a statement about the topology and geometry of manifolds. The key geometric insight is that the boundary of a boundary is empty (∂∂Ω = ∅), which implies that exact forms (dω for some ω) integrate to zero over closed manifolds. This topological fact underlies all conservation laws in physics expressed as differential equations."),
        ("DS Cross-References", 3,
         "EM1 (Gauss's Law for Electricity — the integral form ∯E·dS = Q/ε₀ is the Divergence theorem applied to the electric field; Stokes' theorem connects differential and integral forms of Maxwell's equations). EM3 (Faraday's Law — ∮E·dr = −dΦ_B/dt is the Stokes' theorem applied to the electric field curl). AM5 (Noether's Theorem — conservation laws in physics arise from symmetries; Stokes' theorem provides the geometric framework connecting local symmetry (dω = 0) to global conservation (∫ω = 0)). MATH5 (FTC — the 1D special case; Stokes' theorem is the n-dimensional generalisation)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe Generalized Stokes' Theorem is the mathematical foundation of all conservation laws in physics: a quantity is conserved if and only if its associated differential form is closed (dω = 0). Gauss's law, Faraday's law, and charge conservation are all instances. The deep statement is topological: what happens on the boundary is completely determined by what happens in the interior, and vice versa."),
        ("What The Math Says", 5,
         "The Generalized Stokes' Theorem states that integrating a differential form omega over the boundary of a region equals integrating its exterior derivative d-omega over the region itself. A differential form is a geometrically-covariant object that can be integrated over manifolds of appropriate dimension. The exterior derivative d generalises all classical derivative operators: gradient, curl, and divergence are all special cases of d acting on 0-forms, 1-forms, and 2-forms respectively. The fundamental topological fact is that d-squared equals zero (d composed with d is always zero) — this implies that the boundary of a boundary is empty, and any exact form (d of something) integrates to zero over a closed manifold. All four classical theorems (FTC, Green, Stokes, Divergence) are obtained by choosing the appropriate dimension and form type."),
        ("Concept Tags", 6,
         "• Stokes theorem\n• differential forms\n• exterior derivative\n• manifold boundary\n• vector calculus unification\n• Gauss divergence theorem\n• Green theorem\n• de Rham cohomology\n• conservation laws geometry\n• Cartan"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Stokes theorem, differential forms, exterior derivative, manifold boundary, vector calculus unification, Gauss divergence theorem, Green theorem, de Rham cohomology, conservation laws geometry, Cartan", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "MATH8", "Generalized Stokes' Theorem", "EM1", "Gauss's Law for Electricity", "Gauss's law in integral form is the Divergence theorem (a special case of Stokes'): the flux of E through a closed surface equals the enclosed charge divided by ε₀."),
        ("generalizes", "MATH8", "Generalized Stokes' Theorem", "EM3", "Faraday's Law of Induction", "Faraday's law ∮E·dr = −dΦ_B/dt is the classical Stokes' theorem applied to the electric field — one of the four special cases of the Generalized Stokes' Theorem."),
        ("implements", "MATH8", "Generalized Stokes' Theorem", "AM5", "Noether's Theorem", "Noether's theorem connects symmetries to conservation laws; the Generalized Stokes' Theorem provides the differential-geometric framework (closed forms, exact forms, de Rham cohomology) in which Noether's theorem operates."),
    ],
},

# ── INFORMATION THEORY ─────────────────────────────────────────────────────

{
    "id": "INFO1",
    "title": "Shannon Entropy",
    "filename": "INFO1_shannon_entropy.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The entropy H(X) of a discrete random variable X is the unique measure of average uncertainty (or average information content) consistent with three axioms: continuity, symmetry, and additivity for independent variables (Shannon, 1948). H(X) = −Σ p_i log p_i, where log is base 2 for bits. Entropy measures the average number of binary questions needed to determine X. It is the fundamental measure of information — the currency of all information-theoretic limits."),
        ("Mathematical Form", 1,
         "H(X) = −Σ_i p_i log₂ p_i  (bits; nats if natural log)\nMaximum: H = log₂ n  for uniform distribution (n outcomes)\nJoint entropy: H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)\nKL divergence: D_KL(P||Q) = Σ p_i log(p_i/q_i) ≥ 0  (relative entropy, not symmetric)"),
        ("Constraint Category", 2,
         "Informatic (In): Shannon entropy is the canonical measure of information. It is the unique function satisfying: (1) H is continuous in p_i, (2) uniform distribution maximises H, (3) H(X,Y) = H(X) + H(Y) for independent X,Y. Shannon proved these axioms force H = −c·Σ p_i log p_i for some constant c. The entropy is both an upper bound (maximum lossless compression) and a lower bound (minimum description length)."),
        ("DS Cross-References", 3,
         "B5 (Landauer's Principle — erasing one bit of information costs at least kT ln 2 joules; the entropy H in bits maps to thermodynamic entropy via Boltzmann constant). TD3 (Second Law — Boltzmann's entropy S = k ln W is the thermodynamic special case for uniform distributions; Shannon entropy is the generalisation to arbitrary probability distributions). Ax1 (Information Primacy — Shannon entropy operationalises the axiom that information is the fundamental quantity). M6 (Fisher Information — Fisher information is the second moment of the score function; both Shannon entropy and Fisher information quantify uncertainty but measure different aspects)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nShannon entropy is simultaneously an upper bound (maximum compression rate) and a lower bound (minimum description length) — a thermodynamic-style bound on information operations. The maximum entropy bound H ≤ log n is tight for uniform distributions. The KL divergence D_KL(P||Q) ≥ 0 is the entropy-based measure of the cost of using the wrong model Q when the true distribution is P."),
        ("What The Math Says", 5,
         "Shannon entropy H(X) equals the negative sum over all values i of p-i times log base 2 of p-i, measured in bits. It equals zero when the outcome is certain (one p-i equals 1) and reaches its maximum of log base 2 of n when all n outcomes are equally likely. Intuitively, H measures the average number of yes-or-no questions needed to determine the value of X when using an optimal strategy. The chain rule H(X,Y) equals H(X) plus H(Y given X) shows entropy is additive for conditional distributions. The KL divergence D-KL(P||Q) equals the sum of p-i times log of p-i over q-i and is always non-negative, equalling zero only when P equals Q — it measures the information cost of using the wrong distribution Q instead of the true P."),
        ("Concept Tags", 6,
         "• Shannon entropy\n• information content\n• uncertainty measure\n• bits per symbol\n• maximum entropy\n• KL divergence\n• joint entropy\n• conditional entropy\n• Shannon 1948\n• information theory"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Shannon entropy, information content, uncertainty measure, bits per symbol, maximum entropy, KL divergence, joint entropy, conditional entropy, Shannon 1948, information theory", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "INFO1", "Shannon Entropy", "Ax1", "Ax1: Information Primacy", "Shannon entropy operationalises Information Primacy: it is the canonical quantitative measure of the information content that Ax1 asserts is the fundamental substrate."),
        ("analogous to", "INFO1", "Shannon Entropy", "TD3", "Second Law of Thermodynamics", "Boltzmann's thermodynamic entropy S = k·ln W is the special case of Shannon entropy for uniform distributions; Shannon generalised thermodynamic entropy to arbitrary probability distributions."),
        ("couples to", "INFO1", "Shannon Entropy", "B5", "B5: Landauer's Principle", "Each bit of Shannon entropy erased has a minimum thermodynamic cost of kT ln 2 joules; Landauer's principle is the physical bridge between Shannon entropy (information) and Boltzmann entropy (thermodynamics)."),
    ],
},

{
    "id": "INFO2",
    "title": "Shannon Source Coding Theorem",
    "filename": "INFO2_source_coding_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Shannon's First Theorem (Source Coding Theorem, 1948): any data source with entropy H bits per symbol can be compressed to H bits per symbol on average, but cannot be compressed below H without loss. Lossless compression is possible at rate H, impossible at rate < H. This theorem establishes entropy as the fundamental limit of data compression: no matter how clever the algorithm, you cannot losslessly compress a source below its entropy rate."),
        ("Mathematical Form", 1,
         "For i.i.d. source with entropy H(X):\n  Lossless compression rate R ≥ H(X)  (bits per symbol)\n  Achievable: ∃ code with average length L → H(X)  (Huffman code achieves H ≤ L < H+1)\n  Typical set: P(|−(1/n)log p(x^n) − H| < ε) → 1  (asymptotic equipartition property)\n  Kolmogorov: K(x^n) ≈ n·H(X)  for typical sequences"),
        ("Constraint Category", 2,
         "Informatic (In): entropy H is the hard lower bound on lossless compression. The theorem proves both achievability (codes approaching H exist) and converse (no code can do better). The proof uses the Asymptotic Equipartition Property (AEP): typical sequences of length n occupy a set of size ≈ 2^{nH}, each with probability ≈ 2^{-nH}, enabling near-optimal encoding with nH bits."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — H(X) is the compression limit; the source coding theorem is the operational meaning of entropy). INFO3 (Noisy-Channel Coding — the two fundamental theorems: source coding gives the compression limit, channel coding gives the transmission limit). INFO5 (Kolmogorov Complexity — K(x) ≈ nH for typical sequences; Kolmogorov complexity is the individual-sequence analog of Shannon's ensemble rate). B5 (Landauer — the minimum energy to erase a compressed message is kT ln 2 per bit; source coding determines how many bits must be erased)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nEntropy H is the thermodynamic-style lower bound on lossless compression: it cannot be beaten regardless of the algorithm. The AEP shows that typical sequences cluster into a set of size 2^{nH}, making near-optimal compression achievable. Like a thermodynamic bound, the Shannon limit is: (1) universal (holds for all algorithms), (2) tight (achievable in the limit), and (3) expressed in terms of a state function (entropy) rather than the specific process."),
        ("What The Math Says", 5,
         "For a source generating symbols independently from a distribution with entropy H bits per symbol, the source coding theorem states: there exist codes with average codeword length approaching H bits per symbol arbitrarily closely as block length grows, but no lossless code can have average length less than H. The Huffman code achieves average length L satisfying H less than or equal to L less than H plus 1. The deeper proof uses the asymptotic equipartition property: for long sequences of length n, with high probability the sequence belongs to a typical set of size approximately 2 to the nH, each with roughly equal probability 2 to the minus nH. Assigning binary codewords to typical sequences requires nH bits — exactly the entropy times the length."),
        ("Concept Tags", 6,
         "• source coding theorem\n• data compression\n• entropy rate\n• lossless compression\n• Huffman code\n• asymptotic equipartition\n• typical set\n• Shannon first theorem\n• compression limit\n• information theory"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "source coding theorem, data compression, entropy rate, lossless compression, Huffman code, asymptotic equipartition, typical set, Shannon first theorem, compression limit, information theory", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "INFO2", "Shannon Source Coding Theorem", "INFO1", "Shannon Entropy", "The source coding theorem is the operational interpretation of Shannon entropy: H is not just a formula but the provable lower bound on any lossless compression algorithm."),
        ("couples to", "INFO2", "Shannon Source Coding Theorem", "INFO3", "Shannon Noisy-Channel Coding Theorem", "The two fundamental theorems of information theory: source coding (remove redundancy to compress) and channel coding (add structured redundancy to overcome noise). Together they define the architecture of all digital communication."),
        ("analogous to", "INFO2", "Shannon Source Coding Theorem", "TD3", "Second Law of Thermodynamics", "Both are one-way bounds: the second law says entropy cannot decrease spontaneously; the source coding theorem says compressed message length cannot fall below entropy. Both are irreversibility limits."),
    ],
},

{
    "id": "INFO3",
    "title": "Shannon Noisy-Channel Coding Theorem",
    "filename": "INFO3_channel_capacity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Every noisy communication channel has a channel capacity C (bits per channel use) such that: (1) for any rate R < C, there exist error-correcting codes that achieve arbitrarily small error probability; (2) for any rate R > C, the error probability cannot be made small (Shannon, 1948). The capacity is C = max_{p(x)} I(X;Y), where I(X;Y) is the mutual information between input X and output Y, maximised over all input distributions."),
        ("Mathematical Form", 1,
         "C = max_{p(x)} I(X;Y)  bits per channel use\nGaussian channel: C = (1/2) log₂(1 + SNR)  (Shannon-Hartley theorem, SNR = signal-to-noise ratio)\nBinary symmetric channel: C = 1 − H_b(p)  (H_b = binary entropy, p = crossover probability)\nCapacity-cost: R < C ⟺ reliable communication possible"),
        ("Constraint Category", 2,
         "Informatic/Thermodynamic (In/Th): channel capacity C is the fundamental upper bound on reliable information transmission rate. Like a thermodynamic bound, it cannot be exceeded regardless of coding strategy. The Shannon-Hartley form C = (1/2)log₂(1+SNR) shows capacity scales logarithmically with signal power — adding bandwidth linearly increases capacity while doubling power adds only log₂(2) = 1 bit per channel use."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — C = max I(X;Y) = max[H(Y) − H(Y|X)]; capacity is the maximum reduction in output entropy achievable by the input). INFO2 (Source Coding — source coding removes redundancy; channel coding adds structured redundancy; together they give the full compression-transmission architecture). INFO4 (Mutual Information — channel capacity is the maximum mutual information I(X;Y) over input distributions). QM2 (Heisenberg Uncertainty — quantum channels have an additional capacity bound from quantum uncertainty; the Holevo bound limits quantum channel capacity)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nChannel capacity C is a thermodynamic-style bound: universal, tight, and a property of the channel (not the code). The Shannon-Hartley form C = (½)log₂(1+SNR) has a deep analogy with thermodynamic entropy: capacity is logarithmic in the signal-to-noise ratio just as entropy is logarithmic in the number of states. The coding theorem is an existence proof — it shows codes achieving C exist without constructing them explicitly."),
        ("What The Math Says", 5,
         "A noisy channel takes input symbols from a set X and produces output symbols from a set Y with a conditional probability distribution P(Y|X). The mutual information I(X;Y) equals H(Y) minus H(Y given X) — the reduction in uncertainty about Y when X is known. Channel capacity C is the maximum of I(X;Y) over all possible input probability distributions p(X). For a Gaussian channel with signal-to-noise ratio SNR, Shannon-Hartley gives capacity C equal to one-half times log base 2 of 1 plus SNR bits per channel use. If you transmit at any rate R strictly less than C, there exist codes (possibly very long) that achieve error probability approaching zero. If R exceeds C, the error probability is bounded away from zero no matter how long the code — reliable communication is impossible above capacity."),
        ("Concept Tags", 6,
         "• channel capacity\n• noisy channel theorem\n• Shannon-Hartley theorem\n• mutual information\n• error-correcting codes\n• signal-to-noise ratio\n• reliable communication\n• Shannon second theorem\n• channel coding\n• information transmission"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "channel capacity, noisy channel theorem, Shannon-Hartley theorem, mutual information, error-correcting codes, signal-to-noise ratio, reliable communication, Shannon second theorem, channel coding, information transmission", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "INFO3", "Shannon Noisy-Channel Coding Theorem", "INFO1", "Shannon Entropy", "Channel capacity C = max I(X;Y) = max[H(Y) − H(Y|X)]; it is the maximum entropy reduction at the output achievable by choice of input distribution."),
        ("implements", "INFO3", "Shannon Noisy-Channel Coding Theorem", "INFO4", "Mutual Information and Data Processing Inequality", "Channel capacity is the maximum mutual information I(X;Y) — the operational meaning of mutual information as the rate of reliable information transmission."),
        ("analogous to", "INFO3", "Shannon Noisy-Channel Coding Theorem", "QM2", "Heisenberg Uncertainty Principle", "Both are fundamental bounds on information extraction: Heisenberg limits simultaneous knowledge of conjugate observables; Shannon limits reliable information transmission over noisy channels."),
    ],
},

{
    "id": "INFO4",
    "title": "Mutual Information and Data Processing Inequality",
    "filename": "INFO4_mutual_information_dpi.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Mutual information I(X;Y) measures the reduction in uncertainty about X given knowledge of Y (Shannon, 1948). The Data Processing Inequality (DPI) states: if X → Y → Z forms a Markov chain, then I(X;Z) ≤ I(X;Y). Processing data can never increase the information it contains about the source. This is the information-theoretic no-free-lunch theorem: you cannot extract more information about X from Z than was in Y about X."),
        ("Mathematical Form", 1,
         "I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) = H(X) + H(Y) − H(X,Y)\nI(X;Y) = D_KL(P(X,Y) || P(X)P(Y)) ≥ 0\nDPI: X → Y → Z ⟹ I(X;Z) ≤ I(X;Y) ≤ H(X)\nSufficiency: I(X;Z) = I(X;Y) iff Z is a sufficient statistic for X given Y"),
        ("Constraint Category", 2,
         "Informatic (In): the DPI is a conservation law for information — processing a signal cannot increase its information content about the source. This is deeply related to the Second Law of Thermodynamics: irreversible processing destroys information. The equality condition (sufficient statistic) identifies when no information is lost in the processing step."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — I(X;Y) = H(X) + H(Y) − H(X,Y); mutual information is the symmetric quantity derived from Shannon entropy). INFO3 (Channel Capacity — C = max I(X;Y); channel capacity is the maximum mutual information). BIO5 (Central Dogma — the DPI explains why reverse translation protein→DNA cannot occur: processing (translation) can only decrease mutual information between DNA and the environment, not increase it). B5 (Landauer — each step of irreversible processing has a thermodynamic cost proportional to the information lost: ΔI × kT ln 2)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe DPI is a conservation (actually a monotone decrease) law for mutual information through Markov chains: I(X;Z) ≤ I(X;Y) ≤ H(X). Information about the source can only be conserved (sufficient statistic) or lost (irreversible processing) — never gained. This parallels the Second Law: entropy never decreases; mutual information with the source never increases through processing."),
        ("What The Math Says", 5,
         "Mutual information I(X;Y) equals H(X) minus H(X given Y) — the reduction in uncertainty about X when Y is observed. It is symmetric: I(X;Y) equals I(Y;X). It can also be written as the KL divergence between the joint distribution P(X,Y) and the product of marginals P(X)P(Y), measuring how far X and Y are from being independent. The Data Processing Inequality states: in a Markov chain X to Y to Z, where Z is computed from Y without additional access to X, the mutual information between X and Z cannot exceed that between X and Y. Equality holds when Z is a sufficient statistic for X given Y — meaning Z preserves all information about X that was in Y. The DPI formalises why you cannot reverse-engineer more information about an input than was present in the intermediate representation."),
        ("Concept Tags", 6,
         "• mutual information\n• data processing inequality\n• Markov chain\n• sufficient statistic\n• information conservation\n• KL divergence\n• joint entropy\n• irreversible processing\n• information monotonicity\n• channel capacity"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "mutual information, data processing inequality, Markov chain, sufficient statistic, information conservation, KL divergence, joint entropy, irreversible processing, information monotonicity, channel capacity", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "INFO4", "Mutual Information and Data Processing Inequality", "INFO1", "Shannon Entropy", "Mutual information I(X;Y) = H(X) + H(Y) − H(X,Y) is the symmetric combination of Shannon entropies that measures dependence between two variables."),
        ("implements", "INFO4", "Mutual Information and Data Processing Inequality", "BIO5", "Central Dogma of Molecular Biology", "The DPI provides the information-theoretic proof that protein→DNA reverse translation is impossible: the translation step is lossy (many codons → one amino acid), so I(DNA;protein) < I(DNA;mRNA) — information lost by the degeneracy cannot be recovered."),
        ("analogous to", "INFO4", "Mutual Information and Data Processing Inequality", "TD3", "Second Law of Thermodynamics", "Both are irreversibility laws: the Second Law says thermodynamic entropy never decreases; the DPI says mutual information with the source never increases through Markov processing — they are the thermodynamic and informational faces of irreversibility."),
    ],
},

{
    "id": "INFO5",
    "title": "Kolmogorov Complexity",
    "filename": "INFO5_kolmogorov_complexity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Kolmogorov complexity K(x) of a string x is the length of the shortest program (on a universal Turing machine) that outputs x. K(x) is the algorithmic information content of x — the minimum description length. Most strings of length n have K(x) ≈ n (they are incompressible). K(x) is not computable (Kolmogorov, 1965; Solomonoff, 1964; Chaitin, 1966). This is the foundation of algorithmic information theory and the minimum description length (MDL) principle."),
        ("Mathematical Form", 1,
         "K(x) = min{|p| : U(p) = x}  (shortest program p on universal TM U outputting x)\nIncompressibility: P(K(x) ≥ n − c) ≥ 1 − 2^{-c}  (most strings are incompressible)\nKolmogorov–Chaitin: ∀c, {x : K(x) < |x| − c} is a small set\nRelation to Shannon: E[K(X)] ≈ H(X)  for typical ensembles (up to O(log n))\nUncomputable: K is not a total computable function"),
        ("Constraint Category", 2,
         "Informatic (In): K(x) is the irreducible information content of x — the length of the shortest complete description. It is uncomputable but upper-bounded by any particular description and lower-bounded by incompressibility arguments. The incomputability of K is related to Gödel incompleteness: no formal system of complexity K₀ can prove K(x) > K₀ for any specific x."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — E[K(X)] ≈ H(X) for typical ensembles; K is the individual-sequence analog of ensemble Shannon entropy). INFO2 (Source Coding — lossless compression to length K(x) is optimal for individual sequences; source coding achieves E[K(X)] ≈ H(X) on average). MATH4 (Gödel Incompleteness — Chaitin's incompleteness theorem is a Kolmogorov-complexity reformulation: no system of complexity K₀ can prove K(x) > K₀, directly linking algorithmic information to formal limits). B5 (Landauer — the minimum energy to erase the description of x is K(x) × kT ln 2 joules)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nKolmogorov complexity is conserved under computationally reversible transformations: K(f(x)) ≤ K(x) + K(f) + O(1) for any computable function f. Irreversible operations (like lossy compression) increase K relative to the original: the information lost cannot be recovered. This conservation mirrors the DPI: processing cannot increase algorithmic information content."),
        ("What The Math Says", 5,
         "The Kolmogorov complexity K(x) of a binary string x is the length in bits of the shortest computer program that outputs x and then halts, when run on a fixed universal Turing machine U. A string is considered random (or incompressible) if K(x) is approximately equal to the length of x — there is no shorter description. Most strings of length n have K(x) at least n minus a constant — incompressible strings are the vast majority. K(x) is not computable: there is no algorithm that takes x as input and outputs K(x), because the halting problem prevents systematic identification of the shortest program. However, K(x) is upper-computable: any specific compression algorithm gives an upper bound. For a random variable X drawn from distribution P, the expected value of K(X) equals H(X) plus terms of order log n — K and Shannon entropy agree for typical ensembles up to lower-order terms."),
        ("Concept Tags", 6,
         "• Kolmogorov complexity\n• algorithmic information theory\n• minimum description length\n• incompressibility\n• universal Turing machine\n• Solomonoff Kolmogorov Chaitin\n• random string\n• program length\n• uncomputable function\n• MDL principle"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Kolmogorov complexity, algorithmic information theory, minimum description length, incompressibility, universal Turing machine, Solomonoff Kolmogorov Chaitin, random string, program length, uncomputable function, MDL principle", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "INFO5", "Kolmogorov Complexity", "INFO1", "Shannon Entropy", "K(x) is the individual-sequence analog of Shannon entropy: E[K(X)] ≈ H(X) for typical ensembles; K measures irreducible information for a single string, H for a whole distribution."),
        ("couples to", "INFO5", "Kolmogorov Complexity", "MATH4", "Gödel's Incompleteness Theorems", "Chaitin's incompleteness theorem — no formal system of complexity K₀ can prove K(x) > K₀ for any specific x — reformulates Gödel incompleteness in terms of algorithmic information, directly connecting logical undecidability to information content."),
        ("implements", "INFO5", "Kolmogorov Complexity", "B5", "B5: Landauer's Principle", "The minimum energy to erase a description of x is K(x) × kT ln 2 joules — Kolmogorov complexity determines the thermodynamic cost of the most efficient erasure possible."),
    ],
},

# ── STATISTICS / PROBABILITY ───────────────────────────────────────────────

{
    "id": "STAT1",
    "title": "Maximum Entropy Principle",
    "filename": "STAT1_maximum_entropy.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Among all probability distributions consistent with known constraints, the one with maximum Shannon entropy is the least-biased choice — it incorporates exactly the available information without assuming anything beyond it (Jaynes, 1957). This is the principle of maximum ignorance: MaxEnt selects the distribution that makes the fewest unjustified assumptions. Jaynes showed this is the unique rational inference procedure consistent with the available information."),
        ("Mathematical Form", 1,
         "max H(p) = −Σ p_i log p_i\nsubject to: Σ p_i = 1  and  Σ p_i f_k(x_i) = ⟨f_k⟩  (constraint moments)\n\nSolution (exponential family): p_i = exp(−Σ_k λ_k f_k(x_i)) / Z\nwhere Z = Σ_i exp(−Σ_k λ_k f_k(x_i))  (partition function)\n\nExamples:\n  No constraints → uniform distribution\n  Fixed mean → exponential distribution\n  Fixed mean and variance → Gaussian distribution"),
        ("Constraint Category", 2,
         "Informatic (In): MaxEnt is an inference principle — a rule for constructing probability distributions from partial information. The exponential family (Gaussian, exponential, Boltzmann, Poisson) comprises precisely the maximum entropy distributions under their respective moment constraints. MaxEnt distributions are objectively correct in the sense that any other distribution either violates constraints or makes unjustified additional assumptions."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — MaxEnt maximises H; the entropy H is the objective function). TD3 (Second Law of Thermodynamics — the Boltzmann distribution e^{-E/kT}/Z is MaxEnt with fixed mean energy; statistical mechanics is MaxEnt applied to physical systems). AM1 (Principle of Least Action — both are variational extremal principles: least action extremises S over paths, MaxEnt extremises H over distributions). MATH1 (Bayes — MaxEnt provides the least-informative prior; Bayes provides the update rule when data arrives; together they form the complete Bayesian-MaxEnt inference framework)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nMaxEnt is an optimisation principle: maximise H subject to constraints. The solution is always an exponential family distribution: p_i ∝ exp(−Σ λ_k f_k(x_i)). The Lagrange multipliers λ_k are determined by the constraint equations. This variational structure makes MaxEnt the probabilistic analog of least action — both select the extremal element of a space of possibilities consistent with given constraints."),
        ("What The Math Says", 5,
         "To apply MaxEnt: list all constraints on the probability distribution (normalisation plus any known expected values). Maximise Shannon entropy H equals minus sum of p-i log p-i subject to these constraints using Lagrange multipliers. The solution always takes the exponential family form: p-i proportional to exp of minus the sum over k of lambda-k times f-k of x-i. The partition function Z is the normalising sum. The Lagrange multipliers lambda-k are determined by substituting the solution back into the constraint equations. For no constraints beyond normalisation, MaxEnt gives the uniform distribution — maximum ignorance. For a fixed mean mu, MaxEnt gives the exponential distribution with rate 1/mu. For fixed mean and variance, MaxEnt gives the Gaussian — this explains why the Gaussian is the default distribution when only mean and variance are known."),
        ("Concept Tags", 6,
         "• maximum entropy principle\n• MaxEnt\n• Jaynes\n• exponential family\n• least biased inference\n• partition function\n• Lagrange multipliers\n• Boltzmann distribution\n• prior distribution\n• variational inference"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "maximum entropy principle, MaxEnt, Jaynes, exponential family, least biased inference, partition function, Lagrange multipliers, Boltzmann distribution, prior distribution, variational inference", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "STAT1", "Maximum Entropy Principle", "INFO1", "Shannon Entropy", "MaxEnt maximises Shannon entropy H subject to constraints; entropy H is both the objective function and the measure of information content being maximised."),
        ("analogous to", "STAT1", "Maximum Entropy Principle", "AM1", "Principle of Least Action", "Both are variational extremal principles: least action selects the extremal path in configuration space; MaxEnt selects the extremal distribution in probability space. Both produce exponential-form solutions via Lagrange multipliers."),
        ("derives from", "STAT1", "Maximum Entropy Principle", "TD3", "Second Law of Thermodynamics", "The Boltzmann-Gibbs distribution e^{-E/kT}/Z is the MaxEnt solution with constraint of fixed mean energy — statistical mechanics is MaxEnt applied to physical systems, recovering the Second Law as the entropy-maximisation equilibrium condition."),
    ],
},

{
    "id": "STAT2",
    "title": "Ergodic Theorem",
    "filename": "STAT2_ergodic_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "For an ergodic measure-preserving dynamical system, the time average of any observable f along almost every trajectory equals the ensemble (space) average of f over the invariant measure (Birkhoff, 1931; von Neumann, 1932). A system is ergodic if the only invariant sets have measure zero or one — meaning the trajectory explores the entire phase space (up to measure zero). The ergodic theorem is the dynamical justification for replacing time averages with ensemble averages in statistical mechanics."),
        ("Mathematical Form", 1,
         "Birkhoff: (1/T) ∫_0^T f(T^t x) dt → ∫ f dμ  as T → ∞  (a.e., in L¹)\nVon Neumann: L² convergence of time averages to space averages\nErgodicity condition: T^{-1}(A) = A ⟹ μ(A) ∈ {0,1}  (only trivial invariant sets)\nEntropy: h(T) = lim_{n→∞} (1/n) H(x_0, x_1, ..., x_{n-1})  (Kolmogorov-Sinai entropy)"),
        ("Constraint Category", 2,
         "Dynamical (Di): ergodicity is a dynamical property — it describes how a trajectory samples phase space over time. The theorem bridges the microscopic (single trajectory) and macroscopic (ensemble) descriptions. Non-ergodic systems have invariant subsets: the trajectory is confined to one component, and time averages depend on initial conditions. Phase transitions often break ergodicity."),
        ("DS Cross-References", 3,
         "TD7 (Boltzmann Equation — Boltzmann's H-theorem implicitly assumes ergodicity: the phase space average equals the time average at equilibrium). MATH3 (Law of Large Numbers — the ergodic theorem is the dynamical extension of LLN: for ergodic systems, the time series X_1, X_2, ... satisfies LLN even when the X_t are not independent). INFO1 (Shannon Entropy — Kolmogorov-Sinai (KS) entropy h(T) is the entropy production rate of an ergodic dynamical system; it measures the rate of information generation). H3 (Phase Coherence — loss of ergodicity corresponds to confinement to a coherent subspace; H3 quantifies this confinement via the phase coherence parameter).'),"),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nIn an ergodic system, the time average is conserved at the space average: lim(1/T)∫f(T^t x)dt = ∫f dμ regardless of the starting point x (a.e.). This is a conservation statement: the long-run time average is the same for almost all initial conditions. Breaking ergodicity introduces a conserved quantity that separates phase space into invariant components."),
        ("What The Math Says", 5,
         "Birkhoff's ergodic theorem states that for a measure-preserving transformation T on a probability space, and any integrable function f, the time average (1/T) times the integral from 0 to T of f at T-to-the-t of x dt converges almost everywhere as T goes to infinity. The limit equals the space average, the integral of f with respect to the invariant measure mu, if and only if the system is ergodic. Ergodicity means the transformation T has no non-trivial invariant subsets: any set A such that T-inverse of A equals A must have measure zero or measure one. Intuitively, an ergodic trajectory visits every region of phase space with the correct frequency. Statistical mechanics uses this: measured time averages of macroscopic observables equal their thermal ensemble averages because molecular systems are ergodic (at least approximately, on experimental time scales)."),
        ("Concept Tags", 6,
         "• ergodic theorem\n• Birkhoff\n• time average\n• ensemble average\n• ergodicity\n• phase space\n• invariant measure\n• statistical mechanics foundation\n• Kolmogorov-Sinai entropy\n• dynamical systems"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "ergodic theorem, Birkhoff, time average, ensemble average, ergodicity, phase space, invariant measure, statistical mechanics foundation, Kolmogorov-Sinai entropy, dynamical systems", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "STAT2", "Ergodic Theorem", "TD7", "TD7: Boltzmann Equation", "The Boltzmann equation's approach to equilibrium requires ergodicity — that trajectories sample phase space uniformly. Boltzmann's H-theorem is the non-equilibrium precursor; the ergodic theorem justifies the equilibrium correspondence."),
        ("generalizes", "STAT2", "Ergodic Theorem", "MATH3", "Law of Large Numbers", "The LLN states that sample means of i.i.d. variables converge to the true mean; the ergodic theorem extends this to dependent time series from dynamical systems — the independence assumption is replaced by ergodicity."),
        ("couples to", "STAT2", "Ergodic Theorem", "H3", "H3: Phase Coherence (λ)", "Loss of ergodicity corresponds to confinement to a coherent phase space submanifold; the phase coherence parameter λ in H3 quantifies the degree of ergodicity breaking in the regime framework."),
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
    print(f"Inserting Chunk 2 ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)

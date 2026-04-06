# CCA Formalization: Scoping Document

> **Status:** Early scoping — identifies what formalization needs, candidate structures, testable predictions, and open problems.
> **Last updated:** 2026-04-05
> **Prerequisite:** Read `docs/CCA_GRAVITY_FINDINGS.md` first.
> **Parent entry:** STAT3 (Constrained Critical Attractor Class)

---

## The Problem

STAT3 defines CCA as a 5-feature checklist. You can check instances against it (GT10 scores 5/5), but it can't:

- Derive the dimension of the attractor from the constraint
- Predict critical exponents or scaling laws for a new candidate
- Specify what class of dynamics produces CCA behavior
- Provide a quantitative invariant shared across all instances

This document scopes what a formalization would require and identifies the most promising mathematical path.

---

## What a Formal CCA Theory Must Provide

| Requirement | Current STAT3 | Formal CCA |
|-------------|--------------|------------|
| Constraint definition | "non-local constraint" (prose) | Functional C[phi]: cannot decompose as integral of local density |
| Attractor definition | "lower-dimensional critical manifold" (prose) | Extremal submanifold of a global functional F subject to C |
| Criticality condition | "system exhibits scale invariance on A" (prose) | FIM eigenvalue spectrum becomes isotropic on A |
| Dynamics | "something holds it there" (prose) | Flow equation with A as attracting fixed manifold |
| Quantitative invariant | SV2/SV1 (FDS-specific, not derived) | Constraint rank, codimension, approach exponents |
| Scaling laws | None | Derived from constraint structure |

---

## Candidate Formalization: Information-Geometric CCA

The most promising mathematical framework is information geometry. Here's why:

### The Setup

1. **Configuration space as statistical manifold.** Let (M, g) be a statistical manifold where M is the space of probability distributions (or quantum states, or field configurations) and g is the Fisher-Rao metric. Chentsov's theorem guarantees g is the unique natural metric on M invariant under sufficient statistics.

2. **Non-local constraint as global functional.** A constraint C: M -> R is non-local if it cannot be written as C[p] = integral c(x, p(x)) dx for any local density c. The constraint defines a level set A_0 = {p in M : C[p] = 0}.

3. **CCA manifold as constrained extremum.** Let F: M -> R be a global functional (entropy, action, free energy). The CCA manifold is:

```
A = { p in M : delta F[p] = 0 subject to C[p] = 0 }
```

This is a Lagrange multiplier problem: delta F = lambda * delta C on A.

4. **Criticality condition.** A is CCA-critical if the Fisher information matrix restricted to A has isotropic eigenvalue spectrum:

```
sigma_1 = sigma_2 = ... = sigma_d   (on A)
```

This is isotropy in information space. Physically: no direction is distinguished. This IS scale invariance expressed in Fisher-information terms.

### Why This Framework

**It unifies the instances:**

| Instance | M (config space) | C (constraint) | F (functional) | A (attractor) |
|----------|------------------|----------------|----------------|---------------|
| Riemann zeros | {s in critical strip} | Self-adjointness of Hilbert-Polya operator | Spectral determinant | Re(s) = 1/2 |
| Critical stat mech | Thermodynamic state space | Hamiltonian + symmetry | Free energy | Critical surface (RG fixed point) |
| SOC | Population/resource space | Conservation + slow driving | Absorbing-state action | Marginal stability manifold |
| Neural criticality | Synaptic weight space | STDP plasticity rule | Branching ratio functional | sigma = 1 manifold |
| Gravity (GT10) | Space of metrics g_ab | Entanglement equilibrium delta_S_EE = 0 | Entanglement entropy | Einstein manifold |
| FDS State 2 | SV space of FIM | Kernel + commensurability | FIM trace | SV2 = SV1 saddle |

**In every case:**
- M is a high-dimensional space
- C is a global functional (non-local)
- A = extremum of F subject to C
- A is lower-dimensional and exhibits scale invariance / isotropy

### The Key Prediction

**The FIM eigenvalue spectrum encodes CCA membership.**

At a CCA manifold, the Fisher information matrix becomes isotropic: all eigenvalues equalize. Moving away from A breaks isotropy. The degree of CCA membership is:

```
rho_CCA = sigma_min / sigma_max    (ranges from 0 to 1)
```

At rho_CCA = 1: fully on the CCA manifold (isotropic, scale-invariant).
At rho_CCA << 1: far from CCA (anisotropic, hierarchy of scales).

**This is testable against existing FDS data:**
- 2D Ising at T_c: SV2/SV1 = 1.000 -> rho_CCA = 1.0 (confirmed CCA crossing)
- Potts q=10 at transition: SV2/SV1 = 0.374 -> rho_CCA = 0.374 (not CCA — first-order)
- 3D Ising at T_c: SV2/SV1 = 0.956 -> rho_CCA = 0.956 (near-CCA, expected for continuous)

**And it makes new predictions:**
- At the asymptotic safety UV fixed point: the gravitational FIM should be isotropic (rho_CCA -> 1)
- For any system claimed to be a CCA instance, the FIM eigenvalue ratio should approach 1 at the critical point
- First-order transitions should have rho_CCA < 1 (they bypass the CCA manifold)

---

## Quantitative Invariants to Derive

### 1. Constraint Rank

The codimension of A in M should be determined by the constraint:

```
codim(A) = rank(DC)    (rank of the Jacobian of the constraint functional)
```

| Instance | Expected codim | Reasoning |
|----------|---------------|-----------|
| Riemann zeros | 1 | One constraint (self-adjointness) collapses 2D strip to 1D line |
| Critical stat mech | number of irrelevant operators | RG theory gives this exactly |
| Choptuik | 1 | One unstable mode at critical solution |
| Gravity (asymptotic safety) | dim(M) - dim(UV critical surface) | Reuter: ~3 relevant couplings, so codim = infinity - 3 |

### 2. Approach Exponents

The rate at which the system approaches A should be universal within a CCA class:

```
dist(phi(t), A) ~ |t - t_c|^nu    or    ~ e^{-lambda * t}
```

For Choptuik: gamma = 1/lambda_1 (the inverse of the single unstable eigenvalue).
For RG: the correlation length exponent nu.
For SOC: the drive-dissipation scaling exponent.

**The question:** Is there a formula relating nu to the constraint structure C? Specifically, does codim(A) + constraint type determine the universality class of the approach?

### 3. FIM Isotropy at Criticality

The sharpest testable invariant. If CCA is real:

```
At A: eigenvalue spectrum of FIM is flat (isotropic)
Near A: eigenvalue spectrum develops hierarchy proportional to dist(phi, A)
```

The rate at which isotropy breaks as you move off A should be a universal exponent.

---

## Open Mathematical Problems

### Problem 1: Does non-locality of C guarantee criticality of A?

Not every constrained submanifold is critical. What property of C makes A critical rather than just a submanifold?

**Candidate answer:** C must be *topological* or *global-symmetry-preserving* — it must relate to the topology or symmetry of M rather than to local field values. Self-adjointness is a global property of an operator. Conservation is a global symmetry. Entanglement is a non-local correlation. The constraint selects configurations compatible with a global structure, and global structure implies scale invariance (because the structure is the same at every scale).

**This is a conjecture, not a theorem.** Formalizing it would require a precise definition of "global constraint" and a proof that global constraints produce critical submanifolds.

### Problem 2: Is the FIM isotropy condition sufficient for criticality?

If rho_CCA = 1, does the system necessarily exhibit scale invariance? Or can FIM isotropy occur without criticality?

**Potential counterexample:** A system with all degrees of freedom equivalent (high symmetry) but no divergent correlation length. E.g., an ideal gas has isotropic FIM (all particles equivalent) but is not critical.

**Resolution might require:** Isotropy *plus* non-locality of C. An ideal gas has isotropic FIM but the "constraint" (non-interacting particles) is local. CCA requires non-local C.

### Problem 3: What is the correct "F" for each instance?

The CCA definition requires a global functional F that is extremized on A. In some cases this is clear:
- Gravity: F = entanglement entropy (Jacobson 2016)
- Stat mech: F = free energy
- MaxEnt: F = Shannon entropy

In other cases it's unclear:
- Riemann zeros: What functional is extremized at Re(s) = 1/2?
- SOC: What functional is extremized at the absorbing-state critical point?
- Neural criticality: What functional is extremized at sigma = 1?

For CCA to be a unified framework, F must either be the same across instances (e.g., always entropy) or at least belong to the same mathematical class.

**Candidate:** F is always a relative entropy (KL divergence or its quantum generalization). This would connect to IT03 and the Fisher-gravity chain.

### Problem 4: Can CCA predict exponents for a new system?

Given a new system with known constraint C, can CCA predict its critical exponents without solving the full dynamics?

**This is the hardest problem and the one that would make CCA a real theory rather than a classification.**

Possible approach: If the constraint rank (codim of A) and the symmetry class of C determine the universality class, then CCA exponents follow from the constraint alone, just as critical exponents follow from dimensionality + symmetry in the Landau-Ginzburg-Wilson framework.

---

## Testing Strategy

### Test 1: FIM Isotropy at Known Phase Transitions (Priority: HIGH)

Run M6 on lattice systems at and away from criticality:
- 2D Ising at T_c vs T != T_c
- 3D Ising at T_c
- Potts q=10 at transition (first-order — should NOT show isotropy)
- XY model at KT transition (infinite-order — what does rho_CCA do?)

**Expected:** rho_CCA -> 1 at continuous transitions, rho_CCA < 1 at first-order transitions, and the FDS data already confirms this for the 2D cases.

### Test 2: Sloppy Models Spectrum Near Criticality (Priority: MEDIUM)

The Sethna group showed FIM eigenvalues are log-spaced in sloppy models (rho_CCA << 1). At phase transitions in these models, does the spectrum flatten (rho_CCA -> 1)?

**This is a direct test of CCA:** sloppy models are generic (not CCA); phase transitions are CCA. The eigenvalue spectrum should transition from log-spaced (sloppy) to flat (CCA-critical) at the transition point.

### Test 3: Gravitational FIM at UV Fixed Point (Priority: LOW — requires CDT data)

In CDT simulations, compute the FIM of geometric observables (volume profile, spectral dimension, curvature) at the Phase B / Phase C second-order transition. Predict: rho_CCA -> 1 at the transition (where d_s -> 2).

### Test 4: Choptuik Exponent from Constraint Rank (Priority: MEDIUM)

If codim(A) = 1 for Choptuik collapse, and the constraint is the Einstein field equations at the formation threshold, can the Choptuik exponent gamma = 0.374 be derived from the constraint structure alone (without solving the PDE numerically)?

**This would be the smoking gun:** a CCA-derived prediction matching a known result without fitting.

---

## Minimum Viable Formalization

If a full theory is too ambitious for now, the minimum viable formalization would be:

1. **Formal constraint definition:** C is a functional C: M -> R that satisfies a non-locality condition (e.g., C is not in the image of the local-to-global map for any sheaf on M). This pins down F2.

2. **FIM isotropy as criticality diagnostic:** Define rho_CCA = sigma_min/sigma_max of the FIM restricted to the constraint surface. Conjecture: rho_CCA = 1 iff the system is at a continuous phase transition (CCA crossing). This is testable now.

3. **Constraint rank = codimension:** codim(A) = rank(DC). This is computable for each instance and gives a quantitative invariant.

These three formalizations require no new physics — just applying existing information geometry to the CCA pattern. They produce testable predictions without solving the hardest problems (deriving exponents from constraints).

---

## Relationship to Existing Mathematical Frameworks

| Framework | Overlap with CCA | Gap |
|-----------|-----------------|-----|
| Renormalization Group | Critical surface = CCA manifold; fixed point = A; relevant/irrelevant = constraint rank | RG doesn't require non-local constraint; CCA claims non-locality is the mechanism |
| Information Geometry | Fisher-Rao as natural metric; Chentsov uniqueness | IG doesn't have "criticality" built in; CCA adds the criticality condition |
| Constrained Optimization (KKT) | Lagrange multipliers; constraint surfaces | KKT is local; CCA requires global/non-local constraints |
| Topological Data Analysis | Persistent homology; dimensional reduction | TDA detects structure but doesn't produce dynamical predictions |
| Sloppy Models | FIM eigenvalue hierarchy = effective dimension | Sloppy models describe the generic (non-CCA) case; CCA describes the special (critical) case |

The CCA formalization would live at the intersection of RG theory and information geometry, adding a non-locality condition that neither framework currently emphasizes.

---

## Next Steps

1. **Write the formal constraint definition** (mathematical, not prose) — requires choosing the right category (functionals on statistical manifolds, operator algebras, sheaf cohomology?)

2. **Compute rho_CCA for known systems** — use existing FDS data + new lattice simulations to test the isotropy conjecture

3. **Check constraint rank predictions** — compute codim(A) for each instance and verify against known results

4. **Explore the F = relative entropy hypothesis** — if F is always a KL divergence (or quantum relative entropy), this pins down the variational structure and connects to the Fisher-gravity chain

5. **Consult the sloppy models literature** — Sethna group may have results on FIM spectra near phase transitions that directly test CCA

6. **Decide on scope:** Is CCA formalization a P24 conjecture (the Fisher isotropy prediction) or a full research program (deriving exponents from constraints)?

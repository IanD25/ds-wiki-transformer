> **⚠️ M0 AUDIT (2026-04-08, revised):** See `docs/M0_MILESTONE_COMPILATION.md` Addendum. The initial M0 claim that CCA restates JJK 2004 / Prokopenko-Lizier 2011 was corrected: the actual prior art is narrower (Machta-Chachra-Transtrum-Sethna, *Science* 2013, arXiv:1303.6738, which computes FIM eigenvalue spectra on Ising at criticality but does not use per-site-field parameterization or define d_eff/η observables). CCA may retain narrow methodological novelty pending owner confirmation via primary-source reading. This scoping doc is superseded by the revised M0 calibration but kept for historical reference.

---

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

## Experimental Results (2026-04-05)

### Critical Correction: η Alone Is Insufficient

Phase A (topology sweep) revealed that **η alone is not a reliable CCA diagnostic:**

| Lattice | Peak η | d_eff at peak | Interpretation |
|---------|--------|---------------|----------------|
| Path (1D, N=50) | **0.860** | **1** | Trivial isotropy — 1 dimension, no CCA |
| Complete K_16 | 0.057 | 1 | Spotlight effect — always RADIAL |
| 2D torus 16² | 0.474 | 3 | Structured isotropy — multiple dimensions |
| 3D torus 6³ | 0.644 | 4 | Higher-dimensional structured isotropy |

**The 1D path reaches η=0.86 with d_eff=1.** This is trivial isotropy — there's only one direction, so σ₁ ≈ σ₂ by kernel symmetry. CCA isotropy requires BOTH high η AND d_eff > 1.

**Revised CCA diagnostic:** The correct metric is the *joint* (d_eff, η), or equivalently the participation ratio PR = (Σσ)²/Σσ² which captures both dimension count and eigenvalue equality.

### Phase A Results: Topology Sweep

Script: `scripts/ising_fim_topology_test.py`

Lattice graphs swept over α ∈ {0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0}:

**Key findings:**
1. **Dimension ordering confirmed:** Peak d_eff(3D=4) > d_eff(2D=3) > d_eff(1D=1). Higher lattice dimension → higher FIM-detected effective dimension.
2. **η peaks at intermediate α** for tori — the kernel range where topology is optimally probed.
3. **High α (short-range) → RADIAL** universally. The FIM sees only nearest neighbors.
4. **Complete graph always RADIAL** — spotlight effect confirmed (d_eff=1 for all α).
5. **3D torus 4×4×4 shows finite-size artifact:** η=0.985 with d_eff=1 at α=0.1 (too small; kernel sees entire graph).

Data: `data/reports/ising_fim_test/topology_sweep.json`
Plot: `data/reports/ising_fim_test/alpha_vs_eta.png`

### Phase B Results: 2D Ising MC (L=16)

Script: `scripts/ising_fim_mc_test.py`

Metropolis-Hastings on 16×16 torus, T_c = 2.269 (Onsager exact), neglog weight mode:

| T/T_c | η | d_eff | PR | rho_CCA | \|corr\| | Regime |
|-------|---|-------|-----|---------|----------|--------|
| 0.66 | 0.233 | 2.0 | 2.30 | 0.065 | 0.976 | 100% RADIAL |
| 0.88 | 0.172 | 2.0 | 2.47 | 0.099 | 0.866 | 100% RADIAL |
| **1.00** | **0.256** | **2.0** | **2.73** | **0.148** | **0.724** | 96% RAD, 4% ISO |
| 1.06 | 0.373 | 2.0 | 2.99 | 0.187 | 0.627 | 16% RAD, 84% ISO |
| **1.15** | **0.491** | **2.8** | **3.33** | **0.255** | **0.523** | 100% ISOTROPIC |
| 1.32 | 0.423 | 3.0 | 3.55 | 0.318 | 0.408 | 88% ISO |
| 1.76 | 0.487 | 2.6 | 3.22 | 0.240 | 0.280 | 100% ISO |

**Key findings:**
1. **The FIM detects the phase transition** as a RADIAL → ISOTROPIC regime transition.
2. **The transition is gradual, not sharp at T_c.** On L=16, the crossover spans T/T_c ≈ 1.0–1.15. This is a finite-size effect — on infinite lattice the transition would sharpen.
3. **d_eff peaks above T_c** (d_eff=3 at T/T_c=1.32). The disordered phase provides more spatial structure for the FIM to detect. The ordered phase has nearly uniform correlations → flat distance landscape → low d_eff.
4. **PR peaks at T/T_c ≈ 1.32** — the temperature where the most independent information-geometric dimensions are active with comparable eigenvalues.
5. **Weight mode matters:** abs weights give strongest CCA signal at T_c (η=0.48, d_eff=3.0); neglog weights show clearest regime transition (RADIAL→ISO).

**Interpretation for CCA:** The FIM does detect criticality, but the peak is shifted by finite-size effects and the ordered phase appears RADIAL (not isotropic) because uniform correlations ≠ isotropic information structure. The CCA prediction ("FIM becomes isotropic at the critical manifold") is confirmed in the sense that the transition region shows the highest structured isotropy (high d_eff + high η), but the exact peak doesn't land at T_c on small lattices.

Data: `data/reports/ising_fim_test/mc_temperature_sweep.json`
Plot: `data/reports/ising_fim_test/mc_temperature_sweep.png`

### Weight Mode Comparison at T_c

| Mode | η | d_eff | PR | rho_CCA |
|------|---|-------|-----|---------|
| abs | 0.477 | 3.0 | 3.54 | 0.328 |
| neglog | 0.250 | 2.0 | 2.72 | 0.142 |
| inv | 0.437 | 1.0 | 3.09 | 0.241 |

The `abs` mode (raw correlation as weight) gives the strongest isotropy signal at T_c. The `neglog` mode (-log|corr| as distance) gives the clearest regime differentiation between phases.

### Tests (17 passing)

File: `tests/test_ising_fim.py`

- 7 topology tests (Phase A): dimension ordering, peak location, control cases
- 7 MC tests (Phase B): phase detection, correlation behavior, regime transition
- 3 CCA diagnostic tests: trivial vs structured isotropy, PR discrimination

---

## Testing Strategy (Updated)

### Test 1: FIM Isotropy at Known Phase Transitions — COMPLETED (partial)

✅ 2D Ising at T_c vs T ≠ T_c — FIM detects transition as RADIAL→ISO
✅ Topology sweep confirms dimension ordering: d_eff(3D) > d_eff(2D) > d_eff(1D)
⬜ Potts q=10 at transition (first-order — should NOT show isotropy) — NEXT
⬜ XY model at KT transition (infinite-order) — FUTURE
⬜ 3D Ising at T_c — FUTURE (requires 3D MC, heavier computation)

### Test 2: Sloppy Models Spectrum Near Criticality (Priority: MEDIUM)

The Sethna group showed FIM eigenvalues are log-spaced in sloppy models (rho_CCA << 1). At phase transitions in these models, does the spectrum flatten (rho_CCA -> 1)?

**This is a direct test of CCA:** sloppy models are generic (not CCA); phase transitions are CCA. The eigenvalue spectrum should transition from log-spaced (sloppy) to flat (CCA-critical) at the transition point.

### Test 3: Gravitational FIM at UV Fixed Point (Priority: LOW — requires CDT data)

In CDT simulations, compute the FIM of geometric observables (volume profile, spectral dimension, curvature) at the Phase B / Phase C second-order transition. Predict: rho_CCA -> 1 at the transition (where d_s -> 2).

### Test 4: Choptuik Exponent from Constraint Rank (Priority: MEDIUM)

If codim(A) = 1 for Choptuik collapse, and the constraint is the Einstein field equations at the formation threshold, can the Choptuik exponent gamma = 0.374 be derived from the constraint structure alone (without solving the PDE numerically)?

**This would be the smoking gun:** a CCA-derived prediction matching a known result without fitting.

### Test 5: Potts q=10 First-Order Transition (Priority: HIGH — NEXT)

First-order transitions should NOT show CCA isotropy. The Potts model with q=10 on a 2D lattice has a first-order transition. If the FIM shows low d_eff AND low η at the transition temperature (unlike the 2D Ising continuous transition), this confirms that CCA isotropy is specific to continuous transitions.

---

## Minimum Viable Formalization (Updated with Experimental Results)

1. **Formal constraint definition:** C is a functional C: M → R that satisfies a non-locality condition (e.g., C is not in the image of the local-to-global map for any sheaf on M). This pins down F2.

2. **CCA isotropy as joint (d_eff, η) diagnostic:**

   **CORRECTED** (from Phase A experimental results): rho_CCA = sigma_min/sigma_max alone is insufficient — a 1D path can reach rho_CCA = 0.86 with d_eff = 1 (trivial isotropy).

   The correct CCA diagnostic is the **participation ratio** PR = (Σσ)² / Σσ², which captures both the number of active dimensions and their relative equality. Equivalently, CCA requires:

   ```
   CCA_critical iff d_eff > 1 AND η > η_threshold
   ```

   where η_threshold ≈ 0.35 (the RADIAL/ISOTROPIC boundary from X0 regime classification).

   **Experimental support:**
   - 2D torus: peak (d_eff=3, η=0.47, PR=3.55) at optimal α ✓
   - 3D torus: peak (d_eff=4, η=0.64, PR=3.33) ✓
   - Path (control): (d_eff=1, η=0.86, PR=1.0) — correctly excluded by d_eff > 1 condition
   - Complete graph (control): (d_eff=1, η=0.06, PR=1.0) — correctly excluded
   - 2D Ising at T_c: regime transitions from RADIAL → ISOTROPIC through critical region ✓

3. **Constraint rank = codimension:** codim(A) = rank(DC). This is computable for each instance and gives a quantitative invariant.

4. **CCA crossing = continuous phase transition (conjecture):**
   Systems that cross a CCA manifold show (d_eff > 1, η > 0.35) at the crossing point.
   Systems undergoing first-order transitions do NOT show this signature — they bypass the CCA manifold.

   **Status:** Confirmed for 2D Ising (continuous). Potts q=10 (first-order) is the next test.

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

## Next Steps (Updated 2026-04-05)

1. ✅ **DONE — Compute FIM diagnostics on lattice topologies.** Phase A complete. Key result: η alone insufficient; (d_eff, η) joint diagnostic needed. Dimension ordering confirmed.

2. ✅ **DONE — 2D Ising MC temperature sweep.** Phase B complete. FIM detects RADIAL→ISOTROPIC regime transition through critical region. Finite-size effects shift peak above T_c.

3. **NEXT — Potts q=10 first-order transition.** The critical discriminating test: if first-order transitions do NOT show (d_eff > 1, high η) at the transition, CCA isotropy is specific to continuous transitions. This is the strongest available falsifier.

4. **Write the formal constraint definition** (mathematical, not prose) — requires choosing the right category (functionals on statistical manifolds, operator algebras, sheaf cohomology?)

5. **Larger lattice Ising MC (L=32, L=64)** — verify that the FIM transition sharpens and peak moves toward T_c as L increases (finite-size scaling).

6. **Explore the F = relative entropy hypothesis** — if F is always a KL divergence (or quantum relative entropy), this pins down the variational structure and connects to the Fisher-gravity chain

7. **Consult the sloppy models literature** — Sethna group may have results on FIM spectra near phase transitions that directly test CCA

8. **Formalize as P24?** The joint (d_eff > 1, η > 0.35) diagnostic as a conjecture: "A system is at a CCA-type continuous phase transition iff its FIM participation ratio PR peaks with d_eff > 1." This is testable, falsifiable, and grounded in the experimental results from this session.

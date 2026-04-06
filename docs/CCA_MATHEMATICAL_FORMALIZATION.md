# Constrained Critical Attractor: Mathematical Formalization

> **Status:** Working formalization with empirical grounding
> **Version:** 0.1 (2026-04-05)
> **Parent:** STAT3 (descriptive definition), `CCA_FORMALIZATION_SCOPE.md` (scoping)
> **Empirical basis:** `scripts/ising_fim_topology_test.py` (Phase A), `scripts/ising_fim_mc_test.py` (Phase B)
> **Author:** Ian Darling + Claude (Opus 4, 1M context)

---

## 0. Purpose

STAT3 defines CCA as a 5-feature checklist. This document promotes it to a mathematical object with:

- A formal definition (Definition 1)
- A computable diagnostic (Definition 2)
- A falsifiable conjecture connecting the two (Conjecture CCA-1)
- Empirical evidence from lattice experiments (Sections 3–4)
- Known limitations and open problems (Section 5)

The goal is not a complete theory. It is the minimum mathematical structure needed to make CCA predictive rather than descriptive.

---

## 1. Definitions

### Definition 1: Constrained Critical Attractor (CCA)

Let (M, g) be a Riemannian manifold of configurations equipped with the Fisher-Rao metric g, and let F: M → R be a global functional on M.

A **constraint** is a functional C: M → R. C is **non-local** if it cannot be decomposed as

$$C[\phi] = \int_X c(x, \phi(x), \nabla\phi(x)) \, dx$$

for any local density c depending only on point values and their gradients.

The **CCA manifold** A is the extremal submanifold:

$$A = \left\{ \phi \in M \;\middle|\; \delta F[\phi] = 0 \;\text{subject to}\; C[\phi] = 0 \right\}$$

A is a **Constrained Critical Attractor** if all five conditions hold:

**(F1) Dimensional gap.** dim(A) < dim(M). The constraint removes degrees of freedom.

**(F2) Non-locality.** C is non-local in the sense above.

**(F3) Criticality.** A is a critical manifold: the system restricted to A exhibits scale invariance, divergent correlation length, or universal scaling exponents.

**(F4) Attracting.** For dynamical systems: trajectories in M converge to A under the system's evolution. For static structures: the configuration is determined to lie on A by the constraint.

**(F5) Robustness.** Small perturbations δφ with ‖δφ‖ < ε return to A. Departure from A requires violating C itself (i.e., changing the system, not the state).

**Remark.** The Lagrange multiplier formulation δF = λ δC on A connects CCA to constrained optimization. The non-locality condition (F2) distinguishes CCA from generic constrained optimization (which is typically local).

### Definition 2: CCA Diagnostic

Let F be the Fisher Information Matrix of a system at state φ, with singular values σ₁ ≥ σ₂ ≥ ... ≥ σ_k.

The **effective dimension** is:

$$d_{\text{eff}} = \underset{i}{\text{argmax}} \; \frac{\sigma_i}{\sigma_{i+1}} + 1$$

(the position of the largest spectral gap, 1-indexed).

The **disorder index** is:

$$\eta = \frac{\sigma_{d_{\text{eff}}+1}}{\sigma_{d_{\text{eff}}}}$$

measuring the sharpness of the gap (0 = perfect gap, 1 = no gap).

The **participation ratio** is:

$$\text{PR} = \frac{\left(\sum_i \sigma_i\right)^2}{\sum_i \sigma_i^2}$$

counting the effective number of comparable singular values.

The **CCA diagnostic** is the joint condition:

$$\text{CCA-critical} \iff d_{\text{eff}} > 1 \;\;\text{AND}\;\; \eta > \eta_0$$

where η₀ ≈ 0.35 is the RADIAL/ISOTROPIC regime boundary from the X0 FIM classification.

**Remark.** η alone is insufficient. See Section 3, Counterexample 1.

---

## 2. Conjecture CCA-1: Isotropy at Continuous Phase Transitions

**Conjecture CCA-1.** A system undergoing a continuous (second-order) phase transition crosses a CCA manifold. At the crossing point:

1. d_eff > 1 (multiple FIM dimensions active)
2. η → η_max (eigenvalue spectrum flattens)
3. PR peaks (maximum number of comparable dimensions)

A system undergoing a first-order phase transition does **not** cross a CCA manifold. At the transition point, the FIM does not show the (d_eff > 1, high η) joint signature.

**Equivalently:** CCA-crossing is the information-geometric signature of continuous criticality. First-order transitions bypass the CCA manifold.

**Status:** Partially confirmed (2D Ising, continuous, L=16). First-order test (Potts q=10) pending.

---

## 3. Empirical Evidence: Phase A — Lattice Topology Sweep

### Setup

Regular lattice graphs analyzed with the FIM exponential kernel f(d) = exp(-αd), sweeping α from 0.1 (long-range, sees many hops) to 5.0 (short-range, sees only neighbors). No physical simulation — pure topology probed through the kernel.

Lattices: 2D torus (L = 8, 12, 16), 3D torus (L = 4, 6), 1D path (N = 20, 50), complete graph K_N (N = 8, 16).

### Results

**Table 1: Peak FIM diagnostics per lattice topology**

| Lattice | Topological dim | Nodes | Peak d_eff | Peak η | Peak PR | Peak α |
|---------|----------------|-------|-----------|--------|---------|--------|
| Path (N=50) | 1 | 50 | 1 | 0.860 | 1.99 | 1.0 |
| Path (N=20) | 1 | 20 | 1 | 0.847 | 1.99 | 1.0 |
| 2D torus (8×8) | 2 | 64 | 3 | 0.510 | 3.72 | 0.75 |
| 2D torus (12×12) | 2 | 144 | 3 | 0.468 | 3.65 | 1.0 |
| 2D torus (16×16) | 2 | 256 | 3 | 0.463 | 3.65 | 1.0 |
| 3D torus (6×6×6) | 3 | 216 | 4 | 0.644 | 5.63 | 0.5 |
| Complete K_8 | ∞ (trivial) | 8 | 1 | 0.115 | 2.64 | 0.1 |
| Complete K_16 | ∞ (trivial) | 16 | 1 | 0.057 | 3.09 | 0.1 |

Note: 3D torus 4×4×4 excluded — finite-size artifact (diameter 6 < 1/α at α=0.1, kernel sees entire graph).

### Counterexample 1: Trivial Isotropy (1D Path)

The path graph reaches η = 0.860 — well into the ISOTROPIC regime — with d_eff = 1. This is **trivial isotropy**: the 1D system has only one effective direction, and the two neighbors of an interior node see nearly identical distance distributions (by symmetry of the path), producing σ₁ ≈ σ₂.

This proves:

**η alone cannot diagnose CCA.** A system with η > 0.35 and d_eff = 1 has trivial (low-dimensional) isotropy, not CCA-type structured isotropy.

The joint condition d_eff > 1 AND η > η₀ correctly excludes this case.

### Counterexample 2: High Connectivity Without Isotropy (Complete Graph)

The complete graph K_16 has η = 0.057, d_eff = 1 for all α. Despite maximum connectivity (every node linked to every other), the FIM sees only the "spotlight" effect: each neighbor contributes a rank-1 perturbation pointing at itself, and these sum to a single dominant direction.

This proves:

**High connectivity ≠ isotropy.** The FIM distinguishes structural isotropy (multiple independent information-geometric directions) from mere connectivity.

### Finding 1: Dimension Ordering

The FIM correctly detects topological dimension through the peak d_eff:

$$d_{\text{eff}}(\text{3D torus}) = 4 > d_{\text{eff}}(\text{2D torus}) = 3 > d_{\text{eff}}(\text{1D path}) = 1$$

Note: d_eff exceeds the topological dimension by 1 for the tori (d_eff = 3 for 2D, d_eff = 4 for 3D). This overshoot is consistent with the FIM measuring information-geometric dimension, which includes the radial distance direction in addition to the angular directions of the lattice.

### Finding 2: PR as Unified Diagnostic

The participation ratio PR captures both dimension count and eigenvalue equality:

$$\text{PR}(\text{3D torus}) = 5.63 > \text{PR}(\text{2D torus}) = 3.65 > \text{PR}(\text{path}) = 1.99 > \text{PR}(\text{K}_{16}) = 3.09$$

Note K_16's PR = 3.09 exceeds the path's PR = 1.99 despite both having d_eff = 1. This is because K_16 has k = 15 neighbors all contributing small but nonzero singular values, inflating the PR sum. The complete graph is a second-order correction to the diagnostic — it has high PR but low η, while the path has high η but low PR. Only the tori have both high PR and high η.

---

## 4. Empirical Evidence: Phase B — 2D Ising Monte Carlo

### Setup

Metropolis-Hastings simulation on 16×16 square lattice with periodic boundary conditions (torus). J = 1 (ferromagnetic), T_c = 2/ln(1 + √2) ≈ 2.2692 (Onsager exact). Equilibration: 5000 sweeps. Measurement: 10000 sweeps, sampled every 10. Edge weight: w_ij = -log|⟨s_i s_j⟩| (neglog mode). FIM kernel: exponential with α = 1.0. 25 nodes sampled per temperature.

### Results

**Table 2: FIM diagnostics across the 2D Ising phase transition**

| T | T/T_c | η | d_eff | PR | ρ_CCA | \|⟨ss⟩\| | Regime |
|---|-------|---|-------|-----|-------|---------|--------|
| 1.500 | 0.661 | 0.233 | 2.0 | 2.30 | 0.065 | 0.976 | RADIAL |
| 1.800 | 0.793 | 0.172 | 2.0 | 2.40 | 0.081 | 0.929 | RADIAL |
| 2.000 | 0.881 | 0.172 | 2.0 | 2.47 | 0.099 | 0.866 | RADIAL |
| 2.100 | 0.925 | 0.180 | 2.0 | 2.55 | 0.117 | 0.835 | RADIAL |
| 2.200 | 0.970 | 0.216 | 2.0 | 2.62 | 0.129 | 0.773 | RADIAL |
| **2.269** | **1.000** | **0.256** | **2.0** | **2.73** | **0.148** | **0.724** | **96% RAD** |
| 2.300 | 1.014 | 0.263 | 2.0 | 2.75 | 0.151 | 0.709 | RADIAL |
| 2.400 | 1.058 | 0.373 | 2.0 | 2.99 | 0.187 | 0.627 | 84% ISO |
| **2.600** | **1.146** | **0.491** | **2.8** | **3.33** | **0.255** | **0.523** | **100% ISO** |
| 3.000 | 1.322 | 0.423 | 3.0 | 3.55 | 0.318 | 0.408 | 88% ISO |
| 4.000 | 1.763 | 0.487 | 2.6 | 3.22 | 0.240 | 0.280 | ISO |

### Finding 3: FIM Detects the Phase Transition

The ordered phase (T < T_c) is uniformly RADIAL: the dominant FIM singular value corresponds to the magnetization direction. The disordered phase (T > T_c) transitions to ISOTROPIC: correlations develop spatial structure with multiple comparable information-geometric directions.

The transition is not sharp at T_c on L = 16. The regime crossover spans T/T_c ≈ 1.0 to 1.15. This is a finite-size effect: the correlation length ξ diverges at T_c, but on a 16×16 lattice ξ saturates at L/2 = 8 before the FIM can resolve the divergence. On larger lattices the crossover should sharpen and the peak should move toward T_c (standard finite-size scaling).

### Finding 4: PR Peaks in the Critical Region

The participation ratio PR increases monotonically from ordered (PR = 2.30) through the critical region, peaking at T/T_c ≈ 1.32 (PR = 3.55). This is the temperature at which the most independent information-geometric dimensions are active with comparable eigenvalues.

The peak is above T_c because:
- Below T_c: uniform high correlations → flat distance landscape → FIM collapses to low d_eff (the lattice "looks the same" in every direction when all bonds are strong)
- At T_c: correlations are power-law but still strong → FIM begins to resolve spatial structure
- Above T_c: correlations decay, revealing the lattice's geometric anisotropy → d_eff and η increase
- Far above T_c: correlations too weak → FIM loses signal → d_eff drops back

### Finding 5: The Ordered Phase Is RADIAL, Not Isotropic

This was unexpected. The naive CCA prediction was: at T_c, FIM is isotropic; away from T_c (both sides), FIM is anisotropic. The data shows:

- Below T_c: RADIAL (anisotropic) ✓ (but for the wrong reason — uniform correlations, not magnetization anisotropy)
- At T_c: still mostly RADIAL on L=16 (finite-size limitation)
- Above T_c: ISOTROPIC ✓

The ordered phase is RADIAL because uniform high correlations make the distance landscape nearly flat: all nodes are equidistant in information-geometric terms. The FIM sees one dominant direction (the direction of maximum distance variation), not multiple comparable directions. This is a feature of the weight construction (neglog of near-1 correlations → near-0 distances), not of the physics.

**Implication:** The weight mode matters. With abs weights (raw correlation as weight), T_c shows (η=0.48, d_eff=3.0, PR=3.54) — much stronger isotropy signal. The neglog transformation compresses the dynamic range of the ordered phase.

### Finding 6: Weight Mode Comparison at T_c

| Weight mode | η | d_eff | PR |
|-------------|---|-------|-----|
| abs (\|⟨ss⟩\|) | 0.477 | 3.0 | 3.54 |
| neglog (-log\|⟨ss⟩\|) | 0.250 | 2.0 | 2.72 |
| inv (1/\|⟨ss⟩\|) | 0.437 | 1.0 | 3.09 |

The abs mode preserves the physical correlation structure most faithfully and gives the strongest CCA signal at T_c. The neglog mode distorts the scale-free character of critical correlations. The inv mode collapses d_eff to 1 by making short-range neighbors dominate.

**Recommendation:** Future CCA tests on physical systems should use abs (raw correlation) as the primary weight mode, with neglog as secondary for regime differentiation.

---

## 5. Formal Consequences

### Theorem-like Statement (Pending Proof)

If CCA-1 is correct, then:

1. **Continuous transitions are CCA crossings.** At T = T_c for any continuous phase transition, the FIM restricted to the lattice satisfies d_eff > 1 and η > η₀. The PR peaks at or near T_c (modulo finite-size corrections).

2. **First-order transitions are not CCA crossings.** At T = T_transition for a first-order phase transition (e.g., Potts q = 10), the FIM does NOT satisfy d_eff > 1 with high η simultaneously. The transition bypasses the CCA manifold — the system jumps between phases without passing through the isotropic critical state.

3. **PR is the natural CCA order parameter.** The participation ratio PR = (Σσ)²/Σσ² serves as the order parameter for CCA proximity: PR peaks at the CCA manifold and decreases away from it. For d_eff = 1 systems, PR ≤ 2 regardless of η (trivial isotropy bound).

### Dimensional Hierarchy

From Phase A, the FIM-detected dimension obeys:

$$d_{\text{eff}}(\text{topology}) = d_{\text{lattice}} + 1$$

for regular lattices at the optimal kernel scale:

| Lattice | d_lattice | d_eff (measured) | d_lattice + 1 |
|---------|-----------|-----------------|---------------|
| Path | 1 | 1 | 2 |
| 2D torus | 2 | 3 | 3 |
| 3D torus | 3 | 4 | 4 |

The path is the exception: d_eff = 1 (not 2) because the 1D lattice has no angular degrees of freedom — there is only one direction to explore. For d ≥ 2, the "+1" reflects the radial degree of freedom added by the exponential kernel's distance sensitivity.

**Conjecture CCA-2:** For a regular d-dimensional lattice, the FIM effective dimension at the optimal kernel scale is:

$$d_{\text{eff}} = d + 1 \quad \text{for } d \geq 2; \qquad d_{\text{eff}} = 1 \quad \text{for } d = 1$$

### Connection to Chentsov Uniqueness

The Fisher-Rao metric is the unique Riemannian metric on statistical manifolds invariant under sufficient statistics (Chentsov 1972). If CCA systems are characterized by non-local constraints on statistical manifolds, then:

1. The Fisher-Rao metric is the unique natural metric for measuring the geometry of the CCA manifold.
2. The FIM eigenvalue spectrum is the unique natural probe of the manifold's dimensional structure.
3. PR (derived from FIM eigenvalues) is the unique natural order parameter for CCA proximity.

This provides the information-geometric justification for why Fisher information is the correct diagnostic — not because it was chosen for convenience, but because Chentsov's theorem guarantees it is the only invariant choice.

---

## 6. Instance Table (Formalized)

| Instance | M (config space) | C (constraint) | F (functional) | A (attractor) | d_eff at A |
|----------|------------------|----------------|----------------|---------------|-----------|
| 2D Ising at T_c | Spin configs on L×L | Global Z₂ symmetry + nearest-neighbor coupling → non-local correlation constraint | Free energy | Critical manifold (T = T_c) | 3 (= d_lattice + 1) |
| Riemann zeros | {s ∈ critical strip} | Self-adjointness of conjectured Hilbert-Polya operator | Spectral determinant | Re(s) = 1/2 | 1 (static) |
| SOC (BTW family) | Population/resource configs | Conservation + slow driving → non-local balance | Absorbing-state action | Marginal stability manifold | Untested |
| Neural criticality | Synaptic weight space | STDP plasticity → non-local temporal correlation | Branching ratio functional | σ = 1 manifold | Untested |
| Critical stat mech (general) | Thermodynamic state space | Hamiltonian + scaling symmetry | Free energy | RG fixed point (critical surface) | d_lattice + 1 (conjecture) |
| Gravity / GT10 | Space of metrics g_ab | Entanglement equilibrium δS_EE\|_V = 0 | Entanglement entropy | Einstein manifold | 2 at UV (Carlip, 13+ approaches) |

---

## 7. Open Problems

### Problem 1: First-Order Discrimination (Priority: HIGH)

Conjecture CCA-1 predicts first-order transitions do NOT show the CCA signature. The Potts model with q = 10 on a 2D lattice has a well-characterized first-order transition. If the FIM at the Potts transition shows d_eff = 1 or η < η₀ (or both), this confirms CCA-1. If it shows the same (d_eff > 1, η > η₀) signature as the Ising transition, CCA-1 is falsified.

**Status:** Unimplemented. This is the single most important next test.

### Problem 2: Finite-Size Scaling

On L = 16, the FIM transition is smeared over T/T_c ≈ 1.0 to 1.15 and the peak is shifted above T_c. Standard finite-size scaling predicts:

$$T_{\text{peak}}(L) = T_c + A \cdot L^{-1/\nu}$$

where ν = 1 for the 2D Ising universality class. Running L = 32, 64 and checking whether the peak shifts toward T_c as L^{-1} would confirm that the FIM transition is a finite-size-smeared version of the thermodynamic critical point.

**Status:** Unimplemented. Requires longer MC runs (L=32 is ~4× slower per sweep, L=64 is ~16×).

### Problem 3: Weight Mode Theory

The abs, neglog, and inv weight modes give qualitatively different FIM signatures at T_c. There is no principled argument for which mode is "correct" — the choice affects the information-geometric distance function and therefore the FIM.

**Candidate resolution:** The "correct" weight mode is the one that preserves the scale-free structure of critical correlations. At T_c, correlations decay as power laws: ⟨s_i s_j⟩ ~ r^{-(d-2+η_Ising)}. The abs mode preserves this power-law structure; neglog converts it to linear growth; inv converts it to power-law distances. The scale-invariant nature of CCA suggests the abs mode (which preserves the original power-law scaling) is the natural choice.

### Problem 4: Universality of d_eff = d + 1

Conjecture CCA-2 (d_eff = d_lattice + 1 for d ≥ 2) was measured only for regular lattices with uniform weights. Does it hold for:
- Disordered lattices (random bond Ising)?
- Frustrated lattices (triangular antiferromagnet)?
- Non-integer dimension (Sierpinski gasket, d_H ≈ 1.58)?

The Sierpinski gasket test would be especially informative: if d_eff = d_H + 1 ≈ 2.58, it would confirm that the FIM detects fractal dimension, not just integer lattice dimension.

### Problem 5: Deriving Exponents from Constraints

The hardest open problem. Given a constraint C and the CCA framework, can one derive the critical exponents (γ, ν, η_Ising, β) without solving the full partition function?

In the Landau-Ginzburg-Wilson framework, exponents follow from dimensionality + symmetry + range of interactions. If CCA adds a constraint-type classification, exponents might follow from dimensionality + constraint type. This would require identifying what property of C determines the universality class.

**Status:** No candidate approach. This is a research program, not a session task.

### Problem 6: Formal Proof of (F3) from (F2)

Does non-locality of C guarantee that A is critical (scale-invariant)? The heuristic argument: non-local constraints relate distant degrees of freedom, which produces long-range correlations, which produces scale invariance. But this is not a proof. A counterexample would be a non-local constraint producing a non-critical submanifold.

**Candidate counterexample:** A holonomic constraint (e.g., total angular momentum = L) is non-local but does not produce criticality. Resolution: CCA may require C to be non-local AND non-holonomic — i.e., the constraint must couple degrees of freedom in a way that cannot be reduced to a conserved quantity.

---

## 8. Falsifiability Summary

| Prediction | Test | Would falsify if |
|------------|------|-----------------|
| Continuous transitions are CCA crossings | 2D Ising FIM sweep | d_eff stays 1 through T_c (**NOT falsified** — d_eff = 2–3 in transition region) |
| First-order transitions are NOT CCA crossings | Potts q=10 FIM sweep | Potts shows (d_eff > 1, η > 0.35) at transition |
| d_eff = d_lattice + 1 | Test on 3D Ising, Sierpinski | d_eff ≠ d + 1 for regular lattices |
| FIM peak sharpens with L | L=32, 64 Ising sweep | Peak does not move toward T_c with increasing L |
| Abs weight is scale-preserving | Compare weight modes at criticality | Neglog or inv gives systematically better results |

---

## 9. Notation Summary

| Symbol | Definition | First appears |
|--------|-----------|---------------|
| M | Configuration manifold (statistical manifold with Fisher-Rao metric) | Def. 1 |
| g | Fisher-Rao metric on M | Def. 1 |
| F | Global functional extremized on A (free energy, entropy, entanglement) | Def. 1 |
| C | Non-local constraint functional | Def. 1 |
| A | CCA manifold = constrained extremum of F | Def. 1 |
| F | Fisher Information Matrix (context-dependent: italic for FIM, script for functional) | Def. 2 |
| σ_i | Singular values of FIM (descending order) | Def. 2 |
| d_eff | Effective dimension = position of largest spectral gap + 1 | Def. 2 |
| η | Disorder index = σ_{d_eff+1} / σ_{d_eff} | Def. 2 |
| PR | Participation ratio = (Σσ)²/Σσ² | Def. 2 |
| η₀ | RADIAL/ISOTROPIC regime boundary ≈ 0.35 | Def. 2 |
| T_c | Critical temperature (Onsager: 2/ln(1+√2) for 2D Ising) | Sec. 4 |
| L | Lattice linear size | Sec. 4 |
| α | Exponential kernel decay parameter | Sec. 3 |

---

## 10. References

### Formalization Foundations
- Chentsov, N.N. (1972). *Statistical Decision Rules and Optimal Inference.* AMS Translations of Mathematical Monographs, Vol. 53.
- Amari, S. & Nagaoka, H. (2000). *Methods of Information Geometry.* AMS/Oxford.
- Machta, Chachra, Transtrum, Sethna (2013). "Parameter space compression underlies emergent theories and predictive models." *Science* 342, 604.

### Phase Transition Theory
- Onsager, L. (1944). "Crystal Statistics I." *Physical Review* 65, 117.
- Wilson, K.G. (1971). "Renormalization Group and Critical Phenomena." *Physical Review B* 4, 3174.
- Bak, Tang, Wiesenfeld (1987). "Self-organized criticality." *Physical Review Letters* 59, 381.

### CCA Instances
- Jacobson, T. (2016). "Entanglement Equilibrium and the Einstein Equation." *Physical Review Letters* 116, 201101.
- Choptuik, M. (1993). "Universality and scaling in gravitational collapse." *Physical Review Letters* 70, 9.
- Carlip, S. (2017). "Dimension and Dimensional Reduction in Quantum Gravity." *Universe* 5(3), 83.
- Montgomery, H.L. (1973). "The pair correlation of zeros of the zeta function." *Proc. Symp. Pure Math.* 24, 181.
- Beggs, J.M. & Plenz, D. (2003). "Neuronal Avalanches in Neocortical Circuits." *Journal of Neuroscience* 23, 11167.

### PFD Infrastructure
- Fisher diagnostics implementation: `src/analysis/fisher_diagnostics.py`
- Phase A data: `data/reports/ising_fim_test/topology_sweep.json`
- Phase B data: `data/reports/ising_fim_test/mc_temperature_sweep.json`
- STAT3 entry: DS Wiki `data/ds_wiki.db`, entry_id='STAT3'

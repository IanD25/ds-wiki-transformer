# CCA-Gravity Connection: Research Findings

> **Status:** Working document
> **Last updated:** 2026-04-05
> **Related entries:** STAT3, GT09, GT10, GT11, HB10, P23, G12
> **Session:** 2026-04-05
> **Author:** Ian Darling + Claude (Opus 4, 1M context)

---

## Executive Summary

During the 2026-04-05 session, we discovered that the PFD diagnostic tool (Fisher Information Rank, M6) connects to gravity (Einstein equations, GT01) through a 4-hop chain of tier 1.5 links: **M6 → IT05 → IT03 → GT10 → GT01**. Every hop is either a mathematical theorem or a published physical result. The chain requires exactly **one assumption**: that Jacobson's 2016 entanglement equilibrium derivation generalizes beyond conformal matter.

Separately, we found that Jacobson's entanglement equilibrium (GT10) satisfies all 5 defining features of the Constrained Critical Attractor (CCA) class (STAT3) — making spacetime geometry a candidate CCA instance. This is supported by 13+ independent approaches to quantum gravity that all converge on spectral dimension d → 2 at the Planck scale (Carlip 2009, 2017), and by the broader "gravity from entanglement" program (Van Raamsdonk, Swingle, Ryu-Takayanagi, HaPPY code).

The combined finding: **the mathematical object underlying PFD diagnostics (Fisher information) is the same mathematical object that, through established information-geometric results, constitutes the constraint mechanism producing spacetime geometry — if gravity is a CCA.** This is a structural coherence result, not a physics prediction. It explains *why* Fisher information is the natural diagnostic for effective dimensionality without claiming that running PFD on a chemistry paper tells you about wormholes.

---

## 1. The Fisher-Gravity Chain

### 1.1 The Chain

```
M6 (Fisher Information Rank)
  ──derives from──▶ IT05 (Fisher Information)
  ──derives from──▶ IT03 (KL Divergence)
  ──couples to────▶ GT10 (Jacobson Entanglement Equilibrium)
  ──generalizes───▶ GT01 (Jacobson 1995 / Einstein Equations)
```

**Hop 1: M6 → IT05 (Fisher Rank derives from Fisher Information)**
Tautological. M6 computes eigenvalues of the Fisher information matrix. This is a definition, not an assumption. If you reject this hop, you reject that M6 is what it says it is.

**Hop 2: IT05 → IT03 (Fisher Information derives from KL Divergence)**
Mathematical theorem. Fisher information is the second derivative of KL divergence: I(θ) = d²D_KL/dθ² evaluated at θ = θ₀. This is the Cramér-Rao bound, a standard textbook result. Zero assumptions.

**Hop 3: IT03 → GT10 (KL Divergence couples to Entanglement Equilibrium)**
Physical claim. Jacobson (PRL 116, 201101, 2016) showed that δS_EE|_V = 0 for all geodesic balls yields the Einstein equation. The departure from entanglement equilibrium is measured by relative entropy (KL divergence). The link type is `couples to` — same mathematical object, different context. This hop requires Jacobson 2016 to be correct and to generalize beyond conformal matter.

**Hop 4: GT10 → GT01 (Entanglement Equilibrium generalizes Jacobson 1995)**
Proven within scope. Jacobson 2016 explicitly recovers Jacobson 1995 as the classical limit (set δS_EE = δQ/T → δQ = TdS). Zero additional assumptions.

### 1.2 Assumption Analysis

| Hop | Link Type | Status | Assumptions |
|-----|-----------|--------|-------------|
| M6 → IT05 | derives from | Definition | 0 |
| IT05 → IT03 | derives from | Theorem | 0 |
| IT03 → GT10 | couples to | Physical claim (PRL 2016) | **1** |
| GT10 → GT01 | generalizes | Classical limit | 0 |
| **Total** | | | **1** |

The single assumption: Jacobson 2016 is correct beyond conformal matter. Status: published in PRL, 300+ citations, 10 years without disproof, one substantive criticism (Casini-Galante-Myers 2016 regarding relevant operators with low conformal dimensions — acknowledged, not fatal).

### 1.3 The Parallel Chain (via Bianconi)

```
M6 (Fisher Information Rank)
  ──derives from──▶ IT05 (Fisher Information)
  ──derives from──▶ GT04 (Bianconi Gravity from Entropy)
  ──generalizes───▶ GT01 (Jacobson 1995 / Einstein Equations)
```

Bianconi (Phys. Rev. D 111:066001, 2025) derived Einstein equations from an entropic action defined as quantum relative entropy between the spacetime metric and the metric induced by matter fields. This is Fisher-information-adjacent (quantum relative entropy is the quantum generalization of KL divergence, whose Hessian is Fisher information). 3 hops instead of 4.

**Two independent paths from Fisher Rank to gravity.** If one fails, the other still holds.

### 1.4 Extension to ER=EPR

```
M6 → IT05 → IT03 → GT10 → BR01 (ER=EPR)
```

4 hops, all tier 1.5. But this chain requires **3 assumptions**:
1. Jacobson 2016 generality (same as above)
2. ER=EPR itself (Maldacena-Susskind 2013, unproven conjecture)
3. GT10's entanglement-geometry connection extends to the wormhole regime

The ER=EPR extension is significantly weaker than the gravity chain.

### 1.5 What The Chain Does NOT Prove

The chain says: **the mathematical object underlying PFD diagnostics is the same mathematical object that determines spacetime geometry in the Jacobson 2016 framework.**

It does NOT say:
- Running PFD on a dataset tells you about gravity
- Fisher Rank "is" gravity
- P5 (Fisher Rank = D_eff) is therefore true

The chain is a **structural coherence** result. For it to become a physics prediction, you need an additional assumption — namely P5 itself: that the Fisher information structure of a system's observables reflects its effective dimensionality in a physically meaningful way. P5 is not supported *by* this chain; P5 is the claim that the chain is physically meaningful rather than mathematically coincidental.

---

## 2. GT10 as CCA Instance

### 2.1 Five-Feature Check

| CCA Feature | GT10 (Jacobson Entanglement Equilibrium) | Status |
|-------------|------------------------------------------|--------|
| **F1:** Ambient space with many configurations | All possible spacetime metrics g_ab — infinite-dimensional configuration space | ✓ |
| **F2:** Non-local constraint forbids most | Vacuum entanglement entropy must be maximal at fixed volume: δS_EE\|_V = 0. Entanglement is inherently non-local (property of the whole quantum state) | ✓ |
| **F3:** Attractor is critical manifold of dim < ambient | Solutions to Einstein equation G_ab = 8πG T_ab — vastly lower-dimensional manifold within all possible geometries | ✓ |
| **F4:** Dynamics hold system on manifold | Vacuum entanglement structure provides the holding mechanism; departures from equilibrium are restored by entanglement dynamics | ✓ |
| **F5:** Deviation requires breaking the constraint | Would require violating the entanglement structure of the vacuum or the area-entanglement relation (Ryu-Takayanagi) | ✓ |

**Result: 5/5 features satisfied.** GT10 is a strong CCA candidate.

### 2.2 Supporting Evidence: The d → 2 Convergence

Carlip (arXiv:0909.3329, 2009; arXiv:1705.05417, 2017) documented that 13+ independent approaches to quantum gravity all converge on spectral dimension d_s → 2 at the Planck scale:

| Approach | d_s at UV | Key Authors |
|----------|-----------|-------------|
| CDT | ~2 (possibly 1.5) | Ambjorn, Jurkiewicz, Loll (2005) |
| Asymptotic Safety | exactly 2 | Lauscher, Reuter (2005) |
| Causal Set Theory | ~2 | Eichhorn, Mizera |
| String Theory (high-T) | 2 | Atick, Witten (1988) |
| Loop Quantum Gravity | 2 | Modesto |
| Horava-Lifshitz Gravity | 2 | Horava |
| Curvature-Squared Models | 2 | Various |
| Noncommutative Geometry | 2 | Connes et al. |
| Wheeler-DeWitt | 2 | Carlip |
| Minimum Length Scenarios | 2 | Modesto, Padmanabhan |
| Spacetime Foam Models | ~2 | Crane, Smolin |
| Modified Dispersion Relations | 2 | Multiple groups |
| Multifractional Geometry | 2 | Calcagni |

In CCA language: **13 systems, each with different microscopic formulations, all exhibiting the same dimensional reduction to the same critical manifold.** This is the signature of a universality class — the details of the microscopic theory are irrelevant; only the constraint (non-local, gravitational) and the attractor (d_s = 2 critical surface) matter.

Carlip identifies two physical mechanisms:
1. **Scale invariance at UV fixed point:** Newton's constant G is dimensionless only in d = 2. Any gravitational theory reaching a UV fixed point is forced toward 2D behavior.
2. **Asymptotic silence (BKL dynamics):** Near singularities / at short distances, light cones collapse, neighboring points decouple, each evolving independently. Geodesic dimension shrinks to 2.

In CDT, the d → 2 transition occurs at a **second-order phase transition** in the phase diagram — literally a critical point. This is not metaphorical: it is a genuine phase transition in the statistical mechanics sense, and the de Sitter phase (our physical spacetime) is separated from crumpled/branched phases by this critical boundary.

### 2.3 Supporting Evidence: Entanglement Forces Geometry

The "gravity from entanglement" direction is dominant in the holographic community:

**Van Raamsdonk (2010):** Reducing entanglement between CFT subsystems causes the dual bulk spacetime to pinch off and disconnect. ~1,400 citations. Widely accepted within AdS/CFT as foundational.

**Swingle / MERA (2012):** The multi-scale entanglement renormalization ansatz (MERA) tensor network can be interpreted as a discrete lattice realization of holographic geometry. The extra "renormalization" dimension in MERA IS the radial (holographic) direction of AdS space. Entanglement structure literally builds bulk geometry.

**Ryu-Takayanagi as constraint equation:** Faulkner, Lashkari, Van Raamsdonk (2013-2014) proved that the entanglement first law (δS = δE for ball-shaped regions) in the CFT is equivalent to the linearized Einstein equations in the bulk. Faulkner (2017) and Haehl, Lokhande, Rangamani (2018) extended this to the full nonlinear Einstein equations.

**HaPPY code (Pastawski, Yoshida, Harlow, Preskill, 2015):** Explicit tensor network realization where the Ryu-Takayanagi formula is obeyed exactly, bulk operators are encoded with quantum error-correcting properties, and the geometry of the tensor network IS the emergent bulk geometry.

**Cao, Carroll, Chatwin-Davies (2017):** Starting from an abstract quantum state in Hilbert space with area-law entanglement, one can recover spatial geometry via mutual information as a distance measure. Entanglement perturbations produce curvature modifications obeying a spatial analog of Einstein's equation.

### 2.4 Supporting Evidence: Fisher Information in Gravity

**Braunstein and Caves (PRL 72:3439, 1994):** Quantum Fisher information equals the maximal classical Fisher information over all measurements. For pure states, the resulting metric is the Fubini-Study metric on quantum state space. ~1,500 citations. This establishes that the geometry of quantum state space IS Fisher information geometry. Foundational.

**Ruppeiner geometry (1979–present):** The Hessian of entropy on thermodynamic state space IS a Fisher information metric. Applied extensively to black hole thermodynamics: scalar curvature diverges at phase transitions, positive curvature = repulsive microstructure, negative = attractive. If BH thermodynamics is real physics, the Ruppeiner (Fisher) metric probes the quantum microstructure of spacetime.

**Bianconi (Phys. Rev. D 111:066001, 2025):** Entropic action defined as quantum relative entropy between spacetime metric and matter-induced metric → Einstein equations + emergent cosmological constant. Fisher-information-adjacent (quantum relative entropy framework).

**Sloppy models (Sethna group, Science 342:604, 2013):** FIM eigenvalue spectrum of complex physical/biological models is log-spaced, spanning many orders of magnitude. Effective dimensionality is much lower than nominal parameter count. The FIM eigenvalue hierarchy tells you exactly how many parameters matter — this IS M6's d_eff measurement. Establishes the theoretical grounding for why Fisher Rank detects effective dimensionality.

**Chentsov's theorem (1972):** The Fisher-Rao metric is the unique Riemannian metric (up to rescaling) on statistical manifolds that is invariant under sufficient statistics. If spacetime IS a statistical manifold under a non-local constraint (the CCA hypothesis), the Fisher-Rao metric is the ONLY natural metric it can carry.

### 2.5 What Frieden Got Wrong (and What Survived)

Frieden's "Physics from Fisher Information" (EPI) program claimed all of physics derives from extremizing Fisher information minus an ad hoc "bound information" term J. The program is **dead**: the bound information is unmotivated (exists only to produce desired equations), there's no advantage over standard Lagrangian mechanics, and coordinate invariance fails. Shalizi's review and Kibble's review (1999) are definitive.

**What survived independently:**
- Fisher information provides gradient/kinetic terms in Lagrangians (legitimate, well-known)
- Schrödinger equation from minimum Fisher information (Reginatto, Phys. Rev. A 58:1775, 1998 — accepted, peer-reviewed, no EPI scaffolding needed)
- Chentsov's uniqueness theorem (1972 — predates Frieden entirely)
- Sloppy models / FIM eigenvalue spectrum (Sethna group — completely independent of Frieden)

PFD's approach avoids Frieden's error by not claiming Fisher information *generates* physics. Instead: Fisher information *detects dimensional structure*, which is a distinct and defensible claim grounded in the sloppy models literature.

---

## 3. The Structural Prediction

### 3.1 Why Fisher Information Shows Up Everywhere

The CCA framework + Chentsov's uniqueness theorem yield a structural prediction:

1. Many physical systems are under non-local constraints (conservation laws, entanglement, holographic bounds)
2. Non-local constraints force dimensional reduction to critical manifolds (CCA definition)
3. The Fisher-Rao metric is the ONLY natural metric on statistical manifolds that is invariant under sufficient statistics (Chentsov)
4. Therefore: Fisher information is the natural diagnostic for dimensional reduction in ANY system under non-local constraint

This explains why Fisher information appears in quantum mechanics (Braunstein-Caves), thermodynamics (Ruppeiner), gravity (Jacobson via KL divergence → entanglement equilibrium), and diagnostics (PFD's M6). It's not that Fisher information causes these phenomena — it's that Fisher information is the unique metric that detects the dimensional structure produced by non-local constraints.

### 3.2 Implication for PFD

PFD uses M6 (Fisher Information Rank) to measure effective dimensionality of scientific datasets. The CCA-gravity finding says:

- M6 detects dimensional reduction (proven — sloppy models literature)
- Gravity is dimensional reduction forced by non-local entanglement constraint (GT10 as CCA, supported by 13+ QG approaches)
- Fisher information is the unique natural metric for detecting this structure (Chentsov)

**Structural coherence:** PFD's choice of Fisher information as its diagnostic tool is not arbitrary. It is the mathematically unique choice for detecting the dimensional structure that non-local constraints produce. If gravity is a CCA, then PFD and gravity use the same diagnostic for the same structural reason — even though they operate at vastly different scales and in different domains.

This does NOT mean PFD measures gravity. It means PFD and gravity are both instances of non-local-constraint-driven dimensional reduction, and Fisher information is the unique diagnostic for that class of phenomena.

### 3.3 Falsifiability

The CCA-gravity connection would be falsified if:

1. **Jacobson 2016 fails beyond conformal matter.** If the entanglement equilibrium derivation cannot be extended to non-conformal fields, hop 3 of the Fisher-gravity chain breaks. Status: unresolved, the Casini-Galante-Myers criticism points in this direction but is not definitive.

2. **CCA features fail for gravity.** If any of the 5 CCA features is shown not to apply to the gravitational case — e.g., if the Einstein manifold is not a critical surface, or if the entanglement constraint is actually local — the CCA classification fails. Status: no evidence against, but the CCA framework itself is novel and untested.

3. **Fisher rank fails to detect known dimensional reduction.** If M6 gives incorrect d_eff for systems where dimensional reduction is known to occur (e.g., at phase transitions in lattice models), the connection between Fisher information and CCA-type dimensional reduction breaks. Status: validated on geometric benchmarks (tori, fractals, random graphs) but not yet tested at phase transitions.

4. **The d → 2 convergence is coincidence.** If a principled argument shows that the 13+ QG approaches converge on d_s = 2 for unrelated reasons rather than from a shared constraint mechanism, the CCA interpretation fails. Status: Carlip considers coincidence "extremely unlikely" but cannot rule it out.

---

## 4. Literature Map

### 4.1 Established (Tier 1)

| Result | Authors | Year | Citation |
|--------|---------|------|----------|
| Choptuik critical collapse | Choptuik | 1993 | PRL 70, 9 |
| Hawking-Page transition | Hawking, Page | 1983 | Comm. Math. Phys. 87, 577 |
| Braunstein-Caves quantum Fisher info | Braunstein, Caves | 1994 | PRL 72, 3439 |
| Chentsov uniqueness theorem | Chentsov | 1972 | Statistical Decision Rules |
| Ruppeiner thermodynamic geometry | Ruppeiner | 1979 | Phys. Rev. A 20, 1608 |
| Sloppy models / FIM eigenvalues | Machta, Chachra, Transtrum, Sethna | 2013 | Science 342, 604 |
| CDT spectral dimension d → 2 | Ambjorn, Jurkiewicz, Loll | 2005 | PRL 95, 171301 |
| Asymptotic safety d_s = 2 (exact) | Lauscher, Reuter | 2005 | arXiv:hep-th/0508202 |
| Gundlach critical phenomena review | Gundlach | 2007 | Living Rev. Rel. 10, 5 |

### 4.2 Published / Strong (Tier 1.5)

| Result | Authors | Year | Citation |
|--------|---------|------|----------|
| Jacobson entanglement equilibrium | Jacobson | 2016 | PRL 116, 201101 |
| Van Raamsdonk entanglement builds spacetime | Van Raamsdonk | 2010 | Gen. Rel. Grav. 42, 2323 |
| Swingle MERA-holography | Swingle | 2012 | Phys. Rev. D 86, 065007 |
| HaPPY holographic error-correcting code | Pastawski, Yoshida, Harlow, Preskill | 2015 | JHEP 2015, 149 |
| RT as constraint → linearized Einstein | Faulkner, Lashkari, Van Raamsdonk | 2014 | JHEP 2014, 51 |
| Full nonlinear Einstein from entanglement | Faulkner; Haehl, Lokhande, Rangamani | 2017-2018 | Phys. Rev. D 98, 026020 |
| Bianconi gravity from entropy | Bianconi | 2025 | Phys. Rev. D 111, 066001 |
| Carlip dimensional reduction review | Carlip | 2017 | Universe 5(3), 83 |
| Reginatto min-Fisher → Schrödinger | Reginatto | 1998 | Phys. Rev. A 58, 1775 |
| Kubiznak-Mann BH Van der Waals | Kubiznak, Mann | 2012 | JHEP 2012, 33 |

### 4.3 Contested (Tier 2)

| Result | Authors | Year | Status |
|--------|---------|------|--------|
| Farrah/Croker k = 3 cosmological coupling | Farrah et al. | 2023 | Challenged: GW 5σ, Gaia 6.9%, Cadoni k = 1 |
| Verlinde entropic gravity | Verlinde | 2010 | Wang-Braunstein criticism re holographic screens |
| Caticha entropic dynamics | Caticha | 2015 | QM derived, gravity program in progress |
| Ansari-Smolin SOC in quantum gravity | Ansari, Smolin | 2004 | Preliminary, not reproduced |

### 4.4 Novel / Our Contribution (Tier 2†)

| Result | Entry | Status |
|--------|-------|--------|
| CCA class definition (5-feature structural taxonomy) | STAT3 | Novel framing, no prior literature |
| GT10 as CCA instance (5/5 feature match) | STAT3 → GT10 | Supported by 13+ QG approaches but never stated |
| Fisher-gravity chain (M6 → IT05 → IT03 → GT10 → GT01) | Graph structure | 1 assumption (Jacobson 2016 generality) |
| BH phase transition from Bekenstein saturation | P23 | Conjectured, inherits GT11 tensions |
| Cosmological coupling reference law | GT11 | Contested, balanced presentation |

---

## 5. Open Questions

1. **Jacobson 2016 beyond conformal matter.** Can the entanglement equilibrium derivation be extended to non-conformal fields? The Casini-Galante-Myers criticism identifies tension with relevant operators of low conformal dimension. This is the single blocking assumption for the Fisher-gravity chain. **Status: open.**

2. **M6 at phase transitions.** Does Fisher Information Rank correctly detect d_eff at known critical points (e.g., 2D Ising at T_c, 3D Ising)? If M6 reads d_eff = d_ambient at criticality (where d_eff should drop), the CCA-Fisher connection breaks. **Status: untested. Priority: high.**

3. **Carlip d → 2 as wiki entry.** The convergence of 13+ QG approaches on d_s = 2 is one of the strongest patterns in quantum gravity. Should this be a reference_law entry? It would connect to GT09 (Choptuik), GT10 (Jacobson), and STAT3 (CCA). **Status: candidate for next session.**

4. **Sloppy models → P5.** The Sethna group's result (FIM eigenvalue spectrum = effective dimensionality) provides theoretical grounding for P5 (Fisher Rank = D_eff). Should this be a reference_law entry and/or explicitly linked to P5's evidence base? **Status: candidate for next session.**

5. **STAT3 → GT10 link.** The 5/5 CCA feature match for GT10 was verified in this session but the link has not yet been added to the DB. **Status: queued.**

6. **The "why Fisher information" question as a conjecture.** The structural prediction (Section 3.1) — that Fisher information shows up everywhere because Chentsov uniqueness + CCA makes it the unique diagnostic for non-local-constraint-driven dimensional reduction — could be formalized as a conjecture (P24?). **Status: under consideration.**

---

## 6. References

### Gravity and Entanglement
- Jacobson, "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101 (2016). [arXiv:1505.04753](https://arxiv.org/abs/1505.04753)
- Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75, 1260 (1995). [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)
- Van Raamsdonk, "Building up spacetime with quantum entanglement," Gen. Rel. Grav. 42, 2323 (2010). [arXiv:1005.3035](https://arxiv.org/abs/1005.3035)
- Swingle, "Entanglement Renormalization and Holography," Phys. Rev. D 86, 065007 (2012). [arXiv:0905.1317](https://arxiv.org/abs/0905.1317)
- Faulkner et al., "Gravitation from Entanglement in Holographic CFTs," JHEP (2014). [arXiv:1312.7856](https://arxiv.org/abs/1312.7856)
- Pastawski et al., "Holographic quantum error-correcting codes," JHEP (2015). [arXiv:1503.06237](https://arxiv.org/abs/1503.06237)
- Casini, Galante, Myers, "Comments on Jacobson's entanglement equilibrium," JHEP (2016). [arXiv:1601.00528](https://arxiv.org/abs/1601.00528)

### Dimensional Reduction in Quantum Gravity
- Carlip, "Spontaneous Dimensional Reduction?" [arXiv:0909.3329](https://arxiv.org/abs/0909.3329) (2009)
- Carlip, "Dimension and Dimensional Reduction in Quantum Gravity," Universe 5(3), 83 (2019). [arXiv:1705.05417](https://arxiv.org/abs/1705.05417)
- Ambjorn, Jurkiewicz, Loll, "Spectral Dimension of the Universe," PRL 95, 171301 (2005). [arXiv:hep-th/0505113](https://arxiv.org/abs/hep-th/0505113)
- Lauscher, Reuter, "Fractal Spacetime Structure in Asymptotically Safe Gravity" (2005). [arXiv:hep-th/0508202](https://arxiv.org/abs/hep-th/0508202)
- Modesto, "Fractal Structure of Loop Quantum Gravity" (2009). [arXiv:0905.1665](https://arxiv.org/abs/0905.1665)

### Fisher Information and Geometry
- Braunstein, Caves, "Statistical Distance and the Geometry of Quantum States," PRL 72, 3439 (1994)
- Chentsov, "Statistical Decision Rules and Optimal Inference," AMS Translations (1982, original 1972)
- Ruppeiner, "Thermodynamic curvature and black holes." [arXiv:1309.0901](https://arxiv.org/abs/1309.0901)
- Bianconi, "Gravity from entropy," Phys. Rev. D 111, 066001 (2025). [arXiv:2408.14391](https://arxiv.org/abs/2408.14391)
- Machta, Chachra, Transtrum, Sethna, "Parameter space compression underlies emergent theories," Science 342, 604 (2013)
- Transtrum et al., "Sloppiness and Emergent Theories," J. Chem. Phys. 143, 010901 (2015). [arXiv:1501.07668](https://arxiv.org/abs/1501.07668)
- Reginatto, "Derivation of the equations of nonrelativistic quantum mechanics using the principle of minimum Fisher information," Phys. Rev. A 58, 1775 (1998)
- Caticha, "Entropic Dynamics," MDPI Entropy 17(9), 6110 (2015). [arXiv:1412.5629](https://arxiv.org/abs/1412.5629)

### Gravitational Critical Phenomena
- Choptuik, PRL 70, 9 (1993)
- Gundlach, "Critical Phenomena in Gravitational Collapse," Living Rev. Rel. 10, 5 (2007)
- Hawking, Page, Comm. Math. Phys. 87, 577 (1983)
- Kubiznak, Mann, "P-V criticality of charged AdS black holes," JHEP (2012). [arXiv:1205.0559](https://arxiv.org/abs/1205.0559)

### Cosmological Coupling (Contested)
- Farrah et al., "Observational Evidence for Cosmological Coupling of Black Holes," ApJ 944, L31 (2023). [arXiv:2302.07878](https://arxiv.org/abs/2302.07878)
- Croker et al., "DESI Dark Energy Time Evolution is Recovered by Cosmologically Coupled Black Holes" (2024). [arXiv:2405.12282](https://arxiv.org/abs/2405.12282)
- Amendola et al., "GW constraints on cosmological coupling," MNRAS 528, 2377 (2024)
- Cadoni et al., "Cosmological coupling of nonsingular black holes," JCAP (2023). [arXiv:2306.11588](https://arxiv.org/abs/2306.11588)

### Frieden (Historical — Failed Program)
- Frieden, "Physics from Fisher Information," Cambridge University Press (1998)
- Shalizi, review of Physics from Fisher Information. [bactra.org](https://bactra.org/reviews/physics-from-fisher-info/)

### SOC in Quantum Gravity
- Ansari, Smolin, "Self-organized criticality in quantum gravity" (2004). [arXiv:hep-th/0412307](https://arxiv.org/abs/hep-th/0412307)

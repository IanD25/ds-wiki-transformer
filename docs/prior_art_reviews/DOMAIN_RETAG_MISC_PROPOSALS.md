# Domain Retag — Chunk 6 (misc_entries) — Full Proposals

**Date:** 2026-04-18
**Scope:** 61 entries with single-letter / Ax / OmD / P_STATUS / Q prefixes

These are the legacy DS Wiki type-group entries. Many are **project-internal DFIG-framework constructs** (H-series mechanisms/parameters, M-series methods, T-series tests, X-series instantiations, G1 dimensional redshift, OmD operator, Ax1/Ax2 axioms). Some are named-science entries the framework references (A/B/C/D/E/F-series).

Every entry listed below has primary/secondary/auxiliary proposed. Skim for pushback.

After this batch is approved and applied, Chunk 7 (23 P-series conjectures) is the last pass.

---

## A-series (theorems — geometric scaling)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `A1` | Square-Cube Law | `mathematics.geometry_topology` | `physics.classical` | `biology.physiology` |
| `A2` | Richardson Effect (Fractal Measurement) | `mathematics.geometry_topology` | `networks_systems` | — |

## Ax-series + OmD (project axioms / postulates)

| ID | Title | Primary | Secondary | Aux | Notes |
|---|---|---|---|---|---|
| `Ax1` | Information Primacy | `information_theory` | `physics.modern` | — | project axiom: info-first ontology |
| `Ax2` | Effective Dimensionality ($D_\text{eff}$) | `information_theory` | `physics` | `mathematics.probability_measure` | project axiom: FIM-rank-as-dimension |
| `OmD` | $\Omega_D$: Dimensional Scaling Operator | `physics.cosmology` | `information_theory` | — | project postulate: ties to P3 |

## B-series (named physics laws)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `B1` | Radioactive Decay (Gamow Tunneling) | `physics.modern` | `chemistry` | — |
| `B2` | Arrhenius Equation | `chemistry.physical` | `physics.classical` | — |
| `B3` | Wien's Displacement Law | `physics.classical` | — | — |
| `B4` | Rayleigh Scattering | `physics.classical` | — | — |
| `B5` | Landauer's Principle | `information_theory` | `physics.classical` | — |

## C-series (scaling laws)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `C1` | Metabolic Scaling (Kleiber's Law) | `biology.physiology` | `networks_systems` | — |
| `C2` | Urban Scaling (Bettencourt-West) | `networks_systems` | `computer_science` | `biology.physiology` |
| `C3` | Heavy-Tailed Distributions (Unified) | `statistics_probability.stochastic_processes` | `networks_systems` | `mathematics.probability_measure` |

## D-series

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `D1` | Stevens' Power Law | `biology.neuroscience` | `statistics_probability` | — |
| `D2` | Feigenbaum Universality | `networks_systems.dynamical_systems` | `mathematics` | `physics.modern` |

## E-series (tech scaling)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `E1` | Moore's Law | `networks_systems` | `computer_science` | — |
| `E2` | Koomey's Law | `networks_systems` | `computer_science` | — |

## F-series (constraints)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `F1` | Ashby's Law of Requisite Variety | `information_theory` | `networks_systems` | — |
| `F2` | Liebig's Law of the Minimum | `biology.ecology` | — | — |
| `F3` | Gause's Competitive Exclusion Principle | `biology.ecology` | — | — |
| `F4` | Saturation Dynamics (Consolidated) | `biology` | `physics.modern` | `networks_systems` |
| `F5` | Oxygen Viability Corridor | `biology.physiology` | `earth_sciences` | — |

## G-series (derived gravitational/cosmological entries)

| ID | Title | Primary | Secondary | Aux | Notes |
|---|---|---|---|---|---|
| `G1` | Dimensional Redshift Law | `physics.cosmology` | `information_theory` | — | **project conjecture parallel to P1** |
| `G3` | Holographic Complexity Bound | `physics.cosmology` | `computer_science.complexity` | `information_theory` | **project conjecture parallel to P9** |

## H-series (DFIG mechanism + parameters — project constructs)

| ID | Title | Primary | Secondary | Aux | Notes |
|---|---|---|---|---|---|
| `H1` | Regime ($R_i$) | `information_theory` | `networks_systems` | `physics.modern`, `biology` | project mechanism; FIM-regime classifier |
| `H2` | Fractal Dimension ($d_f$) | `mathematics.geometry_topology` | `networks_systems` | `biology.physiology` | math concept with project extensions |
| `H3` | Phase Coherence ($\lambda$) | `information_theory` | `biology.physiology` | `physics.modern` | project parameter |
| `H4` | Topological Obstruction ($\chi_\text{eff}$) | `mathematics.geometry_topology` | `physics` | — | project parameter; effective Euler char |
| `H5` | Scaling Exponent $\beta(\lambda)$ | `networks_systems` | `biology.physiology`, `information_theory` | `physics.modern` | project-defined cross-domain β |

## M-series (methods)

| ID | Title | Primary | Secondary | Aux | Notes |
|---|---|---|---|---|---|
| `M1` | KKT Constraint Binding | `mathematics` | `statistics_probability.inference` | `computer_science` | convex optimization KKT is math |
| `M2` | OccBin Regime-Switching | `statistics_probability.inference` | `computer_science` | — | DSGE/economics technique |
| `M3` | Preisach Hysteresis Classification | `physics.classical` | `networks_systems` | — | |
| `M4` | Mori-Zwanzig Projection | `physics.modern.statistical_mechanics` | `mathematics` | — | |
| `M5` | Blanchard-Kahn Backward Induction | `statistics_probability.inference` | `mathematics` | `computer_science` | macro/DSGE method |
| `M6` | Fisher Information Rank | `information_theory` | `mathematics.probability_measure` | `statistics_probability` | core DFIG machinery |

## P_STATUS (conjecture-status meta-entries)

These inherit domains from their parent conjectures.

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `P2_STATUS` | P2 Validation Status | `biology.physiology` | `networks_systems`, `information_theory` | — |
| `P12_STATUS` | P12 Validation Status — β(λ) | `networks_systems` | `biology.physiology`, `information_theory` | — |

## Q-series (open questions)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `Q1` | Fractal Dimension from Power-Law Exponent | `mathematics.geometry_topology` | `networks_systems` | `statistics_probability` |
| `Q2` | Effective Poincaré-Hopf via Spectral Triples | `mathematics.geometry_topology` | `physics.modern` | — |
| `Q3` | Regime Capacity Bound | `biology.physiology` | `mathematics`, `information_theory` | — |
| `Q4` | SLT-Biology Correspondence | `computer_science.ml` | `biology.physiology` | `information_theory` |
| `Q5` | Information Cost of Synchronization | `information_theory` | `physics.modern` | `networks_systems` |

## T-series (methods/tests)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `T1` | Fisher Rank Monotonicity | `information_theory` | `mathematics` | — |
| `T2` | Metabolic Exponent–Dimensionality Correlation | `biology.physiology` | `information_theory` | — |
| `T3` | Ω_D Unit Consistency Audit | `physics` | `information_theory` | — |
| `T4` | Redshift–Structure Correlation | `physics.cosmology` | `information_theory` | — |
| `T5` | Critical Exponent–Dimension Sensitivity | `physics.modern.statistical_mechanics` | `information_theory` | — |
| `T6` | Holographic Reconstruction Complexity | `physics.cosmology` | `computer_science.complexity` | — |
| `T7` | Hadron Charge Radii / Effective ℏ | `physics.modern` | `information_theory` | — |
| `T8` | β(λ) Cross-Domain Universality Test | `networks_systems` | `biology.physiology`, `physics.modern` | `information_theory` |
| `T9` | Regime Capacity Bound Test | `biology.physiology` | `mathematics` | — |
| `T10` | RLCT-Biology Correspondence Test | `computer_science.ml` | `biology.physiology` | — |

## X-series (instantiations / applications)

| ID | Title | Primary | Secondary | Aux |
|---|---|---|---|---|
| `X0_FIM_Regimes` | Three Information-Geometric States | `information_theory` | `physics.modern.statistical_mechanics`, `networks_systems` | — |
| `X1` | Vascular/Metabolic — Regime-First | `biology.physiology` | `networks_systems` | `information_theory` |
| `X2` | Information Geometry — Regime-First | `information_theory` | `mathematics.geometry_topology` | — |
| `X3` | Statistical Physics — Regime-First | `physics.modern.statistical_mechanics` | `information_theory` | — |
| `X4` | Quantum Systems — Regime-First | `physics.modern` | `information_theory` | — |
| `X5` | Ecological Networks — Regime-First | `biology.ecology` | `networks_systems` | — |
| `X6` | Neural Networks — Regime-First | `biology.neuroscience` | `networks_systems`, `computer_science.ml` | — |
| `X7` | Developmental Biology — Regime-First | `biology` | `networks_systems` | — |
| `X8` | Financial Market Entropy Production | `statistics_probability` | `information_theory`, `physics.modern.statistical_mechanics` | — |

---

## Summary

**Total: 61 entries** — all with proposed tagging above.

### By primary top-level

| Top-level | Count |
|---|---|
| biology | 16 |
| physics | 12 |
| information_theory | 10 |
| mathematics | 6 |
| networks_systems | 5 |
| statistics_probability | 5 |
| computer_science | 2 |
| chemistry | 1 |
| earth_sciences | 0 |
| formal_logic | 0 |

### Flags worth your attention

1. **Project-internal construct entries** (H1, H3, H4, H5, OmD, G1, G3, Ax1, Ax2, M6, X0, T4, T7, T8, T9) — these are owner-derived DFIG-framework artifacts. They get primary tags reflecting their conceptual home, but many should also be flagged as `internal_construction` in the companion table. I'll do that as a follow-up pass unless you want it now.
2. **G1 Dimensional Redshift** and **G3 Holographic Complexity** — these look like the same conjectures as P1 and P9 respectively, with different IDs. Should they be consolidated? (Not a retag question; flagging for awareness.)
3. **X8 Financial Market Entropy Production** — AlphaEntropy-related; tagged `statistics_probability` primary. Could arguably be `physics.modern.statistical_mechanics` since the proxy is non-eq thermo. Judgment call.
4. **M1 KKT** — I put primary=`mathematics` (optimization is math), secondary=`statistics_probability.inference`. The entry's domain string said "information" — which I disagreed with. Flag for pushback.
5. **C1 Kleiber / P2_STATUS** — primary=`biology.physiology`. If we tag biology.physiology as home, then the WBE mathematics sub-tag (when it's later anchored) gets borrowed here.
6. **H-series parameters** — tagging each with primary informational/mathematical home. `H2 Fractal Dimension` gets mathematics.geometry_topology as home (math concept), even though it's used in biology + physics — those show up as secondaries.

### Review action

Scan the tables, flag any you want to amend. Default is "apply as shown."

### What this doesn't do yet

- Internal-construction flagging for project-internal entries (next pass)
- Borrowings table entries for H-series and X-series (where they legitimately cross domains) — these can be added as the borrowings table grows

# Domain Retagging — Chunk `misc_entries` — Proposals

**Date:** 2026-04-17
**Entries in chunk:** 61
- high confidence: 17
- medium confidence: 6
- low confidence: 38

## How to review

1. Skim the HIGH-confidence table first; flag any rows that look wrong
2. Deep-dive the MEDIUM and LOW confidence sections
3. For each flagged entry: amend the proposed primary/secondary/auxiliary inline OR
   tell Claude which row to fix
4. Once reviewed, Claude inserts approved rows into `wiki_history.db.entry_source_domains`

## High-confidence — auto-apply candidates

| ID | Title | Type | Current `domain` | Primary | Secondary | Auxiliary |
|---|---|---|---|---|---|---|
| `Ax1` | Ax1: Information Primacy | axiom | information | `information_theory` | — | — |
| `B3` | B3: Wien's Displacement Law | law | physics | `physics.classical` | — | — |
| `C1` | C1: Metabolic Scaling (Kleiber's Law) | law | biology | `biology.physiology` | — | — |
| `G1` | G1: Dimensional Redshift Law | law | cosmology | `physics.cosmology` | — | — |
| `G3` | G3: Holographic Complexity Bound | law | physics | `physics.modern` | — | — |
| `H2` | H2: Fractal Dimension ($d_f$) | parameter | geometry · biology · networks | `mathematics.geometry_topology` | biology, networks_systems | — |
| `M6` | M6: Fisher Information Rank | method | information | `information_theory` | — | — |
| `P2_STATUS` | P2 Validation Status: Metabolic Exponent Trac | open question | biology, scaling laws | `biology.physiology` | networks_systems | — |
| `Q1` | Q1: Fractal Dimension from Power-Law Exponent | open question | geometry · networks | `mathematics.geometry_topology` | networks_systems | — |
| `T2` | T2: Metabolic Exponent–Dimensionality Correla | method | biology | `biology.physiology` | — | — |
| `T4` | T4: Redshift–Structure Correlation | method | cosmology | `physics.cosmology` | — | — |
| `X0_FIM_Regimes` | X0: Three Information-Geometric States (FIM R | instantiation | information geometry, statistical physics, networks | `information_theory` | physics.modern.statistical_mechanics, networks_systems | — |
| `X1` | X1: Vascular/Metabolic — Regime-First Instant | instantiation | biology | `biology.physiology` | — | — |
| `X2` | X2: Information Geometry — Regime-First Insta | instantiation | information | `information_theory` | — | — |
| `X4` | X4: Quantum Systems — Regime-First Instantiat | instantiation | physics | `physics.modern` | — | — |
| `X6` | X6: Neural Networks — Regime-First Instantiat | instantiation | biology | `biology` | — | — |
| `X8` | X8: Financial Market Entropy Production Proxy | instantiation | information geometry, finance, non-equilibrium thermodynamics | `information_theory` | statistics_probability, physics.modern.statistical_mechanics | — |

## Medium-confidence — owner review

### `A2` — A2: Richardson Effect (Fractal Measurement)
- Type: theorem
- Current `domain`: `geometry`
- **Proposed primary:** `networks_systems`
- Proposed secondary: ['mathematics.geometry_topology']
- Rationale: Primary = networks_systems (via networks_systems, 1/2 signals agree) |   domain string -> ['mathematics.geometry_topology'] |   top keyword match -> networks_systems (score=1)
- Flags: ['partial-disagreement: domain_string=mathematics.geometry_topology']

### `Ax2` — Ax2: Effective Dimensionality ($D_{\text{eff}}$)
- Type: axiom
- Current `domain`: `physics`
- **Proposed primary:** `networks_systems`
- Proposed secondary: ['physics']
- Rationale: Primary = networks_systems (via networks_systems, 1/2 signals agree) |   domain string -> ['physics'] |   top keyword match -> networks_systems (score=1)
- Flags: ['partial-disagreement: domain_string=physics']

### `B2` — B2: Arrhenius Equation
- Type: law
- Current `domain`: `physics`
- **Proposed primary:** `chemistry`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry (via chemistry, 1/2 signals agree) |   domain string -> ['physics'] |   top keyword match -> chemistry (score=1)
- Flags: ['partial-disagreement: domain_string=physics']

### `D1` — D1: Stevens' Power Law
- Type: law
- Current `domain`: `biology`
- **Proposed primary:** `networks_systems`
- Proposed secondary: ['biology']
- Rationale: Primary = networks_systems (via networks_systems, 1/2 signals agree) |   domain string -> ['biology'] |   top keyword match -> networks_systems (score=1)
- Flags: ['partial-disagreement: domain_string=biology']

### `Q5` — Q5: Information Cost of Synchronization
- Type: open question
- Current `domain`: `physics · information`
- **Proposed primary:** `information_theory`
- Proposed secondary: ['physics']
- Rationale: Primary = information_theory (via information_theory, 1/2 signals agree) |   domain string -> ['physics', 'information_theory'] |   top keyword match -> information_theory (score=1)
- Flags: ['partial-disagreement: domain_string=physics']

### `T6` — T6: Holographic Reconstruction Complexity
- Type: method
- Current `domain`: `physics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['physics']
- Rationale: Primary = computer_science (via computer_science, 1/2 signals agree) |   domain string -> ['physics'] |   top keyword match -> computer_science (score=1)
- Flags: ['partial-disagreement: domain_string=physics']


## Low-confidence — mandatory owner review

### `A1` — A1: Square-Cube Law
- Type: theorem
- Current `domain`: `geometry`
- **Proposed primary:** `mathematics.geometry_topology`
- Rationale: Primary = mathematics.geometry_topology (via mathematics, 1/1 signals agree) |   domain string -> ['mathematics.geometry_topology']
- Flags: ["all-signals-disagree: [('domain_string', 'mathematics.geometry_topology')]"]
- Signals: {'prefix': None, 'domain_string': ['mathematics.geometry_topology'], 'keywords': {}, 'top_keyword_tag': None}

### `B1` — B1: Radioactive Decay (Gamow Tunneling)
- Type: law
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `B4` — B4: Rayleigh Scattering
- Type: law
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `B5` — B5: Landauer's Principle
- Type: law
- Current `domain`: `information`
- **Proposed primary:** `information_theory`
- Rationale: Primary = information_theory (via information_theory, 1/1 signals agree) |   domain string -> ['information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'information_theory')]"]
- Signals: {'prefix': None, 'domain_string': ['information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `C2` — C2: Urban Scaling (Bettencourt-West)
- Type: law
- Current `domain`: `networks`
- **Proposed primary:** `networks_systems`
- Rationale: Primary = networks_systems (via networks_systems, 1/1 signals agree) |   domain string -> ['networks_systems']
- Flags: ["all-signals-disagree: [('domain_string', 'networks_systems')]"]
- Signals: {'prefix': None, 'domain_string': ['networks_systems'], 'keywords': {}, 'top_keyword_tag': None}

### `C3` — C3: Heavy-Tailed Distributions (Unified)
- Type: law
- Current `domain`: `networks`
- **Proposed primary:** `networks_systems`
- Rationale: Primary = networks_systems (via networks_systems, 1/1 signals agree) |   domain string -> ['networks_systems']
- Flags: ["all-signals-disagree: [('domain_string', 'networks_systems')]"]
- Signals: {'prefix': None, 'domain_string': ['networks_systems'], 'keywords': {}, 'top_keyword_tag': None}

### `D2` — D2: Feigenbaum Universality
- Type: law
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `E1` — E1: Moore's Law
- Type: law
- Current `domain`: `networks`
- **Proposed primary:** `networks_systems`
- Rationale: Primary = networks_systems (via networks_systems, 1/1 signals agree) |   domain string -> ['networks_systems']
- Flags: ["all-signals-disagree: [('domain_string', 'networks_systems')]"]
- Signals: {'prefix': None, 'domain_string': ['networks_systems'], 'keywords': {}, 'top_keyword_tag': None}

### `E2` — E2: Koomey's Law
- Type: law
- Current `domain`: `networks`
- **Proposed primary:** `networks_systems`
- Rationale: Primary = networks_systems (via networks_systems, 1/1 signals agree) |   domain string -> ['networks_systems']
- Flags: ["all-signals-disagree: [('domain_string', 'networks_systems')]"]
- Signals: {'prefix': None, 'domain_string': ['networks_systems'], 'keywords': {}, 'top_keyword_tag': None}

### `F1` — F1: Ashby's Law of Requisite Variety
- Type: constraint
- Current `domain`: `information`
- **Proposed primary:** `information_theory`
- Rationale: Primary = information_theory (via information_theory, 1/1 signals agree) |   domain string -> ['information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'information_theory')]"]
- Signals: {'prefix': None, 'domain_string': ['information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `F2` — F2: Liebig's Law of the Minimum
- Type: constraint
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `F3` — F3: Gause's Competitive Exclusion Principle
- Type: constraint
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `F4` — F4: Saturation Dynamics (Consolidated)
- Type: constraint
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `F5` — F5: Oxygen Viability Corridor
- Type: constraint
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `H1` — H1: Regime ($R_i$)
- Type: mechanism
- Current `domain`: `physics · biology · networks`
- **Proposed primary:** `physics`
- Proposed secondary: ['biology', 'networks_systems']
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics', 'biology', 'networks_systems']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics', 'biology', 'networks_systems'], 'keywords': {}, 'top_keyword_tag': None}

### `H3` — H3: Phase Coherence ($\lambda$)
- Type: parameter
- Current `domain`: `biology · physics · information`
- **Proposed primary:** `biology`
- Proposed secondary: ['information_theory', 'physics']
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology', 'physics', 'information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology', 'physics', 'information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `H4` — H4: Topological Obstruction ($\chi_{\text{eff}}$)
- Type: parameter
- Current `domain`: `geometry · physics`
- **Proposed primary:** `mathematics.geometry_topology`
- Proposed secondary: ['physics']
- Rationale: Primary = mathematics.geometry_topology (via mathematics, 1/1 signals agree) |   domain string -> ['mathematics.geometry_topology', 'physics']
- Flags: ["all-signals-disagree: [('domain_string', 'mathematics.geometry_topology')]"]
- Signals: {'prefix': None, 'domain_string': ['mathematics.geometry_topology', 'physics'], 'keywords': {}, 'top_keyword_tag': None}

### `H5` — H5: Scaling Exponent $\beta(\lambda)$
- Type: law
- Current `domain`: `biology · physics · networks · information`
- **Proposed primary:** `biology`
- Proposed secondary: ['information_theory', 'physics']
- Proposed auxiliary: ['networks_systems']
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology', 'physics', 'networks_systems', 'information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology', 'physics', 'networks_systems', 'information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `M1` — M1: KKT Constraint Binding
- Type: method
- Current `domain`: `information`
- **Proposed primary:** `information_theory`
- Rationale: Primary = information_theory (via information_theory, 1/1 signals agree) |   domain string -> ['information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'information_theory')]"]
- Signals: {'prefix': None, 'domain_string': ['information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `M2` — M2: OccBin Regime-Switching
- Type: method
- Current `domain`: `information`
- **Proposed primary:** `information_theory`
- Rationale: Primary = information_theory (via information_theory, 1/1 signals agree) |   domain string -> ['information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'information_theory')]"]
- Signals: {'prefix': None, 'domain_string': ['information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `M3` — M3: Preisach Hysteresis Classification
- Type: method
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `M4` — M4: Mori-Zwanzig Projection
- Type: method
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `M5` — M5: Blanchard-Kahn Backward Induction
- Type: method
- Current `domain`: `information`
- **Proposed primary:** `information_theory`
- Rationale: Primary = information_theory (via information_theory, 1/1 signals agree) |   domain string -> ['information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'information_theory')]"]
- Signals: {'prefix': None, 'domain_string': ['information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `OmD` — Ω_D: Dimensional Scaling Operator
- Type: axiom
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `P12_STATUS` — P12 Validation Status: β(λ) Formula Across Domains
- Type: open question
- Current `domain`: `scaling laws, fractals, networks`
- **Proposed primary:** `networks_systems`
- Proposed secondary: ['mathematics.geometry_topology']
- Rationale: Primary = networks_systems (via networks_systems, 1/1 signals agree) |   domain string -> ['networks_systems', 'mathematics.geometry_topology']
- Flags: ["all-signals-disagree: [('domain_string', 'networks_systems')]"]
- Signals: {'prefix': None, 'domain_string': ['networks_systems', 'mathematics.geometry_topology'], 'keywords': {}, 'top_keyword_tag': None}

### `Q2` — Q2: Effective Poincaré-Hopf via Spectral Triples
- Type: open question
- Current `domain`: `geometry · physics`
- **Proposed primary:** `mathematics.geometry_topology`
- Proposed secondary: ['physics']
- Rationale: Primary = mathematics.geometry_topology (via mathematics, 1/1 signals agree) |   domain string -> ['mathematics.geometry_topology', 'physics']
- Flags: ["all-signals-disagree: [('domain_string', 'mathematics.geometry_topology')]"]
- Signals: {'prefix': None, 'domain_string': ['mathematics.geometry_topology', 'physics'], 'keywords': {}, 'top_keyword_tag': None}

### `Q3` — Q3: Regime Capacity Bound
- Type: open question
- Current `domain`: `geometry · biology`
- **Proposed primary:** `mathematics.geometry_topology`
- Proposed secondary: ['biology']
- Rationale: Primary = mathematics.geometry_topology (via mathematics, 1/1 signals agree) |   domain string -> ['mathematics.geometry_topology', 'biology']
- Flags: ["all-signals-disagree: [('domain_string', 'mathematics.geometry_topology')]"]
- Signals: {'prefix': None, 'domain_string': ['mathematics.geometry_topology', 'biology'], 'keywords': {}, 'top_keyword_tag': None}

### `Q4` — Q4: SLT-Biology Correspondence
- Type: open question
- Current `domain`: `biology · information`
- **Proposed primary:** `biology`
- Proposed secondary: ['information_theory']
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology', 'information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology', 'information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `T1` — T1: Fisher Rank Monotonicity
- Type: method
- Current `domain`: `information`
- **Proposed primary:** `information_theory`
- Rationale: Primary = information_theory (via information_theory, 1/1 signals agree) |   domain string -> ['information_theory']
- Flags: ["all-signals-disagree: [('domain_string', 'information_theory')]"]
- Signals: {'prefix': None, 'domain_string': ['information_theory'], 'keywords': {}, 'top_keyword_tag': None}

### `T10` — T10: RLCT-Biology Correspondence Test
- Type: method
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `T3` — T3: Ω_D Unit Consistency Audit
- Type: method
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `T5` — T5: Critical Exponent–Dimension Sensitivity
- Type: method
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `T7` — T7: Hadron Charge Radii / Effective ℏ
- Type: method
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `T8` — T8: β(λ) Cross-Domain Universality Test
- Type: method
- Current `domain`: `physics · biology`
- **Proposed primary:** `physics`
- Proposed secondary: ['biology']
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics', 'biology']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics', 'biology'], 'keywords': {}, 'top_keyword_tag': None}

### `T9` — T9: Regime Capacity Bound Test
- Type: method
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `X3` — X3: Statistical Physics — Regime-First Instantiation
- Type: instantiation
- Current `domain`: `physics`
- **Proposed primary:** `physics`
- Rationale: Primary = physics (via physics, 1/1 signals agree) |   domain string -> ['physics']
- Flags: ["all-signals-disagree: [('domain_string', 'physics')]"]
- Signals: {'prefix': None, 'domain_string': ['physics'], 'keywords': {}, 'top_keyword_tag': None}

### `X5` — X5: Ecological Networks — Regime-First Instantiation
- Type: instantiation
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}

### `X7` — X7: Developmental Biology — Regime-First Instantiation
- Type: instantiation
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 1/1 signals agree) |   domain string -> ['biology']
- Flags: ["all-signals-disagree: [('domain_string', 'biology')]"]
- Signals: {'prefix': None, 'domain_string': ['biology'], 'keywords': {}, 'top_keyword_tag': None}


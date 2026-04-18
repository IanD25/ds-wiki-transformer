# Domain Retagging — Smoke Test Report

**Date:** 2026-04-17
**Scope:** 20 entries (target 20; missing [])
**Total wall time (script only):** 0.00s

## Summary

- high confidence: 15
- medium confidence: 5
- low confidence: 0
- missing entries: 0

## Hierarchy (foundation-first)

1. `formal_logic`
2. `mathematics`
3. `information_theory`
4. `statistics_probability`
5. `computer_science`
6. `physics`
7. `chemistry`
8. `biology`
9. `earth_sciences`
10. `networks_systems`

## Per-entry proposals

| ID | Type | Current `domain` | Primary | Secondary | Auxiliary | Conf | Flags |
|---|---|---|---|---|---|---|---|
| `Ax1` | axiom | information | `information_theory` | — | — | medium | primary-via-hierarchy-fallback (ID prefix non-deterministic) |
| `BIO1` | reference_law | biology | `biology` | — | — | high | — |
| `CHEM1` | reference_law | chemistry · physics | `chemistry` | physics | — | high | — |
| `CM1` | reference_law | physics | `physics.classical` | — | — | high | — |
| `CS1` | reference_law | computer science · mathematics | `computer_science` | mathematics | — | high | — |
| `ES1` | reference_law | earth sciences · networks | `earth_sciences` | networks_systems | — | high | — |
| `FL1` | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — | high | — |
| `GT01` | reference_law | physics · information | `physics.cosmology` | information_theory | — | high | — |
| `GV1` | reference_law | physics · cosmology | `physics.cosmology` | — | — | high | — |
| `INFO1` | reference_law | information · mathematics | `information_theory` | mathematics | — | high | — |
| `IT02` | reference_law | information · physics | `information_theory` | physics | — | high | — |
| `M1` | method | information | `information_theory` | — | — | medium | primary-via-hierarchy-fallback (ID prefix non-deterministic) |
| `MATH1` | reference_law | mathematics · information | `mathematics` | information_theory | — | high | — |
| `MATH5` | reference_law | mathematics · physics | `mathematics` | physics | — | high | — |
| `NE01` | reference_law | physics · chemistry · biology | `biology.neuroscience` | physics, chemistry | — | high | — |
| `P2_STATUS` | open question | biology, scaling laws | `biology` | networks_systems | — | medium | primary-via-hierarchy-fallback (ID prefix non-deterministic) |
| `Q1` | open question | geometry · networks | `mathematics.geometry_topology` | networks_systems | — | medium | primary-via-hierarchy-fallback (ID prefix non-deterministic) |
| `QM1` | reference_law | physics | `physics.modern` | — | — | high | — |
| `STAT1` | reference_law | information · mathematics · physics | `statistics_probability` | mathematics, information_theory | physics | medium | prefix-tag-top (statistics_probability) not in domain string |
| `TD6` | reference_law | physics | `physics.classical` | — | — | high | — |

## Per-entry rationale

### `Ax1` — Ax1: Information Primacy
- Current `domain`: `information`
- ID prefix: `Ax` -> `None`
- Tags from string: ['information_theory']
- Proposed primary: `information_theory`
- Confidence: medium
- Rationale: ID prefix 'Ax' is non-deterministic. Primary = most foundational tag in string per hierarchy: information_theory.
- Flags: ['primary-via-hierarchy-fallback (ID prefix non-deterministic)']

### `BIO1` — Mendelian Laws of Inheritance
- Current `domain`: `biology`
- ID prefix: `BIO` -> `biology`
- Tags from string: ['biology']
- Proposed primary: `biology`
- Confidence: high
- Rationale: Primary via ID prefix 'BIO' -> biology.

### `CHEM1` — Periodic Law
- Current `domain`: `chemistry · physics`
- ID prefix: `CHEM` -> `chemistry`
- Tags from string: ['chemistry', 'physics']
- Proposed primary: `chemistry`
- Proposed secondary: ['physics']
- Confidence: high
- Rationale: Primary via ID prefix 'CHEM' -> chemistry.

### `CM1` — Newton's Laws of Motion
- Current `domain`: `physics`
- ID prefix: `CM` -> `physics.classical`
- Tags from string: ['physics']
- Proposed primary: `physics.classical`
- Confidence: high
- Rationale: Primary via ID prefix 'CM' -> physics.classical.

### `CS1` — Church-Turing Thesis
- Current `domain`: `computer science · mathematics`
- ID prefix: `CS` -> `computer_science`
- Tags from string: ['computer_science', 'mathematics']
- Proposed primary: `computer_science`
- Proposed secondary: ['mathematics']
- Confidence: high
- Rationale: Primary via ID prefix 'CS' -> computer_science.

### `ES1` — Tobler's First Law of Geography
- Current `domain`: `earth sciences · networks`
- ID prefix: `ES` -> `earth_sciences`
- Tags from string: ['earth_sciences', 'networks_systems']
- Proposed primary: `earth_sciences`
- Proposed secondary: ['networks_systems']
- Confidence: high
- Rationale: Primary via ID prefix 'ES' -> earth_sciences.

### `FL1` — Deductive Validity
- Current `domain`: `formal logic · mathematics`
- ID prefix: `FL` -> `formal_logic`
- Tags from string: ['formal_logic', 'mathematics']
- Proposed primary: `formal_logic`
- Proposed secondary: ['mathematics']
- Confidence: high
- Rationale: Primary via ID prefix 'FL' -> formal_logic.

### `GT01` — Jacobson's Thermodynamic Derivation of Einstein Equations
- Current `domain`: `physics · information`
- ID prefix: `GT` -> `physics.cosmology`
- Tags from string: ['physics', 'information_theory']
- Proposed primary: `physics.cosmology`
- Proposed secondary: ['information_theory']
- Confidence: high
- Rationale: Primary via ID prefix 'GT' -> physics.cosmology.

### `GV1` — General Relativity — Einstein Field Equations
- Current `domain`: `physics · cosmology`
- ID prefix: `GV` -> `physics.cosmology`
- Tags from string: ['physics.cosmology']
- Proposed primary: `physics.cosmology`
- Confidence: high
- Rationale: Primary via ID prefix 'GV' -> physics.cosmology.

### `INFO1` — Shannon Entropy
- Current `domain`: `information · mathematics`
- ID prefix: `INFO` -> `information_theory`
- Tags from string: ['information_theory', 'mathematics']
- Proposed primary: `information_theory`
- Proposed secondary: ['mathematics']
- Confidence: high
- Rationale: Primary via ID prefix 'INFO' -> information_theory.

### `IT02` — Von Neumann Entropy
- Current `domain`: `information · physics`
- ID prefix: `IT` -> `information_theory`
- Tags from string: ['information_theory', 'physics']
- Proposed primary: `information_theory`
- Proposed secondary: ['physics']
- Confidence: high
- Rationale: Primary via ID prefix 'IT' -> information_theory.

### `M1` — M1: KKT Constraint Binding
- Current `domain`: `information`
- ID prefix: `M` -> `None`
- Tags from string: ['information_theory']
- Proposed primary: `information_theory`
- Confidence: medium
- Rationale: ID prefix 'M' is non-deterministic. Primary = most foundational tag in string per hierarchy: information_theory.
- Flags: ['primary-via-hierarchy-fallback (ID prefix non-deterministic)']

### `MATH1` — Bayes' Theorem
- Current `domain`: `mathematics · information`
- ID prefix: `MATH` -> `mathematics`
- Tags from string: ['mathematics', 'information_theory']
- Proposed primary: `mathematics`
- Proposed secondary: ['information_theory']
- Confidence: high
- Rationale: Primary via ID prefix 'MATH' -> mathematics.

### `MATH5` — Fundamental Theorem of Calculus
- Current `domain`: `mathematics · physics`
- ID prefix: `MATH` -> `mathematics`
- Tags from string: ['mathematics', 'physics']
- Proposed primary: `mathematics`
- Proposed secondary: ['physics']
- Confidence: high
- Rationale: Primary via ID prefix 'MATH' -> mathematics.

### `NE01` — Prigogine Dissipative Structures
- Current `domain`: `physics · chemistry · biology`
- ID prefix: `NE` -> `biology.neuroscience`
- Tags from string: ['physics', 'chemistry', 'biology']
- Proposed primary: `biology.neuroscience`
- Proposed secondary: ['physics', 'chemistry']
- Confidence: high
- Rationale: Primary via ID prefix 'NE' -> biology.neuroscience.

### `P2_STATUS` — P2 Validation Status: Metabolic Exponent Tracks Vascular D_eff
- Current `domain`: `biology, scaling laws`
- ID prefix: `P` -> `None`
- Tags from string: ['biology', 'networks_systems']
- Proposed primary: `biology`
- Proposed secondary: ['networks_systems']
- Confidence: medium
- Rationale: ID prefix 'P' is non-deterministic. Primary = most foundational tag in string per hierarchy: biology.
- Flags: ['primary-via-hierarchy-fallback (ID prefix non-deterministic)']

### `Q1` — Q1: Fractal Dimension from Power-Law Exponent
- Current `domain`: `geometry · networks`
- ID prefix: `Q` -> `None`
- Tags from string: ['mathematics.geometry_topology', 'networks_systems']
- Proposed primary: `mathematics.geometry_topology`
- Proposed secondary: ['networks_systems']
- Confidence: medium
- Rationale: ID prefix 'Q' is non-deterministic. Primary = most foundational tag in string per hierarchy: mathematics.geometry_topology.
- Flags: ['primary-via-hierarchy-fallback (ID prefix non-deterministic)']

### `QM1` — Schrödinger Equation
- Current `domain`: `physics`
- ID prefix: `QM` -> `physics.modern`
- Tags from string: ['physics']
- Proposed primary: `physics.modern`
- Confidence: high
- Rationale: Primary via ID prefix 'QM' -> physics.modern.

### `STAT1` — Maximum Entropy Principle
- Current `domain`: `information · mathematics · physics`
- ID prefix: `STAT` -> `statistics_probability`
- Tags from string: ['information_theory', 'mathematics', 'physics']
- Proposed primary: `statistics_probability`
- Proposed secondary: ['mathematics', 'information_theory']
- Proposed auxiliary: ['physics']
- Confidence: medium
- Rationale: Primary via ID prefix 'STAT' -> statistics_probability. Domain string top-level(s) ['information_theory', 'mathematics', 'physics'] differ from prefix-derived top-level 'statistics_probability'.
- Flags: ['prefix-tag-top (statistics_probability) not in domain string']

### `TD6` — Onsager Reciprocal Relations
- Current `domain`: `physics`
- ID prefix: `TD` -> `physics.classical`
- Tags from string: ['physics']
- Proposed primary: `physics.classical`
- Confidence: high
- Rationale: Primary via ID prefix 'TD' -> physics.classical.

## Timing projection for full 278-entry pass

- Average script time per entry: 0.0 ms
- Projected script time for 278 entries: 0.00 seconds
- **Script time is negligible.** Bottleneck is owner review of medium/low-confidence cases.
- Smoke test produced 5 medium+low confidence cases out of 20 (25%).
- Extrapolated review burden for 278 entries: ~69 cases needing manual review.

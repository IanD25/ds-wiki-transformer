# Domain Retagging — Chunk `info_stat_cs` — Proposals

**Date:** 2026-04-17
**Entries in chunk:** 29
- high confidence: 13
- medium confidence: 14
- low confidence: 2

## How to review

1. Skim the HIGH-confidence table first; flag any rows that look wrong
2. Deep-dive the MEDIUM and LOW confidence sections
3. For each flagged entry: amend the proposed primary/secondary/auxiliary inline OR
   tell Claude which row to fix
4. Once reviewed, Claude inserts approved rows into `wiki_history.db.entry_source_domains`

## High-confidence — auto-apply candidates

| ID | Title | Type | Current `domain` | Primary | Secondary | Auxiliary |
|---|---|---|---|---|---|---|
| `CS12` | FLP Impossibility Theorem | reference_law | computer science | `computer_science` | — | — |
| `CS14` | Byzantine Fault Tolerance | reference_law | computer science | `computer_science` | — | — |
| `CS2` | Halting Problem — Turing Undecidability | reference_law | computer science · mathematics | `computer_science` | mathematics | — |
| `CS7` | CAP Theorem | reference_law | computer science | `computer_science` | — | — |
| `CS8` | Amdahl's Law | reference_law | computer science | `computer_science` | — | — |
| `CS9` | Little's Law | reference_law | computer science · mathematics | `computer_science` | mathematics | — |
| `INFO1` | Shannon Entropy | reference_law | information · mathematics | `information_theory` | mathematics | — |
| `INFO2` | Shannon Source Coding Theorem | reference_law | information · mathematics | `information_theory` | mathematics | — |
| `INFO3` | Shannon Noisy-Channel Coding Theorem | reference_law | information · mathematics · physics | `information_theory` | mathematics, physics | — |
| `INFO4` | Mutual Information and Data Processing Inequa | reference_law | information · mathematics | `information_theory` | mathematics | — |
| `INFO5` | Kolmogorov Complexity | reference_law | information · mathematics | `information_theory` | mathematics | — |
| `IT03` | Kullback-Leibler Divergence | reference_law | information · mathematics | `information_theory` | mathematics | — |
| `IT04` | Quantum Relative Entropy | reference_law | information · physics | `information_theory` | physics | — |

## Medium-confidence — owner review

### `CS1` — Church-Turing Thesis
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> mathematics (score=2)
- Flags: ['partial-disagreement: keywords=mathematics']

### `CS10` — No Free Lunch Theorem
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `CS11` — Comparison Sort Lower Bound — Ω(n log n)
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> information_theory (score=1)
- Flags: ['partial-disagreement: keywords=information_theory']

### `CS13` — Perron-Frobenius Theorem
- Type: reference_law
- Current `domain`: `mathematics · computer science`
- **Proposed primary:** `mathematics`
- Proposed secondary: ['computer_science']
- Rationale: Primary = mathematics (via mathematics, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['mathematics', 'computer_science'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: prefix=computer_science']

### `CS15` — Time Hierarchy Theorem
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `CS3` — Rice's Theorem
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `CS4` — Cook-Levin Theorem — NP-Completeness
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `CS5` — Master Theorem — Divide and Conquer Recurrences
- Type: reference_law
- Current `domain`: `computer science · mathematics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['mathematics']
- Rationale: Primary = computer_science (via computer_science, 2/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['computer_science', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `IT02` — Von Neumann Entropy
- Type: reference_law
- Current `domain`: `information · physics`
- **Proposed primary:** `information_theory`
- Proposed secondary: ['physics']
- Rationale: Primary = information_theory (via information_theory, 2/3 signals agree) |   prefix hint 'IT' -> information_theory |   domain string -> ['information_theory', 'physics'] |   top keyword match -> physics.cosmology (score=4)
- Flags: ['partial-disagreement: keywords=physics.cosmology']

### `IT05` — Fisher Information
- Type: reference_law
- Current `domain`: `information · mathematics`
- **Proposed primary:** `information_theory`
- Proposed secondary: ['mathematics']
- Rationale: Primary = information_theory (via information_theory, 2/3 signals agree) |   prefix hint 'IT' -> information_theory |   domain string -> ['information_theory', 'mathematics'] |   top keyword match -> mathematics.geometry_topology (score=3)
- Flags: ['partial-disagreement: keywords=mathematics.geometry_topology']

### `IT06` — IT06: Seifert Stochastic Thermodynamics
- Type: reference_law
- Current `domain`: `information · physics`
- **Proposed primary:** `information_theory`
- Proposed secondary: ['physics']
- Rationale: Primary = information_theory (via information_theory, 2/3 signals agree) |   prefix hint 'IT' -> information_theory |   domain string -> ['information_theory', 'physics'] |   top keyword match -> physics.modern (score=6)
- Flags: ['partial-disagreement: keywords=physics.modern']

### `IT08` — Fisher-Rao Metric
- Type: reference_law
- Current `domain`: `information · mathematics`
- **Proposed primary:** `information_theory`
- Proposed secondary: ['mathematics']
- Rationale: Primary = information_theory (via information_theory, 2/3 signals agree) |   prefix hint 'IT' -> information_theory |   domain string -> ['information_theory', 'mathematics'] |   top keyword match -> mathematics.geometry_topology (score=3)
- Flags: ['partial-disagreement: keywords=mathematics.geometry_topology']

### `STAT1` — Maximum Entropy Principle
- Type: reference_law
- Current `domain`: `information · mathematics · physics`
- **Proposed primary:** `information_theory`
- Proposed secondary: ['mathematics', 'physics']
- Rationale: Primary = information_theory (via information_theory, 2/3 signals agree) |   prefix hint 'STAT' -> statistics_probability |   domain string -> ['information_theory', 'mathematics', 'physics'] |   top keyword match -> information_theory (score=3)
- Flags: ['partial-disagreement: prefix=statistics_probability']

### `STAT3` — STAT3: Constrained Critical Attractor (CCA) Class
- Type: reference_law
- Current `domain`: `mathematics · physics`
- **Proposed primary:** `mathematics`
- Proposed secondary: ['physics']
- Rationale: Primary = mathematics (via mathematics, 2/3 signals agree) |   prefix hint 'STAT' -> statistics_probability |   domain string -> ['mathematics', 'physics'] |   top keyword match -> mathematics (score=2)
- Flags: ['partial-disagreement: prefix=statistics_probability']


## Low-confidence — mandatory owner review

### `CS6` — Nyquist-Shannon Sampling Theorem
- Type: reference_law
- Current `domain`: `information · physics`
- **Proposed primary:** `computer_science`
- Proposed secondary: ['information_theory', 'physics']
- Rationale: Primary = computer_science (via computer_science, 1/3 signals agree) |   prefix hint 'CS' -> computer_science |   domain string -> ['information_theory', 'physics'] |   top keyword match -> mathematics (score=1)
- Flags: ["all-signals-disagree: [('prefix', 'computer_science'), ('keywords', 'mathematics'), ('domain_string', 'information_theory')]"]
- Signals: {'prefix': 'computer_science', 'domain_string': ['information_theory', 'physics'], 'keywords': {'mathematics': 1, 'information_theory': 1}, 'top_keyword_tag': 'mathematics'}

### `STAT2` — Ergodic Theorem
- Type: reference_law
- Current `domain`: `mathematics · physics`
- **Proposed primary:** `statistics_probability`
- Proposed secondary: ['mathematics', 'physics']
- Rationale: Primary = statistics_probability (via statistics_probability, 1/3 signals agree) |   prefix hint 'STAT' -> statistics_probability |   domain string -> ['mathematics', 'physics'] |   top keyword match -> physics.modern (score=2)
- Flags: ["all-signals-disagree: [('prefix', 'statistics_probability'), ('keywords', 'physics.modern'), ('domain_string', 'mathematics')]"]
- Signals: {'prefix': 'statistics_probability', 'domain_string': ['mathematics', 'physics'], 'keywords': {'physics.modern': 2, 'mathematics': 1}, 'top_keyword_tag': 'physics.modern'}


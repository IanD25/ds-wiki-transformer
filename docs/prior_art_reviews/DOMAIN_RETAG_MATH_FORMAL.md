# Domain Retagging — Chunk `math_formal` — Proposals

**Date:** 2026-04-17
**Entries in chunk:** 30
- high confidence: 20
- medium confidence: 10
- low confidence: 0

## How to review

1. Skim the HIGH-confidence table first; flag any rows that look wrong
2. Deep-dive the MEDIUM and LOW confidence sections
3. For each flagged entry: amend the proposed primary/secondary/auxiliary inline OR
   tell Claude which row to fix
4. Once reviewed, Claude inserts approved rows into `wiki_history.db.entry_source_domains`

## High-confidence — auto-apply candidates

| ID | Title | Type | Current `domain` | Primary | Secondary | Auxiliary |
|---|---|---|---|---|---|---|
| `FL1` | Deductive Validity | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL13` | Modus Ponens and Core Inference Rules | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL16` | Quantificational Logic (First-Order) | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL17` | QL Translation and Scope | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL18` | Quantifier Inference Rules | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL19` | The Empty Domain Problem | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL2` | Soundness of Arguments | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL20` | QL Semantics and Validity | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL21` | Identity, Descriptions, and Functions | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL22` | Intuitionistic and Non-Classical Logics | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL3` | Logical Form and Topic Neutrality | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL4` | The Counterexample Method | method | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL6` | Truth-Functionality and Valuations | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL7` | Expressive Adequacy | theorem | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL8` | Tautology and Contradiction | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `FL9` | Tautological Entailment | reference_law | formal logic · mathematics | `formal_logic` | mathematics | — |
| `MATH2` | Central Limit Theorem | reference_law | mathematics · physics | `mathematics` | physics | — |
| `MATH5` | Fundamental Theorem of Calculus | reference_law | mathematics · physics | `mathematics` | physics | — |
| `MATH6` | Prime Number Theorem | reference_law | mathematics | `mathematics` | — | — |
| `MATH8` | Generalized Stokes' Theorem | reference_law | mathematics · physics | `mathematics` | physics | — |

## Medium-confidence — owner review

### `FL10` — The Material Conditional
- Type: reference_law
- Current `domain`: `formal logic · mathematics`
- **Proposed primary:** `formal_logic`
- Proposed secondary: ['mathematics']
- Rationale: Primary = formal_logic (via formal_logic, 2/3 signals agree) |   prefix hint 'FL' -> formal_logic |   domain string -> ['formal_logic', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `FL11` — Explosion and Absurdity (Ex Falso Quodlibet)
- Type: reference_law
- Current `domain`: `formal logic · mathematics`
- **Proposed primary:** `formal_logic`
- Proposed secondary: ['mathematics']
- Rationale: Primary = formal_logic (via formal_logic, 2/3 signals agree) |   prefix hint 'FL' -> formal_logic |   domain string -> ['formal_logic', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `FL12` — Natural Deduction (Fitch System)
- Type: method
- Current `domain`: `formal logic · mathematics`
- **Proposed primary:** `formal_logic`
- Proposed secondary: ['mathematics']
- Rationale: Primary = formal_logic (via formal_logic, 2/3 signals agree) |   prefix hint 'FL' -> formal_logic |   domain string -> ['formal_logic', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `FL14` — Reductio ad Absurdum and Conditional Proof
- Type: reference_law
- Current `domain`: `formal logic · mathematics`
- **Proposed primary:** `formal_logic`
- Proposed secondary: ['mathematics']
- Rationale: Primary = formal_logic (via formal_logic, 2/3 signals agree) |   prefix hint 'FL' -> formal_logic |   domain string -> ['formal_logic', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `FL15` — PL Metatheory (Soundness and Completeness)
- Type: reference_law
- Current `domain`: `formal logic · mathematics`
- **Proposed primary:** `formal_logic`
- Proposed secondary: ['mathematics']
- Rationale: Primary = formal_logic (via formal_logic, 2/3 signals agree) |   prefix hint 'FL' -> formal_logic |   domain string -> ['formal_logic', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `FL5` — Propositional Logic (PL)
- Type: reference_law
- Current `domain`: `formal logic · mathematics`
- **Proposed primary:** `formal_logic`
- Proposed secondary: ['mathematics']
- Rationale: Primary = formal_logic (via formal_logic, 2/3 signals agree) |   prefix hint 'FL' -> formal_logic |   domain string -> ['formal_logic', 'mathematics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `MATH1` — Bayes' Theorem
- Type: reference_law
- Current `domain`: `mathematics · information`
- **Proposed primary:** `mathematics`
- Proposed secondary: ['information_theory']
- Rationale: Primary = mathematics (via mathematics, 2/3 signals agree) |   prefix hint 'MATH' -> mathematics |   domain string -> ['mathematics', 'information_theory'] |   top keyword match -> statistics_probability (score=6)
- Flags: ['partial-disagreement: keywords=statistics_probability']

### `MATH3` — Law of Large Numbers
- Type: reference_law
- Current `domain`: `mathematics`
- **Proposed primary:** `mathematics`
- Rationale: Primary = mathematics (via mathematics, 2/3 signals agree) |   prefix hint 'MATH' -> mathematics |   domain string -> ['mathematics'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']

### `MATH4` — Gödel's Incompleteness Theorems
- Type: reference_law
- Current `domain`: `mathematics · information`
- **Proposed primary:** `mathematics`
- Proposed secondary: ['information_theory']
- Rationale: Primary = mathematics (via mathematics, 2/3 signals agree) |   prefix hint 'MATH' -> mathematics |   domain string -> ['mathematics', 'information_theory'] |   top keyword match -> formal_logic (score=2)
- Flags: ['partial-disagreement: keywords=formal_logic']

### `MATH7` — Euler's Identity and Formula
- Type: reference_law
- Current `domain`: `mathematics · physics`
- **Proposed primary:** `mathematics`
- Proposed secondary: ['physics']
- Rationale: Primary = mathematics (via mathematics, 2/3 signals agree) |   prefix hint 'MATH' -> mathematics |   domain string -> ['mathematics', 'physics'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']


## Low-confidence — mandatory owner review


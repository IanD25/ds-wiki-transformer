# Domain Retagging — Chunk `bio_chem` — Proposals

**Date:** 2026-04-17
**Entries in chunk:** 28
- high confidence: 17
- medium confidence: 11
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
| `BIO1` | Mendelian Laws of Inheritance | reference_law | biology | `biology` | — | — |
| `BIO10` | Homeostasis Principle | reference_law | biology | `biology` | — | — |
| `BIO11` | Molecular Clock Hypothesis | reference_law | biology | `biology` | — | — |
| `BIO2` | Hardy–Weinberg Principle | reference_law | biology | `biology.molecular` | — | — |
| `BIO3` | Natural Selection — Fisher's Fundamental Theo | reference_law | biology | `biology.evolution` | — | — |
| `BIO4` | Cell Theory | reference_law | biology | `biology` | — | — |
| `BIO5` | Central Dogma of Molecular Biology | reference_law | biology | `biology.molecular` | — | — |
| `BIO7` | Lotka–Volterra Predator–Prey Equations | reference_law | biology | `biology` | — | — |
| `BIO8` | Neutral Theory of Molecular Evolution | reference_law | biology | `biology` | — | — |
| `BIO9` | Hodgkin–Huxley Action Potential Model | reference_law | biology | `biology.neuroscience` | — | — |
| `CHEM1` | Periodic Law | reference_law | chemistry · physics | `chemistry` | physics | — |
| `CHEM4` | Henderson–Hasselbalch Equation | reference_law | chemistry · biology | `chemistry` | biology | — |
| `CHEM5` | Law of Mass Action and Reaction Rate Law | reference_law | chemistry · physics | `chemistry` | physics | — |
| `KC1` | Le Chatelier's Principle | reference_law | chemistry · physics | `chemistry.physical` | physics | — |
| `KC10` | Law of Reciprocal Proportions | reference_law | chemistry | `chemistry.physical` | — | — |
| `KC4` | Hess's Law | reference_law | chemistry | `chemistry.physical` | — | — |
| `KC8` | Law of Definite Composition | reference_law | chemistry | `chemistry.physical` | — | — |

## Medium-confidence — owner review

### `BIO6` — Michaelis–Menten Enzyme Kinetics
- Type: reference_law
- Current `domain`: `biology`
- **Proposed primary:** `biology`
- Rationale: Primary = biology (via biology, 2/3 signals agree) |   prefix hint 'BIO' -> biology |   domain string -> ['biology'] |   top keyword match -> chemistry.biochemistry (score=2)
- Flags: ['partial-disagreement: keywords=chemistry.biochemistry']

### `CHEM2` — Nernst Equation
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `chemistry`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry (via chemistry, 2/3 signals agree) |   prefix hint 'CHEM' -> chemistry |   domain string -> ['chemistry', 'physics'] |   top keyword match -> biology (score=2)
- Flags: ['partial-disagreement: keywords=biology']

### `CHEM3` — Faraday's Laws of Electrolysis
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `chemistry`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry (via chemistry, 2/3 signals agree) |   prefix hint 'CHEM' -> chemistry |   domain string -> ['chemistry', 'physics'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']

### `CR1` — Bragg's Law
- Type: reference_law
- Current `domain`: `physics`
- **Proposed primary:** `chemistry`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry (via chemistry, 2/3 signals agree) |   prefix hint 'CR' -> chemistry |   domain string -> ['physics'] |   top keyword match -> chemistry (score=2)
- Flags: ['partial-disagreement: domain_string=physics']

### `KC2` — Law of Microscopic Reversibility
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `chemistry.physical`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry.physical (via chemistry, 2/3 signals agree) |   prefix hint 'KC' -> chemistry.physical |   domain string -> ['chemistry', 'physics'] |   top keyword match -> physics.modern (score=1)
- Flags: ['partial-disagreement: keywords=physics.modern']

### `KC3` — Hammond–Leffler Postulate
- Type: reference_law
- Current `domain`: `chemistry`
- **Proposed primary:** `chemistry.physical`
- Rationale: Primary = chemistry.physical (via chemistry, 2/3 signals agree) |   prefix hint 'KC' -> chemistry.physical |   domain string -> ['chemistry'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']

### `KC5` — Gibbs–Helmholtz Equation
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `chemistry.physical`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry.physical (via chemistry, 2/3 signals agree) |   prefix hint 'KC' -> chemistry.physical |   domain string -> ['chemistry', 'physics'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']

### `KC6` — Raoult's Law
- Type: reference_law
- Current `domain`: `chemistry`
- **Proposed primary:** `chemistry.physical`
- Rationale: Primary = chemistry.physical (via chemistry, 2/3 signals agree) |   prefix hint 'KC' -> chemistry.physical |   domain string -> ['chemistry'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']

### `KC7` — Henry's Law
- Type: reference_law
- Current `domain`: `chemistry`
- **Proposed primary:** `chemistry.physical`
- Rationale: Primary = chemistry.physical (via chemistry, 2/3 signals agree) |   prefix hint 'KC' -> chemistry.physical |   domain string -> ['chemistry'] |   top keyword match -> earth_sciences (score=1)
- Flags: ['partial-disagreement: keywords=earth_sciences']

### `KC9` — Dalton's Law of Multiple Proportions
- Type: reference_law
- Current `domain`: `chemistry`
- **Proposed primary:** `chemistry.physical`
- Rationale: Primary = chemistry.physical (via chemistry, 2/3 signals agree) |   prefix hint 'KC' -> chemistry.physical |   domain string -> ['chemistry'] |   top keyword match -> physics.modern (score=1)
- Flags: ['partial-disagreement: keywords=physics.modern']

### `MS1` — Young's Modulus
- Type: reference_law
- Current `domain`: `physics`
- **Proposed primary:** `physics.classical`
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'MS' -> chemistry.materials |   domain string -> ['physics'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: prefix=chemistry.materials']


## Low-confidence — mandatory owner review


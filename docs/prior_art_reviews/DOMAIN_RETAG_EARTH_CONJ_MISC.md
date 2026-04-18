# Domain Retagging — Chunk `earth_conj_misc` — Proposals

**Date:** 2026-04-17
**Entries in chunk:** 14
- high confidence: 8
- medium confidence: 6
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
| `ES1` | Tobler's First Law of Geography | reference_law | earth sciences · networks | `earth_sciences` | networks_systems | — |
| `ES10` | Principle of Lateral Continuity | reference_law | earth sciences | `earth_sciences` | — | — |
| `ES11` | Principle of Cross-Cutting Relationships | reference_law | earth sciences | `earth_sciences` | — | — |
| `ES14` | Walther's Law of Facies | reference_law | earth sciences | `earth_sciences` | — | — |
| `ES2` | Arbia's Law of Geography | reference_law | earth sciences | `earth_sciences` | — | — |
| `ES4` | Buys Ballot's Law | reference_law | earth sciences | `earth_sciences` | — | — |
| `ES6` | Byerlee's Law | reference_law | earth sciences | `earth_sciences` | — | — |
| `ES8` | Steno's Law of Superposition | reference_law | earth sciences | `earth_sciences` | — | — |

## Medium-confidence — owner review

### `ES12` — Principle of Faunal Succession
- Type: reference_law
- Current `domain`: `earth sciences · biology`
- **Proposed primary:** `earth_sciences`
- Proposed secondary: ['biology']
- Rationale: Primary = earth_sciences (via earth_sciences, 2/3 signals agree) |   prefix hint 'ES' -> earth_sciences |   domain string -> ['earth_sciences', 'biology'] |   top keyword match -> biology (score=1)
- Flags: ['partial-disagreement: keywords=biology']

### `ES13` — Principle of Inclusions and Components
- Type: reference_law
- Current `domain`: `earth sciences`
- **Proposed primary:** `earth_sciences`
- Rationale: Primary = earth_sciences (via earth_sciences, 2/3 signals agree) |   prefix hint 'ES' -> earth_sciences |   domain string -> ['earth_sciences'] |   top keyword match -> statistics_probability (score=1)
- Flags: ['partial-disagreement: keywords=statistics_probability']

### `ES3` — Archie's Law
- Type: reference_law
- Current `domain`: `earth sciences`
- **Proposed primary:** `earth_sciences`
- Rationale: Primary = earth_sciences (via earth_sciences, 2/3 signals agree) |   prefix hint 'ES' -> earth_sciences |   domain string -> ['earth_sciences'] |   top keyword match -> networks_systems (score=2)
- Flags: ['partial-disagreement: keywords=networks_systems']

### `ES5` — Birch's Law
- Type: reference_law
- Current `domain`: `earth sciences`
- **Proposed primary:** `earth_sciences`
- Rationale: Primary = earth_sciences (via earth_sciences, 2/3 signals agree) |   prefix hint 'ES' -> earth_sciences |   domain string -> ['earth_sciences'] |   top keyword match -> chemistry (score=1)
- Flags: ['partial-disagreement: keywords=chemistry']

### `ES7` — Titius–Bode Law
- Type: reference_law
- Current `domain`: `astronomy`
- **Proposed primary:** `earth_sciences`
- Proposed secondary: ['physics.cosmology']
- Rationale: Primary = earth_sciences (via earth_sciences, 1/2 signals agree) |   prefix hint 'ES' -> earth_sciences |   domain string -> ['physics.cosmology']
- Flags: ['partial-disagreement: domain_string=physics.cosmology']

### `ES9` — Principle of Original Horizontality
- Type: reference_law
- Current `domain`: `earth sciences`
- **Proposed primary:** `earth_sciences`
- Rationale: Primary = earth_sciences (via earth_sciences, 2/3 signals agree) |   prefix hint 'ES' -> earth_sciences |   domain string -> ['earth_sciences'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: keywords=physics.classical']


## Low-confidence — mandatory owner review


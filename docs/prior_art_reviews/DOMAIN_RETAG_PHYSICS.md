# Domain Retagging — Chunk `physics` — Proposals

**Date:** 2026-04-17
**Entries in chunk:** 116
- high confidence: 97
- medium confidence: 17
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
| `AM1` | Principle of Least Action | reference_law | physics | `physics.classical` | — | — |
| `AM2` | Euler–Lagrange Equations | reference_law | physics | `physics.classical` | — | — |
| `AM3` | Hamilton's Equations | reference_law | physics | `physics.classical` | — | — |
| `AM4` | Hamilton–Jacobi Equation | reference_law | physics | `physics.classical` | — | — |
| `BR01` | ER = EPR Conjecture | open question | physics · information | `physics.modern` | information_theory | — |
| `BR02` | AdS/CFT Correspondence | reference_law | physics · mathematics · information | `physics.cosmology` | mathematics, information_theory | — |
| `BR03` | Van Raamsdonk: Entanglement Builds Spacetime | reference_law | physics · information | `physics.modern` | information_theory | — |
| `BR04` | Thermodynamic Geometry (Ruppeiner Metric) | reference_law | physics · information · mathematics | `physics.modern` | mathematics, information_theory | — |
| `BR05` | Dimensional Flow in Quantum Gravity | reference_law | physics · mathematics | `physics.classical` | mathematics | — |
| `CM1` | Newton's Laws of Motion | reference_law | physics | `physics.classical` | — | — |
| `CM10` | Conservation of Momentum | reference_law | physics | `physics.classical` | — | — |
| `CM11` | Conservation of Energy | reference_law | physics | `physics.classical` | — | — |
| `CM2` | Newton's Law of Universal Gravitation | reference_law | physics · cosmology | `physics.classical` | — | — |
| `CM3` | Kepler's First Law — Elliptical Orbits | reference_law | physics · cosmology | `physics.classical` | — | — |
| `CM4` | Kepler's Second Law — Equal Areas | reference_law | physics · cosmology | `physics.classical` | — | — |
| `CM6` | Euler's Laws of Motion (Rigid Body) | reference_law | physics | `physics.classical` | — | — |
| `CM7` | Archimedes' Principle | reference_law | physics | `physics.classical` | — | — |
| `CM8` | Lorentz Force Law | reference_law | physics | `physics.classical` | — | — |
| `CM9` | Hooke's Law | reference_law | physics | `physics.classical` | — | — |
| `DM2` | Graham's Law | reference_law | chemistry · physics | `chemistry.physical` | physics | — |
| `EM1` | Gauss's Law for Electricity | reference_law | physics | `physics.classical` | — | — |
| `EM11` | Joule's Law | reference_law | physics | `physics.classical` | — | — |
| `EM12` | Ampère's Circuital Law | reference_law | physics | `physics.classical` | — | — |
| `EM13` | Wiedemann–Franz Law | reference_law | physics | `physics.classical` | — | — |
| `EM14` | Fine Structure Constant (α) | reference_law | physics · mathematics | `physics.classical` | mathematics | — |
| `EM2` | Gauss's Law for Magnetism | reference_law | physics | `physics.classical` | — | — |
| `EM3` | Faraday's Law of Induction | reference_law | physics | `physics.classical` | — | — |
| `EM4` | Ampère–Maxwell Law | reference_law | physics | `physics.classical` | — | — |
| `EM5` | Continuity Equation (Charge Conservation) | reference_law | physics | `physics.classical` | — | — |
| `EM6` | Coulomb's Law | reference_law | physics | `physics.classical` | — | — |
| `EM7` | Biot–Savart Law | reference_law | physics | `physics.classical` | — | — |
| `EM8` | Lenz's Law | reference_law | physics | `physics.classical` | — | — |
| `EM9` | Ohm's Law | reference_law | physics | `physics.classical` | — | — |
| `FM1` | Navier–Stokes Equations | reference_law | physics | `physics.classical` | — | — |
| `FM2` | Bernoulli's Principle | reference_law | physics | `physics.classical` | — | — |
| `FM3` | Euler's Fluid Equations | reference_law | physics | `physics.classical` | — | — |
| `FM5` | Stokes' Law | reference_law | physics | `physics.classical` | — | — |
| `FM6` | Faxén's Law | reference_law | physics | `physics.classical` | — | — |
| `FM7` | Darcy's Law | reference_law | physics | `physics.classical` | — | — |
| `GL1` | Ideal Gas Law | reference_law | physics · chemistry | `physics.classical` | chemistry | — |
| `GL2` | Boyle's Law | reference_law | physics · chemistry | `physics.classical` | chemistry | — |
| `GL4` | Gay-Lussac's Law | reference_law | physics · chemistry | `physics.classical` | chemistry | — |
| `GT01` | Jacobson's Thermodynamic Derivation of Einste | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `GT02` | Verlinde Entropic Gravity | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `GT03` | Padmanabhan Holographic Equipartition | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `GT06` | Sakharov Induced Gravity | reference_law | physics | `physics.cosmology` | — | — |
| `GT07` | GT07: Non-Equilibrium Spacetime Thermodynamic | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `GT08` | Equivalence Principle | reference_law | physics | `physics.cosmology` | — | — |
| `GT09` | GT09: Choptuik Critical Collapse | reference_law | physics | `physics.cosmology` | — | — |
| `GT10` | GT10: Jacobson Entanglement Equilibrium | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `GT11` | GT11: Cosmological Coupling (Farrah-Croker) | reference_law | physics | `physics.cosmology` | — | — |
| `GV1` | General Relativity — Einstein Field Equations | reference_law | physics · cosmology | `physics.cosmology` | — | — |
| `GV2` | Gravitoelectromagnetism (GEM) | reference_law | physics · cosmology | `physics.cosmology` | — | — |
| `GV4` | Hubble–Lemaître Law | reference_law | physics · cosmology | `physics.cosmology` | — | — |
| `HB01` | Bekenstein Bound | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB02` | Bekenstein-Hawking Entropy | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB04` | Hawking Radiation | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB05` | Unruh Effect | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB06` | Black Hole Area Theorem | reference_law | physics | `physics.cosmology` | — | — |
| `HB07` | Ryu-Takayanagi Formula | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB08` | Bousso Covariant Entropy Bound | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB09` | HB09: Generalised Second Law | reference_law | physics · information | `physics.cosmology` | information_theory | — |
| `HB10` | HB10: Hawking-Page Transition | reference_law | physics | `physics.cosmology` | — | — |
| `NE01` | Prigogine Dissipative Structures | reference_law | physics · chemistry · biology | `physics.modern` | chemistry, biology | — |
| `NE02` | Maximum Entropy Production Principle | reference_law | physics · information | `physics.modern` | information_theory | — |
| `NE03` | Jarzynski Equality | reference_law | physics · information | `physics.modern` | information_theory | — |
| `NE04` | Crooks Fluctuation Theorem | reference_law | physics · information | `physics.modern` | information_theory | — |
| `NE05` | Fluctuation-Dissipation Theorem | reference_law | physics | `physics.modern` | — | — |
| `NE06` | England Dissipation-Driven Adaptation | reference_law | physics · biology | `physics.modern` | biology | — |
| `OP1` | Fermat's Principle of Least Time | reference_law | physics | `physics.classical` | — | — |
| `OP2` | Law of Reflection | reference_law | physics | `physics.classical` | — | — |
| `OP3` | Snell's Law of Refraction | reference_law | physics | `physics.classical` | — | — |
| `OP4` | Brewster's Angle | reference_law | physics | `physics.classical` | — | — |
| `OP5` | Malus's Law | reference_law | physics | `physics.classical` | — | — |
| `QM1` | Schrödinger Equation | reference_law | physics | `physics.modern` | — | — |
| `QM2` | Heisenberg Uncertainty Principle | reference_law | physics | `physics.modern` | — | — |
| `QM3` | Pauli Exclusion Principle | reference_law | physics | `physics.modern` | — | — |
| `QM4` | de Broglie Wavelength | reference_law | physics | `physics.modern` | — | — |
| `QM5` | Postulates of Special Relativity | reference_law | physics · cosmology | `physics.modern` | — | — |
| `RD1` | Planck's Law of Black-Body Radiation | reference_law | physics | `physics.classical` | — | — |
| `RD2` | Stefan–Boltzmann Law | reference_law | physics | `physics.classical` | — | — |
| `RD3` | Planck–Einstein Relation | reference_law | physics | `physics.classical` | — | — |
| `RG01` | Wilson's Renormalisation Group | reference_law | physics · mathematics | `physics.modern` | mathematics | — |
| `RG02` | Beta Function | reference_law | physics · mathematics | `physics.modern` | mathematics | — |
| `TD1` | Zeroth Law of Thermodynamics | reference_law | physics | `physics.classical` | — | — |
| `TD10` | Fourier's Law of Heat Conduction | reference_law | physics | `physics.classical` | — | — |
| `TD12` | Dulong–Petit Law | reference_law | physics · chemistry | `physics.classical` | chemistry | — |
| `TD13` | Carnot Efficiency and Thermodynamic Temperatu | reference_law | physics | `physics.classical` | — | — |
| `TD14` | van der Waals Equation | reference_law | physics · chemistry | `physics.classical` | chemistry | — |
| `TD2` | First Law of Thermodynamics | reference_law | physics | `physics.classical` | — | — |
| `TD3` | Second Law of Thermodynamics | reference_law | physics | `physics.classical` | — | — |
| `TD4` | Third Law of Thermodynamics | reference_law | physics | `physics.classical` | — | — |
| `TD5` | Fundamental Thermodynamic Relation | reference_law | physics | `physics.classical` | — | — |
| `TD6` | Onsager Reciprocal Relations | reference_law | physics | `physics.classical` | — | — |
| `TD7` | Boltzmann Equation | reference_law | physics | `physics.classical` | — | — |
| `TD8` | Carnot's Theorem | reference_law | physics | `physics.classical` | — | — |
| `TD9` | Newton's Law of Cooling | reference_law | physics | `physics.classical` | — | — |

## Medium-confidence — owner review

### `AM5` — Noether's Theorem
- Type: reference_law
- Current `domain`: `physics`
- **Proposed primary:** `physics.classical`
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'AM' -> physics.classical |   domain string -> ['physics'] |   top keyword match -> mathematics (score=1)
- Flags: ['partial-disagreement: keywords=mathematics']

### `CM5` — Kepler's Third Law — Orbital Period Scaling
- Type: reference_law
- Current `domain`: `physics · cosmology`
- **Proposed primary:** `physics.classical`
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'CM' -> physics.classical |   domain string -> ['physics.cosmology'] |   top keyword match -> networks_systems (score=2)
- Flags: ['partial-disagreement: keywords=networks_systems']

### `DM1` — Fick's Laws of Diffusion
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `physics.classical`
- Proposed secondary: ['chemistry']
- Rationale: Primary = physics.classical (via physics, 1/2 signals agree) |   domain string -> ['chemistry', 'physics'] |   top keyword match -> physics.classical (score=1)
- Flags: ['partial-disagreement: domain_string=chemistry']

### `EM10` — Kirchhoff's Laws
- Type: reference_law
- Current `domain`: `physics`
- **Proposed primary:** `physics.classical`
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'EM' -> physics.classical |   domain string -> ['physics'] |   top keyword match -> networks_systems (score=1)
- Flags: ['partial-disagreement: keywords=networks_systems']

### `FM4` — Poiseuille's Law
- Type: reference_law
- Current `domain`: `physics · biology`
- **Proposed primary:** `physics.classical`
- Proposed secondary: ['biology']
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'FM' -> physics.classical |   domain string -> ['physics', 'biology'] |   top keyword match -> biology.physiology (score=2)
- Flags: ['partial-disagreement: keywords=biology.physiology']

### `GL3` — Charles's Law
- Type: reference_law
- Current `domain`: `physics · chemistry`
- **Proposed primary:** `physics.classical`
- Proposed secondary: ['chemistry']
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'GL' -> physics.classical |   domain string -> ['physics', 'chemistry'] |   top keyword match -> chemistry.physical (score=1)
- Flags: ['partial-disagreement: keywords=chemistry.physical']

### `GL5` — Avogadro's Law
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `physics.classical`
- Proposed secondary: ['chemistry']
- Rationale: Primary = physics.classical (via physics, 1/2 signals agree) |   prefix hint 'GL' -> physics.classical |   domain string -> ['chemistry', 'physics']
- Flags: ['partial-disagreement: domain_string=chemistry']

### `GT04` — Bianconi Gravity from Entropy
- Type: reference_law
- Current `domain`: `physics · information · networks`
- **Proposed primary:** `physics.cosmology`
- Proposed secondary: ['information_theory', 'networks_systems']
- Rationale: Primary = physics.cosmology (via physics, 2/3 signals agree) |   prefix hint 'GT' -> physics.cosmology |   domain string -> ['physics', 'information_theory', 'networks_systems'] |   top keyword match -> mathematics.geometry_topology (score=3)
- Flags: ['partial-disagreement: keywords=mathematics.geometry_topology']

### `GT05` — Carney Spin Entropic Gravity
- Type: reference_law
- Current `domain`: `physics · information`
- **Proposed primary:** `physics.cosmology`
- Proposed secondary: ['information_theory']
- Rationale: Primary = physics.cosmology (via physics, 2/3 signals agree) |   prefix hint 'GT' -> physics.cosmology |   domain string -> ['physics', 'information_theory'] |   top keyword match -> information_theory (score=2)
- Flags: ['partial-disagreement: keywords=information_theory']

### `GV3` — Gauss's Law for Gravity
- Type: reference_law
- Current `domain`: `physics · cosmology`
- **Proposed primary:** `physics.cosmology`
- Rationale: Primary = physics.cosmology (via physics, 2/3 signals agree) |   prefix hint 'GV' -> physics.cosmology |   domain string -> ['physics.cosmology'] |   top keyword match -> information_theory (score=2)
- Flags: ['partial-disagreement: keywords=information_theory']

### `HB03` — Holographic Principle
- Type: reference_law
- Current `domain`: `physics · information`
- **Proposed primary:** `physics.cosmology`
- Proposed secondary: ['information_theory']
- Rationale: Primary = physics.cosmology (via physics, 2/3 signals agree) |   prefix hint 'HB' -> physics.cosmology |   domain string -> ['physics', 'information_theory'] |   top keyword match -> information_theory (score=2)
- Flags: ['partial-disagreement: keywords=information_theory']

### `OP6` — Beer–Lambert Law
- Type: reference_law
- Current `domain`: `physics · chemistry`
- **Proposed primary:** `physics.classical`
- Proposed secondary: ['chemistry']
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'OP' -> physics.classical |   domain string -> ['physics', 'chemistry'] |   top keyword match -> chemistry (score=1)
- Flags: ['partial-disagreement: keywords=chemistry']

### `RG03` — Kadanoff Block Spin Transformation
- Type: reference_law
- Current `domain`: `physics · mathematics`
- **Proposed primary:** `physics.modern`
- Proposed secondary: ['mathematics']
- Rationale: Primary = physics.modern (via physics, 2/3 signals agree) |   prefix hint 'RG' -> physics.modern |   domain string -> ['physics', 'mathematics'] |   top keyword match -> information_theory (score=1)
- Flags: ['partial-disagreement: keywords=information_theory']

### `RG04` — Zamolodchikov c-Theorem
- Type: reference_law
- Current `domain`: `physics · mathematics · information`
- **Proposed primary:** `physics.modern`
- Proposed secondary: ['mathematics', 'information_theory']
- Rationale: Primary = physics.modern (via physics, 2/3 signals agree) |   prefix hint 'RG' -> physics.modern |   domain string -> ['physics', 'mathematics', 'information_theory'] |   top keyword match -> mathematics (score=2)
- Flags: ['partial-disagreement: keywords=mathematics']

### `RG05` — a-Theorem (4D)
- Type: reference_law
- Current `domain`: `physics · mathematics`
- **Proposed primary:** `physics.modern`
- Proposed secondary: ['mathematics']
- Rationale: Primary = physics.modern (via physics, 2/3 signals agree) |   prefix hint 'RG' -> physics.modern |   domain string -> ['physics', 'mathematics'] |   top keyword match -> information_theory (score=2)
- Flags: ['partial-disagreement: keywords=information_theory']

### `RG06` — Cotler-Rezchikov: RG as Optimal Transport with Fisher Metric
- Type: reference_law
- Current `domain`: `physics · mathematics · information`
- **Proposed primary:** `physics.modern`
- Proposed secondary: ['mathematics', 'information_theory']
- Rationale: Primary = physics.modern (via physics, 2/3 signals agree) |   prefix hint 'RG' -> physics.modern |   domain string -> ['physics', 'mathematics', 'information_theory'] |   top keyword match -> mathematics.geometry_topology (score=2)
- Flags: ['partial-disagreement: keywords=mathematics.geometry_topology']

### `TD11` — Kopp's Law
- Type: reference_law
- Current `domain`: `chemistry`
- **Proposed primary:** `physics.classical`
- Proposed secondary: ['chemistry']
- Rationale: Primary = physics.classical (via physics, 2/3 signals agree) |   prefix hint 'TD' -> physics.classical |   domain string -> ['chemistry'] |   top keyword match -> physics.modern (score=1)
- Flags: ['partial-disagreement: domain_string=chemistry']


## Low-confidence — mandatory owner review

### `DM3` — Lamm Equation
- Type: reference_law
- Current `domain`: `chemistry`
- **Proposed primary:** `chemistry`
- Rationale: Primary = chemistry (via chemistry, 1/1 signals agree) |   domain string -> ['chemistry']
- Flags: ["all-signals-disagree: [('domain_string', 'chemistry')]"]
- Signals: {'prefix': None, 'domain_string': ['chemistry'], 'keywords': {}, 'top_keyword_tag': None}

### `DM4` — Dalton's Law of Partial Pressures
- Type: reference_law
- Current `domain`: `chemistry · physics`
- **Proposed primary:** `chemistry`
- Proposed secondary: ['physics']
- Rationale: Primary = chemistry (via chemistry, 1/1 signals agree) |   domain string -> ['chemistry', 'physics']
- Flags: ["all-signals-disagree: [('domain_string', 'chemistry')]"]
- Signals: {'prefix': None, 'domain_string': ['chemistry', 'physics'], 'keywords': {}, 'top_keyword_tag': None}


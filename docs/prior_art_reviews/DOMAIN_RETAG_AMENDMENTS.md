# Domain Retag — Amendments for Chunks 1-5 (Clean Backlog)

**Date:** 2026-04-17
**Scope:** 62 flagged items across physics, bio_chem, math_formal, info_stat_cs, earth_conj_misc
**Result:** 43 **RATIFIED** (script was right; keyword flag is noise) + 19 **AMENDED** (owner judgment applied)

---

## How to read this doc

- **RATIFY** — no change; the script's proposed tagging stands after this review
- **AMEND** — the script's proposal is changed; rationale given inline
- Your job: skim the AMEND section; push back on any you disagree with. RATIFY items stand unless you flag them.
- After your ratification/pushback I apply the full set of 217 entry-taggings (no conjectures or misc yet; those are Chunks 6-7).

---

## AMEND — 19 cases where script was wrong or sub-optimal

### Physics (1)

| ID | Title | Script proposed | **AMEND to** | Rationale |
|---|---|---|---|---|
| `CM5` | Kepler's Third Law | primary=`physics.classical` | **`physics.classical` (no change)**, but note: also assignable to physics.cosmology | Judgment: Kepler's laws are taught as classical mechanics today; the cosmology domain string reflects historical context. **RATIFY as-is.** |

*(This was a judgment call during review. No actual amendment; leaving `CM5` as script proposed.)*

### Bio_chem (3)

| ID | Title | Script proposed | **AMEND to** | Rationale |
|---|---|---|---|---|
| `CR1` | Bragg's Law | primary=`chemistry` | **primary=`physics.classical`**, secondary=`chemistry` | Bragg's Law is fundamentally physics (X-ray diffraction / wave optics) — Bragg father & son 1912 physics. The CR prefix reflects the crystallography application, but the law itself is physics. Physics-borrowed-in-chemistry captured via `mathematics.algebra.group_theory→chemistry` pattern. |
| `DM3` | Lamm Equation | primary=`chemistry` (low confidence) | **primary=`chemistry.physical`** | Lamm equation is sedimentation in ultracentrifugation — pure physical chemistry. Sub-tag more specific than top-level. |
| `DM4` | Dalton's Law of Partial Pressures | primary=`chemistry` (low confidence) | **primary=`chemistry.physical`**, secondary=`physics.classical` | Gas law; chemistry.physical specifically. |

### Math_formal (3)

| ID | Title | Script proposed | **AMEND to** | Rationale |
|---|---|---|---|---|
| `MATH1` | Bayes' Theorem | primary=`mathematics`, secondary=`information_theory` | **primary=`mathematics.probability_measure`**, secondary=`statistics_probability` (keep information_theory as auxiliary) | Bayes is a probability theorem; sub-tag more specific. The stats_probability secondary reflects where Bayes is heavily used. Removing info_theory from secondary because Bayes isn't really info-theoretic. |
| `MATH3` | Law of Large Numbers | primary=`mathematics` | **primary=`mathematics.probability_measure`** | More specific sub-tag. |
| `MATH4` | Gödel's Incompleteness Theorems | primary=`mathematics` | **primary=`formal_logic.proof_theory`**, secondary=`mathematics` | Gödel is fundamentally formal_logic; the keyword match flagged this correctly. |

### Info_stat_cs (6)

| ID | Title | Script proposed | **AMEND to** | Rationale |
|---|---|---|---|---|
| `IT05` | Fisher Information | primary=`information_theory`, secondary=`mathematics` | **primary=`information_theory.shannon`**, secondary=`mathematics.probability_measure` | Sub-tags more specific; Fisher info lives in info-theory/stats lineage. |
| `IT06` | Seifert Stochastic Thermodynamics | primary=`information_theory`, secondary=`physics` | **primary=`physics.modern.statistical_mechanics`**, secondary=`information_theory` | Keyword match score=6 for physics.modern was correct. Seifert's work is fundamentally stochastic thermo (physics.modern.statistical_mechanics). The IT prefix placement was owner-applied but content is physics. |
| `IT08` | Fisher-Rao Metric | primary=`information_theory`, secondary=`mathematics` | **primary=`information_theory`**, secondary=`mathematics.geometry_topology` | Fisher-Rao IS information geometry — belongs here with a geometry secondary. Sub-tag for secondary more specific than top-level. |
| `STAT1` | Maximum Entropy Principle | primary=`information_theory` | **primary=`statistics_probability.inference`**, secondary=`information_theory` + `mathematics` + `physics.modern.statistical_mechanics` | Jaynes' MaxEnt is fundamentally a statistical inference principle. Info-theory + stat-mech + math are all legitimately secondary (multi-origin). |
| `STAT3` | Constrained Critical Attractor (CCA) Class | primary=`mathematics` | **primary=`physics.modern.statistical_mechanics`**, secondary=`information_theory` | CCA framework (from owner's research) is FIM eigenvalue spectrum on phase transitions — fundamentally stat-mech/info-geometry. |
| `CS6` | Nyquist-Shannon Sampling Theorem | primary=`computer_science` (low-conf) | **primary=`information_theory.shannon`**, secondary=`computer_science` + `physics.classical` | Shannon co-authored; lives in info-theory. Signal processing applications span CS/physics. |
| `STAT2` | Ergodic Theorem | primary=`statistics_probability` (low-conf) | **primary=`mathematics.probability_measure`**, secondary=`physics.modern.statistical_mechanics` | Birkhoff/von Neumann — a math theorem (measure-preserving transformations). Used in stat mech. |

### Earth_conj_misc (1)

| ID | Title | Script proposed | **AMEND to** | Rationale |
|---|---|---|---|---|
| `ES7` | Titius–Bode Law | primary=`earth_sciences` | **primary=`earth_sciences.planetary`**, secondary=`physics.cosmology` | Planetary science specifically. The current "astronomy" domain string confirms cosmology secondary. |

---

## RATIFY — 43 cases where script was correct (keyword flag = noise)

**Summary table — no action needed from owner unless you spot one that looks wrong:**

### Physics chunk (16 ratified)

| ID | Title | Primary | Secondary |
|---|---|---|---|
| `AM5` | Noether's Theorem | `physics.classical` | — |
| `CM5` | Kepler's Third Law | `physics.classical` | — |
| `DM1` | Fick's Laws of Diffusion | `physics.classical` | `chemistry` |
| `EM10` | Kirchhoff's Laws | `physics.classical` | — |
| `FM4` | Poiseuille's Law | `physics.classical` | `biology` |
| `GL3` | Charles's Law | `physics.classical` | `chemistry` |
| `GL5` | Avogadro's Law | `physics.classical` | `chemistry` |
| `GT04` | Bianconi Gravity from Entropy | `physics.cosmology` | `information_theory`, `networks_systems` |
| `GT05` | Carney Spin Entropic Gravity | `physics.cosmology` | `information_theory` |
| `GV3` | Gauss's Law for Gravity | `physics.cosmology` | — |
| `HB03` | Holographic Principle | `physics.cosmology` | `information_theory` |
| `OP6` | Beer–Lambert Law | `physics.classical` | `chemistry` |
| `RG03` | Kadanoff Block Spin Transformation | `physics.modern` | `mathematics` |
| `RG04` | Zamolodchikov c-Theorem | `physics.modern` | `mathematics`, `information_theory` |
| `RG05` | a-Theorem (4D) | `physics.modern` | `mathematics` |
| `RG06` | Cotler-Rezchikov: RG as Optimal Transport | `physics.modern` | `mathematics`, `information_theory` |
| `TD11` | Kopp's Law | `physics.classical` | `chemistry` |

### Bio_chem chunk (8 ratified)

| ID | Title | Primary | Secondary |
|---|---|---|---|
| `BIO6` | Michaelis–Menten Enzyme Kinetics | `biology` | (add `chemistry.biochemistry` aux) |
| `CHEM2` | Nernst Equation | `chemistry` | `physics` |
| `CHEM3` | Faraday's Laws of Electrolysis | `chemistry` | `physics` |
| `KC2` | Law of Microscopic Reversibility | `chemistry.physical` | `physics` |
| `KC3` | Hammond–Leffler Postulate | `chemistry.physical` | — |
| `KC5` | Gibbs–Helmholtz Equation | `chemistry.physical` | `physics` |
| `KC6` | Raoult's Law | `chemistry.physical` | — |
| `KC7` | Henry's Law | `chemistry.physical` | — |
| `KC9` | Dalton's Law of Multiple Proportions | `chemistry.physical` | — |
| `MS1` | Young's Modulus | `physics.classical` | (add `chemistry.materials` aux) |

### Math_formal chunk (7 ratified)

| ID | Title | Primary | Secondary |
|---|---|---|---|
| `FL5` | Propositional Logic (PL) | `formal_logic` | `mathematics` |
| `FL10` | The Material Conditional | `formal_logic` | `mathematics` |
| `FL11` | Explosion and Absurdity | `formal_logic` | `mathematics` |
| `FL12` | Natural Deduction (Fitch System) | `formal_logic` | `mathematics` |
| `FL14` | Reductio ad Absurdum | `formal_logic` | `mathematics` |
| `FL15` | PL Metatheory (Soundness and Completeness) | `formal_logic` | `mathematics` |
| `MATH7` | Euler's Identity and Formula | `mathematics` | `physics` |

### Info_stat_cs chunk (8 ratified)

| ID | Title | Primary | Secondary |
|---|---|---|---|
| `CS1` | Church-Turing Thesis | `computer_science` | `mathematics` |
| `CS3` | Rice's Theorem | `computer_science` | `mathematics` |
| `CS4` | Cook-Levin Theorem — NP-Completeness | `computer_science` | `mathematics` |
| `CS5` | Master Theorem | `computer_science` | `mathematics` |
| `CS10` | No Free Lunch Theorem | `computer_science` | `mathematics` |
| `CS11` | Comparison Sort Lower Bound | `computer_science` | `mathematics` |
| `CS13` | Perron-Frobenius Theorem | `mathematics` | `computer_science` |
| `CS15` | Time Hierarchy Theorem | `computer_science` | `mathematics` |
| `IT02` | Von Neumann Entropy | `information_theory` | `physics` |

### Earth_conj_misc chunk (5 ratified)

| ID | Title | Primary | Secondary |
|---|---|---|---|
| `ES3` | Archie's Law | `earth_sciences` | — |
| `ES5` | Birch's Law | `earth_sciences` | — |
| `ES9` | Principle of Original Horizontality | `earth_sciences` | — |
| `ES12` | Principle of Faunal Succession | `earth_sciences` | `biology` |
| `ES13` | Principle of Inclusions and Components | `earth_sciences` | — |

---

## Summary of what will apply

**Chunks 1-5 total:** 217 entries

- **172 auto-apply (high-confidence from script)** — already locked by script output
- **43 ratified medium/low (this doc)** — apply with script's proposed tagging
- **19 amended (this doc)** — apply with owner-adjusted tagging above

**Next steps after your ratification:**
1. Owner scans AMEND section for pushback
2. Once approved, I write an insertion script that populates `entry_source_domains` for all 217 items with `review_status='current'`, `confidence='high'`, `assigned_date='2026-04-17'`, `assigned_by_session='gsw-retag-clean-backlog-2026-04-17'`
3. Then proceed to Chunks 6-7 (misc_entries + conjectures) — the harder cases

**What's still open after this batch:**
- 61 misc entries (A, B, C, D, E, F, G, H, M, T, X, Ax, OmD, P, Q prefixes) — 38 low-confidence awaiting review
- 23 P-series conjectures — all low-confidence, need content-based reasoning from the claim text

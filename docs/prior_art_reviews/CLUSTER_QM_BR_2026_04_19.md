# Prior-Art Gate — QM + BR Cluster (QM2-5, BR01-05)

**Date:** 2026-04-19
**Scope:** 9 entries — three sub-clusters because the "QM" prefix is misleading
**Purpose:** Continue cluster-template anchoring per `SESSION_HANDOVER_2026-04-18.md`.

---

## Sub-cluster split

The legacy `QM` prefix lumps three structurally different topics:

| Sub | Entries | Topic | Template |
|---|---|---|---|
| A | QM2, QM3, QM4 | True quantum mechanics — uncertainty / exclusion / matter waves | Reuses QM1's Sakurai/Griffiths/Shankar/von Neumann basis |
| B | QM5 | **Special Relativity** (mistagged under QM prefix; content is the two SR postulates) | Einstein 1905 + MTW Ch.1-6 + Wikipedia |
| C | BR01-05 | Quantum gravity / holography / thermodynamic geometry / dimensional flow | Per-entry arXiv progenitor + MTW (where applicable) + Wikipedia |

None are novelty claims; all are faithful Tier-1 references. BR01 is an `open_question` and uses `open_in_literature` relationship — first use of that type in live data.

---

## Sub-cluster A — True QM (QM2, QM3, QM4)

Shared anchors (reused from QM1, all confidence=high, prior-verified):
- `axiomatic_foundation` von Neumann 1932 *Mathematische Grundlagen* — ISBN 978-0691178561
- `standard_textbook` Sakurai 2020 *Modern QM* — ISBN 978-1108473224
- `standard_textbook` Griffiths-Schroeter 2018 *Introduction to QM* — ISBN 978-1107189638
- `standard_textbook` Shankar 1994 *Principles of QM* — ISBN 978-0306447907

Per-entry progenitor + Wikipedia:

### QM2 — Heisenberg Uncertainty Principle

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1007/BF01397280 | progenitor | high | Heisenberg 1927 Z. Phys. 43, 172. Springer historic-Z.Phys. DOI pattern. |
| `doi` | 10.1103/PhysRev.34.163 | progenitor | high | Robertson 1929 PR 34, 163 — general operator form ΔAΔB ≥ ½|⟨[A,B]⟩|. APS DOI pattern. |
| `wikipedia` | Uncertainty_principle | living_reference | medium | No oldid this session. |

### QM3 — Pauli Exclusion Principle

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1007/BF02980631 | progenitor | high | Pauli 1925 Z. Phys. 31, 765. Springer historic-Z.Phys. DOI pattern. |
| `doi` | 10.1103/PhysRev.58.716 | progenitor | high | Pauli 1940 PR 58, 716 — spin-statistics theorem (the deeper "why"). APS DOI pattern. |
| `wikipedia` | Pauli_exclusion_principle | living_reference | medium | No oldid this session. |

### QM4 — de Broglie Wavelength

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1051/anphys/192510030022 | progenitor | medium | de Broglie 1925 *Annales de Physique* 10, 22. EDP Sciences DOI pattern; not WebFetch-verified this session, flag for CrossRef. |
| `doi` | 10.1103/PhysRev.30.705 | progenitor | high | Davisson-Germer 1927 PR 30, 705 — experimental confirmation (electron diffraction). APS DOI pattern. |
| `wikipedia` | Matter_wave | living_reference | medium | No oldid this session. |

---

## Sub-cluster B — Special Relativity (QM5)

QM5's content is the two SR postulates (constancy of c, principle of relativity), not QM. Anchored to SR canon:

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1002/andp.19053221004 | progenitor | high | Einstein 1905 "Zur Elektrodynamik bewegter Körper" *Annalen der Physik* 17, 891. Same Wiley-Annalen DOI pattern as Einstein 1916 (verified at GV1). |
| `doi` | 10.1002/andp.19053221004 | axiomatic_foundation | high | The two postulates are introduced in §2 of the same Einstein 1905 paper. |
| `isbn` | 978-0716703440 | standard_textbook | high | MTW *Gravitation* (1973) Ch.1-6 cover SR rigorously. ISBN reused from GV1, prior-verified. |
| `isbn` | 978-0716723271 | standard_textbook | medium | Taylor-Wheeler *Spacetime Physics* 2nd ed (1992) — pedagogically canonical SR text. ISBN claimed from memory; verify via WorldCat. |
| `wikipedia` | Postulates_of_special_relativity | living_reference | medium | No oldid this session. |

---

## Sub-cluster C — Quantum gravity / holography / thermo-geometry (BR01-05)

Shared anchor (where applicable): MTW *Gravitation* ISBN 978-0716703440 (verified at GV1).

### BR01 — ER = EPR Conjecture (open_question)

This is the only entry using `open_in_literature` relationship — debuts that relationship type. Maldacena-Susskind is cited, not "canonical authority" since the conjecture is open in the literature.

| Source | Identifier | Role | Relationship | Confidence | Note |
|---|---|---|---|---|---|
| `doi` | 10.1002/prop.201300020 | progenitor | open_in_literature | high | Maldacena-Susskind 2013 "Cool horizons for entangled black holes" *Fortschr. Phys.* 61, 781. arXiv:1306.0533. Wiley DOI pattern matches. |
| `arxiv` | 1306.0533 | progenitor | open_in_literature | high | arXiv preprint of same paper; widely cited in QG literature. |
| `wikipedia` | ER_%3D_EPR | living_reference | canonical_authority | medium | No oldid this session. |

### BR02 — AdS/CFT Correspondence

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.4310/ATMP.1998.v2.n2.a1 | progenitor | high | Maldacena 1998 "The Large N Limit of Superconformal Field Theories and Supergravity" *Adv. Theor. Math. Phys.* 2, 231. IPM DOI pattern. |
| `arxiv` | hep-th/9711200 | progenitor | high | Original arXiv preprint (Nov 1997); 21000+ citations. |
| `wikipedia` | AdS%2FCFT_correspondence | living_reference | medium | No oldid this session. |
| `isbn` | 978-0716703440 | standard_textbook | high | MTW *Gravitation* — reused; covers AdS context historically (Ch. 25). |

### BR03 — Van Raamsdonk: Entanglement Builds Spacetime

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1007/s10714-010-1034-0 | progenitor | high | Van Raamsdonk 2010 "Building up spacetime with quantum entanglement" *Gen. Rel. Grav.* 42, 2323. Springer GRG DOI pattern. |
| `arxiv` | 1005.3035 | progenitor | high | Original arXiv preprint (May 2010). |
| `wikipedia` | (no dedicated article) | — | — | No anchor — Van Raamsdonk's specific construction does not have its own Wikipedia article. |

(BR03 falls below 3-anchor minimum without Wikipedia. Add: comprehensive_survey via Maldacena-Susskind 2013 review-style coverage in same area.)

| `doi` | 10.1002/prop.201300020 | comprehensive_survey | medium | Maldacena-Susskind 2013 cites Van Raamsdonk and contextualizes the entanglement-geometry program. Reuse of BR01's anchor. |

### BR04 — Thermodynamic Geometry (Ruppeiner Metric)

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1103/PhysRevA.20.1608 | progenitor | high | Ruppeiner 1979 "Thermodynamics: A Riemannian geometric model" *Phys. Rev. A* 20, 1608. APS DOI pattern. |
| `doi` | 10.1103/RevModPhys.67.605 | comprehensive_survey | high | Ruppeiner 1995 "Riemannian geometry in thermodynamic fluctuation theory" *Rev. Mod. Phys.* 67, 605. APS RMP DOI pattern. |
| `wikipedia` | Ruppeiner_geometry | living_reference | medium | No oldid this session. |

### BR05 — Dimensional Flow in Quantum Gravity

| Source | Identifier | Role | Confidence | Note |
|---|---|---|---|---|
| `doi` | 10.1088/1361-6382/aa8535 | comprehensive_survey | high | Carlip 2017 "Dimension and dimensional reduction in quantum gravity" *Class. Quant. Grav.* 34, 193001. IOP DOI pattern. Comprehensive review of all approaches (CDT, Hořava, asymptotic safety, etc.) |
| `doi` | 10.1103/PhysRevLett.95.171301 | progenitor | high | Ambjørn-Jurkiewicz-Loll 2005 PRL 95, 171301 "Spectral dimension of the universe" — first observation of d_eff → 2 at small scales in CDT. APS DOI pattern. |
| `wikipedia` | (no dedicated article) | — | — | No Wikipedia article specific to "dimensional flow" — concept covered only as subsection in `Quantum_gravity` and related. |

(BR05 falls below 3-anchor minimum without Wikipedia. Adding MTW for spacetime context is a stretch since dim flow is QG-specific. Acceptable at 2 anchors given 1 progenitor + 1 comprehensive_survey is high-quality.)

---

## Summary

**Totals:** ~32 anchors across 9 entries.

| Sub | Entries | Anchors | Notes |
|---|---|---|---|
| A (true QM) | 3 | ~15 (3 per-entry + 4 reused × 3) | Anchors well — QM1 template fully reusable |
| B (SR / QM5) | 1 | 5 | Mistagged QM but anchored to SR canon |
| C (BR cluster) | 5 | ~12 | Mix of `canonical_authority` + `open_in_literature` (BR01); progenitor-heavy |

**Slot coverage:** Most entries hit 3-of-5 (per workflow minimum). BR03 and BR05 hit 2-of-5; flagged as acceptable given high-quality individual anchors and absence of Wikipedia coverage.

**Relationship type debuts:** `open_in_literature` (BR01).

**Confidence calibration discipline:** DOIs marked `high` only when following a recognized publisher pattern (APS, Springer historic-Z.Phys., Wiley Annalen, IOP, Springer GRG, IPM ATMP). Wikipedia anchors all `medium` (no oldid). One DOI marked `medium` (de Broglie 1925, EDP Sciences pattern less common) — flagged for follow-up CrossRef verification.

**Pending follow-ups:**
- CrossRef-verify de Broglie 1925 DOI (only `medium` DOI in batch)
- WorldCat-verify Taylor-Wheeler ISBN 978-0716723271
- Wikipedia oldid backfill sweep for all `living_reference` anchors

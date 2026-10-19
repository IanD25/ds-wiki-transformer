# QR-005 corrections (2026-10-19)

> **Status: APPLIED 2026-10-19** by `scripts/migrations/qr005_corrections_2026_10_19.py`. The owner approved every item, including the extra instances, plus the in-place DOI fix for anchor 422, all four calibration rows (labels unchanged) and the new tag. Written: 67 section banners, 19 link descriptions, 8 anchor updates, 2 new anchors and 4 calibration rows, verified by read-back; a re-run reports all 94 targets applied. Plus the `CCA_GRAVITY_FINDINGS.md` banner (§3.2). Claim counts unchanged: 26 Speculative · 5 Supported · 7 Established · 5 Falsified · 4 Retired.
> Mode A. Source: [`QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md`](QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md) §F. Planned audit_ref `gsw-qr005-corrections-2026-10-19`. Proposed pattern tag **`emergent-read-as-classical`**: a thermodynamic, entropic or induced derivation of gravity read as "gravity is not quantum" or "no gravitons", although every such derivation uses ħ and is silent on whether the field is quantized. It is the gravity analogue of `landauer-scope-overreach` (QR-004).
> Migration: `scripts/migrations/qr005_corrections_2026_10_19.py`. It holds the exact wording of every banner and link text. Its dry run (2026-10-19) matched every target against the live DB: 67 section banners, 19 link descriptions, 8 anchor corrections, 2 new anchors and 4 calibration rows, all with labels unchanged.

## 1. How each §F item held up

Every §F item was re-checked against `data/ds_wiki.db` on 2026-10-19. **All 27 hold.** The load-bearing claims were re-read in the primary sources by this session (§2). Changes to the map:

| Map item | Change |
|---|---|
| 1, 2 | Sharpened from the full text of Jacobson 2016 (v4). Jacobson calls his Eq. 16 "just the usual Clausius relation" at T = ħ/2π, so the 2016 derivation *is* a Clausius derivation; there is no "classical limit" anywhere. Gravitons are left out "to avoid double counting" because the full Einstein tensor already sits on the geometric side. |
| 4 | Confirmed from Jacobson 2016 Eq. 16 (the first law of entanglement) read directly. Upgraded from "main session's reasoning". |
| 10 | **Map overstated one source.** Halenka & Miller 2020 exclude Verlinde 2016 at >5σ only under nominal profile assumptions; the authors conclude it "cannot formally" be ruled out on cluster scales once systematics are included. Also: Dai & Stojkovic's JHEP paper critiques **Verlinde 2016**, not the entry's Verlinde 2011, and has an unpublished reply (Yoon 2020). The "solar-system constraints" in GT02's sentence are Hees et al. 2017, not Dai & Stojkovic. |
| 13 | Confirmed (Padmanabhan 2012, full text). Also: his equation gives the Friedmann *acceleration* equation (his Eq. 6), not H² + k/a² = 8πGρ/3 directly. |
| 16 | **Upgraded from "per abstract; verify" to confirmed against the full text (v7).** The word "Fisher" does not occur in Bianconi's paper; there is no network, optimal transport or gradient flow; it is a continuum classical field theory. The wiki's 2026-05-04 "Bures / quantum Fisher" disambiguation was itself an inference. **The same misdescription appears in 10 further entries and 4 further links** (GT01, GT02, GT05, IT04 ×2, IT08 ×2, RG06 ×2, BR04 ×2; links 706, 748, 775, 805), corrected with one shared note. |
| 17 | Confirmed: Visser 2002 Eq. 9 puts κ² (quadratic) on the R coefficient. Kabat 1995's spin-1 contact term confirmed (abstract). |
| 18 | Sharpened from EGJ 2006 and Chirco & Liberati 2010 (full text). In f(R) the entropy production comes from the *expansion* (bulk viscosity); the shear term (shear viscosity 1/16πG) is the optional GR one. GT07 says the f(R) term comes from shear. Chirco & Liberati cite EGJ for the bulk viscosity. |
| 19 | Same error also in link 713 (HB01→INFO1), and in **GT11**'s HB01 clause and link 857 (GT11 labels the holographic bound S ≤ A/4 as the Bekenstein bound). |
| 20 | Also in IT02 *What It Claims* and links 700, 716, 754. |
| 21 | Also in link 715 (HB01→HB03): "E·R ~ R²" holds only at the edge of collapse. |
| 23 | Confirmed from Van Raamsdonk 2010: less entanglement means longer distance and *smaller* area. Also in link 800. |
| 25 | Confirmed from Wall 2012 (abstract and §2.5): semiclassical; axioms checked for free fields and 1+1 CFTs; monotonicity of *quantum* relative entropy on the horizon. Anchor error confirmed on Crossref. |
| 27 | GT05 says "Carney estimates that current technology is within an order of magnitude". **No such statement is in the paper**; it says "nearly observable" (Eq. 51, ~10⁻²⁴ N/√Hz). |
| 9 | All three anchor errors confirmed on Crossref and arXiv (§3.3). |

## 2. Primary sources read by this session

Markers are upgraded only where this session read the text itself (PDF text extraction, specific passages located and read).

| Source | Read this session | Settles items |
|---|---|---|
| Jacobson 2016, PRL 116:201101, arXiv:1505.04753 **v4** | **full text** | 1, 2, 3, 4, 5, 14 (no Padmanabhan) |
| Jacobson 1995, PRL 75:1260, arXiv:gr-qc/9504004 v2 | **full text** | 2, 6, 7, 8 |
| Verlinde 2011, JHEP 04:029, arXiv:1001.0785 | **full text** (searched; G definition, ΔS postulate, gravitons absent) | 12 |
| Padmanabhan 2012, arXiv:1206.4916 | **full text** | 13 |
| Bianconi 2025, PRD 111:066001, arXiv:2408.14391 **v7** | **full text** (searched for Fisher, network, transport, quantization) | 16 |
| Visser 2002, MPLA 17:977, gr-qc/0204062 | **full text** (setup, Eq. 9) | 17 |
| Kabat 1995, NPB 453:281, hep-th/9503016 | abstract + c₁ table | 17, 20 |
| Eling, Guedens & Jacobson 2006, PRL 96:121301, gr-qc/0602001 | **full text** | 7, 18 |
| Chirco & Liberati 2010, PRD 81:024016, arXiv:0909.4194 | **full text** (passages) | 18 |
| Casini 2008, CQG 25:205021, arXiv:0804.2182 | abstract + introduction | 19 |
| Van Raamsdonk 2010, GRG 42:2323, arXiv:1005.3035 | **full text** (essay) | 23 |
| Wall 2012, PRD 85:104049, arXiv:1105.3445 | abstract + §2.5 | 25 |
| Almheiri et al. 2021, RMP 93:035002, arXiv:2006.06872 | abstract + passages | 22 |
| Kobakhidze 2011, arXiv:1009.5414 | **full text** (short note) | 11 |
| Visser 2011, JHEP 10:140, arXiv:1108.5240 | **full text** (searched) | 11 |
| Brouwer et al. 2017, MNRAS 466:2547, arXiv:1612.03034 | abstract + §1 | 10 |
| Carney et al. 2025, PRX 15:031038, arXiv:2502.17575 | **full text** (Eq. 51, Fig. 5) | 27 |
| Alonso-Serrano & Liška 2020, PRD 102:104056, arXiv:2008.04805 | abstract | 6 |
| Strominger & Vafa 1996; Chaichian et al. 2011; Lelli et al. 2017; Hees et al. 2017; Halenka & Miller 2020; Brouwer et al. 2021; Schimmoller et al. 2021; Dai & Stojkovic (JHEP 2017, PRD 2017); Yoon 2020 | abstract (arXiv API) | 10, 11, 20 |
| Crossref: 10.1103/PhysRevD.80.124008; 10.1088/1126-6708/2009/06/021; 10.1007/JHEP11(2017)007; 10.1103/PhysRevD.96.108501; 10.1103/PhysRevD.95.124018; 10.1103/PhysRevD.85.104049; 10.1103/PhysRevD.102.104056; 10.1103/PhysRevResearch.3.033065 | metadata | 9, 25 |

**Not re-read** (kept at the map's level): Wald 2001, Carlip 2014, Susskind & Uglum 1994, Jacobson 1994, Bousso 1999, Speranza 2016, Casini–Galante–Myers 2016 (body), Westphal 2021 and Fuchs 2024 (the sensor figures in item 27).

## 3. The proposed writes

**Format** (QR-004 precedent):
- **Entry text:** a dated banner goes **after** the wrong text, which stays unchanged above it: `> **CORRECTION 2026-10-19 (gsw-qr005-corrections-2026-10-19).** … *The text above is unchanged.*`
- **Links:** `[Corrected 2026-10-19, gsw-qr005-corrections-2026-10-19] <new text>. Previously: "<old text>"`. Link types and endpoints are not changed.
- **Hygiene:** GT03's duplicated paragraph and six duplicated concept-tag lines are removed (exact duplicates, so no content is lost).

### 3.1 Section banners (67), by item

| # | Where | Severity | Tag |
|---|---|---|---|
| C1 | GT10 What It Claims, Constraint Category, What The Math Says | E | emergent-read-as-classical |
| C2 | GT10 Mathematical Form, DS Cross-Refs (GT01 clause); link 851 | E | emergent-read-as-classical |
| C3 | GT10 Constraint Category, DS Cross-Refs (HB07 clause); link 853 | E | — |
| C4 | GT10 DS Cross-Refs (IT03 clause); link 855 | E | vocabulary-stacking-analogy |
| C5 | GT10 Mathematical Form | Q | — |
| C6 | GT01 What The Math Says | E | — |
| C7 | GT01 What It Claims, Constraint Category | Q | emergent-read-as-classical |
| C8 | GT01 DS Cross-Refs (TD3 clause) | Q | — |
| C9–C11 | GT02 What It Claims (status paragraph); anchors 852–856 | E (attribution) / Q | — |
| C12 | GT02 What It Claims, Mathematical Form, What The Math Says, DS Cross-Refs; link 742 | Q | emergent-read-as-classical |
| C13 | GT03 What It Claims, Mathematical Form, Mathematical Archetype, What The Math Says | E | — |
| C14 | GT03 Constraint Category, DS Cross-Refs, Archetype, What The Math Says; links 852, 866 | Q | vocabulary-stacking-analogy |
| C15 | GT03 What It Claims, Concept Tags (dedupe) | H | — |
| C16 | GT04 (6 sections); the Bianconi clause in GT01, GT02, GT05, IT04 ×2, IT08 ×2, RG06 ×2, BR03, BR04 ×2; links 706, 747, 748, 775, 805; anchor 837 | E | vocabulary-stacking-analogy |
| C17 | GT06 Constraint Category, Mathematical Form, What The Math Says; link 754 | Q / E (formula) | emergent-read-as-classical |
| C18 | GT07 (5 sections) | E / H | vocabulary-stacking-analogy (parallels) |
| C19 | HB01 What It Claims, Constraint Category, What The Math Says; GT11 DS Cross-Refs; links 713, 857 | E / Q | — |
| C20 | HB02 What It Claims, DS Cross-Refs; IT02 What It Claims, DS Cross-Refs; links 700, 716 | E / Q | — |
| C21 | HB03 What It Claims, DS Cross-Refs; link 715 | H / Q | — |
| C22 | HB04 What It Claims | E | — |
| C23 | BR03 What It Claims, What The Math Says, DS Cross-Refs; HB07 DS Cross-Refs; link 800 | E | — |
| C24 | BR01 What The Math Says, Mathematical Archetype; BR03 (thermofield double) | Q / H | — |
| C25 | HB09 (5 sections); link 812; anchor 422 | Q; anchor E | vocabulary-stacking-analogy |
| C26 | IT05 What It Claims | Q | vocabulary-stacking-analogy |
| C27 | GT05 What The Math Says; `CCA_GRAVITY_FINDINGS.md` §1.1 Hops 2–4 (doc banner) | Q / E | — |

### 3.2 `docs/CCA_GRAVITY_FINDINGS.md` (doc edit; dated banner, body unchanged)

A banner after §1.1 Hop 4 records three things:
- **Hop 2:** the identity is right (Fisher information is the Hessian of KL divergence), but it is not the Cramér–Rao bound, which bounds an estimator's variance by the inverse Fisher information.
- **Hop 3:** it rests on the first law of entanglement, which holds whether or not Einstein's equation does, and the quantity is quantum relative entropy, not KL divergence.
- **Hop 4:** there is no "classical limit" in Jacobson 2016; both derivations are semiclassical, and "zero additional assumptions" falls with it.

A one-line note also goes on the 2026-05-04 banner's Bianconi bullet: the paper uses no Bures metric either.

### 3.3 Anchors (`wiki_history.db`)

| Anchor | Now | Proposed |
|---|---|---|
| 422 (HB09) | "Wall 2009 Ten proofs…", doi:10.1103/PhysRevD.80.124008, which is **Guica, Hartman, Song & Strominger, "The Kerr/CFT correspondence"** | Identifier → 10.1088/1126-6708/2009/06/021 (JHEP 06 (2009) 021; Crossref). Role progenitor → comprehensive_survey (Bekenstein 1973 is the progenitor). The note records the old DOI. |
| 855 (GT02) | "Hossenfelder 2017 - Inconsistencies…", doi:10.1007/JHEP11(2017)007 | Title → Dai & Stojkovic 2017 (the DOI is right; the authors were wrong). |
| 856 (GT02) | "Hossenfelder 2017 - A covariant version…", arXiv:1706.07854 | Title → Dai & Stojkovic, arXiv preprint of PRD 96:108501. |
| new (GT02) | — | Hossenfelder 2017, PRD 95:124018 (arXiv:1703.01415), `adjacent_concept`. |
| new (HB09) | — | Wall 2012, PRD 85:104049, `cites`. |
| 837, 388, 852, 853, 854 | notes repeat corrected claims | Correction note appended (the original note is kept). |

**Owner choice on 422:** fix the identifier in place (recommended: no earlier pass has done this, but an anchor whose DOI points at another paper is a typo, not a claim to preserve, and the old value stays in the note), or keep the wrong row, mark it low-confidence and add a new one.

## 4. Calibration (append-only; no label changes)

| Entity | Label | Why a row |
|---|---|---|
| `fisher_gravity_chain` | Speculative (unchanged) | Three of the four hop descriptions are wrong as written. Hop 3 is vacuous: the KL/relative-entropy variation is zero for any state. The label stays because the chain is already recorded as a conceptual analogy, not a theorem chain. *Alternative for the owner:* a stronger label, e.g. Falsified as a structural chain. Not recommended, since no current row claims it is structural. |
| GT04 | Speculative (unchanged) | The paper uses no Fisher metric; the 2026-05-04 "Bures" row was an inference. |
| GT02 | Speculative (unchanged) | The 2026-05-04 row repeats the Hossenfelder misattribution; Verlinde 2011 and 2016 are separated; the Halenka & Miller nuance. |
| GT10 | Supported (unchanged) | "Linearized only" restated precisely: first-order variations of the local vacuum state; semiclassical; no holography; silent on gravitons. **Item 4 does not touch GT10's label**: it concerns the wiki's GT10→IT03 link, not Jacobson's result. |

Claim counts are unchanged: 26 Speculative · 5 Supported · 7 Established · 5 Falsified · 4 Retired.

## 5. Left out, recorded as follow-ups

- **Link 869** (GT10 → HB09): "the Einstein equation is the fixed point of the entropy-increasing process the GSL governs". Unsourced and speculative; not in the map.
- **Link 714** (HB01 → HB02): mixes Bekenstein's GSL argument with the collapse argument. Covered in substance by the HB01 banner; the link is not changed.
- **BR01's `mathematical_archetype` facet** (conservation-law) does not fit; it goes to the archetype review.
- **Facet values:** many gravity entries carry `dimensional_sensitivity: D-sensitive` on the Ω_D posit (CLAUDE.md open item 11).
- **Fold-in candidates:** R7–R14 (map §G).

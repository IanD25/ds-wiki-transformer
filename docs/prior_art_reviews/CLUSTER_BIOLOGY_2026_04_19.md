# Prior-Art Gate — Biology Cluster

**Date:** 2026-04-19
**Scope:** 16 entries — BIO2-11 + D1 + F1-5
**Template seed:** C1, BIO1 (anchored 2026-04-18) provide WBE 1997 / Schmidt-Nielsen / Mendel / Griffiths-genetics basis.

---

## Two-axis split: anchor vs internal_construction

After reading entry content for F4 and F5:

**Anchor (14 entries):** BIO2-11, D1, F1, F2, F3
**Flag as `internal_construction` (2 entries):** F4, F5

| ID | Title | Why IC |
|---|---|---|
| F4 | Saturation Dynamics (Consolidated) | Wiki-internal consolidation of three saturation forms (Michaelis-Menten, Logistic, Hyperbolic). The underlying physics is real and each form has its own canonical literature, but the *named* meta-pattern "F4 Saturation Dynamics" is a wiki-construct — not citable as a single source. |
| F5 | Oxygen Viability Corridor | AlphaEntropy/CcO-program-specific PO2 corridor with hysteretic boundaries. Specific bounds (~1-3 mmHg / ~50-100 mmHg) tied to wiki's CcO conjecture program. Owner-derived corridor specifics, not standalone literature. |

---

## Anchor map (14 entries)

### Genetics / Evolution
| Entry | Title | Progenitor |
|---|---|---|
| BIO2 | Hardy-Weinberg | Hardy 1908 *Science* 28, 49 (DOI 10.1126/science.28.706.49); Weinberg 1908 (no DOI) |
| BIO3 | Fisher's Fundamental Theorem | Fisher 1930 *The Genetical Theory of Natural Selection* (book; ISBN 978-0198504405 medium) |
| BIO8 | Neutral Theory | Kimura 1968 *Nature* 217, 624 (DOI 10.1038/217624a0) |
| BIO11 | Molecular Clock | Zuckerkandl-Pauling 1965 chapter (no DOI) — anchored via Hartl-Clark; cites Kimura 1968 |

Shared textbook: Hartl-Clark *Principles of Population Genetics* 4th ed (ISBN 978-0878933082, medium).
Reuse: Griffiths *Introduction to Genetic Analysis* (978-1319114770, verified BIO1).

### Cell / Molecular Biology
| Entry | Title | Progenitor |
|---|---|---|
| BIO4 | Cell Theory | Schleiden 1838 + Schwann 1839 (no modern DOIs) — anchor via Alberts |
| BIO5 | Central Dogma | Crick 1970 *Nature* 227, 561 (DOI 10.1038/227561a0); Crick 1958 chapter |
| BIO6 | Michaelis-Menten | Michaelis-Menten 1913 *Biochem. Z.* 49, 333; Johnson-Goody 2011 reissue *Biochemistry* 50, 8264 (DOI 10.1021/bi201284u) |

Shared textbook: Alberts et al. *Molecular Biology of the Cell* 6th ed (ISBN 978-0815344322, medium).

### Ecology / Math Biology
| Entry | Title | Progenitor |
|---|---|---|
| BIO7 | Lotka-Volterra | Lotka 1925 *Elements of Physical Biology* (book); Volterra 1926 *Mem. Acad. Lincei* (no DOI) |

Textbook: Murray *Mathematical Biology* 3rd ed (ISBN 978-0387952239, medium).

### Physiology / Neuroscience
| Entry | Title | Progenitor |
|---|---|---|
| BIO9 | Hodgkin-Huxley | Hodgkin-Huxley 1952 *J. Physiol.* 117, 500 (DOI 10.1113/jphysiol.1952.sp004764) |
| BIO10 | Homeostasis | Cannon 1929 *Physiol. Rev.* 9, 399 (DOI 10.1152/physrev.1929.9.3.399) |

Textbook: Kandel et al. *Principles of Neural Science* 6th ed (ISBN 978-1259642234, medium).

### Psychophysics
| Entry | Title | Progenitor |
|---|---|---|
| D1 | Stevens' Power Law | Stevens 1957 *Psychol. Rev.* 64, 153 (DOI 10.1037/h0046162) |

### Constraint Laws (F1-3)
| Entry | Title | Progenitor |
|---|---|---|
| F1 | Ashby's Law of Requisite Variety | Ashby 1956 *Introduction to Cybernetics* (book; ISBN 978-0412197604, medium) |
| F2 | Liebig's Law of the Minimum | Liebig 1840 *Organic Chemistry in Its Application to Agriculture* (no DOI) — anchored via ecology textbook (Begon ISBN 978-1405151986, medium) |
| F3 | Gause's Competitive Exclusion | Gause 1934 *The Struggle for Existence* (book; reprint ISBN 978-1605209708, medium) |

---

## Confidence policy applied
- DOIs in recognized publisher patterns → `high`
- Pre-DOI books → anchor via verified-or-flagged ISBN, mark `medium` if ISBN claimed from memory
- Wikipedia → `medium` (no oldid this session)
- Schmidt-Nielsen / WBE 1997 / Griffiths-genetics ISBNs reused from C1+BIO1 are `high`

## Pending follow-ups
- WorldCat-verify new ISBNs: Alberts, Hartl-Clark, Murray, Kandel, Fisher 1930, Begon, Ashby, Gause reprint
- Wikipedia oldid backfill (continues)
- Several pre-DOI papers (Lotka 1925, Volterra 1926, Schleiden 1838, Schwann 1839, Liebig 1840, Zuckerkandl-Pauling 1965) anchored via textbook citation only

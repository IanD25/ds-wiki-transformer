# Prior-Art Gate — Tier 1 Batch — CM1, GV1, AM5

**Date:** 2026-04-18
**Scope:** 3 Tier-1 canonical entries across 3 different domains/sub-domains
**Purpose:** Second live anchor batch (after INFO1). Stress-tests the basket across physics.classical / physics.cosmology / math-physics bridge. Fills the `comprehensive_survey` slot for the first time.

---

## Entries in this batch

| ID | Title | Primary domain | Verdict |
|---|---|---|---|
| `CM1` | Newton's Laws of Motion | `physics.classical` | CANONICAL_TIER_1_ESTABLISHED |
| `GV1` | General Relativity — Einstein Field Equations | `physics.cosmology` | CANONICAL_TIER_1_ESTABLISHED |
| `AM5` | Noether's Theorem | `physics.classical` | CANONICAL_TIER_1_ESTABLISHED |

None are novelty claims; each is a faithful Tier-1 reference_law. Gate verdict for each: assemble canonical external anchors and insert.

---

## CM1 — Newton's Laws of Motion

Six anchors proposed; 3 of 5 canonicity slots filled.

| # | Source | Identifier | Tier | Stability | Role | Notes |
|---|---|---|---|---|---|---|
| 1 | `isbn` | 978-0520088177 | 1 | canonical | `progenitor` | Cohen-Whitman translation of Newton's *Philosophiae Naturalis Principia Mathematica* (1687), UC Press 1999. Contains the three axioms verbatim. |
| 2 | `isbn` | 978-0201657029 | 1 | canonical | `standard_textbook` | Goldstein, Poole & Safko, *Classical Mechanics* (3rd ed., 2001) — standard graduate textbook. |
| 3 | `isbn` | 978-1891389221 | 1 | canonical | `standard_textbook` | Taylor, *Classical Mechanics* (2005) — standard undergraduate textbook. |
| 4 | `wikipedia` | Newton's_laws_of_motion, oldid 1349645204 | 2 | active-literature | `living_reference` | Article verified via WebFetch. Three laws presented verbatim from Newton; F = dp/dt emphasized. |
| 5 | `scholarpedia` | /article/Newton's_laws | 1 | canonical | `living_reference` | Scholarpedia article confirmed via WebSearch; direct fetch timed out (flaky, known). Confidence `medium` pending re-fetch. |
| 6 | `mathworld` | /FormOfNewtonsLaws.html (and related) | 2 | canonical | `living_reference` | MathWorld covers Newton's laws under several pages; primarily for math-adjacent treatment. |

**Slots:** progenitor ✓, standard_textbook ✓ (×2), living_reference ✓ (×3)
**Empty:** axiomatic_foundation (the *Principia* itself serves as both progenitor and axiomatic foundation — modern reformulations like Mach 1883 exist but are not canonical), comprehensive_survey (textbooks cover this for such a mature topic).

---

## GV1 — General Relativity / Einstein Field Equations

Seven anchors proposed; 3 of 5 canonicity slots filled (4 if MTW is counted as axiomatic_foundation separate from standard_textbook).

| # | Source | Identifier | Tier | Stability | Role | Notes |
|---|---|---|---|---|---|---|
| 1 | `ads` | 1915SPAW.......844E | 1 | canonical | `progenitor` | Einstein 1915 "Die Feldgleichungen der Gravitation," *Sitzungsberichte der Preussischen Akademie der Wissenschaften zu Berlin*, pp. 844-847 (Nov 25, 1915). No DOI (predates DOI system); anchored via NASA ADS bibcode. |
| 2 | `doi` | 10.1002/andp.19163540702 | 1 | canonical | `progenitor` | Einstein 1916 "Die Grundlage der allgemeinen Relativitätstheorie," *Annalen der Physik* 354(7), pp. 769-822. Definitive long-form exposition; verified via CrossRef. |
| 3 | `isbn` | 978-0716703440 | 1 | canonical | `standard_textbook` | Misner, Thorne, Wheeler, *Gravitation* (1973) — "MTW"; canonical GR reference. |
| 4 | `isbn` | 978-0226870335 | 1 | canonical | `standard_textbook` | Wald, *General Relativity* (1984) — rigorous mathematical treatment; alternative to MTW. |
| 5 | `isbn` | 978-0805387322 | 1 | canonical | `standard_textbook` | Carroll, *Spacetime and Geometry* (2004) — modern standard. |
| 6 | `wikipedia` | Einstein_field_equations, oldid 1347658026 | 2 | active-literature | `living_reference` | Article verified via WebFetch. EFE stated as G_μν + Λ g_μν = κ T_μν, κ = 8πG/c⁴. Full Einstein 1915/1916 citations present. |
| 7 | `scholarpedia` | /article/Einstein_field_equations | 1 | canonical | `living_reference` | Scholarpedia article; direct fetch timed out. Confidence `medium` pending re-fetch. |

**Slots:** progenitor ✓ (×2), standard_textbook ✓ (×3), living_reference ✓ (×2)
**Empty:** axiomatic_foundation (arguably filled by Wald Ch. 4 or MTW Ch. 17, already in standard_textbook), comprehensive_survey (Living Reviews in Relativity covers subtopics; no single article anchors the full EFE).

---

## AM5 — Noether's Theorem

Six anchors proposed; 4 of 5 canonicity slots filled — **first batch to fill `comprehensive_survey`**.

| # | Source | Identifier | Tier | Stability | Role | Notes |
|---|---|---|---|---|---|---|
| 1 | `doi` | 10.1080/00411457108231446 | 1 | canonical | `progenitor` | Noether 1918 "Invariante Variationsprobleme," Nachr. Ges. Wiss. Göttingen, pp. 235-257. English translation by Tavel 1971, *Transport Theory and Statistical Physics* 1(3), 186-207. Verified via CrossRef. |
| 2 | `isbn` | 978-0201657029 | 1 | canonical | `standard_textbook` | Goldstein, *Classical Mechanics* (3rd ed., 2001) — treats Noether's theorem in Ch. 2/13. |
| 3 | `isbn` | 978-0387968902 | 1 | canonical | `standard_textbook` | Arnold, *Mathematical Methods of Classical Mechanics* (2nd ed., 1989) — rigorous symplectic-geometric treatment. |
| 4 | `isbn` | 978-0387878676 | 1 | canonical | `comprehensive_survey` | Kosmann-Schwarzbach, *The Noether Theorems: Invariance and Conservation Laws in the Twentieth Century* (Springer 2011) — definitive scholarly survey. |
| 5 | `wikipedia` | Noether%27s_theorem, oldid 1348624666 | 2 | active-literature | `living_reference` | Article verified via WebFetch. First theorem + second theorem distinguished; Noether 1918 citation present. |
| 6 | `scholarpedia` | /article/Noether%27s_theorem | 1 | canonical | `living_reference` | Direct fetch timed out. Confidence `medium` pending re-fetch. |

**Slots:** progenitor ✓, standard_textbook ✓ (×2), living_reference ✓ (×2), comprehensive_survey ✓ (first time in any batch!)
**Empty:** axiomatic_foundation (Noether's own paper serves both roles).

---

## Summary

**Totals:** 19 anchors across 3 entries

| Entry | Anchors | Slots filled |
|---|---|---|
| CM1 | 6 | 3/5 (progenitor, standard_textbook, living_reference) |
| GV1 | 7 | 3/5 (progenitor, standard_textbook, living_reference) |
| AM5 | 6 | **4/5** (progenitor, standard_textbook, living_reference, **comprehensive_survey**) |

**Canonicity-slot coverage across all 3:**
- progenitor: 4 anchors (CM1 Principia, GV1 Einstein 1915+1916, AM5 Noether 1918)
- axiomatic_foundation: 0 anchors (for each of these three, the original publication fills both roles, so this slot stays empty honestly)
- standard_textbook: 7 anchors (Goldstein appears twice — CM1 and AM5; MTW + Wald + Carroll for GR; Taylor for CM1; Arnold for AM5)
- living_reference: 7 anchors (Wikipedia + Scholarpedia each ×3; MathWorld for CM1)
- comprehensive_survey: 1 anchor (Kosmann-Schwarzbach for Noether — new slot filled for the first time)

**New source enum values used for the first time:** `ads` (Einstein 1915 bibcode)

**Scholarpedia reliability note:** 3/3 Scholarpedia fetches timed out this batch, same as INFO1 run. Confirms flaky — confidence=medium on all 3 pending batched retry.

---

## Net effect of this batch

- **Active anchor coverage:** 1 entry → 4 entries (INFO1 + CM1 + GV1 + AM5)
- **Total external_anchor rows:** 8 → 27
- **First `comprehensive_survey` anchor** lands
- **First `ads` source anchor** lands
- **Pattern stable** — workflow works across domains, scaffolds for remaining retrospective pass

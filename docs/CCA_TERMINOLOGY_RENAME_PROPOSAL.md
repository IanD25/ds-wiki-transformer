# CCA Terminology Rename Proposal

> **Status:** Proposal awaiting owner sign-off. Created 2026-04-08 as part of the M0 audit closeout.
> **Anchor:** `docs/M0_MILESTONE_COMPILATION.md` Fourth + Fifth + Sixth Addenda identified two terminology collisions that must be addressed before any external CCA writeup. This document proposes specific replacements and provides an implementation checklist.
> **Scope:** Documentation and notation only — no behavioral changes to any code, no DB schema changes. The renames are scholarly hygiene, not novelty challenges.

---

## TL;DR

Two CCA observables share symbols with established physics terminology that means something else. **Both must be renamed before CCA is written up externally**, because external readers familiar with the established terminology will assume CCA's symbols mean the established things.

| Current CCA symbol | What CCA means | What the same symbol means in established physics | Recommended rename |
|---|---|---|---|
| **d_eff** | Participation ratio (Σλ)²/Σλ² of the FIM eigenvalue spectrum | **Mattingly et al. 2018 PNAS**: Σ_r r·Ω_r, weighted boundary dimensionality from optimal maximum-information prior | **PR_FIM** (with formula given on first use) |
| **η** | Isotropy indicator on FIM eigenvalue distribution (loose definition; see "What is η_CCA actually?" below) | **Standard stat-mech**: anomalous dimension of two-point function, C(r) ~ r^(-(d-2+η)). For 2D Ising universality class, η = 1/4. | **ι** (iota for isotropy), or **iso_FIM** |

Both renames are mandatory for external work; either rename alone is acceptable for internal work, but doing both at once is cleaner.

---

## Why this matters

**Terminology collisions are cheap to prevent and expensive to fix later.** External reviewers reading "d_eff" or "η" in a CCA writeup will, with very high probability, assume those symbols mean the established things — Mattingly's prior-weight-by-dimension and the standard η critical exponent respectively. They will then either:

1. Be confused for several pages until they realize the symbols mean something different, then form a negative impression of the work's scholarly hygiene; or
2. Misread results because they're applying the wrong mental model; or
3. Cite a "novelty challenge" that doesn't actually exist, because they assumed the symbols meant the prior-art definitions.

All three outcomes are avoidable with a one-line "we use $X$ to denote ... not to be confused with the standard usage" footnote, plus a consistent symbol choice. **The audit found this is the second-most-important hygiene item after the prior-art reading**, ahead of the experimental work.

It is also worth noting: **CCA's η at criticality is mathematically related to the standard η_critical** because the FIM IS the connected correlation matrix and its spectrum is governed by the standard η at the critical point. So the symbols don't just collide — they collide in a way that makes the related-but-different distinction harder to communicate. This makes the rename more important, not less.

---

## Collision 1: `d_eff` (CCA) vs `d_eff` (Mattingly 2018)

### Established definition (Mattingly 2018)

**Source**: Mattingly, Transtrum, Abbott, Machta, *"Maximizing the information learned from finite data selects a simple model,"* PNAS 115, 1760 (2018), arXiv:1705.01166.

In Figure 4C and surrounding text, the paper defines:

$$d_\text{eff} = \sum_{r=1}^{D} r \cdot \Omega_r$$

where $\Omega_r$ is the total weight of the optimal maximally informative discrete prior $p_\star(\theta)$ on edges of dimension $r$ of the parameter manifold. As measurement noise σ decreases (more data), $d_\text{eff}$ grows smoothly from 0 toward the full parameter-space dimension $D$, corresponding to weight migrating from lower-dimensional boundaries into the interior.

This is in the Sethna sloppy-models lineage and is well-established Sethna-group terminology since 2018.

### CCA's definition

CCA's $d_\text{eff}$ is the **participation ratio** of the Fisher Information Matrix eigenvalue spectrum:

$$d_\text{eff}^\text{CCA} = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}$$

This is the standard random-matrix / deep-learning participation-ratio definition (cf. Karakida-Akaho-Amari 2019 for FIM applications in neural networks).

### Why the collision matters

Both are scalar observables. Both are called "d_eff." Both measure "effective dimensionality" in a sloppy-models sense. **They are different formulas.** Mattingly's grows from 0 to D as data improves; CCA's varies based on eigenvalue concentration. They have different scaling behaviors and different physical interpretations.

A reader familiar with Mattingly 2018 (which is in the canonical sloppy-models lineage every reviewer would know) will assume CCA's d_eff is the same observable. It isn't.

### Recommended rename

**Primary recommendation: `PR_FIM`** (participation ratio of the Fisher Information Matrix).

Rationale:
- **Unambiguous**: directly names the mathematical object. No collision risk.
- **Connects to established literature**: "participation ratio" is standard in random matrix theory, Anderson localization, and the deep-learning FIM-spectrum literature (Karakida 2019). External readers will immediately recognize the term.
- **Compact**: short enough to use repeatedly in equations.
- **Subscript flexibility**: PR_FIM(T) for the temperature-dependent version is clean.

**Alternative: `λ_eff`** (effective number of stiff eigenvalues). Less ideal — still has the "eff" overlap with Mattingly's d_eff and might still confuse.

**Alternative: `D_PR`** (capital D for dimensionality, PR subscript for participation ratio). Acceptable; slightly more typographically heavy.

### Where the rename needs to be applied

In `docs/CCA_MATHEMATICAL_FORMALIZATION.md`:
- Definition section (wherever d_eff is defined)
- All theorem/lemma statements involving d_eff
- All experimental-result paragraphs (Phase A, B, C, D)
- Figure captions and labels

In `docs/CCA_GRAVITY_FINDINGS.md`:
- Any reference to d_eff in the Fisher-gravity discussion

In experiment scripts (`scripts/ising_fim_*.py`, `scripts/cca1b_*.py`):
- Variable names containing `d_eff` should be renamed to `pr_fim` for clarity (this is documentation code, not behavioral code, so the rename is purely for readability)

In wiki entries and conjectures referencing CCA observables:
- P5 discussion (the broader "Fisher rank = D_eff" framing predates CCA and uses a different D_eff — the Wiki's existing Ax2 / M6 / D_eff terminology is its own framework; check carefully whether wiki D_eff is meant in the Mattingly sense, the participation-ratio sense, or yet a third sense)
- CCA-related conjecture entries (CCA-1, CCA-1b, CCA-1c, CCA-2)

**Compatibility note**: the Wiki has its own `D_eff` (capital D) entry (Ax2 / M6 in the conjecture chain). That predates the CCA framework and refers to a more general "effective dimensionality" concept. **The wiki's D_eff and CCA's d_eff are not necessarily the same observable** — this is yet a third definition collision. Resolving the wiki D_eff question is a separate, larger task; for now the CCA rename to PR_FIM keeps CCA's terminology unambiguous regardless of how the wiki D_eff question resolves.

---

## Collision 2: `η` (CCA) vs `η` (standard stat-mech)

### Established definition (textbook stat mech)

**The standard η critical exponent** is the anomalous dimension of the two-point correlation function:

$$C(r) \sim r^{-(d-2+\eta)} \quad \text{at criticality}$$

For 2D Ising universality class, η = 1/4 (exact).
For 2D Potts q=3, η = 4/15.
For 2D Potts q=4, η = 1/4.
For 2D Potts q≥5, the transition is first-order and η is not defined in the usual sense.

This is in every stat-mech textbook (Goldenfeld 1992, Cardy 1996, Henkel 1999, etc.). Any working physicist reads "η" in a 2D Ising context and assumes the anomalous dimension.

### CCA's definition

CCA's η is **an isotropy indicator on the FIM eigenvalue spectrum**. The exact mathematical form depends on which version of CCA — see "What is η_CCA actually?" below. Roughly, it captures "how spread out is the eigenvalue spectrum beyond the dominant direction" — high η means many comparable eigenvalues (isotropic spectrum); low η means spectrum dominated by one direction (radial/spotlight).

### Why the collision matters worse than collision 1

This collision is more dangerous than the d_eff one because **the two η's are mathematically related**. Specifically:

- The FIM in CCA IS the connected correlation matrix χ_ij (Fifth Addendum finding)
- Vinayak-Prosen-Buča-Seligman 2014 EPL proves that the eigenvalue density of the connected correlation matrix at 2D Ising criticality is a power-law derivable from the standard η critical exponent
- Therefore, **CCA's η at criticality is some function of standard η_critical**

So a reader sees "η" in a CCA paper and assumes it means the anomalous dimension. They are not entirely wrong — at criticality, the CCA η IS controlled by the standard η. But the symbols don't refer to the same number, and at off-critical or first-order conditions they diverge entirely.

A reviewer who notices this overlap will likely say one of:
1. "Why aren't you just using the standard η? Your η is just a function of the standard one." (Partially valid critique, depending on what CCA-1c actually shows.)
2. "Your notation conflates two different objects that are related but distinct." (Definitely valid critique.)
3. "Your CCA η at first-order doesn't have a standard-η interpretation; you should rename to make this clear." (The right critique.)

### Recommended rename

**Primary recommendation: `ι` (lowercase iota)** for "isotropy indicator."

Rationale:
- **No collision**: ι is rarely used in stat mech and never for an anomalous dimension.
- **Mnemonic**: "iota" → "isotropy" is straightforward.
- **Greek letter consistency**: keeps CCA's notation in Greek alphabet (consistent with d_eff → PR_FIM only if you're flexible on alphabet; if you want strict Greek, see alternative below).
- **Visually distinct**: ι is unlikely to be confused with η in a paper.

**Alternative: `iso_FIM`** (isotropy of FIM). Latin acronym, more verbose, parallels PR_FIM.

**Alternative: `η_spec`** (with explicit subscript distinguishing it from η critical). Acceptable but the subscript is easy to drop in casual reference and the collision risk returns. Less ideal than full rename.

**Alternative: `α_CCA`** or similar Greek letter with explicit subscript. Acceptable but more verbose.

### Where the rename needs to be applied

Same locations as the d_eff → PR_FIM rename, plus:

- Phase C discussion of "isotropy = criticality" (CCA-1 falsified) — kept for historical record
- Phase D discussion of "dη/dT magnitude separation" — currently the most important CCA result; rename to dι/dT
- The "curve shape discriminator" (CCA-1c) language

Note that **CCA-1 was named "isotropy = criticality" but used η as the symbol** — this naming choice itself contributed to the terminology problem. Renaming to ι makes the conjecture name consistent with its symbol.

---

## What is η_CCA actually?

A separate concern that the rename forces us to confront: **the exact mathematical definition of η_CCA varies across CCA documents.** In some places it's described as λ₂/λ₁ (second-to-largest eigenvalue ratio). In others it's described as a more general "isotropy indicator." In still others it's vaguer.

**Before doing the rename**, the owner should pin down the definition explicitly. The recommended form depends on which version is canonical. Possible canonical forms:

1. **Top-eigenvalue ratio**: ι = λ₂/λ₁ where eigenvalues are ordered. Range [0, 1]. Captures "how much does the second direction matter relative to the first."
2. **Inverse participation ratio at the top**: ι = 1 - λ₁/Σλ. Range [0, 1]. Captures "what fraction of the spectrum is NOT in the top direction."
3. **Effective rank ratio**: ι = (rank with ε threshold) / N. Captures "fraction of directions that matter at threshold ε."
4. **Spectral entropy**: ι = -Σ(λᵢ/Σλ) log(λᵢ/Σλ) / log N. Range [0, 1]. Standard information-theoretic spread measure.

The owner's existing experiment scripts will reveal which form was actually used. **Pin this down before the rename**, then use the rename document to make the canonical form explicit.

The most defensible choice for external work is **option 4 (spectral entropy)**, because it's a standard information-theoretic measure with a clean interpretation. But the choice should match what the experiments actually computed.

---

## Implementation checklist

Once the renames are accepted:

- [ ] **Pin down the canonical η_CCA definition** by checking experiment scripts (scripts/ising_fim_*.py, scripts/cca1b_*.py). Write the formula explicitly in CCA_MATHEMATICAL_FORMALIZATION.md.
- [ ] **Apply d_eff → PR_FIM** in:
  - `docs/CCA_MATHEMATICAL_FORMALIZATION.md` (definitions + all subsequent uses)
  - `docs/CCA_GRAVITY_FINDINGS.md` (any references)
  - `docs/CCA_FORMALIZATION_SCOPE.md` (any references)
  - Variable names in experiment scripts (documentation only, not behavior)
- [ ] **Apply η → ι** in same locations, plus:
  - Conjecture names referencing "isotropy" (CCA-1 historical record, CCA-1b, CCA-1c)
  - All "dη/dT" references → "dι/dT"
- [ ] **Add a "Notation" section** to CCA_MATHEMATICAL_FORMALIZATION.md that explicitly:
  - Defines PR_FIM with formula
  - Defines ι with formula
  - States that PR_FIM should not be confused with Mattingly 2018's d_eff (cite Mattingly)
  - States that ι should not be confused with the standard η critical exponent (cite a standard textbook, e.g., Cardy 1996)
- [ ] **Migration script** to add a calibration record noting the renames are complete (audit_ref `M0_2026-04-08_terminology_rename`).
- [ ] **Update SESSION_HANDOVER_2026-04-08.md** to note the renames are complete and that CCA documents now use the unambiguous symbols.
- [ ] **Optional: rename in `wiki_history.db.confidence_calibration` rationales** for the entries that reference CCA's d_eff and η (CCA-1c, CCA-1b-magnitude, cca_d_eff_naming, cca_eta_naming). This is cosmetic — the historical records can stay as-is, with a note that the symbols have been updated.

---

## What the rename does NOT do

**It does NOT change the mathematical content of CCA.** Same observables, same experimental results, same conjecture status (CCA-1c remains Speculative, single-test, awaiting q=2,5,7,10 sweep).

**It does NOT resolve the M0 audit's open scientific questions.** The mechanism question (does CCA capture interfacial geometry, or something different?), the analytical-T_c-comparison check, and the q=2,5,7,10 experiment are all separate work.

**It does NOT touch `ds_wiki.db`.** The renames are in CCA documents and experiment-script variable names. The wiki's existing D_eff (capital D, in entry M6 / Ax2) is a separate framework predating CCA, and its relationship to CCA's PR_FIM is a separate question to resolve.

**It does NOT require any new primary-source reading.** The case for renaming is established by the audit; the renames themselves are mechanical.

---

## Why now

Three reasons to do this rename now rather than later:

1. **Cheap to do at this stage** (CCA documents are short; experiments are not deployed externally). Cost grows linearly with how much CCA content gets written before the rename.
2. **Required for any external writeup**, including direct correspondence with Saberi (the Sixth Addendum's recommended external reviewer). Saberi would notice the η collision immediately — he works in 2D Ising criticality where η=1/4 is the standard exponent.
3. **Forces the canonical-definition step** for η_CCA, which has been ambiguous across CCA documents. Pinning this down is independently valuable.

Three reasons to defer:

1. **Owner has not yet run the q=2,5,7,10 experiment.** If the experiment shows CCA-1c is fully reducible to standard critical exponents at all q, then CCA may not need an external writeup at all and the renames become moot.
2. **Owner has not yet read Vinayak 2014 or Borgs-Chayes 1996.** Those readings might reveal additional terminology issues to address simultaneously.
3. **Owner may want to redesign CCA's observables** based on the mechanism-question outcome, which would change what needs to be renamed.

**Recommendation**: defer the actual rename until after the owner has read Vinayak 2014 + Borgs-Chayes 1996 (1-2 days of work) but **pin down the canonical η_CCA definition now** (10 minutes from looking at the experiment scripts). The pin-down is cheap and removes the largest source of confusion in any future CCA discussion.

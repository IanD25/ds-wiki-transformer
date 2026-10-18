# Prior-Art Fold-In — 2026-10-18

**audit_ref:** `gsw-prior-art-fold-in-2026-10-18` · **Mode A** (curation / grounding) · no promotions
**Migrations:** `scripts/migrations/prior_art_fold_in_2026_10_18.py` (+ `prior_art_fold_in_data_2026_10_18.py`, the content) and `scripts/migrations/prior_art_fold_in_conjectures_2026_10_18.py`. Both are dry-run by default, idempotent and read-back verified. They were tested end-to-end and re-run on scratch copies of both databases before being applied.
**Owner decisions (2026-10-18, relayed from the parent session):** statuses as proposed, except IT10 and STAT6, which are contested until independently reproduced. Anchor 100 gets a correction note. P8 and P11 close as **Falsified** by the source they restated, not Folded. DEB is anchored to Sousa et al. 2008 as `comprehensive_survey`.

---

## 1. Why

The 2026-10-18 consistency pass found that the framework's "original" content mostly restates literature. P2 restates WBE 1997, P5 Machta 2013, P8 Gefen 1980 + JJK 2004, P11 Bettencourt, H5 West et al. 2003, and C2 Bettencourt 2013. The wiki recorded these as `reframing_of` anchors on the conjectures, but never added the prior art itself as knowledge. This pass adds it, as twelve `reference_law` entries written from the primary sources and linked to the content that restated or depends on them.

## 2. The twelve entries

"First-hand" means I read the passage myself, from the PDF text or a rendered page image. "Agent" means a background research agent read it and transcribed it verbatim with URLs. Every load-bearing quote and equation that appears in an entry was checked first-hand unless marked *(agent)*.

| ID | Source(s) | Status | What was read | Links added |
|---|---|---|---|---|
| **BIO12** West–Brown–Enquist network model | WBE 1997 *Science* 276:122; WBE 1999 *Science* 284:1677; Savage et al. 2008 | contested, Tier 2 † | WBE 1997 full text (agent; Eq. 5 context, assumptions and p. 126 D/(D+1) first-hand); WBE 1999 full text first-hand; Savage 2008 abstract only | P2 → derives from; → C1 predicts for; H5 → generalizes (H5's own claim); X1 → derives from; FM4 → implements |
| **BIO13** Allometric cascade + sum rule | Darveau et al. 2002 *Nature* 417:166; West et al. 2003 *Nature* 421:713; Banavar et al. 2003 *Nature* 421:713; Darveau reply 421:714 | contested, Tier 2 † | all full text (agent); West 2003 published wording, Banavar "weighted average" and "flawed" quotes first-hand; West preprint read in the H5 gate | H5 → derives from; → BIO12 tensions with |
| **BIO14** Metabolic-level boundaries hypothesis | Glazier 2005 *Biol. Rev.* 80:611; Glazier 2010 *Biol. Rev.* 85:111 | contested, Tier 2 † | both full text (agent); 2010 abstract wording and Eqs. 2–3 first-hand | → C1 predicts for; H5 → analogous to; → BIO12 tensions with; → BIO15 derives from |
| **BIO15** DEB theory and scaling | Sousa, Domingos & Kooijman 2008 *Phil. Trans. B* 363:2453; Maino et al. 2014 *J. Anim. Ecol.* 83:20 | contested, Tier 2 † | Sousa full text HTML (agent; proof appendix not read); Maino published abstract + July 2012 manuscript (agent; manuscript lines first-hand); **Kooijman 2010 book not read** | → C1 predicts for; H5 → couples to; → BIO12 tensions with |
| **BIO16** Natural selection and Fisher information | Frank 2009 *J. Evol. Biol.* 22:231 | established, Tier 2 | full text first-hand (journal reprint; Eqs. 5, 14, 17 on page images) | → BIO3 derives from; → IT05 derives from |
| **URB1** Origins of scaling in cities | Bettencourt 2013 *Science* 340:1438 | contested, Tier 2 † | full text + SM first-hand; critiques (Arcaute 2015, Leitão 2016, Shalizi 2011) abstracts only (agent) | → C2 predicts for; P11 → tensions with; → BIO12 analogous to |
| **IT09** Sloppy models / parameter-space compression | Machta et al. 2013 *Science* 342:604; Transtrum et al. 2015 *JCP* 143:010901; Quinn et al. 2023 *RPP* 86:035901 | established, Tier 2 | Machta published full text + arXiv SM (quotes first-hand); Transtrum arXiv v1 (agent); Quinn arXiv v2 (agent); **Machta erratum (Science 342:931) not read** | P5 → derives from; M6 → derives from; → IT05 derives from; → RG01 couples to |
| **STAT4** Critical phenomena on fractal lattices | Gefen, Mandelbrot & Aharony 1980 *PRL* 45:855 | established, Tier 1 | full text (4-page scan) — abstract, ramification rule, gasket set-up first-hand; gasket fixed-point result and carpet values (agent) | P8 → derives from; → T5 constrains; → Gate G5 tests; → RG03 derives from |
| **IT10** Information geometry of phase transitions | Janke, Johnston & Kenna 2004 *Physica A* 336:181 | **contested, Tier 2 †** (single study) | full text (arXiv) first-hand | P8 → couples to; → IT08 derives from; → BR04 couples to |
| **STAT5** Correlation-matrix spectra at criticality | Vinayak et al. 2014 *EPL* 108:20006; Borgs & Chayes 1996 *J. Stat. Phys.* 82:1235 | established, Tier 2 | Vinayak full text, Eq. 5 first-hand; Borgs–Chayes intro + Thm 3.5 (agent; proofs not read) | → `gloss_anomalous_dimension_cca_isotropy_iota` predicts for; → STAT3 couples to |
| **STAT6** Global transfer entropy at first-order transitions | Brown, Bossomaier & Barnett 2022 *Sci. Rep.* 12:15145 | **contested, Tier 2 †** (single study) | published full text (agent); arXiv v3 first-hand | → STAT3 analogous to; → X0_FIM_Regimes analogous to; → INFO4 derives from |
| **IT11** Quantum Fisher information / QCR bound | Braunstein & Caves 1994 *PRL* 72:3439 | established, Tier 1 | full text (scan) first-hand — abstract, Eqs. 11–15, 28, 32–33, Bures relation, Helstrom/Holevo credit | → IT05 generalizes; → QM2 couples to; → IT08 couples to |

**Totals:** 12 entries (7 sections each, 4 facet properties each), **38 links** (existing link types only), **22 anchors** (12 `canonical_authority`, 10 `cites`; all 22 DOIs verified on Crossref), **26 domain tags** (GSW taxonomy, 12 primary). No calibration rows were added for the new entries; a reference entry's status lives on the entry, and adding rows would inflate the claim count.

**Required links from the brief, all present:** (1) → C1, P2, H5, X1; (2) → H5; (3)/(4) → H5, C1; (5) → C2, P11; (6) → P5, M6; (7) → P8, T5, G5; (8) → P8, BR04, IT08; (9) → CCA context (STAT3, ι glossary entry); (10) → STAT3 (+ X0); (11) → BIO3; (12) → IT05, QM2.

**IDs:** BIO12–16, IT09–11 (IT07 avoided: it is a spec alias for INFO4), STAT4–6, and **URB1** (new prefix, owner-approved). `type_group` is RL for all.

## 3. Conjecture closures (calibration append-only)

| Conjecture | Label (calibration `confidence` / `short_status`) | Pattern tags |
|---|---|---|
| **P2** | Retired — "Folded: answered by BIO12 (WBE 1997, Science 276:122) — a = D/(D+1) is WBE's" | restatement-in-new-vocabulary; untestable-without-owner-data |
| **P8** | **Falsified** — "Falsified by Gefen–Mandelbrot–Aharony 1980: critical behaviour depends on topology as well as dimension; phenomenon folded into STAT4" | restatement-in-new-vocabulary; contradicted-by-restated-prior-art |
| **P11** | **Falsified** — "Falsified by Bettencourt 2013: δ = H/[D(D+H)], not D/(D+1), which cannot exceed 1; phenomenon folded into URB1" | restatement-in-new-vocabulary; contradicted-by-restated-prior-art; over-extension-beyond-formula-range |

For each conjecture, `three_state` and `conjecture_summary.status` are prefixed with the label, and the previous value follows " | was: " verbatim. A dated banner (`> **CLOSED 2026-10-18 …**`) is prepended to the claim; the 2026-10-18 consistency-pass banner and the original claim follow unchanged. P8's row and banner also record a correction: **Janke–Johnston–Kenna 2004 never discusses first-order versus continuous transitions**, so M0's "Rediscovery of JJK-style FIM-distinguishes-order" misattributes.

**P5 stays Supported and H5 stays Speculative**; both are now linked to IT09 and BIO12–15 respectively. `contradicted-by-restated-prior-art` is a new pattern tag, added to the memory catalog.

**Claim counts (`claim_status_latest`):** before, 47 = 29 Speculative · 8 Supported · 7 Established · 3 Falsified. After, 47 = **26 Speculative · 8 Supported · 7 Established · 5 Falsified · 1 Retired**. No new `entity_type` was introduced, so the views are unchanged.

## 4. Other correction applied

- **Anchor 100 (P5 → Transtrum et al. 2015) has a wrong DOI.** `10.1063/1.4918623` resolves on Crossref to Beechem, Yates & Graham, *Rev. Sci. Instrum.* 86:041101, a Raman thermal-conductivity paper. The correct DOI is `10.1063/1.4923066`. A dated correction note was appended to the row; the row itself is unchanged, following the 818/819 convention. The correct DOI is anchored on IT09. The wrong DOI also appears in `scripts/migrations/insert_foldin_batch2_2026_04_18.py`, which was left as a historical record.

## 5. Findings for the owner — logged, **not** edited this session

1. **T5's planned test is ill-posed.** It, like P8's *would_confirm*, asks for Ising exponents on the Sierpiński gasket. The gasket is finitely ramified, so T_c = 0 and ν = ∞ (Gefen 1980 Eq. 1): there is no finite-temperature transition to measure. The STAT4 → T5 `constrains` link says so; T5's text is unchanged.
2. **CLAUDE.md mis-states three sources:**
   - **Vinayak 2014** gives a *rank* (Zipf) law, λ_j ≈ c_d/j^ζ with ζ = (d − θ)/d, stated in the correlation-decay exponent θ. It is not a density law in η_critical. θ = η only in d = 2.
   - **Borgs–Chayes 1996** is about the q × q *colour* covariance matrix of a site pair, not the N × N site–site matrix, and says nothing about site–site spectra.
   - **Brown et al. 2022** computed GTE for **q = 5, 7, 10** only. q = 2 enters through their earlier Ising work and the interface-length figure. "Hybrid 2-point + multi-point" is the wiki's description of GTE, not the authors' (GTE is a lag-1 dynamical conditional mutual information).
3. **Two attribution errors in P5's banner.** The banner attributes "Ising at its microscopic parameterisation is not sloppy" to Quinn 2023; it is Machta 2013's statement ("neither the diffusion model nor the Ising model are sloppy at their microscopic scales"). The banner also cites Vinayak et al. 2014 for the Phase-E point; that is fine, given the rank-law caveat above.
4. **Transtrum 2015's parameterisation caveat** ("the FIM can be transformed into any positive definite matrix by a simple linear transformation of parameters") bears directly on any D_eff participation ratio built from FIM eigenvalues (M6, P5, CCA). It is recorded in IT09 and in the P5/M6 link descriptions.
5. **X0_FIM_Regimes is labelled established / Tier 1** for a first-order-vs-continuous classifier validated on four lattice systems in-project. Under the owner's definition of Established (independently reproduced), that label looks generous, and STAT6 is the external prior art. Not changed.
6. **H5 ↔ Glazier.** Glazier 2010 Eq. 2, b = 1·p + (2/3)(1 − p), *is* H5's β(λ) with d_f = 2 and λ = 1 − p, published with the same activity-level reading. This strengthens the H5 RESTATEMENT verdict. The H5 → BIO14 link records it; H5's label is unchanged.
7. **BIO15 TODO:** add Kooijman 2010 (the DEB book) as progenitor anchor once read.

## 6. Left unverified

- Kooijman 2010 (book): not read.
- Sousa et al. 2008's proof appendix (the α ∈ [0.66, 1] and [0.5, 1] intervals): not read.
- Maino et al. 2014 version of record: only the published abstract and a 2012 manuscript were read; equations and quotes in BIO15 are marked as manuscript.
- Machta 2013 erratum (*Science* 342:931): not read. The published Fig. 3 caption's shrink factor disagrees in sign with the arXiv SM and Quinn Eq. 16. IT09 uses the SM/Quinn form.
- Transtrum 2015 and Quinn 2023: arXiv versions only.
- Borgs–Chayes proofs; the Gefen carpet numbers (approximate Migdal–Kadanoff); Gefen et al. 1983–84 follow-ups (bibliographic only).
- Dodds–Rothman–Weitz 2001 and Kozłowski & Konarzewski 2004 are named in BIO12 as critiques but were not read this pass. Savage et al. 2008 was read at abstract level only (anchor confidence: medium).
- Helstrom 1976 / Holevo 1982 (credited by Braunstein & Caves for the quantum bound): not read, not anchored.

## 7. Before → after

| | Before | After |
|---|---|---|
| Entries | 319 | **331** |
| Links | 849 | **887** |
| External anchors | 910 over 276 entities | **932 over 288** (+ note on id 100) |
| Domain-tag rows (current) | 545 | **571** |
| Calibration rows / audit refs | 89 / 13 | **92 / 14** |
| Claims (`claim_status_latest`) | 29 Spec · 8 Sup · 7 Est · 3 Fals | **26 Spec · 8 Sup · 7 Est · 5 Fals · 1 Retired** |
| Non-glossary orphans | 0 | 0 |
| Tests | 575 pass / 12 fail | **574 pass / 13 fail** — the original 12 plus `test_integration.py::TestCoverageAnalyzerLive::test_reference_law_count`, which hard-codes 213 reference_law entries (now 225). Another stale count, not fixed (per brief). |
| ChromaDB chunks | 2,056 | **2,128** (snapshot `snap_20261018_201041`, plain sync; milestone `snap_20261018_190812` still protected) |

## 8. Handover note

- **Done:** 12 reference entries with anchors, tags and links; P2 Folded, and P8/P11 Falsified by the work they restated; the anchor-100 DOI correction; the index rebuilt with `python3 -m src.sync` (plain). Commits are local only and **not pushed**.
- **Not done (owner to schedule):** the §5 findings, i.e. the CLAUDE.md wording, T5's protocol, the P5 banner attribution and the X0 label; the Kooijman book anchor; the glossary `[[g:…]]` markup for the new entries.
- **CLAUDE.md counts are now stale** (319 entries, 849 links, 910 anchors, 29/8/7/3 claims). They were not edited, per the parent session's instruction; they need a refresh in the next CLAUDE.md pass.
- **Re-running:** both migrations are safe to re-run (applied markers checked first). The closure script refuses to write if P2/P8/P11 text has changed since 2026-10-18, because it fingerprints the fields it edits.
- **Errors I made this pass:**
  - A `cd` in a compound command moved the working directory into `scripts/migrations/`; caught before any relative-path write.
  - A text-extraction loop wrote five scratch files under `/tmp`; they were deleted.
  - I first transcribed JJK's Eq. 7 determinant from agent notes, then simplified it to a description because I had not checked it on the page.
  - The first closure draft used "Folded" for P8/P11; the owner corrected this to Falsified.

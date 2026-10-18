# Early-Warning-Signal Fold-In — 2026-10-18

**audit_ref:** `gsw-ews-fold-in-2026-10-18` · **Mode A** (curation / grounding) · no promotions, no new conjectures or Q-entries, no calibration rows
**Migration:** `scripts/migrations/ews_fold_in_2026_10_18.py` (+ `ews_fold_in_data_2026_10_18.py`, the content). Dry run by default, idempotent, read-back verified. Applied, re-applied (no-op) and orphan-checked on scratch copies of both databases first.
**Purpose:** ground Questions Raised Log item **QR-006** ("can information-theoretic measures warn of tipping points earlier or more reliably than classical indicators?"). Before this pass the wiki had no entries on critical slowing down, tipping types or early-warning signals (EWS).
**Owner decisions (2026-10-18, answered by the owner, relayed by the parent session): all as recommended.**
- New prefix EWS1–EWS10.
- Ten entries with the statuses in §2, keeping the in-text single-study caveats (EWS2, EWS3, EWS7).
- No Prokopenko 2011 entry (logged as a lead); Kéfi 2013 sits in EWS4.
- Fath 2003 is the canonical progenitor (confidence medium, noted "not read"), with Karunanithi 2008 and Spanbauer 2014 as `cites`.
- Kritzman 2011 is a `cites` anchor (confidence low, unread).
- Burnett 2019 is named in EWS6 with no anchor.
- At the parent session's request, the linear-Gaussian equivalence is recorded in EWS8 (§3.2).

---

## 1. Reading record

"Full text" means I read the passages used, from the PDF text, an HTML page or the PMC XML. An equation is only transcribed where I saw it, including equation images (Karunanithi Eqs. 4–5) and TeX sources (Weinans, Chen 2019, Bury). Nothing here rests on the agent-compiled literature map alone; where the map and the source disagree, §5 says so.

| Source | Access | Used in |
|---|---|---|
| Scheffer et al. 2009, *Nature* 461:53 | **Full text** via its reprint as Ch. 2 of V. Dakos's 2011 Wageningen PhD thesis (edepot.wur.nl/168815). The Nature typeset version was not accessible. | EWS1 |
| Dakos et al. 2012, *PLoS ONE* 7:e41010 | **Full text** (PLoS PDF) | EWS1 |
| Ditlevsen & Johnsen 2010, *GRL* 37 | **Full text of the authors' draft dated 25 May 2010** (gfy.ku.dk/~pditlev), not the version of record | EWS1, EWS3 |
| Carpenter et al. 2011, *Science* 332:1079 | **Authors' preprint** (Cary Institute) + abstract | EWS2 |
| Dai et al. 2012, *Science* 336:1175 | Abstract only | EWS2 |
| Ashwin et al. 2012, *Phil. Trans. A* 370:1166 | Abstract + arXiv:1103.0169v5 front matter (formal definitions not transcribed) | EWS3 |
| Hastings & Wysham 2010, *Ecol. Lett.* 13:464 | Abstract only | EWS3 |
| Boettiger & Hastings 2012, *J. R. Soc. Interface* 9:2527 | Abstract + arXiv:1204.6231 (ROC/likelihood method confirmed; results not transcribed) | EWS4 |
| Boettiger & Hastings 2012, *Proc. R. Soc. B* 279:4734 | Abstract + arXiv:1210.1204 set-up | EWS4 |
| Jäger & Füllsack 2019, *PLoS ONE* 14:e0211072 | **Full text** (PMC) | EWS4 |
| Kéfi et al. 2013, *Oikos* 122:641 | **Full text** (typeset copy hosted at sciences.ucf.edu) | EWS4 |
| Barnett et al. 2013, *PRL* 111:177203 | **Full text, authors' version dated 13 Sep 2013** (users.sussex.ac.uk/~lionelb). SM downloaded, derivations not checked. | EWS5 |
| Fath, Cabezas & Pawlowski 2003, *J. Theor. Biol.* 222:517 | **Not read** (paywalled; no open copy; no abstract retrieved). Crossref record verified. | EWS6 (via Karunanithi) |
| Karunanithi et al. 2008, *Ecol. Soc.* 13(1):22 | **Full text** incl. equation images 1, 4, 5 | EWS6 |
| Spanbauer et al. 2014, *PLoS ONE* 9:e108936 | **Full text** (PMC); Eq. 2 (discrete form) is an image, not transcribed | EWS6 |
| Burnett 2019, UNL PhD dissertation | Abstract only (digitalcommons.unl.edu/natresdiss/299); no DOI, not anchored | EWS6 |
| Brock & Carpenter 2006, *Ecol. Soc.* 11(2):9 | **Full text** (Appendix 1 not read) | EWS7 |
| Chen, O'Dea, Drake & Epureanu 2019, *Sci. Rep.* 9:2572 | **Full text** (PMC); SI proof not read | EWS7 |
| Chen, Liu, Liu, Li & Aihara 2012, *Sci. Rep.* 2:342 | **Full text** (PMC); composite-index formula is an image, not transcribed | EWS7 |
| Held & Kleinen 2004, *GRL* 31 | **Paper not read**; abstract text via the EarthRef index | EWS7 |
| Kritzman, Li, Page & Rigobon 2011, *J. Portfolio Mgmt* 37(4):112 | **Not read**; secondary sources only | EWS7 |
| Weinans et al. 2021, *Sci. Rep.* 11:9148 | **Full text** (PMC); figures not inspected | EWS8 |
| Bury et al. 2021, *PNAS* 118:e2106140118 | **Full text** (PMC); AUC values are in Fig. 2 and were not read; SI not read | EWS9 |
| Tirabassi & Masoller 2023, *PNAS* 120:e2215667120 | **Full text** (PMC); SI power analysis not read | EWS10 |
| Barnett, Barrett & Seth 2009, *PRL* 103:238701 | **Full text, arXiv:0910.4514v2** (Eqs. 8, 10–13); version of record not read | EWS8 |
| Prokopenko et al. 2011, *PRE* 84:041116 | Abstract only; no entry (see §6) | — |
| Bandt & Shiha 2007, *J. Time Ser. Anal.* 28:646 | Crossref record only (no abstract or open text found); not used — left to the parent session | — |

All 24 distinct DOIs used as anchors (25 anchor rows; Ditlevsen & Johnsen is anchored on EWS1 and EWS3) resolve on Crossref with matching title and authors (checked 2026-10-18). Two Crossref "issued" years are the online date, not the print volume: Kéfi (2012 vs vol. 2013) and Tirabassi (2022 vs vol. 2023). Both are noted in the anchor rows.

## 2. The ten entries

| ID | Title (short) | Status | Canonical anchor | Links added |
|---|---|---|---|---|
| **EWS1** | Critical slowing down and classical EWS | established, Tier 1 | Scheffer 2009 (comprehensive_survey) + cites Dakos 2012, Ditlevsen & Johnsen 2010 | → NE05 derives from |
| **EWS2** | Experimental tests (lake, yeast) | established, Tier 2 | Carpenter 2011 (progenitor) + cites Dai 2012 | → EWS1 tests |
| **EWS3** | Tipping types; transitions without warning | established, Tier 2 | Ashwin 2012 (progenitor) + cites Hastings & Wysham 2010, Ditlevsen & Johnsen 2010 | → EWS1 constrains; → M3 constrains |
| **EWS4** | False alarms and limits of detection | established, Tier 2 | Boettiger & Hastings 2012 JRSI (progenitor) + cites B&H 2012 PRSB, Jäger & Füllsack 2019, Kéfi 2013 | → EWS1 constrains; → MATH1 derives from |
| **EWS5** | Information flow peaks on the disordered side | contested, Tier 2 † (single study) | Barnett 2013 (progenitor) | STAT6 → derives from; → INFO4 derives from; → EWS1 predicts for |
| **EWS6** | Ecological Fisher Information index | contested, Tier 2 † | Fath 2003 (progenitor, **confidence medium, not read**) + cites Karunanithi 2008, Spanbauer 2014 | → IT05 derives from; → EWS1 couples to; → X0_FIM_Regimes disambiguates from; → BIO16 disambiguates from |
| **EWS7** | Covariance-eigenvalue / dominant-mode indicators | established, Tier 2 | Brock & Carpenter 2006 (progenitor) + cites Chen 2019, Chen 2012, Held & Kleinen 2004 (medium), Kritzman 2011 (**low, not read**) | → EWS1 generalizes; → STAT5, STAT3, X0_FIM_Regimes analogous to |
| **EWS8** | Multivariate indicator benchmark (+ linear-Gaussian equivalence note) | contested, Tier 2 † (single study) | Weinans 2021 (progenitor) + cites Barnett, Barrett & Seth 2009 (medium) | → EWS7, EWS1, INFO4 tests |
| **EWS9** | Deep-learning EWS, ROC benchmark | contested, Tier 2 † (single study) | Bury 2021 (progenitor) | → EWS1, EWS4 tests |
| **EWS10** | Spatial permutation entropy | contested, Tier 2 † (single study) | Tirabassi & Masoller 2023 (progenitor) | → INFO1 derives from; → EWS1 tests |

**Totals:** 10 entries (7 sections each, 4 facet properties each), **24 links** (existing link types only; tiers hand-assigned from {1, 1.5, 2} as in the previous fold-in), **25 anchors** (10 `canonical_authority`, 15 `cites`), **27 domain tags** (GSW taxonomy, 10 primary). No calibration rows: a reference entry's status lives on the entry, and rows would inflate the claim count.

**Statuses** follow `wiki_meta.status_definitions` (Established = peer-reviewed and independently reproduced; otherwise contested). EWS1, EWS3, EWS4 and EWS7 are theory or methodology confirmed by several independent groups. EWS2 counts as reproduced because two independent experimental systems confirm the same prediction. The five single-study entries (EWS5, EWS6, EWS8–10) are contested.

**Prefix:** `EWS` is new; no existing prefix fits a topic that spans dynamical systems, ecology and climate (URB1 precedent). `type_group` is RL.

**Merging and splitting relative to the brief's eleven proposed entries:**
- Kéfi 2013 sits in EWS4 (limits), not EWS3, because its point is non-specificity.
- Prokopenko 2011 has no entry, because only the abstract was obtainable (§6).
- The other nine follow the brief.

**Links considered and not added:**
- **D2 (Feigenbaum).** None of the sources read discusses period-doubling. Slowing down at a flip bifurcation (multiplier → −1) is standard dynamical-systems theory, but it is not in any source read this pass.
- **STAT4 (Gefen).** No source connects fractal-lattice critical behaviour to EWS.
- **X5 (ecological regime-first stub).** A `tests` link would overstate the connection.
- **X0's label was not touched**; only links were added.

## 3. Findings that bear on QR-006

Tags: **Established** = a standard result, cited. **Supported** = follows from cited results by short argument. **Speculative** = my reading, not checked.

1. **Barnett et al. 2013's information-flow peak comes before the transition in temperature only, not in time** (Established, read in the paper). The global transfer entropy maximum is at T = 2.354 ± 0.003 against T_c ≈ 2.269. It was found in an equilibrium temperature sweep (L = 512; the position does not move for L = 64–512). Using it as a warning is a proposal: watch for T_gl, estimated over short time windows, to peak while the multi-information still rises. The authors say testing "both in complex dynamical models and on real-world data" is still needed. No driven series, no lead time, no comparison with autocorrelation or variance. QR-006 sub-question 3 is therefore genuinely open as far as this paper goes.
2. **In the linear-Gaussian regime, the information measures are functions of the classical ones** (Supported: each step is established, and the synthesis is mine).
   - Lag-1 mutual information of a Gaussian series is MI = −½ log(1 − ρ²), a monotone function of lag-1 autocorrelation. Weinans et al. state this, and it is why they found MI adds estimation cost but no signal.
   - In the Ornstein–Uhlenbeck limit, ⟨x²⟩/T = σ²/2 (Ditlevsen & Johnsen), so variance and correlation time move together.
   - The location Fisher information of a Gaussian fluctuation density is 1/σ² (Karunanithi Eq. 4 with a Gaussian p).
   - **Consequence for the gate:** an information-theoretic indicator can only beat autocorrelation and variance by using non-Gaussian or nonlinear structure (flickering, bimodality, asymmetry), or through estimation behaviour. Any benchmark test (sub-question 1) should be designed around that.
   - For jointly Gaussian processes, Granger causality is exactly twice the transfer entropy, F = 2T (Barnett, Barrett & Seth 2009, *PRL* 103:238701, Eq. 13; read in arXiv v2). So the reduction covers transfer entropy too.
   - Recorded in EWS8 ("Linear-Gaussian equivalence") at the parent session's request. The ordinal-pattern (permutation-entropy) case, Bandt & Shiha 2007, was not verified and is not recorded.
3. **The Fisher Information index as a pooled-variance proxy** (Supported for the continuous form; Speculative for the estimator). Karunanithi et al.'s Eq. 4 is the shift-invariant (location) Fisher information of the fluctuation density p(s), and is exactly 1/σ² for a Gaussian. Two further points:
   - The derivation itself assumes fluctuations are independent of the mean, and the authors note this becomes an approximation near a transition, the very place the index is used.
   - The estimator bins points into states whose size is fixed from the least variable window (Spanbauer). With fixed bins, wider dispersion spreads points over more states and lowers I. That is my reading of the algorithm and has not been checked numerically. The agent map's triviality claim is right for the continuous form; for the binned multivariate estimator it is untested (sub-question 2).
4. **Weinans et al. 2021 scores trend strength (Kendall τ), not error rates.** Their "no single best method" is therefore about trend robustness under data degradation. The ROC-style head-to-head with null series, which QR-006 needs, is Bury et al. 2021's design. Boettiger & Hastings 2012 asked for it, and only deep learning has been scored that way among the sources read.
5. **Bury et al.'s test set is reproducible but not packaged.**
   - The "268 empirical and model time series" figure is from the abstract.
   - The data sit across GitHub (code and thermoacoustic data), PANGAEA (geochemical) and NOAA (paleoclimate).
   - A common-benchmark study would have to reassemble it and regenerate the null series. That is feasible, but it is work, not a download.
6. **Critical slowing down does not discriminate transition type** (Established; Kéfi et al. 2013). It precedes transcritical, Hopf and non-bifurcation sharp responses as well as folds. For the wiki's CCA/X0 interest in first-order versus continuous: none of the EWS sources read claims an indicator that classifies transition order. Kéfi et al. say indicators specific to catastrophic shifts "are still lacking".

## 4. Findings that bear on X0 and CCA (no labels changed)

- **X0 vs the Fisher Information index: different objects.** Recorded as a `disambiguates from` link (EWS6 → X0). The shared vocabulary ("Fisher information", "regime") is the only overlap: a scalar location FI of a time-windowed occupancy density, against a singular-value spectrum of a spatial correlation-kernel matrix.
- **X0's "one dominant direction" and its finance case are the covariance-concentration idea** (EWS7). The finance case is close to the absorption ratio, though Kritzman 2011 was not read. Recorded as `analogous to`; X0's established / Tier 1 label is unchanged, as in the previous fold-in's finding 5.
- **CCA (STAT3).** Two of the indicators are concentration measures of a covariance spectrum. Chen et al. 2019's second indicator is σ₁/√(Σσᵢ²), and the absorption ratio is a top-k explained-variance share. CCA's d_eff is the participation ratio (Σσ)²/Σσ², another concentration measure of the same spectrum. Using d_eff collapse as a *warning* restates EWS7. Using it to *classify transition order* from an equilibrium temperature sweep is not addressed by any source read; this stays provisional, per the prior-art gate's meta-observation. The S(k = 0) reduction suggested in the agent map is unchanged by this pass and still unrun (CCA-1c reduction test).

## 5. Corrections to the agent-compiled literature map (`QR-006_EWS_LITERATURE_MAP_2026_10_18.md`)

The map file was not edited. It is the agent's record and carries its own provenance banner. These corrections are recorded here:

1. **Tirabassi & Masoller.** The map says PE "rose before tipping in 6 of 6 and correlation in 4 of 6". The main text says the spatial PE reaches a **minimum** at or near the start of the bistability region in **five of the six** transects (no minimum in transect 2), and that PE *decreases* before the transition to desert in both models. The 6/6 vs 4/6 figures were not found in the main text; they may be in the SI, which was not read.
2. **Bury et al. "public set of 268 transition and null series".** The 268 are empirical and model series; null series were generated for the ROC comparison. The data are spread across several repositories (§3.5).
3. **Weinans et al. "MI failed in 20D".** The text says MI is the indicator most affected by reduced data accuracy, and that it needs increasingly more data in high dimension. "Failed" is stronger than the text.
4. **Dai et al. 2012 "Allee effect".** The abstract does not use the term. EWS2 is limited to the abstract.
5. **Fath et al. 2003.** Still not read. Its method is now known first-hand through Karunanithi 2008, which also says the original computation used first and second time derivatives of the series.

## 6. Left unverified

- **Not read at all:**
  - Fath, Cabezas & Pawlowski 2003 (anchored with confidence medium, noted "not read").
  - Kritzman et al. 2011 (anchored `cites`, confidence low; the number of eigenvectors in the absorption ratio is not verified).
  - Held & Kleinen 2004 (abstract via index only).
  - Mayer et al. 2006; Eason, Garmestani & Cabezas 2014; Dablander & Bury 2022 (named from the PMC header only); Deng et al. 2014 (PRE 90:063308, Rényi follow-up to Barnett); Bandt & Shiha 2007.
- **Abstract only:** Dai 2012; Hastings & Wysham 2010; Burnett 2019; Prokopenko 2011.
- **Prokopenko et al. 2011** (abstract: FIM elements relate to the rate of change of order parameters; second-order transitions show as divergences of individual elements; FI of the magnetization bias peaks at criticality in random Boolean networks). This is closer prior art for "FIM detects criticality" (X0, IT10) than for EWS. **Recommended:** add it as a `cites` anchor on IT10 once read. No entry was created.
- **Not transcribed although seen:** Spanbauer Eq. 2 and Karunanithi's discrete estimator; Chen 2012's composite-index formula; Bury's AUC values (Fig. 2); Boettiger & Hastings simulation counts.
- **Versions:**
  - Scheffer 2009 was read in a thesis reprint.
  - Ditlevsen & Johnsen and Carpenter were read in authors' drafts or preprints.
  - Barnett was read in the authors' version.
  - Wording in the published versions may differ slightly; the quotes used are from abstracts (Carpenter, Boettiger, Kéfi, Weinans, Tirabassi), from the authors' text (Barnett, Dakos), or are paraphrase.

## 7. Before → after

| | Before | After |
|---|---|---|
| Entries | 331 | **341** (reference_law 225 → 235) |
| Links | 887 | **911** |
| External anchors | 932 over 288 entities | **957 over 298** |
| Domain-tag rows (current) | 571 | **598** |
| Calibration rows / audit refs | 92 / 14 | 92 / 14 (unchanged) |
| Claims (`claim_status_latest`) | 26 Spec · 8 Sup · 7 Est · 5 Fals · 1 Retired | unchanged |
| Non-glossary orphans | 0 | 0 |
| Tests | 574 pass / 13 fail | **574 pass / 13 fail** — identical failing set (stale hard-coded counts, incl. the reference_law count, now 235) |
| ChromaDB chunks | 2,128 | **2,188** (+60 new, 0 changed; snapshot `snap_20261018_205821`, plain sync; milestone `snap_20261018_190812` still protected) |

## 8. Handover

- **Done:** `30841fa` (migrations + databases + index) and the commit that adds this report and the QR-006 log lines. Both are local only and **not pushed**.
- **QR-006 log:** the "Wiki holdings" line and the "Coverage gaps" bullet now name EWS1–EWS10, with a changelog line. Nothing else in the log was edited.
- **For the triviality / "worth asking" gate on QR-006 sub-question 1:** §3.2 is the main input. In the linear-Gaussian regime the information measures reduce to autocorrelation and variance, so a benchmark is only worth running if it targets non-Gaussian structure or estimation behaviour, and if it scores error rates (ROC against null series, as Bury et al. do) rather than trend strength.
- **Not done (owner to schedule):**
  - Read Fath 2003 and Kritzman 2011 if access appears.
  - Read Prokopenko 2011 and anchor it on IT10.
  - Check M3's Type VI "R-tipping" usage against Ashwin et al. (EWS3 → M3 link).
  - Glossary `[[g:…]]` markup for the new entries.
- **Errors I made this pass:**
  - A `cd` in a compound command moved the shell into `scripts/migrations/`; caught at once, nothing was written there.
  - My first draft gave Bury's fold normal form as ẋ = μ + x²; the paper has ẋ = μ − x². Fixed before applying.
  - My first draft of EWS2 added "cooperative growth" and "diluted" to Dai et al., which the abstract does not say. Removed.
  - My first draft used link tiers 2.5 and 3, outside the wiki's {1, 1.5, 2}; normalised to 2.
  - My first draft had an EWS2 → X5 `tests` link that overstated the connection. Removed.
  - `data/chroma_db/chroma.sqlite3` showed as modified before the sync, most likely from the baseline test run; the sync then rewrote it.

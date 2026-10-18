# QR-006b — second, independent prior-art search

**Date:** 2026-10-18 · **Mode A** (read-only literature work) · **Question:** QR-006b (Questions Raised Log)
**Purpose:** the PROCEED in [`QR-006_BENCHMARK_GATES_2026_10_18.md`](QR-006_BENCHMARK_GATES_2026_10_18.md) is provisional until a second search, run in a different session with different vocabulary, fails to find the study (`QUESTION_GATES.md`, "Recording"). This is that search. It deliberately leaned towards finding the reason the question is not new.
**Not touched:** `ds_wiki.db`, `wiki_history.db`, the Chroma index, `docs/demo/`, the podcast folder. No entries, anchors or calibration rows.

**Reading markers.** *Full text* means the passages used were read from the paper's own text: PMC/Europe PMC XML, an arXiv PDF or a publisher PDF. *Full text, keyword scan* means the whole text was searched for the information-measure terms and the baseline passages were read, but the paper was not read end to end. *Abstract* means the abstract only, from Europe PMC, OpenAlex or the publisher. *Search summary* means only a search engine's summary of the paper was seen. That is a lead, not a reading. No marker is upgraded anywhere in this report.

---

## 1. How this search differs from the first

The first search used "mutual information", "transfer entropy", "permutation entropy", "Fisher information", "complexity", "information dissipation", "multivariate resilience indicators", "ROC/AUC" and "null model", inside the ecology and early-warning literature.

This search used other fields' own vocabulary:
- **Seizure prediction:** "linear vs nonlinear measures", "seizure prediction characteristic", "surrogate validation".
- **Time-series feature screens:** "highly comparative time-series analysis", hctsa, catch22, "distance to criticality".
- **Noise theory:** "α-stable" and "Lévy noise", "multiplicative noise", "flickering", "Langevin" and "drift–diffusion–jump".
- **Complexity measures:** "Kolmogorov complexity", "Lempel-Ziv", "approximate entropy", "sample entropy".
- **Non-equilibrium indicators:** "entropy production", "time irreversibility".
- **Domain terms:** Dansgaard–Oeschger, AMOC, thermoacoustics, power grids, financial crises.
- **ML early warning:** the machine-learning EWS papers' own baseline sections, read directly.

## 2. Sources

| Source | Read | Bearing on QR-006b |
|---|---|---|
| **Alvarez-Martinez & Miramontes 2026**, *Entropy* 28:628, doi:10.3390/e28060628 (the review the first search could not open) | **Full text** (Europe PMC XML, PMC13298826; figures not inspected) | **Not prior art.** A narrative review. Its Table 1 lists permutation/Shannon entropy and Fisher information among 15 indicators, with expected direction and caveats ("interpretation is system-specific"). There is no head-to-head scoring of any information measure against AR(1) or variance. Its recommendations (null-model benchmarking, preregistered protocols, prospective false-alarm rates; §3.2.3 and §5.6) **independently restate the gap** Dakos et al. 2024 named. Oddity: its entropy-indicator citation [27] is Quax et al. 2017 on synergistic information, not an early-warning study. |
| **Harris, Gollo & Fulcher 2024**, *Phys. Rev. X* 14:031021 (arXiv:2310.14791v3) | **Full text** (arXiv PDF). **Supplemental Table S1 read in full** as a data file (arXiv ancillary file; §7); Tables S2–S3 and supp.pdf not read | **Closest new adjacent work.** A "highly comparative" screen of about 7,500 hctsa features, which include entropy and automutual-information features, for tracking distance to criticality near a supercritical Hopf bifurcation. **Fixed noise:** SD and AC1 are among the best. **Variable noise amplitude:** SD and AC1 collapse (Spearman ρ 0.98 → 0.23 and 0.97 → 0.48). The winners measure *the shape of the value distribution relative to the spread of differences*, and the authors build a new statistic from that (RAD). The top features named are distributional, extreme-value and motif features, not entropies. Scoring is Spearman ρ against the control parameter, not ROC with null series. One model, additive Gaussian noise. The authors state they did **not** study non-Gaussian or multiplicative noise (Discussion). |
| **Layritz, Rammig, Pavlyukevich & Kuehn 2025**, *Sci. Rep.* 15:13758, doi:10.1038/s41598-025-88659-0 | **Full text, keyword scan** (Europe PMC XML) | **Adjacent; confirms the premise.** Under α-stable (non-Gaussian) noise, rising variance and autocorrelation lack theoretical support and risk false positives. The replacement they propose is the α-stable scale factor γ_X, a **distributional** parameter, not an information measure. No ROC, no information measures. |
| **Mormann et al. 2005**, *Clin. Neurophysiol.* 116:569 | **Abstract** (Europe PMC) + **search summary** of a secondary write-up (Sapien Labs) | **Prior art in another field's vocabulary, for one empirical regime.** An ROC comparison of 30 univariate and bivariate, linear and nonlinear EEG measures (preictal vs interictal) on multi-day recordings, with surrogate-based significance testing. Abstract: linear measures performed "similar or better than non-linear measures". Many earlier claims were not significant. **Not verified:** whether the measure set includes variance and decorrelation time, and which "nonlinear" measures are information-theoretic. |
| **McSharry, Smith & Tarassenko 2003**, *IEEE Trans. Biomed. Eng.* 50:628; and *Nat. Med.* 9:241 (2003) | IEEE: **abstract** (LSE copy; its header says 2002). *Nat. Med.*: bibliographic record only | **Same direction.** With surrogate tests, the pre-seizure drop in correlation density (a nonlinear measure) "may simply reflect increases in the variance". The seizure field's stated rule: a nonlinear statistic must beat variance to be worth using. |
| **Mormann, Andrzejak, Elger & Lehnertz 2007**, *Brain* 130:314 | **Abstract** | A field review. The optimistic 1990s seizure-precursor results did not reproduce under controlled evaluation. It proposes methodological guidelines that match QR-006b's design conditions. |
| **Dakos & Soler-Toscano 2017**, *Ecol. Complex.* 32:144, doi:10.1016/j.ecocom.2016.08.005 | **Search summary only.** Closed access; the HAL record (hal-01990931) sits behind a bot check and holds no file; Crossref and OpenAlex carry no abstract | The search summary says block-decomposition Kolmogorov complexity "decreased before all ecological transitions" in simulated series and spatial data, across transition types. **Not verified** whether it scores against AR(1)/variance, or how. **Still an open check** (§5). |
| **Eason, Garmestani & Cabezas 2014**, *Clean Technol. Environ. Policy* 16:773 | **Abstract + first page** (EPA excerpt PDF). The full copy at UNL Digital Commons was not reached: Cloudflare check for scripts, file download in the browser pane | Abstract: Fisher information "is compared to traditional indicators" (variance, skewness, kurtosis, critical slowing down) on model and real systems, and is called a leading indicator. Scoring method and nulls are not visible in what was read. **Still an open check** (§5). |
| **Dmitriev et al. 2023**, *Front. Phys.* 11:1274685 | **Abstract** (OpenAlex) | **Adjacent, positive direction, one model family.** In sandpile automata (self-organised criticality, outside CSD theory), approximate entropy, embedding dimension and correlation dimension were the "effective" precursors: fewest false signals and longest lead. AC1 and spectral slope could not be used. The score is a bespoke efficiency measure, not ROC against matched nulls. |
| Bury et al. 2023, *Nat. Commun.* 14:6331 (discrete-time bifurcations) | **Full text, keyword scan** (PMC10564974) | ROC: the deep-learning classifier vs variance and AC1. "Entropy" appears only as the loss function. **No information-measure baseline.** |
| Deb et al. 2022, *R. Soc. Open Sci.* 9:211475 (EWSNet) | **Full text, keyword scan** (PMC8847887) | Compared with other ML models and classical indicators. **No information-measure baseline.** |
| Dylewsky et al. 2023, *J. R. Soc. Interface* 20:20220562 | **Full text, keyword scan** (PMC10072946) | Five traditional indicators (variance, skewness, kurtosis and autocorrelations, in space and time) vs a CNN-LSTM; ROC on test systems. **No information-measure baseline.** |
| Dablander & Bury 2022, *PNAS* 119:e2207720119 | **Full text, keyword scan** (PMC9477405) | Preprocessing matters. No information measures. |
| Grziwotz et al. 2023, *Sci. Adv.* 9:eabq4558 | **Full text, keyword scan** (PMC9821862) | DEV indicator vs AR1 and SD. No information measures. |
| Huang, Bathiany, Ashwin & Boers 2024, *Nat. Mach. Intell.* 6:1556 | **Search summary** (via the *Entropy* review's text, which is *full text*) | R-tipping: critical slowing down cannot separate tipping from non-tipping runs, and deep learning can. Baselines not checked. |
| Xu, Patterson, Levin, Wang et al. 2023, *PNAS* 120:e2218663120 | **Abstract + keyword scan** (PMC9945981) | Entropy production, flux and time irreversibility warn "much earlier" than conventional predictors in one shallow-lake model. These are thermodynamic, not information-theoretic, indicators. No ROC, no nulls. **Adjacent.** |
| Garland et al. 2018, *Entropy* 20:931 | **Full text, keyword scan** (PMC7512518) | Permutation entropy used as a forensic tool for ice-core data artefacts. Not early-warning work. |
| Garland et al. 2018, "Climate entropy production recorded in a deep Antarctic ice core" (arXiv:1806.10936) | **Search summary** | Weighted permutation entropy shows only small Dansgaard–Oeschger signatures. No head-to-head. |
| Boers 2018, *Nat. Commun.* 9:2556 | **Abstract** | Variance and AC1 warnings for D–O events in 5-year NGRIP data, in the 10–50-year band. Classical indicators only. |
| Hummel, Boers & Rypdal 2025, *Earth Syst. Dynam.* ("Inconclusive early warning signals for D–O events …") | **Search summary** (title) | The D–O warning evidence is contested. No information measures seen. |
| Morr et al. 2023, arXiv:2308.16773; Boettner & Boers 2022, *Phys. Rev. Research* | **Search summary** | Time-dependent, multiplicative or correlated noise breaks variance and AC1. The fixes offered are model-based (Langevin), not information-theoretic. |
| Pang, Li & Jin 2025, *Nonlinear Dyn.* (spatial occupancy entropy) | **Search summary** (no abstract retrievable) | Reportedly beats CSD indicators, with ROC in an appendix. Spatial, one model family. **Lead, unverified.** |
| Morales et al. 2015, *PLoS ONE* (2D Ising EWS); Marinazzo et al. 2019 arXiv:1901.05405 (synergy) | **Search summary** | Equilibrium temperature sweeps. Same limitation as Barnett 2013 (EWS5): a peak before T_c in temperature is not a lead in time. |
| Gatfaoui, Nagot & de Peretti 2016 (CSD in financial crises); finance PE and transfer-entropy case studies | **Search summary** | Classical indicators mixed (variance and skewness partly; AC1 not). Information-measure papers are single-case, without matched false-alarm comparisons. |
| Thermoacoustics (Gotoda PE; Sujith Hurst and recurrence) and power grids (Hines, Cotilla-Sanchez et al.) | **Search summary** | Many single-indicator papers. None found ranking information measures against AC1 and variance on the same data at matched false-alarm rates. |

## 3. Gate 1, revised

**Generic benchmark: still OPEN IN THE LITERATURE, now framed by two sources.** Dakos et al. 2024 (§4.3.1) name the gap, and the *Entropy* 2026 review independently calls for null-model benchmarking and prospective false-alarm rates. No information-theoretic baseline appears in any ML-EWS paper whose full text was keyword-scanned (Bury 2023, Deb 2022, Dylewsky 2023, Dablander & Bury 2022, Grziwotz 2023).

**Regime-stratified version: NO STUDY FOUND that does the QR-006b design.** That design is a common labelled benchmark with matched nulls, scored by ROC or by lead time at fixed specificity, putting information measures against AC1 and variance, stratified by mechanism. Two things change the picture, however.

1. **Partial answers exist under other vocabulary.**
   - *Seizure prediction (2002–2007)* ran exactly this kind of ROC horse race, "linear vs nonlinear", in an empirical regime where critical slowing down is doubtful. It found no gain from univariate nonlinear measures over linear ones (Mormann 2005 and McSharry 2003, both *abstract*).
   - *Sandpile automata (Dmitriev 2023, abstract)* found the opposite in a self-organised-criticality setting: approximate entropy worked and AC1 did not.
   - *Highly comparative feature screens (Harris 2024, full text)* answered a neighbouring question. Under unknown noise amplitude, distribution-shape features beat SD and AC1. The top-ranked features were not information measures (the full ranking in S1 was not read).
2. **The competitor set in the non-Gaussian regimes is not just AC1 and variance.** Where CSD's assumptions fail, the literature's own answers are distributional and model-based indicators: RAD (Harris 2024), the α-stable scale factor γ_X (Layritz 2025), Langevin and drift–diffusion–jump estimates (Morr 2023; Carpenter & Brock 2011, cited in the *Entropy* review §3.3.1), and higher moments. An information measure that beats AC1 and variance there might only be rediscovering what those indicators already capture.

**Verdict:** generic `open-in-literature` (strengthened); regime-stratified `narrow-angle-provisional`, **not overturned**. The angle is narrower than the first report stated (§4, tests 1 and 2).

## 4. Gate 2, updated

### Test 1 (triviality): an extension of the existing FOLD

The first report folded the linear-Gaussian case. One more sub-case folds by a short derivation. Tag: **Supported.** Each step is a standard result; the synthesis is this report's.

- **The sub-case.** The observed series is a strictly monotone transform of a Gaussian process, x_t = g(z_t). Its marginal distribution is non-Gaussian, but its dependence (copula) is Gaussian. Examples: log-abundances, saturating sensors.
- **Mutual information.** It is invariant under invertible transforms of each variable separately (standard; e.g. Cover & Thomas). So I(x_t; x_{t+1}) = −½ log(1 − ρ_z²).
- **Ordinal-pattern statistics.** Permutation entropy is unchanged by strictly increasing g, by construction (Bandt & Pompe 2002). So it is whatever the latent Gaussian process gives.
- **Rank correlations recover ρ_z.** For a Gaussian copula, Kendall's τ = (2/π) arcsin ρ_z (standard).
- **Consequence.** In this sub-case, lagged MI and permutation entropy are functions of the **rank** autocorrelation. They can beat a rank-based AC1 only through estimation behaviour. The fair baseline is therefore rank AC1, not just Pearson AC1. Beating Pearson AC1 here would only show that rank statistics resist heavy tails.
- **What it does not cover.** α-stable-driven systems, multiplicative noise and strong nonlinearity near the fold all make the dependence itself non-Gaussian. Those regimes remain non-trivial.

### Test 2 (absence): updated with what this search found

| | Explanation | Finding (second search) |
|---|---|---|
| a | Wrong vocabulary or field | **Partly yes. This corrects the first report's "nothing found under other names".** Seizure prediction ran ROC comparisons of linear vs nonlinear measures from 2002 to 2007 and reported no univariate nonlinear advantage. The feature-screening literature ("highly comparative time-series analysis") runs indicator horse races under its own name. Neither covers QR-006b's cross-mechanism design. |
| b | Done, but not as a paper | Not found. |
| c | Too obvious to publish | Applies only to the Gaussian half (first report) and the Gaussian-copula sub-case (test 1 above). |
| d | False premise | No. Layritz 2025 confirms in full text that CSD's theoretical support fails under α-stable noise. Harris 2024 shows SD and AC1 collapse under variable noise amplitude. |
| e | Experts avoid it for a known reason | **Yes, two reasons.** (i) Information measures are data-hungry (Weinans 2021, first report). (ii) Where CSD fails, the communities that work on it reach first for distributional or model-based replacements (γ_X, RAD, Langevin, DDJ), not information measures. The seizure field's earlier negative result made nonlinear univariate measures unattractive. |
| f | Data and tools only recently available | **Yes, strengthened.** Theory for the non-Gaussian regimes dates from 2023–2025 (Morr 2023, Harris 2024, Layritz 2025), and labelled benchmarks from 2021 (Bury). |
| g | Genuinely unasked | **What remains:** no study scores information measures at matched false-alarm rates against the *full*, regime-appropriate baseline set (Pearson and rank AC1, variance, the distributional and model-based indicators above), stratified by noise type and tipping mechanism. Harris et al. explicitly left non-Gaussian and multiplicative noise unstudied. |

The absence is now explained more fully than before, by (a) partly, (e) and (f). What remains under (g) is narrower but real.

### Test 4 (expert view): a sourced addition

The likely reply from the seizure-prediction community is that a nonlinear or information statistic is worth using only if it beats variance under surrogate-validated ROC, and that it usually has not (McSharry 2003, abstract; Mormann 2005, abstract). This sharpens the first report's expert view; it does not reverse it.

### Recommended RE-SCOPE of the baseline set

This is a design change, not a new question. QR-006b should read "beat lag-1 autocorrelation and variance, **their rank-based versions, and the regime-appropriate non-information indicators** (skewness, kurtosis and bimodality; RAD; the α-stable scale factor; drift–diffusion–jump or Langevin estimates)". Without that, a "yes" is uninterpretable: it could mean information measures add something, or only that anything distributional beats AC1 when noise is non-Gaussian. The owner decides on the wording. The log's question line is not edited here. *Owner approved the re-scope later on 2026-10-18; the log's question line now carries it.*

## 5. Final verdict: **STILL PROVISIONAL (narrowed)**

**Not overturned.** No study found does the regime-stratified, matched-false-alarm benchmark. Not confirmed either, for two reasons:
1. The search turned up a needed baseline re-scope (§4) and a further triviality fold (test 1).
2. Four specific items that could still flip the verdict were not readable in this session. Item 4 has since been read (§7) and does not contain the study; three remain.

**What is left before PROCEED stops being provisional (no third search needed if these come back clean):**
1. **Dakos & Soler-Toscano 2017**, full text (closed; needs library access). This is the item most likely to contain a complexity-vs-CSD comparison across transition types.
2. **Mormann et al. 2005**, full text: the 30-measure list (are any information-theoretic, and are variance and decorrelation time included?) and the per-measure ROC results. This decides how much of the non-CSD regime the seizure literature has already settled negatively.
3. **Eason et al. 2014**, results section: how Fisher information was scored against variance, skewness and kurtosis. The owner can open the UNL Digital Commons copy (usepapapers/197) in their own browser.
4. ~~**Harris et al. 2024, Supplemental Table S1**~~: **read, 2026-10-18 (§7).** Not the study: one model, trend-tracking scores, no nulls or ROC. It gives a partial answer that supports the §4 baseline re-scope.

**If 1–4 do not contain the study:** confirm PROCEED on the re-scoped QR-006b (baseline set as in §4).
**If any does:** FOLD the matching regime with tag `found-under-other-vocabulary`, and RE-SCOPE the rest.

## 6. Notes for the wiki (owner's call; nothing written)

- **Candidate reference knowledge, not yet anchored:** the seizure-prediction negative result (Mormann 2005; McSharry 2003) as the neuroscience counterpart of EWS3/EWS4, and Layritz 2025 and Harris 2024 as non-Gaussian and unknown-noise limits of EWS1. All four would need reading upgrades first (two are abstract-only).
- **The Gaussian-copula fold** (§4, test 1) could join EWS8's linear-Gaussian equivalence note once the owner accepts it.
- **CCA and QR-007:** nothing here bears on transition-order classification.

## 7. Addendum (later on 2026-10-18): Harris et al. 2024, Supplemental Table S1

**Source and reading level.** Supplemental_Table_S1.xls is an arXiv ancillary file (`arxiv.org/src/2310.14791v3/anc/`). It is *not* in the `brendanjohnharris/criticality` GitHub repository, which holds code and figure PDFs only. **Full text** (the data file was read in full).

**Contents.** 8,018 features: 7,873 from hctsa plus 145 of the authors' own (the RAD family). Each has a fixed-noise and a variable-noise score, the Spearman ρ between the feature and the control parameter μ. 7,637 features have a variable-noise score. Rows without one carry 0 in the table's "absolute" column; this analysis treats them as missing.

**Classification.** A feature counts as "information-theoretic" if its hctsa keywords include entropy, information, AMI, sampen or mse, or if its name marks it as an entropy, automutual-information or Lempel-Ziv feature. That gives 1,299 features (1,249 scored, 16% of the scored total). This is a keyword heuristic, not a feature-by-feature reading. Symbolic-motif features (SB_Motif*) are counted as non-information.

**Reference points.** SD: fixed 0.977 (rank 7), variable 0.233 (rank 3,976). AC1: fixed 0.966 (rank 81), variable 0.482 (rank 1,516).

| Variable-noise threshold \|ρ\| | All features | Information-theoretic |
|---|---|---|
| > 0.48 (beats AC1) | 1,603 | 244 |
| > 0.7 | 177 | 4 |
| > 0.8 | 74 | **0** |
| > 0.9 | 13 | **0** |

| Family (best variable-noise \|ρ\|, rank of 7,637) | Best fixed-noise \|ρ\| |
|---|---|
| Recurrence-period density entropy, EN_rpde: **0.747, rank 120** (best information feature) | 0.755 |
| Sample / multiscale entropy: 0.708, rank 164 | 0.960 |
| Automutual information: 0.689, rank 189 | 0.971 |
| Lempel-Ziv complexity: 0.638, rank 345 | 0.958 |
| Distribution (Shannon) entropy: 0.629, rank 389 | 0.960 |
| Permutation entropy: 0.616, rank 496 | 0.892 |
| Approximate entropy: 0.419, rank 2,404 (below AC1) | 0.942 |
| *For comparison:* RAD 0.927 (rank 1); best hctsa feature CO_Embed2_Basic_1_stdincircle 0.905; SB_MotifTwo_mean_uu 0.877, rank 27 | |

**Findings.** Tag: **Established** for the numbers, read from the authors' table; **Supported** for the interpretation, which is mine.

1. **The fixed-noise regime confirms the linear-Gaussian fold on independent data.** The information features that score highest there are proxies for their second-order counterparts:
   - The entropy of the kernel-smoothed value distribution (DN_FitKernelSmoothraw_entropy) scores 0.980 fixed and 0.252 variable, almost exactly SD's 0.977 and 0.233. For a near-Gaussian distribution, differential entropy is ½ log(2πeσ²), a function of variance.
   - The automutual-information features (fixed ≈ 0.97, variable 0.54–0.60) behave like AC1 (0.966, 0.482).
2. **Under unknown noise amplitude, many information features beat SD and AC1.** 244 beat AC1's variable-noise score; the best is 0.747. **None reaches the top 100, and none exceeds 0.8.** All 74 features above 0.8 are distribution-shape, extreme-value, embedding-geometry or motif features. In this regime the answer to "does an information measure beat AC1 and variance?" is **yes, but distribution-shape features beat both by a wide margin**.
3. **Consequence for QR-006b.** This is direct evidence for the §4 baseline re-scope. Without distributional baselines, a QR-006b "yes" in this kind of regime would credit information measures with a gain that non-information features deliver more strongly.
4. **Limits.** These limits are why this is not the study QR-006b asks for:
   - one model (the supercritical Hopf normal form) with additive Gaussian noise of unknown amplitude, not non-Gaussian or multiplicative noise;
   - noise amplitude varies *across recordings*, not within a series;
   - scored by Spearman trend-tracking, not ROC against matched nulls;
   - no N- or R-tipping.

**Effect on the verdict.** Item 4 of §5 is closed and does not contain the study. The verdict stays **STILL PROVISIONAL (narrowed)**, with three items left: Dakos & Soler-Toscano 2017, Mormann 2005 and Eason 2014, each in full.


## 8. Addendum (later on 2026-10-18): the three open readings, and the final verdict

**Purpose.** This closes §5's three remaining items. The reading markers follow the rule at the top of this report, and none is upgraded. Session: QR-006b readings + pre-registration (Mode A for this section).

### 8.1 Access attempts

| Source | Routes tried | Outcome |
|---|---|---|
| **Eason, Garmestani & Cabezas 2014** | EPA archive PDF; UNL Digital Commons `usepapapers/197`; Unpaywall, OpenAlex, Semantic Scholar | EPA copy is a 2-page excerpt. The UNL PDF sits behind a Cloudflare bot check, which was not bypassed. **The owner downloaded the UNL copy in their own browser**; it was read from that file |
| **Dakos & Soler-Toscano 2017** | Unpaywall, OpenAlex (closed, "no repository has full text"), Semantic Scholar (closed; abstract elided); HAL `hal-01990931` ("Fichier non déposé"); Universidad de Sevilla idUS (not found); ScienceDirect (blocked the in-app browser); Dakos's 2019 BIRS talk slides (they list the paper in a table only) | **Unobtainable this session.** The owner chose not to pursue library access or an author request |
| **Mormann et al. 2005** | Unpaywall, OpenAlex, Semantic Scholar (all closed); Jülich JuSER record 49824 (full abstract, no file); UCL Discovery 145363 (404); the same group's 2007 *Brain* review (closed); one secondary search for a published list of the 30 measures | **Full text unobtainable.** The abstract was re-read in full from JuSER |

### 8.2 Eason et al. 2014: **full text** (owner-supplied UNL Digital Commons PDF)

**What it does.** It relates the Fisher Information index to variance, skewness, kurtosis and AR1, and to the variance index (the largest covariance eigenvalue), in four cases:
- a time-varying sinusoid;
- a two-species Lotka–Volterra predator–prey model with a time-varying parameter;
- a discrete shallow-lake phosphorus model with AR(1)-correlated input noise;
- the Bering Strait / North Pacific record: 65 variables (35 biological, 30 climate), 1965–1997, with known shifts in 1977 and 1989 (Hare & Mantua 2000).

**How indicators are scored.** In the two model systems, the relationship is the **Spearman rank correlation between the indicator time courses** ("SROC"). In the lake model and the real record, the "leading indicator" claim rests on **visual inspection of single trajectories**. There are:
- no null (no-transition) series;
- no ROC and no false-alarm rate;
- no replicate realisations;
- no stratification by noise type or tipping mechanism.

**Results relevant here.**
- In the sinusoid, FI correlates with variance at ρ = −0.98, with kurtosis at +0.81 and with skewness at −0.78.
- In the predator–prey model, FI correlates with variance at −0.74 and with AR1 at −0.68.
- The FI–AR1 and FI–skewness relationships were inconsistent across the two models.
- The near-perfect anti-correlation with variance is what the identity I = 1/σ² for Gaussian fluctuations predicts (EWS6). It is consistent with the linear-Gaussian fold, on the developers' own data.

**Verdict on this item:** **not the study.** It is a qualitative single-run comparison, by the method's developers.

### 8.3 Dakos & Soler-Toscano 2017: **search summary only** (unchanged)

**What is known** (from search summaries and a citing work's reference list only): block-decomposition (BDM) Kolmogorov complexity "decreased before all ecological transitions" in simulated time series and spatial data, across several transition types.

**Not known:**
- whether it scores against AR1 or variance at all;
- whether it uses null series, ROC or false-alarm rates;
- which transition types are included, in particular whether any are noise- or rate-induced.

**Which QR-006b regimes it could touch:**
- the bifurcation-induced strata of the pre-registration (C0 and S3, possibly S1);
- S4 and S5, if its "types of transition" include noise- or rate-induced tipping.

It could not touch the α-stable (S2) or multivariate (SM) strata. Neither is in its reported scope, which is a search-summary-level statement.

**Its measure (BDM complexity) is not in the pre-registered indicator set.** If the paper turns out to show BDM complexity beating AC1 and variance at matched false-alarm rates in some regime, that regime FOLDs (`found-under-other-vocabulary`), and adding BDM to the benchmark is an owner decision (a logged deviation).

### 8.4 Mormann et al. 2005: **abstract** (re-read in full, Jülich JuSER record)

**What is known.**
- 30 univariate and bivariate, linear and non-linear measures, on continuous intracranial EEG from five patients over days.
- ROC curves separate the amplitude distributions of preictal and interictal profiles, with an emphasis on statistical validation.
- Univariate measures were significant only in a channelwise, seizurewise analysis with an adaptive baseline (changes 5–30 min before seizures).
- Bivariate measures were significant with a constant baseline (changes at least 240 min before).
- "Linear measures were found to perform similar or better than non-linear measures."

**Not known:**
- the measure list: whether any of the non-linear measures are information-theoretic, and whether variance and decorrelation time are the linear baselines;
- the per-measure ROC values.

A secondary search summary says decorrelation time separated the periods, and that correlation dimension, Lyapunov exponent and signal energy did not. That is a lead, not a reading.

**Which QR-006b regimes it could touch.** It is one empirical system (epileptic EEG), not labelled by noise type or tipping mechanism, and it does not stratify. It therefore **cannot fold any simulated stratum**. It bears on the empirical stratum E only, and as a prior on the answer: the seizure field's negative result for univariate non-linear measures, at abstract level, is evidence for an eventual NO.

### 8.5 Final verdict: **PROCEED with named gaps**

| Item | Reading level | Contains the QR-006b study? |
|---|---|---|
| Eason et al. 2014 | full text | **No** (clean) |
| Dakos & Soler-Toscano 2017 | search summary | **Unknown: gap.** Could touch C0/S1/S3, and S4/S5 if those types are included |
| Mormann et al. 2005 | abstract | **Unknown in detail, but structurally cannot be the stratified study** (one empirical system, no regime labels). Gap for stratum E and for the prior only |

- **Not PROCEED confirmed.** Two items are unobtainable, so "all three clean" is not established.
- **Not FOLD.** The one item read in full is clean, and nothing read contains the study.
- The QR-006b PROCEED (re-scoped, widened baselines) stands, **with two named gaps**:
  1. **Dakos & Soler-Toscano 2017** (bifurcation, flickering and possibly N/R strata; BDM complexity not in the indicator set);
  2. **Mormann et al. 2005** (empirical stratum and prior).

  Both are carried into the pre-registration (`docs/experiments/QR006B_BENCHMARK_PREREGISTRATION.md` §10, gap 1).
- **Re-open the verdict if either is read later.** If Dakos & Soler-Toscano 2017 contains a matched-false-alarm comparison against AR1 and variance, the overlapping strata are recorded as replications (`found-under-other-vocabulary`), not new answers.

**Tag:** the verdict is a process record, not a scientific claim. Nothing is promoted.

# QR-006 — well-posedness review, prior-art gate, and worth-asking gate

**Date:** 2026-10-18 · **Question:** QR-006 (Questions Raised Log), owner's priority · **Gates:** `memory/feedback_prior_art_gate.md` (Gate 1), `docs/QUESTION_GATES.md` (Gate 2) — first use of Gate 2
**Inputs:** `QR-006_EWS_LITERATURE_MAP_2026_10_18.md` (agent map), plus the first-hand checks in this report. Sources marked *verified* were read in this session (abstract or full text, as stated); the rest come from the agent map and are leads.

---

## Part 1 — Is QR-006 well-posed?

**As logged:** *Do information-theoretic measures give earlier or more reliable warning of critical transitions in real systems than rising variance and autocorrelation?*

**Not yet.** It bundles five problems.

1. **"Earlier" is undefined without a false-alarm rate.** Any indicator fires earlier if its threshold is lowered. The comparison has to be made at matched specificity: ROC-AUC against matched no-transition series, or lead time at a fixed false-alarm rate.
2. **"Tipping points" covers different mechanisms.** Bifurcation-induced tipping (fold, transcritical, Hopf) is the only kind critical-slowing-down (CSD) theory covers. Noise- and rate-induced tipping can occur with no slowing at all (Ashwin et al. 2012; Ditlevsen & Johnsen 2010 — leads). The question has to be asked per mechanism.
3. **"Information measures" is a heterogeneous family.** It includes lagged mutual information, transfer entropy (multivariate), the ecological Fisher Information index, permutation and sample entropy, and complexity measures. **Correlation-matrix concentration** (participation ratio, absorption ratio, largest-eigenvalue share) belongs to a different family: it is a second-order statistic, not information-theoretic. The wiki's CCA observable belongs there.
4. **In the regime where the classical theory holds, the answer is largely known in advance (triviality — see Gate 2, test 1).** Near a bifurcation, with small noise, fluctuations are approximately a linear, stationary, Gaussian (Ornstein–Uhlenbeck) process. That approximation is the basis of CSD theory. For such processes the information measures are functions of the autocovariance:
   - lagged mutual information = −½ log(1 − ρ²) for a bivariate Gaussian with correlation ρ (textbook identity), so it is a monotone function of lag-1 autocorrelation;
   - transfer entropy equals Granger causality for Gaussian variables — Barnett, Barrett & Seth 2009, *PRL* 103:238701 (*verified, abstract*) — a second-order quantity;
   - ordinal-pattern probabilities, and hence permutation entropy, for Gaussian and ARMA processes are derived in Bandt & Shiha 2007, *J. Time Ser. Anal.* 28:646 (*verified, abstract*). For Gaussian processes they are orthant probabilities fixed by the autocorrelations;
   - the location Fisher information of a Gaussian is 1/σ² (textbook), the inverse of variance.

   So in the textbook CSD regime the information measures carry **no information beyond autocorrelation and variance**. They can differ only through estimation, where they are noisier: Weinans et al. 2021 found them data-hungry (*verified, full text*). Information measures can add real skill only where the linear-Gaussian picture fails: non-Gaussian, heavy-tailed or multiplicative noise; strong nonlinearity close to the fold (skewness, flickering, multimodality); and noise- or rate-induced tipping, where CSD itself fails.
5. **The wiki's CCA results don't bear on lead time directly.** CCA and Brown et al. 2022 are equilibrium temperature sweeps. A peak "before" T_c in control-parameter space is not a lead time in a slowly forced time series. CCA belongs to a separate sub-question: classifying the *type* of transition.

### The re-scoped question

> **QR-006b.** On a common labelled benchmark of transition series and matched no-transition series, scored at matched false-alarm rates, does any information-theoretic indicator beat lag-1 autocorrelation and variance, measured by ROC-AUC or by lead time at fixed specificity? In particular, does it do so where the linear-Gaussian approximation fails: non-Gaussian or multiplicative noise, strong nonlinearity near the fold, and noise- or rate-induced tipping?

**Plain language (charter rule 5):** *Do information-based warning signs ever beat the standard ones, and is it only where the standard theory's own assumptions break down?*

QR-006 itself stays in the log as the umbrella question. QR-006b is what the gates assess.

---

## Part 2 — Gate 1: prior art

**Search angles:**
1. Head-to-head ROC or lead-time comparisons of information measures against autocorrelation and variance.
2. Benchmarks of multivariate resilience indicators.
3. Field reviews.
4. Machine-learning early-warning benchmarks, which publish labelled data.
5. Gaussian equivalence results.
6. 2026 preprints.
7. Spectral early-warning signals.

| Source | Read | Bearing on QR-006b |
|---|---|---|
| **Weinans, Quax, van Nes & van de Leemput 2021**, *Sci. Rep.* 11:9148 | *verified, full text* | **Closest prior art.** Compares 13 multivariate indicators including **lagged mutual information**, on one plant–pollinator model family (4D, 20D), under data-degradation scenarios. Scored by **Kendall τ against the bifurcation parameter, not ROC**; specificity checked only in a supplement. MI is the indicator most hurt by measurement noise and fails in both 20D models under multiplicative noise; they advise against it unless data are abundant. Fisher information and entropy measures were **explicitly left out**. No real data, no noise- or rate-induced tipping. |
| **Dakos et al. 2024**, *Earth Syst. Dynam.* 15:1117 (review of real-world EWS studies) | *verified, full text (to 100k chars)* | No information-theoretic indicator appears among the reviewed real-world applications. States that few studies have systematically compared warnings across systems, so their overlapping information is unclear (§4.3.1), and recommends exactly that. Notes publication bias toward positive results. |
| **Bury et al. 2021**, *PNAS* 118:e2106140118 | *verified, abstract + repository* | ROC benchmark of deep learning against autocorrelation and variance on model series with null runs and empirical records (anoxia cores, thermoacoustics, paleoclimate). **No information measures.** Repository ships simulation scripts for transition and null runs and the empirical records; licence CC BY-NC-SA 4.0. |
| Ngueuleweu 2026, arXiv:2607.11935 | *verified, full text* | Computes permutation entropy and MI, but only as lead-lag correlations against its own signal on one satellite dataset; no known transitions, no nulls, no ROC. **Not prior art.** |
| Yu & Liang 2026, arXiv:2606.17553 | *verified, abstract* | Uses transfer entropy to build a spatial causal graph; the warning comes from recovery rates. AUROC 0.783 on AMOC against an AR1 baseline. TE is a network-building tool there, not the indicator under test. **Adjacent.** |
| Tirabassi & Masoller 2023, *PNAS* 120:e2215667120 | agent map | Spatial permutation entropy vs spatial correlation: mixed (better / similar / worse by system). Not against AC1 and variance on a common benchmark. **Adjacent.** |
| Bury et al. 2020, *J. R. Soc. Interface* 17:20200482 (spectral EWS) | search summary | AUCs for a spectral indicator vs variance. Spectral, not information-theoretic. **Adjacent.** |
| Barnett, Barrett & Seth 2009; Bandt & Shiha 2007 | *verified, abstracts* | Establish the Gaussian equivalences in Part 1 (Gate 2, test 1). |
| *Entropy* 28:628 (2026), "Early warning signals in ecological time-series" | **not read** (HTTP 403) | Unknown; could contain a comparison. **Open check.** |

**Gate 1 verdict:**
- **The generic benchmark is OPEN IN THE LITERATURE.** A cross-system ROC comparison of information measures against autocorrelation and variance is a gap the field itself names (Dakos et al. 2024, §4.3.1). The closest study, Weinans 2021, used one model family, Kendall τ instead of ROC, and only mutual information.
- **The regime-stratified version is NO PRIOR ART FOUND — provisional.** That version tests specifically where the linear-Gaussian equivalence breaks. Remaining risks: the unread *Entropy* 2026 review; Dakos & Soler-Toscano 2017 (complexity indicators); and the machine-learning EWS literature, which may include information-measure baselines this search did not surface.

---

## Part 3 — Gate 2: worth-asking

**1. Triviality.** *Partially trivial.* In the linear-Gaussian regime where CSD theory holds, the answer follows in five minutes from the identities in Part 1. The information measures are functions of the autocovariance, so they can match autocorrelation and variance at best, and will usually do worse because they are noisier estimators. That part is a re-derivation and **FOLDS**. Outside that regime the identities say nothing, and the question is not trivial.

**2. Why is the regime-stratified benchmark absent?**

| | Explanation | Finding |
|---|---|---|
| a | Wrong vocabulary or field | Searched "mutual information", "transfer entropy", "permutation entropy", "Fisher information", "complexity", "information dissipation", "multivariate resilience indicators", "ROC/AUC", "null model". Nothing found under other names. |
| b | Done but not as a paper | The Gaussian redundancy is very likely known informally: Weinans et al. describe MI as a *nonlinear alternative* to autocorrelation. Not found stated as an early-warning result; partial. |
| c | Too obvious to publish | Applies to the Gaussian half (test 1) only. |
| d | False premise | No: CSD's linear-Gaussian basis and its failure regimes are established. |
| e | **Experts avoid it for a known reason** | **Yes, partly:** information measures are data-hungry, and their theoretical link to transitions is weaker than for simpler metrics (Weinans et al. 2021, background and Box 1, *verified*). Real ecological series are short. |
| f | **Data and tools only recently available** | **Yes, partly:** labelled transition and null benchmarks with public scripts date from 2021 (Bury et al.). Since then the field's methods effort has gone mainly into machine learning, not information measures. |
| g | Genuinely unasked | What remains after a, b, c and e: no study tests whether information measures earn their data cost *specifically where* CSD's assumptions fail. |

The absence is explained for the generic question by (e) and (f). For the regime-stratified question, (g) remains, and (f) shows why it is feasible now.

**3. Obvious or erroneous?** Well-posed in the re-scoped form, provided that:
- indicators, windows, detrending and thresholds are fixed **in advance**;
- the same preprocessing is used for every indicator (Dablander & Bury 2022 show that preprocessing changes results — lead);
- each transition series has matched null series;
- metrics are ROC-AUC, plus lead time at fixed false-alarm rates.

One trap: in noise- and rate-induced tipping, *nothing* may beat chance, and then "beats CSD" is empty. So every indicator has to be scored against chance as well as against CSD.

**4. Expert view.** The likely one-line reply from an early-warning researcher: *"Information measures are data-hungry and mostly re-express autocorrelation near a bifurcation; use them only when data are abundant."* This is sourced to Weinans et al. 2021, Discussion and Box 1, *verified*. The same researcher would likely add that systematic cross-indicator comparisons are missing and needed: Dakos et al. 2024, §4.3.1, *verified*. So experts deprioritise information measures for a stated reason, but they do not regard the question as settled.

**5. Should it be asked?**
- **A "yes"** (information measures beat CSD in a named regime) rules out "CSD indicators are sufficient for non-Gaussian, nonlinear or noise-induced systems". It would justify adding specific information indicators to the toolbox for those cases.
- **A "no"** (they never beat CSD at matched false-alarm rates) rules out recommending them outside data-rich settings. That is a clean negative the field currently lacks: practice guidance changes either way.
- **Decidable:** yes, on public data. The Bury et al. 2021 simulation scripts with null runs, plus the anoxia, thermoacoustic and paleoclimate records; the Weinans model family; standard estimators. Modest compute.
- **Cost:** moderate, and it serves the owner's top question directly.

**Gate 2 verdict:**
- **FOLD** the linear-Gaussian equivalence: information measures are functions of the autocovariance in the CSD regime. Record it as knowledge, a re-derivation from standard identities, not a finding.
- **RE-SCOPE → PROCEED (provisional)** on QR-006b, in its regime-stratified form. Reason tag for the folded part: `trivial-from-known-result`. **What is unasked, in one sentence:** no study has tested, on a common labelled benchmark at matched false-alarm rates, whether information-theoretic indicators beat autocorrelation and variance *specifically where* the linear-Gaussian assumptions behind critical slowing down fail. The absence is partly explained by data-hungriness (e) and by benchmarks only being available since 2021 (f).

**Provisional until:**
1. A second, independent search — a different session using different vocabulary, including the machine-learning EWS literature and the unread *Entropy* 2026 review — fails to find the study.
2. The unread leads that could flip the verdict are read: Dakos & Soler-Toscano 2017, and Eason et al. 2014 in full.

---

## Bearing on the wiki's own work

- **CCA's participation ratio** is a second-order (covariance) statistic. In the Gaussian regime it carries the same information as covariance-eigenvalue indicators (Chen et al. 2019 eigenvalue share; Weinans 2021 explained variance), so it gets no special standing in QR-006b. It can enter only as a covariance-family entrant. CCA's distinct angle, classifying transition *order*, is a separate question and should be logged separately (proposed **QR-007**). The CCA-1c reduction test, still pending, bears on it directly.
- **X0's Fisher-information framing** inherits the same point: in Gaussian fluctuations, Fisher information is a function of the covariance.
- **New knowledge to fold in** (owner's call; the early-warning fold-in session may already cover some): the four Gaussian equivalences above, as a reference entry or a section of the CSD entry, citing Barnett, Barrett & Seth 2009 and Bandt & Shiha 2007.

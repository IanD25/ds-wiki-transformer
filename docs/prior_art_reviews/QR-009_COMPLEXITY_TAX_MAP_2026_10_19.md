# QR-009 literature map — the complexity tax (2026-10-19)

> **Provenance (2026-10-19).** Mode A, literature mapping only. This is the map for Questions Raised Log entry **QR-009**, raised by the owner today: *when does making a predictive or decision model smarter make it worse out of sample, and what sets the size of that penalty?* Following the deep-research pattern, the search was fanned out across seven read-only research sub-agents:
> 1. statistics and machine learning (bias–variance, model selection, effective degrees of freedom, double descent);
> 2. finance I: estimation error in portfolios, 1/N, turnover and costs, volatility management, dynamic hedging;
> 3. finance II: backtest overfitting, the factor zoo, out-of-sample failure of return predictors, the "virtue of complexity" debate;
> 4. forecasting: the combination puzzle, the M-competitions, forecasting under breaks;
> 5. decision science, regulation and reflexivity (improper linear models, heuristics, "The dog and the frisbee", Goodhart, Lucas);
> 6. engineering, control and biology (HOT, Bode, adaptive control, named heuristics, the cost of complexity in evolution);
> 7. what sets the "tax rate" (tracking versus noise, estimation windows under breaks, regime-switching failure, adjustment costs, bandits), and where the phrase comes from.
>
> **Sub-agent summaries are leads, not readings.** The main session re-checked the load-bearing citations itself: about 75 DOIs against Crossref, about 25 abstracts, and the headline numbers in 19 primary texts by PDF text extraction (column "MS" in §J). It also checked numerically the two closed forms used in §E. Markers in §J are never upgraded. The sub-agents' notes are kept outside the repo, in the session notes folder (`research_notes/Complexity tax literature map/`, files 1–7).
>
> **The wiki itself was read, not written.** `ds_wiki.db` (entries, sections, conjectures P18–P20) and `wiki_history.db` (`claim_status_latest`) were queried read-only. No gate has been run, nothing has been folded in, and nothing has been written to either database. Confidence tags: **Established / Supported / Speculative**.
>
> **Scope note.** The owner's AlphaEntropy project is discussed only through the facts in the 2026-10-19 read-only review summary given to this session; the project itself was not opened. Nothing here is investment advice.

**QR-009 in one sentence a physicist could check:** *A more flexible or more adaptive rule fitted to a finite, noisy and possibly changing record usually predicts worse than a simpler one, unless the record is long enough relative to the rule's effective number of free choices; how long "long enough" is depends on noise, change rate, adjustment costs and how many variants were tried.*

---

## (A) The answer in plain terms

- **The phenomenon is old, well documented and well explained, under other names.** Statistics calls it *overfitting* and the *variance* half of the bias–variance trade-off. Finance calls it *estimation error* and *backtest overfitting*. Forecasting calls it the *combination puzzle* and *forecast failure under breaks*. Psychology calls it *less-is-more*. Control theory has *robustness of adaptive control* and the Bode *waterbed*. Evolutionary biology has a formal *cost of complexity* (Orr 2000). No field treats "simple beats complex" as unexplained.
- **"Complexity tax" is not a technical term anywhere we looked.** It appears informally in software, DevOps and management writing, with no definition and no identifiable coiner (Google Ngram: rare, peaking around 2008). The quantified neighbours are the statistical *complexity penalty* (AIC, BIC, MDL), Orr's *cost of complexity*, and Besbes, Gur & Zeevi's *price of non-stationarity*. If the wiki adopts the owner's phrase, it should be defined as shorthand for these, not presented as a new concept.
- **There is no single tax.** At least seven distinct mechanisms produce "smarter did worse", and they have different rates and different cures (§F):
  1. estimation variance;
  2. selection over many tries;
  3. lag versus noise in a changing world;
  4. costs per adjustment;
  5. misreading turning points;
  6. fragility to what the design did not anticipate;
  7. the environment reacting to the model.

  Only the first three share mathematics in a strict sense. The rest share a logical shape.
- **What sets the rate is known in closed form for the cleanest cases (§E).**
  - **Per parameter:** σ²/N in-sample for least squares, rising as γ/(1−γ) with γ = p/n out of sample.
  - **Per variant tried:** the best of N skill-less tries looks, on average, like 1.57 standard errors of "skill" at N = 10 and 2.28 at N = 50, growing as roughly √(2 ln N) (an upper bound). With 5 years of data, 45 tries give a Sharpe of about 1 from nothing (Bailey et al. 2014).
  - **Per unit of change rate:** the best adaptive rule pays about σ²√q, where q is drift variance over noise variance; a never-updating rule pays lag growing with the length of the record (Muth 1960; Widrow et al. 1976).
  - **Per unit of trading cost:** the optimal "do nothing" band widens as cost^(1/3), and the loss is of order cost^(2/3), in continuous time.

  Everywhere, the effective sample size is the number of independent events that inform the parameter, not the number of rows.
- **Complexity wins under identifiable conditions (§D, primer (d)):**
  - the effective data are plentiful: M5 pooled 30,490 related retail series and won by 22%;
  - the extra parameters are regularised toward the simple rule: shrinkage, ridge, intermediate Bayesian priors, mixing with 1/N;
  - the environment changes often and cheaply observed signals track it;
  - in very-high-dimensional, high-signal settings, interpolating models can generalise ("double descent", with stated conditions).

  Whether that last result carries over to low-signal financial prediction is **openly contested** (Kelly, Malamud & Zhou 2024 against Nagel 2025 and others).
- **The intermediate option usually beats both extremes.** In every field mapped, the best performer is neither the simplest rule nor the unrestricted complex one. It is a *shrunk* version: James–Stein, ridge, Bayesian ridge between tallying and regression (Parpart et al. 2018), 1/N mixed with optimisation (Tu & Zhou 2011), optimal exponential smoothing, pooled estimation windows. "Less is more" mostly means "less than unregularised".
- **For the wiki.** Coverage is thin: no entry on bias–variance, model selection, multiple testing, forecast combination, heuristics, Goodhart/Lucas, HOT/Bode or Orr (§G). Two AlphaEntropy-derived conjectures bear on QR-009 directly:
  - P19's "validated fix" is a Calmar gain of +0.006, below the project's own +0.02 adoption threshold;
  - P20's error formula conflicts with the textbook identity for averaging equally good signals.

  Both are flagged for owner review (§G.3); nothing was changed.
- **The AlphaEntropy case** (project records, §G.4). The core strategy survives a correctly specified deflated Sharpe test. The dynamic additions do not survive their own tests. The tax fell on the increments, not on the whole system.

**Calibrated summary.**

| Claim | Tag |
|---|---|
| Out-of-sample error of a fitted model contains a variance term that grows with effective degrees of freedom and falls with sample size | **Established** (ESL §7.3; Hastie et al. 2022 Thm 1) |
| Model search spends more effective degrees of freedom than the parameters finally kept | **Established** (ESL §7.5; Ye 1998; Freedman 1983) |
| Selecting the best of N noisy variants inflates its apparent performance by an amount growing like √(2 ln N) standard errors | **Established** (extreme-value statistics; Bailey et al. 2014; Smith & Winkler 2006) |
| For a randomly drifting quantity, the optimal degree of adaptation and its irreducible cost are closed-form functions of drift-to-noise ratio | **Established** (Muth 1960; Widrow et al. 1976; local-level Kalman filter; checked numerically here) |
| Simple rules often match or beat complex ones out of sample in portfolios, macro and business forecasting, bank-failure prediction and judgement tasks | **Supported** (many studies; effect sizes vary widely; several comparisons use *unregularised* complex benchmarks) |
| A regularised (shrunk) model generally beats both the simplest rule and the unregularised complex one | **Supported** (Parpart et al. 2018; Şimşek & Buckmann 2015; Tu & Zhou 2011; Hastie et al. 2022 for ridge) |
| Over-parameterised interpolating models can generalise well | **Established** for linear and random-feature models under stated spectral and SNR conditions; **Supported** empirically for deep nets; **contested** for return prediction |
| The various "simple beats complex" results across fields are one law | **Not supported.** They are several mechanisms (§F); only the first three share mathematics |
| "Complexity tax" is a term of art | **No.** Informal usage only (search summary level) |

---

## (B) Settled — Established

### B1. The per-parameter variance cost
- **The decomposition.** Err(x₀) = σ² + Bias² + Variance. For least squares with p fitted parameters, the variance averaged over the training inputs is exactly **(p/N)σ²** (ESL, Hastie, Tibshirani & Friedman, 2nd ed., §7.3, eq. 7.12; sub-agent read).
  - A parameter that removes no bias is pure cost at σ²/N each.
  - The standard reference for the dilemma framing is Geman, Bienenstock & Doursat 1992 (*Neural Comput.* 4:1).
- **Out of sample it is worse than linear.** With random isotropic features and γ = p/n < 1, least-squares risk is **σ²γ/(1−γ)**, which diverges as p → n (Hastie, Montanari, Rosset & Tibshirani 2022, *Ann. Statist.* 50:949, Thm 1).
  - In that model, least squares beats simply predicting zero only when γ < SNR/(SNR + 1).
- **Model-selection penalties put a price on each parameter.** On the −2 log-likelihood scale:
  - AIC charges **2** per parameter and estimates in-sample error; it over-selects as N grows (Akaike 1974).
  - BIC charges **ln N** per parameter; it is consistent only if the true model is among the candidates (Schwarz 1978).
  - Crude two-part MDL gives the BIC criterion (Rissanen 1978).
  - All three assume independent draws from a fixed distribution. Cross-validation assumes the folds are exchangeable with future data (Stone 1974). **None of them protects against change over time** (ESL §7.4–7.8).

### B2. Search costs more than it shows
- **The general measure is effective degrees of freedom**, df = Σ Cov(ŷᵢ, yᵢ)/σ² (Efron 1986, 2004; Ye 1998, *JASA* 93:120).
  - Ridge spends fewer than p.
  - Choosing the best subset of d inputs from p spends **more than d** (ESL §7.5).
  - A one-split regression tree on n = 100 spends about 5.7–9.9 df, not 2 (Wang, Zhao & Fan 2024, *JCGS*; simulation).
- **Freedman's paradox.** Regress pure noise on 50 noise predictors with n = 100: R² averages (p−1)/(n−1) ≈ 0.5. Screen out the weak predictors and refit, and the result still looks significant, with R² ≈ 0.37 and miscalibrated F-tests.
  - Original: Freedman 1983, *Am. Stat.* 37:152, not read.
  - The numbers are from Ding's 2024 textbook replication, arXiv:2401.00649.
- **The workflow version.** Undisclosed analytic choices raised false-positive rates from 5% to about 61% in simulation (Simmons, Nelson & Simonsohn 2011; search summary). The inflation happens even without deliberate fishing (Gelman & Loken 2014). **Supported.**

### B3. Selection over many tries: the optimiser's curse
- **The expected maximum of N independent standard normals** is ≈ (1−γ)Z⁻¹(1−1/N) + γZ⁻¹(1−1/(Ne)), with γ the Euler–Mascheroni constant, bounded by √(2 ln N).
- **Applied to backtests** (Bailey, Borwein, López de Prado & Zhu 2014, *Notices AMS* 61:458, Thm 3.1; **main session read the passage**): with only 5 years of data, "no more than 45 independent model configurations should be tried" before a skill-less strategy is almost certain to show an in-sample Sharpe of 1. The required record length grows as ≈ 2 ln N / (target Sharpe)².
- **Overfitting can turn harmful.**
  - If returns have no memory, optimising in-sample is merely useless out of sample.
  - With a global constraint or mean reversion, in-sample rank and out-of-sample rank **invert**: the better a variant looked, the worse it does (§6, Props 6.1–6.3).
- **Smith & Winkler 2006** (*Mgmt Sci.* 52:311; main session read the figure) is the decision-analysis form. Picking the best of 3, 4 or 10 options on unbiased but noisy estimates leaves you on average **0.85, 1.03 or 1.54** estimate standard deviations short. The cure is to shrink the estimates toward a prior before choosing.
- **This is the same object as Manheim & Garrabrant's "regressional Goodhart"** (2018, arXiv:1803.04585). That identification is our inference: neither paper makes it, so do not attribute it.

### B4. Shrinkage toward the simple rule dominates both extremes
- **James–Stein.** Estimating three or more means jointly, shrinking toward a common value beats estimating each separately (Stein 1956; Efron & Morris 1977).
- **The portfolio versions:**
  - covariance shrinkage (Ledoit & Wolf 2003, 2004);
  - constraints acting as shrinkage (Jagannathan & Ma 2003, *JF* 58:1651);
  - mixing optimisation with 1/N (Tu & Zhou 2011, *JFE* 99:204);
  - the three-fund rule under parameter uncertainty (Kan & Zhou 2007, *JFQA* 42:621).
- **The heuristics version** (Parpart, Jones & Love 2018, *Cogn. Psychol.* 102:127; main session read the abstract):
  - tallying and take-the-best are Bayesian regression "under the limit of infinitely strong priors";
  - "intermediate models perform better across all our simulations";
  - it is never optimal to discard information at the computational level.

### B5. Lag against noise in a changing world (closed form)
- **Muth's result.** For a level that drifts as a random walk observed with noise, exponential smoothing is the optimal linear forecast. Its weight is set by q = σ²_drift/σ²_noise (Muth 1960, *JASA* 55:299; metadata plus secondary).
- **The closed form** (main session checked against a Riccati iteration):
  - in steady state the Kalman gain is k = p/(1+p), with p = (q + √(q² + 4q))/2, so k ≈ √q for small q;
  - one-step excess error over a known level is pσ²_noise ≈ √q·σ²_noise;
  - for q = 0.04 the gain is 0.18100, matching QuantEcon's published value.
- **The rolling-window version** (sub-agent derivation; main session confirmed by a 200,000-step simulation):
  - loss ≈ σ²_noise/w + σ²_drift·w/3, minimised at w* = √(3/q);
  - setting the window wrong by a factor of 2 raises the excess loss by 25%; a factor of 4 raises it by 113%;
  - a rule that never updates pays a lag cost growing linearly with record length.
- **LMS adaptive filters** have the same structure (Widrow, McCool, Larimore & Johnson 1976, *Proc. IEEE* 64:1151; abstract-level).
  - Gradient-noise error grows with adaptation speed and the number of weights.
  - Lag error falls with speed.
  - Total error is minimised when the two are equal.
- **The worst-case version** (Besbes, Gur & Zeevi; arXiv:1405.3316 Thms 1–2, sub-agent read). With total change budget V_T over horizon T, the best achievable regret is of order **V_T^(1/3) T^(2/3)**. Their 2015 paper (*Oper. Res.* 63:1227; main session read the abstract) calls this "the price of non-stationarity".

### B6. Costs per adjustment
- **The no-trade band.** With proportional trading costs ε, the optimal policy does nothing inside a band and trades at its edge.
  - In continuous time the band's half-width scales as **ε^(1/3)** and the welfare loss as **ε^(2/3)** (Constantinides 1986; Davis & Norman 1990; Shreve & Soner 1994).
  - Rogers 2004 asks the ε^(2/3) question in his title. Content is search-summary level; the exponent differs in discrete time and for fixed costs. **Established in the literature; our reading is secondary.**
- **The dynamic-trading version** (Gârleanu & Pedersen 2013, *JF* 68:2309). With quadratic costs, "aim in front of the target" and "trade partially".

### B7. Hard limits on feedback: the waterbed
- **Bode's sensitivity integral.** For a stable loop of relative degree ≥ 2, ∫₀^∞ ln|S(jω)| dω = 0. With unstable open-loop poles the integral is π Σ Re(p_k).
  - Sensitivity pushed down at some frequencies must rise at others, however complex the controller.
  - Sources: Bode 1945; Freudenberg & Looze 1985; Seron, Braslavsky & Goodwin 1997. **Established theorem, for linear time-invariant feedback.**
- **Chandra, Buzi & Doyle 2011** (*Science* 333:187; main session read the passage) apply a strengthened form to a glycolysis model: more controller complexity "can thus fine-tune the shape" of the sensitivity "but cannot uniformly improve it". **Shared mathematics, not analogy**, because glycolysis has a real feedback loop.

### B8. Reflexivity as a principle
- **Goodhart (1975):** any observed statistical regularity "will tend to collapse once pressure is placed upon it for control purposes" (wording via secondary sources).
  - The familiar "when a measure becomes a target…" is Strathern's 1997 paraphrase; she credits the label "Goodhart's law" to Hoskin (sub-agent read Strathern).
- **The Lucas critique (1976):** reduced-form relations estimated under one policy are not invariant to a change in policy.
- **Campbell's law (1979):** the corrupting pressure on indicators used for social decisions.
- **Status.** All are Established as principles. Their *size* in practice is contested (§D6).

---

## (C) Measured — where the tax was quantified, and how big

| Domain | Study | Simple vs complex | Size of the tax | Mechanism (§F) | MS |
|---|---|---|---|---|---|
| Portfolios | DeMiguel, Garlappi & Uppal 2009, *RFS* 22:1915 | 1/N vs 14 optimising models, 7 datasets | None of the 14 consistently beats 1/N on Sharpe, certainty-equivalent return or turnover. Window needed for mean–variance to win: about **3,000 months (25 assets), 6,000 months (50 assets)** | estimation variance | abs |
| Portfolios, rebuttal | Kirby & Ostdiek 2012, *JFQA* 47:437 | Low-turnover volatility timing vs 1/N | Mean–variance often beats 1/N gross; turnover erodes it. Their low-turnover timing rules beat 1/N even with high costs | variance + costs | abs |
| Volatility management | Cederburg, O'Doherty, Wang & Yan 2020, *JFE* 138:95 | Real-time scaled + unscaled mix vs plain factor, 103 strategies | In-sample: 77/103 positive alphas. **Real time: only 45/103 beat the plain factor on Sharpe, 31/103 on certainty-equivalent return.** Cause: structural breaks in the combination regressions. Survivors: momentum, profitability, betting-against-beta | non-stationarity + estimation | ft |
| Return predictors | Welch & Goyal 2008, *RFS* 21:1455 | Equity-premium predictors vs historical mean | Predictors "predicted poorly both in-sample and out-of-sample", would not have helped a real-time investor | variance + instability | abs |
| Return predictors | Campbell & Thompson 2008, *RFS* 21:1509 | Same, with sign restrictions | Restricted forecasts beat the mean; gains "small, but … economically meaningful". Monthly out-of-sample R² of 0.25% ≈ a 21% gain in expected return for a mean–variance investor | shrinkage cures variance | ft (abstract) |
| Publication decay | McLean & Pontiff 2016, *JF* 71:5 | 97 published predictors | Returns **26% lower out of sample** (an upper bound on data mining), **58% lower post-publication**. They attribute the 32-point difference to publication-informed trading | selection + reflexivity | ft (abstract) |
| Factor zoo | Harvey, Liu & Zhu 2016, *RFS* 29:5 | 316 factors | A new factor needs **t > 3.0**; "most claimed research findings in financial economics are likely false". Dissent: Jensen, Kelly & Pedersen 2023 find most factors replicate under a hierarchical Bayesian model | selection | ft (abstract) |
| Backtests | Bailey et al. 2014 (§B3) | N variants on y years | 5 years tolerate about 45 independent tries | selection | ft |
| Researcher choices | Menkveld et al. 2024, *JF* 79:2339 | 164 teams, same data, same hypotheses | Dispersion across teams about twice what the median standard error implies (one hypothesis: 6.7 vs 3.4 points). Peer feedback cut it by 47%; teams underestimated it | selection (forking paths) | cit |
| Hedging | Lien 2005, *J. Futures Mkts* 25:1121 | Static least-squares hedge vs correct error-correction model | The misspecified static hedge "usually outperforms" the correct model's hedge; the reverse needs a major post-sample structural change | estimation variance | ss |
| Market timing via ML | Kelly, Malamud & Zhou 2024, *JF* 79:459 | 12,000 random features, 12-month windows | Timing Sharpe +0.47/yr (t ≈ 3) with negative out-of-sample R²; "divest" before 14 of 15 recessions. **Contested:** Nagel 2025 (NBER WP 34104) reproduces it with volatility-timed momentum and shows the method "mislearns" on reversal data. By KMZ's own theory the achievable Sharpe is ≈ 0.017 annualised | inductive bias vs learning | ft |
| Regulation, large banks | Haldane & Madouros 2012, BIS speech | Leverage ratio vs risk-weighted Basel ratio, ~100 global banks | Failed banks' pre-crisis leverage ratio was lower by 1.2 points (significant at 1%); the risk-weighted ratio did not separate them. The simplest capital measure had "about 10 times" the explanatory power | estimation variance (and Goodhart) | ft |
| Regulation, US banks | same | 5-indicator CAMEL model vs single indicators | With 100 banks the model "is out-performed by every one of the single-indicator models", and by a constant. With 1,000 banks it still loses to one liquidity indicator. *But* among ~8,500 US banks the risk-weighted ratio wins, which the authors read as banks already managing to the leverage rule | variance; reflexivity | ft |
| Simulation | same | GARCH(3,3) truth vs simpler GARCH | Below ~2 years of daily data the simple model beats the true one ("trumps the truth"); the true model wins only beyond ~100,000 days (400 years) | estimation variance | ft |
| Bank failure | Aikman et al. 2021, *Ind. Corp. Change* 30:317 (BoE FSP 28, 2014) | 4-question decision tree vs logit, 116 banks | Trees "can perform comparably" out of sample: a tie, not a win | variance | ft |
| Judgement | Dawes 1979, *Am. Psychol.* 34:571 | Equal weights vs regression vs committee | Oregon graduate ratings: equal weights **.48**, cross-validated regression **.38**, admissions committee **.19**. In the large-sample study (861 patients) regression wins (.46 vs .34). Rule of thumb: about 15–20 observations per predictor before fitted weights win | variance | ft |
| Heuristics | Gigerenzer & Brighton 2009, *TopiCS* 1:107 | Tallying and take-the-best vs regression, 20 datasets | Heuristics higher on average out of sample; "betting on lower variance, not lower bias" | variance | ft |
| Heuristics, larger test | Şimşek & Buckmann 2015, NIPS 28 | 63 datasets, 50% training | Logistic regression **0.747**, CART 0.746, take-the-best 0.743, tallying **0.725**. Tallying wins only with very few training examples | variance (crossover) | ft |
| Forecasting | Green & Armstrong 2015, *J. Bus. Res.* 68:1678 | 97 comparisons in 32 papers | None favours complexity on balance; complexity raised error **27% on average** over 25 papers. Caveats: "complexity" means hard for decision-makers to understand, not parameter count; ties and wins counted together; assembled by advocates | mixed | ft (abstract) |
| Forecasting | Stock & Watson 2004, *J. Forecast.* 23:405 | Simple mean of forecasts vs estimated weights, 7 countries | The best combinations are the *least* sensitive to recent performance; hard to explain if relationships were stable | variance + instability | cit |
| Regime switching | Bessec & Bouabdallah 2005, *SNDE* 9(2) | Markov-switching vs linear on data generated by a switching model | Gain "never exceeds 12%" and vanishes at long horizons; misclassifying the future regime explains "60% of the total error" | turning points | ft |
| Recessions | An, Jalles & Loungani 2018, *Int. Finance* 21:100 | Consensus forecasts, 63 countries, 1992–2014 | 5 of 153 recessions predicted by April of the preceding year (search summaries) | turning points | cit |
| Competition | M5 (Makridakis, Spiliotis & Assimakopoulos 2022, *IJF* 38:1346) | LightGBM-type ML vs statistical benchmarks, 42,840 hierarchical series | **Complexity won**: winner +22.4% over the best benchmark, every top-50 entry +14%. Credited to learning across 30,490 aligned series and to price/promotion data. At the noisiest level the margin over Croston was only 4.5% | complexity pays | ft |
| Competition | M6 (Makridakis et al. 2025, *IJF* 41:1315; arXiv v1 read) | 163 teams, live stock/ETF forecasting and portfolios | 23.3% beat the "no information" forecast benchmark, 28.8% the equal-weight portfolio, 6.7% both. Forecast accuracy and investment performance uncorrelated (**r = 0.04**). The median team was slightly worse than no information | low-signal limit | ft |
| Evolution, theory | Orr 2000, *Evolution* 54:13 | Fisher's geometric model, n traits | Rate of adaptation "declines at least as fast as n⁻¹" | high-dimensional search geometry | abs |
| Evolution, data | Wagner et al. 2008, *Nature* 452:470 | 102 mouse QTLs, 70 traits | No cost of complexity found: pleiotropy is restricted, and total effect grows with it. Contested by Hermisson & McGregor 2008 | — | cit |
| Biology, cost of regulation | Dekel & Alon 2005, *Nature* 436:588 | Lac-protein expression, cost vs benefit measured | An optimal expression level for each lactose level, reached in a few hundred generations; at low lactose the cost exceeds the benefit (search summary) | overhead vs benefit | cit |
| Products | Thompson, Hamilton & Rust 2005, *JMR* 42:431 | Feature count vs satisfaction | People choose feature-rich products, then like them less after use ("feature fatigue"); effect sizes not retrieved | user burden (separate mechanism) | cit |

**Two cautions on reading the table.**
- **Several "simple wins" compare against an *unregularised* complex model.** Plain least squares, logit or sample mean–variance are the weakest complex benchmarks. Against a regularised one, the simple rule's lead often shrinks to a tie or reverses: Şimşek 2013 found elastic net up to 19% better than plain least squares in some datasets. So the measured tax is partly a tax on *not regularising*.
- **Effect sizes are not comparable across rows.** The metrics differ: correlation, Sharpe, percentage error, hit rates. So do the definitions of "complex": parameter count, number of trials, comprehensibility, frequency of adjustment.

---

## (D) Open — and who frames it as open

1. **Does benign overfitting carry over to low-signal, changing data?**
   - Kelly, Malamud & Zhou 2024 prove that, in their random-feature setting, timing performance can rise with complexity.
   - The critics, mostly working papers:
     - Nagel 2025 (NBER WP 34104), read for key passages;
     - Berk 2023, Buncic 2025, Cartea, Jin & Shi 2025 and Fallahgoul 2025, known only through Nagel's description;
     - they argue that the gain reflects the kernel's built-in recency weighting, not learning.
   - The general theory's conditions are stated by Bartlett et al. 2020 and Hastie et al. 2022: high SNR and a long flat tail of small covariance eigenvalues. Neither condition is typical of return data. **Open in the literature, actively contested.**
2. **How much of the combination puzzle is estimation error, and how much instability?**
   - Smith & Wallis 2009 and Claeskens et al. 2016 explain it by estimating the weights.
   - Stock & Watson 2004 say their results are hard to explain in a stationary world.
   - Timmermann's 2006 survey (not read) is the standard treatment. No source gives a general split. **Open, framed by those authors.**
3. **When simple methods win, is it estimation variance or location shifts?** Clements & Hendry 2001 (*IJF* 17:550; abstract) argue that shifts in means are the main cause of forecast failure, with "non-parsimony" playing only a supporting role. We found no cross-study estimate of how often each mechanism explains a simple-method win.
4. **Is ignoring information ever optimal, or only cheaper?**
   - The ecological-rationality school (Gigerenzer; Katsikopoulos et al. 2021) holds that heuristics are the right tool under uncertainty.
   - Parpart et al. 2018 prove that, at the computational level, a suitable prior always does at least as well.
   - The live question is practical: whether the right prior can be found without enough data, which is where heuristics help. **Open; framed by Parpart et al. and their critics.**
5. **Does a cost of complexity limit real organisms?** It holds in Fisher's model (Orr 2000; Welch & Waxman 2003). Measured pleiotropy says it may not, because effective dimension is low (Wagner et al. 2008), and that measurement is itself disputed (Hermisson & McGregor 2008). **Open in evolutionary genetics.**
6. **How large is the reflexive tax in general?**
   - McLean & Pontiff measure it for published stock predictors (≥ 32 points).
   - Direct evidence for the Lucas critique in macro relations is weak, though the tests have low power: Ericsson & Irons 1995 found "virtually no evidence"; Lindé 2001 on power.
   - **No general law relating decay rate to how widely a model is used was found.** Gap; crowding studies (Khandani & Lo 2011; Lou & Polk; Chordia et al. 2014) were not mapped.
7. **How much of finance's factor research replicates?** Hou, Xue & Zhang 2020 (65% of 452 anomalies fail) and Harvey, Liu & Zhu 2016 differ from Jensen, Kelly & Pedersen 2023 (most replicate). The disagreement is mostly about the statistical model of the trials: independent noise or correlated clusters. **Open, actively debated.**
8. **The few-events corner.** No source was found that studies regime-detecting rules when the record holds only ~5–20 regime episodes. In that corner, estimating the regime parameters, not misclassifying the next regime, may dominate. Bessec & Bouabdallah's long samples put estimation error at only 10–15%. **Gap in our search, not a recognised open problem**; a targeted search is needed before calling it open (§I, S1).

---

## (E) What sets the tax rate: factor by factor

| Factor | What is established | By whom | Rate law (where one exists) |
|---|---|---|---|
| **Data length vs flexibility** | The variance term scales with effective degrees of freedom over *independent* observations. Serial correlation and rare events shrink the effective sample: a crisis model is informed by the number of crises, not the number of days | ESL §7.3; Hastie et al. 2022; DeMiguel et al. 2009; Lo 2002 (serial correlation can overstate annual Sharpe by up to 65%); Dawes 1979 (15–20:1) | σ²p/N in-sample; σ²γ/(1−γ) out of sample. A rate estimated from N events has relative error ≈ 1/√N: ±30% at N = 10 (elementary) |
| **Noise / signal-to-noise** | Lower SNR moves the crossover toward simpler rules; in isotropic models least squares beats predicting zero only for γ < SNR/(SNR+1); overparameterisation helps only at high SNR | Hastie et al. 2022; Gigerenzer & Brighton 2009 ("more noise makes variance more dominant"); M5 (gain 77.9% at the aggregate level, 4.5% at the noisiest) | γ < SNR/(1+SNR) (isotropic least squares) |
| **Number of variants tried** | Selection inflates apparent skill by an extreme-value factor in N; correlated variants count as fewer effective tries; hidden researcher choices count as tries | Bailey et al. 2014; Bailey & López de Prado 2014 (deflated Sharpe ratio); Harvey, Liu & Zhu 2016; Menkveld et al. 2024 | E[max] = 1.57, 2.07, 2.28 SE at N = 10, 30, 50 (bounded by √(2 ln N)); required years < 2 ln N/SR² |
| **Rate of change (non-stationarity)** | Optimal adaptivity rises with drift-to-noise ratio; too adaptive pays noise, too static pays lag. After location shifts, models carrying memory of the old equilibrium fail systematically, and robust devices trade bias for variance | Muth 1960; Widrow et al. 1976; Pesaran & Timmermann 2007; Pesaran, Pick & Pranovich 2013; Clements & Hendry 2001; Hendry 2006; Cederburg et al. 2020 | k ≈ √q, excess ≈ σ²√q; window w* = √(3/q); regret ∝ V_T^(1/3) T^(2/3). Heuristic (unchecked): discrete breaks of rate λ and size δ act like q ≈ λδ²/σ² for a smoothing rule |
| **Cost per adjustment** | Costs scale with turnover; high-turnover signals lose most; the optimal response is inertia | Novy-Marx & Velikov 2016 (anomalies with monthly one-sided turnover > 50% rarely survive); Gârleanu & Pedersen 2013; Barroso & Detzel 2021 | band ∝ ε^(1/3), loss ∝ ε^(2/3) (continuous time) |
| **Asymmetric loss at turning points** | Under asymmetric loss the optimal forecast is biased, with time-varying bias. Regime-aware rules earn their gain only if the *next* regime is called correctly, and turning points are rarely called in advance. Under a random walk, every stop-loss rule lowers expected return | Christoffersen & Diebold 1997; Dacco & Satchell 1999; Bessec & Bouabdallah 2005; An et al. 2018; Kaminski & Lo 2014 | No general law; misclassification ≈ 60% of switching-model error in one Monte Carlo design |
| **Environment reacting to the model** | Published and widely used regularities decay; regulated metrics get managed to | McLean & Pontiff 2016; Haldane & Madouros 2012 (US leverage reversal); Goodhart 1975; Lucas 1976 | Level only (≥ 32% for stock predictors); no rate law found |
| **Size of the true edge** | A small true advantage of the complex rule needs an enormous sample to show | DeMiguel et al. 2009 (3,000 months); Haldane & Madouros (400 years for GARCH); Campbell & Thompson 2008 | Required T scales with (noise/edge)² |
| **Prior structure available** | Known signs, shared structure across series, and good priors shrink the tax. Unit weights need correct signs; cross-learning lets ML win | Dawes 1979; Parpart et al. 2018; M5 2022; Jensen, Kelly & Pedersen 2023 | — |

**The common thread is statistical, and Established:** the complex rule's extra freedom is paid for by its estimation and selection noise. It is worth the price only when the record holds enough independent information about the extra structure. The *amount* of information is set by events, not rows, and by how many variants were tried. Non-stationarity both shortens the useful record and is the reason to adapt at all. That tension is why the best rule is usually intermediate.

---

## (F) Same math, or same mechanism?

The cross-field examples sort into seven mechanisms. In the table, "same math" means a common derivation exists and is cited; "same mechanism" means the causal story is the same but no common equation is written down; "surface analogy" means the shared part is the word.

| Mechanism | Members | Relationship | Cure |
|---|---|---|---|
| **M1. Estimation variance** (finite data, more parameters) | Least squares p/N; 1/N vs mean–variance; the combination puzzle; Dawes's unit weights; take-the-best and tallying; Lien's static hedge; Haldane's GARCH and CAMEL results; M3; Kan & Zhou | **Same math** (bias–variance; shrinkage). Parpart et al. 2018 show the heuristics are the extreme-prior end of Bayesian regression; Tu & Zhou and Ledoit–Wolf are shrinkage in the same sense | Shrink toward the simple rule; more independent data |
| **M2. Selection over many tries** | Backtest overfitting; the deflated Sharpe ratio; the factor zoo; Freedman's paradox; forking paths; Ye's search degrees of freedom; the optimiser's curse; "regressional Goodhart"; McLean & Pontiff's 26% | **Same math** (order statistics of noisy estimates) | Count all tries; hold out data untouched by any choice; deflate; pre-register |
| **M3. Lag vs noise under change** | Muth / exponential smoothing; Kalman; LMS; estimation windows under breaks; Clements & Hendry location shifts; Cederburg's breaks; Besbes regret | **Same math** for the first five (aμ + b/μ-type loss); Clements & Hendry is the same trade-off in reverse (robustness buys bias reduction with variance) | Tune adaptivity to the measured change rate; pool windows; combine recursive and rolling estimates |
| **M4. Cost per adjustment** | Turnover drag; no-trade bands; Kirby & Ostdiek; Barroso & Detzel; Dekel & Alon's expression cost; Kussell & Leibler's sensing cost | **Same mechanism** (fixed or proportional overhead against the benefit of responding). Same math within finance (singular control); the biology cases share the structure but not the equations | Bands of inaction; trade partially; respond only when the benefit clears the cost |
| **M5. Turning-point asymmetry and misclassification** | Dacco & Satchell; Bessec & Bouabdallah; recession forecasting; stop-loss and re-entry (Kaminski & Lo); trend-following whipsaw | **Same mechanism**; Bessec & Bouabdallah give a decomposition within one model class | Value a switch by its error rates at the turns, not on average; prefer rules that are wrong cheaply |
| **M6. Fragility to the unanticipated** | HOT (Carlson & Doyle); the Bode integral; Chandra's glycolysis; Rohrs-type adaptive-control instability; Perrow's normal accidents; Manheim & Garrabrant's "extremal Goodhart" | **Same math only for Bode ↔ Chandra** (linear feedback). HOT is a model class whose heavy tails depend on a risk-neutral objective (Newman, Girvan & Farmer 2002). Rohrs is a specific adaptive-control failure. Perrow is qualitative. Note that extremal Goodhart can punish an *over-simple* model | Risk-averse objectives; robustness margins; leakage/dead zones in adaptation |
| **M7. The environment reacts** | Goodhart; Lucas; Campbell; McLean & Pontiff's 32%; Haldane's US leverage reversal; crowding (Khandani & Lo) | **Same mechanism**, no shared equation | Assume decay; prefer signals with economic reasons to persist; monitor live against backtest |
| **Surface analogy** | Gall's law; Brooks's second-system effect; feature creep; Tainter's declining returns; Kitano's "conservation of robustness" outside linear feedback; Orr's 1/n ↔ LMS's n-scaling | Named heuristics and historical theses: cite as such. Thompson et al. 2005 is measured but concerns user burden, not prediction. The Orr ↔ LMS parallel (both slow down as noise or steps spread over n dimensions) is **Speculative** until a common derivation is written | — |

**Vocabulary warning (precedent: `vocabulary-stacking-analogy`).** "Complexity" names at least six different objects here:
- parameter count;
- effective degrees of freedom;
- number of variants tried;
- frequency of adjustment;
- design elaboration;
- comprehensibility to a decision-maker (Green & Armstrong's definition, which excludes parameter count).

A claim that "complexity costs X" must say which one. The statement "all of these are one complexity-tax law" is **not supported** by anything found: only M1–M3 share mathematics, and even there the variable being charged differs.

---

## (G) What the wiki holds, and its gaps

### G.1 Holdings (read-only query, 2026-10-19)
- **IT09** (sloppy models; Machta et al. 2013) and **M6** (Fisher information rank). These are the QR-001 side of the coin: parameter combinations the data cannot pin down are the ones whose estimation is pure variance cost.
- **INFO2** (source coding) and **INFO5** (Kolmogorov complexity) sit next to MDL, but no model-selection entry draws the link.
- **F1, Ashby's law of requisite variety.** This is the wiki's one entry on the *other* side: a regulator needs at least as much variety as the disturbances it must absorb. It sets a *floor* on controller complexity. It is the natural counterweight to QR-009, and the map should be read with it: the tax applies to complexity beyond what the environment's variety requires, estimated from limited data.
- **EWS4** (error rates and false alarms of warning indicators) and **EWS8** (multivariate indicator benchmark), plus the **QR-006b** result. In that pre-registered benchmark the simple indicators won and the information indicators that came close were near-copies of them. This is the wiki's own measured instance of M1/M2.
- **H1** (regime) and **M2** (OccBin regime switching) are regime machinery, with no entry on how regime-switching models forecast out of sample.
- **X8** (financial entropy-production proxy, AlphaEntropy-derived). Its three-archetype crisis model was already falsified on clustering a handful of episodes.
- **P18, P19, P20** (AlphaEntropy-derived, Supported as single-domain observations since M0). See G.3.

### G.2 Gaps
The wiki has no reference entry for any of:
- bias–variance;
- AIC/BIC/MDL model selection;
- effective degrees of freedom;
- multiple testing and backtest overfitting;
- estimation error in portfolios and 1/N;
- out-of-sample failure of return predictors and publication decay;
- forecast combination and the M-competitions;
- forecasting under breaks and the tracking–noise trade-off;
- improper linear models and heuristics;
- Goodhart, Lucas and Campbell, and the optimiser's curse;
- HOT and the Bode integral;
- adaptive-control robustness;
- the cost of complexity in evolution.

QR-009 sits on an almost empty patch of the map. Per the log's rules, that means grounding (Mode A) before any exploration.

### G.3 Wiki items this map bears on (flagged for owner review; nothing changed)
1. **P19's "validated" fix is a Calmar gain of 0.532 → 0.538 (+0.006).** The AlphaEntropy review records a +0.02 Calmar adoption threshold and repeat-run noise larger than several adopted gains. On those facts the fix is within noise. This is mechanism M2 (Menkveld et al. 2024; Bailey et al. 2014). P19's label rests on more than the fix, so no label change is proposed. The word "validated" overstates it.
2. **P20's formula conflicts with a textbook identity.** P20 states E_combined = E_best·(1 + ρn), so that at ρ ≥ 0.7 any combination of two or more signals is worse than the best one alone.
   - For n signals of *equal* error variance σ² and pairwise error correlation ρ, the equal-weight average has error variance σ²[ρ + (1−ρ)/n] ≤ σ². That is never worse than one signal, for any ρ (an identity; Bates & Granger 1969 for the two-forecast case).
   - P20's form also predicts **no** gain from combining *independent* signals (ρ = 0), contradicting the same identity.
   - "Combined worse than best" does happen, but through unequal signal quality, estimated weights (Smith & Wallis 2009; Claeskens et al. 2016) or post-hoc selection of which signals to add. Those are M1/M2 mechanisms, not a correlation law.
   - P20 is labelled an empirical fit to 19 variants with ρ "estimated qualitatively". The map suggests a reading against the combination literature (§I, S7). This is a Mode A check, not a research question.
3. **P18 and X8 rest on few independent episodes** (four D_eff troughs; a handful of crises). Per §E, the effective sample is the event count. Nothing is proposed beyond noting it.

### G.4 The AlphaEntropy case: facts from the project records (added 2026-10-19)
*Source: AlphaEntropy project records (owner's private repo), via main session 2026-10-19. Reading marker: main-session check of project files; not a publication; not read by this session.*

1. **The deflated Sharpe ratio test** (Bailey & López de Prado 2014; §B3).
   - V28.8c validation battery, 2026-05-04: DSR = 0.0 ("plausibly random given # tested", N = 9).
   - The JSON value was later hand-edited to 0.948 and recorded as "borderline-strong".
   - A 2026-10-18 audit found the test mis-specified: run on a local simulation rather than the QuantConnect backtest, with N = 9 when about 66 Sharpe values were on file.
   - Recomputed on the real curves: DSR ≈ 1.00 for N up to 200, so "Sharpe > 0" survives multiple testing. "Beats a 0.55-Sharpe passive alternative" holds only at about 84%.
2. **The factor-zoo novelty claim** (Harvey, Liu & Zhu 2016; Zakamulin 2017).
   - An archived note claimed the "profitability durability" composite matched none of "319+ documented" factors.
   - The traded signal uses only about 3 months of fundamentals, so it is mostly profitability level.
   - Regressed on FF5 + momentum + QMJ + BAB: alpha ≈ 4.5%/yr (t ≈ 4.3, an in-sample backtest statistic). The structure is close to RMW + size + momentum.
   - The novelty claim was a framing error, tag `found-under-other-vocabulary`.
3. **Reading.**
   - The core system (quality sleeve, trend sleeve, near-static hedge) survives a proper correction for the number of tries.
   - The added dynamic layers do not: their increments were below repeat-run noise, and the ablation preferred them off.
   - **The tax fell on the increments, not on the whole system.** This matches mechanisms M1, M2 and M5. It is consistent with §E, and it is the pattern the literature predicts for durable known effects plus tuning on few events. **Supported** as a reading of project records; not independently checked here.
4. **Process lesson** (neutral: the files do not show who made the edit). A failed test was recorded as a pass and caught later by audit. That supports pre-registration, results logs that cannot be edited afterwards, and re-running validations on the production record. QR-006b's commit-ordered, pre-registered design is the wiki's own precedent.

---

## (H) Candidate fold-in reference entries (owner decides; nothing written)

| # | Proposed entry | Core sources | Would ground / correct |
|---|---|---|---|
| R1 | Bias–variance decomposition and the per-parameter variance cost | ESL §7.3; Geman et al. 1992; Hastie et al. 2022 | QR-009; IT09 link |
| R2 | Model-selection penalties (AIC, BIC, MDL, cross-validation) and their assumptions | Akaike 1974; Schwarz 1978; Rissanen 1978; Stone 1974; ESL §7.4–7.9 | INFO2/INFO5 link to MDL |
| R3 | Effective degrees of freedom and the hidden cost of model search | Efron 2004; Ye 1998; Freedman 1983; Wang, Zhao & Fan 2024 | — |
| R4 | Selection under many trials: backtest overfitting, the deflated Sharpe ratio, the optimiser's curse | Bailey et al. 2014, 2016/17; Bailey & López de Prado 2014; Harvey, Liu & Zhu 2016; Smith & Winkler 2006; Menkveld et al. 2024 | P19 (fix within noise) |
| R5 | Double descent and benign overfitting, with conditions | Belkin et al. 2019; Hastie et al. 2022; Bartlett et al. 2020; Nakkiran et al. 2021 (both); KMZ 2024 vs Nagel 2025 as a contested application | — |
| R6 | Estimation error in portfolio choice; 1/N and its rebuttals | DeMiguel et al. 2009; Kan & Zhou 2007; Kirby & Ostdiek 2012; Tu & Zhou 2011; Jagannathan & Ma 2003; Ledoit & Wolf 2004; Zakamulin 2017 | — |
| R7 | Out-of-sample failure of return predictors and post-publication decay | Welch & Goyal 2008; Campbell & Thompson 2008; Rapach et al. 2010; Goyal, Welch & Zafirov 2024; McLean & Pontiff 2016 | — |
| R8 | The forecast-combination puzzle and the M-competitions | Bates & Granger 1969; Clemen 1989; Stock & Watson 2004; Smith & Wallis 2009; Claeskens et al. 2016; M3, M4, M5, M6 papers | P20 |
| R9 | Adapting under change: the tracking–noise trade-off and forecasting under breaks | Muth 1960; Widrow et al. 1976; Pesaran & Timmermann 2007; Pesaran, Pick & Pranovich 2013; Clements & Hendry 2001; Hendry 2006; Besbes, Gur & Zeevi 2015 | — |
| R10 | Why regime-switching rules disappoint out of sample | Dacco & Satchell 1999; Bessec & Bouabdallah 2005; An et al. 2018; Kaminski & Lo 2014 | H1, M2 (OccBin) |
| R11 | Improper linear models and fast-and-frugal heuristics, read as regularisation | Dawes 1979; Gigerenzer & Brighton 2009; Parpart et al. 2018; Şimşek & Buckmann 2015; Haldane & Madouros 2012; Aikman et al. 2021 | — |
| R12 | Goodhart, Lucas and Campbell: when the environment reacts | Goodhart 1975; Strathern 1997; Lucas 1976; Campbell 1979; Manheim & Garrabrant 2018; McLean & Pontiff 2016; Ericsson & Irons 1995 | — |
| R13 | Robust yet fragile, and hard limits on feedback | Carlson & Doyle 1999, 2002; Newman, Girvan & Farmer 2002; Bode 1945; Freudenberg & Looze 1985; Chandra et al. 2011; Rohrs et al. 1985 | F1 (Ashby) cross-link |
| R14 | The cost of complexity in adaptation, and when sensing pays | Orr 2000; Welch & Waxman 2003; Wagner et al. 2008; Hermisson & McGregor 2008; Kussell & Leibler 2005; Dekel & Alon 2005 | — |

**R1, R3, R4 and R9 are the priority.** They are the three mechanisms with shared mathematics (M1–M3). Together they would let the wiki state QR-009 in its own terms. Each new entry needs an anchor at creation.

---

## (I) Candidate sub-questions, and what would decide each

| # | Sub-question | Deciding data | Disposition (suggested; no gate run) |
|---|---|---|---|
| S1 | **The in-house tax-rate simulation:** out-of-sample loss of an adaptive rule against a static one, as a function of record length (events), flexibility and regime-change rate | See below | **Mostly answered**; main form FOLD (`found-under-other-vocabulary`); one narrow corner worth a targeted prior-art search |
| S2 | Is "complexity" one quantity with one tax across fields? | The mechanism table, §F | **Answered: no.** RE-SCOPE any cross-field claim to a named mechanism. Re-asking it would be `ill-posed` |
| S3 | Is overfitting merely useless or actively harmful out of sample? | Memory in the data-generating process | **Answered** for backtests: harmful under compensation effects or mean reversion (Bailey et al. 2014 §6) |
| S4 | How fast does a published or widely used rule decay with adoption? | Anomaly-level decay against crowding or assets under management | **Not mapped.** McLean & Pontiff give a level, not a rate; crowding literature not read. Open or answered unknown |
| S5 | Are bacterial bet-hedging (switch vs sense) and Muth-type tracking the same mathematics? | A common derivation | **Likely answered elsewhere**: the link between growth rate and information about a fluctuating environment is Kussell & Leibler's own result, in the Kelly-betting tradition. Not mapped; a prior-art gate would probably return `answered` |
| S6 | In the combination puzzle, how much is estimation error and how much instability? | Monte Carlo plus empirical decompositions | **Open in the literature** (Stock & Watson 2004; Claeskens et al. 2016). Not a natural in-house target |
| S7 | Does P20's error formula survive comparison with the combination literature? | P20's 19-variant data and the identity in §G.3 | **Mode A bookkeeping**, an hour's work; no gate needed |
| S8 | Is there literature on regime models fitted to very few episodes? | Targeted search: bear-market dating (Pagan & Sossounov 2003; Lunde & Timmermann 2004), small-sample Markov-switching estimation | **Mode A search**, needed before S1's corner can be called open |

**S1 in detail.** The proposal is pre-registerable and laptop-sized. Most of it is already answered:
- **Continuous drift, smoothing rule.** The answer is closed form (§B5). The loss is σ²/w + q·σ²·w/3 for a window, or excess ≈ σ²√q for the optimal exponential smoother. A simulation would reproduce Muth 1960 and Pesaran & Timmermann 2007: a **RESTATEMENT**.
- **Discrete regime switches, detect-and-switch rule.** Answered by theory and Monte Carlo. Even when the data really switch, the gain is ≤ 12% and dominated by misclassification (Dacco & Satchell 1999; Bessec & Bouabdallah 2005). A RESTATEMENT.
- **Worst case over change budgets.** Answered exactly (Besbes et al.).
- **Costs per switch.** Answered in continuous time (no-trade bands).
- **Many variants tried.** Answered (Bailey et al. 2014).

**What may remain** (Speculative, each needing the S8 search first):
- the few-events corner, about 5–20 regime episodes, where estimating the regime parameters may dominate;
- the joint objective: detect-and-switch, asymmetric drawdown loss, per-switch cost and a search over N variants in one setting.

**Gate-2 triviality check:** the components predict the qualitative answer. The cost band widens inaction, asymmetric loss biases the static rule toward caution, misclassification caps the gain, and selection inflates the backtest. So the information gained from simulating it is probably small.

**Suggested handling:**
- Gate 1 on the main form would likely return `answered` → **FOLD** (via R9 and R10).
- The few-events corner could be gated separately as `narrow-angle-provisional` at best, after S8.
- If the owner wants the simulation as a *personal calibration tool* (how big is the tax for my record length?), that is a reasonable use. It is not a research result. It should benchmark against the strong middle options:
  - optimal exponential smoothing;
  - pooled windows;
  - James–Stein shrinkage;
  - the recursive–rolling combination (Clark & McCracken 2009);
  - not only a fully static rule.

**Overall.** QR-009 as worded looks headed for Gate 1 `answered` in its general form. The answer is framed by bias–variance theory, Bailey et al. 2014, Muth 1960 / Pesaran & Timmermann 2007, and Clements & Hendry. Its "what sets the rate" half is answered factor by factor (§E). There are recognised open edges, D1, D2, D4, D5 and D7, but none is decidable in-house. The wiki's main job here is Mode A: ground the mechanisms (R1, R3, R4, R9) and use them to audit its own AlphaEntropy-derived claims (§G.3).

**Drift note.** A tempting move is to treat the complexity tax as a universal law with a single "rate", perhaps expressed through effective dimension or Fisher rank, to connect it with D_eff and QR-001. The map does not support that. The rates differ by mechanism. The QR-001 link is real but specific: sloppy directions are where estimation variance is paid (M1). It does not cover selection (M2), change (M3), costs (M4), turning points (M5), fragility (M6) or reflexivity (M7). A cross-field claim that forbids nothing ("complexity always costs something") is decorative.

---

## (J) Sources and reading markers

**Sub-agent markers:**
- **ft** — full text, or the named sections, read by text extraction;
- **ft-ss** — full text read through an automated summariser;
- **abs** — abstract only;
- **ss** — search summary only;
- **meta** — bibliographic record only, content from background knowledge (must be verified before quoting);
- **nr** — not retrieved.

**MS** = what the main session checked itself:
- **cit** — DOI, authors, title, venue and pages confirmed through Crossref;
- **abs** — abstract read (Crossref, Europe PMC, IDEAS, or the PDF's abstract page);
- **ft** — the cited passage or number found in the primary text by PDF extraction;
- **num** — formula checked numerically;
- **ss** — search summary only.

Nothing below is upgraded.

### Statistics and machine learning
| Source | Sub-agent | MS |
|---|---|---|
| Hastie, Tibshirani & Friedman, *Elements of Statistical Learning*, 2nd ed. (2009), §3.4, §7.3–7.9 | ft | — |
| Geman, Bienenstock & Doursat 1992, *Neural Comput.* 4:1, doi:10.1162/neco.1992.4.1.1 | meta | cit |
| Hastie, Montanari, Rosset & Tibshirani 2022, *Ann. Statist.* 50:949, doi:10.1214/21-AOS2133 | ft (§1–2) | cit |
| Akaike 1974, *IEEE TAC* 19:716; Schwarz 1978, *Ann. Statist.* 6:461; Rissanen 1978, *Automatica* 14:465; Stone 1974, *JRSS-B* 36:111 | meta | — |
| Efron 1986, *JASA* 81:461; Efron 2004, *JASA* 99:619 | meta | — |
| Ye 1998, *JASA* 93:120, doi:10.1080/01621459.1998.10474094 (the often-cited …10473769 is a different paper) | meta | cit |
| Wang, Zhao & Fan 2024, *JCGS*, doi:10.1080/10618600.2024.2388545 | ft (Table 3) | — |
| Freedman 1983, *Am. Stat.* 37:152, doi:10.1080/00031305.1983.10482729; Ding 2024, arXiv:2401.00649 ch. 13 | meta; ft (Ding) | cit (Freedman) |
| Simmons, Nelson & Simonsohn 2011, *Psychol. Sci.* 22:1359; Gelman & Loken 2014, *Am. Sci.* 102:460 | ss; meta | — |
| Belkin, Hsu, Ma & Mandal 2019, *PNAS* 116:15849, doi:10.1073/pnas.1903070116 | ft | cit, ft (abstract) |
| Bartlett, Long, Lugosi & Tsigler 2020, *PNAS* 117:30063 | ft (Defs, Thms 4, 6) | cit |
| Nakkiran et al. 2021, *J. Stat. Mech.* 124003 (deep double descent); Nakkiran, Venkat, Kakade & Ma, ICLR 2021 (optimal regularisation) | ft (§1–2); ft (§1) | cit (first) |
| Zhang et al. 2017, ICLR / *CACM* 64:107 | ft (§1) | — |
| Recht et al. 2019; Taori et al. 2020; Miller et al. 2021 (distribution shift) | abs | — |

### Finance
| Source | Sub-agent | MS |
|---|---|---|
| DeMiguel, Garlappi & Uppal 2009, *RFS* 22:1915, doi:10.1093/rfs/hhm075 | abs | cit, abs (via IDEAS fetch, paraphrase) |
| Kirby & Ostdiek 2012, *JFQA* 47:437, doi:10.1017/S0022109012000117 | abs | cit, abs |
| Tu & Zhou 2011, *JFE* 99:204; Kan & Zhou 2007, *JFQA* 42:621 | abs | cit |
| Kritzman, Page & Turkington 2010, *FAJ* 66(2):31 | ss | cit |
| Zakamulin 2017, *Finance Res. Lett.* 22:122, **doi:10.1016/j.frl.2016.12.007** | abs (DOI unverified) | cit (DOI found by main session) |
| Michaud 1989, *FAJ* 45(1):31; Jagannathan & Ma 2003, *JF* 58:1651 | ss | cit |
| Chopra & Ziemba 1993, *JPM* 19(2):6 (the "means ≈ 10× variances" ratio unverified and contested) | ss | — |
| Ledoit & Wolf 2003, *J. Emp. Fin.* 10:603; 2004, *JPM* 30(4):110 | ss | — |
| Novy-Marx & Velikov 2016, *RFS* 29:104 | abs | cit |
| Gârleanu & Pedersen 2013, *JF* 68:2309 | abs | cit |
| Frazzini, Israel & Moskowitz 2018, SSRN 3229719 (AQR-affiliated authors, proprietary data) | abs | — |
| Moreira & Muir 2017, *JF* 72:1611 | abs | cit |
| Cederburg, O'Doherty, Wang & Yan 2020, *JFE* 138:95 | ft | cit, ft (45/103, 31/103, 77/103, structural breaks) |
| Liu, Tang & Zhou 2019, *JPM* 46(1):38; Barroso & Detzel 2021, *JFE* 140:744; Barroso & Santa-Clara 2015, *JFE* 116:111 | ss | — |
| Lien 2005, *J. Futures Mkts* 25:1121 | ss | ss (abstract via IDEAS search summary) |
| Kaminski & Lo 2014, *J. Fin. Mkts* 18:234 | abs | cit |
| Welch & Goyal 2008, *RFS* 21:1455 | ss | cit, abs (IDEAS) |
| Campbell & Thompson 2008, *RFS* 21:1509 | ft (WP §2) | cit, ft (abstract) |
| Rapach, Strauss & Zhou 2010, *RFS* 23:821; Goyal, Welch & Zafirov 2024, *RFS* 37:3490 | abs | cit |
| Asness, Ilmanen & Maloney 2017, *J. Invest. Mgmt* 15(3) | ss | — |
| Bailey, Borwein, López de Prado & Zhu 2014, *Notices AMS* 61:458, doi:10.1090/noti1105 | ft (preprint §2–6) | cit, ft (45 configurations) |
| Bailey, Borwein, López de Prado & Zhu, "The probability of backtest overfitting", *J. Comput. Finance*, doi:10.21314/JCF.2016.322 (Crossref: 2016 online; vol. 20(4) per sub-agent, unverified) | ft (preprint) | cit |
| Bailey & López de Prado 2014, *JPM* 40(5):94 (deflated Sharpe ratio; typeset formula not verified) | ft (preprint, maths garbled) | cit |
| Harvey, Liu & Zhu 2016, *RFS* 29:5 | ft (WP) | cit, ft (t > 3.0) |
| Harvey & Liu 2015, "Backtesting", *JPM* (volume 41 vs 42 unresolved) | ft | — |
| Hou, Xue & Zhang 2020, *RFS* 33:2019; Jensen, Kelly & Pedersen 2023, *JF* 78:2465 | abs | cit |
| McLean & Pontiff 2016, *JF* 71:5 | ft (abstract, intro) | cit, ft (26% / 58% / 32%) |
| Kelly, Malamud & Zhou 2024, *JF* 79:459 | ft (intro) | cit, abs, ft (14 of 15) |
| Nagel 2025, "Seemingly virtuous complexity in return prediction", NBER WP 34104 | ft (key sections) | ft ("mislearns"; 0.017 annualised) |
| Berk 2023; Buncic 2025; Kelly & Malamud 2025; Cartea, Jin & Shi 2025; Fallahgoul 2025 | secondary (via Nagel) | — |
| Gu, Kelly & Xiu 2020, *RFS* 33:2223 | ft (WP intro) | cit |
| Menkveld et al. 2024, *JF* 79:2339 | ft (intro) | cit |
| Lo 2002, *FAJ* 58(4):36 | abs | cit |
| Greenwood, Shleifer & You 2019, *JFE* 131:20 | ss | — |

### Forecasting
| Source | Sub-agent | MS |
|---|---|---|
| Bates & Granger 1969, *Oper. Res. Q.* 20:451 | nr | cit |
| Clemen 1989, *IJF* 5:559 | secondary | cit |
| Stock & Watson 2004, *J. Forecast.* 23:405 | ss | cit |
| Smith & Wallis 2009, *Oxf. Bull. Econ. Stat.* 71:331 | ss | cit |
| Claeskens, Magnus, Vasnev & Wang 2016, *IJF* 32:754 | abs | cit |
| Timmermann 2006, *Handbook of Economic Forecasting* vol. 1 ch. 4 | meta | — |
| Makridakis & Hibon 2000, *IJF* 16:451 (M3) | nr (paraphrase via Clements & Hendry) | cit |
| Hyndman & Billah 2003, *IJF* 19:287 (Theta ≈ SES with drift) | ss | — |
| Makridakis, Spiliotis & Assimakopoulos 2018, *IJF* 34:802; 2020, *IJF* 36:54 (M4) | ss; abs | cit |
| Makridakis, Spiliotis & Assimakopoulos 2022, *IJF* 38:1346 (M5; 2020 preprint read) | ft | cit, ft (22.4%) |
| Makridakis et al. 2025, *IJF* 41:1315 (M6; arXiv:2310.13357 v1 read) | ft | cit, ft (r = 0.04; 23.3/28.8/6.7%) |
| Green & Armstrong 2015, *J. Bus. Res.* 68:1678 | ft (WP v224) | cit, ft (abstract) |
| Clements & Hendry 2001, *IJF* 17:550 | abs | — |
| Hendry 2006, *J. Econometrics* 135:399 | ss | cit |
| Pesaran & Timmermann 2007, *J. Econometrics* 137:134 | ft (WP abstract, §1) | cit |
| Pesaran, Pick & Pranovich 2013, *J. Econometrics* 177:134 | abs | cit |
| Muth 1960, *JASA* 55:299 | meta + ss | cit, num (closed form) |
| Widrow, McCool, Larimore & Johnson 1976, *Proc. IEEE* 64:1151 | abs (OCR snippet) | cit |
| Dacco & Satchell 1999, *J. Forecast.* 18:1 | abs | cit |
| Bessec & Bouabdallah 2005, *SNDE* 9(2), doi:10.2202/1558-3708.1171 | ft (WP) | cit, ft (12%; 60%) |
| Clark & McCracken 2009, *Int. Econ. Rev.* 50:363; Inoue, Jin & Rossi 2017; Rossi 2013; Giacomini & White 2006 | meta | — |
| Besbes, Gur & Zeevi, arXiv:1405.3316; 2015, *Oper. Res.* 63:1227 | ft (Thms 1–2); abs | cit, abs ("price of non-stationarity") |
| Christoffersen & Diebold 1997, *Econometric Theory* 13:808 | abs | — |
| An, Jalles & Loungani 2018, *Int. Finance* 21:100 | abs + ss | cit |
| Constantinides 1986, *JPE* 94:842; Davis & Norman 1990; Shreve & Soner 1994; Rogers 2004; Janeček & Shreve 2004; Dixit 1991 | meta / ss | cit (Constantinides) |
| Stein 1956; Efron & Morris 1977 | meta | — |
| Hurst, Ooi & Pedersen 2017, *JPM* 44(1):15 | meta | — |

### Decision science, regulation, reflexivity
| Source | Sub-agent | MS |
|---|---|---|
| Dawes 1979, *Am. Psychol.* 34:571 | ft | cit, ft (.48/.38/.19; Table 1; 15–20:1) |
| Einhorn & Hogarth 1975; Wainer 1976 (k/96 bound unverified); Meehl 1954 | ss / secondary | — |
| Gigerenzer & Brighton 2009, *TopiCS* 1:107 | ft | cit, ft ("lower variance, not lower bias") |
| Brighton & Gigerenzer 2012, ch. 2 in *Ecological Rationality* (OUP); 2015, *J. Bus. Res.* 68:1772 | abs | cit (2015) |
| Parpart, Jones & Love 2018, *Cogn. Psychol.* 102:127 | abs | cit, abs (Europe PMC) |
| Şimşek 2013, NIPS 26; Şimşek & Buckmann 2015, NIPS 28 | ft | ft (2015: 0.747 … 0.725) |
| Hilbig 2010, *PB&R* 17:923; Hilbig & Richter 2011, *TopiCS* 3:187; Newell 2005; Chater et al. 2003 | meta / abs | — |
| Katsikopoulos, Şimşek, Buckmann & Gigerenzer 2021, *Classification in the Wild* (MIT Press) | publisher description | — |
| Grove et al. 2000, *Psychol. Assess.* 12:19 | abs | cit |
| Kahneman, Sibony & Sunstein 2021, *Noise* | ss (cite the book directly, never the summaries) | — |
| Haldane & Madouros 2012, "The dog and the frisbee", BIS speech, 31 Aug 2012 (Basel I had five risk weights, not seven; parameter counts "thousands, perhaps tens of thousands" up to "several millions") | ft | ft (1.2 pp; 10×; CAMEL vs constant; 400 years; "trumps the truth") |
| Aikman et al. 2021, *Ind. Corp. Change* 30:317, doi:10.1093/icc/dtaa024 (BoE FSP 28, 2014; **not** *Nature Human Behaviour*) | ft (FSP 28) | cit, ft ("perform comparably") |
| Goodhart 1975; Campbell 1979; Soros 1987 | ss | — |
| Strathern 1997, *Eur. Rev.* 5:305 | ft (passage) | — |
| Lucas 1976, *Carnegie-Rochester* 1:19 | meta | cit |
| Ericsson & Irons 1995, FRB IFDP 506; Lindé 2001 | abs | — |
| Manheim & Garrabrant 2018, arXiv:1803.04585 | ft | — |
| Smith & Winkler 2006, *Mgmt Sci.* 52:311 (erratum affects Fig. 3 only) | ft | cit, ft (0.85/1.03/1.54) |
| Lo 2004, *JPM* 30(5):15; Khandani & Lo 2011, *J. Fin. Mkts* 14:1 | abs | — |

### Engineering, control, biology
| Source | Sub-agent | MS |
|---|---|---|
| Carlson & Doyle 1999, *PRE* 60:1412; Doyle & Carlson 2000, *PRL* 84:5656 | meta | — |
| Carlson & Doyle 2002, *PNAS* 99 suppl. 1:2538 ("robustness is conserved" is **not** in this paper) | ft-ss | cit, abs |
| Csete & Doyle 2002, *Science* 295:1664; Doyle et al. 2005, *PNAS* 102:14497 | meta | — |
| Newman, Girvan & Farmer 2002, *PRL* 89:028301 | abs | cit |
| Bode 1940, *BSTJ* 19:421; Bode 1945 (book); Freudenberg & Looze 1985, *IEEE TAC* 30:555; Stein 2003, *IEEE CSM* 23(4):12; Seron, Braslavsky & Goodwin 1997 | meta | — |
| Chandra, Buzi & Doyle 2011, *Science* 333:187 | ft | cit, ft ("cannot uniformly improve it") |
| Rohrs, Valavani, Athans & Stein 1985, *IEEE TAC* 30:881 | meta (content from standard accounts, not read) | cit |
| Ioannou & Kokotović 1984, *Automatica* 20:583; Anderson 1985, *Automatica* 21:247; Egardt 1979; Narendra & Annaswamy 1987 | meta | cit (Ioannou & Kokotović) |
| Gall 1975/1977 *Systemantics*; Brooks 1975 *The Mythical Man-Month* ch. 5; Tainter 1988; Perrow 1984/1999; Sculley et al. 2015 | ss / meta (heuristics; cite as such) | — |
| Thompson, Hamilton & Rust 2005, *JMR* 42:431 | meta | cit |
| Orr 2000, *Evolution* 54:13 | abs | cit, abs (Europe PMC) |
| Welch & Waxman 2003, *Evolution* 57:1723; Martin & Lenormand 2006, *Evolution* 60:893 | ss / meta | — |
| Wagner et al. 2008, *Nature* 452:470; Hermisson & McGregor 2008, *Nature* 456:E3 | abs / ss | cit (Wagner) |
| Kitano 2004, *Nat. Rev. Genet.* 5:826; Kitano 2007, *Mol. Syst. Biol.* 3:137 | meta | cit (2004) |
| Dekel & Alon 2005, *Nature* 436:588 | abs | cit |
| Kussell & Leibler 2005, *Science* 309:2075 (exact sensing-vs-switching inequality unverified) | abs | cit, abs |

### Case study
| Source | Sub-agent | MS |
|---|---|---|
| AlphaEntropy project records (owner's private repo): V28.8c DSR battery 2026-05-04; 2026-10-18 audit; archived factor note (§G.4) | — | not read by this session; facts relayed by the main session, which checked the project files (not a publication) |

### Phrase provenance
| Source | Sub-agent | MS |
|---|---|---|
| Google Books Ngram, "complexity tax" / "cost of complexity" / "complexity penalty", 1900–2022 | ft (data) | — |
| Wilson & Perumal 2009, *Waging War on Complexity Costs* (uses "complexity costs") | ss | — |
| Informal "complexity tax" uses (DevOps, software, supply-chain blogs) | ss | — |

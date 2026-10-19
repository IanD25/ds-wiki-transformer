# The complexity tax: when does a smarter model do worse? A primer (QR-009, 2026-10-19)

> **What this is.** A companion to the literature map [`prior_art_reviews/QR-009_COMPLEXITY_TAX_MAP_2026_10_19.md`](../prior_art_reviews/QR-009_COMPLEXITY_TAX_MAP_2026_10_19.md), written for the owner. It runs in layers: (a) the core idea, (b) the named versions across fields, (c) what sets the "tax rate", (d) when complexity wins, (e) how the AlphaEntropy experience fits, and (f) a reading list.
>
> **Citations** point to the map, whose sources table (§J) records how each source was read. Numbers marked ✓ were checked by the main session in the primary text. Confidence tags: **Established / Supported / Speculative**. Nothing here is new research, and nothing here is investment advice.
>
> **On the name.** "Complexity tax" is your phrase. No field uses it as a technical term; the map found only informal blog and management usage. The closest technical terms are the statistician's *complexity penalty*, the evolutionary biologist's *cost of complexity* and the operations researcher's *price of non-stationarity*. It is a good name for a podcast, as long as the episode says what it stands for.

---

## (a) The core idea, with one everyday example

**Any rule you fit to the past learns two things at once: the pattern, and the noise.** Giving the rule more freedom lets it learn more of both. On the data it was fitted to, both look like skill. On new data, only the pattern pays; the noise it learned is now a cost. That cost is the tax. **Established.**

**Example: when to leave for work.** Your commute takes 30 minutes on average, but it varies.
- **Rule A, static:** leave at the same time every day, set by your average commute.
- **Rule B, fully adaptive:** each evening, look at today's journey and shift tomorrow's departure by the full amount you were early or late.
- **Rule C, partly adaptive:** shift tomorrow's departure by a fraction, say a fifth, of today's surprise.

Which wins depends on what the day-to-day variation *is*.
- **Mostly random** (a slow lorry today, nothing tomorrow): Rule B chases yesterday's noise and is wrong more often than Rule A.
- **Mostly persistent** (roadworks that last six weeks): Rule A keeps being late for six weeks and Rule B wins.
- **A mix, as in real life:** Rule C beats both. The best fraction has a formula. It is roughly the square root of how much of the variation persists from day to day, relative to how much is random (Muth 1960; map §B5). **Established.**

Now add the complications that real decisions have, and each one raises or lowers the tax:
- **How long you have been watching.** After a week you cannot tell roadworks from bad luck; after a year you can.
- **How many rules you tried.** If you tested twenty departure rules on last month's data and kept the best, its record flatters it.
- **What being wrong costs, and whether it is symmetric.** Ten minutes early is fine; ten minutes late loses the meeting.
- **Whether changing costs anything.** Re-planning every morning is a hassle.
- **Whether the world reacts.** If everyone in your street adopts Rule B, the shortcut jams.

These five, plus noise, are the whole subject in miniature.

---

## (b) The main named versions across fields

Each field found the same experience on its own and named it differently. Each item below gives the field's name, the most striking concrete result, and the honest caveat.

### 1. Statistics: overfitting and the bias–variance trade-off
- **Idea.** Error = bias (the model is too rigid) + variance (the model chases noise) + irreducible noise. Each extra fitted parameter adds a variance cost. For least squares, it is the noise variance divided by the sample size, *every time*, whether or not the parameter is useful. **Established.**
- **Striking result: Freedman's paradox (1983).**
  - Take 100 observations of pure noise and "explain" them with 50 columns of pure noise. On average the regression explains about half the variation (R² ≈ 0.5).
  - Throw out the weakest predictors and refit, and the result still looks significant.
  - Numbers from a textbook replication (Ding 2024); Freedman's paper itself was not read.
- **Caveat.** "Number of parameters" is the wrong count. What matters is *effective* degrees of freedom. Searching among models spends more of them than the parameters you end up keeping (map §B2).

### 2. Finance: estimation error and "1/N"
- **Striking result: DeMiguel, Garlappi & Uppal 2009.**
  - Fourteen sophisticated portfolio models were tested against simply splitting money equally across assets ("1/N"). None beat 1/N consistently on risk-adjusted return, certainty-equivalent return or turnover.
  - By their calibration, the textbook optimiser would need about **3,000 months of data, i.e. 250 years, to beat 1/N with 25 assets**, and about 6,000 months with 50 (abstract ✓).
- **Caveat.** The rebuttals do not overturn this. They show *how* to win:
  - estimate fewer things (ignore expected returns, time only volatility: Kirby & Ostdiek 2012);
  - shrink the optimiser toward 1/N (Tu & Zhou 2011);
  - impose constraints (Jagannathan & Ma 2003).

  Zakamulin 2017 adds that some "optimisation wins" are hidden factor bets. **Supported.**

### 3. Finance: backtest overfitting and the factor zoo
- **Striking result: Bailey, Borwein, López de Prado & Zhu 2014.**
  - With five years of data, if you try more than about **45 independent strategy variants**, you are almost guaranteed to find one with an excellent-looking Sharpe ratio of 1. That happens even if every variant is worthless (✓).
  - The best of many coin-flippers always looks like a genius.
- **Striking result: McLean & Pontiff 2016.** Across 97 published stock-return predictors:
  - returns are 26% lower out of sample, the statistical part;
  - they are 58% lower after publication, the part where other investors read the paper and trade the signal away (✓).
- **Striking result: Harvey, Liu & Zhu 2016.**
  - After 316 published "factors", they argue a new one needs a t-statistic above 3, not 2.
  - They also argue that most claimed findings in the field are likely false (✓).
  - **Dissent:** Jensen, Kelly & Pedersen 2023 find most factors replicate under a different statistical model of the trials. **Open** (map §D7).

### 4. Forecasting: the M-competitions and the combination puzzle
- **The puzzle.** Averaging several forecasts usually beats each one. But estimating "optimal" weights for the average usually does *no better than equal weights*, and often worse (Bates & Granger 1969; Stock & Watson 2004; Smith & Wallis 2009). The weights are themselves estimated, so they carry noise. **Supported.**
- **The competitions.** Spyros Makridakis has run open forecasting contests since 1982.
  - M3 (2000) concluded that sophisticated methods did not necessarily beat simple ones.
  - M3's winning "new" method was later shown to be a simple smoother in disguise (Hyndman & Billah 2003).
- **Striking result: M6 (2022–23), a live year of forecasting 100 stocks and funds and building portfolios.**
  - Of 163 teams, only 23% beat a forecast that assumed *no information at all*; the median team did slightly worse than that.
  - Forecasting skill and portfolio returns were **uncorrelated (r = 0.04)** (✓).

### 5. Judgement: improper linear models and fast-and-frugal heuristics
- **Striking result: Dawes 1979.** Predicting how faculty would rate graduate students:
  - a committee's judgement correlated **.19** with the outcome;
  - a fitted regression, tested on fresh cases, correlated **.38**;
  - *adding up the same predictors with equal weights* correlated **.48** (✓).
  - His rule of thumb: fitted weights need about 15–20 observations per predictor before they beat equal weights.
- **Gigerenzer & Brighton 2009.** Simple heuristics such as "take the best cue and ignore the rest" beat regression on average across 20 datasets. They frame it in exactly bias–variance terms: "betting on lower variance, not lower bias" (✓).
- **Caveat, and the important one.**
  - Most of these wins are against *unregularised* regression.
  - Parpart, Jones & Love 2018 prove the heuristics are the extreme end of Bayesian regression with an infinitely strong prior, and that intermediate priors do better than both ends (abstract ✓).
  - On 63 datasets with half used for training, ordinary logistic regression (0.747) edged out the simplest heuristic (0.725) (Şimşek & Buckmann 2015 ✓).
  - So "less is more" really means "less is more than *unrestrained* more". **Supported.**

### 6. Regulation: "The dog and the frisbee" (Haldane & Madouros 2012)
- **The image.** Catching a frisbee is, in physics terms, a hard problem. A dog solves it with a simple rule: run so that the angle of gaze to the frisbee stays roughly constant.
- **Striking results** from Haldane's Jackson Hole speech (✓):
  - **Rulebooks.** The US 1933 Glass–Steagall Act ran to 37 pages; Dodd–Frank (2010) to 848, with thousands more pages of rules to follow. Basel I had five risk weights; a large bank's Basel models may run to millions of parameters.
  - **Large banks.** Among about 100 large global banks, those that failed in the crisis had pre-crisis leverage ratios 1.2 points lower than survivors. The complex risk-weighted ratio did not separate them.
  - **US banks.** A five-indicator model fitted on 100 banks lost to every single indicator alone, and even to just guessing the average failure rate.
  - **Simulation.** With under about two years of daily data, a simple volatility model beat *the true model that generated the data*. In their words, simple "trumps the truth". The true model only pulled ahead after about 400 years.
- **Caveats.**
  - It is a speech, not a peer-reviewed paper. The large-bank analysis was joint early work with Gigerenzer's group.
  - Among 8,500 smaller US banks the ranking *reversed*. Haldane's own explanation is that those banks were already managed to a leverage rule, which is Goodhart's law acting on the simple metric (item 9).
  - The peer-reviewed follow-up (Aikman et al. 2021) found a four-question decision tree performed about as well as a regression: **a tie**.

### 7. Engineering and control: the waterbed, and robust-yet-fragile
- **The waterbed (Bode's sensitivity integral, 1945).**
  - In a feedback loop, pushing sensitivity to disturbances *down* at some frequencies forces it *up* at others, like pressing on a waterbed. A cleverer controller can move the bulge but cannot remove it. **Established theorem**, for linear feedback.
  - Chandra, Buzi & Doyle 2011 showed the same limit in a model of glycolysis: more control complexity "can thus fine-tune the shape" of the sensitivity "but cannot uniformly improve it" (✓). Here the mathematics is shared, not borrowed.
- **Adaptive control's warning (Rohrs et al. 1985).**
  - Self-tuning controllers with proofs of stability for their idealised model could go unstable when the real plant had small dynamics the model left out, excited by noise or disturbances.
  - The cure was to make the adaptation deliberately less eager ("leakage"), giving up some ideal-case accuracy for robustness.
  - *The 1985 paper was not read this pass; this is the standard account.*
- **Robust yet fragile (Carlson & Doyle 2002).** Systems optimised against the disturbances they expect become fragile to the ones they do not. Their example is a forest designed with firebreaks for typical sparks.
  - **Caveat:** the heavy tail of rare disasters depends on optimising for the *average* outcome. Adding risk aversion to the design goal removes it (Newman, Girvan & Farmer 2002). **Supported.**
- **Named heuristics, cited as heuristics:**
  - Gall's law: a complex system that works has evolved from a simple one that worked.
  - Brooks's "second-system effect": the second design gets every feature held back from the first.
  - Feature creep: one marketing study measured "feature fatigue", in which people buy feature-rich products and then like them less (Thompson et al. 2005).

  None has a measured tax rate.

### 8. Biology: the cost of complexity
- **Orr 2000, in Fisher's geometric model of evolution.** An organism with n independent traits adapts **at least n times more slowly** than a simple one, for mutations of the same size. A random change is less likely to help along every dimension at once (abstract ✓). **Established within the model.**
- **The twist for a podcast.** When Wagner et al. 2008 measured gene effects on 70 mouse skeletal traits, they found **no** such cost. Most genes touch only a few traits, so the *effective* complexity is low. This is itself disputed (Hermisson & McGregor 2008). **Open.**
- **When sensing pays (Kussell & Leibler 2005).** Bacteria can sense their environment and respond, or switch randomly between forms without looking. Random switching wins "when the environment changes infrequently" and sensing has a running cost (abstract ✓). This is the commute example in a microbe.

### 9. Reflexivity: Goodhart, Lucas, Campbell
- **Goodhart (1975):** a statistical regularity tends to collapse once pressure is put on it for control.
- **Lucas (1976):** relationships estimated under one policy break when the policy changes, because people respond to it.
- **The best measurement is McLean & Pontiff's** (item 3): at least 32 of the 58 points of post-publication decay came from other investors acting on the published signal.
- **Caveat.** Direct evidence for the Lucas critique in macroeconomic relations is weak, though the tests are weak too (Ericsson & Irons 1995). Do not assume reflexivity is the main term everywhere.

### For a "same math, or same mechanism?" segment

| Mechanism | Examples | Verdict |
|---|---|---|
| Estimation variance | Freedman; 1/N; equal-weight forecasts; Dawes; heuristics; Haldane's models | **Same math** (bias–variance and shrinkage) |
| Selection over many tries | Backtests; the factor zoo; the optimiser's curse | **Same math** (the best of many noisy numbers) |
| Lag against noise under change | The commute rule; exponential smoothing; adaptive filters; estimation windows | **Same math** |
| Costs per adjustment | Trading costs; a cell's cost of making a protein; the bacterium's cost of sensing | **Same mechanism**, same equations only within finance |
| Missing the turn | Regime-switching models; recession forecasts; stop-losses | **Same mechanism** |
| Fragility to the unexpected | Waterbed; firebreak forests; adaptive autopilots | **Same math only for the waterbed and glycolysis**; elsewhere the same shape |
| The world reacts | Goodhart; Lucas; published anomalies | **Same mechanism**, no shared equation |
| Gall, Brooks, feature creep, collapse of civilisations | — | **Surface analogy**: cite as rules of thumb |

**Honest bottom line for the episode.** It is not one law with one rate. There are about seven mechanisms. Three share real mathematics; the others share a story.

---

## (c) What sets the tax rate

For each factor: what is known, and the simplest formula where there is one (map §E).

1. **How much independent evidence you have, relative to how many free choices the model makes.**
   - The tax per free choice is roughly *noise ÷ number of independent observations*, and it grows faster than that as the two approach each other.
   - "Independent observations" is the catch. A model of crises is informed by the number of crises, not the number of days. Ten events pin down a rate only to about ±30%. **Established.**
2. **Noise.** The noisier the data, the earlier simple rules win. In the cleanest textbook case, a fitted least-squares model beats predicting nothing at all only if parameters-per-observation is below SNR/(1 + SNR). **Established** (Hastie et al. 2022).
3. **How many variants you tried, including the ones you tried in your head.**
   - The best of N worthless tries looks, on average, like about 1.6 standard errors of skill for 10 tries, 2.1 for 30 and 2.3 for 50. It grows slowly, roughly as √(2 ln N), but it never stops growing.
   - Every analysis choice counts as a try. In one study, 164 research teams working on the same data disagreed about twice as much as their own standard errors implied (Menkveld et al. 2024). **Established** (the mathematics); **Supported** (the team study).
4. **How fast the world changes.**
   - Too adaptive pays noise; too static pays lag.
   - The best adaptive rule moves by about √q of each surprise, where q is persistent variation over random variation, and still pays a cost of about √q.
   - A rule that never updates pays a lag cost that grows the longer it runs.
   - After sudden shifts in level, models that "remember" the old normal are the ones that fail (Clements & Hendry). **Established.**
5. **What each adjustment costs.** With trading costs, the best rule has a band of doing nothing. In continuous-time theory the band widens as the cube root of the cost. High-turnover signals are the ones costs kill (Novy-Marx & Velikov 2016). **Established** (theory); **Supported** (data).
6. **Lopsided costs at turning points.**
   - Most of the value of a regime-switching rule comes from calling the *next* regime, and turning points are almost never called: consensus forecasts predicted 5 of 153 recessions a year ahead (An et al. 2018, from summaries).
   - In a Monte Carlo study where the data really did switch regimes, the switching model gained at most 12%, and 60% of its error came from misreading the coming regime (Bessec & Bouabdallah 2005 ✓).
   - Under a random walk, every stop-loss rule lowers expected return (Kaminski & Lo 2014). **Supported.**
7. **Whether the environment reacts.** Published or widely used signals decay; measured at ≥ 32 points for stock predictors. **Supported**; no general rate law found.
8. **How big the real edge is.** A small genuine advantage of the complex rule needs an enormous record to show: 250 years for portfolios, 400 years in Haldane's simulation. **Supported.**

**The common thread.** Extra freedom is paid for in estimation and selection noise. It is worth the price only if the record holds enough *independent* information about the extra structure. Change is both what shortens the useful record and the reason to adapt at all. That tension is why the winning rule is usually in the middle.

---

## (d) When complexity wins

This is the half that keeps the episode honest. Complexity reliably pays under these conditions:

- **Lots of related data, pooled.** In the M5 competition (2020; Walmart sales, 42,840 series), machine-learning methods beat every statistical benchmark: the winner by 22.4%, every top-50 entry by more than 14% (✓).
  - **What changed:** the models learned across 30,490 related product series at once and used prices and promotions.
  - **Even there,** at the noisiest level (single products in single stores) the edge shrank to a few percent.
  - **And** the winners combined their models with *equal weights*.
- **Complexity with a leash.** Gu, Kelly & Xiu 2020 found machine learning improved stock-return prediction. But plain regression on 900+ predictors failed badly, the gains needed heavy regularisation, and neural networks peaked at three layers, then got worse (sub-agent reading). In every field the winner is the *regularised* complex model: shrunk, constrained or pooled.
- **Enough data per choice.** In Dawes's largest study (861 patients), fitted regression beat equal weights (.46 vs .34 ✓). Simple wins at small samples; the crossover moves as the sample grows.
- **A fast-changing world with cheap, timely signals.**
  - Bacteria sense rather than gamble when the environment changes often (Kussell & Leibler).
  - In M6, the winners updated at every round.
  - Simple volatility-scaling held up for momentum and profitability strategies (Cederburg et al. 2020 ✓), but failed in real time for most others.
- **Very high dimension with a strong signal: "double descent".**
  - Belkin et al. 2019 showed that past the point where a model can fit the training data exactly, making it *even bigger* can make it predict better again (✓). This is why huge neural networks work.
  - The conditions are known: lots of weak, spread-out directions in the data to absorb noise harmlessly, and a strong signal.
  - Whether this carries over to noisy, changing financial data is **actively contested**. Kelly, Malamud & Zhou 2024 say yes. Nagel 2025 shows their result can be reproduced by a simple volatility-timed momentum rule, and that the method "mislearns" when the data are reversed (✓).
- **The environment really is complex.** Ashby's law of requisite variety (wiki entry F1): a regulator needs at least as many distinct responses as the disturbances it must handle. Too simple a controller fails for a different reason, and Goodhart's "extremal" variant can punish an *over-simple* model pushed outside its range.

**The rule of thumb the literature supports:** complexity pays when the record holds many independent examples of the structure it adds, when the extra freedom is regularised toward the simple rule, and when the world either stays put or changes fast enough to be tracked. **Supported.**

---

## (e) How the AlphaEntropy experience fits

The facts below come from the 2026-10-19 read-only review summary; the project itself was not reopened. Some of what happened looks like the phenomenon; some looks like workflow. The two need separating, because they have different cures.

### Parts that match the documented phenomenon
- **"Everything clever off" beat "everything on"** (Calmar 1.064 vs 0.904; the entry gate alone off gave 1.102). This is the direction the literature predicts for a small number of independent events. **Supported as consistent; not a measurement of the tax** (see below).
- **The survivors are the simple parts:** a profitability-quality sleeve, a trend sleeve and a near-static hedge.
  - This matches the literature's survivors: profitability and momentum held up out of sample in Cederburg et al.; static hedges often match dynamic ones (Lien 2005); low-turnover signals survive costs (Novy-Marx & Velikov).
  - This says the outcome is *ordinary*, not that those parts will keep working.
- **The D_eff hedge switch whose benefit was mostly extra exposure** is Zakamulin's warning in another form. An "optimisation win" that is really a different bet, here more market exposure, is a framing failure: the gain was real but was not what it seemed to be.
- **The timing engine, falsified by a placebo,** matches Welch & Goyal (return-timing signals rarely survive out of sample). The placebo test was the right tool. It is the same logic as Nagel's reversal test: a rule that has learned something should fail when the thing is removed.
- **Crisis discriminators that "sold bottoms", and un-hedging that came off before the bottom,** are the turning-point mechanism:
  - a switch earns its keep only by calling the *next* regime, and turns are rarely called (Dacco & Satchell; Bessec & Bouabdallah);
  - under near-random-walk prices, exit-and-re-entry rules cost expected return (Kaminski & Lo).
- **All 16 dynamic and PID hedges worse than static** fits estimation variance plus lag (Lien; the lag–noise trade-off), probably with turnover costs on top. The control-theory echo, where eager adaptation is fragile (Rohrs), is suggestive. It is not established for this case.
- **About 8–10 independent ≥10% drawdowns since 2007.** This is the binding constraint. Any rule meant to act around drawdowns has roughly ten data points of evidence, whatever the number of trading days. At that size, a switching rate or a crisis threshold is pinned down only to about ±30%, before any search over variants.

### Parts that are workflow, not the phenomenon
- **Thirty to fifty variants without a sealed holdout until late.** By Bailey et al.'s arithmetic, the best of 30–50 worthless variants looks like about 2.1–2.3 standard errors of skill. Over a short, event-poor history that is easily a good-looking Calmar. This is the *selection* tax (M2). It is a property of the search, not of the market.
- **Adopting features below your own +0.02 Calmar threshold, when repeat-run noise exceeded several adopted gains.** Each such adoption was, in expectation, a coin flip recorded as progress. The wiki carries one instance: P19's "validated" fix was +0.006 (map §G.3). Menkveld et al.'s 164 teams show this is how competent people work by default, and that people underestimate it.
- **Calmar is a noisy yardstick here.** Its denominator is the single worst drawdown, so with 8–10 drawdowns it is driven by one or two events. A 0.16 difference between "all on" and "all off" may be partly noise. The literature says the direction is unsurprising; the size is not measured.

### What the summary does not let us tell apart
Were the features *harmful*, or just *worthless and adopted by luck*?
- If they were adopted on noise, removing them would on average change nothing. Removing them *improved* the result, which suggests either real harm or noise in the ablation itself.
- If the ablation ran on the same history the features were tuned on, features that fail even there suggest their adoption gains were noise (the optimiser's curse) or that they interfered with each other.
- Bailey et al. show that, when returns mean-revert, optimised variants can be *worse* out of sample than unoptimised ones, so harm is possible.

From the review summary alone, the selection tax and the structural tax cannot be separated. The project records below separate them partly.

### What the project records add
*Source: AlphaEntropy project records (owner's private repo), via main session 2026-10-19. These are a main-session check of project files, not a publication, and this session did not read them.*

- **The deflated Sharpe ratio test (Bailey & López de Prado's correction for the number of strategies tried).**
  - In the V28.8c validation battery (2026-05-04), the script and report gave DSR = 0.0, "observed SR plausibly random given # tested", with N = 9.
  - The JSON value was later hand-edited to 0.948, and that figure entered the project history as "borderline-strong".
  - A 2026-10-18 audit found the test mis-specified: computed on a local simulation rather than the QuantConnect backtest, and with N = 9 when about 66 Sharpe values were on file.
  - Recomputed on the real curves, DSR ≈ 1.00 for N up to 200. So "Sharpe above zero" **survives** a proper multiple-testing correction.
  - The stronger claim, beating a passive alternative with Sharpe 0.55, holds only at about 84% confidence.
- **The factor-zoo novelty claim.**
  - An archived note said the "profitability durability" composite matched none of the 319+ documented factors, citing Harvey, Liu & Zhu.
  - The traded signal uses only about 3 months of fundamentals, so it is mostly the *level* of profitability: a known factor.
  - The audit's regression on standard factor sets (Fama–French five-factor, momentum, quality-minus-junk, betting-against-beta) left an alpha of about 4.5%/yr (t ≈ 4.3), with a structure close to profitability + size + momentum.
  - So the "new factor" claim was a framing error (Zakamulin's point: check what known bet you are making before calling it new). The residual alpha is an in-sample backtest statistic: it says nothing about the future, and none of this is investment advice.
- **What this does to the reading.**
  - The core system (quality sleeve, trend sleeve, near-static hedge) survives a correction for everything tried. Its record is not just a lucky pick from many variants.
  - The **added complexity** does not survive: its increments were smaller than repeat-run noise, and the ablation preferred it switched off.
  - **The tax fell on the increments, not on the whole system.** That is exactly what the literature predicts. A strategy built from known, durable effects can be real, while the fine-tuning layered on top is mostly selection noise (M2), turning-point misses (M5) and estimation variance (M1).
- **The process lesson.**
  - A failed test was recorded as a pass, and an audit caught it later. The files do not show who made the edit, and the point is not blame.
  - It is the strongest argument in this case for three practices: pre-register a test before running it; write results to a log that cannot be edited afterwards; re-run key validations against the production record, not a local stand-in.
  - The wiki's own QR-006b benchmark used pre-registration and commit-ordered results for the same reason.

### What would make it measurable
These are the standard tools, not new ones:
- count every variant tried, including abandoned ones;
- estimate repeat-run noise directly;
- deflate the chosen variant's Sharpe for the number of tries (the deflated Sharpe ratio);
- keep a sealed holdout that no decision has touched;
- count evidence in drawdowns, not days.

**Calibrated summary.** AlphaEntropy looks like a textbook case: a core built from known effects survives a correction for multiple testing, while the dynamic additions on top carry the tax. The tax on those additions is mostly the *selection* tax plus the *turning-point* tax on few events, rather than a newly measured "complexity tax". **Supported** as a reading of the review summary and the project-record facts above; not independently tested.

---

## (f) Reading list, easiest first

1. **Haldane & Madouros, "The dog and the frisbee"** (BIS speech, 31 August 2012; free). The best single read for a podcast: vivid, numerical, about 20 pages. *(Read by this session.)*
2. **Dawes, "The robust beauty of improper linear models in decision making"**, *American Psychologist* 34:571 (1979). A classic: short, witty, and the equal-weights result in its original form. *(Read.)*
3. **Smith & Winkler, "The optimizer's curse"**, *Management Science* 52:311 (2006). Why the best-looking option disappoints, with a cure. Light mathematics. *(Read for the key figure.)*
4. **Gigerenzer & Brighton, "Homo heuristicus"**, *Topics in Cognitive Science* 1:107 (2009). The heuristics case at full strength, including a clear bias–variance section. *(Read for key passages.)*
5. **Parpart, Jones & Love, "Heuristics as Bayesian inference under extreme priors"**, *Cognitive Psychology* 102:127 (2018). The reconciliation: heuristics are a limit of regularised regression, and the middle beats both ends. *(Abstract read.)*
6. **Bailey, Borwein, López de Prado & Zhu, "Pseudo-mathematics and financial charlatanism"**, *Notices of the AMS* 61:458 (2014). Backtest overfitting for mathematicians; the 45-trials result. *(Read for key passages.)*
7. **DeMiguel, Garlappi & Uppal 2009**, *RFS* 22:1915, then **Kirby & Ostdiek 2012**, *JFQA* 47:437, for the rebuttal. *(Abstracts read.)*
8. **McLean & Pontiff 2016**, *Journal of Finance* 71:5. Statistical decay versus reflexive decay, measured. *(Abstract and introduction read.)*
9. **Makridakis et al., "The M6 forecasting competition"** (arXiv:2310.13357; *IJF* 41:1315, 2025). What happened when 163 teams tried to forecast markets live. *(Read for key passages.)*
10. **Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*, chapter 7** (free PDF from the authors). The textbook account of the per-parameter cost, AIC/BIC and cross-validation.
11. **Clements & Hendry, "Explaining the results of the M3 forecasting competition"**, *IJF* 17:550 (2001), short, then **Pesaran & Timmermann 2007**, *J. Econometrics* 137:134. Why simple, robust methods win when the world shifts.
12. **Belkin et al. 2019**, *PNAS* 116:15849, on double descent, then **Kelly, Malamud & Zhou 2024** (*JF* 79:459) **against Nagel 2025** (NBER WP 34104). The live debate on whether huge models help in finance.
13. **Carlson & Doyle, "Complexity and robustness"**, *PNAS* 99:2538 (2002), with **Chandra, Buzi & Doyle 2011**, *Science* 333:187. Robust-yet-fragile, and the waterbed in a cell.
14. **Orr, "Adaptation and the cost of complexity"**, *Evolution* 54:13 (2000), with **Wagner et al. 2008**, *Nature* 452:470, for the empirical challenge. The biologists' own complexity tax.

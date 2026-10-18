# Questions Raised Log

> **What this is.** A running intake log of open scientific questions that the wiki's compiled knowledge raises — questions to ask the world, not answers we claim. Started 2026-10-18 after the pre-merge consistency pass, when the project returned to its original purpose: compile real science, map the connections, and look for good questions.
>
> **What this is not.** Not conjectures (P-series) and not yet open-question entries (Q-series in `ds_wiki.db`). Nothing here asserts that a question is new. Most will turn out to be well-known open problems, and that is fine: placing ourselves correctly in an existing conversation is the point.

## How the log works

**IDs** use the prefix `QR-` so they never collide with the wiki's Q-series (Q1–Q5) or P-series.

**Status ladder** (a question moves down it; nothing skips a step):

1. **Raised** — written down, with why the wiki's map suggests it.
2. **Literature-mapped** — the field's current state found and read from primary sources: who works on it, what is settled, what is not.
3. **Gated** — the prior-art gate (`memory/feedback_prior_art_gate.md`) has run, with one verdict:
   - `open-in-literature` — a recognised open problem; record it as such, citing who frames it.
   - `answered` — the literature already settles it; fold the answer in as reference entries.
   - `narrow-angle-provisional` — the field asks it, but the wiki's cross-domain view adds a specific sub-question nobody seems to ask. Provisional until a second, primary-source search fails to find it.
4. **Filed** (optional) — becomes a Q-series entry in `ds_wiki.db`, anchored `open_in_literature`.

**Rules.** Literature cited below is a *starting point* unless marked verified. No question becomes a wiki entity without the gate. Each entry names the wiki entities involved and the gaps in the wiki's own coverage, because a question sitting on an empty patch of the map needs grounding (Mode A) before any exploration (Mode B).

---

## QR-006 · Can information measures warn of tipping points earlier, or more reliably, than classical indicators? — **PRIORITY**

- **Question.** Do information-theoretic measures (transfer entropy and information flow, mutual information, Fisher-information indices, entropy rates, complexity measures, correlation-matrix concentration) give earlier or more reliable warning of critical transitions in real systems — ecosystems, climate, medicine, markets — than rising variance and autocorrelation (critical slowing down)?
- **Why the wiki raises it.** It is the honest descendant of the CCA thread. CCA found that correlation-matrix observables discriminate first-order from continuous transitions, using different signatures from Brown–Bossomaier–Barnett's transfer entropy (STAT3, CCA-1c, Phase E). It is also the subject of the podcast's S1E2 *Tipping Points*. It is the owner's top real-world question.
- **Wiki holdings.** STAT3, CCA-1c, X0_FIM_Regimes, M3 (Preisach hysteresis), D2 (Feigenbaum). **Gap:** the wiki has no entries for critical slowing down, early-warning signals, bifurcation types, or regime-shift ecology. The question sits on an almost empty patch of the map.
- **Starting literature (not yet verified this session):** Scheffer et al. 2009 (*Nature* 461:53); Dakos et al. 2012 (*PLoS ONE*); Boettiger & Hastings 2012; Ditlevsen & Johnsen 2010; Barnett et al. 2013 (*PRL* 111:177203); Brown, Bossomaier & Barnett 2022; Fath, Cabezas & Pawlowski 2003 (Fisher information for regime shifts); Chen et al. 2012 (dynamical network biomarkers); Bury et al. 2021 (*PNAS*).
- **What would decide it.** Head-to-head comparisons on the same data: lead time and false-alarm rate of each indicator, across transition types (fold, noise-induced, rate-induced), on systems where the transition is known.
- **Possible prior art inside the wiki to check:** X0's "Fisher-information regime" classification against the ecological Fisher Information index; CCA's correlation-concentration signal against dynamical network biomarkers.
- **Status:** Raised → **literature mapping in progress** (2026-10-18).
- **Next:** read the literature map; fold the classical EWS and information-EWS literature in as reference entries (Mode A); then decide whether the first-order vs continuous angle from the CCA work is a question the field already asks.

## QR-001 · Why is nature describable with so few parameters?

- **Question.** Is there a measurable, domain-general signature of when a complex system — biological, ecological, economic — admits a low-dimensional effective description, and when it does not?
- **Why the wiki raises it.** It is the honest descendant of "effective dimensionality as the hidden variable" (Ax2, P5–P7). The map puts RG, information geometry and sloppy models side by side.
- **Wiki holdings.** RG01, RG04, M4 (Mori–Zwanzig), M6, IT03, IT05, P5, P7; sloppy models arriving via the fold-in (Machta 2013). Coverage is good.
- **Starting literature:** Machta, Chachra, Transtrum & Sethna 2013 (*Science* 342:604; anchored); Transtrum et al. 2015 (*J. Chem. Phys.* 143:010901); Quinn et al. 2023 (*Rep. Prog. Phys.*).
- **What would decide it.** A predictor of compressibility, such as the eigenvalue-spectrum shape of the Fisher information, tested on model classes from different fields before fitting.
- **Status:** Raised.

## QR-002 · Are living systems poised at criticality, and what tunes them there?

- **Question.** Is the apparent criticality of neural, genetic and collective biological systems real, and if so is it selected, self-organised, or an artefact of how the data are analysed?
- **Why the wiki raises it.** It descends from the regimes and three-state thread (H1, X0). Criticality entries link to biology mainly through information theory.
- **Wiki holdings.** C3, STAT3, the criticality glossary page. **Gap:** almost no biological-criticality entries.
- **Starting literature:** Mora & Bialek 2011 (*J. Stat. Phys.*); Muñoz 2018 (*Rev. Mod. Phys.* 90:031001).
- **What would decide it.** Criticality tests that survive known artefacts (subsampling, thresholding, latent common drivers); evidence of a tuning mechanism.
- **Status:** Raised.

## QR-003 · What sets biological and urban scaling exponents, and why is there no universal one?

- **Question.** The network-delivery theories (WBE for organisms, Bettencourt for cities), Dynamic Energy Budget theory and Glazier's metabolic-level boundaries predict different exponents and different dependence on dimension. Can they be tested against each other across organisms, cities and engineered networks, where the embedding dimension and network type differ?
- **Why the wiki raises it.** It descends from P2, P11 and P12; C1 and C2 sit side by side on the map.
- **Wiki holdings.** C1, C2, H5, X1, and soon WBE 1997, the allometric-cascade debate, metabolic-level boundaries, DEB and Bettencourt 2013 as reference entries (fold-in in progress). Coverage will be good.
- **Starting literature:** West, Brown & Enquist 1997; Bettencourt 2013 (verified 2026-10-18: δ = H/[D(D+H)] ≈ 1/6); Glazier 2010; Kooijman (DEB); Kolokotrones 2010 and its replication record (in C1).
- **What would decide it.** Each theory's prediction for a system it was not built for (WBE for a planar network, Bettencourt for a 3-D one), checked against data.
- **Status:** Raised.

## QR-004 · How close do living systems run to the thermodynamic limits of information processing?

- **Question.** Do cells, organisms and ecosystems operate near Landauer and thermodynamic-uncertainty bounds when sensing, signalling and regulating, and what does running near those bounds buy them?
- **Why the wiki raises it.** It is the real version of P15's retired "cost of coherence". It runs through the map's biggest genuine hubs (Second Law TD3, Shannon INFO1, Landauer B5) into biology.
- **Wiki holdings.** TD3, INFO1, INFO2, INFO4, INFO5, B5, BIO5, F1, F5. Coverage is good on the physics side, thinner on the measured biology.
- **Starting literature:** Bérut et al. 2012 (Landauer test); Barato & Seifert 2015 (*PRL* 114:158101); Lan et al. 2012 (*Nat. Phys.* 8:422, energy–speed–accuracy in sensory adaptation).
- **What would decide it.** Measured dissipation versus precision for specific biochemical networks, compared with the bound.
- **Status:** Raised.

## QR-005 · Is gravity quantum, or thermodynamic?

- **Question.** Will tabletop experiments show gravity carrying quantum information (mediating entanglement), or the decoherence and force noise that entropic and thermodynamic models predict?
- **Why the wiki raises it.** It is the testable form of the Fisher–gravity and entropic-gravity strand, and of the owner's information-first worldview.
- **Wiki holdings.** GT01, GT02, GT05 (corrected 2026-10-18), GT10, HB02, BR01. Coverage is good.
- **Starting literature:** Bose et al. 2017 (*PRL* 119:240401); Marletto & Vedral 2017 (*PRL* 119:240402); Carney, Karydas, Scharnhorst, Singh & Taylor 2025 (*PRX* 15:031038, **verified 2026-10-18**: free-energy models, with S_FF(0) force noise and decoherence signatures; the non-local λ = 0 model is already excluded).
- **What would decide it.** A gravitational-entanglement witness, or the absence of predicted excess decoherence and force noise, at the relevant mass and separation scales.
- **Status:** Raised.

---

## Coverage gaps the log has surfaced

- **Tipping points and early-warning signals (QR-006):** no entries for critical slowing down, bifurcation classes, regime-shift ecology, or information-based early warning. This is the highest-priority Mode A gap.
- **Criticality in biology (QR-002):** almost no entries.

## Changelog

- **2026-10-18** — Log started with QR-001 to QR-006, drawn from the big-picture review after the consistency pass. QR-006 marked priority by the owner; literature mapping launched.

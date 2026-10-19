# IT06 geodesic check (2026-10-18)

> **Status: APPLIED 2026-10-18** by `scripts/migrations/it06_geodesic_check_2026_10_18.py`. The owner approved items 1–22, the P21 calibration row only (no X8 row), and the audit_ref dated 2026-10-18. Written: 13 section values, the P21 claim, 7 link descriptions, 1 calibration row (P21, Established, unchanged). Item 22 is a banner at the top of `docs/ALPHAENTROPY_GEODESIC_TEST_SPEC.md`. Claim counts unchanged: 26 Speculative · 5 Supported · 7 Established · 5 Falsified · 4 Retired.
> Mode A. Follow-up to [`QR004_CORRECTIONS_2026_10_18.md`](QR004_CORRECTIONS_2026_10_18.md) §4, which left IT06 out. Planned audit_ref: `gsw-it06-geodesic-check-2026-10-18`. The brief suggested `-2026-10-19`; today's local date is used instead, and the owner can change it.
> Pattern tags (existing, no new tag): `vocabulary-stacking-analogy` (a friction tensor called "Fisher–Rao"); `over-extension-beyond-formula-range` (a slow-driving result stated as general, then applied to fast market shocks).

## 0. Summary in plain words

IT06 says that the least-wasteful way to drive a small system from one state to another follows a shortest path (a geodesic) measured with the Fisher–Rao metric of information geometry. That is true only in a special case.

- **The general result (Sivak & Crooks 2012).** For slow driving near equilibrium, the wasted work is set by a *friction tensor*. The friction tensor equals the Fisher information multiplied, entry by entry, by a relaxation-time matrix. Optimal protocols are geodesics of the friction tensor.
- **When it becomes Fisher–Rao.** Only when the relaxation time is the same everywhere along the path. That is the setting of the older thermodynamic-length results (Salamon & Berry 1983; Crooks 2007).
- **Outside slow driving.** The geodesic picture fails: exact optimal protocols jump at the start and end.

IT06 also writes the Jarzynski and Crooks theorems as the total-entropy theorem with a substitution. They are sister results with different starting conditions: both require the system to start in equilibrium. And IT06 calls the fluctuation theorem a proof of the second law, which Seifert's own review explicitly says it is not.

**What depends on it:**
- **X8.** The "Seifert's bound ⟨W_diss⟩ ≥ d_geodesic²/τ" is not Seifert's. It uses the wrong metric and mismatched units, and it is applied in the fast regime where the result does not hold. Test 3 never used the bound, though, so no reported number changes.
- **P21.** Instance (4) and the 2026-05-04 addendum say Chentsov's theorem covers this instance. It does not, because the friction tensor depends on the dynamics.
- **BR04.** One sentence of the same overreach.
- **Links.** Seven link descriptions.
- **The Fisher–gravity chain** (M6→IT05→IT03→GT10→GT01) **does not depend on IT06.** None of its five entries cites IT06 or dissipation geodesics. The only contact is P21's prose.

**Confidence labels:** none change. One P21 calibration row is proposed, with its label unchanged (Established, for Chentsov's classical theorem only), recording that instance (4) is withdrawn from the list Chentsov covers. Claim counts stay 26 / 5 / 7 / 5 / 4.

## 1. Primary sources read by this session

| Source | Read | What it settles |
|---|---|---|
| Sivak & Crooks 2012, *PRL* 108:190602, arXiv:1201.4166v2 | **full text** | Friction tensor ζ_ij = β∫₀^∞⟨δX_j(0)δX_i(t″)⟩ dt″ (Eq. 12). Excess power P_ex = λ̇ᵀζλ̇ (Eq. 13). Valid in linear response, when "control parameter velocities change on timescales slower than the relaxation time" (before Eq. 11). L = ∫√P_ex dt; **W_ex ≥ L²/Δt**, with equality only at constant excess power, by Cauchy–Schwarz (p. 3). Minimum-excess-work protocols are geodesics of ζ (p. 3). **ζ = k_BT τ∘I**, the Hadamard product of the integral relaxation-time matrix and the Fisher information (Eq. 14). "When the relaxation time does not vary with the control parameter, the Riemannian metric reduces to the Fisher information metric" (p. 4). Excess work equals dissipation only once the system re-equilibrates at the end (p. 3). The method misses the boundary jumps of exact optima (Schmiedl & Seifert 2007) (p. 5). |
| Crooks 2007, *PRL* 99:100602, arXiv:0706.0559v2 | **full text** | The thermodynamic metric is the covariance of the collective variables, which equals the Fisher information of the Gibbs family in natural parameters (Eqs. 4, 6). Divergence J = τ∫λ̇ᵀgλ̇ dt, and J ≥ L² (Eqs. 8–9). The dissipation link is for a protocol of N discrete steps with full re-equilibration after each: forward-plus-reverse hysteresis ω → J/N (Eq. 12). One direction is half that ("differs by a factor of 2", p. 3). The units are k_B, because λ includes β. Geodesics "minimize the dissipation for slow, but finite time transformations" (p. 1). |
| Seifert 2012, *Rep. Prog. Phys.* 75:126001, arXiv:1205.4176 | §§3.2–3.3, 4.1–4.3, 7.1–7.2 | Jarzynski (Eq. 58) is the IFT for the dissipated work w_d = (w − ΔF)/T (Eq. 59); "Its validity requires that one starts in the equilibrium distribution" (§3.2.1). Crooks (Eq. 61) needs the reverse process to start in equilibrium at λ_t (§3.2.3). The IFT for Δs_tot (Eq. 64) holds for arbitrary initial distribution, driving and duration, but "should definitely not be considered to constitute a fundamental proof of the second law" (§3.3.1). A detailed FT for Δs_tot holds in a NESS (Eq. 65). All these IFTs are one master identity with different choices of the end distribution p₁ (Eq. 80, §4.3). ⟨w⟩ − ΔF equals a path relative entropy when both processes "start and end in the respective equilibrium states" (§7.2, Eqs. 147–148). Exact optimal protocols have jumps "absent in a linear response treatment" (§7.1.1). The review does **not** state a Fisher–Rao geodesic result; its only thermodynamic-length mention is a passing citation of Feng & Crooks (§7.2, ref. 274). |
| Salamon & Berry 1983, *PRL* 51:1127 | **secondary only.** APS returned 403. Read via Deffner & Bonança 2020, arXiv:2006.13761, Eqs. 1–7, full section | Endoreversible processes, with the Weinhold metric η = ∂²U/∂X∂X. Dissipated availability ΔE = ε̄∫Ẋᵀ η Ẋ dt ≥ ε̄ℓ²/τ, where ε̄ is the time-averaged lag (relaxation) time. Constant thermodynamic speed is optimal. |

**Not re-read this session, cited as standard:**
- Kawai, Parrondo & Van den Broeck 2007, *PRL* 98:080602. Seifert §7.2 states the same result.
- Schmiedl & Seifert 2007, *PRL* 98:108301. Sivak–Crooks p. 5 and Seifert §7.1 describe it.
- Skovgaard 1984, *Scand. J. Stat.* 11:211: the affine-invariant metric on covariance matrices is (up to a factor 2) the Fisher–Rao metric of the zero-mean Gaussian family.

## 2. What held

- ⟨Δs_tot⟩ = D_KL(P_F‖P_R) ≥ 0, with the reverse process started from the actual final distribution (Seifert Eqs. 71, 80).
- The IFT ⟨e^{−Δs_tot}⟩ = 1 for arbitrary initial distribution, driving and duration (Seifert Eq. 64), within Langevin or master-equation dynamics.
- ⟨W⟩ − ΔF ≥ 0 and the Jarzynski and Crooks formulas themselves. Only their derivation and conditions are wrong in IT06.
- BR04's identity "Ruppeiner metric = Fisher information of the Gibbs family" (Crooks 2007 Eqs. 4, 6; Brody & Rivier 1995).
- X8's use of the affine-invariant SPD distance as a Fisher–Rao distance (zero-mean Gaussians; Skovgaard 1984). X8's empirical η values are untouched.
- GT07's analogies to s_tot and W_diss are not touched.

## 3. Numbered correction list

**Format** (as in QR-004): a dated banner goes **after** the original text, which stays unchanged:

> **CORRECTION 2026-10-18 (`gsw-it06-geodesic-check-2026-10-18`).** … *The text above is unchanged.*

Link descriptions follow `[Corrected 2026-10-18, gsw-it06-geodesic-check-2026-10-18] <new text>. Previously: "<old text>"`. Link types and endpoints are not changed. In a markdown table the banner goes after the table.

### IT06 (entry text)

**1. IT06 — What It Claims.**
Quotes:
- (a) "holds exactly for any stochastic process, and the Jarzynski equality and Crooks fluctuation theorem follow as special cases by setting s_tot = β(W − ΔF)"
- (b) "This is the information-theoretic proof of the second law"
- (c) "Stochastic thermodynamics further reveals that the Fisher-Rao metric governs the geometry of optimal non-equilibrium processes: minimum-dissipation paths between thermodynamic states are geodesics on the Fisher-Rao manifold of probability distributions"

Corrected:
> (a) The IFT for Δs_tot holds for Markovian (Langevin or master-equation) dynamics with any initial distribution, driving and duration. Its thermodynamic reading assumes that the noise is not affected by the driving (Seifert 2012 §3.2.1, §3.3.1, Eq. 64). Jarzynski and Crooks are not this IFT with a substitution. All three are cases of one master identity ⟨e^{−R}⟩ = 1, whose R depends on the chosen end distribution (Seifert 2012 Eq. 80):
> - with the actual final distribution, R = Δs_tot;
> - with an equilibrium start at λ₀ and the equilibrium distribution at λ_t as reference, R = β(W − ΔF), the dissipated work.
>
> Jarzynski requires that equilibrium start (§3.2.1). Crooks also requires the reverse process to start in equilibrium at λ_t (§3.2.3). β(W − ΔF) equals Δs_tot only if the system has also relaxed to equilibrium at the end.
>
> (b) Within stochastic dynamics, ⟨Δs_tot⟩ = D_KL(P_F‖P_R) ≥ 0 restates the second law as distinguishability of forward and reverse paths. It is not an independent proof: the irreversibility is built in through the stochastic dynamics (Seifert 2012 §3.3.1).
>
> (c) For slow driving near equilibrium, the mean excess work is W_ex ≈ ∫ λ̇ᵀ ζ(λ) λ̇ dt. Here ζ_ij = β∫₀^∞⟨δX_j(0)δX_i(t)⟩_λ dt is the friction tensor, a Riemannian metric on control-parameter space. Minimum-excess-work protocols are its geodesics, run at constant excess power (Sivak & Crooks 2012, Eqs. 12–13, p. 3). In general ζ is **not** the Fisher–Rao metric: ζ = k_BT τ∘I, the entry-by-entry product of an integral relaxation-time matrix and the Fisher information of the equilibrium family (Eq. 14).
>
> It reduces to the Fisher metric times a constant only when the relaxation time does not vary along the path (p. 4; for several parameters, a single relaxation time common to all of them). That is the setting of the classical thermodynamic-length results: Salamon & Berry 1983 (endoreversible, with a mean relaxation time) and Crooks 2007 (stepwise protocols with re-equilibration after each step). Even then the manifold is the family of equilibrium states indexed by the control parameters, not the space of all distributions. Outside linear response, exact optimal protocols jump at the start and end (Schmiedl & Seifert 2007; Seifert 2012 §7.1), which the geodesic picture misses. Seifert's 2012 review does not itself state the geodesic result.

**2. IT06 — Mathematical Form.**
Quotes:
- "Jarzynski: s_tot = β(W − ΔF)"
- "Crooks: P_F(s_tot = a) / P_R(s_tot = −a) = e^a"
- "⟨W_diss⟩ ≥ (1/τ) ∫ g_ij λ̇^i λ̇^j dt where g_ij = Fisher-Rao metric on parameter space. Equality: minimum-dissipation path is a geodesic on Fisher-Rao manifold"

Corrected:
> **Jarzynski** (equilibrium start at λ₀): ⟨e^{−β(W−ΔF)}⟩ = 1. This is the master IFT with R = β(W − ΔF), a different functional from Δs_tot (Seifert 2012 Eqs. 58–59, 80).
>
> **Crooks** (forward process starts in equilibrium at λ₀, reverse at λ_t): p̃(−W)/p(W) = e^{−β(W−ΔF)} (Eq. 61). A detailed theorem for Δs_tot itself holds in a non-equilibrium steady state (Eq. 65), not in general.
>
> **Thermodynamic geometry** (slow driving, linear response):
> - W_ex ≈ ∫₀^Δt λ̇ᵀ ζ(λ) λ̇ dt, with no 1/τ prefactor when written with dλ/dt.
> - ζ = k_BT τ∘I (friction tensor).
> - L = ∫₀^Δt √(λ̇ᵀζλ̇) dt.
> - **W_ex ≥ L²/Δt**, with equality only at constant excess power, i.e. a geodesic of ζ (Sivak & Crooks 2012, Eqs. 13–14, p. 3).
> - W_ex is excess work. It equals dissipation once the system re-equilibrates at the end.
>
> **Fisher special case** (constant relaxation time τ_R): ζ = k_BT τ_R I, so W_ex ≥ k_BT τ_R L_I²/Δt, where L_I is the Fisher (thermodynamic) length.
>
> **Stepwise form** (N steps, re-equilibration after each; Crooks 2007 Eqs. 9–13): forward-plus-reverse hysteresis ≈ J/N ≥ L_I²/N, in units of k_B; one direction is about half that.
>
> **Salamon & Berry 1983** (endoreversible): ΔE ≥ ε̄ℓ²/τ, with the Weinhold metric and ε̄ a mean lag time (via Deffner & Bonança 2020, Eq. 7).

**3. IT06 — Constraint Category.**
Quotes:
- "The non-negativity of KL divergence (IT03) is therefore the information-theoretic foundation of the second law, the Jarzynski equality (NE03), and the Crooks fluctuation theorem (NE04) — all are consequences of D_KL ≥ 0"
- "dissipation is minimised by following geodesics on the Fisher-Rao manifold"

Corrected:
> D_KL ≥ 0 gives the mean inequalities (⟨Δs_tot⟩ ≥ 0, ⟨W⟩ ≥ ΔF). The Jarzynski and Crooks *equalities* are not consequences of D_KL ≥ 0. They come from the master identity ⟨e^{−R}⟩ = 1 (path-probability normalisation) with equilibrium initial states (Seifert 2012 §§3.2, 4.3). In slow driving, excess work is minimised along geodesics of the friction tensor ζ = k_BT τ∘I. These are Fisher–Rao (IT08) geodesics only when the relaxation time is constant (Sivak & Crooks 2012, Eq. 14, p. 4).

**4. IT06 — DS Cross-References.**
Quotes:
- NE03 clause: "Jarzynski follows from the integral fluctuation theorem ⟨e^{−s_tot}⟩ = 1 by setting s_tot = β(W − ΔF); … the proof that ⟨W_diss⟩ = D_KL(P_F||P_R) × k_BT"
- NE04 clause: "Crooks follows from the detailed fluctuation symmetry P_F(a)/P_R(−a) = e^a of the entropy production distribution"
- IT08 clause: "minimum-dissipation non-equilibrium processes are geodesics on the Fisher-Rao manifold"

Corrected:
> NE03: Jarzynski is the master IFT with R = β(W − ΔF) for an equilibrium initial state. ⟨W⟩ − ΔF = k_BT·D_KL(P_F‖P_R) holds when forward and reverse processes both start in equilibrium (Kawai, Parrondo & Van den Broeck 2007; Seifert 2012 §7.2, Eqs. 147–148).
>
> NE04: Crooks is a detailed theorem for the work, p̃(−W)/p(W) = e^{−β(W−ΔF)}, with equilibrium starts for both processes (Seifert 2012 Eq. 61). The symmetry for Δs_tot holds in a steady state (Eq. 65).
>
> IT08: slow-driving optimal protocols are geodesics of the friction tensor ζ = k_BT τ∘I. These coincide with Fisher–Rao geodesics of the equilibrium family only for constant relaxation time (Sivak & Crooks 2012; Crooks 2007).

**5. IT06 — Mathematical Archetype.**
Quote: "The information-geometric interpretation (minimum dissipation = geodesic on Fisher-Rao manifold) adds a geometric layer: entropy production measures deviation from the geodesic path through the space of probability distributions."
Corrected:
> Entropy production does not measure deviation from a geodesic: even an optimal (geodesic, constant-power) protocol produces W_ex = L²/Δt > 0, which vanishes only as Δt → ∞. The geometric layer is the slow-driving friction-tensor metric (Sivak & Crooks 2012), and it is Fisher–Rao only for constant relaxation time.

**6. IT06 — What The Math Says.**
Quotes:
- "Setting s_tot = β(W − ΔF) recovers the Jarzynski equality"
- "Taking the ratio of the probability of observing entropy production a to the probability of observing −a gives the Crooks relation P_F(a)/P_R(−a) = e^a"
- "The minimum-dissipation result follows from the Cramér-Rao bound applied to the Fisher-Rao metric on the space of thermodynamic states: the fastest path between states with minimum entropy production is a geodesic, with dissipation proportional to the geodesic distance squared divided by the protocol duration"

Corrected:
> Jarzynski and Crooks need equilibrium initial states and use the dissipated work β(W − ΔF), not Δs_tot (see item 1).
>
> The minimum-dissipation result does not come from the Cramér–Rao bound. It comes from linear response (excess power is a quadratic form λ̇ᵀζλ̇) plus the Cauchy–Schwarz inequality, which gives W_ex ≥ L²/Δt with equality at constant excess power (Sivak & Crooks 2012, p. 3; Crooks 2007, Eq. 9). It is a lower bound, reached by the geodesic of the friction tensor ζ, and is Fisher–Rao only for constant relaxation time.

**7. IT06 — Concept Tags.**
Quote: "• Fisher-Rao metric and minimum dissipation"
Banner:
> Read this tag as "thermodynamic (friction-tensor) metric and minimum excess work in slow driving". The metric is Fisher–Rao only for constant relaxation time (Sivak & Crooks 2012).

### Links touching IT06

**8. Link 820** (IT06 *generalizes* NE03).
Old: "Jarzynski equality follows from the integral fluctuation theorem ⟨e^{-s_tot}⟩ = 1 by setting s_tot = β(W - ΔF); IT06 is the general framework"
New:
> Jarzynski is a sister case of the same master fluctuation identity, with R = β(W − ΔF) and an equilibrium initial state (Seifert 2012 Eqs. 58–59, 80); IT06 is the general framework.

**9. Link 821** (IT06 *generalizes* NE04).
Old: "Crooks fluctuation theorem follows from the detailed fluctuation symmetry P_F(a)/P_R(-a) = e^a of the entropy production distribution"
New:
> Crooks is the detailed fluctuation theorem for work, p̃(−W)/p(W) = e^{−β(W−ΔF)}, with forward and reverse processes started in equilibrium (Seifert 2012 Eq. 61); it is a special case of IT06's master identity.

**10. Link 822** (IT06 *couples to* IT08).
Old: "Minimum-dissipation non-equilibrium processes are geodesics on the Fisher-Rao manifold; IT08 provides the geometric structure that governs optimal IT06 paths"
New:
> In slow driving, minimum-excess-work protocols are geodesics of the friction tensor ζ = k_BT τ∘I (Sivak & Crooks 2012). This equals the Fisher–Rao metric of the equilibrium family (IT08) times a constant only when the relaxation time is constant (Crooks 2007; Salamon & Berry 1983).

**11. Link 832** (IT06 *couples to* FL1).
Old: "The integral fluctuation theorem <e^{-s_tot}> = 1 is deductively valid for any stochastic dynamics — it follows from the normalization of probability distributions, with no physical assumptions."
New:
> The identity ⟨e^{−R}⟩ = 1 follows from normalisation of path probabilities. Reading R as entropy production needs physical assumptions: Markovian stochastic dynamics with the noise unaffected by the driving (Seifert 2012 §3.2.1, §3.3.1).

**12. Link 977** (NE09 *couples to* IT06).
Old: "A core result of stochastic thermodynamics. (IT06's own Fisher-Rao geodesic sentence is under separate review.)"
New:
> A core result of stochastic thermodynamics. (IT06's Fisher–Rao geodesic sentence was corrected 2026-10-18 under gsw-it06-geodesic-check-2026-10-18: the slow-driving metric is the friction tensor.)

### X8

**13. X8 — Geodesic Test** (hypothesis and test design).
Quotes:
- "This would be the financial market instance of Seifert's minimum-dissipation result (IT06): optimal non-equilibrium processes are geodesics on the Fisher-Rao manifold."
- "Compare Σ_actual to the minimum possible dissipation d_geodesic²/τ (Seifert's bound: ⟨W_diss⟩ ≥ d_geodesic²/τ)"

Corrected:
> The bound is not Seifert's, and it does not apply here as written. The source form is W_ex ≥ L²/Δt (Sivak & Crooks 2012, p. 3), with L the length in the friction-tensor metric ζ = k_BT τ∘I, in units of √(energy × time). The Fisher form is W_ex ≥ k_BT τ_R L_I²/Δt and needs a constant relaxation time τ_R (p. 4). The endoreversible form is ΔE ≥ ε̄ℓ²/τ (Salamon & Berry 1983). Four mismatches:
> 1. **Metric.** The affine-invariant SPD distance is the Fisher–Rao distance of zero-mean Gaussians, not a friction metric, and it has no relaxation-time factor.
> 2. **Units.** Σ = ∫v²/D_eff dt has units of D_eff per time, d_geo²/τ has units of 1/time, and the source bound is a work. Nothing fixes the conversion.
> 3. **Regime.** The bound is a slow-driving result, valid when the protocol changes slower than the system relaxes (Sivak & Crooks, before Eq. 11). The fast episodes X8 calls near-geodesic (duration < τ_relax) are where it does not hold.
> 4. **Setting.** A market has no externally driven control parameter and no equilibrium Gibbs family.
>
> Test 3 computed only η = d_geo/L_actual, never step 2, so no reported number depends on this bound.
>
> Note (Established, a mathematical identity): σ = v²/D_eff = (d(2√D_eff)/dt)². So by Cauchy–Schwarz, for any path, Σ ≥ 4(√D_end − √D_start)²/τ, with equality when √D_eff changes at a constant rate. This is the thermodynamic-length inequality for X8's own one-dimensional quadratic form. It follows from the proxy's definition and carries no thermodynamic content.

**14. X8 — Geodesic Test** (Test 3 interpretation).
Quotes:
- "P21 universal geodesic: NOT supported."
- "P21 conditional (fast-shock limit): SUPPORTED. Acute crisis descents (<10 days) have η ≈ 0.50 — close to geodesic."
- "This is the adiabatic limit in thermodynamics."
- "P21 irreversibility: CONFIRMED. … This asymmetry is the financial market signature of entropy production: P_forward ≠ P_reverse (IT06/Seifert)."

Corrected:
> η measures how straight a path is on the SPD manifold. P21, now Established only as Chentsov's uniqueness theorem, makes no prediction about market paths, so these results neither support nor contradict P21. η ≈ 0.50 is below the near-geodesic threshold of 0.8 in this project's own spec (`docs/ALPHAENTROPY_GEODESIC_TEST_SPEC.md`). Fast driving relative to relaxation is the far-from-quasi-static regime, where excess work is largest (W_ex ∝ 1/Δt), not a minimum-dissipation limit. The descent/recovery asymmetry (1.75×) is an empirical asymmetry in path straightness: no path probabilities were computed, so it is not a measurement of P_F ≠ P_R. The η values themselves stand.

**15. X8 — DS Connections** (table row).
Quote: "| Geodesic test | P21 (Fisher-Rao Universality) | If crisis paths minimize Σ, they are Fisher-Rao geodesics — key test for P21 |"
Banner after the table:
> Σ depends only on the scalar D_eff(t). Its minimisers at fixed duration are paths along which √D_eff changes at a constant rate (item 13), so minimising Σ cannot select a geodesic on the SPD manifold. The test does not bear on P21 (item 14).

**16. X8 — Three Crisis Archetypes.**
Quotes:
- "The thermodynamic analog is exact: whether a process appears adiabatic or isothermal depends on the ratio of the process timescale to the thermal relaxation time of the measuring apparatus."
- "Is optimal filtering inherently selecting the Fisher-Rao relaxation scale?"

Corrected:
> The analogy holds in name only. In thermodynamics "adiabatic" means no heat exchange. In the thermodynamic-length and slow-driving literature, the near-reversible limit is *slow* driving relative to relaxation (Sivak & Crooks 2012; Deffner & Bonança 2020). X8's "adiabatic" (fast) regime is the opposite of that limit. The Fisher metric contains no time scale: relaxation times enter only through the friction tensor ζ = k_BT τ∘I (Sivak & Crooks 2012, Eq. 14). So there is no "Fisher–Rao relaxation scale" for the EWMA filter to select. The empirical scaling of η with duration/τ_relax stands as an observation about the estimator.

**17. X8 — Thermodynamic Connections** (IT06 paragraph).
Quote: "Σ = ∫σ dt approximates the total entropy produced in the market regime transition. … The proxy σ(t) = v²/D_eff is an approximation that captures the qualitative behavior"
Corrected:
> Unverified. No derivation or test shows that Σ approximates D_KL(P_F‖P_R) of any model of returns (X8 Overview: "This has not been done"). Treat Σ as an analogy-motivated proxy only.

**18. Link 825** (X8 *analogous to* IT06).
Old: "Σ=∫σ dt approximates Seifert's D_KL(P_forward||P_reverse) trajectory entropy production; both measure the total irreversibility of a stochastic transition"
New:
> Analogy only: Σ = ∫σ dt is not derived from path probabilities and is not shown to approximate Seifert's D_KL(P_F‖P_R) (X8 Overview).

**19. Link 828** (X8 *tests* P21).
Old: "The geodesic test (Σ_actual vs d_geodesic²/τ) is the primary falsifiable prediction connecting X8 financial trajectories to P21 Fisher-Rao universality"
New:
> The geodesic test does not test P21. The "Seifert bound" it used is mis-stated (see X8 Geodesic Test correction), and P21 is Established only as Chentsov's theorem, which predicts nothing about market paths. Test 3's η is a path-straightness measure.

### P21 (conjectures.claim)

**20. P21 — claim**, instance (4) and the 2026-05-04 addendum.
Quotes:
- "(4) non-equilibrium thermodynamics, where minimum-dissipation paths between states are geodesics on the Fisher-Rao manifold (IT06 ↔ IT08)"
- addendum: "(1) Ruppeiner-on-Gibbs and (4) Fisher-Rao non-equilibrium dissipation paths are both CLASSICAL Fisher-Rao on probability-distribution parameter manifolds … These are correctly covered by Chentsov uniqueness"
- financial test: "P21 holds conditionally in the fast-shock limit"

Corrected:
> Instance (4) is mis-stated. The metric governing slow-driving dissipation is the friction tensor ζ = k_BT τ∘I (Sivak & Crooks 2012, Eq. 14). It depends on the dynamics through the relaxation times, so Chentsov's theorem, which is about invariance under sufficient statistics, does not single it out. It equals the Fisher–Rao metric of the equilibrium family times a constant only for constant relaxation time (p. 4; Crooks 2007). Instance (4) is therefore withdrawn from the list of instances Chentsov covers; at most it is a special case of instance (1). The financial-market paragraphs do not test P21 (see X8 corrections). The label is unchanged: Established, for the classical theorem only.

### BR04

**21. BR04 — Constraint Category and Mathematical Archetype.**
Quotes:
- "the geodesics (optimal thermodynamic paths)"
- "The Ruppeiner metric defines optimal paths through thermodynamic state space: geodesics are the most efficient thermodynamic processes."

Corrected:
> Geodesics of the Ruppeiner/Weinhold metric minimise dissipated availability only for slow, endoreversible processes with a given mean relaxation time (Salamon & Berry 1983, ΔE ≥ ε̄ℓ²/τ). For slow driving in general, the optimal paths are geodesics of the friction tensor ζ = k_BT τ∘I, which is this metric times a constant only when the relaxation time is constant (Sivak & Crooks 2012).

### Docs (not the DB)

**22. `docs/ALPHAENTROPY_GEODESIC_TEST_SPEC.md`.**
- Rows 17–18 repeat IT06's sentence.
- Line 273 says "Seifert's framework predicts that the MINIMUM dissipation path should be the same in both directions".
- Line 484 says "Seifert minimum-dissipation applies to financial markets in the fast-shock limit".

Proposal: a dated banner at the top pointing to items 13–14 and 20, with the body unchanged. Historical handovers (e.g. `SESSION_HANDOVER_2026-04-03.md` line 30) are left alone.

## 4. Calibration rows (append-only, `wiki_history.db`)

| Entity | Proposed row | Effect on counts |
|---|---|---|
| **P21** | Established (**unchanged**), audit_ref `gsw-it06-geodesic-check-2026-10-18`. Short status: "Classical Chentsov uniqueness + quantum Petz classification; instance (4) withdrawn — slow-driving dissipation metric is the friction tensor (Sivak & Crooks 2012), Fisher–Rao only for constant relaxation time". Precedent: the P15 row in QR-004 (label unchanged). | none |
| fisher_gravity_chain | **No row.** It does not depend on IT06. | none |
| IT06, X8, BR04 | **No row by default.** These are wording corrections, and the core of IT06 is Established textbook material. | none |
| *Option* X8 | Add X8 as a tracked claim, Speculative ("analogy-motivated proxy; geodesic test inapplicable"). | 48 claims; 27 Speculative |

Recommendation: the P21 row only.

## 5. Follow-ups (not in this pass)

- IT08 Mathematical Archetype: "the minimum variance of an estimator equals the inverse of the metric component, which is the geodesic distance squared in the parameter direction". Cramér–Rao is a bound, and the inverse Fisher information is not a squared geodesic distance.
- BR04: "The curvature measures the cost of deviating from optimal paths". Not supported by the sources read here; Ruppeiner reads |R| as a correlation volume.
- IT06 and X8 archetype labels: the text says "conservation-law" but describes monotonicity. Both entries are already `KNOWN_UNTAGGED`.
- X8 `entries.status = 'established'` for a proxy (the entries table is not edited).

## 6. Migration plan (after approval)

`scripts/migrations/it06_geodesic_check_2026_10_18.py`, modelled on `qr004_corrections_2026_10_18.py`:
- dry run by default, `--apply` to write;
- banners appended after the original text;
- each target matched by an exact quote, aborting if a quote matches zero or more than one place or a target appears twice;
- idempotent (it skips anything that already carries the audit_ref);
- the P21 row inserted with INSERT OR IGNORE;
- read-back verification.

Then `python3 -m src.sync`, commit, the tests, and `git checkout -- data/chroma_db/chroma.sqlite3`, in that order. No push.

# Glossary Lint — Punch List

- Total findings scanned: 1533
- Problems flagged: 1533
- Entries needing attention: 166

Each finding is a load-bearing word that appears in prose without either `[[g:slug]]` markup OR a 'Here, X means ...'-style binding in the same section. The lint is a candidate-surfacer, not a verdict — some flagged usages are fine (well-known phrases in context). Triage manually.

---

## IT06  (55 flags)

**Section: What It Claims**

- ⚠️ `Fisher-Rao` — 'reverse. Stochastic thermodynamics further reveals that the Fisher-Rao metric governs the geometry of optimal non-equilibrium proc'
- ⚠️ `Fisher-Rao` — 'ion paths between thermodynamic states are geodesics on the Fisher-Rao manifold of probability distributions, connecting non-equil'
- ⚠️ `information geometry` — 'ions, connecting non-equilibrium thermodynamics directly to information geometry.'
- · `entropy` — 'rocess described by a trajectory x(t), the trajectory-level entropy production is s_tot[x(t)] = log[P_F[x(t)] / P_R[x̃(t)]], wh'
- · `entropy` — ' as special cases by setting s_tot = β(W − ΔF). The average entropy production equals the KL divergence between forward and rev'
- · `entropy` — ' This is the information-theoretic proof of the second law: entropy production is non-negative because KL divergence is non-neg'
- · `fluctuation` — 'ides the microscopic framework unifying all non-equilibrium fluctuation theorems under a single information-theoretic identity. For'
- · `fluctuation` — 'eversed trajectory under the reverse protocol. The integral fluctuation theorem ⟨e^{−s_tot}⟩ = 1 holds exactly for any stochastic p'
- · `fluctuation` — 'y stochastic process, and the Jarzynski equality and Crooks fluctuation theorem follow as special cases by setting s_tot = β(W − ΔF'

**Section: Mathematical Form**

- ⚠️ `Fisher-Rao` — 'try):   ⟨W_diss⟩ ≥ (1/τ) ∫ g_ij λ̇^i λ̇^j dt   where g_ij = Fisher-Rao metric on parameter space   Equality: minimum-dissipation p'
- ⚠️ `Fisher-Rao` — 'space   Equality: minimum-dissipation path is a geodesic on Fisher-Rao manifold'
- · `entropy` — 'Trajectory entropy production:   s_tot[x(t)] = log[ P_F[x(t)] / P_R[x̃(t)] ]  '
- · `symmetry` — '              (detailed fluctuation theorem / time-reversal symmetry)  Minimum dissipation (thermodynamic geometry):   ⟨W_diss⟩ '
- · `fluctuation` — 'on:   s_tot[x(t)] = log[ P_F[x(t)] / P_R[x̃(t)] ]  Integral fluctuation theorem (master identity):   ⟨e^{−s_tot}⟩ = 1   (exact, any'
- · `fluctuation` — '(s_tot = a) / P_R(s_tot = −a) = e^a               (detailed fluctuation theorem / time-reversal symmetry)  Minimum dissipation (the'

**Section: Constraint Category**

- ⚠️ `Fisher-Rao` — 'f D_KL ≥ 0 instantiated in different physical settings. The Fisher-Rao metric (IT08) connection shows that information geometry go'
- ⚠️ `Fisher-Rao` — 'hem: dissipation is minimised by following geodesics on the Fisher-Rao manifold.'
- ⚠️ `information geometry` — 'ettings. The Fisher-Rao metric (IT08) connection shows that information geometry governs not just the statistics of thermodynamic states but'
- · `entropy` — ' about distinguishability of probability distributions. The entropy production s_tot = log(P_F/P_R) is the log-likelihood ratio'
- · `connection` — 'n different physical settings. The Fisher-Rao metric (IT08) connection shows that information geometry governs not just the statis'
- · `fluctuation` — 'e second law, the Jarzynski equality (NE03), and the Crooks fluctuation theorem (NE04) — all are consequences of D_KL ≥ 0 instantia'

**Section: DS Cross-References**

- ⚠️ `Fisher-Rao` — ' the general framework from which Crooks is derived). IT08 (Fisher-Rao Metric — minimum-dissipation non-equilibrium processes are '
- ⚠️ `Fisher-Rao` — '-dissipation non-equilibrium processes are geodesics on the Fisher-Rao manifold; the Fisher metric governs the thermodynamic cost '
- ⚠️ `information geometry` — 'mic cost of non-equilibrium driving at rate 1/τ, connecting information geometry to entropy production). GT07 (Non-Equilibrium Spacetime The'
- · `entropy` — '|P_R) ≥ 0 is the fundamental identity connecting stochastic entropy production to KL divergence; the second law IS KL non-negat'
- · `entropy` — 'e detailed fluctuation symmetry P_F(a)/P_R(−a) = e^a of the entropy production distribution; stochastic thermodynamics is the g'
- · `entropy` — 'ium driving at rate 1/τ, connecting information geometry to entropy production). GT07 (Non-Equilibrium Spacetime Thermodynamics'
- · `entropy` — 'on-Equilibrium Spacetime Thermodynamics — the gravitational entropy production rate σ in Chirco-Liberati is the continuous spac'
- · `entropy` — " is the continuous spacetime analog of Seifert's trajectory entropy production s_tot; both provide the non-equilibrium correcti"
- · `symmetry` — 'tion Theorem — Crooks follows from the detailed fluctuation symmetry P_F(a)/P_R(−a) = e^a of the entropy production distribution'
- · `fluctuation` — 'econd law IS KL non-negativity at the trajectory level; all fluctuation theorems follow from this single information-theoretic fact'
- · `fluctuation` — '3 (Jarzynski Equality — Jarzynski follows from the integral fluctuation theorem ⟨e^{−s_tot}⟩ = 1 by setting s_tot = β(W − ΔF); stoc'
- · `Fluctuation` — ' proof that ⟨W_diss⟩ = D_KL(P_F||P_R) × k_BT). NE04 (Crooks Fluctuation Theorem — Crooks follows from the detailed fluctuation symm'
- · `fluctuation` — 'ooks Fluctuation Theorem — Crooks follows from the detailed fluctuation symmetry P_F(a)/P_R(−a) = e^a of the entropy production dis'

**Section: Mathematical Archetype**

- ⚠️ `Fisher-Rao` — 'geometric interpretation (minimum dissipation = geodesic on Fisher-Rao manifold) adds a geometric layer: entropy production measur'
- · `entropy` — 'ity framework: ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0. The trajectory entropy production s_tot is a stochastic variable that can be negat'
- · `entropy` — ' = geodesic on Fisher-Rao manifold) adds a geometric layer: entropy production measures deviation from the geodesic path throug'
- ⚠️ `monotonicity` — 'archetype: conservation-law  Stochastic thermodynamics is a monotonicity framework: ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0. The trajectory ent'
- · `fluctuation` — 'ate the second law) but has non-negative mean. The integral fluctuation theorem ⟨e^{−s_tot}⟩ = 1 is the exact master identity; Jens'
- · `fluctuation` — ' ≥ 0 immediately. The framework unifies all non-equilibrium fluctuation theorems — Jarzynski, Crooks, the fluctuation-dissipation t'
- · `fluctuation` — 'n-equilibrium fluctuation theorems — Jarzynski, Crooks, the fluctuation-dissipation theorem — as consequences of this single exact '

**Section: What The Math Says**

- ⚠️ `Fisher-Rao` — 'ion result follows from the Cramér-Rao bound applied to the Fisher-Rao metric on the space of thermodynamic states: the fastest pa'
- · `entropy` — "on. Jensen's inequality then gives the second law: the mean entropy production ⟨s_tot⟩ is non-negative. Setting s_tot = β(W − Δ"
- · `entropy` — 'diss⟩ ≥ 0. Taking the ratio of the probability of observing entropy production a to the probability of observing −a gives the C'
- · `Entropy` — ' divergence between forward and reverse path distributions. Entropy production measures how distinguishable the forward process'
- · `entropy` — 'ynamic states: the fastest path between states with minimum entropy production is a geodesic, with dissipation proportional to '
- · `symmetry` — 'tio that a statistician would compute to test time-reversal symmetry. The minimum-dissipation result follows from the Cramér-Rao'
- · `fluctuation` — 'k, briefly, like they violate the second law). The integral fluctuation theorem states that the exponential average of −s_tot equal'

**Section: Concept Tags**

- ⚠️ `Fisher-Rao` — 'ic thermodynamics • Crooks from stochastic thermodynamics • Fisher-Rao metric and minimum dissipation • information geometry of no'
- ⚠️ `information geometry` — 'hermodynamics • Fisher-Rao metric and minimum dissipation • information geometry of non-equilibrium • log-likelihood ratio • thermodynamic i'
- · `entropy` — '• stochastic thermodynamics • trajectory entropy production • integral fluctuation theorem • detailed fluctu'
- · `entropy` — ' theorem • detailed fluctuation theorem • KL divergence and entropy production • time-reversal symmetry • non-equilibrium work '
- · `symmetry` — 'orem • KL divergence and entropy production • time-reversal symmetry • non-equilibrium work • Jarzynski from stochastic thermody'
- · `fluctuation` — 'c thermodynamics • trajectory entropy production • integral fluctuation theorem • detailed fluctuation theorem • KL divergence and '
- · `fluctuation` — 'ntropy production • integral fluctuation theorem • detailed fluctuation theorem • KL divergence and entropy production • time-rever'

---

## HB09  (53 flags)

**Section: What It Claims**

- · `entropy` — 'The Generalised Second Law (GSL) states that the total entropy S_total = S_matter + S_BH never decreases: dS_total/dt ≥ 0,'
- · `entropy` — ', where S_BH = A/4l_P² is the Bekenstein-Hawking black hole entropy and S_matter is the von Neumann entropy S(ρ) = −Tr(ρ log ρ)'
- · `entropy` — '-Hawking black hole entropy and S_matter is the von Neumann entropy S(ρ) = −Tr(ρ log ρ) of quantum fields outside the event hor'
- · `entropy` — 'en when matter falls into a black hole reducing the visible entropy, the event horizon area grows to compensate. The GSL is the'
- ⚠️ `monotonicity` — 'ify them as special cases of a single information-theoretic monotonicity constraint.'
- · `fluctuation` — 'zynski equality ⟨e^{−W/k_BT}⟩ = e^{−ΔF/k_BT} and the Crooks fluctuation theorem, which quantify irreversibility via exponential ave'
- · `fluctuation` — 'tial averages of non-equilibrium work. Both the GSL and the fluctuation theorems are consequences of the non-negativity of KL diver'
- · `fluctuation` — ' in non-equilibrium thermodynamics. A quantum gravitational fluctuation theorem — extending the Crooks relation to black hole proce'

**Section: Mathematical Form**

- · `entropy` — '/ (4 l_P²)  where:   S_matter = −Tr(ρ log ρ)  — von Neumann entropy of exterior quantum fields   A         — event horizon area'
- · `entropy` — 'm: dA/dt ≥ 0)   l_P = √(ℏG/c³)  — Planck length  Bekenstein entropy bound: S_matter ≤ 2πER/ℏc (matter entropy bounded by energy'
- · `entropy` — 'ength  Bekenstein entropy bound: S_matter ≤ 2πER/ℏc (matter entropy bounded by energy E and linear size R)  Limiting cases:   G'
- · `Fluctuation` — 'm)   GSL → Second Law            (A fixed, flat spacetime)  Fluctuation theorem parallel:   Crooks: P_F(W) / P_R(−W) = exp((W − ΔF)'

**Section: Constraint Category**

- · `entropy` — 'ic (Th-Gm): The GSL combines thermodynamic irreversibility (entropy non-decrease) with geometric monotonicity (event horizon ar'
- · `entropy` — ' the non-equilibrium case, and the equivalent gravitational entropy balance in the black hole case. A quantum gravitational flu'
- ⚠️ `monotonicity` — 'namic irreversibility (entropy non-decrease) with geometric monotonicity (event horizon area non-decrease). It is the gravitational '
- ⚠️ `monotonicity` — 'ify them as two instances of the same information-theoretic monotonicity constraint, bridging non-equilibrium thermodynamics and bla'
- · `fluctuation` — "ki dissipation bound ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 and the Crooks fluctuation theorem's non-equilibrium work asymmetry. All three — the G"
- · `fluctuation` — 'All three — the GSL, the Jarzynski equality, and the Crooks fluctuation theorem — are manifestations of the non-negativity of KL di'
- · `fluctuation` — 'opy balance in the black hole case. A quantum gravitational fluctuation theorem extending the Crooks relation P_F(W)/P_R(−W) = exp('

**Section: DS Cross-References**

- · `entropy` — ' dA/dt ≥ 0: quantum fields allow area to decrease if matter entropy compensates; the area theorem is the classical vacuum limit'
- · `entropy` — '} is the microscopic fluctuation-theorem version of the GSL entropy balance; Jarzynski follows by exponential averaging over th'
- · `Entropy` — 'ing over the Crooks distribution). HB02 (Bekenstein-Hawking Entropy — S_BH = A/4l_P² is the gravitational entropy term in the G'
- · `entropy` — 'stein-Hawking Entropy — S_BH = A/4l_P² is the gravitational entropy term in the GSL; the GSL asserts this quantity plus matter '
- · `entropy` — ' term in the GSL; the GSL asserts this quantity plus matter entropy is non-decreasing). IT03 (KL Divergence — D_KL(p||q) ≥ 0 is'
- · `entropy` — 'spacetime; the Second Law is the GSL with the gravitational entropy term removed).'
- · `fluctuation` — '3 (Jarzynski Equality — ⟨W_diss⟩ ≥ 0 is the non-equilibrium fluctuation-theorem counterpart of dS_total ≥ 0; both are irreversibili'
- · `fluctuation` — 'ng to KL divergence non-negativity; a quantum gravitational fluctuation theorem would unify them). NE04 (Crooks Fluctuation Theorem'
- · `Fluctuation` — 'ational fluctuation theorem would unify them). NE04 (Crooks Fluctuation Theorem — the Crooks ratio P_F(W)/P_R(−W) = e^{β(W−ΔF)} is '
- · `fluctuation` — 'rooks ratio P_F(W)/P_R(−W) = e^{β(W−ΔF)} is the microscopic fluctuation-theorem version of the GSL entropy balance; Jarzynski follo'

**Section: Mathematical Archetype**

- · `relative entropy` — 'asing) and the KL divergence non-negativity D_KL(p||q) ≥ 0 (relative entropy is always positive). The monotonicity is saturated at rever'
- · `entropy` — " type as the Second Law and Hawking's area theorem: a total entropy functional S_total = S_matter + A/4l_P² is non-decreasing u"
- · `entropy` — '4l_P² is non-decreasing under time evolution. Gravitational entropy (area) and matter entropy trade off — any process decreasin'
- · `entropy` — 'der time evolution. Gravitational entropy (area) and matter entropy trade off — any process decreasing one must increase the ot'
- · `entropy` — 'd the KL divergence non-negativity D_KL(p||q) ≥ 0 (relative entropy is always positive). The monotonicity is saturated at rever'
- ⚠️ `monotonicity` — 'atical archetype: conservation-law  The GSL is an extensive monotonicity constraint of the same structural type as the Second Law an'
- ⚠️ `monotonicity` — 'y D_KL(p||q) ≥ 0 (relative entropy is always positive). The monotonicity is saturated at reversibility: GSL equality holds for quasi'

**Section: What The Math Says**

- · `entropy` — 'Throw matter with von Neumann entropy S_matter into a black hole. The exterior entropy decreases '
- · `entropy` — 'on Neumann entropy S_matter into a black hole. The exterior entropy decreases by S_matter. The event horizon area grows by at l'
- · `entropy` — 'grows by at least 4l_P² × S_matter — the Bekenstein-Hawking entropy increases by at least S_matter. The GSL dS_total/dt ≥ 0 is '
- · `entropy` — 'tal/dt ≥ 0 is satisfied: gravitational geometry absorbs the entropy loss of infalling matter.  The structural parallel to the J'
- · `entropy` — 'pated work ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 is always non-negative — entropy is produced in the environment. In both cases, a total entr'
- · `entropy` — 'ropy is produced in the environment. In both cases, a total entropy budget is non-decreasing: matter + horizon entropy in the g'
- · `entropy` — ' a total entropy budget is non-decreasing: matter + horizon entropy in the gravitational case, system + environment entropy in '
- · `entropy` — 'zon entropy in the gravitational case, system + environment entropy in the thermodynamic case.  Both the GSL and the Jarzynski/'
- · `entropy` — ' ≥ 0. The gravitational analog would express the black hole entropy balance as a KL divergence between forward (infall) and tim'
- · `fluctuation` — 'follow from the same mathematical fact: D_KL(p||q) ≥ 0. For fluctuation theorems: D_KL(p_forward||p_reverse) = ⟨W_diss⟩/k_BT ≥ 0. T'

**Section: Concept Tags**

- · `entropy` — '• generalised second law • GSL • black hole entropy • Bekenstein-Hawking entropy • event horizon area • gravita'
- · `entropy` — ' second law • GSL • black hole entropy • Bekenstein-Hawking entropy • event horizon area • gravitational second law • area theo'
- · `entropy` — 'dissipated work • quantum fluctuation theorem • von Neumann entropy • KL divergence • entropy monotonicity • irreversibility • '
- · `entropy` — 'fluctuation theorem • von Neumann entropy • KL divergence • entropy monotonicity • irreversibility • thermodynamic irreversibil'
- ⚠️ `monotonicity` — 'ion theorem • von Neumann entropy • KL divergence • entropy monotonicity • irreversibility • thermodynamic irreversibility • forward'
- · `fluctuation` — 'on-equilibrium thermodynamics • Jarzynski equality • Crooks fluctuation theorem • dissipated work • quantum fluctuation theorem • v'
- · `fluctuation` — 'ty • Crooks fluctuation theorem • dissipated work • quantum fluctuation theorem • von Neumann entropy • KL divergence • entropy mon'

---

## IT04  (51 flags)

**Section: What It Claims**

- ⚠️ `Fisher information` — ' destroy the distinguishability between states. The quantum Fisher information emerges as the Hessian of quantum relative entropy, linking'
- · `relative entropy` — 'Quantum relative entropy S(ρ||σ) = Tr(ρ log ρ − ρ log σ) is the quantum generalisati'
- · `relative entropy` — 'uantum Fisher information emerges as the Hessian of quantum relative entropy, linking quantum information geometry to gravitational dyna'
- ⚠️ `information geometry` — "as the Hessian of quantum relative entropy, linking quantum information geometry to gravitational dynamics in frameworks such as Bianconi's."
- · `entropy` — 'Quantum relative entropy S(ρ||σ) = Tr(ρ log ρ − ρ log σ) is the quantum generalisati'
- · `entropy` — 'sher information emerges as the Hessian of quantum relative entropy, linking quantum information geometry to gravitational dyna'
- ⚠️ `monotonicity` — 'serving maps — the quantum data processing inequality. This monotonicity is the deepest formulation of the second law of quantum the'

**Section: Mathematical Form**

- ⚠️ `Fisher information` — "ps)  Pinsker's inequality: ||ρ − σ||₁² ≤ 2 S(ρ||σ)  Quantum Fisher information: g_ij^Q = −∂²S(ρ_θ||ρ_{θ₀})/∂θ^i∂θ^j |_{θ=θ₀}"
- ⚠️ `monotonicity` — "ality)   S(ρ||σ) = 0  iff ρ = σ   S(Φ(ρ)||Φ(σ)) ≤ S(ρ||σ)  (monotonicity under CPTP maps)  Pinsker's inequality: ||ρ − σ||₁² ≤ 2 S(ρ"

**Section: Constraint Category**

- · `relative entropy` — 'Informatic (In): The monotonicity of quantum relative entropy under quantum channels (CPTP maps) is the master inequality'
- · `relative entropy` — 'n the classical limit (commuting density matrices), quantum relative entropy reduces exactly to the Kullback-Leibler divergence, and the'
- · `entropy` — 'Informatic (In): The monotonicity of quantum relative entropy under quantum channels (CPTP maps) is the master inequality'
- · `entropy` — 'tion theory. It implies strong subadditivity of von Neumann entropy, the quantum data processing inequality, and the second law'
- · `entropy` — 'ssical limit (commuting density matrices), quantum relative entropy reduces exactly to the Kullback-Leibler divergence, and the'
- ⚠️ `monotonicity` — 'Informatic (In): The monotonicity of quantum relative entropy under quantum channels (CPTP ma'

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — ' relative entropy against the maximally mixed state). IT05 (Fisher Information — quantum Fisher information is the Hessian of quantum rela'
- ⚠️ `Fisher information` — ' maximally mixed state). IT05 (Fisher Information — quantum Fisher information is the Hessian of quantum relative entropy, the infinitesim'
- ⚠️ `Fisher information` — " Bianconi's framework uses quantum relative entropy and its Fisher information to derive gravitational dynamics from information geometry)"
- · `relative entropy` — 'IT03 (KL Divergence — quantum relative entropy generalises KL divergence to non-commutative quantum states'
- · `relative entropy` — '(ρ||I/d) + log d; von Neumann entropy is related to quantum relative entropy against the maximally mixed state). IT05 (Fisher Informatio'
- · `relative entropy` — 'tion — quantum Fisher information is the Hessian of quantum relative entropy, the infinitesimal geometry of quantum state space). GT04 ('
- · `relative entropy` — "ni Gravity from Entropy — Bianconi's framework uses quantum relative entropy and its Fisher information to derive gravitational dynamics"
- ⚠️ `information geometry` — 'ts Fisher information to derive gravitational dynamics from information geometry).'
- · `entropy` — 'IT03 (KL Divergence — quantum relative entropy generalises KL divergence to non-commutative quantum states'
- · `Entropy` — 'neously diagonalisable density matrices). IT02 (Von Neumann Entropy — S(ρ) = −S(ρ||I/d) + log d; von Neumann entropy is related'
- · `entropy` — 'on Neumann Entropy — S(ρ) = −S(ρ||I/d) + log d; von Neumann entropy is related to quantum relative entropy against the maximall'
- · `entropy` — '+ log d; von Neumann entropy is related to quantum relative entropy against the maximally mixed state). IT05 (Fisher Informatio'
- · `entropy` — 'antum Fisher information is the Hessian of quantum relative entropy, the infinitesimal geometry of quantum state space). GT04 ('
- · `Entropy` — "ometry of quantum state space). GT04 (Bianconi Gravity from Entropy — Bianconi's framework uses quantum relative entropy and it"
- · `entropy` — "y from Entropy — Bianconi's framework uses quantum relative entropy and its Fisher information to derive gravitational dynamics"

**Section: Mathematical Archetype**

- · `relative entropy` — 'Mathematical archetype: thermodynamic-bound  Quantum relative entropy is the quantum master bound: non-negative, monotone under p'
- ⚠️ `information geometry` — 'ty), the data processing inequality (information loss), and information geometry (curvature of state space) into a single mathematical objec'
- · `entropy` — 'thematical archetype: thermodynamic-bound  Quantum relative entropy is the quantum master bound: non-negative, monotone under p'

**Section: What The Math Says**

- ⚠️ `Fisher information` — 'he square root of twice their relative entropy. The quantum Fisher information matrix g-ij-Q is the negative Hessian of quantum relative e'
- ⚠️ `Fisher-Rao` — 'on the space of quantum states — the quantum version of the Fisher-Rao metric.'
- · `relative entropy` — 'Quantum relative entropy of rho with respect to sigma equals the trace of rho times '
- · `relative entropy` — 'ny quantum channel Phi to both states cannot increase their relative entropy, meaning S of Phi-rho given Phi-sigma is at most S of rho g'
- · `relative entropy` — 'stance between two states by the square root of twice their relative entropy. The quantum Fisher information matrix g-ij-Q is the negati'
- · `relative entropy` — 'nformation matrix g-ij-Q is the negative Hessian of quantum relative entropy, making it the natural Riemannian metric on the space of qu'
- · `entropy` — 'Quantum relative entropy of rho with respect to sigma equals the trace of rho times '
- · `entropy` — 'm channel Phi to both states cannot increase their relative entropy, meaning S of Phi-rho given Phi-sigma is at most S of rho g'
- · `entropy` — 'tween two states by the square root of twice their relative entropy. The quantum Fisher information matrix g-ij-Q is the negati'
- · `entropy` — 'n matrix g-ij-Q is the negative Hessian of quantum relative entropy, making it the natural Riemannian metric on the space of qu'
- ⚠️ `monotonicity` — 'only when the two states are identical. The key property is monotonicity: applying any quantum channel Phi to both states cannot inc'

**Section: Concept Tags**

- ⚠️ `Fisher information` — 'um data processing inequality • CPTP monotonicity • quantum Fisher information • quantum second law • Pinsker inequality • quantum state d'
- · `relative entropy` — '• quantum relative entropy • Umegaki relative entropy • Klein inequality • quantum dat'
- · `relative entropy` — '• quantum relative entropy • Umegaki relative entropy • Klein inequality • quantum data processing inequality • C'
- ⚠️ `information geometry` — 'w • Pinsker inequality • quantum state distinguishability • information geometry'
- · `entropy` — '• quantum relative entropy • Umegaki relative entropy • Klein inequality • quantum dat'
- · `entropy` — '• quantum relative entropy • Umegaki relative entropy • Klein inequality • quantum data processing inequality • C'
- ⚠️ `monotonicity` — 'lein inequality • quantum data processing inequality • CPTP monotonicity • quantum Fisher information • quantum second law • Pinsker'

---

## GT04  (46 flags)

**Section: What It Claims**

- ⚠️ `Fisher information` — 'termined by the quantum relative entropy and its associated Fisher information metric (Bianconi, PRD 111, 066001, 2025). The key insight i'
- ⚠️ `Fisher information` — 'k defines a natural distance, and its Hessian — the quantum Fisher information matrix — defines a Riemannian metric on the space of quantu'
- ⚠️ `Fisher information` — "ce of quantum states. **Disambiguation (2026-05-04):** the 'Fisher information matrix' here is the QUANTUM Fisher information / Bures metr"
- ⚠️ `Fisher information` — "-04):** the 'Fisher information matrix' here is the QUANTUM Fisher information / Bures metric on density matrices, governed by the Petz 19"
- ⚠️ `Fisher information` — 'um state space — both are gradient flows driven by the same Fisher information metric.'
- ⚠️ `Fisher-Rao` — 'unique self-dual, RLD the largest). It is NOT the classical Fisher-Rao metric on a parameter manifold of probability distributions'
- ⚠️ `Fisher-Rao` — 'rk therefore is not a continuous extension of the classical-Fisher-Rao parameter-space-compression programme (Sethna sloppy models'
- ⚠️ `Fisher-Rao` — 'l thermodynamics to quantum information geometry, using the Fisher-Rao metric as the bridge between information theory and spaceti'
- ⚠️ `Fisher-Rao` — "ormalisation group flow as Wasserstein gradient flow on the Fisher-Rao manifold, Bianconi's framework treats gravitational dynamic"
- · `relative entropy` — ' quantum states whose geometry is determined by the quantum relative entropy and its associated Fisher information metric (Bianconi, PRD'
- · `relative entropy` — 'PRD 111, 066001, 2025). The key insight is that the quantum relative entropy S(ρ||σ) between quantum states on a network defines a natur'
- ⚠️ `information geometry` — "oni's framework derives gravitational dynamics from quantum information geometry by treating spacetime as a network of quantum states whose "
- ⚠️ `information geometry` — 'manabhan programme from classical thermodynamics to quantum information geometry, using the Fisher-Rao metric as the bridge between informat'
- · `entropy` — 'states whose geometry is determined by the quantum relative entropy and its associated Fisher information metric (Bianconi, PRD'
- · `entropy` — '066001, 2025). The key insight is that the quantum relative entropy S(ρ||σ) between quantum states on a network defines a natur'

**Section: Mathematical Form**

- ⚠️ `Fisher information` — ' relative entropy: S(ρ||σ) = Tr(ρ log ρ − ρ log σ)  Quantum Fisher information metric:   g_ij^Q = −∂²S(ρ_θ||ρ_{θ₀})/∂θ^i ∂θ^j |_{θ=θ₀}  Em'
- ⚠️ `Fisher information` — ' |_{θ=θ₀}  Emergent curvature: R_ij ~ T_ij  (curvature from Fisher information   on the quantum network satisfies Einstein-like equations)'
- ⚠️ `Fisher-Rao` — 'ons)  Key structural equation:   Gravity = curvature of the Fisher-Rao metric on quantum state space'
- · `relative entropy` — 'Quantum relative entropy: S(ρ||σ) = Tr(ρ log ρ − ρ log σ)  Quantum Fisher informatio'
- · `entropy` — 'Quantum relative entropy: S(ρ||σ) = Tr(ρ log ρ − ρ log σ)  Quantum Fisher informatio'

**Section: Constraint Category**

- ⚠️ `Fisher information` — 'ramme: gravity (geometry) emerges from quantum information (Fisher information). The constraint structure is: quantum relative entropy → F'
- ⚠️ `Fisher information` — 'the informatic content (quantum states, distinguishability, Fisher information).'
- · `relative entropy` — ' (Fisher information). The constraint structure is: quantum relative entropy → Fisher metric → curvature → Einstein equations. The geome'
- · `entropy` — 'information). The constraint structure is: quantum relative entropy → Fisher metric → curvature → Einstein equations. The geome'

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — "||σ) is the starting point of Bianconi's derivation). IT05 (Fisher Information — the quantum Fisher information matrix, the Hessian of QRE"
- ⚠️ `Fisher information` — "nconi's derivation). IT05 (Fisher Information — the quantum Fisher information matrix, the Hessian of QRE, provides the emergent metric). "
- ⚠️ `Fisher-Rao` — 'x, the Hessian of QRE, provides the emergent metric). IT08 (Fisher-Rao Metric — the Fisher-Rao metric on quantum state space is th'
- ⚠️ `Fisher-Rao` — 'rovides the emergent metric). IT08 (Fisher-Rao Metric — the Fisher-Rao metric on quantum state space is the emergent spacetime met'
- · `Relative Entropy` — 'IT04 (Quantum Relative Entropy — the quantum relative entropy S(ρ||σ) is the starting poin'
- · `relative entropy` — "IT04 (Quantum Relative Entropy — the quantum relative entropy S(ρ||σ) is the starting point of Bianconi's derivation). IT"
- ⚠️ `emergent spacetime` — "etric — the Fisher-Rao metric on quantum state space is the emergent spacetime metric in Bianconi's framework). GT01 (Jacobson — Bianconi "
- ⚠️ `emergent spacetime` — "etric — the Fisher-Rao metric on quantum state space is the emergent spacetime metric in Bianconi's framework). GT01 (Jacobson — Bianconi "
- · `Entropy` — 'IT04 (Quantum Relative Entropy — the quantum relative entropy S(ρ||σ) is the starting poin'
- · `entropy` — "IT04 (Quantum Relative Entropy — the quantum relative entropy S(ρ||σ) is the starting point of Bianconi's derivation). IT"

**Section: Mathematical Archetype**

- ⚠️ `Fisher information` — 'stationarity condition for an action built from the quantum Fisher information metric — gravity is the geometry that extremises the inform'

**Section: What The Math Says**

- ⚠️ `Fisher information` — 'ers theta at a reference point theta-zero gives the quantum Fisher information matrix g-ij-Q — a positive-definite matrix that defines a R'
- · `relative entropy` — 'states, each described by a density matrix rho. The quantum relative entropy S of rho given sigma measures how distinguishable the two s'
- ⚠️ `information geometry` — 'd. Spacetime geometry and its curvature emerge from quantum information geometry on the network.'
- · `entropy` — 'ach described by a density matrix rho. The quantum relative entropy S of rho given sigma measures how distinguishable the two s'

**Section: Concept Tags**

- ⚠️ `Fisher information` — 'y • emergent spacetime • quantum relative entropy • quantum Fisher information • Fisher-Rao metric • network gravity • information-geometr'
- ⚠️ `Fisher-Rao` — 'e • quantum relative entropy • quantum Fisher information • Fisher-Rao metric • network gravity • information-geometric gravity • '
- · `relative entropy` — 'quantum information geometry • emergent spacetime • quantum relative entropy • quantum Fisher information • Fisher-Rao metric • network '
- ⚠️ `information geometry` — '• Bianconi gravity • quantum information geometry • emergent spacetime • quantum relative entropy • quantum F'
- ⚠️ `emergent spacetime` — '• Bianconi gravity • quantum information geometry • emergent spacetime • quantum relative entropy • quantum Fisher information • F'
- ⚠️ `emergent spacetime` — '• Bianconi gravity • quantum information geometry • emergent spacetime • quantum relative entropy • quantum Fisher information • F'
- · `entropy` — 'nformation geometry • emergent spacetime • quantum relative entropy • quantum Fisher information • Fisher-Rao metric • network '

---

## GT07  (40 flags)

**Section: What It Claims**

- · `entropy` — 'Clausius relation δQ = TdS assumes equilibrium: the horizon entropy changes reversibly, with zero internal entropy production. '
- · `entropy` — ' the horizon entropy changes reversibly, with zero internal entropy production. Eling, Guedens, and Jacobson (2006) showed this'
- · `entropy` — ' derivation requires a non-equilibrium correction term — an entropy production rate σ ≥ 0 on the horizon. The full non-equilibr'
- · `entropy` — 'ing of spacetime curvature fluctuations — plays the role of entropy production in the non-equilibrium extension, giving spaceti'
- · `entropy` — 'brium relation in the quasi-static limit. The gravitational entropy production rate σ is the spacetime analog of the dissipated'
- · `entropy` — "iss = ⟨W⟩ − ΔF in the Jarzynski equality and the trajectory entropy production s_tot = log[P_F/P_R] in Seifert's stochastic the"
- · `fluctuation` — 'e conceptual framework as the Jarzynski equality and Crooks fluctuation theorem — a thermodynamic identity valid for irreversible p'

**Section: Mathematical Form**

- · `entropy` — 'horizon   T  = Unruh temperature = ℏa/2πck_B   dS = horizon entropy change   σ  ≥ 0  = internal entropy production rate (from h'
- · `entropy` — 'a/2πck_B   dS = horizon entropy change   σ  ≥ 0  = internal entropy production rate (from horizon shear)  Raychaudhuri equation'
- · `entropy` — 'ν + ω_μν ω^μν − R_μν k^μ k^ν   (shear tensor σ_μν terms are entropy-producing)  Equilibrium limit (σ = 0) → Jacobson 1995:   δQ'

**Section: Constraint Category**

- · `entropy` — 'n irreversibility constraint on gravitational dynamics. The entropy production term σ ≥ 0 is the gravitational counterpart of t'
- · `entropy` — "iss⟩ ≥ 0 in the Jarzynski equality and the trajectory-level entropy production ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0 in Seifert's stocha"
- · `entropy` — 'ium thermodynamics (NE pillar) at the level of their shared entropy-production structure.'
- · `fluctuation` — ' reduces to an equilibrium identity (Clausius / Jarzynski / fluctuation theorem) in the reversible limit. The non-equilibrium exten'

**Section: DS Cross-References**

- · `entropy` — "rectly generalises Jacobson's equilibrium δQ = TdS; setting entropy production σ = 0 recovers exactly Jacobson's derivation and"
- · `entropy` — 'e non-equilibrium thermodynamic analog of the gravitational entropy production σ ≥ 0; both reduce to the equilibrium second law'
- · `entropy` — 'heorem — the full probability distribution of gravitational entropy production would obey a Crooks-type fluctuation symmetry; a'
- · `entropy` — 'IT06 (Seifert Stochastic Thermodynamics — the gravitational entropy production rate σ is the continuous-spacetime analog of Sei'
- · `entropy` — "e continuous-spacetime analog of Seifert's trajectory-level entropy production s_tot = log[P_F/P_R]; both provide the non-equil"
- · `symmetry` — 'nal entropy production would obey a Crooks-type fluctuation symmetry; a quantum gravitational fluctuation theorem extending Croo'
- · `Fluctuation` — 'uilibrium second law in the reversible limit). NE04 (Crooks Fluctuation Theorem — the full probability distribution of gravitationa'
- · `fluctuation` — 'f gravitational entropy production would obey a Crooks-type fluctuation symmetry; a quantum gravitational fluctuation theorem exten'
- · `fluctuation` — 'a Crooks-type fluctuation symmetry; a quantum gravitational fluctuation theorem extending Crooks to horizon processes is the outsta'

**Section: Mathematical Archetype**

- · `entropy` — 'acetime thermodynamic relation is a monotonicity law: total entropy (horizon entropy dS plus bulk entropy production σ) is non-'
- · `entropy` — 'amic relation is a monotonicity law: total entropy (horizon entropy dS plus bulk entropy production σ) is non-decreasing. The e'
- · `entropy` — 'notonicity law: total entropy (horizon entropy dS plus bulk entropy production σ) is non-decreasing. The entropy production ter'
- · `entropy` — 'y dS plus bulk entropy production σ) is non-decreasing. The entropy production term σ ≥ 0 is structurally identical to the Jarz'
- · `entropy` — "i dissipated-work bound W_diss ≥ 0 and Seifert's stochastic entropy production ⟨s_tot⟩ = D_KL(P_F||P_R) ≥ 0. All three are inst"
- · `entropy` — 'e are instances of the same monotonicity structure: a total entropy budget is non-decreasing under time evolution, with the pro'
- · `entropy` — ' to a reversible process; the non-equilibrium case produces entropy proportional to the irreversibility of the process.'
- ⚠️ `monotonicity` — '  The non-equilibrium spacetime thermodynamic relation is a monotonicity law: total entropy (horizon entropy dS plus bulk entropy pr'
- ⚠️ `monotonicity` — '⟩ = D_KL(P_F||P_R) ≥ 0. All three are instances of the same monotonicity structure: a total entropy budget is non-decreasing under t'

**Section: What The Math Says**

- · `entropy` — 'ions. Eling et al. (2006) showed that for f(R) gravity, the entropy of the horizon changes not just due to heat flux but also d'
- · `entropy` — ' changes not just due to heat flux but also due to internal entropy production σ from the shear of the null congruences generat'
- · `entropy` — ' a term −σ_μν σ^μν ≤ 0 that focusses the horizon, producing entropy. Setting σ = 0 (no shear, reversible horizon) recovers Jaco'
- · `entropy` — 'd gravity equations. Chirco and Liberati (2010) showed this entropy production is a gravitational viscosity: spacetime has an e'
- · `fluctuation` — "e outstanding open question is whether a full gravitational fluctuation theorem exists — extending Crooks' P_F(a)/P_R(−a) = e^a to "

**Section: Concept Tags**

- · `entropy` — 'rmodynamics • Jacobson derivation extension • gravitational entropy production • Clausius relation • horizon shear viscosity • '
- · `entropy` — ' • non-equilibrium Clausius • bulk viscosity of spacetime • entropy production rate • dissipated work analog • irreversible hor'
- · `fluctuation` — 'work analog • irreversible horizon dynamics • gravitational fluctuation theorem'

---

## HB02  (36 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'n the three-dimensional interior. This is the origin of the holographic principle. The Bekenstein-Hawking entropy has been reproduc'
- · `entropy` — 'The Bekenstein-Hawking entropy S_BH = A/4l_P² = Ak_Bc³/4Gℏ states that the entropy of a bl'
- · `entropy` — 'Hawking entropy S_BH = A/4l_P² = Ak_Bc³/4Gℏ states that the entropy of a black hole is proportional to the area of its event ho'
- · `entropy` — 'tum mechanics, and thermodynamics in a single equation. The entropy counts the number of microscopic quantum states consistent '
- · `entropy` — 'origin of the holographic principle. The Bekenstein-Hawking entropy has been reproduced by string theory microstate counting (S'
- · `entropy` — 'Vafa, 1996) and is now understood to equal the entanglement entropy — the von Neumann entropy S(ρ) = −Tr(ρ log ρ) of the reduce'
- · `entropy` — 'erstood to equal the entanglement entropy — the von Neumann entropy S(ρ) = −Tr(ρ log ρ) of the reduced density matrix — of quan'
- · `entropy` — ' thermal density matrix for the exterior, whose von Neumann entropy exactly equals A/4l_P². This identifies black hole entropy '
- · `entropy` — ' entropy exactly equals A/4l_P². This identifies black hole entropy as a quantum information quantity: it measures the entangle'

**Section: Constraint Category**

- · `entropy` — 'Thermodynamic-Geometric (Th-Gm): The BH entropy is simultaneously a thermodynamic quantity (it obeys the la'

**Section: DS Cross-References**

- ⚠️ `holographic` — 'horizons). HB07 (Ryu-Takayanagi — generalises BH entropy to holographic entanglement entropy in AdS/CFT).'
- · `Entropy` — 'IT02 (Von Neumann Entropy — BH entropy equals the entanglement entropy of quantum fie'
- · `entropy` — 'IT02 (Von Neumann Entropy — BH entropy equals the entanglement entropy of quantum fields across th'
- · `entropy` — '2 (Von Neumann Entropy — BH entropy equals the entanglement entropy of quantum fields across the horizon; the von Neumann entro'
- · `entropy` — 'tropy of quantum fields across the horizon; the von Neumann entropy of the exterior state). HB01 (Bekenstein Bound — BH entropy'
- · `entropy` — 'entropy of the exterior state). HB01 (Bekenstein Bound — BH entropy saturates the Bekenstein bound; black holes are maximally e'
- · `entropy` — 'ropic). HB04 (Hawking Radiation — Hawking radiation carries entropy away from the black hole at temperature T = ℏc³/8πGMk_B). H'
- · `entropy` — " showed that Einstein's equations follow from requiring the entropy-area proportionality to hold for all local causal horizons)"
- · `entropy` — 'cal causal horizons). HB07 (Ryu-Takayanagi — generalises BH entropy to holographic entanglement entropy in AdS/CFT).'
- · `entropy` — 'yanagi — generalises BH entropy to holographic entanglement entropy in AdS/CFT).'

**Section: Mathematical Archetype**

- ⚠️ `holography` — 'It bounds the information content of any region from above (holography), and its area-proportionality — rather than volume-proport'
- ⚠️ `holographic` — ' than volume-proportionality — is the defining signature of holographic physics. Every gravity-from-information programme ultimatel'
- · `entropy` — 'ematical archetype: thermodynamic-bound  Bekenstein-Hawking entropy is the prototype of a geometric entropy: a thermodynamic qu'
- · `entropy` — ' Bekenstein-Hawking entropy is the prototype of a geometric entropy: a thermodynamic quantity that equals a geometric measure ('

**Section: What The Math Says**

- · `entropy` — 'The entropy of a black hole equals the area of its event horizon A divi'
- · `entropy` — 'a is 16 pi G-squared M-squared over c-to-the-fourth, giving entropy 4 pi G M-squared k-B over h-bar c. This entropy is enormous'
- · `entropy` — 'rth, giving entropy 4 pi G M-squared k-B over h-bar c. This entropy is enormous: a solar-mass black hole has entropy roughly 10'
- · `entropy` — 'ar c. This entropy is enormous: a solar-mass black hole has entropy roughly 10-to-the-77 in units of k-B, far exceeding the ent'
- · `entropy` — 'opy roughly 10-to-the-77 in units of k-B, far exceeding the entropy of the pre-collapse star. The formula contains all four fun'

**Section: Concept Tags**

- ⚠️ `holographic` — 'tropy • black hole entropy • area-entropy proportionality • holographic entropy • Planck area • event horizon • entanglement entrop'
- · `entropy` — '• Bekenstein-Hawking entropy • black hole entropy • area-entropy proportionality • holog'
- · `entropy` — '• Bekenstein-Hawking entropy • black hole entropy • area-entropy proportionality • holographic entropy • Plan'
- · `entropy` — '• Bekenstein-Hawking entropy • black hole entropy • area-entropy proportionality • holographic entropy • Planck area • event'
- · `entropy` — 'k hole entropy • area-entropy proportionality • holographic entropy • Planck area • event horizon • entanglement entropy • four'
- · `entropy` — 'raphic entropy • Planck area • event horizon • entanglement entropy • four fundamental constants • microstate counting • geomet'
- · `entropy` — 'our fundamental constants • microstate counting • geometric entropy'

---

## BR04  (30 flags)

**Section: What It Claims**

- ⚠️ `Fisher-Rao` — 'f their fluctuation properties. The Ruppeiner metric IS the Fisher-Rao metric applied to the canonical Gibbs ensemble: thermodynam'
- ⚠️ `Fisher-Rao` — 'ry (IT) and gravity-thermodynamics (GT) by showing that the Fisher-Rao metric — the fundamental object of information geometry — a'
- ⚠️ `information geometry` — 'to the canonical Gibbs ensemble: thermodynamic geometry and information geometry are the same geometry. The curvature of the Ruppeiner metri'
- ⚠️ `information geometry` — 'wing that the Fisher-Rao metric — the fundamental object of information geometry — appears naturally in thermodynamic state space and, throu'
- · `entropy` — 'on thermodynamic state space as the negative Hessian of the entropy: g_ij = −∂²S/∂X^i ∂X^j, where the X^i are extensive variabl'
- · `fluctuation` — 'een states — how far apart two states are in terms of their fluctuation properties. The Ruppeiner metric IS the Fisher-Rao metric a'

**Section: Mathematical Form**

- ⚠️ `Fisher-Rao` — 've variables)  Relation: ds²_R = (1/T) ds²_W  Identity with Fisher-Rao:   g_ij^R = g_ij^{FR}(Gibbs)  for the canonical ensemble   '
- · `entropy` — 'iner metric: g_ij^R = −∂²S/∂X^i ∂X^j   (negative Hessian of entropy w.r.t. extensive variables)  Weinhold metric: g_ij^W = ∂²U/'
- · `entropy` — 'g_ij^W = ∂²U/∂S^i ∂S^j   (Hessian of internal energy w.r.t. entropy + extensive variables)  Relation: ds²_R = (1/T) ds²_W  Iden'

**Section: Constraint Category**

- ⚠️ `Fisher information` — 'nded by the inverse of the Ruppeiner metric component — the Fisher information sets the precision limit for thermodynamic parameter estima'
- ⚠️ `Fisher-Rao` — 'vature (phase transition signatures). The identity with the Fisher-Rao metric makes this simultaneously a geometric and informatio'
- ⚠️ `phase transition` — 'geodesics (optimal thermodynamic paths), and the curvature (phase transition signatures). The identity with the Fisher-Rao metric makes '

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'mic geometry and information geometry are identical). IT05 (Fisher Information — the Ruppeiner metric tensor is the Fisher information mat'
- ⚠️ `Fisher information` — '05 (Fisher Information — the Ruppeiner metric tensor is the Fisher information matrix for the canonical distribution, connecting thermodyn'
- ⚠️ `Fisher-Rao` — 'IT08 (Fisher-Rao Metric — the Ruppeiner metric IS the Fisher-Rao metric on t'
- ⚠️ `Fisher-Rao` — 'IT08 (Fisher-Rao Metric — the Ruppeiner metric IS the Fisher-Rao metric on the Gibbs canonical ensemble; thermodynamic geome'
- ⚠️ `information geometry` — 'on the Gibbs canonical ensemble; thermodynamic geometry and information geometry are identical). IT05 (Fisher Information — the Ruppeiner me'
- ⚠️ `information geometry` — "mbined with Ruppeiner's identification of thermodynamic and information geometry, suggests that spacetime geometry is ultimately information"
- ⚠️ `information geometry` — "on geometry, suggests that spacetime geometry is ultimately information geometry). GT04 (Bianconi — Bianconi's framework uses the Fisher met"
- · `entropy` — 'T03 (KL Divergence — the Ruppeiner metric is the Hessian of entropy, which is the Legendre transform of the Hessian of KL diver'

**Section: Mathematical Archetype**

- ⚠️ `Fisher-Rao` — 'c bridges information theory and thermodynamics through the Fisher-Rao identification.'

**Section: What The Math Says**

- ⚠️ `Fisher information` — 'n theta equals 1 over Z times exp of minus beta H of x, the Fisher information matrix g-ij-FR equals the expected value of the product of '
- ⚠️ `information geometry` — 'metric. This proves the identity: thermodynamic geometry IS information geometry for thermal systems. The curvature scalar R of the Ruppeine'
- · `entropy` — 'The Ruppeiner metric g-ij-R is the negative Hessian of entropy S with respect to extensive variables X-i and X-j. For a sy'
- · `entropy` — 'unctions, which evaluates to minus the second derivative of entropy with respect to extensive variables — exactly the Ruppeiner'

**Section: Concept Tags**

- ⚠️ `Fisher-Rao` — 'iner metric • thermodynamic geometry • Hessian of entropy • Fisher-Rao identity • phase transition curvature • Weinhold metric • t'
- ⚠️ `information geometry` — 'tion curvature • Weinhold metric • thermodynamic distance • information geometry of thermodynamics • geodesic thermodynamic path • fluctuati'
- · `entropy` — '• Ruppeiner metric • thermodynamic geometry • Hessian of entropy • Fisher-Rao identity • phase transition curvature • Weinho'
- ⚠️ `phase transition` — 'namic geometry • Hessian of entropy • Fisher-Rao identity • phase transition curvature • Weinhold metric • thermodynamic distance • info'
- · `fluctuation` — ' geometry of thermodynamics • geodesic thermodynamic path • fluctuation geometry'

---

## IT02  (30 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 't volume) of this entanglement entropy is the origin of the holographic principle — the quantum information content of a region is '
- · `entropy` — 'The von Neumann entropy S(ρ) = −Tr(ρ log ρ) is the quantum generalisation of Shanno'
- · `entropy` — '(ρ) = −Tr(ρ log ρ) is the quantum generalisation of Shannon entropy, measuring the information content — equivalently the degre'
- · `entropy` — "aximally mixed state of dimension d, S = log d. Von Neumann entropy quantifies entanglement: the entropy of a subsystem's reduc"
- · `entropy` — "S = log d. Von Neumann entropy quantifies entanglement: the entropy of a subsystem's reduced density matrix equals the entangle"
- · `entropy` — " subsystem's reduced density matrix equals the entanglement entropy between subsystem and environment. This makes it the bridge"
- · `entropy` — 'heory and black hole thermodynamics: the Bekenstein-Hawking entropy S_BH = A/4l_P² of a black hole equals the von Neumann entro'
- · `entropy` — 'tropy S_BH = A/4l_P² of a black hole equals the von Neumann entropy of the reduced density matrix obtained by tracing over the '
- · `entropy` — 'rea-proportionality S ∝ A (not volume) of this entanglement entropy is the origin of the holographic principle — the quantum in'

**Section: Mathematical Form**

- · `symmetry` — 'ure state |ψ⟩_AB:   S(ρ_A) = S(ρ_B)  (Schmidt decomposition symmetry)  Subadditivity: S(ρ_AB) ≤ S(ρ_A) + S(ρ_B) Strong subadditi'

**Section: Constraint Category**

- · `entropy` — 'Informatic (In): Von Neumann entropy is the unique measure of quantum uncertainty satisfying con'
- · `entropy` — 'completely positive trace-preserving map (quantum channel), entropy cannot decrease.'

**Section: DS Cross-References**

- · `Relative Entropy` — 'information to gravitational thermodynamics). IT04 (Quantum Relative Entropy — S(ρ||σ) = Tr(ρ log ρ − ρ log σ) generalises KL divergence'
- · `Entropy` — 'INFO1 (Shannon Entropy — von Neumann entropy reduces to Shannon entropy for diagon'
- · `entropy` — 'INFO1 (Shannon Entropy — von Neumann entropy reduces to Shannon entropy for diagonal density matrices; t'
- · `entropy` — '1 (Shannon Entropy — von Neumann entropy reduces to Shannon entropy for diagonal density matrices; the quantum-classical bridge'
- · `Entropy` — 'es; the quantum-classical bridge). HB02 (Bekenstein-Hawking Entropy — BH entropy equals entanglement entropy across the horizon'
- · `entropy` — 'um-classical bridge). HB02 (Bekenstein-Hawking Entropy — BH entropy equals entanglement entropy across the horizon, connecting '
- · `entropy` — 'Bekenstein-Hawking Entropy — BH entropy equals entanglement entropy across the horizon, connecting quantum information to gravi'
- · `Entropy` — 'on to gravitational thermodynamics). IT04 (Quantum Relative Entropy — S(ρ||σ) = Tr(ρ log ρ − ρ log σ) generalises KL divergence'
- · `entropy` — 'σ) generalises KL divergence to quantum states; von Neumann entropy is S(ρ||I/d) up to a constant). TD3 (Second Law — strong su'

**Section: Mathematical Archetype**

- · `entropy` — 'Mathematical archetype: thermodynamic-bound  Von Neumann entropy is bounded: 0 ≤ S(ρ) ≤ log d. The lower bound is saturated '
- ⚠️ `monotonicity` — 'he second law constrains thermodynamic processes — both are monotonicity statements about information processing.'

**Section: What The Math Says**

- · `entropy` — 'The von Neumann entropy of a quantum state described by density matrix rho equals m'
- · `entropy` — 's log lambda-i. For a pure state (single eigenvalue 1), the entropy is zero — there is no uncertainty. For a maximally mixed st'
- · `entropy` — 'ally mixed state of d dimensions (all eigenvalues 1/d), the entropy is log d — maximum uncertainty. For a bipartite pure state,'
- · `entropy` — 'm uncertainty. For a bipartite pure state, the entanglement entropy of subsystem A equals that of subsystem B — entanglement is'
- · `entropy` — 'ystem B — entanglement is symmetric. Subadditivity says the entropy of a joint system AB is at most the sum of entropies of A a'

**Section: Concept Tags**

- · `entropy` — '• von Neumann entropy • density matrix • quantum information • entanglement entro'
- · `entropy` — 'tropy • density matrix • quantum information • entanglement entropy • strong subadditivity • reduced density matrix • quantum c'

---

## GT03  (29 flags)

**Section: What It Claims**

- ⚠️ `holographic` — "Padmanabhan's holographic equipartition principle states that the expansion of the un"
- ⚠️ `holographic` — 'e between the number of degrees of freedom on the boundary (holographic surface) and in the bulk: dV/dt = l_P²(N_sur − N_bulk), whe'
- ⚠️ `holographic` — 'ntracts when the bulk has more. The universe evolves toward holographic equipartition: a state where N_sur = N_bulk and expansion h'
- ⚠️ `holographic` — 'of the expansion of the universe. The monotonic approach to holographic equipartition (N_bulk → N_sur as the universe expands) is t'
- ⚠️ `holographic` — ' RG scale, one along cosmic time. The monotonic approach to holographic equipartition (N_bulk → N_sur as the universe expands) is t'
- ⚠️ `monotonicity` — 'nse configurations to the present de Sitter epoch. Both are monotonicity/irreversibility theorems about degree-of-freedom counting u'
- ⚠️ `monotonicity` — 'nse configurations to the present de Sitter epoch. Both are monotonicity/irreversibility theorems about degree-of-freedom counting u'
- ⚠️ `coarse-graining` — 'freedom decreases monotonically under renormalisation group coarse-graining (c_UV ≥ c_IR), the bulk degrees of freedom N_bulk decrease '
- ⚠️ `coarse-graining` — 'rsibility theorems about degree-of-freedom counting under a coarse-graining flow — one along the RG scale, one along cosmic time. The m'
- ⚠️ `coarse-graining` — 'freedom decreases monotonically under renormalisation group coarse-graining (c_UV ≥ c_IR), the bulk degrees of freedom N_bulk decrease '
- ⚠️ `coarse-graining` — 'rsibility theorems about degree-of-freedom counting under a coarse-graining flow — one along the RG scale, one along cosmic time.'

**Section: Constraint Category**

- ⚠️ `holographic` — 'en by information disequilibrium. The monotonic approach to holographic equipartition (N_bulk → N_sur) parallels the monotonic decr'

**Section: DS Cross-References**

- ⚠️ `Holographic` — 'ic force by applying it to the cosmological horizon). HB03 (Holographic Principle — the N_sur term counts holographic degrees of fr'
- ⚠️ `holographic` — 'rizon). HB03 (Holographic Principle — the N_sur term counts holographic degrees of freedom on the boundary). RG04 (Zamolodchikov c-'
- ⚠️ `holographic` — "ixed volume is the microscopic foundation for Padmanabhan's holographic equipartition N_sur = N_bulk)."
- · `entropy` — 'condition delta_S_EE|_V = 0 for maximal vacuum entanglement entropy at fixed volume is the microscopic foundation for Padmanabh'

**Section: Mathematical Archetype**

- ⚠️ `Holographic` — 'Mathematical archetype: equilibrium-condition  Holographic equipartition is an equilibrium condition: the universe exp'
- ⚠️ `holographic` — 'boundary — a counting argument, not a force law. This makes holographic equipartition the cosmological c-theorem: just as the Zamol'
- · `entropy` — 'logical equilibrium, analogous to thermal equilibrium where entropy is maximised. The approach to equilibrium (expansion) is dr'
- ⚠️ `coarse-graining` — 's toward the initial state) are both instances of monotonic coarse-graining.'

**Section: What The Math Says**

- ⚠️ `holographic` — ': space expands. When N-sur equals N-bulk, expansion halts: holographic equipartition is achieved. This yields the standard Friedma'
- ⚠️ `holographic` — 'effective bulk degrees of freedom decreases relative to the holographic surface N-sur as the universe coarse-grains from its initia'
- ⚠️ `monotonicity` — ' its initial state toward de Sitter equipartition. Both are monotonicity theorems about irreversible coarse-graining: RG flow cannot'
- ⚠️ `coarse-graining` — 'artition. Both are monotonicity theorems about irreversible coarse-graining: RG flow cannot run backward (c increases), and cosmologica'

**Section: Concept Tags**

- ⚠️ `holographic` — '• holographic equipartition • Padmanabhan • cosmological expansion • degr'
- ⚠️ `coarse-graining` — 'theorem analog • monotonic decrease of degrees of freedom • coarse-graining flow • RG-cosmology duality • RG irreversibility • UV-IR an'
- ⚠️ `coarse-graining` — 'theorem analog • monotonic decrease of degrees of freedom • coarse-graining flow • RG-cosmology duality • RG irreversibility • UV-IR an'
- ⚠️ `duality` — 'of degrees of freedom • coarse-graining flow • RG-cosmology duality • RG irreversibility • UV-IR analogy • c-theorem analog • m'
- ⚠️ `duality` — 'of degrees of freedom • coarse-graining flow • RG-cosmology duality • RG irreversibility • UV-IR analogy'

---

## AM5  (28 flags)

**Section: What It Claims**

- · `symmetry` — 'Every continuous symmetry of the action corresponds to a conserved quantity. Time-tra'
- · `symmetry` — 'ction corresponds to a conserved quantity. Time-translation symmetry → energy conservation. Spatial-translation symmetry → momen'
- · `symmetry` — 'slation symmetry → energy conservation. Spatial-translation symmetry → momentum conservation. Rotational symmetry → angular mome'
- · `symmetry` — 'al-translation symmetry → momentum conservation. Rotational symmetry → angular momentum conservation. Gauge symmetry → charge co'
- · `symmetry` — ' Rotational symmetry → angular momentum conservation. Gauge symmetry → charge conservation. This theorem is the deepest explanat'
- · `symmetry` — 'ey are not independent axioms but consequences of geometric symmetry.'

**Section: Mathematical Form**

- · `symmetry` — 'Continuous symmetry of S ⟺ conserved Noether current J^μ with ∂_μ J^μ = 0'

**Section: Constraint Category**

- · `symmetry` — 'Geometric (Ge): symmetry is a geometric property of the action; the theorem maps sym'
- · `symmetry` — 'try is a geometric property of the action; the theorem maps symmetry groups to conservation laws. It is the backbone behind all '

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'um (CM4), charge (EM4). Ω_D: if physical constants run with D_eff, the time-translation symmetry is broken → energy may not b'
- · `symmetry` — ' if physical constants run with D_eff, the time-translation symmetry is broken → energy may not be globally conserved across sca'

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  A constraint derived from the geometric symme'
- · `symmetry` — "metry-conservation  A constraint derived from the geometric symmetry of a system or Hilbert space. Noether's theorem is the mast"
- · `symmetry` — "Noether's theorem is the master statement: every continuous symmetry of the action generates a conserved current. Discrete symme"
- · `symmetry` — 'aws for quantum numbers. The Pauli exclusion principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions'
- · `symmetry` — 'xchange, constraining the entire structure of matter. Gauge symmetry generates charge conservation via Noether. Topological symm'
- · `Symmetry` — 'ed topological invariants (winding numbers, Chern classes). Symmetry-conservation laws are D-sensitive when the relevant symmetr'
- · `symmetry` — 'ymmetry-conservation laws are D-sensitive when the relevant symmetry group changes with dimension — for instance, the rotation g'
- · `symmetry` — ' deepest explanation of conservation laws: every continuous symmetry of the action generates a conserved current. It is the math'
- · `symmetry` — "'s theorem applies to continuous symmetries of the action — symmetry groups change structure with D (e.g., rotation group SO(D) "

**Section: What The Math Says**

- · `symmetry` — "Noether's theorem states that every continuous symmetry of the action corresponds to a conserved Noether current J-"
- · `symmetry` — 'nce condition partial_mu J-mu equals zero. Time translation symmetry (H unchanged under t shifted to t plus epsilon) gives energ'
- · `symmetry` — 'lus epsilon) gives energy conservation; spatial translation symmetry gives momentum conservation; rotation symmetry gives angula'
- · `symmetry` — ' translation symmetry gives momentum conservation; rotation symmetry gives angular momentum conservation; U(1) phase symmetry gi'
- · `symmetry` — 'on symmetry gives angular momentum conservation; U(1) phase symmetry gives electric charge conservation. The theorem is construc'

**Section: Concept Tags**

- · `symmetry` — '• Noether theorem • symmetry and conservation • conserved current • continuous symmetry '
- · `symmetry` — ' symmetry and conservation • conserved current • continuous symmetry • energy conservation • momentum conservation • angular mom'
- · `symmetry` — 'angular momentum conservation • charge conservation • gauge symmetry'

---

## GT10  (28 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'yers 2016 (JHEP 03 (2016) 194; arXiv:1601.00528) showed via holographic calculation that THIS ASSUMPTION FAILS for relevant operato'
- ⚠️ `holographic` — '14) 051; arXiv:1312.7856) provides a parallel theorem-level holographic bridge from the boundary entanglement first law to LINEARIZ'
- · `entropy` — 'quation follows from the condition that vacuum entanglement entropy is maximal at fixed volume in all small geodesic balls. Thi'
- · `entropy` — 'y insight: for conformal matter, decompose the entanglement entropy of a small geodesic ball into an area term (Bekenstein-Hawk'
- · `entropy` — 'rity condition means: the area contribution to entanglement entropy (which wants to increase with curvature) is exactly balance'
- ⚠️ `modular Hamiltonian` — 'ry area A/4G) and a bulk term (the expectation value of the modular Hamiltonian K). If the vacuum state is stationary under first-order met'
- ⚠️ `modular Hamiltonian` — "4 deep-research pass):** Jacobson's derivation requires the modular Hamiltonian on a small geodesic ball to reduce to the boost generator. "

**Section: Mathematical Form**

- · `entropy` — 'Entanglement entropy decomposition in geodesic ball B:   S_EE(B) = S_area + S_bu'
- ⚠️ `modular Hamiltonian` — 'rea = (A/4G)(1 + delta_A/A)   S_bulk = <K>  (expectation of modular Hamiltonian)  Stationarity condition (maximal entanglement at fixed vol'

**Section: Constraint Category**

- ⚠️ `holographic` — 'the Ryu-Takayanagi formula (HB07) is promoted from a static holographic identity to a dynamical principle: the Einstein equation is'
- · `entropy` — 'on emerges as the condition for maximal vacuum entanglement entropy at fixed volume. This is an information-geometric constrain'
- · `entropy` — 'in G_ab) is determined by the requirement that entanglement entropy is extremal. No classical thermodynamic concepts (heat flux'
- · `connection` — 'straint is purely quantum-informatic. The area-entanglement connection from the Ryu-Takayanagi formula (HB07) is promoted from a s'

**Section: DS Cross-References**

- · `relative entropy` — "rgence — departure from maximal entanglement is measured by relative entropy; GT10's stationarity condition delta_S_EE = 0 is equivalent"
- ⚠️ `Holographic` — '016 entanglement-equilibrium derivation). GT03 (Padmanabhan Holographic Equipartition — N_sur = N_bulk is the global version of GT1'
- ⚠️ `holographic` — 'lement relation S = A/4G_N that GT10 promotes from a static holographic identity to a dynamical constraint determining spacetime ge'
- · `Entropy` — 't determining spacetime geometry). HB02 (Bekenstein-Hawking Entropy — S = A/4 emerges as the area contribution to entanglement '
- · `entropy` — ' — S = A/4 emerges as the area contribution to entanglement entropy in each geodesic ball; GT10 gives it a dynamical role). IT0'
- · `entropy` — "departure from maximal entanglement is measured by relative entropy; GT10's stationarity condition delta_S_EE = 0 is equivalent"

**Section: Mathematical Archetype**

- · `entropy` — ' equation is the condition for extremal vacuum entanglement entropy at fixed volume. This is a variational principle: among all'
- · `entropy` — 'me geometries, the physical geometry maximizes entanglement entropy in every small region. The optimization structure parallels'
- · `entropy` — 'ntity being extremized is quantum information (entanglement entropy) rather than a classical action functional.'

**Section: What The Math Says**

- · `entropy` — 'll are entangled with those outside. The total entanglement entropy has two contributions: an area term proportional to the bou'
- · `entropy` — 'hat if the vacuum state locally maximizes this entanglement entropy, holding the volume fixed? The answer: you get the Einstein'
- ⚠️ `modular Hamiltonian` — 'ng piece) and a bulk term capturing the matter content (the modular Hamiltonian expectation). Jacobson asks: what if the vacuum state local'

**Section: Concept Tags**

- ⚠️ `holographic` — ' • Ryu-Takayanagi dynamical • quantum information gravity • holographic entanglement • stationarity condition • informatic-geometri'
- · `entropy` — 'anglement equilibrium • Jacobson 2016 • vacuum entanglement entropy • modular Hamiltonian • geodesic ball • area-entanglement r'
- ⚠️ `modular Hamiltonian` — 'equilibrium • Jacobson 2016 • vacuum entanglement entropy • modular Hamiltonian • geodesic ball • area-entanglement relation • Einstein equ'

---

## NE02  (28 flags)

**Section: What It Claims**

- · `Entropy` — 'The Maximum Entropy Production Principle (MEPP) proposes that non-equilibrium s'
- · `entropy` — 'ady states will select the state that maximises the rate of entropy production, subject to the imposed constraints (Ziegler, 19'
- · `entropy` — "3; Martyushev & Seleznev, 2006). Unlike Prigogine's minimum entropy production theorem (valid only near equilibrium in the line"
- · `entropy` — 'ic justification (Dewar, 2003) connects MEPP to the maximum entropy principle (Jaynes): the most probable macroscopic state is '
- · `entropy` — 'e most microscopic realisations, which is the one producing entropy fastest. MEPP remains debated — it is not universally valid'
- · `connection` — 'and may apply only to specific classes of systems — but its connection to information theory and the second law makes it a key ent'

**Section: Mathematical Form**

- · `entropy` — 'τ / k_B)   (path probability proportional to exponential of entropy production)  Steady-state selection: among all states consi'

**Section: Constraint Category**

- · `entropy` — ' state) and an information-theoretic principle (the maximum entropy production state is the most probable state, connecting to '
- · `entropy` — "e is the most probable state, connecting to Jaynes' maximum entropy). The constraint is that among all possible dissipative con"
- · `entropy` — 'e configurations, nature selects the one that maximises the entropy production rate.'

**Section: DS Cross-References**

- · `entropy` — "NE01 (Prigogine — MEPP contrasts with Prigogine's minimum entropy production: Prigogine applies near equilibrium (linear), ME"
- · `entropy` — ' law but goes further: it selects not just the direction of entropy change but the rate). STAT1 (Maximum Entropy Principle — De'
- · `Entropy` — "e direction of entropy change but the rate). STAT1 (Maximum Entropy Principle — Dewar's justification connects MEPP to Jaynes' "
- · `entropy` — "ynes' MaxEnt: the most probable macroscopic state maximises entropy production, just as the most probable probability distribut"
- · `entropy` — "he most probable probability distribution maximises Shannon entropy). NE06 (England — England's dissipation-driven adaptation c"
- · `entropy` — ' a biological manifestation of MEPP: organisms that produce entropy faster are more likely to replicate).'

**Section: Mathematical Archetype**

- · `entropy` — 'nciple: nature selects the state that maximises the rate of entropy production. It extends the second law from a direction cons'
- · `entropy` — 'ion. It extends the second law from a direction constraint (entropy increases) to a rate constraint (entropy increases as fast '
- · `entropy` — 'ection constraint (entropy increases) to a rate constraint (entropy increases as fast as possible given the constraints). The o'
- · `entropy` — 'misation connects to information theory through the maximum entropy formalism.'

**Section: What The Math Says**

- · `entropy` — 'The entropy production rate sigma equals the sum over all irreversible '
- · `entropy` — ' probabilities proportional to the exponential of the total entropy produced along the path: P of path is proportional to exp o'
- · `entropy` — 'his makes the most probable path the one producing the most entropy — a maximum-entropy argument applied to trajectory space. T'
- · `entropy` — 'robable path the one producing the most entropy — a maximum-entropy argument applied to trajectory space. The principle contras'
- · `entropy` — "ory space. The principle contrasts with Prigogine's minimum entropy production theorem, which applies only in the linear near-e"
- · `entropy` — ' linear approximation breaks down and MEPP replaces minimum entropy production as the selection principle.'

**Section: Concept Tags**

- · `entropy` — '• maximum entropy production • MEPP • non-equilibrium selection • entropy pro'
- · `entropy` — 'mum entropy production • MEPP • non-equilibrium selection • entropy production rate • Dewar justification • far-from-equilibriu'

---

## HB07  (26 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 's to A, divided by 4G_N (Ryu & Takayanagi, 2006). This is a holographic formula: it computes a quantum information quantity (entang'
- ⚠️ `holographic` — 'rom black hole horizons to arbitrary boundary subregions in holographic theories. Its quantum correction (the Faulkner-Lewkowycz-Ma'
- · `entropy` — ') formula S_A = Area(γ_A)/4G_N states that the entanglement entropy of a boundary region A in the AdS/CFT correspondence equals'
- · `entropy` — 'a: it computes a quantum information quantity (entanglement entropy) using a geometric quantity (minimal surface area). The RT '
- · `entropy` — 'ce area). The RT formula generalises the Bekenstein-Hawking entropy from black hole horizons to arbitrary boundary subregions i'
- · `entropy` — 'kowycz-Maldacena generalisation) adds the bulk entanglement entropy across the minimal surface. The RT formula has been proven '
- ⚠️ `quantum correction` — ' arbitrary boundary subregions in holographic theories. Its quantum correction (the Faulkner-Lewkowycz-Maldacena generalisation) adds the '

**Section: Mathematical Form**

- · `entropy` — 'S_A = Area(γ_A) / 4G_N  where:   S_A = entanglement entropy of boundary region A   γ_A = minimal area surface in the bu'
- · `entropy` — ' S_bulk(Σ_A) + O(G_N)  where S_bulk(Σ_A) is the von Neumann entropy of bulk fields on the entanglement wedge Σ_A bounded by A ∪'

**Section: Constraint Category**

- · `entropy` — ' it equates an information-theoretic quantity (entanglement entropy, defined via von Neumann entropy) with a geometric quantity'
- · `entropy` — 'tic quantity (entanglement entropy, defined via von Neumann entropy) with a geometric quantity (minimal surface area, defined v'

**Section: DS Cross-References**

- · `Entropy` — 'HB02 (Bekenstein-Hawking Entropy — RT generalises BH entropy: for a boundary region equal to'
- · `entropy` — 'HB02 (Bekenstein-Hawking Entropy — RT generalises BH entropy: for a boundary region equal to the entire boundary, γ_A is'
- · `Entropy` — 's the black hole horizon and S_A = S_BH). IT02 (Von Neumann Entropy — the entanglement entropy S_A is a von Neumann entropy: S_'
- · `entropy` — 'd S_A = S_BH). IT02 (Von Neumann Entropy — the entanglement entropy S_A is a von Neumann entropy: S_A = −Tr(ρ_A log ρ_A) where '
- · `entropy` — 'ann Entropy — the entanglement entropy S_A is a von Neumann entropy: S_A = −Tr(ρ_A log ρ_A) where ρ_A is the reduced density ma'

**Section: Mathematical Archetype**

- · `entropy` — 'cs) to the information-theoretic structure of entanglement (entropy maximisation). The surface is both a geometric extremum and'

**Section: What The Math Says**

- ⚠️ `holographic` — 'The entanglement entropy of a boundary region A in the holographic CFT equals the area of the minimal-area bulk surface gamma-'
- ⚠️ `holographic` — ' a bulk region whose boundary is A union gamma-A. This is a holographic dictionary entry: a quantum quantity on the boundary (entan'
- · `entropy` — 'The entanglement entropy of a boundary region A in the holographic CFT equals the ar'
- · `entropy` — 'ary entry: a quantum quantity on the boundary (entanglement entropy) equals a classical quantity in the bulk (area). The quantu'
- · `entropy` — 'ea). The quantum-corrected FLM formula adds the von Neumann entropy of bulk quantum fields on the entanglement wedge — the bulk'

**Section: Concept Tags**

- ⚠️ `holographic` — '• Ryu-Takayanagi formula • holographic entanglement entropy • minimal surface • AdS/CFT • entangle'
- ⚠️ `holographic` — 'rrection • boundary-bulk duality • geometric entanglement • holographic dictionary • strong subadditivity'
- · `entropy` — '• Ryu-Takayanagi formula • holographic entanglement entropy • minimal surface • AdS/CFT • entanglement wedge • FLM corr'
- ⚠️ `duality` — 'S/CFT • entanglement wedge • FLM correction • boundary-bulk duality • geometric entanglement • holographic dictionary • strong '

---

## INFO1  (26 flags)

**Section: What It Claims**

- · `entropy` — 'The entropy H(X) of a discrete random variable X is the unique measure '
- · `Entropy` — '1948). H(X) = −Σ p_i log p_i, where log is base 2 for bits. Entropy measures the average number of binary questions needed to d'
- · `symmetry` — 'ormation content) consistent with three axioms: continuity, symmetry, and additivity for independent variables (Shannon, 1948). '

**Section: Mathematical Form**

- · `relative entropy` — 'H(X|Y) KL divergence: D_KL(P||Q) = Σ p_i log(p_i/q_i) ≥ 0  (relative entropy, not symmetric)'
- · `entropy` — 'um: H = log₂ n  for uniform distribution (n outcomes) Joint entropy: H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y) KL divergence: D_KL'
- · `entropy` — ' divergence: D_KL(P||Q) = Σ p_i log(p_i/q_i) ≥ 0  (relative entropy, not symmetric)'

**Section: Constraint Category**

- · `entropy` — 'Informatic (In): Shannon entropy is the canonical measure of information. It is the unique f'
- · `entropy` — ' axioms force H = −c·Σ p_i log p_i for some constant c. The entropy is both an upper bound (maximum lossless compression) and a'

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'he axiom that information is the fundamental quantity). M6 (Fisher Information — Fisher information is the second moment of the score func'
- ⚠️ `Fisher information` — 'tion is the fundamental quantity). M6 (Fisher Information — Fisher information is the second moment of the score function; both Shannon en'
- ⚠️ `Fisher information` — 'cond moment of the score function; both Shannon entropy and Fisher information quantify uncertainty but measure different aspects).'
- · `entropy` — 'g one bit of information costs at least kT ln 2 joules; the entropy H in bits maps to thermodynamic entropy via Boltzmann const'
- · `entropy` — "kT ln 2 joules; the entropy H in bits maps to thermodynamic entropy via Boltzmann constant). TD3 (Second Law — Boltzmann's entr"
- · `entropy` — "ropy via Boltzmann constant). TD3 (Second Law — Boltzmann's entropy S = k ln W is the thermodynamic special case for uniform di"
- · `entropy` — 'ermodynamic special case for uniform distributions; Shannon entropy is the generalisation to arbitrary probability distribution'
- · `entropy` — 'bability distributions). Ax1 (Information Primacy — Shannon entropy operationalises the axiom that information is the fundament'
- · `entropy` — 'on is the second moment of the score function; both Shannon entropy and Fisher information quantify uncertainty but measure dif'

**Section: Mathematical Archetype**

- · `entropy` — 'Mathematical archetype: thermodynamic-bound  Shannon entropy is simultaneously an upper bound (maximum compression rate)'
- · `entropy` — 'odynamic-style bound on information operations. The maximum entropy bound H ≤ log n is tight for uniform distributions. The KL '
- · `entropy` — 'form distributions. The KL divergence D_KL(P||Q) ≥ 0 is the entropy-based measure of the cost of using the wrong model Q when t'

**Section: What The Math Says**

- · `entropy` — 'Shannon entropy H(X) equals the negative sum over all values i of p-i times'
- · `entropy` — '. The chain rule H(X,Y) equals H(X) plus H(Y given X) shows entropy is additive for conditional distributions. The KL divergenc'

**Section: Concept Tags**

- · `entropy` — '• Shannon entropy • information content • uncertainty measure • bits per symb'
- · `entropy` — 'n content • uncertainty measure • bits per symbol • maximum entropy • KL divergence • joint entropy • conditional entropy • Sha'
- · `entropy` — '• bits per symbol • maximum entropy • KL divergence • joint entropy • conditional entropy • Shannon 1948 • information theory'
- · `entropy` — 'ximum entropy • KL divergence • joint entropy • conditional entropy • Shannon 1948 • information theory'

---

## IT05  (26 flags)

**Section: What It Claims**

- ⚠️ `Fisher information` — 'The Fisher information I(θ) = E[(∂/∂θ log f(x;θ))²] measures the amount of informa'
- ⚠️ `Fisher information` — 'bability distribution responds to changes in the parameter. Fisher information is the Hessian of KL divergence: the infinitesimal version '
- ⚠️ `Fisher information` — 'nfinitesimal version of statistical distinguishability. The Fisher information matrix g_ij = E[∂_i log f · ∂_j log f] defines a Riemannian'
- ⚠️ `Fisher information` — 'rgent gravity (Bianconi). In thermodynamic state space, the Fisher information matrix becomes the Ruppeiner metric — the negative Hessian '
- ⚠️ `Fisher-Rao` — 'nian metric on the space of probability distributions — the Fisher-Rao metric — making parameter estimation a problem of different'
- ⚠️ `information geometry` — 'hat thermodynamic fluctuation geometry is a special case of information geometry.'
- · `entropy` — 'trix becomes the Ruppeiner metric — the negative Hessian of entropy — showing that thermodynamic fluctuation geometry is a spec'
- · `fluctuation` — 'he negative Hessian of entropy — showing that thermodynamic fluctuation geometry is a special case of information geometry.'

**Section: Constraint Category**

- ⚠️ `Fisher information` — 'biased estimator can have variance smaller than the inverse Fisher information. This is the information-theoretic analog of the uncertaint'
- ⚠️ `Fisher information` — 'curvature of the underlying probability/wavefunction space. Fisher information also decreases under sufficient statistics (the information'

**Section: DS Cross-References**

- ⚠️ `Fisher information` — 'IT03 (KL Divergence — Fisher information is the Hessian of KL divergence; the local curvature of the'
- ⚠️ `Fisher information` — 'ence surface at its minimum). IT08 (Fisher-Rao Metric — the Fisher information matrix IS the metric tensor of the Fisher-Rao Riemannian me'
- ⚠️ `Fisher information` — 'y to scale dependence). INFO4 (Data Processing Inequality — Fisher information decreases under data processing; the infinitesimal version '
- ⚠️ `Fisher-Rao` — ' curvature of the divergence surface at its minimum). IT08 (Fisher-Rao Metric — the Fisher information matrix IS the metric tensor'
- ⚠️ `Fisher-Rao` — '— the Fisher information matrix IS the metric tensor of the Fisher-Rao Riemannian metric on statistical manifolds). BR04 (Thermody'
- ⚠️ `Fisher-Rao` — "hermodynamic Geometry — Ruppeiner's thermodynamic metric is Fisher-Rao applied to Gibbs/Boltzmann distributions, connecting statis"
- ⚠️ `information geometry` — 'is Wasserstein gradient flow with Fisher metric, connecting information geometry to scale dependence). INFO4 (Data Processing Inequality — F'

**Section: Mathematical Archetype**

- ⚠️ `Fisher information` — 'Mathematical archetype: optimization-principle  Fisher information defines the optimal precision of parameter estimation (Cram'
- ⚠️ `Fisher information` — ' wherever a probability distribution depends on parameters, Fisher information supplies the natural metric for comparing nearby distributi'
- ⚠️ `Fisher-Rao` — 'n (Cramér-Rao), the natural geometry of statistical models (Fisher-Rao), and the local structure of information divergence (Hessia'

**Section: What The Math Says**

- ⚠️ `Fisher information` — 'The Fisher information of a distribution f parameterised by theta is the expected '
- ⚠️ `Fisher information` — 'at least 1 over I of theta. In the multiparameter case, the Fisher information matrix g-ij has entries equal to the expected product of sc'
- ⚠️ `Fisher-Rao` — 'c tensor on the manifold of probability distributions — the Fisher-Rao metric. The key bridge identity: g-ij at theta-zero equals '

**Section: Concept Tags**

- ⚠️ `Fisher information` — '• Fisher information • Fisher information matrix • Cramér-Rao bound • score func'
- ⚠️ `Fisher information` — '• Fisher information • Fisher information matrix • Cramér-Rao bound • score function • log-likelihood'
- ⚠️ `information geometry` — 'mér-Rao bound • score function • log-likelihood curvature • information geometry • statistical estimation • Riemannian metric • parameter se'

---

## IT08  (26 flags)

**Section: What It Claims**

- ⚠️ `Fisher-Rao` — 'The Fisher-Rao metric ds² = g_ij dθ^i dθ^j, where g_ij = E[∂_i log f · ∂_j'
- ⚠️ `Fisher-Rao` — 'ndational object of information geometry (Amari, 1985). The Fisher-Rao metric on thermodynamic state space IS the Ruppeiner metric'
- ⚠️ `Fisher-Rao` — 'necting information geometry to thermodynamic geometry. The Fisher-Rao metric on quantum state space IS the Fubini-Study metric (f'
- ⚠️ `Fisher-Rao` — 'ation geometry to quantum mechanics. These bridges make the Fisher-Rao metric the geometric unifier of statistics, thermodynamics,'
- ⚠️ `information geometry` — 'ical distinguishability. This is the foundational object of information geometry (Amari, 1985). The Fisher-Rao metric on thermodynamic state'
- ⚠️ `information geometry` — 'ermodynamic state space IS the Ruppeiner metric, connecting information geometry to thermodynamic geometry. The Fisher-Rao metric on quantum'
- ⚠️ `information geometry` — ' states) or the Bures metric (for mixed states), connecting information geometry to quantum mechanics. These bridges make the Fisher-Rao met'

**Section: Mathematical Form**

- · `entropy` — 'uppeiner metric: ds² = −∂²S/∂X^i∂X^j dX^i dX^j  (Hessian of entropy)'

**Section: Constraint Category**

- ⚠️ `Fisher-Rao` — "Geometric (Gm): The Fisher-Rao metric is a geometric constraint — Chentsov's theorem shows"
- ⚠️ `information geometry` — ' (up to diffeomorphisms) satisfying the Einstein equations, information geometry has a unique metric satisfying invariance under sufficient '

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'IT05 (Fisher Information — the Fisher information matrix IS the metric tensor of the'
- ⚠️ `Fisher information` — 'IT05 (Fisher Information — the Fisher information matrix IS the metric tensor of the Fisher-Rao metric; the m'
- ⚠️ `Fisher-Rao` — '— the Fisher information matrix IS the metric tensor of the Fisher-Rao metric; the metric is the global geometric structure built '
- ⚠️ `Fisher-Rao` — 'ocal curvature of KL divergence). IT03 (KL Divergence — the Fisher-Rao metric is the infinitesimal structure of KL divergence; ds²'
- ⚠️ `Fisher-Rao` — 'Geometry — Ruppeiner metric on thermodynamic state space is Fisher-Rao applied to the canonical Gibbs ensemble; the Hessian of ent'
- ⚠️ `Fisher-Rao` — 'er-Rezchikov — RG flow is gradient flow with respect to the Fisher-Rao metric, connecting scale dependence to information geometry'
- ⚠️ `Fisher-Rao` — '). GT04 (Bianconi — derives gravitational dynamics from the Fisher-Rao geometry on quantum state space).'
- ⚠️ `information geometry` — 'ct to the Fisher-Rao metric, connecting scale dependence to information geometry). GT04 (Bianconi — derives gravitational dynamics from the '
- · `entropy` — 'Rao applied to the canonical Gibbs ensemble; the Hessian of entropy IS the Fisher metric). RG06 (Cotler-Rezchikov — RG flow is '

**Section: Mathematical Archetype**

- ⚠️ `Fisher-Rao` — 'Mathematical archetype: optimization-principle  The Fisher-Rao metric is the unique natural geometry on probability space,'

**Section: What The Math Says**

- ⚠️ `Fisher-Rao` — 'The Fisher-Rao line element ds-squared equals g-ij times d-theta-i times d'
- ⚠️ `Fisher-Rao` — 'square root of p times q. On thermodynamic state space, the Fisher-Rao metric becomes the Ruppeiner metric: minus the Hessian of e'
- ⚠️ `Fisher-Rao` — 'tates, it becomes the Bures metric. This universality makes Fisher-Rao the geometric bridge between information theory, thermodyna'
- · `entropy` — 'o metric becomes the Ruppeiner metric: minus the Hessian of entropy with respect to extensive variables. On quantum state space'

**Section: Concept Tags**

- ⚠️ `Fisher-Rao` — '• Fisher-Rao metric • information geometry • Chentsov theorem • statisti'
- ⚠️ `information geometry` — '• Fisher-Rao metric • information geometry • Chentsov theorem • statistical manifold • Riemannian metr'

---

## NE01  (26 flags)

**Section: What It Claims**

- · `entropy` — 'd by the continuous dissipation of energy and production of entropy (Prigogine, Nobel Prize 1977). These structures arise throu'
- · `entropy` — 'ures arise through symmetry-breaking instabilities when the entropy production rate exceeds a critical threshold. Examples incl'
- · `entropy` — ' biological organisms. The key insight is counterintuitive: entropy production, far from being the enemy of order, is its drive'
- · `entropy` — 'ver in open systems. The second law requires that the total entropy of system plus environment increases, but this increase can'
- · `entropy` — 'ordered structures (stars, galaxies) while increasing total entropy, making it an astrophysical dissipative structure.'
- · `symmetry` — 'rigogine, Nobel Prize 1977). These structures arise through symmetry-breaking instabilities when the entropy production rate exc'

**Section: Mathematical Form**

- · `Entropy` — 'Entropy production rate: σ = dS_i/dt = Σ_k J_k X_k ≥ 0  where:   J_'
- · `entropy` — 'ion (far from equilibrium):   δ²S < 0  (second variation of entropy becomes negative)   → spontaneous symmetry breaking → dissi'
- · `entropy` — 'ntaneous symmetry breaking → dissipative structure  Minimum entropy production (linear): dσ/dt ≤ 0  (Prigogine theorem)'
- · `symmetry` — 'cond variation of entropy becomes negative)   → spontaneous symmetry breaking → dissipative structure  Minimum entropy productio'

**Section: Constraint Category**

- · `entropy` — ' exist only in open systems with continuous energy flow and entropy production. The structure is a thermodynamic constraint — i'
- · `entropy` — 'input from environment) while obeying the second law (total entropy increases). The structure organises the entropy production,'
- · `entropy` — ' law (total entropy increases). The structure organises the entropy production, channelling it through ordered pathways.'

**Section: DS Cross-References**

- · `entropy` — 'fully compatible with the second law: the local decrease in entropy of the structured system is more than compensated by the en'
- · `entropy` — 'py of the structured system is more than compensated by the entropy increase in the environment). NE02 (Maximum Entropy Product'
- · `Entropy` — ' by the entropy increase in the environment). NE02 (Maximum Entropy Production Principle — MEPP proposes that dissipative struc'
- · `entropy` — 'nciple — MEPP proposes that dissipative structures maximise entropy production rate, selecting the pattern that most efficientl'

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — 'erns emerge spontaneously. The transition is analogous to a phase transition but occurs in a non-equilibrium, open system maintained by '
- · `symmetry` — 'y flux the system remains homogeneous; above the threshold, symmetry breaks and ordered patterns emerge spontaneously. The trans'

**Section: What The Math Says**

- · `entropy` — 'The entropy production rate sigma equals the sum over all irreversible '
- · `entropy` — "ons). In this linear regime, the system evolves to minimise entropy production (Prigogine's minimum entropy production theorem)"
- · `entropy` — "evolves to minimise entropy production (Prigogine's minimum entropy production theorem). Far from equilibrium, the linear appro"
- · `entropy` — 'ear approximation breaks down. When the second variation of entropy delta-squared-S becomes negative, the uniform state becomes'
- · `symmetry` — ' state becomes unstable and the system spontaneously breaks symmetry, forming a dissipative structure — a spatially or temporall'

**Section: Concept Tags**

- · `entropy` — 'es • Prigogine • far-from-equilibrium • self-organisation • entropy production • symmetry breaking • open systems • Bénard conv'
- · `symmetry` — 'from-equilibrium • self-organisation • entropy production • symmetry breaking • open systems • Bénard convection • order from di'

---

## GT02  (25 flags)

**Section: What It Claims**

- ⚠️ `holographic` — "w of gravity F = GmM/r² and Newton's second law F = ma from holographic and thermodynamic principles: the Bekenstein bound for info"
- ⚠️ `holographic` — 'dynamic principles: the Bekenstein bound for information on holographic screens, the equipartition of energy E = ½NkT, and the Unru'
- ⚠️ `holographic` — ' effect of the underlying microscopic degrees of freedom on holographic screens.  **Status (2026-05-04 deep-research pass):** Conte'
- · `entropy` — 'g from the statistical tendency of a system to increase its entropy (Verlinde, JHEP 1104:029, 2011). Just as an elastic polymer'
- · `entropy` — 'tal restoring force but because the coiled state has higher entropy than the stretched state, gravitational attraction arises b'
- · `entropy` — "configurations at lower gravitational potential have higher entropy than those at higher potential. Verlinde derives Newton's l"
- · `entropy` — 'vations of conservative many-body forces require unphysical entropy structures and multiple temperature baths; Hossenfelder & c'

**Section: Mathematical Form**

- ⚠️ `holographic` — "vation of Newton's gravity:   E = ½Nk_BT  (equipartition on holographic screen)   N = Ac³/Gℏ  (bits on screen of area A)   → F = Gm"

**Section: Constraint Category**

- · `entropy` — 'ional force is a thermodynamic constraint — the gradient of entropy with respect to position. If correct, gravity is not a fund'

**Section: DS Cross-References**

- ⚠️ `Fisher information` — 'the framework quantum by using quantum relative entropy and Fisher information).'
- · `relative entropy` — 'oni — Bianconi makes the framework quantum by using quantum relative entropy and Fisher information).'
- ⚠️ `holographic` — "py change ΔS uses the Bekenstein bound to count bits on the holographic screen). GT03 (Padmanabhan — Padmanabhan's holographic equi"
- ⚠️ `holographic` — " the holographic screen). GT03 (Padmanabhan — Padmanabhan's holographic equipartition extends Verlinde to cosmology, deriving the F"
- · `entropy` — "entropic force's temperature). HB01 (Bekenstein Bound — the entropy change ΔS uses the Bekenstein bound to count bits on the ho"
- · `entropy` — 'nconi makes the framework quantum by using quantum relative entropy and Fisher information).'

**Section: Mathematical Archetype**

- ⚠️ `holographic` — 'ndscape. The force law emerges from counting microstates on holographic screens — it is a statistical, not dynamical, derivation of'
- · `entropy` — 'is an optimization argument: the system evolves to maximise entropy (equivalently, minimise free energy), and gravitational att'
- · `entropy` — 'ergy), and gravitational attraction is the gradient of this entropy landscape. The force law emerges from counting microstates '

**Section: What The Math Says**

- ⚠️ `holographic` — 'e uses the equipartition theorem E equals half N k-B T on a holographic screen of area A equals 4 pi r-squared, where the number of'
- ⚠️ `holographic` — ' law of universal gravitation from purely thermodynamic and holographic arguments.'
- · `entropy` — " by F times displacement Delta-x equals temperature T times entropy change Delta-S. Verlinde derives Newton's second law by usi"
- · `entropy` — 'erature T equals h-bar a over 2 pi c k-B and the Bekenstein entropy change Delta-S equals 2 pi k-B m c Delta-x over h-bar (repr'

**Section: Concept Tags**

- ⚠️ `holographic` — "• entropic gravity • Verlinde • entropic force • holographic screen • emergent gravity • equipartition • Newton's law fr"
- ⚠️ `holographic` — ' information-based gravity • macroscopic entropy gradient • holographic degrees of freedom'
- · `entropy` — 'om thermodynamics • information-based gravity • macroscopic entropy gradient • holographic degrees of freedom'

---

## HB03  (24 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'The holographic principle states that the maximum entropy — hence maximum i'
- ⚠️ `holographic` — '-dimensional, not three-dimensional — the bulk physics is a holographic projection of boundary data. The holographic principle is r'
- ⚠️ `holographic` — 'k physics is a holographic projection of boundary data. The holographic principle is realised concretely in the AdS/CFT corresponde'
- · `entropy` — 'The holographic principle states that the maximum entropy — hence maximum information content — of any region of spac'

**Section: Mathematical Form**

- · `entropy` — 'S_max(V) ≤ A(∂V) / 4l_P²  where:   S_max = maximum entropy of region V   A(∂V) = area of the boundary ∂V   l_P² = ℏG/c'

**Section: Constraint Category**

- ⚠️ `holographic` — 'Informatic-Geometric (In-Gm): The holographic principle is both an information bound (maximum entropy sca'
- · `entropy` — 'holographic principle is both an information bound (maximum entropy scales as area) and a geometric principle (the degrees of f'

**Section: DS Cross-References**

- ⚠️ `holographic` — 'HB01 (Bekenstein Bound — the holographic principle follows from the Bekenstein bound: the energy-rad'
- ⚠️ `holographic` — '2 (Bekenstein-Hawking Entropy — BH entropy is the prototype holographic entropy: area-proportional, not volume-proportional). BR02 '
- ⚠️ `holography` — ' BR02 (AdS/CFT Correspondence — the concrete realisation of holography: a gravitational bulk is exactly dual to a non-gravitationa'
- ⚠️ `holographic` — 'tivity is built from entanglement, the mechanism underlying holographic encoding).'
- · `Entropy` — 'proportional information content). HB02 (Bekenstein-Hawking Entropy — BH entropy is the prototype holographic entropy: area-pro'
- · `entropy` — 'information content). HB02 (Bekenstein-Hawking Entropy — BH entropy is the prototype holographic entropy: area-proportional, no'
- · `entropy` — 'n-Hawking Entropy — BH entropy is the prototype holographic entropy: area-proportional, not volume-proportional). BR02 (AdS/CFT'
- · `entropy` — 'ndary theory). HB07 (Ryu-Takayanagi — computes entanglement entropy holographically as a minimal surface area in the bulk). BR0'

**Section: Mathematical Archetype**

- ⚠️ `holographic` — 'Mathematical archetype: dimensional-scaling  The holographic principle is a dimensional scaling law: information scales '
- · `entropy` — ' and distinguishes them from ordinary quantum systems where entropy is extensive (volume-scaling). The dimensional reduction is'

**Section: What The Math Says**

- ⚠️ `holographic` — 'f boundary. For a room-sized volume of 10 cubic metres, the holographic limit is roughly 10-to-the-70 bits — encoded on the walls, '
- ⚠️ `holographic` — 'ravitational theory live on the boundary: the interior is a holographic projection.'
- · `entropy` — 'The maximum entropy of a spatial region V is at most the area A of its boundary'

**Section: Concept Tags**

- ⚠️ `holographic` — '• holographic principle • area-entropy scaling • information bound • dime'
- ⚠️ `holographic` — 'ion • boundary degrees of freedom • Planck area • AdS/CFT • holographic encoding • bulk-boundary duality • emergent dimensionality'
- · `entropy` — '• holographic principle • area-entropy scaling • information bound • dimensional reduction • bound'
- ⚠️ `duality` — 'lanck area • AdS/CFT • holographic encoding • bulk-boundary duality • emergent dimensionality'

---

## RG06  (22 flags)

**Section: What It Claims**

- ⚠️ `Fisher information` — 'rence measure, where the cost function is determined by the Fisher information metric on the space of field configurations. This establish'
- ⚠️ `Fisher-Rao` — 'sport — on the space of probability distributions, with the Fisher-Rao metric providing the natural geometry (Cotler & Rezchikov, '
- ⚠️ `Fisher-Rao` — 'rt theory (Wasserstein geometry), and information geometry (Fisher-Rao metric). The Fisher metric IS the infinitesimal geometry of'
- ⚠️ `Fisher-Rao` — "hrough Bianconi's framework, to gravitational dynamics. The Fisher-Rao metric thus serves as the common geometric substrate of bot"
- ⚠️ `information geometry` — 'ence), optimal transport theory (Wasserstein geometry), and information geometry (Fisher-Rao metric). The Fisher metric IS the infinitesimal'
- ⚠️ `emergent spacetime` — ' geometric substrate of both renormalisation group flow and emergent spacetime curvature: scale evolution and gravitational dynamics are b'
- ⚠️ `emergent spacetime` — ' geometric substrate of both renormalisation group flow and emergent spacetime curvature: scale evolution and gravitational dynamics are b'

**Section: Mathematical Form**

- ⚠️ `Fisher-Rao` — 'e   F[ρ] = free energy functional   t = RG scale parameter  Fisher-Rao metric on configuration space:   g_ij = E_ρ[∂_i log ρ · ∂_j'

**Section: Constraint Category**

- ⚠️ `Fisher-Rao` — 'hows that the geometry of RG flow (scale dependence) is the Fisher-Rao metric (information geometry). The constraint is that RG fl'
- ⚠️ `information geometry` — 'try of RG flow (scale dependence) is the Fisher-Rao metric (information geometry). The constraint is that RG flow is not arbitrary but follo'

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'IT05 (Fisher Information — the Fisher information matrix provides the Riemannian met'
- ⚠️ `Fisher information` — 'IT05 (Fisher Information — the Fisher information matrix provides the Riemannian metric that governs the geom'
- ⚠️ `Fisher-Rao` — 'ometry of RG flow in the Cotler-Rezchikov framework). IT08 (Fisher-Rao Metric — the Fisher-Rao metric IS the metric of RG flow: Co'
- ⚠️ `Fisher-Rao` — ' Cotler-Rezchikov framework). IT08 (Fisher-Rao Metric — the Fisher-Rao metric IS the metric of RG flow: Cotler-Rezchikov makes thi'
- ⚠️ `monotonicity` — 'stein gradient flow structure: gradient flows have built-in monotonicity).'

**Section: Mathematical Archetype**

- ⚠️ `Fisher-Rao` — 'on space along the most efficient routes as measured by the Fisher-Rao distance. The gradient flow structure automatically implies'
- ⚠️ `monotonicity` — 'distance. The gradient flow structure automatically implies monotonicity (connecting to the c-theorem) and provides the geometric fr'

**Section: What The Math Says**

- ⚠️ `Fisher-Rao` — 'l metric on the underlying field configuration space is the Fisher-Rao metric g-ij equals the expected product of score functions.'
- ⚠️ `Fisher-Rao` — 'ic g-ij equals the expected product of score functions. The Fisher-Rao metric is the unique Riemannian metric on probability space'
- ⚠️ `Fisher-Rao` — ' governing RG flow is determined by information theory: the Fisher-Rao metric encodes how distinguishable nearby theories are, and'

**Section: Concept Tags**

- ⚠️ `Fisher-Rao` — 'kov • RG as optimal transport • Wasserstein gradient flow • Fisher-Rao metric • information geometry of RG • earth mover distance '
- ⚠️ `information geometry` — 'transport • Wasserstein gradient flow • Fisher-Rao metric • information geometry of RG • earth mover distance • free energy minimisation • s'

---

## HB08  (21 flags)

**Section: What It Claims**

- ⚠️ `holographic` — '(Bousso, 1999). This is the covariant generalisation of the holographic principle. Unlike the Bekenstein bound, which applies to sp'
- ⚠️ `holography` — 'osmological horizons. It is the most general formulation of holography: the entropy flowing through any light sheet is bounded by '
- · `entropy` — 'The Bousso bound (covariant entropy bound) states that the entropy passing through any light sh'
- · `entropy` — 'The Bousso bound (covariant entropy bound) states that the entropy passing through any light sheet L(B) — a null hypersurface '
- · `entropy` — 'zons. It is the most general formulation of holography: the entropy flowing through any light sheet is bounded by the area of t'

**Section: Mathematical Form**

- · `entropy` — 'xpanding orthogonal null geodesics from B   S[L(B)] = total entropy passing through L(B)   A(B) = area of B  Light sheet condit'

**Section: Constraint Category**

- · `entropy` — 'cture of spacetime (light rays) to its information content (entropy), showing that geometry constrains information flow.'

**Section: DS Cross-References**

- ⚠️ `Holographic` — 'ein bound is the special case for nearly flat space). HB03 (Holographic Principle — the Bousso bound is the covariant, rigorous ver'
- ⚠️ `holographic` — ' the Bousso bound is the covariant, rigorous version of the holographic principle that applies to all spacetimes). HB02 (Bekenstein'
- · `Entropy` — 'e that applies to all spacetimes). HB02 (Bekenstein-Hawking Entropy — BH entropy saturates the Bousso bound on the black hole h'
- · `entropy` — "s to all spacetimes). HB02 (Bekenstein-Hawking Entropy — BH entropy saturates the Bousso bound on the black hole horizon's ligh"

**Section: Mathematical Archetype**

- · `observer` — 'principle as special cases. Its covariance (independence of observer or time slicing) makes it the natural information-theoretic'
- ⚠️ `holographic` — 'bound in physics — it subsumes the Bekenstein bound and the holographic principle as special cases. Its covariance (independence of'
- · `entropy` — ': thermodynamic-bound  The Bousso bound is the most general entropy bound in physics — it subsumes the Bekenstein bound and the'

**Section: What The Math Says**

- · `entropy` — 'itive (meaning the light rays are not diverging). The total entropy S passing through this light sheet is at most the area of B'
- · `entropy` — 'where the Bekenstein bound fails (because arbitrarily large entropy can exist in large volumes), the Bousso bound remains valid'
- · `entropy` — 'und remains valid because the light sheet captures only the entropy that flows through the null surface. For a black hole horiz'
- · `entropy` — 'going future null surface, and the bound is saturated — the entropy passing through is exactly A over 4 G-N.'

**Section: Concept Tags**

- ⚠️ `holography` — 'ight sheet • null hypersurface • null expansion • covariant holography • entropy flow • causal structure • Raychaudhuri equation •'
- · `entropy` — '• Bousso bound • covariant entropy bound • light sheet • null hypersurface • null expansion • '
- · `entropy` — 'null hypersurface • null expansion • covariant holography • entropy flow • causal structure • Raychaudhuri equation • spacetime'

---

## INFO4  (20 flags)

**Section: What It Claims**

- ⚠️ `coarse-graining` — 'ov c-theorem in quantum field theory: renormalisation group coarse-graining — integrating out UV degrees of freedom at each RG step — i'
- ⚠️ `coarse-graining` — 'ctive degrees of freedom decreases monotonically under this coarse-graining for the same reason that I(X;Z) ≤ I(X;Y): each RG step can '
- ⚠️ `coarse-graining` — ' proof that RG flow is irreversible: information loss under coarse-graining implies c_UV ≥ c_IR.'

**Section: Constraint Category**

- ⚠️ `coarse-graining` — 'ion of the Zamolodchikov c-theorem in quantum field theory: coarse-graining (integrating out degrees of freedom in the renormalisation '

**Section: DS Cross-References**

- · `Entropy` — 'INFO1 (Shannon Entropy — I(X;Y) = H(X) + H(Y) − H(X,Y); mutual information is the '
- · `entropy` — ' information is the symmetric quantity derived from Shannon entropy). INFO3 (Channel Capacity — C = max I(X;Y); channel capacit'
- ⚠️ `coarse-graining` — 'he c-theorem is the field-theoretic instance of the DPI: RG coarse-graining is a Markov chain step, and the c-function counting effecti'
- ⚠️ `coarse-graining` — 'nder it, exactly as I(X;Z) ≤ I(X;Y). Information loss under coarse-graining IS RG irreversibility). RG04 (Zamolodchikov c-theorem — the'
- ⚠️ `coarse-graining` — 'he c-theorem is the field-theoretic instance of the DPI: RG coarse-graining is a Markov chain step, and the c-function counting effecti'
- ⚠️ `coarse-graining` — 'nder it, exactly as I(X;Z) ≤ I(X;Y). Information loss under coarse-graining IS RG irreversibility).'

**Section: Mathematical Archetype**

- · `entropy` — ' processing) — never gained. This parallels the Second Law: entropy never decreases; mutual information with the source never i'
- ⚠️ `coarse-graining` — 'ntum field theory is a monotone under renormalisation group coarse-graining because each RG step is a Markov data-processing step. c_UV'

**Section: What The Math Says**

- ⚠️ `coarse-graining` — 'tance is the Zamolodchikov c-theorem: renormalisation group coarse-graining is a Markov chain step from UV to IR, and the c-function — '
- ⚠️ `coarse-graining` — ' > c_IR means information was irreversibly destroyed in the coarse-graining, just as I(X;Z) < I(X;Y) means information was irreversibly'

**Section: Concept Tags**

- · `entropy` — 'tatistic • information conservation • KL divergence • joint entropy • irreversible processing • information monotonicity • chan'
- ⚠️ `monotonicity` — 'nce • joint entropy • irreversible processing • information monotonicity • channel capacity • coarse-graining • degrees of freedom r'
- ⚠️ `monotonicity` — 'duction • RG irreversibility • c-theorem foundation • UV-IR monotonicity • RG flow analog • coarse-graining • degrees of freedom red'
- ⚠️ `monotonicity` — 'duction • RG irreversibility • c-theorem foundation • UV-IR monotonicity • RG flow analog'
- ⚠️ `coarse-graining` — ' processing • information monotonicity • channel capacity • coarse-graining • degrees of freedom reduction • RG irreversibility • c-the'
- ⚠️ `coarse-graining` — '-theorem foundation • UV-IR monotonicity • RG flow analog • coarse-graining • degrees of freedom reduction • RG irreversibility • c-the'

---

## NE06  (20 flags)

**Section: What It Claims**

- · `entropy` — 'are exceptionally good at dissipating energy — they produce entropy faster than non-replicating alternatives (England, JCP 139,'
- · `entropy` — 's fluctuation theorem, England derived a lower bound on the entropy produced by a self-replicating system: the irreversibility '
- · `entropy` — " dissipative structures that increase the rate of universal entropy production. The theory extends Prigogine's dissipative stru"
- · `fluctuation` — ' (England, JCP 139, 121923, 2013). Starting from the Crooks fluctuation theorem, England derived a lower bound on the entropy produ'

**Section: Mathematical Form**

- · `Entropy` — 'Entropy production bound for self-replication:   ⟨ΔS_total⟩ ≥ −Δs_i'
- · `entropy` — 'l⟩ ≥ −Δs_int + log(n_rep/n_init)  where:   ΔS_total = total entropy production (system + environment)   Δs_int = internal entro'
- · `entropy` — 'tropy production (system + environment)   Δs_int = internal entropy change of the replicator   n_rep/n_init = replication ratio'
- · `fluctuation` — 'tor   n_rep/n_init = replication ratio  Derived from Crooks fluctuation theorem:   P_F(W)/P_R(−W) = e^{(W−ΔF)/kT}   applied to self'

**Section: Constraint Category**

- · `entropy` — 'amic constraint on biological self-replication: the minimum entropy cost of replication is set by the Crooks theorem. Replicato'
- · `entropy` — 'gradients) are thermodynamically favoured — they occupy the entropy-producing pathways that the second law makes most probable.'

**Section: DS Cross-References**

- · `entropy` — "spite the second law but because of it — organisms maximise entropy production). NE02 (MEPP — England's dissipation-driven adap"
- · `entropy` — "h MEPP: self-replicators are selected because they maximise entropy production rate). B5 (Landauer's Principle — the informatio"
- · `Fluctuation` — "NE04 (Crooks Fluctuation Theorem — England's bound is derived directly from the Croo"

**Section: What The Math Says**

- · `entropy` — 'tion as the forward process, England derives that the total entropy production averaged over many replication events is at leas'
- · `entropy` — 'replication events is at least the negative of the internal entropy change Delta-s-int plus the logarithm of the replication ra'
- · `entropy` — 'hm of the replication ratio n-rep over n-init. The internal entropy change accounts for the organisational cost of building the'
- · `entropy` — 'g the replica — a highly ordered structure has low internal entropy, requiring more total entropy production (more dissipation)'
- · `entropy` — 'ed structure has low internal entropy, requiring more total entropy production (more dissipation) to create. The log replicatio'
- · `fluctuation` — 'Starting from the Crooks fluctuation theorem applied to self-replication as the forward process,'

**Section: Concept Tags**

- · `entropy` — '• self-replication thermodynamics • biological complexity • entropy production bound • Crooks theorem biology • life as dissipa'

---

## RG04  (20 flags)

**Section: What It Claims**

- ⚠️ `monotonicity` — 'eory flows to the IR theory under coarse-graining. Both are monotonicity theorems proving that lossy processing — whether of data or'
- ⚠️ `coarse-graining` — 's and the information-theoretic data processing inequality: coarse-graining can only lose information, never gain it. The c-theorem was'
- ⚠️ `coarse-graining` — 'c_UV ≥ c_IR when the UV theory flows to the IR theory under coarse-graining. Both are monotonicity theorems proving that lossy processi'

**Section: Mathematical Form**

- ⚠️ `Monotonicity` — '*} = 0  For 2D CFT: c = central charge of Virasoro algebra  Monotonicity: c_UV ≥ c_IR  (strict inequality for non-trivial flow)  Str'

**Section: Constraint Category**

- ⚠️ `holographic` — "tive degrees of freedom appears in cosmology: Padmanabhan's holographic equipartition shows that the universe expands until the bul"
- · `entropy` — 'nic decrease under RG flow is the field-theoretic analog of entropy increase (second law) and information loss (data processing'

**Section: DS Cross-References**

- · `entropy` — 'cond Law — the c-theorem is the field-theoretic second law: entropy (in the form of lost degrees of freedom) can only increase '
- ⚠️ `monotonicity` — ') can only lose information). HB06 (Area Theorem — both are monotonicity/irreversibility statements: area increases in black hole pr'
- ⚠️ `coarse-graining` — 'eld-theoretic version of the DPI: both say that processing (coarse-graining) can only lose information). HB06 (Area Theorem — both are '

**Section: Mathematical Archetype**

- · `entropy` — 'otonicity structure connects three domains: thermodynamics (entropy increase), information theory (information loss), and quant'
- ⚠️ `monotonicity` — 'athematical archetype: conservation-law  The c-theorem is a monotonicity law (not a conservation law): c can decrease but never incr'
- ⚠️ `monotonicity` — 'g of the second law and the data processing inequality. The monotonicity structure connects three domains: thermodynamics (entropy i'
- ⚠️ `coarse-graining` — ' three are manifestations of the same underlying principle: coarse-graining is irreversible.'

**Section: Concept Tags**

- ⚠️ `monotonicity` — 'rem • Zamolodchikov • central charge • RG irreversibility • monotonicity • degrees of freedom counting • conformal field theory • Vi'
- ⚠️ `monotonicity` — 'ng • data processing inequality analog • mutual information monotonicity • Markov coarse-graining • effective degrees of freedom • i'
- ⚠️ `monotonicity` — 'ng • data processing inequality analog • mutual information monotonicity • Markov coarse-graining • effective degrees of freedom'
- ⚠️ `coarse-graining` — '-theoretic second law • UV-IR flow • information loss under coarse-graining • data processing inequality analog • mutual information mo'
- ⚠️ `coarse-graining` — 'nequality analog • mutual information monotonicity • Markov coarse-graining • effective degrees of freedom • information loss under coa'
- ⚠️ `coarse-graining` — 'ing • effective degrees of freedom • information loss under coarse-graining • data processing inequality analog • mutual information mo'
- ⚠️ `coarse-graining` — 'nequality analog • mutual information monotonicity • Markov coarse-graining • effective degrees of freedom'

---

## BR02  (19 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'dacena, 1997). This is the most concrete realisation of the holographic principle: the entire content of a gravitational bulk theor'
- ⚠️ `holographic` — 'imensional boundary theory without gravity. AdS/CFT bridges holographic bounds (HB) and renormalisation group (RG) physics: the ext'
- ⚠️ `holographic` — 'pondence connects information theory to gravity through the holographic dictionary: boundary entanglement entropy equals bulk geome'
- · `entropy` — 'y through the holographic dictionary: boundary entanglement entropy equals bulk geometric area (Ryu-Takayanagi), boundary confo'
- · `symmetry` — 'ls bulk geometric area (Ryu-Takayanagi), boundary conformal symmetry maps to bulk isometries, and boundary RG flow corresponds t'

**Section: Mathematical Form**

- ⚠️ `Holographic` — 'boundary  (bulk radial coordinate = boundary energy scale)  Holographic dictionary:   Boundary S_ent(A) = Bulk Area(γ_A)/4G_N  (Ryu'
- ⚠️ `Duality` — 'Duality: gravity in AdS_{d+1}  ⟺  CFT_d on boundary  Partition func'
- ⚠️ `duality` — 'ry)   Boundary RG flow = Bulk radial evolution  Strong/weak duality: strong boundary coupling ↔ weak bulk coupling'

**Section: Constraint Category**

- ⚠️ `duality` — 'Geometric-Informatic (Gm-In): AdS/CFT is a duality constraint: it requires that two superficially different th'

**Section: DS Cross-References**

- ⚠️ `Holographic` — 'HB03 (Holographic Principle — AdS/CFT is the precise mathematical realisation'
- ⚠️ `holographic` — 'le — AdS/CFT is the precise mathematical realisation of the holographic principle: (d+1)-dimensional gravity is encoded on a d-dime'
- · `entropy` — 'agi — RT is a consequence of AdS/CFT: boundary entanglement entropy equals bulk minimal surface area). RG01 (Wilson RG — the ex'
- ⚠️ `monotonicity` — "nergies on the boundary). RG04 (c-theorem — the c-theorem's monotonicity is geometrised in AdS/CFT: the c-function corresponds to a "

**Section: Mathematical Archetype**

- ⚠️ `duality` — 'Mathematical archetype: conservation-law  AdS/CFT is a duality: it establishes a one-to-one map between two complete theor'

**Section: Concept Tags**

- ⚠️ `holographic` — '• AdS/CFT correspondence • holographic duality • Maldacena conjecture • bulk-boundary duality • an'
- ⚠️ `holographic` — 'tter space • conformal field theory • strong-weak duality • holographic dictionary • geometric RG • radial-energy correspondence'
- ⚠️ `duality` — '• AdS/CFT correspondence • holographic duality • Maldacena conjecture • bulk-boundary duality • anti-de Si'
- ⚠️ `duality` — ' holographic duality • Maldacena conjecture • bulk-boundary duality • anti-de Sitter space • conformal field theory • strong-we'
- ⚠️ `duality` — 'anti-de Sitter space • conformal field theory • strong-weak duality • holographic dictionary • geometric RG • radial-energy cor'

---

## GT01  (19 flags)

**Section: What It Claims**

- ⚠️ `η` — 'on, and (2) the entropy-area proportionality δS = ηδA where η = 1/4l_P². The heat flux δQ is identified with the energy f'
- · `entropy` — 'neral relativity can be derived from the proportionality of entropy to horizon area, combined with the Clausius relation δQ = T'
- · `entropy` — 'thermodynamic identity relating heat flow, temperature, and entropy at every point in spacetime. The key inputs are: (1) the Un'
- · `entropy` — 'erating observers near a local Rindler horizon, and (2) the entropy-area proportionality δS = ηδA where η = 1/4l_P². The heat f'

**Section: Mathematical Form**

- ⚠️ `η` — '= T dS  Inputs:   T = ℏa/2πck_B  (Unruh temperature)   dS = η dA = (1/4l_P²) dA  (entropy-area proportionality)   δQ = T_'
- · `entropy` — 'ℏa/2πck_B  (Unruh temperature)   dS = η dA = (1/4l_P²) dA  (entropy-area proportionality)   δQ = T_ab k^a dΣ^b  (heat flux thro'

**Section: Constraint Category**

- · `entropy` — 'etric content (curvature) equals the thermodynamic content (entropy production) at every point. This is not an analogy: it is a'
- · `entropy` — ' derivation. The constraint has both thermodynamic content (entropy, temperature, heat) and geometric content (curvature, area,'

**Section: DS Cross-References**

- ⚠️ `Fisher information` — 'tends to quantum regime, using quantum relative entropy and Fisher information). TD3 (Second Law — the Clausius relation δQ = TdS is a con'
- · `relative entropy` — 'Entropy — Bianconi extends to quantum regime, using quantum relative entropy and Fisher information). TD3 (Second Law — the Clausius rel'
- · `observer` — '2πck_B provides the local temperature for each accelerating observer). GV1 (Einstein Field Equations — the output of the derivat'
- · `Entropy` — 'HB02 (Bekenstein-Hawking Entropy — the entropy-area relation S = A/4l_P² is the key input to'
- · `entropy` — "HB02 (Bekenstein-Hawking Entropy — the entropy-area relation S = A/4l_P² is the key input to Jacobson's de"
- · `Entropy` — ' gravity as an entropic force). GT04 (Bianconi Gravity from Entropy — Bianconi extends to quantum regime, using quantum relativ'
- · `entropy` — ' Bianconi extends to quantum regime, using quantum relative entropy and Fisher information). TD3 (Second Law — the Clausius rel'

**Section: What The Math Says**

- ⚠️ `eta` — 'l geodesics. Assign entropy proportional to area: dS equals eta times dA, with eta equals 1 over 4 l-P-squared. The heat fl'
- ⚠️ `eta` — ' entropy proportional to area: dS equals eta times dA, with eta equals 1 over 4 l-P-squared. The heat flux delta-Q through '
- · `entropy` — 'celeration of the horizon-generating null geodesics. Assign entropy proportional to area: dS equals eta times dA, with eta equa'

**Section: Concept Tags**

- · `entropy` — 'nt gravity • Raychaudhuri equation • local causal horizon • entropy-area proportionality • thermodynamic consistency'

---

## HB01  (19 flags)

**Section: What It Claims**

- · `entropy` — 'The Bekenstein bound S ≤ 2πER/ℏc states that the maximum entropy (equivalently, the maximum information content) of any phys'
- · `entropy` — ' not form a black hole, which would have Bekenstein-Hawking entropy proportional to its horizon area.'

**Section: Mathematical Form**

- · `entropy` — 'S ≤ 2πER / ℏc  (in natural units: S ≤ 2πER)  where:   S = entropy (in nats; divide by ln 2 for bits)   E = total energy of th'

**Section: Constraint Category**

- · `entropy` — 'und is simultaneously a thermodynamic constraint (it limits entropy) and an informatic constraint (it limits information conten'

**Section: DS Cross-References**

- ⚠️ `Holographic` — 'py is the maximum entropy for a given boundary area). HB03 (Holographic Principle — the Bekenstein bound implies holography: maxima'
- ⚠️ `holography` — ' HB03 (Holographic Principle — the Bekenstein bound implies holography: maximal information scales with area, not volume). INFO1 ('
- · `Entropy` — 'HB02 (Bekenstein-Hawking Entropy — the BH entropy S = A/4l_P² saturates the Bekenstein bound'
- · `entropy` — 'HB02 (Bekenstein-Hawking Entropy — the BH entropy S = A/4l_P² saturates the Bekenstein bound for black holes;'
- · `entropy` — ' A/4l_P² saturates the Bekenstein bound for black holes; BH entropy is the maximum entropy for a given boundary area). HB03 (Ho'
- · `entropy` — 'Bekenstein bound for black holes; BH entropy is the maximum entropy for a given boundary area). HB03 (Holographic Principle — t'
- · `Entropy` — 'l information scales with area, not volume). INFO1 (Shannon Entropy — the Bekenstein bound limits the Shannon entropy of any ph'
- · `entropy` — ' (Shannon Entropy — the Bekenstein bound limits the Shannon entropy of any physical information storage system). TD3 (Second La'
- · `entropy` — 'n when matter falls into black holes: the total generalised entropy never decreases).'

**Section: Mathematical Archetype**

- ⚠️ `holography` — 'formation capacity — the foundational insight that leads to holography and eventually to gravity-from-information programmes.'

**Section: What The Math Says**

- · `entropy` — 'The maximum entropy S of a system with total energy E enclosed in a sphere of r'
- · `entropy` — 'ck hole of energy E and Schwarzschild radius R = 2GE/c⁴ has entropy exactly equal to the Bekenstein bound. Any attempt to pack '

**Section: Concept Tags**

- ⚠️ `holographic` — 'enstein bound • information density limit • entropy bound • holographic limit • Planck-scale information • black hole saturation • '
- · `entropy` — '• Bekenstein bound • information density limit • entropy bound • holographic limit • Planck-scale information • blac'
- · `entropy` — ' black hole saturation • information-energy bound • maximum entropy • quantum states • gravitational information bound'

---

## HB06  (19 flags)

**Section: What It Claims**

- · `entropy` — 'ravitational analog of the second law of thermodynamics: if entropy is proportional to area (Bekenstein-Hawking), then the area'
- · `entropy` — 'em, but the generalised second law — total area plus matter entropy — remains valid.'
- · `connection` — 'w for black holes. The theorem established the first formal connection between black hole mechanics and thermodynamics. Quantum ef'

**Section: Constraint Category**

- · `entropy` — 'e monotonicity of area is the monotonicity of gravitational entropy. Combined with the four laws of black hole mechanics, it es'
- ⚠️ `monotonicity` — 't as the second law constrains thermodynamic processes. The monotonicity of area is the monotonicity of gravitational entropy. Combi'
- ⚠️ `monotonicity` — 'ns thermodynamic processes. The monotonicity of area is the monotonicity of gravitational entropy. Combined with the four laws of bl'
- · `fluctuation` — ' work ⟨W_diss⟩ ≥ 0 in the Jarzynski equality and the Crooks fluctuation theorem. A quantum gravitational fluctuation theorem — exte'
- · `fluctuation` — 'and the Crooks fluctuation theorem. A quantum gravitational fluctuation theorem — extending the Crooks relation to black hole proce'

**Section: DS Cross-References**

- · `entropy` — 'itational version of the second law: area plays the role of entropy, surface gravity plays the role of temperature). HB02 (Beke'
- · `Entropy` — 'ty plays the role of temperature). HB02 (Bekenstein-Hawking Entropy — the area theorem becomes the second law when S = A/4l_P²)'
- · `entropy` — 'eorem states that gravitational processes can only increase entropy; both are monotonicity/irreversibility statements). NE03 (J'
- ⚠️ `monotonicity` — 'gravitational processes can only increase entropy; both are monotonicity/irreversibility statements). NE03 (Jarzynski Equality — Jar'
- · `fluctuation` — 'ms; the area theorem is the gravitational analog awaiting a fluctuation-theorem generalisation).'

**Section: Mathematical Archetype**

- · `entropy` — ' — area can increase but never decrease. It is analogous to entropy in thermodynamics and mutual information loss in informatio'
- ⚠️ `monotonicity` — 'ematical archetype: conservation-law  The area theorem is a monotonicity law rather than a strict conservation law — area can increa'
- ⚠️ `monotonicity` — ' and mutual information loss in information processing. The monotonicity structure (irreversibility) is the common thread linking th'

**Section: What The Math Says**

- · `entropy` — 'arallels the third law. The generalised second law adds the entropy of matter outside the black hole: the total d of A over 4 l'

**Section: Concept Tags**

- · `entropy` — 'eneralised second law • surface gravity • irreversibility • entropy increase • four laws of black hole mechanics'
- ⚠️ `monotonicity` — 'theorem • black hole mechanics • gravitational second law • monotonicity • null energy condition • generalised second law • surface '

---

## IT03  (19 flags)

**Section: What It Claims**

- ⚠️ `Fisher information` — 've) of KL divergence with respect to parameters defines the Fisher information metric on the space of probability distributions, making it'
- · `relative entropy` — 'ity distributions; its quantum generalisation — the quantum relative entropy S(ρ||σ) = Tr(ρ log ρ − ρ log σ) — extends this to density m'
- ⚠️ `information geometry` — 'ity distributions, making it the infinitesimal generator of information geometry.'
- · `entropy` — 'ibutions; its quantum generalisation — the quantum relative entropy S(ρ||σ) = Tr(ρ log ρ − ρ log σ) — extends this to density m'
- ⚠️ `monotonicity` — 'rices and quantum states, preserving the non-negativity and monotonicity properties in the non-commutative setting. KL divergence co'

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'g σ) is the quantum generalisation of KL divergence). IT05 (Fisher Information — the Fisher metric is the Hessian of KL divergence; Fisher'
- ⚠️ `Fisher information` — 'mation — the Fisher metric is the Hessian of KL divergence; Fisher information is the infinitesimal version of KL divergence). TD3 (Second'
- · `Relative Entropy` — ' measures distance from maximum uncertainty). IT04 (Quantum Relative Entropy — S(ρ||σ) = Tr(ρ log ρ − ρ log σ) is the quantum generalisa'
- · `Entropy` — 'INFO1 (Shannon Entropy — KL divergence D_KL(P||U) from any distribution to the uni'
- · `entropy` — ' to the uniform distribution equals log N minus the Shannon entropy H(P); entropy measures distance from maximum uncertainty). '
- · `entropy` — 'm distribution equals log N minus the Shannon entropy H(P); entropy measures distance from maximum uncertainty). IT04 (Quantum '
- · `Entropy` — ' distance from maximum uncertainty). IT04 (Quantum Relative Entropy — S(ρ||σ) = Tr(ρ log ρ − ρ log σ) is the quantum generalisa'

**Section: What The Math Says**

- ⚠️ `Fisher information` — 'ative of KL divergence at theta equals theta-zero gives the Fisher information matrix g-ij — this is the key bridge to information geometr'
- ⚠️ `Fisher-Rao` — 'is the key bridge to information geometry, showing that the Fisher-Rao metric is the infinitesimal structure of statistical diverg'
- ⚠️ `information geometry` — ' Fisher information matrix g-ij — this is the key bridge to information geometry, showing that the Fisher-Rao metric is the infinitesimal st'

**Section: Concept Tags**

- ⚠️ `Fisher information` — 'inequality • statistical distinguishability • free energy • Fisher information • information geometry • asymmetric divergence • Sanov theo'
- · `relative entropy` — '• KL divergence • relative entropy • information divergence • Gibbs inequality • statistical d'
- ⚠️ `information geometry` — 'cal distinguishability • free energy • Fisher information • information geometry • asymmetric divergence • Sanov theorem'
- · `entropy` — '• KL divergence • relative entropy • information divergence • Gibbs inequality • statistical d'

---

## NE04  (18 flags)

**Section: What It Claims**

- · `entropy` — '-equilibrium thermodynamics — it relates the probability of entropy-producing (forward) and entropy-consuming (reverse) fluctua'
- · `entropy` — ' relates the probability of entropy-producing (forward) and entropy-consuming (reverse) fluctuations. The Crooks theorem is the'
- · `symmetry` — ' (Crooks, PRE 60, 2721, 1999). This is an exact microscopic symmetry of non-equilibrium thermodynamics — it relates the probabil'
- · `fluctuation` — 'The Crooks fluctuation theorem states that the ratio of the probability of perform'
- · `fluctuation` — 'e) fluctuations. The Crooks theorem is the most fundamental fluctuation theorem: the Jarzynski equality follows from it by integrat'

**Section: Constraint Category**

- · `entropy` — 'sipated work — and determines the probability ratio between entropy-producing and entropy-consuming fluctuations.'
- · `entropy` — 'ermines the probability ratio between entropy-producing and entropy-consuming fluctuations.'
- · `symmetry` — 'mic (Th): The Crooks theorem is a fundamental thermodynamic symmetry: it quantifies the asymmetry between forward and reverse pr'

**Section: DS Cross-References**

- · `entropy` — 'aw — the second law is a macroscopic consequence of Crooks: entropy-producing paths are exponentially more probable than entrop'
- · `entropy` — 'ntropy-producing paths are exponentially more probable than entropy-consuming paths). NE05 (Fluctuation-Dissipation Theorem — t'
- · `Fluctuation` — 'entially more probable than entropy-consuming paths). NE05 (Fluctuation-Dissipation Theorem — the FDT is the near-equilibrium linea'
- · `fluctuation` — ' between forward and reverse path distributions, connecting fluctuation theorems to information theory).'

**Section: Mathematical Archetype**

- · `symmetry` — 'are symmetric — this is equilibrium. Non-zero ΔF breaks the symmetry, and the Crooks theorem quantifies exactly how much the for'

**Section: What The Math Says**

- · `entropy` — 'tive. For large systems where W is much greater than k-B-T, entropy-consuming fluctuations are exponentially suppressed; for mo'
- · `fluctuation` — 'The Crooks fluctuation theorem relates the probability P-F of W of doing work W in'

**Section: Concept Tags**

- · `entropy` — 'stribution • forward-reverse asymmetry • detailed balance • entropy production • microscopic reversibility • crossing point met'
- · `symmetry` — '• Crooks fluctuation theorem • time-reversal symmetry • work distribution • forward-reverse asymmetry • detailed '
- · `fluctuation` — '• Crooks fluctuation theorem • time-reversal symmetry • work distribution • forw'

---

## QM5  (17 flags)

**Section: What It Claims**

- ⚠️ `D_eff` — 'traction, and E = mc². The DS framework takes c as fixed at D_eff = 4 by construction of Ω_D; deviation at other D_eff values'
- ⚠️ `D_eff` — 'xed at D_eff = 4 by construction of Ω_D; deviation at other D_eff values is an open conjecture.'
- · `observer` — 'n all inertial frames regardless of the motion of source or observer. These imply Lorentz transformations: time dilation, length'

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'General Relativity). Ω_D: c is set to be frame-invariant at D_eff=4 by construction. G1 (Dimensional Redshift): proposes that'
- ⚠️ `D_eff` — 'G1 (Dimensional Redshift): proposes that c is invariant but D_eff varies — energy attenuates, light slows cosmologically.'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'z transformations. The DS framework takes c as invariant at D_eff=4 by construction of Ω_D, with behavior at D_eff≠4 left as '
- ⚠️ `D_eff` — 'variant at D_eff=4 by construction of Ω_D, with behavior at D_eff≠4 left as an open conjecture.  Dimensional sensitivity: D-s'
- ⚠️ `D_eff` — 'roup SO(D,1) changes structure. Ω_D takes c as invariant at D_eff=4 by construction.'
- · `symmetry` — 'Mathematical archetype: symmetry-conservation  A constraint derived from the geometric symme'
- · `symmetry` — "metry-conservation  A constraint derived from the geometric symmetry of a system or Hilbert space. Noether's theorem is the mast"
- · `symmetry` — "Noether's theorem is the master statement: every continuous symmetry of the action generates a conserved current. Discrete symme"
- · `symmetry` — 'aws for quantum numbers. The Pauli exclusion principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions'
- · `symmetry` — 'xchange, constraining the entire structure of matter. Gauge symmetry generates charge conservation via Noether. Topological symm'
- · `Symmetry` — 'ed topological invariants (winding numbers, Chern classes). Symmetry-conservation laws are D-sensitive when the relevant symmetr'
- · `symmetry` — 'ymmetry-conservation laws are D-sensitive when the relevant symmetry group changes with dimension — for instance, the rotation g'
- · `symmetry` — 'elativity establish c-invariance as a fundamental spacetime symmetry generating Lorentz transformations. The DS framework takes '

**Section: What The Math Says**

- · `observer` — ' is the same in all inertial frames regardless of source or observer motion — require that space and time coordinates mix under '

---

## TD3  (17 flags)

**Section: What It Claims**

- · `entropy` — 'The total entropy of an isolated system never decreases: ΔS ≥ 0. Entropy S me'
- · `Entropy` — 'otal entropy of an isolated system never decreases: ΔS ≥ 0. Entropy S measures the number of microstates consistent with a macr'

**Section: Constraint Category**

- · `entropy` — 'Thermodynamic/Informatic (Th/In): entropy is simultaneously a thermodynamic state function and a meas'

**Section: DS Cross-References**

- · `entropy` — 'Grounds B5 (Landauer: erasing information costs entropy). F1 (Ashby: regulatory variety has an entropy cost). Ax1 ('
- · `entropy` — 'mation costs entropy). F1 (Ashby: regulatory variety has an entropy cost). Ax1 (information primacy: information loss = physica'
- · `entropy` — "DS framework's vector history topology is an application of entropy growth: the semantic manifold drifts irreversibly. Cross-do"

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'
- · `Entropy` — 'ure (B5, Landauer).  Dimensional sensitivity: D-sensitive — Entropy production rates, phase-space volumes, and equilibrium dist'
- · `entropy` — 'pendent through the density of states — in D dimensions the entropy of ideal systems scales differently.'

**Section: What The Math Says**

- · `entropy` — 'The second law states that the total entropy S of an isolated system never decreases: delta-S is greater'
- · `entropy` — "o zero, with equality for reversible processes. Boltzmann's entropy formula S equals k_B times ln(Omega), where Omega is the nu"
- · `entropy` — 'figurations consistent with the macroscopic state, connects entropy to statistical mechanics. Systems evolve toward states with'
- · `entropy` — 's to be disordered. The law establishes the arrow of time — entropy increase distinguishes the future from the past. Perpetual '

**Section: Concept Tags**

- · `entropy` — '• second law thermodynamics • entropy increase • arrow of time • irreversibility • Boltzmann entr'
- · `entropy` — 'ropy increase • arrow of time • irreversibility • Boltzmann entropy • statistical mechanics • heat flow direction • Carnot effi'

---

## BR01  (16 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'le corresponds to an entangled pair. The conjecture bridges holographic bounds and quantum information theory by identifying a geom'
- ⚠️ `holographic` — 'ing entanglement disconnects the geometry. This bridges HB (holographic bounds) and IT (information theory): geometric connections '

**Section: Mathematical Form**

- · `entropy` — 'o-sided AdS black hole connected by ER bridge  Entanglement entropy: S_ent = S_BH = A/4G_N   (entanglement entropy equals geome'
- · `entropy` — 'Entanglement entropy: S_ent = S_BH = A/4G_N   (entanglement entropy equals geometric area)  Disconnecting limit: S_ent → 0  ↔  '

**Section: Constraint Category**

- · `connection` — ', spacetime connectivity). It proposes that every geometric connection is an information correlation, and every information correl'
- · `connection` — 'rrelation, and every information correlation is a geometric connection. This would make information the fundamental substance from'

**Section: DS Cross-References**

- · `Entropy` — 'HB02 (Bekenstein-Hawking Entropy — the entanglement entropy of ER = EPR equals the BH entrop'
- · `entropy` — 'HB02 (Bekenstein-Hawking Entropy — the entanglement entropy of ER = EPR equals the BH entropy, connecting information t'
- · `entropy` — 'ntropy — the entanglement entropy of ER = EPR equals the BH entropy, connecting information to horizon area). IT02 (Von Neumann'
- · `Entropy` — ' connecting information to horizon area). IT02 (Von Neumann Entropy — the entanglement in ER = EPR is measured by von Neumann e'
- · `entropy` — 'y — the entanglement in ER = EPR is measured by von Neumann entropy of the reduced state). HB07 (Ryu-Takayanagi — RT computes e'
- · `entropy` — 'ced state). HB07 (Ryu-Takayanagi — RT computes entanglement entropy as geometric area; ER = EPR identifies the geometric surfac'

**Section: Mathematical Archetype**

- ⚠️ `duality` — 'atical archetype: conservation-law  ER = EPR is an identity/duality: it equates two seemingly different objects (geometric conn'

**Section: What The Math Says**

- · `entropy` — 'stein-Rosen bridge (wormhole) in the bulk. The entanglement entropy of the left system equals the Bekenstein-Hawking entropy S-'
- · `entropy` — 'nt entropy of the left system equals the Bekenstein-Hawking entropy S-BH equals A over 4 G-N, where A is the area of the wormho'

**Section: Concept Tags**

- ⚠️ `holographic` — 'om qubit • geometry from information • Maldacena-Susskind • holographic entanglement'

---

## HB10  (15 flags)

**Section: What It Claims**

- · `entropy` — 'arge BH phase dominates. The transition is first-order: the entropy jumps discontinuously at T_HP. Via the AdS/CFT corresponden'
- ⚠️ `phase transition` — 't in anti-de Sitter (AdS) spacetime, there is a first-order phase transition between two gravitational configurations: thermal radiation'
- ⚠️ `phase transition` — 'spondence (Maldacena 1997, Witten 1998), this gravitational phase transition maps to the confinement/deconfinement transition in the dua'

**Section: Mathematical Form**

- ⚠️ `Phase transition` — '  F_BH = r_+/4 - pi*T*r_+^2  (large Schwarzschild-AdS BH)   Phase transition at F_BH = 0  =>  r_+ = l  =>  T = T_HP  Euclidean path inte'

**Section: Constraint Category**

- ⚠️ `phase transition` — 'Th): The Hawking-Page transition is a genuine thermodynamic phase transition in the gravitational sector. The constraint is free energy '

**Section: DS Cross-References**

- ⚠️ `Holographic` — 'termines which phase is thermodynamically preferred). HB03 (Holographic Principle — AdS/CFT maps the bulk Hawking-Page transition t'
- ⚠️ `holographic` — 'ion to a boundary confinement/deconfinement transition; the holographic principle underlies this duality). GT01 (Jacobson Thermodyn'
- · `Entropy` — 'ion to define a phase transition). HB02 (Bekenstein-Hawking Entropy — S = A/4 enters the free energy F = M - TS that determines'
- ⚠️ `phase transition` — 'perature, there is no thermodynamic competition to define a phase transition). HB02 (Bekenstein-Hawking Entropy — S = A/4 enters the fre'
- ⚠️ `duality` — "nement transition; the holographic principle underlies this duality). GT01 (Jacobson Thermodynamic Derivation — Jacobson's fram"

**Section: What The Math Says**

- · `entropy` — 'low temperature, thermal radiation wins (low energy, modest entropy). At high temperature, the large BH wins (huge entropy ~ A/'
- · `entropy` — 'dest entropy). At high temperature, the large BH wins (huge entropy ~ A/4 overwhelms the energy cost). The crossover at T_HP = '
- · `entropy` — 'r at T_HP = 1/(pi*l) is a first-order phase transition: the entropy jumps discontinuously. Through AdS/CFT, this maps to the de'
- ⚠️ `phase transition` — 'gy cost). The crossover at T_HP = 1/(pi*l) is a first-order phase transition: the entropy jumps discontinuously. Through AdS/CFT, this m'

**Section: Concept Tags**

- ⚠️ `phase transition` — '• Hawking-Page transition • first-order phase transition • anti-de Sitter space • AdS/CFT correspondence • confineme'

---

## TD4  (14 flags)

**Section: What It Claims**

- · `entropy` — 'As temperature approaches absolute zero, the entropy of a perfect crystal approaches a constant minimum (zero fo'
- · `entropy` — 'ps. The third law fixes the absolute reference point of the entropy scale and governs the behavior of all thermal properties ne'

**Section: Constraint Category**

- · `entropy` — 'Thermodynamic (Th): lower bound on entropy at finite temperature; makes absolute-zero a geometric asym'

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'
- · `entropy` — 'his entry: The Third Law of Thermodynamics establishes that entropy approaches a constant minimum at absolute zero, making T=0 '
- · `entropy` — 'acy are D-sensitive — in D dimensions zero-point energy and entropy at T→0 depend on the density of states of the quantum syste'

**Section: What The Math Says**

- · `entropy` — ' states that as absolute temperature T approaches zero, the entropy S of a perfect crystal with a unique ground state approache'
- · `entropy` — 'pproaches 0 as T approaches 0. This establishes an absolute entropy scale rather than one defined only by differences. The law '
- · `entropy` — 'finite steps — each cooling step removes progressively less entropy and temperature approaches zero asymptotically. It also req'
- · `entropy` — 'vanish as T tends to zero (otherwise integrating C/T to get entropy change would diverge).'

**Section: Concept Tags**

- · `entropy` — '• third law thermodynamics • absolute zero • entropy zero • unattainability of absolute zero • heat capacity van'
- · `entropy` — 'bility of absolute zero • heat capacity vanishes • absolute entropy scale • Nernst theorem'

---

## CM4  (13 flags)

**Section: What It Claims**

- · `symmetry` — "e a special case of Noether's theorem applied to rotational symmetry."

**Section: Constraint Category**

- · `symmetry` — 'Geometric (Ge): rotational symmetry → conserved angular momentum → areal velocity constant.'

**Section: DS Cross-References**

- · `symmetry` — "AM5 (Noether's theorem) is the parent: rotational symmetry → angular momentum. Connects to CM2 and CM5."

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Kepler's Second Law (Equal Areas) "
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "
- · `symmetry` — "bital expression of Noether's theorem applied to rotational symmetry.  Dimensional sensitivity: D-sensitive — Equal areas follow"
- · `symmetry` — 'ngular momentum conservation, which follows from rotational symmetry via Noether — rotational symmetry and its conservation law '
- · `symmetry` — 'h follows from rotational symmetry via Noether — rotational symmetry and its conservation law are D-sensitive through the struct'

---

## TD2  (13 flags)

**Section: What It Claims**

- · `symmetry` — "orms. This is Noether's theorem applied to time-translation symmetry — the universe has no preferred moment, so energy is conser"

**Section: DS Cross-References**

- · `symmetry` — 'AM5 (Noether) is the parent via time symmetry. B5 (Landauer): erasing a bit dissipates k_BT ln2 — a first'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — 'ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: The First Law of Thermodynamics is'
- ⚠️ `D_eff` — 'me-translation symmetry may be broken if constants run with D_eff, making this a subtle D-sensitivity.'
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "
- · `symmetry` — ' δQ − δW. It is the Noether consequence of time-translation symmetry and bounds all energy-converting processes.  Dimensional se'
- · `symmetry` — 'variant — Energy conservation follows from time-translation symmetry via Noether — and time-translation symmetry may be broken i'
- · `symmetry` — 'ime-translation symmetry via Noether — and time-translation symmetry may be broken if constants run with D_eff, making this a su'

---

## C1  (12 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — 'bolic scaling exponent is a direct rational function of the effective dimension of the vascular branching network.'
- ⚠️ `D_eff` — 'imary biological scaling law. The ¾ vs ⅔ debate resolves to D_eff=3 network vs D_eff=2 surface geometry — a direct dimensiona'
- ⚠️ `D_eff` — 'aling law. The ¾ vs ⅔ debate resolves to D_eff=3 network vs D_eff=2 surface geometry — a direct dimensional discrimination.  '
- ⚠️ `D_eff` — "mensional sensitivity: D-sensitive — Kleiber's exponent ¾ = D_eff/(D_eff+1) for D_eff=3 — the observed metabolic scaling expo"
- ⚠️ `D_eff` — "al sensitivity: D-sensitive — Kleiber's exponent ¾ = D_eff/(D_eff+1) for D_eff=3 — the observed metabolic scaling exponent is"
- ⚠️ `D_eff` — "y: D-sensitive — Kleiber's exponent ¾ = D_eff/(D_eff+1) for D_eff=3 — the observed metabolic scaling exponent is a direct rat"

**Section: What The Math Says**

- ⚠️ `D_eff` — 'c normalization constant. In the DS framework, alpha equals D_eff divided by (D_eff plus 1), where D_eff is the fractal dimen'
- ⚠️ `D_eff` — 'nstant. In the DS framework, alpha equals D_eff divided by (D_eff plus 1), where D_eff is the fractal dimensionality of the v'
- ⚠️ `D_eff` — 'mework, alpha equals D_eff divided by (D_eff plus 1), where D_eff is the fractal dimensionality of the vascular distribution '
- ⚠️ `D_eff` — 'illing network in three dimensions with fractal surface has D_eff equal to 3, giving alpha of 3/4 exactly. The exponent is no'
- ⚠️ `D_eff` — 'ganisms with different vascular geometries (higher or lower D_eff) should have different metabolic exponents, and this predic'
- ⚠️ `D_eff` — 'mparing alpha measured from oxygen consumption data against D_eff measured by micro-CT box-counting.'

---

## GT05  (12 flags)

**Section: What It Claims**

- · `entropy` — 'interaction between two masses arises from the entanglement entropy of a quantum spin network connecting them (Carney, PRX 15, '
- · `entropy` — 'he tendency of the spin system to maximise its entanglement entropy. Crucially, Carney derives testable predictions: the entang'

**Section: Mathematical Form**

- · `entropy` — 'ropic force: F = T ∂S_ent/∂r  where:   S_ent = entanglement entropy of spin network between two masses   T = effective temperat'

**Section: DS Cross-References**

- ⚠️ `Fisher information` — 'T04 (Bianconi — both use quantum information (entanglement, Fisher information) to derive gravity, but Carney focuses on testability while'
- · `entropy` — "ic derivation: the spin network is the microstructure whose entropy drives gravity). GT02 (Verlinde — Carney's entropic force m"
- · `Entropy` — 'Bianconi focuses on geometric structure). IT02 (Von Neumann Entropy — the entanglement entropy driving the force is a von Neuma'
- · `entropy` — 'ic structure). IT02 (Von Neumann Entropy — the entanglement entropy driving the force is a von Neumann entropy of the spin syst'
- · `entropy` — "the entanglement entropy driving the force is a von Neumann entropy of the spin system's reduced density matrix). BR01 (ER=EPR "

**Section: Mathematical Archetype**

- · `entropy` — "rinciple  Carney's spin entropic gravity is an optimization/entropy-maximisation model: the spin system evolves to maximise its"
- · `entropy` — 'model: the spin system evolves to maximise its entanglement entropy, and the resulting entropic force reproduces Newtonian grav'

**Section: What The Math Says**

- · `entropy` — 'f quantum degrees of freedom on a lattice. The entanglement entropy S-ent of the spin network depends on the separation r betwe'

**Section: Concept Tags**

- · `entropy` — '• spin entropic gravity • Carney • entanglement entropy • entropic force • spin network • testable quantum gravity '

---

## INFO2  (12 flags)

**Section: What It Claims**

- · `entropy` — 'Theorem (Source Coding Theorem, 1948): any data source with entropy H bits per symbol can be compressed to H bits per symbol on'
- · `entropy` — 'at rate H, impossible at rate < H. This theorem establishes entropy as the fundamental limit of data compression: no matter how'
- · `entropy` — 'lgorithm, you cannot losslessly compress a source below its entropy rate.'

**Section: Mathematical Form**

- · `entropy` — 'For i.i.d. source with entropy H(X):   Lossless compression rate R ≥ H(X)  (bits per symbo'

**Section: Constraint Category**

- · `entropy` — 'Informatic (In): entropy H is the hard lower bound on lossless compression. The theo'

**Section: DS Cross-References**

- · `Entropy` — 'INFO1 (Shannon Entropy — H(X) is the compression limit; the source coding theorem '
- · `entropy` — 'it; the source coding theorem is the operational meaning of entropy). INFO3 (Noisy-Channel Coding — the two fundamental theorem'

**Section: Mathematical Archetype**

- · `Entropy` — 'Mathematical archetype: thermodynamic-bound  Entropy H is the thermodynamic-style lower bound on lossless compre'
- · `entropy` — 'the limit), and (3) expressed in terms of a state function (entropy) rather than the specific process.'

**Section: What The Math Says**

- · `entropy` — 'e generating symbols independently from a distribution with entropy H bits per symbol, the source coding theorem states: there '
- · `entropy` — 'dewords to typical sequences requires nH bits — exactly the entropy times the length.'

**Section: Concept Tags**

- · `entropy` — '• source coding theorem • data compression • entropy rate • lossless compression • Huffman code • asymptotic equ'

---

## EM5  (11 flags)

**Section: What It Claims**

- · `symmetry` — "ows from Maxwell's equations and is equivalent to the gauge symmetry of electrodynamics — a Noether consequence (AM5). The same "

**Section: DS Cross-References**

- · `symmetry` — 'AM5 (Noether): gauge symmetry → charge conservation. The same PDE structure governs TD10 '

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — 'ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: The Continuity Equation (∂ρ/∂t + ∇'
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "
- · `symmetry` — ' statement of charge conservation, following from the gauge symmetry of electrodynamics. The same PDE form governs mass, energy,'
- · `symmetry` — 's the local charge conservation law — it follows from gauge symmetry via Noether (AM5). In D dimensions the same PDE structure h'

---

## HB05  (11 flags)

**Section: What It Claims**

- · `observer` — 'The Unruh effect states that a uniformly accelerating observer in flat Minkowski spacetime perceives the vacuum state of q'
- · `observer` — 'ere a is the proper acceleration (Unruh, 1976). An inertial observer sees empty space; an accelerating observer sees thermal par'
- · `observer` — '76). An inertial observer sees empty space; an accelerating observer sees thermal particles. This effect reveals that the partic'
- · `observer` — "eveals that the particle concept in quantum field theory is observer-dependent — the notion of a vacuum depends on the observer'"
- · `observer` — " observer-dependent — the notion of a vacuum depends on the observer's state of motion. The Unruh effect is the flat-spacetime v"

**Section: Constraint Category**

- · `observer` — 'geometry — the acceleration — with no free parameters. This observer-dependence of vacuum and temperature is a geometric constra'

**Section: What The Math Says**

- · `observer` — 'ressed in Rindler coordinates (natural for the accelerating observer) is an entangled state where each mode with Rindler frequen'
- · `observer` — 'uces a thermal density matrix at the Unruh temperature. The observer-dependence of the vacuum means that particles and temperatu'
- · `observer` — "and temperature are not absolute concepts but depend on the observer's causal structure."

**Section: Concept Tags**

- · `observer` — '• Unruh effect • Unruh temperature • accelerating observer • Rindler horizon • observer-dependent vacuum • thermofield'
- · `observer` — 'ruh temperature • accelerating observer • Rindler horizon • observer-dependent vacuum • thermofield double • thermal bath • equi'

---

## B5  (10 flags)

**Section: Formula**

- · `entropy` — '$$E_{\\min} = k_B T \\ln 2$$  per bit erased. The entropy floor for irreversible computation is $\\Delta S \\geq k_B \\l'

**Section: Why It Matters Here**

- ⚠️ `holographic` — 'he Landauer limit asymptotically. Third, it connects to the holographic bound (G3): if information capacity is bounded by boundary '

**Section: Phase Coherence Cost (Tier 3 ‡_p)**

- · `connection` — 'y disproportionately more to maintain low coherence.  *This connection is postulated from the Landauer principle by dimensional an'

**Section: Key Connections**

- ⚠️ `Holographic` — 'ency | | **couples to →** | [G3](G3_holographic_bound.md) | Holographic entropy bound times $k_B T \\ln 2$ gives total erasure cost '
- · `entropy` — 'ouples to →** | [G3](G3_holographic_bound.md) | Holographic entropy bound times $k_B T \\ln 2$ gives total erasure cost | | **de'

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

**Section: Concept Tags**

- · `entropy` — '• thermodynamic cost of computation • entropy and information • irreversible erasure • minimum energy per'
- · `entropy` — '• irreversible erasure • minimum energy per bit • Boltzmann entropy • computation thermodynamics • logical irreversibility • Ma'

---

## BIO3  (10 flags)

**Section: What It Claims**

- ⚠️ `Fisher information` — 'uctural bridge: additive genetic variance in fitness IS the Fisher information of the population about its environment. Natural selection '
- ⚠️ `Fisher information` — ' the population about its environment. Natural selection is Fisher information maximization.'

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'M6 (Fisher Information Rank): the metric of the DS information geometry is Fisher '
- ⚠️ `Fisher information` — 'rmation Rank): the metric of the DS information geometry is Fisher information — same as fitness in biological evolution. The structural b'
- ⚠️ `Fisher information` — ' in biological evolution. The structural bridge: maximizing Fisher information (M6) = maximizing fitness (BIO3). F3 (Gause competitive exc'
- ⚠️ `information geometry` — 'M6 (Fisher Information Rank): the metric of the DS information geometry is Fisher information — same as fitness in biological evolu'

**Section: Mathematical Archetype**

- ⚠️ `Fisher information` — 'dditive genetic variance — and additive genetic variance IS Fisher information. This structural bridge (fitness maximization = Fisher info'
- ⚠️ `Fisher information` — 'information. This structural bridge (fitness maximization = Fisher information maximization) directly connects evolutionary biology to the'
- ⚠️ `Fisher information` — 'ditive genetic variance in fitness — is D-sensitive because Fisher information is D-sensitive through the dimensionality of the parameter '

**Section: What The Math Says**

- · `entropy` — "ond law of thermodynamics, with fitness playing the role of entropy's inverse, always increasing under selection."

---

## BR03  (10 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'sconnects into two separate spacetimes. This result bridges holographic bounds (HB) and information theory (IT) directly: spacetime'

**Section: Mathematical Form**

- · `entropy` — 'L ⊗ |n⟩_R   ↔  connected two-sided black hole  Entanglement entropy: S_ent = S_BH = A(throat)/4G_N  Reduce entanglement: S_ent '

**Section: DS Cross-References**

- · `Entropy` — 'wormhole stretching until disconnection). IT02 (Von Neumann Entropy — the entanglement is measured by the von Neumann entropy o'
- · `entropy` — 'n Entropy — the entanglement is measured by the von Neumann entropy of the reduced state; zero von Neumann entropy implies disc'
- · `entropy` — ' von Neumann entropy of the reduced state; zero von Neumann entropy implies disconnected geometry). BR01 (ER = EPR — Van Raamsd'

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — 'changes from connected to disconnected. This is a geometric phase transition driven by information content — the most dramatic example o'

**Section: What The Math Says**

- · `entropy` — 'angled state between two copies of a CFT, with entanglement entropy equal to the Bekenstein-Hawking entropy S-BH equals A of th'
- · `entropy` — ', with entanglement entropy equal to the Bekenstein-Hawking entropy S-BH equals A of the throat divided by 4 G-N. In the dual b'
- · `entropy` — 'ith local unitaries or partial projections. As entanglement entropy decreases, the Ryu-Takayanagi surface area grows — the worm'
- · `connection` — 'connects into two separate AdS spacetimes with no geometric connection. The conclusion is that spacetime connectivity requires ent'

---

## BR05  (10 flags)

**Section: What It Claims**

- ⚠️ `holographic` — 'd point of the gravitational RG flow). This connects to the holographic principle: the reduction to 2 effective dimensions at the P'
- ⚠️ `holographic` — 'ctive dimensions at the Planck scale is consistent with the holographic bound S ∝ A, since area is a 2-dimensional quantity.'

**Section: Mathematical Form**

- ⚠️ `holographic` — 'upling G is dimensionless   d_s = 2: consistent with S ∝ A (holographic bound)   d_s flow: spectral dimension runs under gravitatio'

**Section: Constraint Category**

- ⚠️ `effective dimension` — 'eometric constraint that varies dynamically with scale. The effective dimension of spacetime is not fixed but runs — it is a scale-dependen'
- ⚠️ `holography` — 'mical geometry connects to the RG (scale dependence) and to holography (area-entropy scaling at d_s = 2).'
- · `entropy` — 'nnects to the RG (scale dependence) and to holography (area-entropy scaling at d_s = 2).'

**Section: DS Cross-References**

- ⚠️ `Holographic` — ' point where the gravitational coupling is marginal). HB03 (Holographic Principle — d_s ≈ 2 at the Planck scale is consistent with '
- ⚠️ `holography` — ' Principle — d_s ≈ 2 at the Planck scale is consistent with holography: the effective degrees of freedom are 2-dimensional at the '
- · `entropy` — 'are 2-dimensional at the smallest scales, matching the area-entropy scaling S ∝ A). GV1 (Einstein Field Equations — dimensional'

**Section: Mathematical Archetype**

- ⚠️ `holographic` — ', d_s = 4 (standard physics); at the Planck scale, d_s ≈ 2 (holographic, scale-invariant physics). The transition between these reg'

---

## EM14  (10 flags)

**Section: Constraint Category**

- ⚠️ `D_eff` — 's D-sensitive: if any of its components (ℏ, c, ε₀) run with D_eff via Ω_D, then α itself becomes a function of effective dime'

**Section: DS Cross-References**

- ⚠️ `D_eff` — '₀. OmD (Ω_D Scaling Operator): if ℏ, c, and ε₀ all run with D_eff via Ω_D, then α(D_eff) = e²/(4πε₀(D)ℏ(D)c(D)) — the fine st'
- ⚠️ `D_eff` — 'erator): if ℏ, c, and ε₀ all run with D_eff via Ω_D, then α(D_eff) = e²/(4πε₀(D)ℏ(D)c(D)) — the fine structure constant itsel'
- ⚠️ `D_eff` — 'ε₀(D)ℏ(D)c(D)) — the fine structure constant itself becomes D_eff-dependent, isomorphic to QED renormalization group running.'
- ⚠️ `D_eff` — '/128 at 91 GeV. If P3 is correct, this running reflects the D_eff gradient across energy scales, not just vacuum polarization'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'y scale q sets the observation resolution, which determines D_eff(q), which modulates ℏ, c, ε₀ via Ω_D, producing a D_eff-dep'
- ⚠️ `D_eff` — 'nes D_eff(q), which modulates ℏ, c, ε₀ via Ω_D, producing a D_eff-dependent α(D). The two descriptions — vacuum polarization '
- ⚠️ `D_eff` — 'endent α(D). The two descriptions — vacuum polarization and D_eff running — make identical predictions at D=4 but diverge at '
- ⚠️ `D_eff` — 'ake identical predictions at D=4 but diverge at non-integer D_eff, providing a testable distinction.  Dimensional sensitivity'
- ⚠️ `D_eff` — 'ction.  Dimensional sensitivity: D-sensitive — α depends on D_eff through all three of its non-charge components (ℏ, c, ε₀). '

---

## NE03  (10 flags)

**Section: What It Claims**

- · `entropy` — 'ct relationship between irreversible work, free energy, and entropy production at any scale.'
- · `fluctuation` — 'measurements. The Jarzynski equality, along with the Crooks fluctuation theorem, extends thermodynamics from the near-equilibrium r'

**Section: Mathematical Form**

- · `Entropy` — 'hange)  Dissipated work: W_diss = W − ΔF ≥ 0  (on average)  Entropy production: ⟨ΔS_tot⟩ = ⟨W_diss⟩/T ≥ 0'

**Section: Constraint Category**

- ⚠️ `monotonicity` — ' al., Science 296, 1832, 2002). The Jarzynski equality is a monotonicity statement: average dissipated work ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 '
- ⚠️ `monotonicity` — "rk ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 is non-negative, paralleling the monotonicity of black hole horizon area dA/dt ≥ 0 (Hawking's area theore"

**Section: DS Cross-References**

- · `entropy` — 'versibility statements: the area theorem says gravitational entropy increases; Jarzynski says ⟨W_diss⟩ ≥ 0. Both await a fluctu'
- · `Fluctuation` — "NE04 (Crooks Fluctuation Theorem — Crooks' theorem is the more fundamental result fr"
- · `Fluctuation` — "'s inequality: ⟨e^{−W/kT}⟩ ≥ e^{−⟨W⟩/kT} → ⟨W⟩ ≥ ΔF). NE05 (Fluctuation-Dissipation Theorem — Jarzynski generalises the FDT to far-"
- · `fluctuation` — 'ntropy increases; Jarzynski says ⟨W_diss⟩ ≥ 0. Both await a fluctuation-theorem generalisation in the gravitational case). IT03 (KL'

**Section: Concept Tags**

- · `fluctuation` — '• second law generalisation • single-molecule experiments • fluctuation theorem • path probability • information and irreversibilit'

---

## NE05  (10 flags)

**Section: What It Claims**

- · `fluctuation` — 'The fluctuation-dissipation theorem (FDT) states that the linear response o'

**Section: Constraint Category**

- · `fluctuation` — 'tities — response (how a system reacts to perturbation) and fluctuation (how a system spontaneously varies). The linking factor is '

**Section: DS Cross-References**

- · `entropy` — ' the temperature, and the positivity of dissipation ensures entropy production). NE01 (Prigogine — the FDT operates in the line'
- · `entropy` — "he linear near-equilibrium regime where Prigogine's minimum entropy production applies). STAT2 (Ergodic Theorem — the FDT requi"
- · `fluctuation` — 'he FDT is the linear (near-equilibrium) limit of the Crooks fluctuation theorem; Crooks generalises the FDT to arbitrary non-equili'
- · `fluctuation` — 'encodes the second law at the linear level: dissipation and fluctuation are linked by the temperature, and the positivity of dissip'

**Section: Mathematical Archetype**

- · `fluctuation` — 'ndition of thermal equilibrium: it states that the ratio of fluctuation to dissipation is fixed by the temperature. Systems violati'

**Section: What The Math Says**

- · `fluctuation` — 'The fluctuation-dissipation theorem in its Kubo form states that the dissip'
- · `fluctuation` — 'ver gamma is a special case: the diffusion coefficient D (a fluctuation property) equals the thermal energy k-B T divided by the dr'

**Section: Concept Tags**

- · `fluctuation` — '• fluctuation-dissipation theorem • Kubo formula • linear response • equi'

---

## TD5  (10 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — 'ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: The Fundamental Thermodynamic Rela'
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

**Section: What The Math Says**

- · `entropy` — 'ifferential equation for internal energy U as a function of entropy S, volume V, and particle numbers N_i. The temperature T eq'
- · `entropy` — 'rtial U / partial S at constant V and N (temperature is the entropy-based rate of energy change); pressure P equals minus parti'

**Section: Concept Tags**

- · `entropy` — '• fundamental thermodynamic relation • entropy internal energy volume • chemical potential • thermodynamic'

---

## TD6  (10 flags)

**Section: What It Claims**

- · `symmetry` — 'qually. The relations follow from microscopic time-reversal symmetry (detailed balance) and are the foundation of non-equilibriu'

**Section: Constraint Category**

- · `symmetry` — 'Thermodynamic (Th): symmetry of linear response near equilibrium; consequence of microsc'

**Section: DS Cross-References**

- · `entropy` — ' parent: Onsager relations are the linear-response limit of entropy production. Connects to M4 (Mori–Zwanzig): projection onto '

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'mics — a discrete symmetry that holds regardless of spatial D_eff.'
- · `symmetry` — 'modynamics.  Dimensional sensitivity: D-invariant — Onsager symmetry L_ij = L_ji follows from time-reversal symmetry of microsco'
- · `symmetry` — 't — Onsager symmetry L_ij = L_ji follows from time-reversal symmetry of microscopic dynamics — a discrete symmetry that holds re'
- · `symmetry` — 'time-reversal symmetry of microscopic dynamics — a discrete symmetry that holds regardless of spatial D_eff.'

**Section: What The Math Says**

- · `symmetry` — 'oefficient matrix L_ij is symmetric: L_ij equals L_ji. This symmetry means the coupling from thermal gradient to electric curren'
- · `symmetry` — 'cient). The relations follow from microscopic time-reversal symmetry and reduce the number of independent transport coefficients'

**Section: Concept Tags**

- · `symmetry` — 'ible thermodynamics • thermoelectric effect • time reversal symmetry transport'

---

## Q2  (9 flags)

**Section: Current Status**

- · `connection` — "is a genuinely open problem in noncommutative geometry. The connection between the spectral triple's $d_s$ and the fractal dimensi"

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — ' to noncommutative geometry via spectral triples, constrain D_eff in physical systems.  Dimensional sensitivity: D-sensitive '
- · `symmetry` — 'Mathematical archetype: symmetry-conservation  A constraint derived from the geometric symme'
- · `symmetry` — "metry-conservation  A constraint derived from the geometric symmetry of a system or Hilbert space. Noether's theorem is the mast"
- · `symmetry` — "Noether's theorem is the master statement: every continuous symmetry of the action generates a conserved current. Discrete symme"
- · `symmetry` — 'aws for quantum numbers. The Pauli exclusion principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions'
- · `symmetry` — 'xchange, constraining the entire structure of matter. Gauge symmetry generates charge conservation via Noether. Topological symm'
- · `Symmetry` — 'ed topological invariants (winding numbers, Chern classes). Symmetry-conservation laws are D-sensitive when the relevant symmetr'
- · `symmetry` — 'ymmetry-conservation laws are D-sensitive when the relevant symmetry group changes with dimension — for instance, the rotation g'

---

## QM2  (9 flags)

**Section: What It Claims**

- ⚠️ `D_eff` — 'ads ℏ as encoding the projection grain from higher to lower D_eff: the minimum uncertainty is the irreducible loss from dimen'
- · `observer` — 'aint on how much information about position and momentum an observer can extract simultaneously — a dimensional constraint on me'

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'certainty is information-theoretic, not just physical. Ax2 (D_eff): the uncertainty at a given scale is the projection loss f'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'connecting Heisenberg to Ax1 (Information Primacy) and Ax2 (D_eff).  Dimensional sensitivity: D-sensitive — ΔxΔp ≥ ℏ/2 is a b'
- ⚠️ `D_eff` — 'eading, ℏ encodes the projection grain from higher to lower D_eff.'
- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

**Section: Concept Tags**

- ⚠️ `duality` — 'uncertainty • position momentum uncertainty • wave-particle duality • Fourier conjugate variables • quantum measurement limit •'

---

## QM3  (9 flags)

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  A constraint derived from the geometric symme'
- · `symmetry` — "metry-conservation  A constraint derived from the geometric symmetry of a system or Hilbert space. Noether's theorem is the mast"
- · `symmetry` — "Noether's theorem is the master statement: every continuous symmetry of the action generates a conserved current. Discrete symme"
- · `symmetry` — 'aws for quantum numbers. The Pauli exclusion principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions'
- · `symmetry` — 'xchange, constraining the entire structure of matter. Gauge symmetry generates charge conservation via Noether. Topological symm'
- · `Symmetry` — 'ed topological invariants (winding numbers, Chern classes). Symmetry-conservation laws are D-sensitive when the relevant symmetr'
- · `symmetry` — 'ymmetry-conservation laws are D-sensitive when the relevant symmetry group changes with dimension — for instance, the rotation g'
- · `symmetry` — '  Applied to this entry: The Pauli Exclusion Principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions'
- · `symmetry` — 'sional sensitivity: D-sensitive — Fermion antisymmetry is a symmetry constraint on Hilbert space — in D dimensions the permutati'

---

## RG03  (9 flags)

**Section: What It Claims**

- ⚠️ `coarse-graining` — "onstants. Kadanoff's procedure makes the connection between coarse-graining and information processing explicit: replacing many spins b"
- ⚠️ `coarse-graining` — ' analogous to data processing. The information lost in each coarse-graining step is bounded by the data processing inequality.'
- · `connection` — "the same coupling constants. Kadanoff's procedure makes the connection between coarse-graining and information processing explicit"

**Section: Mathematical Form**

- ⚠️ `criticality` — 'n length: ξ → ξ/b after block-spin with scale factor b   At criticality: ξ = ∞  →  ξ/b = ∞  (self-similar)  Critical exponents from'

**Section: DS Cross-References**

- · `entropy` — 'reedom). TD3 (Second Law — block-spin coarse-graining is an entropy-increasing process: the block spin system has higher entrop'
- · `entropy` — 'ntropy-increasing process: the block spin system has higher entropy than the original, connecting RG to the second law).'
- ⚠️ `coarse-graining` — "ff's ideas). INFO4 (Data Processing Inequality — block-spin coarse-graining is a data-processing channel: replacing many spins by one b"
- ⚠️ `coarse-graining` — 'remaining degrees of freedom). TD3 (Second Law — block-spin coarse-graining is an entropy-increasing process: the block spin system has'

**Section: Concept Tags**

- ⚠️ `coarse-graining` — '• block spin • Kadanoff • real-space RG • coarse-graining • lattice spin system • critical point • scale invariance •'

---

## RG05  (9 flags)

**Section: What It Claims**

- · `entropy` — 'eld theory (degrees of freedom decrease) to thermodynamics (entropy increase under lossy compression).'
- ⚠️ `coarse-graining` — 'onstraint connecting information theory (irreversibility of coarse-graining) to quantum field theory (degrees of freedom decrease) to t'

**Section: Mathematical Form**

- ⚠️ `Monotonicity` — 'where:   E₄ = Euler density in 4D   W_{μνρσ} = Weyl tensor  Monotonicity: a_UV ≥ a_IR  (strict for non-trivial flow)  Free field val'

**Section: Constraint Category**

- ⚠️ `coarse-graining` — 'reedom in the same sense as the central charge does in 2D — coarse-graining can only reduce the number of effective degrees of freedom.'

**Section: DS Cross-References**

- · `entropy` — ' is the second law for RG flow in 4D: the a-function is the entropy-like quantity that can only decrease).'
- ⚠️ `coarse-graining` — 'ssing Inequality — the a-theorem, like the DPI, proves that coarse-graining (data processing) is irreversible: degrees of freedom (info'

**Section: Mathematical Archetype**

- ⚠️ `monotonicity` — 'athematical archetype: conservation-law  The a-theorem is a monotonicity law: a can decrease but never increase along RG flow. It is'
- · `symmetry` — 'tion — the dilaton is a Goldstone boson of broken conformal symmetry, and its scattering amplitude encodes the a-coefficient.'

**Section: What The Math Says**

- · `symmetry` — 'eld — the Goldstone boson of spontaneously broken conformal symmetry. The forward scattering amplitude of four dilatons at low e'

---

## CM1  (8 flags)

**Section: Constraint Category**

- ⚠️ `D_eff` — 'Ge): the laws encode motion through Euclidean D=3 space. In D_eff ≠ 3, the geometric structure of force and inertia changes —'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Newton's Laws of Motion define the"
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## EM10  (8 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'he node topology connects to C2 (Urban Scaling) and network D_eff arguments.'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Kirchhoff's Laws are the network-l"
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## ES2  (8 flags)

**Section: What It Claims**

- ⚠️ `coarse-graining` — 'f observation. This is a methodological statement about how coarse-graining (scale change) affects correlation structure.'

**Section: Constraint Category**

- ⚠️ `D_eff` — ' (Co/Di): scale-dependent correlation — a spatial analog of D_eff scale-dependence.'

**Section: DS Cross-References**

- ⚠️ `D_eff` — "Directly relevant to Ax2 (D_eff is scale-dependent: the observer's resolution changes measu"
- · `observer` — "Directly relevant to Ax2 (D_eff is scale-dependent: the observer's resolution changes measured correlations). ES1 (Tobler): "

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "cal constant matches a rational function of D, the system's effective dimension is being revealed. Examples: Stefan-Boltzmann's T^(D+1) exp"
- ⚠️ `D_eff` — "s dimensional-scaling is a potential site where a change in D_eff produces a measurable, predictive change in the law's outpu"
- ⚠️ `D_eff` — "nd on the scale of measurement, exactly as Ax2 predicts for D_eff.  Dimensional sensitivity: D-sensitive — Arbia's aggregatio"
- ⚠️ `D_eff` — 'lations depend on the resolution of observation, which is a D_eff-scaling effect.'

---

## FM3  (8 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Euler's Fluid Equations are the in"
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "
- · `symmetry` — ' equations are time-reversible; viscosity (FM1) breaks this symmetry. The transition is a regime change in the sense of H1 (Regi'

---

## GT06  (8 flags)

**Section: What It Claims**

- · `entropy` — '. Modern formulations connect it to the vacuum entanglement entropy: the induced gravitational action arises from the entanglem'

**Section: Mathematical Form**

- · `entropy` — 'Modern (entanglement): G_ind determined by the entanglement entropy   of quantum fields across a horizon:   S_ent = (A/4G_ind) '

**Section: DS Cross-References**

- · `Entropy` — ' induced by quantum fluctuations). HB02 (Bekenstein-Hawking Entropy — the modern interpretation of induced gravity connects the'
- · `entropy` — 'gravity connects the gravitational constant to entanglement entropy, which equals BH entropy for horizons).'
- · `entropy` — 'itational constant to entanglement entropy, which equals BH entropy for horizons).'

**Section: What The Math Says**

- · `entropy` — 'he gravitational constant is determined by the entanglement entropy of quantum fields across a horizon: S-ent equals A over 4 G'
- · `entropy` — "his connects Sakharov's 1968 idea to the Bekenstein-Hawking entropy and to Jacobson's 1995 thermodynamic derivation."

**Section: Concept Tags**

- · `entropy` — 'ional constant • quantum vacuum fluctuations • entanglement entropy • ultraviolet cutoff • effective field theory • vacuum ener'

---

## QM4  (8 flags)

**Section: What It Claims**

- ⚠️ `duality` — 'ssociated de Broglie wavelength λ = h/p. This wave-particle duality is the foundation of quantum mechanics — particles have wav'

**Section: Constraint Category**

- ⚠️ `D_eff` — 'he scale boundary between quantum and classical regimes — a D_eff transition boundary.'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'antum effects dominate. This boundary shifts if h runs with D_eff.  Dimensional sensitivity: D-sensitive — λ = h/p involves h'
- ⚠️ `D_eff` — 'ects become important, and this scale shifts if h runs with D_eff.'
- ⚠️ `duality` — 'ling disturbance. The quantum ℏ that sets the wave-particle duality scale is acted on by Ω_D in the DS framework.  Applied to t'
- ⚠️ `duality` — 'y: The de Broglie Wavelength (λ = h/p) is the wave-particle duality relation. It defines the quantum-classical boundary: when λ'

**Section: What The Math Says**

- ⚠️ `duality` — ' to the minus 29 meters — utterly negligible. Wave-particle duality predicted by de Broglie was confirmed by the Davisson-Germe'

**Section: Concept Tags**

- ⚠️ `duality` — '• de Broglie wavelength • matter wave • wave-particle duality • electron diffraction • particle momentum wavelength • Dav'

---

## RD3  (8 flags)

**Section: What It Claims**

- ⚠️ `D_eff` — 'dimensional scales. Ω_D acts on h directly — if h runs with D_eff, all quantum energy scales shift.'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — 'ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: The Planck-Einstein Relation (E = '
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## STAT3  (8 flags)

**Section: What It Claims**

- ⚠️ `criticality` — ' fall into different classes including DP and RFIM). Neural criticality (STDP-driven tuning to branching ratio sigma = 1 — Beggs-Pl'

**Section: Mathematical Form**

- · `symmetry` — 'a = thermodynamic state space     C = Hamiltonian + scaling symmetry     A = critical surface (RG fixed point)'

**Section: Constraint Category**

- · `symmetry` — 'f the whole operator; conservation laws are global; scaling symmetry is global; Bekenstein saturation depends on the total mass/'

**Section: DS Cross-References**

- · `Entropy` — 'ises the structural pattern across domains). STAT1 (Maximum Entropy Principle — MaxEnt provides the constraint framework; CCA i'
- · `entropy` — 'rations onto critical manifolds, which can be understood as entropy-extremal surfaces). MATH6 (Prime Number Theorem — the Riema'

**Section: What The Math Says**

- ⚠️ `criticality` — ' ordinary critical phenomena is the robustness: in standard criticality, you tune a parameter (temperature) to reach the critical p'

**Section: Concept Tags**

- ⚠️ `criticality` — 'bert-Polya conjecture • Montgomery-Odlyzko • self-organized criticality • Bak-Tang-Wiesenfeld • neural criticality • Beggs-Plenz • '
- ⚠️ `criticality` — '• self-organized criticality • Bak-Tang-Wiesenfeld • neural criticality • Beggs-Plenz • FDS State 2 • SV2/SV1 diagnostic • RG fixed'

---

## CM10  (7 flags)

**Section: What It Claims**

- · `symmetry` — 'nservation is the direct consequence of spatial translation symmetry: if the laws of physics are the same at every location in s'

**Section: Mathematical Form**

- · `symmetry` — 'Quantum:  ⟨p⟩ conserved when [H, p] = 0  (space-translation symmetry of Hamiltonian)'

**Section: Constraint Category**

- · `Symmetry` — 'Symmetry/Conservation (Sy/Co): momentum conservation is the Noether '
- · `symmetry` — 'ion is the Noether charge of continuous spatial translation symmetry. It constrains all collision, explosion, and flow problems '

**Section: DS Cross-References**

- · `symmetry` — " forces only). AM5 (Noether's Theorem — spatial translation symmetry of the Lagrangian L generates momentum as the conserved Noe"

**Section: What The Math Says**

- · `symmetry` — "ch occurs precisely when the system has spatial translation symmetry — the operator form of Noether's Theorem."

**Section: Concept Tags**

- · `symmetry` — "ewton's third law • Noether's theorem • spatial translation symmetry • collision • impulse • relativistic momentum • 4-momentum "

---

## CM6  (7 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Euler's Laws of Motion for rigid b"
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## DM4  (7 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Dalton's Law of Partial Pressures "
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## E2  (7 flags)

**Section: Formula**

- ⚠️ `eta` — '$$\\eta(t) = \\eta_0 \\cdot 2^{t/\\tau_K}$$  where $\\eta$ is computati'
- ⚠️ `eta` — '$$\\eta(t) = \\eta_0 \\cdot 2^{t/\\tau_K}$$  where $\\eta$ is computations per joule and $\\tau_K \\approx 1.57$ years '

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

**Section: What The Math Says**

- ⚠️ `eta` — 'Computational efficiency eta (computations per joule) doubles approximately every 1.57 y'
- ⚠️ `eta` — 'er joule) doubles approximately every 1.57 years, following eta(t) equals eta_0 times 2 to the power (t divided by tau_K). '

---

## EM2  (7 flags)

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  A constraint derived from the geometric symme'
- · `symmetry` — "metry-conservation  A constraint derived from the geometric symmetry of a system or Hilbert space. Noether's theorem is the mast"
- · `symmetry` — "Noether's theorem is the master statement: every continuous symmetry of the action generates a conserved current. Discrete symme"
- · `symmetry` — 'aws for quantum numbers. The Pauli exclusion principle is a symmetry constraint on Hilbert space geometry: fermion wavefunctions'
- · `symmetry` — 'xchange, constraining the entire structure of matter. Gauge symmetry generates charge conservation via Noether. Topological symm'
- · `Symmetry` — 'ed topological invariants (winding numbers, Chern classes). Symmetry-conservation laws are D-sensitive when the relevant symmetr'
- · `symmetry` — 'ymmetry-conservation laws are D-sensitive when the relevant symmetry group changes with dimension — for instance, the rotation g'

---

## FM2  (7 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Bernoulli's Principle is energy co"
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## HB04  (7 flags)

**Section: Mathematical Form**

- · `Entropy` — ' (15360π G²M²)  Evaporation time: t_evap = 5120πG²M³ / ℏc⁴  Entropy: S = A/4l_P² = 4πGM²k_B/ℏc  Spectrum: thermal (Planckian) a'

**Section: Constraint Category**

- · `entropy` — 's as thermodynamic objects with a well-defined temperature, entropy, and luminosity. The temperature is inversely proportional '

**Section: DS Cross-References**

- · `observer` — 'flat-spacetime analog of Hawking radiation: an accelerating observer sees thermal radiation at temperature T = ℏa/2πck_B). TD3 ('
- · `Entropy` — 'HB02 (Bekenstein-Hawking Entropy — Hawking radiation carries entropy at temperature T_H, val'
- · `entropy` — 'B02 (Bekenstein-Hawking Entropy — Hawking radiation carries entropy at temperature T_H, validating the BH entropy formula). HB0'
- · `entropy` — 'ation carries entropy at temperature T_H, validating the BH entropy formula). HB05 (Unruh Effect — the Unruh effect is the flat'
- · `entropy` — "a Hawking radiation tests the generalised second law: total entropy including radiation must increase). RD1 (Planck's Law — Haw"

---

## KC2  (7 flags)

**Section: What It Claims**

- · `symmetry` — ' a net flux at equilibrium. This follows from time-reversal symmetry in microscopic dynamics and is the molecular foundation of '

**Section: Constraint Category**

- · `symmetry` — 'Thermodynamic (Th): time-reversal symmetry of microscopic dynamics → no net circulation at equilibrium'

**Section: DS Cross-References**

- · `symmetry` — 'ocal relations). AM5 (Noether): time-reversal is a discrete symmetry → detailed balance. Connects to H1 (Regime): breakdown of d'

**Section: Mathematical Archetype**

- · `symmetry` — ' Detailed balance at equilibrium follows from time-reversal symmetry of microscopic dynamics — a discrete symmetry that is D-inv'
- · `symmetry` — 'time-reversal symmetry of microscopic dynamics — a discrete symmetry that is D-invariant.'

**Section: What The Math Says**

- · `symmetry` — 'otion machine. The principle follows from the time-reversal symmetry of the underlying microscopic equations of motion and is eq'

**Section: Concept Tags**

- · `symmetry` — 'ty • detailed balance • kinetic equilibrium • time reversal symmetry • forward reverse rates • equilibrium constant • thermodyna'

---

## KC4  (7 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "nges of scale. Whether conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's th"
- ⚠️ `D_eff` — "er conservation laws survive changes of effective dimension D_eff is an open question in the DS framework: Noether's theorem "
- ⚠️ `D_eff` — "ymmetry, which may be broken if physical constants run with D_eff.  Applied to this entry: Hess's Law states that enthalpy ch"
- · `symmetry` — "theorem, every conservation law corresponds to a continuous symmetry of the system's action: time-translation symmetry generates"
- · `symmetry` — "ontinuous symmetry of the system's action: time-translation symmetry generates energy conservation, spatial translation generate"
- · `symmetry` — 'rotation generates angular momentum conservation, and gauge symmetry generates charge conservation. Conservation laws constrain '
- · `symmetry` — "e DS framework: Noether's theorem requires time-translation symmetry, which may be broken if physical constants run with D_eff. "

---

## CM11  (6 flags)

**Section: What It Claims**

- · `symmetry` — "ther's Theorem, this is the consequence of time-translation symmetry: physical laws that do not change with time imply energy co"

**Section: Constraint Category**

- · `Symmetry` — 'Symmetry/Conservation (Sy/Co): energy conservation is the Noether ch'
- · `symmetry` — 'ergy conservation is the Noether charge of time-translation symmetry. It is the master scalar constraint on all physical process'

**Section: DS Cross-References**

- · `symmetry` — "e by the system). AM5 (Noether's Theorem — time-translation symmetry of the Lagrangian generates the Hamiltonian H as the conser"

**Section: What The Math Says**

- · `symmetry` — 'lisations of the same Noether charge under time-translation symmetry.'

**Section: Concept Tags**

- · `symmetry` — "nservation of energy • Noether's theorem • time-translation symmetry • Hamiltonian • kinetic energy • potential energy • first l"

---

## CS11  (6 flags)

**Section: Constraint Category**

- · `entropy` — 'es the lower bound. This is a direct application of Shannon entropy to algorithm complexity.'

**Section: DS Cross-References**

- · `Entropy` — 'INFO1 (Shannon Entropy — the proof uses entropy: log₂(n!) bits are needed to sort '
- · `entropy` — 'INFO1 (Shannon Entropy — the proof uses entropy: log₂(n!) bits are needed to sort n elements; the lower bou'
- · `entropy` — ' bits are needed to sort n elements; the lower bound is the entropy of the uniform distribution over n! permutations). INFO2 (S'
- · `entropy` — 'e coding: you cannot do better than H bits to distinguish H-entropy outcomes; sorting is a special case of optimal encoding of '

**Section: Concept Tags**

- · `entropy` — 'heoretic lower bound • merge sort • heap sort • permutation entropy • Stirling approximation • optimal sorting'

---

## CS4  (6 flags)

**Section: Constraint Category**

- ⚠️ `phase transition` — 'sy (satisfiable, 2-SAT) and hard (3-SAT) is a computational phase transition analogous to physical phase transitions.'

**Section: DS Cross-References**

- · `Entropy` — 't encoding for a general source is NP-hard). STAT1 (Maximum Entropy Principle — MaxEnt inference can become NP-hard when the co'

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — 'al archetype: threshold-transition  NP-completeness marks a phase transition in computational difficulty. For constraint satisfaction pr'
- ⚠️ `phase transition` — ' rare satisfying assignments exist. This is a computational phase transition with critical exponents, analogous to thermodynamic phase t'

**Section: What The Math Says**

- ⚠️ `phase transition` — 'y discovered the same result in the Soviet Union. The k-SAT phase transition occurs at clause-to-variable ratio approximately 4.27 for 3'

**Section: Concept Tags**

- ⚠️ `phase transition` — 'sfiability • polynomial reduction • P vs NP • computational phase transition • Boolean formula • NP-hard • constraint satisfaction • com'

---

## EM11  (6 flags)

**Section: Constraint Category**

- · `entropy` — 'Thermodynamic (Th): irreversible dissipation — entropy production at rate P/T.'

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'
- · `entropy` — 'l sensitivity: D-invariant — Joule heating P = I²R produces entropy at rate P/T — the dissipation is a first-law consequence th'

**Section: What The Math Says**

- · `entropy` — 'lectrical energy into disordered thermal energy, increasing entropy. The effect is the microscopic mechanism of resistance: ele'

---

## MATH5  (6 flags)

**Section: What It Claims**

- ⚠️ `duality` — 'antaneous rate of change and accumulated area — as a single duality, founding all of analysis.'

**Section: Constraint Category**

- ⚠️ `duality` — "eometry (tangent) and global geometry (area) are dual. This duality is extended to all dimensions by the Generalized Stokes' Th"

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  The FTC expresses a deep symmetry: the operat'
- · `symmetry` — ' archetype: symmetry-conservation  The FTC expresses a deep symmetry: the operations of differentiation (local, instantaneous) a'
- · `symmetry` — '(global, cumulative) are exact inverses of each other. This symmetry is a conservation law in the space of functions: the inform'

**Section: Concept Tags**

- ⚠️ `duality` — 'ndamental theorem of calculus • differentiation integration duality • antiderivative • Riemann integral • Newton Leibniz • area'

---

## MATH7  (6 flags)

**Section: Mathematical Archetype**

- · `symmetry` — "Mathematical archetype: symmetry-conservation  Euler's formula reveals a deep symmetry: e^{i"
- · `symmetry` — "type: symmetry-conservation  Euler's formula reveals a deep symmetry: e^{iθ} has unit modulus for all real θ — rotation in the c"
- · `symmetry` — "otations U(1) = {e^{iθ} : θ ∈ ℝ} is the simplest continuous symmetry group. Noether's theorem (AM5) links this U(1) symmetry to "
- · `symmetry` — "ous symmetry group. Noether's theorem (AM5) links this U(1) symmetry to conservation of a quantity — in electromagnetism, U(1) g"
- · `symmetry` — 'onservation of a quantity — in electromagnetism, U(1) gauge symmetry is the source of charge conservation.'

**Section: Concept Tags**

- · `symmetry` — 'otation operator • Fourier analysis • wave mechanics • U(1) symmetry • complex plane • phase'

---

## QM1  (6 flags)

**Section: What It Claims**

- ⚠️ `D_eff` — 'sical Hamiltonian. The DS framework conjectures ℏ runs with D_eff — if true, quantum evolution itself becomes scale-dependent'

**Section: Constraint Category**

- ⚠️ `D_eff` — 'Dimensional (Di): ℏ is the quantum of action; D_eff governs how much of phase space is accessible at each resol'

**Section: DS Cross-References**

- ⚠️ `holographic` — 'on-Jacobi) reduces to Schrödinger in the quantum limit. G3 (holographic complexity): solving Schrödinger in high-D Hilbert space is'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'setting the scale of quantum discretization. If ℏ runs with D_eff as Ω_D predicts, all quantum phenomena become D-sensitive. '
- ⚠️ `D_eff` — 'r equation contains ℏ explicitly — Ω_D predicts ℏ runs with D_eff, shifting energy levels, tunneling rates, and the boundary '
- ⚠️ `duality` — 'ling disturbance. The quantum ℏ that sets the wave-particle duality scale is acted on by Ω_D in the DS framework.  Applied to t'

---

## STAT1  (6 flags)

**Section: What It Claims**

- · `entropy` — 'istent with known constraints, the one with maximum Shannon entropy is the least-biased choice — it incorporates exactly the av'

**Section: Constraint Category**

- · `entropy` — 'ential, Boltzmann, Poisson) comprises precisely the maximum entropy distributions under their respective moment constraints. Ma'

**Section: DS Cross-References**

- · `Entropy` — 'INFO1 (Shannon Entropy — MaxEnt maximises H; the entropy H is the objective functi'
- · `entropy` — 'INFO1 (Shannon Entropy — MaxEnt maximises H; the entropy H is the objective function). TD3 (Second Law of Thermodyna'

**Section: What The Math Says**

- · `entropy` — 'alisation plus any known expected values). Maximise Shannon entropy H equals minus sum of p-i log p-i subject to these constrai'

**Section: Concept Tags**

- · `entropy` — '• maximum entropy principle • MaxEnt • Jaynes • exponential family • least bi'

---

## STAT2  (6 flags)

**Section: Mathematical Form**

- · `Entropy` — 'T^{-1}(A) = A ⟹ μ(A) ∈ {0,1}  (only trivial invariant sets) Entropy: h(T) = lim_{n→∞} (1/n) H(x_0, x_1, ..., x_{n-1})  (Kolmogo'
- · `entropy` — 'im_{n→∞} (1/n) H(x_0, x_1, ..., x_{n-1})  (Kolmogorov-Sinai entropy)'

**Section: DS Cross-References**

- · `Entropy` — ' LLN even when the X_t are not independent). INFO1 (Shannon Entropy — Kolmogorov-Sinai (KS) entropy h(T) is the entropy product'
- · `entropy` — 'ndependent). INFO1 (Shannon Entropy — Kolmogorov-Sinai (KS) entropy h(T) is the entropy production rate of an ergodic dynamical'
- · `entropy` — 'Shannon Entropy — Kolmogorov-Sinai (KS) entropy h(T) is the entropy production rate of an ergodic dynamical system; it measures'

**Section: Concept Tags**

- · `entropy` — 'asure • statistical mechanics foundation • Kolmogorov-Sinai entropy • dynamical systems'

---

## TD8  (6 flags)

**Section: What It Claims**

- ⚠️ `η` — '_hot and T_cold can be more efficient than a Carnot engine: η ≤ 1 − T_cold/T_hot. The Carnot engine is reversible and ach'

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- ⚠️ `η` — '.  Dimensional sensitivity: D-invariant — Carnot efficiency η = 1 − T_cold/T_hot is a ratio of absolute temperatures — D-'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

**Section: What The Math Says**

- ⚠️ `eta` — 'icient than the reversible Carnot cycle: maximum efficiency eta equals 1 minus T_cold divided by T_hot. The Carnot cycle co'

---

## FM1  (5 flags)

**Section: What It Claims**

- ⚠️ `D_eff` — 'll scales). This D-dependence makes Navier-Stokes a natural D_eff test bed.'

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'nnects to A1 (Square-Cube): viscous dissipation scales with D_eff. TD7 (Boltzmann equation) → Navier-Stokes via moments. D2 ('

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — 'tween D=2 and D=3, providing a direct experimental probe of effective dimension.  Dimensional sensitivity: D-sensitive — Navier-Stokes is s'
- ⚠️ `D_eff` — 'mental difference in diffusive behavior that directly tests D_eff.  Applied to this entry: Navier-Stokes Equations are the no'
- ⚠️ `D_eff` — ' dependence of cascade direction makes FM1 a direct test of D_eff.'

---

## FM5  (5 flags)

**Section: What It Claims**

- ⚠️ `η` — "re of radius r moving at velocity v in a fluid of viscosity η is F = 6πηrv. Linear in velocity — no turbulence. Stokes' l"

**Section: What The Math Says**

- ⚠️ `eta` — 'r moving at velocity v through a fluid of dynamic viscosity eta: F_drag equals 6 pi eta r v. The linear velocity dependence'
- ⚠️ `eta` — 'hrough a fluid of dynamic viscosity eta: F_drag equals 6 pi eta r v. The linear velocity dependence (as opposed to v-square'
- ⚠️ `eta` — 'ent drag) holds at low Reynolds numbers Re equals rho v r / eta much less than 1, where viscous forces dominate inertia. Th'
- ⚠️ `eta` — ' times (rho_particle minus rho_fluid) times g divided by (9 eta), obtained by balancing Stokes drag against gravitational f'

---

## GT08  (5 flags)

**Section: What It Claims**

- · `observer` — 'lly indistinguishable from the effects of acceleration — an observer in a uniformly accelerating elevator cannot distinguish the'

**Section: Mathematical Archetype**

- · `symmetry` — 'archetype: conservation-law  The equivalence principle is a symmetry statement: the local equivalence of gravity and acceleratio'
- · `symmetry` — 'he local equivalence of gravity and acceleration is a gauge symmetry (diffeomorphism invariance) of the gravitational field. Lik'
- · `symmetry` — "he unique second-order field equations consistent with this symmetry (Lovelock's theorem)."

**Section: What The Math Says**

- ⚠️ `eta` — ' so that the metric g-mu-nu reduces to the Minkowski metric eta-mu-nu, with corrections of order x-squared — meaning the ef'

---

## GT09  (5 flags)

**Section: Constraint Category**

- ⚠️ `phase transition` — 'formation has the same structural character as a continuous phase transition: the critical solution is a fixed point of the RG-like scal'
- · `symmetry` — 'e critical solution is a fixed point of the RG-like scaling symmetry Z -> Z(e^Delta r, e^Delta t), and gamma is determined by th'

**Section: DS Cross-References**

- · `entropy` — "Derivation — critical collapse occurs within GR; Jacobson's entropy-area framework provides the thermodynamic interpretation of"
- · `Entropy` — 'ation of the formation threshold). HB02 (Bekenstein-Hawking Entropy — BH formation saturates S = A/4; Choptuik scaling describe'
- · `entropy` — ' S = A/4; Choptuik scaling describes how mass and therefore entropy approach zero continuously at the critical threshold in Typ'

---

## INFO3  (5 flags)

**Section: Mathematical Form**

- · `entropy` — 'io) Binary symmetric channel: C = 1 − H_b(p)  (H_b = binary entropy, p = crossover probability) Capacity-cost: R < C ⟺ reliable'

**Section: DS Cross-References**

- · `Entropy` — 'INFO1 (Shannon Entropy — C = max I(X;Y) = max[H(Y) − H(Y|X)]; capacity is the maxi'
- · `entropy` — 'H(Y) − H(Y|X)]; capacity is the maximum reduction in output entropy achievable by the input). INFO2 (Source Coding — source cod'

**Section: Mathematical Archetype**

- · `entropy` — 'rm C = (½)log₂(1+SNR) has a deep analogy with thermodynamic entropy: capacity is logarithmic in the signal-to-noise ratio just '
- · `entropy` — 'apacity is logarithmic in the signal-to-noise ratio just as entropy is logarithmic in the number of states. The coding theorem '

---

## MATH1  (5 flags)

**Section: DS Cross-References**

- ⚠️ `Fisher Information` — 'ce D_KL(posterior||prior) measures information gained). M6 (Fisher Information — Fisher information is the curvature of the log-likelihood'
- ⚠️ `Fisher information` — 'ior) measures information gained). M6 (Fisher Information — Fisher information is the curvature of the log-likelihood; Bayes and Fisher ar'
- · `Entropy` — 'INFO1 (Shannon Entropy — Bayesian updating minimises expected posterior entropy; t'
- · `entropy` — 'on Entropy — Bayesian updating minimises expected posterior entropy; the KL divergence D_KL(posterior||prior) measures informat'
- · `Entropy` — "lies Bayes' theorem to molecular evolution). STAT1 (Maximum Entropy Principle — MaxEnt provides the least-informative prior; Ba"

---

## RG01  (5 flags)

**Section: What It Claims**

- ⚠️ `criticality` — "nd to scale-invariant theories (conformal field theories at criticality). Wilson's RG explains universality: why systems with compl"
- ⚠️ `coarse-graining` — 'al theories change as one varies the scale of observation — coarse-graining from microscopic to macroscopic descriptions (Wilson, Rev. '

**Section: DS Cross-References**

- ⚠️ `coarse-graining` — "in is the real-space version of Wilson's momentum-space RG: coarse-graining by spatially averaging). RG04 (Zamolodchikov c-theorem — th"
- ⚠️ `coarse-graining` — 'ng irreversibility). INFO4 (Data Processing Inequality — RG coarse-graining is a form of data processing: integrating out degrees of fr'

**Section: Concept Tags**

- ⚠️ `coarse-graining` — '• renormalisation group • Wilson RG • coarse-graining • effective theory • scale dependence • universality • fixe'

---

## C3  (4 flags)

**Section: Why It Matters Here**

- · `symmetry` — 'na (physics), exponents depend on spatial dimension $d$ and symmetry class. This is the link to the DFIG framework: if $\\alpha$ '

**Section: What's Established**

- · `entropy` — 'zed criticality (Bak, Tang & Wiesenfeld, 1987), and maximum entropy under moment constraints (Jaynes, 1957). The Euler-Maschero'
- ⚠️ `criticality` — 'ential attachment (Barabási & Albert, 1999), self-organized criticality (Bak, Tang & Wiesenfeld, 1987), and maximum entropy under m'

**Section: References**

- ⚠️ `criticality` — '- Bak, P., Tang, C. & Wiesenfeld, K. (1987). Self-organized criticality. *Physical Review Letters*, 59, 381–384.'

---

## CM2  (4 flags)

**Section: Constraint Category**

- ⚠️ `D_eff` — 'cales as r^(1−D). Ω_D predicts G is not fixed but runs with D_eff.'

**Section: DS Cross-References**

- ⚠️ `D_eff` — "imensional Redshift — alternative to ΛCDM built on changing D_eff). CM5 (Kepler's 3rd law derives from this). Coulomb's law ("

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — "king inverse-square laws among the most sensitive probes of D_eff.  Applied to this entry: Newton's Law of Universal Gravitat"
- ⚠️ `D_eff` — 'l force scales as r^(−D+1). Ω_D predicts G itself runs with D_eff.'

---

## CS5  (4 flags)

**Section: Constraint Category**

- ⚠️ `effective dimension` — '-level-work dominated. The critical exponent log_b a is the effective dimension of the recursion tree — the fractal dimension of the recurs'

**Section: DS Cross-References**

- ⚠️ `effective dimension` — 'power law exponent; in both cases the exponent reflects the effective dimension of the underlying structure). H2 (Fractal Dimension — log_b'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'y the same structure as metabolic scaling B ∝ M^α where α = D_eff/(D_eff+1). The recursion tree has a fractal structure with '
- ⚠️ `D_eff` — 'ame structure as metabolic scaling B ∝ M^α where α = D_eff/(D_eff+1). The recursion tree has a fractal structure with dimensi'

---

## D2  (4 flags)

**Section: Why It Matters Here**

- · `symmetry` — 'rties of a fixed point that attracts all maps with the same symmetry and dimensionality. Under the DFIG axioms, the spatial dime'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "cal constant matches a rational function of D, the system's effective dimension is being revealed. Examples: Stefan-Boltzmann's T^(D+1) exp"
- ⚠️ `effective dimension` — 'ing cascades converge at universal constants that depend on effective dimension. It is the prototypical example of dimension-encoding throu'
- ⚠️ `D_eff` — "s dimensional-scaling is a potential site where a change in D_eff produces a measurable, predictive change in the law's outpu"

---

## F1  (4 flags)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'onal in the informatic sense but does not depend on spatial D_eff.'
- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

---

## F2  (4 flags)

**Section: What's Established**

- · `connection` — "'essential nutrient' rather than citing Liebig by name; the connection between his framework and Liebig's law of the minimum was m"

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

---

## FL6  (4 flags)

**Section: DS Cross-References**

- · `Entropy` — 'en truth-functional connectives. Connects to INFO1 (Shannon Entropy): valuations are complete Boolean state descriptions — a va'
- · `entropy` — 'ⁿ possible states, the exact state space over which Shannon entropy is computed.'

**Section: What The Math Says**

- · `entropy` — 'pecifies one of 2ⁿ equally possible Boolean states; Shannon entropy H = −∑pᵢ log pᵢ measures uncertainty over this state space.'
- · `connection` — 'tion, identifying which sets are functionally complete. The connection to Shannon information is precise: a valuation over n atoms'

---

## GV3  (4 flags)

**Section: What It Claims**

- · `entropy` — 'The Bekenstein bound (G3 in DS wiki) generalizes this to an entropy-area law, bounding information by geometric surface.'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — "king inverse-square laws among the most sensitive probes of D_eff.  Applied to this entry: Gauss's Law for Gravity is the New"
- ⚠️ `D_eff` — 'identical structure to EM1 (Gauss electricity). G runs with D_eff through Ω_D.'

**Section: Concept Tags**

- · `symmetry` — 'tional flux • enclosed mass • Newtonian gravity • spherical symmetry • gravitational field lines • inverse square'

---

## KC5  (4 flags)

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

**Section: Concept Tags**

- · `entropy` — 'Hoff equation • equilibrium constant temperature • enthalpy entropy compensation • thermodynamic driving force'

---

## MATH2  (4 flags)

**Section: DS Cross-References**

- · `Entropy` — 'e distribution of additive genetic effects). INFO1 (Shannon Entropy — the Gaussian maximises entropy for fixed mean and varianc'
- · `entropy` — 'c effects). INFO1 (Shannon Entropy — the Gaussian maximises entropy for fixed mean and variance; the CLT is why maximum-entropy'
- · `entropy` — 'entropy for fixed mean and variance; the CLT is why maximum-entropy distributions arise so naturally). TD7 (Boltzmann Equation '

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — ',1) as a fixed point. This is the probabilistic analog of a phase transition — many microscopic distributions flow to the same macroscop'

---

## RD2  (4 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'his structurally analogous to C1 (Kleiber: exponent encodes D_eff of vascular network). Ω_D: both h and c enter σ — running c'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "cal constant matches a rational function of D, the system's effective dimension is being revealed. Examples: Stefan-Boltzmann's T^(D+1) exp"
- ⚠️ `effective dimension` — 't becomes T^(D+1), making this one of the clearest tests of effective dimension in radiation physics.'
- ⚠️ `D_eff` — "s dimensional-scaling is a potential site where a change in D_eff produces a measurable, predictive change in the law's outpu"

---

## TD13  (4 flags)

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

**Section: What The Math Says**

- ⚠️ `eta` — ' any specific thermometric substance. The Carnot efficiency eta equals 1 minus T_cold over T_hot sets the maximum fraction '

---

## B3  (3 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "cal constant matches a rational function of D, the system's effective dimension is being revealed. Examples: Stefan-Boltzmann's T^(D+1) exp"
- ⚠️ `D_eff` — "s dimensional-scaling is a potential site where a change in D_eff produces a measurable, predictive change in the law's outpu"
- ⚠️ `D_eff` — '_B — both acted on by Ω_D — shifting the spectral peak with D_eff.'

---

## CM5  (3 flags)

**Section: Constraint Category**

- ⚠️ `D_eff` — 'Geometric (Ge): exponent 3/2 = D_eff / 2 for D=3. Changes if gravitational potential dimension c'

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'exponents. CM2 (gravitation — parent law). Ω_D (G runs with D_eff, changing the proportionality constant).'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — 'th are power laws whose exponents are rational functions of effective dimension.  Dimensional sensitivity: D-sensitive — T² ∝ a³ encodes th'

---

## CS6  (3 flags)

**Section: DS Cross-References**

- · `Entropy` — 'ersions of the same time-frequency duality). INFO1 (Shannon Entropy — the information content per sample is log₂(1+SNR) bits; N'
- ⚠️ `duality` — 'e classical and quantum versions of the same time-frequency duality). INFO1 (Shannon Entropy — the information content per samp'

**Section: Concept Tags**

- ⚠️ `duality` — ' • sinc interpolation • sampling frequency • time-frequency duality • reconstruction theorem • Shannon-Nyquist'

---

## DM3  (3 flags)

**Section: DS Cross-References**

- ⚠️ `Fisher information` — 'dy-force fields. Relevant to X2 (Information Geometry): the Fisher information metric on statistical manifolds has a Lamm-like evolution e'
- ⚠️ `Information Geometry` — 'ization of DM1 (Fick) to body-force fields. Relevant to X2 (Information Geometry): the Fisher information metric on statistical manifolds ha'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'mental difference in diffusive behavior that directly tests D_eff.  Applied to this entry: The Lamm Equation generalizes Fick'

---

## EM1  (3 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'geometric structure as CM2 (gravitation). Ω_D: ε₀ runs with D_eff through c = 1/√(ε₀μ₀). Part of unified Maxwell system (EM1–'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — "king inverse-square laws among the most sensitive probes of D_eff.  Applied to this entry: Gauss's Law for Electricity is one"
- ⚠️ `D_eff` — 'rse-square in D=3 becomes inverse-cube in D=4. ε₀ runs with D_eff through c = 1/√(ε₀μ₀).'

---

## EM6  (3 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — "re D=3 Gauss-law consequences. Ω_D acts on ε₀ → k runs with D_eff. EM1 (Gauss's law) is the field formulation."

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — "king inverse-square laws among the most sensitive probes of D_eff.  Applied to this entry: Coulomb's Law is the electrostatic"
- ⚠️ `D_eff` — "ntical in structure to Newton's gravity (CM2). ε₀ runs with D_eff."

---

## EM7  (3 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'Static limit of EM4 (Ampère–Maxwell). Ω_D: μ₀ runs with D_eff through c = 1/√(ε₀μ₀).'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'king inverse-square laws among the most sensitive probes of D_eff.  Applied to this entry: The Biot-Savart Law is the magneto'
- ⚠️ `D_eff` — 'uct structure is D=3-specific and the coupling μ₀ runs with D_eff through c = 1/√(ε₀μ₀).'

---

## ES1  (3 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'Spatial correlation decay encodes D_eff of the geographic network substrate — directly testable wit'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'of the geographic network — making it a geographic probe of D_eff analogous to fractal dimension (H2).  Dimensional sensitivi'
- ⚠️ `D_eff` — 'ivity: D-sensitive — Spatial correlation decay rate encodes D_eff of the geographic substrate — a slower decay suggests highe'

---

## ES14  (3 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — "al axis (time). Connects structurally to the DS framework's D_eff as a scale-dependent coordinate system, where spatial and t"
- · `symmetry` — 'A space-time translation symmetry: the horizontal axis (space) maps to the vertical axis (tim'

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — 'al sequences — a space-time transformation that encodes the effective dimension of the depositional environment.'

---

## ES6  (3 flags)

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

---

## FL21  (3 flags)

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  Identity is the symmetry relation: a = b mean'
- · `symmetry` — 'hematical archetype: symmetry-conservation  Identity is the symmetry relation: a = b means a and b are interchangeable in all co'
- · `symmetry` — 'conserves truth under substitution of identicals — the same symmetry-conservation principle that underlies topic neutrality (FL3'

---

## FL3  (3 flags)

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  Topic neutrality is a symmetry of logical for'
- · `symmetry` — 'cal archetype: symmetry-conservation  Topic neutrality is a symmetry of logical form under substitution of non-logical vocabular'
- · `symmetry` — 'tion group. Just as physical laws conserve quantities under symmetry transformations, logical validity is conserved under all un'

---

## FL9  (3 flags)

**Section: Mathematical Form**

- ⚠️ `Monotonicity` — 'Decision: 2^k rows where k is the number of distinct atoms. Monotonicity: if Γ ⊨ B then Γ∪Δ ⊨ B.'

**Section: What The Math Says**

- ⚠️ `Monotonicity` — 'ntic consequence apparatus to a single decidable predicate. Monotonicity holds: adding premises never destroys entailment. Compactne'

**Section: Concept Tags**

- ⚠️ `monotonicity` — ' propositional logic • logical implication • decidability • monotonicity • compactness • deductive inference'

---

## GV1  (3 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'ional Redshift): alternative to ΛCDM built on Ω_D acting on D_eff. Ω_D: both G and c in the coupling factor 8πG/c⁴ are dimens'
- ⚠️ `Holographic` — " G and c in the coupling factor 8πG/c⁴ are dimensional. G3 (Holographic Complexity Bound) derives from GR's holographic structure."
- ⚠️ `holographic` — "sional. G3 (Holographic Complexity Bound) derives from GR's holographic structure."

---

## INFO5  (3 flags)

**Section: DS Cross-References**

- · `Entropy` — 'INFO1 (Shannon Entropy — E[K(X)] ≈ H(X) for typical ensembles; K is the individual'
- · `entropy` — 'es; K is the individual-sequence analog of ensemble Shannon entropy). INFO2 (Source Coding — lossless compression to length K(x'

**Section: What The Math Says**

- · `entropy` — ' K(X) equals H(X) plus terms of order log n — K and Shannon entropy agree for typical ensembles up to lower-order terms.'

---

## KC3  (3 flags)

**Section: Mathematical Archetype**

- ⚠️ `η` — 'hable states. Examples span all domains: Carnot efficiency (η ≤ 1 − T_cold/T_hot), Landauer erasure cost (E ≥ k_BT ln2 pe'
- · `entropy` — 'y mechanism, no matter how clever, because they follow from entropy, energy conservation, and the statistics of distinguishable'
- · `entropy` — 'structure: a system trying to exceed the bound must violate entropy non-decrease, energy conservation, or the distinguishabilit'

---

## OP2  (3 flags)

**Section: Constraint Category**

- · `symmetry` — 'Geometric (Ge): symmetry of path length with respect to surface normal.'

**Section: Mathematical Archetype**

- · `symmetry` — 'cts the angle of incidence and reflection. It expresses the symmetry of optical path length across the surface normal.  Dimensio'
- · `symmetry` — 'nsional sensitivity: D-sensitive — θ_i = θ_r is a geometric symmetry of path length with respect to the surface normal — in D di'

---

## Q1  (3 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "cal constant matches a rational function of D, the system's effective dimension is being revealed. Examples: Stefan-Boltzmann's T^(D+1) exp"
- ⚠️ `D_eff` — "s dimensional-scaling is a potential site where a change in D_eff produces a measurable, predictive change in the law's outpu"
- ⚠️ `D_eff` — 'ctal dimension from power-law exponents is definitionally a D_eff measurement — the question is whether the inference is reli'

---

## TD14  (3 flags)

**Section: DS Cross-References**

- · `symmetry` — 'from pairwise intermolecular potentials; KC2 constrains the symmetry of these collision processes).'

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — 'd, spinodal, gas solutions) — the hallmark of a first-order phase transition. The critical point is where the three roots merge: (∂P/∂V)'

**Section: Concept Tags**

- ⚠️ `phase transition` — ' intermolecular forces • excluded volume • critical point • phase transition • law of corresponding states • equation of state • van der'

---

## TD7  (3 flags)

**Section: What It Claims**

- · `entropy` — ' (∂f/∂t)_coll. The H-theorem (Boltzmann) shows this implies entropy increases: the bridge from microscopic reversibility to mac'

**Section: Constraint Category**

- · `entropy` — 'Thermodynamic/Informatic (Th/In): the H-theorem is an entropy-production statement; f is a probability distribution — inf'

**Section: What The Math Says**

- · `entropy` — 'inus (f minus f_eq) divided by tau. The H-theorem shows the entropy functional H equals minus integral of f ln(f) dp never decr'

---

## A2  (2 flags)

**Section: Why It Matters Here**

- ⚠️ `Fisher Information` — 'ty ($D_{\\text{eff}}$), measured not by ruler scaling but by Fisher Information Rank. The conjecture is that these two measures converge fo'

**Section: What's Conjectured**

- ⚠️ `Fisher Information` — 'ramework posits that fractal dimension $D_f$ converges with Fisher Information Rank for self-similar systems — that the geometric and info'

---

## AM3  (2 flags)

**Section: DS Cross-References**

- ⚠️ `Fisher information` — ' of AM4 (Hamilton–Jacobi). Phase-space geometry connects to Fisher information (M6): Fisher metric is the symplectic metric on statistical'

**Section: Mathematical Archetype**

- ⚠️ `Fisher information` — 'tural home of statistical mechanics, quantum mechanics, and Fisher information.  Dimensional sensitivity: D-sensitive — Phase space has a '

---

## BIO10  (2 flags)

**Section: DS Cross-References**

- · `entropy` — 'stasis requires continuous energy expenditure to counteract entropy production). H3 (Phase Coherence — physiological homeostasi'

**Section: What The Math Says**

- · `fluctuation` — 'ns requires more energy. This is the biological form of the fluctuation-dissipation relationship.'

---

## C2  (2 flags)

**Section: Mathematical Archetype**

- ⚠️ `effective dimension` — "ublinear for infrastructure) depend on the social network's effective dimension — the crossover exponent encodes D_eff of the urban network"
- ⚠️ `D_eff` — "work's effective dimension — the crossover exponent encodes D_eff of the urban network."

---

## CHEM2  (2 flags)

**Section: DS Cross-References**

- · `entropy` — 'TD3 (Second Law — entropy maximisation drives the cell reaction; the Nernst equation '

**Section: Mathematical Archetype**

- · `entropy` — 'ogarithmic dependence on concentration ratio Q reflects the entropy of mixing: the cell potential decreases logarithmically as '

---

## CM8  (2 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — "es to Maxwell's equations (EM1–EM5). Ω_D: if c changes with D_eff, E and B field strengths re-couple."

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'ic, and the coupling constants ε₀, μ₀ (and thus c) run with D_eff through Ω_D.'

---

## CS10  (2 flags)

**Section: DS Cross-References**

- · `entropy` — 'ree-something theorems: the Second Law says no free energy (entropy always increases); NFL says no free performance (gains must'
- · `Entropy` — 'ormance (gains must be paid for elsewhere)). STAT1 (Maximum Entropy Principle — MaxEnt and NFL are complementary: MaxEnt specif'

---

## EM3  (2 flags)

**Section: DS Cross-References**

- · `symmetry` — 'law) is the consequence. Together with AM5 (Noether), gauge symmetry of electrodynamics → charge conservation.'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'ling E — the coupling constant (speed of light c) runs with D_eff through Ω_D acting on ε₀ and μ₀.'

---

## EM4  (2 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — ' Maxwell system. Ω_D: c = 1/√(ε₀μ₀) — if ε₀ and μ₀ run with D_eff, c runs. GV1 (General Relativity) and G1 (Dimensional Redsh'

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'rent-driven B fields — the coupling c = 1/√(ε₀μ₀) runs with D_eff, changing the speed of electromagnetic wave propagation.'

---

## FM4  (2 flags)

**Section: Mathematical Form**

- ⚠️ `η` — 'Q = πr⁴ΔP / (8ηL)  (η = dynamic viscosity, L = pipe length)'

**Section: What The Math Says**

- ⚠️ `eta` — ' fourth times delta-P divided by (8 times dynamic viscosity eta times L). The dramatic r-to-the-fourth dependence means hal'

---

## OP3  (2 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'Derived from OP1. The refractive index n is analogous to D_eff: it governs how wave propagation changes across a boundary '

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'ave vector. The refractive index n is the optical analog of D_eff: it governs how wave speed — and thus propagation — changes'

---

## OP5  (2 flags)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'ojection loss in dimensional compression). Connects to Ax2 (D_eff as observer-dependent projection).'
- · `observer` — 'loss in dimensional compression). Connects to Ax2 (D_eff as observer-dependent projection).'

---

## AM4  (1 flag)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'r equation). AM1 (least action) parent. Ω_D: if ℏ runs with D_eff, the classical–quantum boundary shifts.'

---

## B1  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'eling rate contains ℏ explicitly — Ω_D predicts ℏ runs with D_eff, shifting the tunneling probability and thus the decay cons'

---

## B2  (1 flag)

**Section: What's Conjectured**

- ⚠️ `effective dimension` — 'ff}}$ signature if metabolic networks operate at fractional effective dimension. This remains speculative and is not directly tested by any'

---

## BIO9  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — "ion. This is the biological implementation of a first-order phase transition in the membrane's electrical state — a sharp transition fro"

---

## CHEM1  (1 flag)

**Section: Constraint Category**

- · `symmetry` — 's. The periodicity is topological: it reflects the discrete symmetry of the Schrödinger equation for the hydrogen-like atom.'

---

## CHEM4  (1 flag)

**Section: DS Cross-References**

- · `entropy` — 'lch). TD3 (Second Law — equilibrium is the state of maximum entropy; Ka is determined by ΔG° = ΔH° − TΔS°).'

---

## CM3  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'tal geometry changes if the force law exponent changes with D_eff.'

---

## CS13  (1 flag)

**Section: Constraint Category**

- · `symmetry` — ' version of the spectral theorem, with positivity replacing symmetry as the key condition.'

---

## CS14  (1 flag)

**Section: Mathematical Form**

- · `symmetry` — 'ed messages (signed): n ≥ 2f + 1  (digital signatures break symmetry) Single-bit consensus: achievable with n = 3f + 1 in O(f) r'

---

## CS7  (1 flag)

**Section: DS Cross-References**

- · `entropy` — 'g global consistency in the presence of partitions requires entropy-reducing coordination that becomes thermodynamically costly'

---

## D1  (1 flag)

**Section: What's Contested**

- · `entropy` — 'sting the power law may be a consequence of sensory channel entropy rather than a primitive relationship.'

---

## DM1  (1 flag)

**Section: Constraint Category**

- · `entropy` — 'centration gradient (chemical potential gradient); produces entropy.'

---

## EM12  (1 flag)

**Section: Constraint Category**

- · `symmetry` — 'sense that the geometry of the Amperian loop must match the symmetry of the current distribution to be analytically tractable.'

---

## EM13  (1 flag)

**Section: DS Cross-References**

- · `symmetry` — ' Wiedemann–Franz Law is a further constraint beyond Onsager symmetry that emerges from Fermi-Dirac statistics). QM3 (Pauli Exclu'

---

## ES11  (1 flag)

**Section: DS Cross-References**

- · `connection` — 'rdering in H4 (χ_eff) and directed graph analysis in the DS connection network.'

---

## ES7  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'ing may reflect resonance conditions in protoplanetary disk D_eff — the exponential sequence a_n ≈ 0.4 + 0.3×2ⁿ suggests a pe'

---

## F3  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'ws from resource competition dynamics regardless of spatial D_eff.'

---

## FL11  (1 flag)

**Section: Constraint Category**

- · `entropy` — 'tinguishes nothing. This is the logical analogue of maximum entropy: zero structure, no useful distinctions remaining.'

---

## FL17  (1 flag)

**Section: Mathematical Archetype**

- · `symmetry` — 'Mathematical archetype: symmetry-conservation  Correct translation preserves logical form: t'

---

## FL19  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `phase transition` — 'reshold-transition  The empty/non-empty boundary is a sharp phase transition: above it (|D| ≥ 1), standard QL inference is valid; at it '

---

## FL8  (1 flag)

**Section: What The Math Says**

- ⚠️ `duality` — 'a tautology requires exhaustive enumeration. The structural duality between tautologies and contradictions (A is a tautology if'

---

## FM6  (1 flag)

**Section: What The Math Says**

- ⚠️ `eta` — ' on a sphere in background flow u_infinity is F equals 6 pi eta r times (u_infinity plus r-squared over 6 times the Laplaci'

---

## GL5  (1 flag)

**Section: DS Cross-References**

- ⚠️ `D_eff` — ' molar (macroscopic) and molecular (microscopic) scales — a D_eff transition in scale.'

---

## GT11  (1 flag)

**Section: DS Cross-References**

- · `Entropy` — 'g coupled from uncoupled objects). HB02 (Bekenstein-Hawking Entropy — S = A/4 saturates the Bekenstein bound at the horizon; th'

---

## GV2  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — ' Maxwell-like structure with G replacing 1/ε₀ — G runs with D_eff through Ω_D, making gravitomagnetic effects D-sensitive.'

---

## GV4  (1 flag)

**Section: What It Claims**

- · `observer` — 'f a distant galaxy is proportional to its distance from the observer (Lemaître, 1927; Hubble, 1929). The proportionality constan'

---

## KC6  (1 flag)

**Section: Constraint Category**

- · `entropy` — 'deal mixing — no interaction between components changes the entropy of mixing.'

---

## MATH8  (1 flag)

**Section: DS Cross-References**

- · `symmetry` — "' theorem provides the geometric framework connecting local symmetry (dω = 0) to global conservation (∫ω = 0)). MATH5 (FTC — the"

---

## MS1  (1 flag)

**Section: What The Math Says**

- · `connection` — "the spring constant is k equals E A over L-zero, making the connection to Hooke's law explicit: F equals k times delta-L. Poisson'"

---

## RD1  (1 flag)

**Section: Mathematical Archetype**

- ⚠️ `D_eff` — 'tefan-Boltzmann exponent becomes D+1. h and c both run with D_eff through Ω_D.'

---

## TD11  (1 flag)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 't). Connects to the idea that effective degrees of freedom (D_eff) are additive within a regime.'

---

## TD12  (1 flag)

**Section: DS Cross-References**

- ⚠️ `D_eff` — 'dimensionality): the number of active degrees of freedom is D_eff, not fixed.'

---

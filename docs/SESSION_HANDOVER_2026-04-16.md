# Session Handover — 2026-04-16 (M0 Audit Complete)

> **Read order for fresh sessions:**
> 1. `docs/RESEARCH_PLATFORM_CHARTER.md` — mission, epistemic contract, working modes
> 2. `CLAUDE.md` — project context, current state
> 3. **This document** — what happened in the M0 audit and what's next
> 4. `docs/M0_MILESTONE_COMPILATION.md` — the full audit findings (six addenda)
> 5. `docs/CCA_MATHEMATICAL_FORMALIZATION.md` header — current calibrated CCA status
> 6. Query `data/wiki_history.db.confidence_calibration` for entity-level calibration
> 7. Earlier session handovers (`SESSION_HANDOVER_2026-04-03.md`, `_04-05.md`, `_04-07.md`) for pre-reset technical history

---

## What happened this session (one-line summary per phase)

This was a single very long working session that went through several distinct phases, all on 2026-04-16:

1. **General assessment** of project state → identified product-arc (PFD) vs research-arc divergence
2. **Research platform reset** → owner chose to drop product framing, adopt personal-research-platform framing
3. **Research Platform Charter written** → epistemic contract codified
4. **CLAUDE.md rewritten + product-arc docs archived** → docs/PFD_PROJECT_FOUNDATIONAL_PLAN.md and docs/SCF_PHASE3_DESIGN.md moved to docs/archive/
5. **M0 audit launched** → six addenda over the rest of the session, each sharpening the calibration of CCA, P17/P23, Fisher-gravity chain
6. **Primary-source reading** of 5 papers (Machta 2013, Transtrum 2015, Mattingly 2018, Brown 2022, Quinn 2023, Saberi 2024) drove the iterative corrections
7. **Database calibration** of all 23 conjectures + CCA sub-conjectures + Fisher-gravity chain into `wiki_history.db.confidence_calibration` (45 records across 4 audit refs)
8. **Handover + terminology proposal** (this doc + `docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md`) — ends the session

**Total commits**: 4 (`6194ea2`, `ffed5b1`, `4b835f0`, `8abb28a`, `[this commit]`)
**Tests**: 587 passing throughout, untouched by the audit work
**Schema changes**: One new table `confidence_calibration` in `wiki_history.db`. **No changes to `ds_wiki.db`.**

---

## Current project state

### Mission framing (post-reset)

A **personal research platform** — structured lab notebook with epistemic guardrails — for Ian Darling's physics and cross-domain research. NOT a product, not a paper validator, not chasing publication. See `docs/RESEARCH_PLATFORM_CHARTER.md` for the full epistemic contract.

### Wiki scale (unchanged from pre-reset, calibration is what changed)

- **278 entries** across 22 type-prefixes (A/B/C/D/E/F/G/H/M/Q/T/X/Ax/OmD/BIO/CHEM/MATH/INFO/STAT/CS/CR/MS/FL/NE/IT/GT/HB/BR/RG/EM/FM/TD/GV/ES/OP)
- **819 links** (35 tier-1, 528 tier-1.5, 87 tier-2, 169 original null-tier)
- **23 conjectures (P1–P23)**, **12 gates (G1–G12)**
- **1,913 ChromaDB chunks** (bge-large 1024-dim)
- **1,126 property rows**
- **587 tests passing**

### Confidence calibration after M0 (from `wiki_history.db.confidence_calibration`)

The audit calibrated 30 + 5 + 6 + 4 = **45 entities** across **4 audit refs** (initial M0 + 3 addenda batches). The headline distribution from the initial M0 calibration:

- **Established**: 1 (P21 core — Fisher-Rao universality, classical case only, via Chentsov/Amari)
- **Supported**: 7 (P5 as application, P18/19/20 single-domain empirical, CCA-1b-magnitude, CCA-1c, CCA-2)
- **Speculative**: 20 (P1–P4, P6–P17, P22, P23, fisher_gravity_chain, GT10_as_CCA_instance)
- **Falsified**: 2 (CCA-1, CCA-1b L^d scaling)

Plus from later addenda:
- **+1 Established pattern observation**: "matrix observables on 2D Ising at criticality reduce to standard critical exponents" (confirmed by Vinayak 2014, Saberi 2024, Borgs-Chayes 1996)
- **+5 Speculative refinements**: P17 + P23 (Amendola/Cadoni citation corrections), CCA-1c (rationale refinements across addenda), CCA-1b-magnitude (Brown 2022 thematic adjacency), and various terminology / mechanism / reviewer flags

### Active research threads

**CCA (Constrained Critical Attractor) framework** — the most-developed thread:
- General approach (FIM eigenvalue spectrum on lattice phase transitions) is **substantially in established lineages**: Sethna sloppy models (Machta 2013), correlation-matrix RMT at criticality (Vinayak 2014), Potts covariance matrix → FK clusters (Borgs-Chayes 1996). Three independent constructions all reduce to standard critical exponents.
- CCA's specific construction (per-site fields + d_eff/η scalar observables + temperature sweep + first-order Potts discriminator) has **possibly narrow novelty** in the first-order regime, where 2-point observables (CCA) may diverge from hybrid 2-point + multi-point observables (Brown 2022 GTE).
- **CCA-1 and CCA-1b L^d scaling are FALSIFIED** (Phase C/D 2026-04-07).
- **CCA-1b magnitude and CCA-1c curve shape are qualitatively supported on a single test** (q=2 vs q=10 Potts).
- Status: **Speculative**; charter prohibits promotion above without (a) second independent test (extended q=2,5,7,10 sweep recommended) and (b) reduction-check vs standard critical exponents at T_c.

**Fisher-gravity chain** (M6→IT05→IT03→GT10→GT01):
- Downgraded from "structural coherence result" to **conceptual analogy**.
- Stacks vocabulary ("relative entropy") across three distinct mathematical objects: classical Fisher metric, classical KL divergence, quantum entanglement entropy (von Neumann on a subalgebra in Jacobson 2016).
- Jacobson 2016 is also linearized only; full nonlinear Einstein not derived; modular-Hamiltonian assumption holds in CFT/holographic contexts but generality not proven.
- No prior art found bridging sloppy models / classical FIM to emergent gravity.
- Status: **Speculative** (downgraded from earlier "supported structural finding").

**P17 cosmological coupling** (and P23 horizon formation):
- Citations VERIFIED via Fifth Addendum deep-research pass:
  - **Amendola, Rodrigues, Kumar, Quartin 2024** (MNRAS 528, 2377; arXiv:2307.02474) — real paper
  - **Cadoni et al. 2023** (JCAP 11, 007; arXiv:2306.11588) — real paper, 7 authors
- BUT wiki wording was inflated:
  - **Amendola "5σ" was a forecast, not current data**. Current GWTC-3 gives 2σ upper limit k<2.1, ~3σ tension with k=3.
  - **Cadoni 2023 is "universal" not "generic"**, applies to regular BHs (not all nonsingular compact objects). Crucially, their own KS analysis on Farrah elliptical-galaxy sample prefers k=3 over k=1 — they interpret as evidence BHs may be non-GR, NOT as confirming their k=1 prediction.
- Status: **Speculative, high-risk**. Wording corrections needed in `ds_wiki.db` (calibration table is the override until then).

---

## The six M0 addenda — one paragraph each

**Initial M0 (main body)**: 30-entity calibration from harsh first-pass agent audit. Result: 1 Established / 7 Supported / 20 Speculative / 2 Falsified. Headline: DFIG = re-parameterization of Sethna sloppy models; CCA framework = restatement of Janke-Johnston-Kenna 2004 + Prokopenko-Lizier 2011 (this claim later corrected); Fisher-gravity chain = vocabulary stacking; P17 = high-risk speculation with unverified citations.

**First Addendum**: Follow-up audit corrected the "JJK + Prokopenko-Lizier as CCA prior art" claim. Those papers use 2×2 thermodynamic Fisher metric with scalar curvature, NOT high-dim per-site-field FIM with eigenvalue spectrum. Identified Machta-Chachra-Transtrum-Sethna 2013 Science as the actual prior art for general setting.

**Second Addendum**: After owner provided Machta 2013 PDF and brief search agent work. Confirmed Machta 2013 uses global Hamiltonian couplings (not per-site fields), at T_c (not T-sweep), no Potts, no transition-order discrimination. CCA's specific construction not preempted. Three remaining open vectors flagged for follow-up.

**Third Addendum**: Closed the inverse-Ising / maxent gap with focused search. Tkačik 2015 PNAS (heat capacity via thermodynamic integration in retinal maxent model) is closest adjacency in neural-criticality lineage but uses heat capacity, not FIM spectrum. arXiv:2507.02574 (2025) verified via direct WebFetch as inference-method comparison paper, not FIM spectroscopy. **Final state: NO confirmed prior art for CCA's specific construction with moderate confidence.**

**Fourth Addendum**: Owner provided four primary-source PDFs (Machta 2013 — already covered, Transtrum 2015 perspective, Mattingly 2018 PNAS bonus, Brown-Bossomaier-Barnett 2022, Quinn 2023). Five papers read in full. **Two findings**: (a) **Mattingly 2018 introduces "d_eff" terminology with a different formula** — TERMINOLOGY COLLISION, mandatory citation; (b) **Brown 2022 is prior art for the broader research program** of information-theoretic discrimination of first-order Potts transitions, with a simple physical mechanism (cluster interfacial length) CCA lacks.

**Fifth Addendum (deep-research pass)**: Three parallel agent passes + direct primary-source verification of remaining citations. **Three major findings**: (a) **Amendola 2024 verified but "5σ" was a forecast not current data**; (b) **Cadoni 2023 verified with corrections** ("universal" not "generic"; their own analysis prefers Farrah's k=3 on elliptical sample); (c) **MAJOR — the FIM in CCA IS the connected correlation matrix χ_ij** (textbook stat mech), with broader prior art at three levels: Vinayak 2014 EPL (correlation matrix → η_critical power-law), Borgs-Chayes 1996 (Potts covariance → FK clusters), Saberi 2024 PRB (claimed at the time as direct prior art). **Two terminology collisions** flagged: CCA d_eff vs Mattingly d_eff; CCA η vs standard stat-mech η_critical.

**Sixth Addendum**: Owner provided Saberi 2024 + Brown 2022 PDFs. **Critical correction**: Saberi 2024 uses **a different matrix object** — the spin configuration arranged as L×L matrix and symmetrized, NOT the connected correlation matrix. CCA's narrow novelty surface is **slightly broader than Fifth Addendum claimed**. Brown 2022 mechanism analysis refined: GTE is a **hybrid 2-point + multi-point** observable, not purely multi-point. Sharpened mechanism question: at first-order Potts, can pure 2-point observable (CCA) reproduce hybrid 2-point + multi-point discrimination (Brown's GTE)? **Saberi (Univ. Tehran / Max Planck Dresden) identified as obvious external reviewer** — works on both cluster geometry and matrix-spectrum-of-Ising. Pattern "matrix observables on 2D Ising at criticality reduce to standard critical exponents" upgraded to **Established** (3 independent constructions confirm).

---

## What's actually open (in priority order)

### Owner-action items (cannot be done by Claude without new inputs)

1. **Run the analytical-comparison-at-T_c check.** For Potts q=2 at T_c, derive CCA's d_eff and η_CCA analytically from η_critical=1/4 and β/ν=1/8 via finite-size scaling. Compare to existing Phase B/C numerics in `data/reports/ising_fim_test/`. If agree: continuous-transition CCA reduces to standard critical exponents (no novel content there). If disagree: something else is being captured. **Hours-to-days of computational work.**

2. **Run extended q=2,5,7,10 Potts sweep with both observables.** This directly tests the Sixth Addendum's sharpened mechanism question: does pure 2-point (CCA d_eff/η) reproduce hybrid 2-point + multi-point (Brown's GTE)? Compute both observables on the same data. Two outcomes (both honest): (a) CCA tracks Brown → defensible narrow novelty; (b) CCA captures partial signal only → CCA reduces to less-informative version of Brown. **Weeks of computational work.**

3. **Read Vinayak 2014 EPL** (arXiv:1403.7218) and **Borgs-Chayes 1996 J. Stat. Phys.** (arXiv:adap-org/9411001). The two unread primary sources in the new prior-art map. The Vinayak paper is short and is the analytical framework for "correlation matrix spectrum at criticality reduces to η." Borgs-Chayes is the rigorous Potts-covariance-vs-FK-cluster bridge.

4. **Address the two terminology collisions.** See `docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md` (this session) for specific replacement proposals. Mandatory before any external writeup.

5. **Update P17/P23 wording in `ds_wiki.db`.** The verified Amendola/Cadoni corrections need to land in the actual claim text. Calibration table is the override until then. Requires explicit owner sign-off because it touches the source-of-truth DB.

6. **Optional but high-leverage: contact Saberi directly** (ab.saberi@ut.ac.ir or saberi@pks.mpg.de) to ask about per-site-field FIM eigenvalue spectroscopy on thermal phase transitions — would resolve CCA novelty question definitively.

### Long-tail uncommitted-files cleanup (deferred from prior sessions)

The repo has ~30 untracked files from earlier sessions (alpha_entropy_v22.py, .DS_Store, prior pillar migrations, chroma_db rebuild artifacts, scripts/migrations/correct_conjectures_P5_P18_P19.py, etc.). They are **explicitly out of scope** for the M0 audit and were not touched. A future cleanup session should decide what to commit, gitignore, or delete.

### Things that are intentionally NOT next steps

- **No new conjectures.** Wiki has 23 already; M0 found most are speculative. Adding more is drift.
- **No new experimental phases on CCA without doing (1) and (2) above first.** Charter prohibits.
- **No re-engagement with PFD product framing.** Retired by 2026-04-16 reset.
- **No external writeup of CCA without addressing terminology collisions and reading Vinayak + Borgs-Chayes.**
- **No further audit iterations** without new inputs (experimental data or additional primary sources). The audit has reached its useful depth.

---

## Key files for fresh sessions

### Always read first

| File | What it does |
|------|---|
| `docs/RESEARCH_PLATFORM_CHARTER.md` | Mission, epistemic contract, working modes |
| `CLAUDE.md` | Auto-loaded project context |
| `docs/M0_MILESTONE_COMPILATION.md` | Full audit findings, six addenda |
| `docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md` | Pending terminology fixes |
| **This document** | Session-specific handover |

### CCA-relevant primary sources (in `Research_Papers/`)

| Paper | Status | What it does |
|---|---|---|
| Machta-Chachra-Transtrum-Sethna 2013 Science (`EmergentTheories(2013).pdf`) | Read 2026-04-16 | Foundational sloppy models on Ising at criticality |
| Transtrum 2015 J. Chem. Phys. perspective | Read 2026-04-16 | Sethna-group framing document |
| Mattingly 2018 PNAS | Read 2026-04-16 | Bonus — d_eff terminology precedent (different formula) |
| Brown-Bossomaier-Barnett 2022 Sci. Rep. | Read 2026-04-16 | Closest broader-program prior art (transfer entropy on Potts q=2,5,7,10) |
| Quinn 2023 Rep. Prog. Phys. | Read 2026-04-16 (pages 1-40) | Modern synthesis |
| Saberi-Saber-Moessner 2024 PRB | Read 2026-04-16 | NOT direct prior art for CCA (different matrix object) |

### CCA-relevant primary sources still to read (owner action)

| Paper | arXiv | What it would resolve |
|---|---|---|
| Vinayak-Prosen-Buča-Seligman 2014 EPL 108, 20006 | arXiv:1403.7218 | Analytical framework for correlation-matrix spectrum at criticality reducing to η |
| Borgs-Chayes 1996 J. Stat. Phys. 82, 1235 | arXiv:adap-org/9411001 | Rigorous Potts-covariance-matrix-vs-FK-cluster bridge |

### Database / experiment outputs to refer to

| Path | Contents |
|---|---|
| `data/wiki_history.db` (table: `confidence_calibration`) | All 45 M0 calibration records across 4 audit refs |
| `data/ds_wiki.db` | The knowledge graph (READ ONLY, do NOT schema-alter) |
| `data/chroma_db/` | ChromaDB semantic index (bge-large 1024-dim, 1913 chunks) |
| `data/reports/ising_fim_test/` | Phase A/B/C/D experiment outputs from 2026-04-07 session |
| `scripts/migrations/m0_calibration_2026_04_08.py` | Initial M0 calibration migration |
| `scripts/migrations/m0_primary_source_verified_2026_04_08.py` | Fourth Addendum corrections |
| `scripts/migrations/m0_deep_research_2026_04_08.py` | Fifth Addendum (deep research) |
| `scripts/migrations/m0_sixth_addendum_2026_04_08.py` | Sixth Addendum (Saberi correction + Brown refinement) |

### Useful query: get current calibration of any entity

```python
import sqlite3
conn = sqlite3.connect('data/wiki_history.db')
# All audit records for a given entity (in order):
for row in conn.execute('''
    SELECT calibration_date, audit_ref, confidence, short_status, rationale
    FROM confidence_calibration
    WHERE entity_id = ?
    ORDER BY id
''', ('CCA-1c',)):
    print(f'[{row[1]}] {row[2]}: {row[3]}')
    print(f'  {row[4][:200]}\n')
```

The latest record for any entity is the current calibration. Earlier records show how it evolved.

---

## Honest meta-observations from this session

Three patterns worth knowing for future sessions:

**1. Single-pass audit results are unreliable.** The CCA novelty status moved through five distinct calibrations across the M0 process. Each correction came from primary-source reading or owner pushback, not from agent searches alone. The first audit was confidently wrong about prior art (JJK 2004); the Fifth Addendum was wrong about Saberi 2024; both required correction. **Treat any LLM-assisted novelty verdict as provisional until verified against primary sources.**

**2. The FIM = connected correlation matrix realization should have come immediately.** The CCA framework was built around per-site-field FIM analysis for many sessions. Recognizing that this matrix IS the textbook connected correlation matrix χ_ij = ⟨s_i s_j⟩_c took until the Fifth Addendum's deep-research pass. Once the identification was made, the prior-art landscape changed substantially. **For any future construction, ask immediately: "what textbook stat-mech object is this?" before claiming novelty.**

**3. Saberi keeps appearing.** Cited by Brown 2022 (cluster geometry expert via Saberi 2009 J. Stat. Mech.) and lead author of Saberi 2024 PRB (matrix spectrum on Ising). He spans both literatures relevant to CCA. If the project ever tries to write CCA up externally, **reaching out to Saberi directly is the highest-value single action**.

---

## Session totals (for the curious)

- **Conversation length**: ~200k tokens at session end
- **Commits in M0 audit**: 4 substantive commits (`6194ea2` reset+initial M0, `ffed5b1` primary-source verifications, `4b835f0` deep research, `8abb28a` Sixth Addendum)
- **Calibration records added**: 45 (initial 30 + addenda 5 + 6 + 4)
- **Documents written**: M0_MILESTONE_COMPILATION.md (six addenda, ~750 lines), RESEARCH_PLATFORM_CHARTER.md, CCA_TERMINOLOGY_RENAME_PROPOSAL.md, this handover
- **Documents archived**: PFD_PROJECT_FOUNDATIONAL_PLAN.md, SCF_PHASE3_DESIGN.md
- **Documents marked legacy**: MASTER_SUMMARY.md, USER_GUIDE.md
- **Tests broken**: zero
- **`ds_wiki.db` schema changes**: zero (charter rule preserved)
- **CCA novelty calibrations the audit went through**: 5 distinct states across 6 addenda

The audit work is preserved end-to-end across the M0 doc, the calibration table, and the migration scripts. A fresh Claude session reading the recommended doc order will reach the same calibrated belief state without needing to re-derive any of it.

# Domain Retag — Chunk 7 (23 P-series Conjectures) — Full Proposals

**Date:** 2026-04-18
**Scope:** 23 conjectures P1–P23 from `ds_wiki.db.conjectures` table
**Context:** Conjectures have no `domain` column — proposed tags derived from claim text + M0 calibration context.

---

## All 23 conjectures — proposed tagging

Column key: **FV** = fold verdict from earlier audit (FOLD / FALSIFY / RECLASSIFY / ARCHIVE / KEEP)

| # | Title | Primary | Secondary | Auxiliary | FV |
|---|---|---|---|---|---|
| `P1` | Cosmological Redshift as Dimensional Gradient | `physics.cosmology` | `information_theory` | — | FOLD |
| `P2` | Metabolic Exponent Tracks Vascular D_eff | `biology.physiology` | `networks_systems`, `information_theory` | — | FOLD (WBE 1997) |
| `P3` | Single Ω_D Governs G, h, m | `physics.cosmology` | `information_theory` | `physics.modern` | FOLD (RG running) |
| `P4` | CcO 1.5 ms as Thermodynamic Refresh Rate | `chemistry.biochemistry` | `biology.physiology` | `physics.classical` | FOLD (std enzyme kinetics) |
| `P5` | Fisher Information Rank Equals D_eff | `information_theory` | `mathematics.probability_measure`, `statistics_probability` | — | FOLD (sloppy models) |
| `P6` | Fractal Dim Converges with Fisher Rank | `mathematics.geometry_topology` | `information_theory` | — | FALSIFY |
| `P7` | D_eff Decreases Monotonically Under CG | `information_theory` | `mathematics.probability_measure` | `physics.modern.statistical_mechanics` | FALSIFY |
| `P8` | Continuous Critical Exponent on Fractional-D | `physics.modern.statistical_mechanics` | `mathematics.geometry_topology` | `information_theory` | FOLD (Gefen/JJK) |
| `P9` | Holographic Dictionary LWE Complexity | `physics.cosmology` | `computer_science.complexity` | `information_theory` | RECLASSIFY→Q |
| `P10` | Hadron Charge Radii / Running ℏ | `physics.modern` | `information_theory` | — | FOLD (std QCD) |
| `P11` | Urban Scaling Tracks Spectral Dimension | `networks_systems` | `computer_science`, `biology.physiology` | — | FOLD (Bettencourt-West) |
| `P12` | β(λ) Cross-Domain Formula | `networks_systems` | `biology.physiology`, `information_theory` | — | ARCHIVE |
| `P13` | λ_min = (d_f−1)/(d_f+1) Capacity Bound | `information_theory` | `biology.physiology`, `mathematics.geometry_topology` | — | FALSIFY (ansatz) |
| `P14` | Branching Variance Predicts β Gap | `biology.physiology` | `networks_systems`, `statistics_probability` | — | ARCHIVE |
| `P15` | Metabolic Cost ∝ (1−λ)²·d_f | `biology.physiology` | `information_theory`, `mathematics.geometry_topology` | — | FALSIFY (ansatz) |
| `P16` | RLCT = d_f at Regime Transitions | `computer_science.ml` | `biology.physiology`, `mathematics.geometry_topology` | — | ARCHIVE (blocked by Q4) |
| `P17` | Cosmological Coupling k = D_eff | `physics.cosmology` | `information_theory` | — | ARCHIVE (contested) |
| `P18` | Structural Coherence Floor in Markets | `statistics_probability` | `information_theory`, `networks_systems` | — | KEEP (single-domain) |
| `P19` | Non-Ergodicity of Tier-3 Regime Signals | `statistics_probability.stochastic_processes` | `information_theory` | — | KEEP (single-domain) |
| `P20` | Subadditive Error Propagation in Signal Stacks | `statistics_probability.inference` | `information_theory` | — | KEEP (empirical fit) |
| `P21` | Fisher-Rao Metric Universality | `mathematics.probability_measure` | `information_theory`, `mathematics.geometry_topology` | — | FOLD (Chentsov/Amari — Established) |
| `P22` | Irreversible Lockout Trichotomy for SSB | `physics.modern.statistical_mechanics` | `information_theory` | — | RECLASSIFY→Q |
| `P23` | Horizon Formation as Bekenstein-Saturation Transition | `physics.cosmology` | `information_theory`, `physics.modern.statistical_mechanics` | — | ARCHIVE (contested) |

### Primary-tag distribution for conjectures

| Top-level | Count |
|---|---|
| physics.cosmology | 5 (P1, P3, P9, P17, P23) |
| biology.physiology | 3 (P2, P14, P15) |
| physics.modern.statistical_mechanics | 2 (P8, P22) |
| physics.modern | 1 (P10) |
| chemistry.biochemistry | 1 (P4) |
| information_theory | 2 (P5, P7, P13) |
| mathematics.geometry_topology | 1 (P6) |
| mathematics.probability_measure | 1 (P21) |
| networks_systems | 2 (P11, P12) |
| computer_science.ml | 1 (P16) |
| statistics_probability (+ sub-tags) | 3 (P18, P19, P20) |

---

## ⚠️ Critical flag: P18 / P19 / P20 are AlphaEntropy-adjacent

You just flagged **X8** as "side finance project, not science wiki content." Looking at P18/P19/P20:

- **P18** "US equity markets never reached FRAGMENTED regime 2003-2025" — single dataset, **AlphaEntropy domain**
- **P19** "D_eff non-stationarity in Tier 3 domains" — **US equities only, AlphaEntropy-derived**
- **P20** "subadditive error propagation from 19 A/B variants" — explicitly **AlphaEntropy A/B testing work**

These three conjectures were audited as "Supported — single-domain empirical" but the domain IS your AlphaEntropy side project. By the same logic you applied to X8, they may also belong outside the science wiki (or inside with a clear "AlphaEntropy-derived" label).

**Three options:**
- **(a) Treat same as X8** — exclude from `entry_source_domains`, add to `internal_constructions` as side-project content
- **(b) Keep tagged but flag internal_construction with "AlphaEntropy-derived, single-domain observation, treat as side-project-adjacent"** so they're surfaced as first-class potentially-non-wiki content
- **(c) Keep tagged as science-wiki content** — rationale: they're at least candidate *scientific* claims about regulation/non-ergodicity/signal stacking, even if the only dataset is your trading work

My recommendation: **(b)** — tag them so they don't disappear from the graph, but flag `internal_construction` so you get the honest label. Can always change later.

---

## Other flags

1. **P9 and P22 are marked RECLASSIFY → Q-series** in the audit. But they're still in the `conjectures` table with P-prefix IDs. Tagging here doesn't move them; that's a separate data-surgery question. For now, they're tagged as conjectures where they live.

2. **P13 and P15 are owner-acknowledged ansatz** (FALSIFY bucket). They get domain tags, but should ALSO be flagged as `internal_construction` with scrutiny level `needs-review`. This is the "preserve falsifications as learning" rule from your feedback memory.

3. **P6 and P7 falsified by own testing** — tag normally; their falsification status lives in `wiki_history.db.confidence_calibration` already (from M0).

4. **P16 "RLCT = d_f"** — I tagged primary=`computer_science.ml` because RLCT is singular learning theory (Watanabe). But RLCT usage in biology metabolism is unusual; owner may disagree and want primary=biology.physiology. Flag for pushback.

5. **P3 primary=`physics.cosmology`** — the Ω_D operator is used in P3 to tie G, h, m running. Could argue `physics` (top-level) since it touches all of classical/modern/cosmology. Picked cosmology because the master Ω_D framing is cosmological. Pushback welcome.

6. **P5 sub-tag secondary** — I put `mathematics.probability_measure` and `statistics_probability` as secondaries. You could argue for a single more-specific secondary; kept both because Fisher info sits at the intersection.

---

## What this migration will do

- Insert 23 conjecture-level domain tags into `entry_source_domains`
- Conjectures use P-series IDs as `entry_id` (same FK pattern as regular entries)
- All rows: `review_status='current'`, `confidence='high'`, `assigned_date=2026-04-18`

## After P18/19/20 decision

If you pick option (a) or (b), I'll add the `internal_constructions` flag pattern from X8 for those three (plus P13/P15 ansatz ones per flag #2 above).

## Your action

1. **Decide on P18/P19/P20** — options (a) / (b) / (c)
2. **Push back on any other tagging** (P16, P3, P5 are the closest calls)
3. Say "apply" and I build the migration script

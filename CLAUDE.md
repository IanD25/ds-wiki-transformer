# DS Wiki Research Platform — Claude Code Context

> **This file is auto-loaded by Claude Code on every session start.**
> **Read the charter first: `docs/RESEARCH_PLATFORM_CHARTER.md`** — it defines mission, epistemic rules, and working modes.
> Session history: `MASTER_SUMMARY.md` (legacy technical narrative, partially superseded) and latest `docs/SESSION_HANDOVER_*.md`.

---

## What This Project Is (2026-04-08 Reset)

A **personal research platform** — a structured, grounded lab notebook for Ian Darling's physics and cross-domain research. It is a guardrail against speculation, a cross-domain mapper, a hypothesis generator, and a continuous research journal.

It is **not** a product, not a paper validator, not seeking publication. See `docs/RESEARCH_PLATFORM_CHARTER.md` for the full mission statement and epistemic contract.

**Prior framing (archived):** The project was previously scoped as "Principia Formal Diagnostics (PFD)" — a paper validation tool. That framing is no longer active. The product-arc documents (`PFD_PROJECT_FOUNDATIONAL_PLAN.md`, `SCF_PHASE3_DESIGN.md`, Phase 3/4/5 plans) are historical reference only.

- GitHub: `https://github.com/IanD25/ds-wiki-transformer`
- Python: 3.13, Apple M4 dev machine | also: Windows ShadowPC with RTX 2000 GPU
- Owner: Ian Darling (no academic affiliation, not chasing publication)

---

## The Epistemic Contract (Critical — Read Charter For Full Version)

Claude's standing instructions when working on this platform:

1. **Novelty skepticism is the default.** When something looks new, literature-search for prior art before treating it as a discovery. Report searches before celebrating.
2. **Triviality check.** Before promoting a finding, ask: *"Is this a 5-minute derivation from a known result?"* If yes, it's a re-derivation, not a discovery.
3. **Framing check.** Ask: *"Is there a standard framing where this becomes obvious or vacuous?"*
4. **Falsification first.** When the owner proposes a conjecture, try to break it before trying to support it.
5. **Plain-language statement.** Every conjecture must be statable in one sentence a physicist without wiki context could understand.
6. **Tripwire phrases.** Stop and audit if the session produces: "unification," "breakthrough," "paradigm," "fundamental insight," "solves [big problem]," "novel [X]" without a completed literature search.
7. **Confidence calibration.** Every claim tagged **Established** / **Supported** / **Speculative**. No silent promotion.
8. **AI-rabbit-hole tripwire.** Claude's job is to push back, not cheerlead. Stacking conjectures without testing them is drift. Feature-fitting to post-hoc definitions is drift. Flag it.

**The worst failure mode:** accumulating speculative claims that feel grounded because they're inside a well-organized wiki. The wiki's structure is not evidence for the wiki's content.

---

## Current Status (2026-04-08, Post-M0 Audit)

**Mission state:** Reset complete. **M0 audit complete.** The current honest snapshot of belief is `docs/M0_MILESTONE_COMPILATION.md` — read it before doing any new conjecture work. M0 downgrades a substantial fraction of previously-"supported" claims to Speculative based on a skeptical literature audit. Headline findings:

- **DFIG is a re-parameterization of the sloppy-models program** (Sethna group, 2006–present). Not novel. P5 is Supported as application, not Established as discovery.
- **CCA's general setting is Machta-Chachra-Transtrum-Sethna Science 2013** (arXiv:1303.6738) — confirmed via primary-source reading. FIM eigenvalue spectrum on 2D Ising at criticality with stiff/sloppy hierarchy. Uses global couplings, not per-site fields. Does not sweep temperature. No Potts, no first-order discrimination. **Primary-source reading of 4 additional papers completed** (Transtrum 2015 JCP perspective, Mattingly 2018 PNAS, Brown-Bossomaier-Barnett 2022 Sci. Rep., Quinn 2023 Rep. Prog. Phys.): **no paper covers CCA's specific construction** (per-site fields + d_eff/η + T-sweep + first-order-vs-continuous discriminator). However, **two important findings from primary-source reading**: (1) **Mattingly 2018 is a mandatory citation** — it uses the term `d_eff` with a DIFFERENT formula (d_eff = Σ_r r·Ω_r from optimal discrete prior weight on manifold boundaries vs CCA's d_eff = (Σλ)²/Σλ² participation ratio) — CCA must cite Mattingly and distinguish the two formulas. (2) **Brown-Bossomaier-Barnett 2022 is the prior art for the broader research program** — they study Potts q=2,5,7,10 via Global Transfer Entropy and find curve-shape differences qualitatively similar to CCA-1c, with a simple physical mechanism (cluster interfacial length). CCA currently lacks a comparable mechanism. **Highest-leverage open question:** can CCA's d_eff/η be explained via cluster interfacial geometry, or does it measure something structurally different from transfer entropy? See `docs/M0_MILESTONE_COMPILATION.md` Fourth Addendum for full findings. CCA-1 and CCA-1b L^d scaling are FALSIFIED; CCA-1b magnitude and CCA-1c shape are qualitatively supported on a single test only; charter rule prohibits promoting above Speculative without a second independent test (recommended: extend to q=2,5,7,10 to enable direct comparison with Brown et al.).
- **Fisher-gravity chain is downgraded from "structural coherence result" to conceptual analogy.** It stacks vocabulary ("relative entropy") across three distinct mathematical objects; Jacobson 2016 uses quantum entanglement entropy, not classical Fisher.
- **P17 is Speculative, high risk.** Citations VERIFIED via deep-research pass (Fifth Addendum): Amendola, Rodrigues, Kumar, Quartin 2024 MNRAS 528, 2377 (arXiv:2307.02474) is real — but wiki's "5σ" claim was the paper's FORECAST, not current data; current GWTC-3 gives 2σ upper limit k<2.1 with ~3σ tension. Cadoni et al. 2023 JCAP 11, 007 (arXiv:2306.11588) verified — 7-author paper, "universal" not "generic" k=1 for regular BHs, and crucially their own KS analysis prefers k=3 over k=1. Wiki wording for P17/P23 must be corrected.
- **CCA prior-art surface broadened by Fifth Addendum deep-research pass.** The FIM in CCA IS the connected correlation matrix χ_ij — textbook stat mech. New prior art: **Vinayak-Prosen-Buča-Seligman 2014 EPL 108, 20006** (arXiv:1403.7218) proves correlation-matrix eigenvalue density at 2D Ising criticality is power-law from η_critical; **Borgs-Chayes 1996 J. Stat. Phys. 82, 1235** (arXiv:adap-org/9411001) rigorously connects Potts covariance matrix to FK clusters; **Saberi-Saber-Moessner 2024 PRB 110, L180102** (arXiv:2503.03472) interaction-correlated RMT on 2D Ising with top eigenvalue order parameter — **highest-priority single paper**. CCA-1c remains Speculative; the candidate novel territory shrinks to first-order regime where scale invariance fails. Mechanism question (Brown 2022): at continuous transitions CCA observables likely reduce to standard η_critical; at first-order they decouple from cluster interfacial length. **Two terminology collisions** flagged: CCA d_eff vs Mattingly 2018 d_eff (different formulas), CCA η vs standard stat-mech η_critical (anomalous dimension). Both must be renamed.

Before any new experimental or conjecture work: read Transtrum-Machta-Sethna 2015, Quinn et al. 2022, Janke-Johnston-Kenna 2004, Prokopenko-Lizier 2011 (prior-art reading list in M0).

**Wiki scale (pre-audit, may shift after M0):**
- **278 entries** (213 reference_law, 18 method, 15 law, 9 instantiation, 8 open_question, 5 constraint, 3 axiom, 3 parameter, 3 theorem, 1 mechanism)
- **819 links** (35 tier-1, 528 tier-1.5, 87 tier-2, 169 original null-tier)
- **1,913 ChromaDB chunks**, **1,126 property rows**
- **23 conjectures (P1–P23)**, **12 gates (G1–G12)**
- **587 tests passing**
- Entry ID prefixes: A/B/C/D/E/F/G/H/M/Q/T/X/Ax/OmD + BIO/CHEM/MATH/INFO/STAT/CS/CR/MS/FL/NE/IT/GT/HB/BR/RG/EM/FM/TD/GV/ES/OP

**Research threads currently live:**
- **CCA (Constrained Critical Attractor) framework** — wounded from 2026-04-07 falsification cascade. CCA-1 falsified, CCA-1b scaling falsified, CCA-1b magnitude and CCA-1c curve-shape qualitatively confirmed. **Needs literature audit before continuing.** Likely overlap with sloppy-models (Sethna) and Amari information geometry.
- **Fisher-gravity chain** (M6→IT05→IT03→GT10→GT01) — structural observation derived in-wiki. **Needs audit:** is this a genuine structural insight or stacked analogies? Depends on Jacobson 2016 generality claim which is itself contested.
- **P17 cosmological coupling** — updated with 2024-2025 tensions (GW 5σ rejection of k=3, Gaia BH, Cadoni k=1, JWST AGN). Contested, honestly documented.

**Pending M0 audit actions** (see charter § "Immediate Next Steps"):
1. Conjecture audit P1–P23 against confidence calibration
2. CCA literature check (sloppy models, Amari, Sethna)
3. Fisher-gravity chain audit
4. Archive product-arc documents
5. Write M0 milestone compilation

---

## Working Modes

Be explicit about which mode you're in at the start of any work session:

- **Mode A — Curation / Grounding.** Adding established science, cleaning links, running diagnostics on the wiki itself, literature searches to ground entries. Success = wiki better reflects cited science.
- **Mode B — Exploratory Research.** Testing owner's conjectures, running experiments, falsification attempts. Success = conjectures move through lifecycle with honest documentation.

Mode B depends on Mode A. Don't run experiments on ungrounded foundations.

---

## Quick Start (Fresh Machine)

```bash
# 1. Clone
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd ds-wiki-transformer

# 2. One-command environment setup
bash setup.sh

# 3. Verify
source .venv/bin/activate
python3 -m pytest tests/ -v --tb=short   # 587 tests should pass

# 4. Optional: start MCP server (for Claude tool access)
python3 src/mcp_server.py
```

**All data committed to repo (no download or rebuild needed):**
- `data/ds_wiki.db` — the knowledge graph (READ ONLY)
- `data/rrp/` — external dataset bundles (zoo_classes, ecoli_core, periodic_table, opera, ccbh, ieee_power_grid)
- `data/chroma_db/` — ChromaDB semantic index (bge-large 1024-dim)
- `data/wiki_history.db` — embedding history snapshots
- `data/reports/` — diagnostic reports + experiment outputs

**Rebuild only if ds_wiki.db changes:** `python3 -m src.sync`

---

## Architecture (Unchanged — Tools Are Solid)

```
ds_wiki.db (SQLite, READ-ONLY)           RRP bundles (rrp_*.db, per-dataset)
        │                                        │
        ▼                                        ▼
   chroma_db/ (semantic index)         Pass 1: Parse → entries/links
        │                              Pass 1.5: EntityCatalogPass
        │                              Pass 2: CrossUniverseQuery
        │◄───────── bridges ──────────────────────│
        ▼
   MCP Server (mcp_server.py) — exposes tools to Claude
```

**Tools available:**
- **Fisher Suite** — `scripts/run_fisher_suite.py` with 6 modes (node, ds_wiki, internal_rrp, bridge, report, bridges). Structural analysis via FIM eigenvalue decomposition.
- **RRP ingestion** — parsers for 6 dataset types (zoo_classes_json, cobra_json, flat_json, ro_crate, frictionless, codemeta/citation_cff)
- **Cross-universe bridge detection** — semantic similarity matching between RRP and wiki
- **Gap analyzer** — finds isolated entries, sparse properties, link-type imbalances
- **Hypothesis generator** — surprising-pair detection via cosine similarity + type baselines
- **Visualizations** — tier-1 (D3.js network, regime charts) and tier-2 (bridge histogram, bipartite network, domain heatmap)

---

## Key Files

| File | Purpose |
|------|---------|
| `docs/RESEARCH_PLATFORM_CHARTER.md` | **ANCHOR DOCUMENT** — mission, epistemic contract, lifecycle |
| `docs/M0_MILESTONE_COMPILATION.md` | **CURRENT BELIEF SNAPSHOT (2026-04-08)** — post-audit conjecture calibration, headline downgrades, action items |
| `src/config.py` | Paths, model, thresholds |
| `src/sync.py` | Rebuild chroma_db + wiki_history.db from ds_wiki.db |
| `src/mcp_server.py` | FastMCP server exposing tools to Claude |
| `src/embedder.py` | BGE embedding, ChromaDB operations |
| `src/analysis/fisher_diagnostics.py` | FIM math, `analyze_node`, `sweep_graph`, `build_bridge_graph` |
| `src/analysis/fisher_bridge_filter.py` | Per-bridge quality scoring |
| `src/analysis/fisher_report.py` | Two-tier diagnostic report (wiki health tool) |
| `src/analysis/gap_analyzer.py` | Gap detection on the wiki |
| `src/analysis/hypothesis_generator.py` | Surprising-pair detection |
| `src/analysis/coverage_analyzer.py` | Coverage metrics |
| `src/ingestion/rrp_bundle.py` | RRP SQLite schema |
| `src/ingestion/cross_universe_query.py` | Pass 2: RRP → wiki bridge detection |
| `src/ingestion/passes/entity_catalog_pass.py` | Pass 1.5: pattern extraction |
| `scripts/run_fisher_suite.py` | Fisher CLI (6 modes) |
| `scripts/run_entity_catalog_pass.py` | Pass 1.5 + 2b CLI |
| `data/ds_wiki.db` | The knowledge graph (READ ONLY — never schema-alter) |
| `MASTER_SUMMARY.md` | Legacy technical narrative (partially superseded by charter) |
| `docs/SESSION_HANDOVER_2026-04-07.md` | Most recent session handover (CCA falsification cascade) |
| `docs/CCA_MATHEMATICAL_FORMALIZATION.md` | CCA framework — pending literature audit |
| `docs/CCA_GRAVITY_FINDINGS.md` | Fisher-gravity chain — pending audit |
| `docs/archive/` | Product-arc docs (PFD foundational plan, Phase 3 designs) — historical only |

**Deprecated / deprioritized (still exist, no longer primary):**
- `src/analysis/result_validator.py` — paper claim validator. Useful as a quick-check utility. Not a featured capability.
- `src/analysis/link_classifier.py` — LLM link-type classifier. Wiki curation only.
- `src/analysis/structural_alignment.py` — SCF structural alignment. Not being built on.
- `src/analysis/semantic_position_test.py` — parked prototype.

---

## Current Embedding Model

```python
# src/config.py — auto-detected at import time
# CUDA (ShadowPC RTX 2000): "BAAI/bge-large-en-v1.5"  # 1024-dim
# MPS  (Mac Apple Silicon): "BAAI/bge-large-en-v1.5"  # 1024-dim
# CPU  (fallback):          "BAAI/bge-base-en-v1.5"   # 768-dim
DEVICE, EMBED_MODEL, EMBED_DIM = _detect_device()
```

**Windows note:** DS Wiki entry data contains Unicode math symbols. Always prefix Python commands with `PYTHONUTF8=1` on ShadowPC:
```powershell
PYTHONUTF8=1 .venv\Scripts\python.exe scripts\run_entity_catalog_pass.py ...
```

---

## Key Commands

```bash
# Rebuild semantic index after any ds_wiki.db change
python3 -m src.sync

# Run all tests
python3 -m pytest tests/ -v   # 587 tests

# Wiki self-analysis (check wiki health)
python3 scripts/run_fisher_suite.py --mode ds_wiki --wiki-db data/ds_wiki.db

# Single-node structural analysis
python3 scripts/run_fisher_suite.py --mode node \
    --wiki-db data/ds_wiki.db --node-id CHEM5

# Internal RRP diagnostics (for imported datasets)
python3 scripts/run_fisher_suite.py --mode internal_rrp \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db

# Cross-domain bridge detection (RRP vs wiki)
python3 scripts/run_fisher_suite.py --mode bridge \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db --min-sim 0.75

# Run Pass 1.5 + Pass 2b on an RRP bundle
python3 scripts/run_entity_catalog_pass.py \
    data/rrp/periodic_table/rrp_periodic_table.db \
    data/chroma_db \
    data/ds_wiki.db
```

---

## Critical Architectural Constraints

1. **Never schema-alter `ds_wiki.db`** — read-only source of truth; all new tables go in `wiki_history.db`
2. **INSERT OR IGNORE throughout** — all migration scripts safe to re-run
3. **numpy only** (no scipy) in ingestion passes — scipy not installed
4. **Confidence calibration required** — every new entry or conjecture tagged Established / Supported / Speculative; no silent promotion
5. **Falsification before support** — no conjecture reaches "Supported" without at least one honest falsification attempt
6. **Literature check before novelty claims** — charter § Epistemic Contract rule 1

---

## Conjecture Summary (23 total — **pending M0 audit, numbers may shift**)

**Honest status as of 2026-04-08 — all of these need recalibration in the M0 pass:**

- Previously called "strongest": P4, P15 (information-thermodynamics chain via B5↔INFO1↔INFO5)
- Previously "strengthened": P2, P8, P11, P12, P13
- Contested: P17 (cosmological coupling — multiple 2024-2025 tensions documented)
- New / speculative: P23 (horizon formation as Bekenstein-saturation phase transition) — inherits contested GT11

**CCA-related conjectures (from 2026-04-07 session):**
- CCA-1 (isotropy = criticality) — **FALSIFIED** Phase C
- CCA-1b L^d scaling — **FALSIFIED** Phase D
- CCA-1b magnitude separation (dη/dT ~20× for first-order) — qualitatively confirmed, single test, **not yet in DB as conjecture**
- CCA-1c curve shape — qualitatively confirmed, single test, **not yet in DB as conjecture**
- CCA-2 (d_eff = d_lattice + 1 for d ≥ 2) — confirmed for 2D and 3D tori, single topology family

**Fisher-gravity chain** (M6→IT05→IT03→GT10→GT01): structural observation derived in-wiki from the 2026-04-07 session. Currently framed as a "discovery" — **needs audit** (is this a genuine structural insight or stacked analogies via Jacobson 2016 generality?).

---

## Repo Organization

```
/
├── CLAUDE.md                            ← YOU ARE HERE
├── docs/
│   ├── RESEARCH_PLATFORM_CHARTER.md     ← ANCHOR — read this first
│   ├── SESSION_HANDOVER_2026-04-07.md   ← most recent session
│   ├── CCA_MATHEMATICAL_FORMALIZATION.md ← pending audit
│   ├── CCA_GRAVITY_FINDINGS.md          ← pending audit
│   ├── FISHER_PIPELINE_REDESIGN.md      ← tool spec (still valid)
│   ├── ARCHITECTURE_DECISIONS.md        ← ADR log
│   └── archive/                         ← product-arc docs (historical only)
│       ├── PFD_PROJECT_FOUNDATIONAL_PLAN.md
│       ├── SCF_PHASE3_DESIGN.md
│       └── (other deprecated specs)
├── README.md
├── MASTER_SUMMARY.md                    ← legacy narrative (partially superseded)
├── USER_GUIDE.md                        ← legacy (product framing)
├── setup.sh
├── requirements.txt
├── src/
│   ├── config.py
│   ├── sync.py, embedder.py, extractor.py, topology.py, mcp_server.py
│   ├── analysis/          ← Fisher Suite + diagnostic tools
│   ├── ingestion/         ← RRP parsers and passes
│   └── viz/               ← tier-1/tier-2 visualization
├── scripts/
│   ├── run_fisher_suite.py
│   ├── run_entity_catalog_pass.py
│   ├── ising_fim_*.py, potts_fim_test.py, cca1b_*.py   ← CCA experiments
│   └── migrations/        ← one-time DB insert scripts
├── tests/                 ← pytest suite (587 tests)
├── data/
│   ├── ds_wiki.db         ← READ ONLY
│   ├── chroma_db/, wiki_history.db
│   ├── reports/           ← diagnostic reports + experiment outputs
│   └── rrp/               ← external dataset bundles
└── Outside Ref/           ← external analysis documents
```

---

## If You're A Fresh Claude Session

1. **Read `docs/RESEARCH_PLATFORM_CHARTER.md` first.** It defines the mission and the epistemic rules.
2. **Read the latest `docs/SESSION_HANDOVER_*.md`** for recent state.
3. **Check whether the M0 audit has been completed** — if not, that's the priority before any new work.
4. **Operate as a skeptical research collaborator, not an assistant.** Your job is to push back. Stacking claims is drift. Feature-fitting is drift. Flag both.
5. **Confidence tag everything new.** Established / Supported / Speculative. No silent promotion.

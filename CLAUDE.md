# Principia Formal Diagnostics (PFD) — Claude Code Context

> **This file is auto-loaded by Claude Code on every session start.**
> Full project narrative: `MASTER_SUMMARY.md` | Foundational plan: `docs/PFD_PROJECT_FOUNDATIONAL_PLAN.md` | Pipeline spec: `docs/FISHER_PIPELINE_REDESIGN.md` | Phase 3 SCF design: `docs/SCF_PHASE3_DESIGN.md`

---

## What This Project Is

**PFD** is a research validation system that checks scientific papers and reports for logical consistency against a formalized knowledge graph of scientific and logical foundations. It is a **diagnostic tool, not a judge** — every output shows full reasoning, no black-box verdicts.

- Prior name: DS_Wiki / DS Wiki Transformation
- GitHub: `https://github.com/IanD25/ds-wiki-transformer`
- Python: 3.13, Apple M4 dev machine | also: Windows ShadowPC with RTX 2000 GPU
- Owner: Ian Darling

---

## Quick Start (Fresh Machine / ShadowPC)

```bash
# 1. Clone
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd ds-wiki-transformer

# 2. One-command environment setup
bash setup.sh

# 3. Verify
source .venv/bin/activate
python3 -m pytest tests/ -v --tb=short   # 403 tests should pass

# 4. Optional: start MCP server (for Claude tool access)
python3 src/mcp_server.py
```

**All data committed to repo (no download or rebuild needed):**
- `data/ds_wiki.db` — DS Wiki source of truth (1.5MB, 209 entries, 573 links)
- `data/rrp/` — RRP bundles (zoo_classes, ecoli_core, periodic_table, opera, ccbh)
- `data/chroma_db/` — ChromaDB semantic index (bge-large 1024-dim)
- `data/wiki_history.db` — embedding history snapshots
- `data/reports/` — Fisher Suite HTML reports + structural alignment JSON
- `data/viz/` — Tier-2 visualization outputs

**Rebuild only if ds_wiki.db changes:** `python3 -m src.sync`

---

## Architecture

```
DS Wiki (ds_wiki.db)          RRP Bundle (rrp_*.db)
   SQLite source of truth          Per-dataset SQLite
        │                               │
        ▼                               ▼
   ChromaDB (chroma_db/)        Pass 1: Parse → entries/links
   Semantic index                Pass 1.5: EntityCatalogPass
        │                        Pass 2: CrossUniverseQuery
        │◄──────── bridges ───────────►│
        ▼
   MCP Server (mcp_server.py)
   Exposes all tools to Claude
```

**Six-step PFD diagnostic pipeline (canonical — FISHER_PIPELINE_REDESIGN.md):**
```
Step 1: Ingest RRP → rrp_*.db (entries + links)
Step 2: Build G_internal (within-RRP graph)
Step 3: Internal Diagnostics → Tier-1 Report (coherence, d_eff, regime distribution)
Step 4: Build G_bridge (full Option B: rrp:: nodes + wiki:: nodes + bridge edges)
Step 5: Bridge Diagnostics → Tier-2 Report (DS Wiki integration quality)
Step 6: Two-Tier Output → PFD Score (0.0–1.0)
```
DS Wiki is the **reference lake** — analyzed last, not first.

**Six-layer paper validation pipeline (Phase 3+):**
Layer 1: Claim Extraction (mandatory human gate) →
Layer 2: Foundation Matching (ChromaDB cosine similarity) →
Layer 3: Formal Logic Validation (probabilistic, not boolean) →
Layer 4: Rhetorical Quality (argument structure) →
Layer 5: Evidence Sufficiency →
Layer 6: Domain Boundary Validation → Diagnostic Report

---

## Key Files

| File | Purpose |
|------|---------|
| `src/config.py` | All paths, model name, tier thresholds — edit here first |
| `src/sync.py` | Rebuild chroma_db + wiki_history.db from ds_wiki.db |
| `src/mcp_server.py` | FastMCP server exposing all tools to Claude |
| `src/embedder.py` | BGE embedding, ChromaDB operations |
| `src/ingestion/cross_universe_query.py` | Pass 2: RRP → DS Wiki bridge detection |
| `src/ingestion/passes/entity_catalog_pass.py` | Pass 1.5: Pattern extraction for entity datasets |
| `src/ingestion/detector.py` | Format detection + dataset type classification |
| `scripts/run_entity_catalog_pass.py` | CLI: Pass 1.5 + Pass 2b on a bundle |
| `src/analysis/fisher_diagnostics.py` | Fisher suite: FIM math, `analyze_node`, `sweep_graph`, `build_wiki_graph`, `build_bridge_graph` |
| `src/analysis/fisher_bridge_filter.py` | Per-bridge quality scoring utility (Phase C) |
| `src/analysis/fisher_report.py` | Two-tier PFD report generator (`generate_report`, `PFDReport`) |
| `src/analysis/structural_alignment.py` | Link-type weighted bridge scorer — signed polarity per entry (SCF replacement for SPT) |
| `scripts/run_structural_alignment.py` | CLI: structural alignment on any RRP with populated bridges |
| `docs/SCF_PHASE3_DESIGN.md` | Phase 3 SCF-grounded design — Options 3A–3D |
| `scripts/run_fisher_suite.py` | CLI entry point — all 6 Fisher modes |
| `docs/FISHER_PIPELINE_REDESIGN.md` | Canonical 6-step PFD pipeline spec (Option B bridge graph) |
| `docs/ARCHITECTURE_DECISIONS.md` | ADR log — key design decisions and rationale |
| `data/ds_wiki.db` | The knowledge graph (READ ONLY — never schema-alter) |
| `MASTER_SUMMARY.md` | Full technical re-entry document (read for deep context) |
| `docs/PFD_PROJECT_FOUNDATIONAL_PLAN.md` | v1.1 foundational plan (vision + architecture + governance) |
| `Outside Ref/` | External analysis documents (stress tests, references) |
| `docs/archive/` | Completed specs and planning docs (read-only historical reference) |

---

## Current Embedding Model

```python
# src/config.py — auto-detected at import time (no manual edit needed)
# CUDA (ShadowPC RTX 2000): "BAAI/bge-large-en-v1.5"  # 1024-dim
# MPS  (Mac Apple Silicon): "BAAI/bge-large-en-v1.5"  # 1024-dim
# CPU  (fallback):          "BAAI/bge-base-en-v1.5"   # 768-dim
DEVICE, EMBED_MODEL, EMBED_DIM = _detect_device()  # set automatically
```

Model downloads automatically from HuggingFace on first use (~100MB for base, ~430MB for large).

**Windows note:** DS Wiki entry data contains Unicode math symbols. Always prefix Python commands with `PYTHONUTF8=1` on ShadowPC:
```powershell
PYTHONUTF8=1 .venv\Scripts\python.exe scripts\run_entity_catalog_pass.py ...
```

---

## Phase Status

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 0: Core pipeline | ✅ Complete | sync, embed, topology, MCP |
| Phase 1: Diagnostic tools | ✅ Complete | 268 tests passing |
| Phase 2: RRP Ingestion | ✅ Complete | Zoo + Periodic Table + E. coli + IEEE Power Grid; 403 tests passing |
| Fisher Suite A–G | ✅ Complete | Full 6-step PFD pipeline; bridge graph; two-tier report; 3 MCP tools |
| Tier-1 Visualization | ✅ Complete | D3.js network graph, coherence/regime charts, HTML report per dataset |
| Tier-2 Visualization | ✅ Complete | Bridge histogram, bipartite network, domain heatmap, HTML report |
| Repo Cleanup | ✅ Complete | Docs reorganized; Subsystem B scoped; prototype files marked |
| Phase 3: Paper Analysis | 🔧 In Design | SCF-grounded (see SCF_PHASE3_DESIGN.md): Options 3A–3D. OPERA paper RRP is prototype test case. structural_alignment.py built. |
| Phase 4: Formal Logic Layer | 📋 Planned | Formal annotations on RRP entries; link-type weighted bridge scoring |
| Phase 5: Community Governance | 📋 Planned | After Phase 3 vertical integration complete |

### Fisher Suite — What's Built (Phases A–F)

| Phase | Deliverable | Status |
|-------|-------------|--------|
| A | `decompose_fim`, `build_fim`, `FIMResult`, `analyze_node` | ✅ |
| B | `sweep_graph`, `FisherSweepResult`, `build_wiki_graph` | ✅ |
| C | `fisher_bridge_filter.py`, `scripts/run_fisher_suite.py` (ds_wiki/node/bridges modes) | ✅ |
| D | `build_bridge_graph(rrp_db, wiki_db)`, `--mode internal_rrp`, `--mode bridge` | ✅ |
| E | MCP tools: `fisher_analyze_node`, `fisher_sweep_rrp`, `fisher_sweep_bridge` | ✅ |
| F | `fisher_report.py`, `PFDReport`, `generate_report`, `--mode report` | ✅ |
| G | CLAUDE.md + MASTER_SUMMARY.md documentation pass | ✅ |

**E. coli smoke test (2026-03-11):** PFD Score 0.973/1.000 | INTERNALLY CONSISTENT + WELL-INTEGRATED
- Top internal hub: `met_pyr_c` (pyruvate, d_eff=11) | Top DS Wiki anchor: CHEM5 (134 bridges)

### Fisher Suite CLI Reference

```bash
# Step 3: Internal RRP diagnostics (Tier-1)
python scripts/run_fisher_suite.py --mode internal_rrp \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db

# Step 5: Bridge diagnostics (Tier-2)
python scripts/run_fisher_suite.py --mode bridge \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db --min-sim 0.75

# Steps 3+5+6: Full two-tier PFD report
python scripts/run_fisher_suite.py --mode report \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db

# DS Wiki self-analysis (reference lake health check)
python scripts/run_fisher_suite.py --mode ds_wiki \
    --wiki-db data/ds_wiki.db

# Single node analysis
python scripts/run_fisher_suite.py --mode node \
    --wiki-db data/ds_wiki.db --node-id CHEM5
```

### Phase 2 — What's Done

**Done:**
- `src/ingestion/parsers/zoo_classes_parser.py` — 426 entries, 437 links
- `src/ingestion/parsers/periodic_table_parser.py` — 119 elements, 1671 properties
- `src/ingestion/parsers/ecoli_core_parser.py` — 304 entries, 536 links, 912 bridges
- `src/ingestion/parsers/opera_paper_parser.py` — OPERA paper RRP (Phase 3 prototype)
- `src/ingestion/parsers/ccbh_cluster_parser.py` — 3-paper CCBH cluster RRP
- `src/ingestion/passes/entity_catalog_pass.py` — Pass 1.5 (pattern extraction)
- `scripts/run_entity_catalog_pass.py` — CLI orchestrator
- Periodic table result (bge-large 1024-dim): 497 bridges, 35 tier-1.5, mean_sim 0.818
- Zoo classes result  (bge-large 1024-dim): 1135 bridges, 70 tier-1.5, mean_sim 0.828
  - Top bridge: thm_Nondeterministic_time_hierarchy_theorem <-> CS15 @ 0.9187 (tier-1)
- E. coli result (bge-large 1024-dim): 912 bridges, CHEM5 top anchor (134 bridges)

---

## Key Commands

```bash
# Rebuild semantic index after any ds_wiki.db change
python3 -m src.sync

# Run all tests
python3 -m pytest tests/ -v   # 403 tests

# Run Pass 1.5 + Pass 2b on a bundle
python3 scripts/run_entity_catalog_pass.py \
    data/rrp/periodic_table/rrp_periodic_table.db \
    data/chroma_db \
    data/ds_wiki.db

# Full PFD two-tier diagnostic report for any RRP
python scripts/run_fisher_suite.py --mode report \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db

# Internal RRP diagnostics only (Tier-1, no DS Wiki needed)
python scripts/run_fisher_suite.py --mode internal_rrp \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db

# Query cross-universe bridges directly
python3 -c "
import sqlite3
conn = sqlite3.connect('data/rrp/periodic_table/rrp_periodic_table.db')
for row in conn.execute('SELECT source_entry_title, ds_entry_id, similarity, tier FROM cross_universe_bridges ORDER BY similarity DESC LIMIT 10'):
    print(row)
"

# Run visualizations
python3 -m src.viz.viz_runner \
    data/rrp/periodic_table/rrp_periodic_table.db \
    --ds data/ds_wiki.db
```

---

## DS Wiki Scale (live — as of 2026-03-11)

- **209 entries**: 149 reference_law, 16 method, 15 law, 8 instantiation, 7 open_question, 5 constraint, 3 axiom, 3 parameter, 2 theorem, 1 mechanism
- **573 links**: 29 tier-1, 304 tier-1.5, 73 tier-2, 167 original(null-tier)
- **1,483 ChromaDB chunks** | **786 property rows**
- **0 isolated reference_law entries** (all 12 formerly isolated entries linked)
- Entry ID prefixes: A/B/C/D/E/F/G/H/M/Q/T/X/Ax/OmD + BIO/CHEM/MATH/INFO/STAT/CS/CR/MS (Option E)

---

## Critical Architectural Constraints

1. **Never schema-alter `ds_wiki.db`** — read-only source of truth; all new tables go in `wiki_history.db`
2. **Probabilistic pipeline, not boolean** — never return VALID/INVALID; always return `path_probability` (0–1)
3. **Mandatory human gate at Layer 1** — pipeline pauses for claim verification before Layer 2
4. **formality_tier field** (Phase 4): Tier 1 = physics/math (max 0.95), Tier 2 = chemistry (max 0.85), Tier 3 = soft science (max 0.70)
5. **Vertical integration first** — Phase 3 restricted to thermodynamics + CS complexity; no cross-domain until >80% entries have formality_tier
6. **INSERT OR IGNORE throughout** — all scripts safe to re-run
7. **numpy only** (no scipy) in ingestion passes — scipy not installed

---

## DS Wiki Conjectures Summary (16 total — last assessed 2026-03-11)

Strongest (most supported): P4, P15 (information-thermodynamics chain complete via B5↔INFO1↔INFO5)
Strengthened: P2, P8, P11, P12, P13 (Option E CS/BIO entries added support)
Actionable gap: P7 — INFO4 (DPI) not linked to Ax2; one link closes the chain

---

## GPU Notes (ShadowPC — RTX 2000)

Both machines (Mac M4 MPS + ShadowPC CUDA) auto-detect and run bge-large 1024-dim.

Future upgrade priorities:
1. Add `cross-encoder/ms-marco-MiniLM-L-12-v2` for bridge reranking
2. Local LLM for Phase 3 claim extraction: `phi-3-mini-4k-instruct` (4-bit, ~2.5GB VRAM)
3. Fine-tune bge-small on DS Wiki link pairs (contrastive learning, ~2-4 hours)

---

## Repo Organization

```
/
├── CLAUDE.md              ← YOU ARE HERE (auto-loaded by Claude Code)
├── README.md              ← GitHub/public facing
├── MASTER_SUMMARY.md      ← Full technical context for re-entry
├── USER_GUIDE.md          ← End-user report interpretation guide
├── setup.sh               ← One-command environment setup
├── requirements.txt       ← Python dependencies
├── docs/
│   ├── FISHER_PIPELINE_REDESIGN.md  ← Canonical 6-step PFD pipeline spec
│   ├── ARCHITECTURE_DECISIONS.md    ← ADR log
│   ├── PFD_PROJECT_FOUNDATIONAL_PLAN.md  ← v1.1 vision + governance
│   ├── TIER1_VALIDATION_REPORT.md   ← Cross-domain validation results
│   ├── design_philosophy/
│   └── archive/           ← Completed specs (read-only historical)
├── src/
│   ├── config.py          ← All paths, model, thresholds — edit here first
│   ├── sync.py, embedder.py, extractor.py, topology.py, mcp_server.py
│   ├── analysis/          ← Diagnostic tools
│   │   ├── fisher_diagnostics.py   ← FIM math, analyze_node, sweep_graph, build_bridge_graph
│   │   ├── fisher_bridge_filter.py ← Per-bridge quality scoring
│   │   ├── fisher_report.py        ← Two-tier PFD report generator
│   │   ├── gap_analyzer.py         ← [DS Wiki scoped] Gap detection — Phase 3 integration target
│   │   ├── coverage_analyzer.py    ← [DS Wiki scoped] Coverage metrics — Phase 3 integration target
│   │   ├── hypothesis_generator.py ← [DS Wiki scoped] Surprising pair detection
│   │   ├── result_validator.py     ← [DS Wiki scoped] Claim validator — PRIMARY Phase 3 target
│   │   ├── link_classifier.py      ← [DS Wiki scoped] LLM link-type classifier
│   │   └── semantic_position_test.py  ← [PROTOTYPE/PARKED] SPT — see file header
│   ├── ingestion/
│   │   ├── parsers/       ← zoo_classes, periodic_table, ecoli_core, ieee_power_grid, opera, ccbh_cluster
│   │   ├── passes/        ← entity_catalog_pass.py
│   │   ├── enrichers/     ← prose_enricher.py [PARKED — see file header]
│   │   ├── rrp_bundle.py, detector.py, cross_universe_query.py
│   └── viz/               ← Visualization module
│       ├── tier1_dashboard.py  ← Tier-1 PNG charts + D3.js network
│       ├── tier1_report.py     ← Tier-1 HTML report generator
│       ├── tier2_report.py     ← Tier-2 HTML report generator
│       ├── bridge_network.py, domain_heatmap.py, similarity_hist.py
│       └── viz_runner.py       ← CLI entry for all viz outputs
├── scripts/
│   ├── run_fisher_suite.py    ← Fisher CLI (6 modes)
│   ├── run_entity_catalog_pass.py
│   ├── run_spt.py             ← [PROTOTYPE/PARKED] SPT CLI
│   └── migrations/            ← One-time DB insert scripts
├── tests/                 ← pytest suite (403 tests)
├── data/
│   ├── ds_wiki.db         ← Reference knowledge graph (READ ONLY)
│   ├── chroma_db/         ← ChromaDB vector index (bge-large 1024-dim)
│   ├── wiki_history.db    ← Embedding history snapshots
│   ├── reports/           ← Fisher Suite HTML reports + SA results
│   ├── viz/               ← Tier-2 visualization outputs
│   ├── viz_outputs/       ← Tier-1 visualization outputs
│   └── rrp/               ← RRP bundles
│       ├── zoo_classes/
│       ├── periodic_table/
│       ├── ecoli_core/
│       ├── opera/
│       └── ccbh/          ← 3-paper CCBH cluster + Layer 1 analysis
└── Outside Ref/           ← External analysis documents
```

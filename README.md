# Principia Formal Diagnostics (PFD)
## Graph Coherence Engine for Research Datasets

**Automatically analyze research datasets for structural coherence, dimensionality, and formal grounding.**

Give PFD a structured dataset — metabolic networks, taxonomies, power grids, chemical databases, knowledge graphs — and it produces:

- **Tier-1 Report** — Internal structural coherence, Fisher effective dimension (D_eff), regime classification, interactive network visualization
- **Tier-2 Report** — Cross-dataset bridge analysis: how well this dataset anchors to a formal reference knowledge graph
- **PFD Score** — Combined 0.0–1.0 quality score with full reasoning (no black-box verdicts)

> **Status: Active research tool. Not yet public-release ready. Architecture stable; Phase 3 (paper analysis) in design.**

---

## Pipeline Overview

```
Your Dataset (CSV / JSON / MATPOWER / custom)
    │
[Step 1] INGEST         → entries + links → rrp_*.db (SQLite)
[Step 2] BUILD GRAPH    → NetworkX internal graph
[Step 3] TIER-1         → D_eff, coherence score, regime distribution
    │                      → Tier-1 HTML report + D3.js network viz
    │
[Step 4] BUILD BRIDGE   → RRP nodes ↔ DS Wiki nodes (semantic similarity)
[Step 5] TIER-2         → Bridge quality, anchor distribution, domain coverage
    │                      → Tier-2 HTML report
    │
[Step 6] PFD SCORE      → 0.0–1.0 combined verdict
```

---

## Validated Datasets (as of 2026-03-14)

| Dataset | Entries | Links | PFD Score | Verdict |
|---------|---------|-------|-----------|---------|
| E. coli core metabolic network | 304 | 536 | 0.973 | CONSISTENT + WELL-INTEGRATED |
| Zoo animal taxonomy | 426 | 437 | — | CONSISTENT |
| Periodic Table | 119 elements | 1,671 properties | — | CONSISTENT |
| IEEE Power Grid (case14/57/118) | 14–118 buses | varies | — | MARGINAL (domain-correct for sparse grids) |
| OPERA paper (Phase 3 prototype) | 15 | 19 | — | Paper-based RRP test case |
| CCBH cluster (3 papers) | multi-paper | multi-paper | — | Cosmological coupling cluster |

---

## Quick Start

```bash
# 1. Clone + setup
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd ds-wiki-transformer
bash setup.sh

# 2. Activate environment
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows

# 3. Run Tier-1 diagnostics on an included dataset
python scripts/run_fisher_suite.py --mode internal_rrp \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db

# 4. Full two-tier report
python scripts/run_fisher_suite.py --mode report \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db

# 5. Verify (403 tests)
python -m pytest tests/ -v --tb=short
```

**Windows (ShadowPC):** Prefix Python commands with `PYTHONUTF8=1` to handle Unicode math symbols in DS Wiki entries.

---

## Documentation

| Document | Purpose |
|----------|---------|
| **[USER_GUIDE.md](USER_GUIDE.md)** | Report interpretation, metric definitions, worked examples |
| [MASTER_SUMMARY.md](MASTER_SUMMARY.md) | Full technical reference for contributors |
| [docs/FISHER_PIPELINE_REDESIGN.md](docs/FISHER_PIPELINE_REDESIGN.md) | Canonical 6-step pipeline specification |
| [docs/ARCHITECTURE_DECISIONS.md](docs/ARCHITECTURE_DECISIONS.md) | Key design decisions and rationale |
| [docs/SCF_PHASE3_DESIGN.md](docs/SCF_PHASE3_DESIGN.md) | Phase 3 SCF-grounded design |
| [CLAUDE.md](CLAUDE.md) | Project context for LLM assistants (auto-loaded by Claude Code) |

---

## Key Commands

```bash
# Tier-1 only (no DS Wiki needed)
python scripts/run_fisher_suite.py --mode internal_rrp \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db

# Tier-2 bridge diagnostics
python scripts/run_fisher_suite.py --mode bridge \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db --min-sim 0.75

# Full report (both tiers + PFD score)
python scripts/run_fisher_suite.py --mode report \
    --rrp-db data/rrp/ecoli_core/rrp_ecoli_core.db \
    --wiki-db data/ds_wiki.db

# DS Wiki self-analysis (reference graph health check)
python scripts/run_fisher_suite.py --mode ds_wiki \
    --wiki-db data/ds_wiki.db

# Single node deep-dive
python scripts/run_fisher_suite.py --mode node \
    --wiki-db data/ds_wiki.db --node-id CHEM5
```

---

## Requirements

- Python 3.13
- ~500MB disk (all data committed — no rebuild needed after clone)
- CPU, CUDA (RTX 2000+), or Apple Silicon — auto-detected

```
sentence-transformers  # BGE embeddings (auto-downloaded from HuggingFace)
chromadb               # semantic indexing
pandapower             # IEEE power grid parsing
fastmcp                # optional MCP server for Claude tool access
```

---

## Project Structure

```
ds-wiki-transformer/
├── CLAUDE.md                      ← LLM context (auto-loaded)
├── README.md                      ← This file
├── MASTER_SUMMARY.md              ← Full technical reference
├── USER_GUIDE.md                  ← User-facing interpretation guide
├── docs/
│   ├── FISHER_PIPELINE_REDESIGN.md
│   ├── ARCHITECTURE_DECISIONS.md
│   ├── PFD_PROJECT_FOUNDATIONAL_PLAN.md
│   ├── TIER1_VALIDATION_REPORT.md
│   └── archive/                   ← Completed specs (historical)
├── src/
│   ├── analysis/
│   │   ├── fisher_diagnostics.py  ← Core FIM math + graph metrics
│   │   ├── fisher_report.py       ← Report generator
│   │   └── fisher_bridge_filter.py
│   ├── ingestion/
│   │   ├── parsers/               ← ecoli, zoo, periodic_table, ieee, opera, ccbh
│   │   ├── passes/                ← entity_catalog_pass.py
│   │   └── cross_universe_query.py
│   └── viz/
│       ├── tier1_dashboard.py     ← Coherence/regime charts + D3.js network
│       ├── tier1_report.py        ← Tier-1 HTML report
│       └── tier2_report.py        ← Tier-2 HTML report
├── scripts/
│   ├── run_fisher_suite.py        ← Main CLI (6 modes)
│   └── run_entity_catalog_pass.py
├── data/
│   ├── ds_wiki.db                 ← Reference knowledge graph
│   ├── chroma_db/                 ← ChromaDB vector index (bge-large 1024-dim)
│   ├── wiki_history.db            ← Embedding history snapshots
│   ├── reports/                   ← Fisher Suite HTML reports
│   ├── viz/                       ← Visualization outputs
│   └── rrp/                       ← Dataset bundles
└── tests/                         ← 403 tests
```

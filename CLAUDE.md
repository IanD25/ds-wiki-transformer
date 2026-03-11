# Principia Formal Diagnostics (PFD) — Claude Code Context

> **This file is auto-loaded by Claude Code on every session start.**
> Full project narrative: `MASTER_SUMMARY.md` | Full foundational plan: `PFD_PROJECT_FOUNDATIONAL_PLAN.md`

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

# 3. Rebuild generated artifacts (chroma_db + wiki_history.db from ds_wiki.db)
source .venv/bin/activate
python3 -m src.sync

# 4. Verify
python3 -m pytest tests/ -v --tb=short   # 268 tests should pass

# 5. Optional: start MCP server (for Claude tool access)
python3 src/mcp_server.py
```

**Data files committed to repo (no download needed):**
- `data/ds_wiki.db` — DS Wiki source of truth (1.5MB, 209 entries, 573 links)
- `data/rrp/` — RRP test bundles (zoo_classes, ecoli_core, periodic_table)

**Generated artifacts (gitignored, rebuilt by sync.py):**
- `data/chroma_db/` — ChromaDB semantic index (~30s to rebuild)
- `data/wiki_history.db` — embedding history snapshots (~10s to rebuild)

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

**Six-layer validation pipeline (Phase 3+):**
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
| `data/ds_wiki.db` | The knowledge graph (READ ONLY — never schema-alter) |
| `MASTER_SUMMARY.md` | Full technical re-entry document (read for deep context) |
| `PFD_PROJECT_FOUNDATIONAL_PLAN.md` | v1.1 foundational plan (vision + architecture + governance) |
| `Outside Ref/` | External analysis documents (stress tests, references) |

---

## Current Embedding Model

```python
# src/config.py
EMBED_MODEL = "BAAI/bge-base-en-v1.5"   # 768-dim
# GPU upgrade target: "BAAI/bge-large-en-v1.5"  # 1024-dim, better bridges
```

Model downloads automatically from HuggingFace on first use (~100MB).

---

## Phase Status

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 0: Core pipeline | ✅ Complete | sync, embed, topology, MCP |
| Phase 1: Diagnostic tools | ✅ Complete | 268 tests passing |
| Phase 2: RRP Ingestion | ⏳ In Progress | Zoo + Periodic Table done; E. coli pending |
| Phase 3: Paper Analysis | 📋 Planned | Claim extractor, logic validator, report gen |
| Phase 4: Formal Logic Layer | 📋 Planned | Formal axioms, argument templates, fallacy catalog |
| Phase 5: Community Governance | 📋 Planned | After Phase 3 vertical integration complete |

### Phase 2 — What's Done vs. Next

**Done:**
- `src/ingestion/parsers/zoo_classes_parser.py` — 426 entries, 437 links
- `src/ingestion/parsers/periodic_table_parser.py` — 119 elements, 1671 properties
- `src/ingestion/passes/entity_catalog_pass.py` — Pass 1.5 (pattern extraction)
- `scripts/run_entity_catalog_pass.py` — CLI orchestrator
- Periodic table result: 500 bridges, 40 tier-1.5, mean_sim 0.818

**Next (Phase 2 remaining):**
1. **Hyperedge architecture decision** (PREREQUISITE for E. coli parser) — document in `ARCHITECTURE_DECISIONS.md`: Reification (Option A) vs. Native Hyperedge Table (Option B)
2. `src/ingestion/parsers/ecoli_core_parser.py` — COBRA JSON, 95 reactions, 72 metabolites, stoichiometry-as-links
3. `INGESTION_GUIDE.md` + `SCHEMA_REFERENCE.md`

---

## Key Commands

```bash
# Rebuild semantic index after any ds_wiki.db change
python3 -m src.sync

# Run all tests
python3 -m pytest tests/ -v

# Run Pass 1.5 + Pass 2b on a bundle
python3 scripts/run_entity_catalog_pass.py \
    data/rrp/periodic_table/rrp_periodic_table.db \
    data/chroma_db \
    data/ds_wiki.db

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

With CUDA available, upgrade priorities:
1. Change `EMBED_MODEL` in `config.py` to `"BAAI/bge-large-en-v1.5"` (1024-dim, better bridges)
2. Add `cross-encoder/ms-marco-MiniLM-L-12-v2` for reranking
3. Local LLM for Phase 3 claim extraction: `phi-3-mini-4k-instruct` (4-bit, ~2.5GB VRAM)
4. Fine-tune bge-small on DS Wiki link pairs (contrastive learning, ~2-4 hours)
Install: `pip install torch --extra-index-url https://download.pytorch.org/whl/cu118`

---

## Repo Organization

```
/
├── CLAUDE.md              ← YOU ARE HERE (auto-loaded by Claude Code)
├── README.md              ← GitHub/public facing
├── MASTER_SUMMARY.md      ← Full technical context for re-entry
├── PFD_PROJECT_FOUNDATIONAL_PLAN.md  ← v1.1 foundational plan
├── setup.sh               ← One-command environment setup
├── requirements.txt       ← Python dependencies
├── src/                   ← Source code
│   ├── config.py          ← All config constants
│   ├── sync.py, embedder.py, extractor.py, topology.py, mcp_server.py
│   ├── analysis/          ← Phase 1 diagnostic tools
│   ├── ingestion/         ← Phase 2 RRP ingestion
│   │   ├── parsers/       ← zoo_classes, periodic_table, (ecoli_core TBD)
│   │   ├── passes/        ← entity_catalog_pass.py
│   │   ├── rrp_bundle.py, detector.py, cross_universe_query.py
│   └── viz/               ← Visualization module
├── scripts/               ← Operational scripts (run_entity_catalog_pass.py etc.)
│   └── migrations/        ← One-time DB insert scripts (insert_chunk*.py etc.)
├── tests/                 ← pytest suite (268 tests)
├── data/
│   ├── ds_wiki.db         ← Source of truth (committed)
│   └── rrp/               ← RRP bundles + raw data (committed)
│       ├── zoo_classes/
│       ├── periodic_table/
│       └── ecoli_core/
└── Outside Ref/           ← External analysis documents
```

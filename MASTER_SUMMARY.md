# DS Wiki Transformation — Master Summary
**The definitive re-entry document. Read this at the start of any new session.**

**Last Updated**: 2026-03-10
**Status**: Phase 1 Diagnostics complete. Option E (DS Tier 1/2 expansion) complete. Phase 2 (RRB ingestion) designed, not yet coded.

---

## What This Project Is

Transform the DS 2.x Wiki (a physics framework called Dimensional Scaling) from a
SQLite + Markdown knowledge base into a semantically-indexed discovery engine accessible
to Claude via MCP server. Then generalise that engine into a **domain-agnostic toolkit**
for any researcher with a structured knowledge base.

**Two goals in parallel:**
1. DS-specific: make the DS wiki searchable and discoverable via semantic vectors
2. Generic: make that same architecture reusable for any research domain

---

## Repository Layout

```
GitHub: IanD25/ds-wiki-transformer
Local:  /Users/iandarling/Projects/DS_Wiki_Transformation/

DS_Wiki_Transformation/
├── MASTER_SUMMARY.md              ← THIS FILE
├── SPEC.md                        ← Original DS-specific architecture spec
├── GENERIC_TOOLKIT_SPEC.md        ← Full generic toolkit architecture (1,083 lines)
├── IMPLEMENTATION_ROADMAP.md      ← Phase 1 implementation plan (complete)
├── PROJECT_OVERVIEW.md            ← Navigation document (high-level)
├── README.md
├── requirements.txt
│
├── src/
│   ├── config.py                  ← Paths, model settings, tier thresholds
│   ├── extractor.py               ← Reads ds_wiki.db → Chunk objects
│   ├── embedder.py                ← Embeds chunks into ChromaDB + snapshots
│   ├── topology.py                ← Reads wiki_history.db, semantic evolution
│   ├── sync.py                    ← Full pipeline: extract → embed → snapshot
│   ├── mcp_server.py              ← MCP server exposing all tools to Claude
│   └── analysis/                  ← Phase 1 Diagnostics (JUST BUILT)
│       ├── __init__.py
│       ├── hypothesis_generator.py
│       └── coverage_analyzer.py
│
├── scripts/                       ← One-time enrichment scripts (all completed)
│   ├── add_phase1_taxonomy.py     ← Mathematical archetypes + D-sensitivity
│   ├── add_phase2_math_prose.py   ← "What The Math Says" prose sections
│   ├── add_phase3_concept_tags.py ← Semantic anchor phrases
│   └── add_tier2_links.py         ← Hand-validated explicit links
│
├── tests/
│   ├── test_hypothesis_generator.py   ← 31 unit tests (all passing)
│   ├── test_coverage_analyzer.py      ← 56 unit tests (all passing)
│   └── test_integration.py            ← 52 integration tests (all passing)
│
└── data/
    ├── chroma_db/                 ← ChromaDB persistent storage
    └── wiki_history.db            ← Append-only embedding snapshot history
```

**Source DB (read-only, never modified):**
```
/Users/iandarling/Library/Mobile Documents/com~apple~CloudDocs/Primary Work Outputs/
wiki build/ds-wiki-repo/ds_wiki.db
```

---

## Architecture: Three Layers

```
LAYER 3: SEMANTIC ENRICHMENT
  ├── Taxonomy layers (archetypes, d-sensitivity, concept tags)
  ├── "What The Math Says" prose (equations → natural language)
  ├── Explicit links (3-tier confidence validation)
  └── Diagnostic tools (HypothesisGenerator, CoverageAnalyzer)
         ↑
LAYER 2: VECTOR INDEX
  ├── BGE-Small-EN-v1.5 (112M params, 384-dim, local, ~90MB)
  ├── ChromaDB persistent storage
  ├── One chunk per section (chunk_id = {entry_id}_{section_name_normalized})
  └── wiki_history.db: append-only embedding snapshots
         ↑
LAYER 1: KNOWLEDGE BASE
  ├── ds_wiki.db (SQLite, read-only source of truth)
  └── Tables: entries, sections, entry_properties, links,
              entry_connections, references_, bridge_content,
              conjectures, gates, conjecture_summary,
              link_type_definitions, wiki_meta
```

**Embedding model**: `BAAI/bge-small-en-v1.5` — 112M parameters, 384-dim dense
vectors, trained with contrastive learning on scientific + general text. Runs
locally, no API calls, no cost.

---

## DS Wiki: Current Data State

| Metric | Value | Notes |
|--------|-------|-------|
| Total entities | 199 | 139 reference_law + 60 DS-native |
| Entity types | 10 | reference_law, method, law, instantiation, open question, constraint, axiom, parameter, theorem, mechanism |
| Total sections | 1,550 | 398 original + 851 enrichment + 301 Option E |
| Total links | 383 | 167 original (NULL tier) + 174 discovered (tier 1.5) + 38 Tier 2 + 4 other |
| Property rows | 786 | archetype + d-sensitivity + concept_tags + others |
| ChromaDB chunks | 1,562 | One per section |
| Embedding dimension | 384 | BGE-Small |
| ChromaDB snapshots | 7 | snap_20260309_233846 through snap_20260310_090912 |
| High-similarity pairs | 983+ | Similarity ≥ 0.82 (pre-Option E baseline) |
| Cross-domain pairs | 90+ | Increased from 53 (+37, +70%) — pre-Option E baseline |

### Entity Type Breakdown
```
reference_law   139    (physics, biology, chemistry, CS, math, info theory, etc. — 43 added by Option E)
method           16    (DS computational methods)
law              15    (DS-native laws, including OmD — the core Ω_D operator)
instantiation     8    (concrete realisations in specific D_eff regimes)
open question     7    (unresolved DS questions)
constraint        5    (DS constraints)
axiom             3    (DS axioms)
parameter         3    (DS parameters)
theorem           2    (DS theorems)
mechanism         1    (DS mechanisms)
```

### Archetype Distribution (15 categories)
```
thermodynamic-bound        21   ████████████████████
equilibrium-condition      20   ████████████████████
dimensional-scaling        18   ██████████████████
geometric-ratio            16   ████████████████
statistical-distribution   15   ███████████████
power-law-scaling          12   ████████████
conservation-law           12   ████████████
gradient-flux-transport     9   █████████
variational-principle       6   ██████
symmetry-conservation       6   ██████
coupled-field-equations     6   ██████
inverse-square-geometric    5   █████
exponential-decay           5   █████
wave-equation               3   ███
diffusion-equation          2   ██
```

### Link Type Distribution
```
tests           59   (DS conjectures/gates tested by entries)
couples to      49   (semantic coupling)
implements      42   (DS methods implementing reference laws)
generalizes     30   (DS laws generalising reference laws)
derives from    28   (derivation chains)
analogous to    26   (structural analogies)
constrains      13   (constraint relationships)
predicts for     5   (predictive links)
tensions with    2   (contradictions/tensions)
```

### Key Discoveries (from pairwise analysis)
```
Wien ↔ Planck         (B3 ↔ RD1)   sim=0.8999  Cross-domain: EM ↔ QM
Landauer ↔ 2nd Law    (B5 ↔ TD3)   sim=0.8673  Info theory ↔ Thermodynamics (Tier 2 linked)
Ax1 ↔ QM2                          sim=0.8464  DS axiom ↔ quantum mechanics
Carnot Efficiency ↔ Carnot Theorem  (TD13 ↔ TD8) sim=0.9481 (NO existing link — candidate)
Newton ↔ Euler Laws   (CM1 ↔ CM6)  sim=0.9249  (NO existing link — candidate)
```

---

## What Was Built: Session-by-Session

### Session 1 (earlier — pre-summary)
- Designed 3-layer architecture (SPEC.md)
- Built config.py, extractor.py, embedder.py, topology.py, sync.py
- Created wiki_history.db schema
- Imported 96 reference laws from a 114-law markdown document

### Session 2 (prior session — compacted)
**Phase 1 Taxonomy** (add_phase1_taxonomy.py):
- Added `mathematical_archetype` and `dimensional_sensitivity` properties to all 156 entries
- Added "Mathematical Archetype" section to all 156 entries
- Result: 312 property rows + 156 new sections → ChromaDB grew 817 → 973 chunks

**Phase 2 Math Prose** (add_phase2_math_prose.py):
- Translated LaTeX equations to natural language for 132 entries
- Most impactful enrichment: LaTeX tokenises to noise in BGE; prose carries signal
- Result: 132 new sections → 973 → 1105 chunks; pairs: 697 → 983 (+41%)

**Phase 3 Concept Tags** (add_phase3_concept_tags.py):
- 5-10 semantic anchor phrases per entry, as both properties and sections
- Result: 156 new property rows + 156 sections → 1105 → 1261 chunks

**Tier 2 Links** (add_tier2_links.py):
- 38 explicit hand-validated links (derives from, implements, generalizes, analogous to)
- Covered: OmD→GV1/CM2/QM1/EM1/EM6, G1→GV1/CM2/GV3, B5→TD3, B3→RD1/RD3
- Total links: 167 original + 87 discovered + 38 Tier 2 = 254

**Errors resolved** (important context):
- Git object corruption from iCloud offloading → fixed with `git fetch --all`
- Non-fast-forward push → resolved by extracting remote DB, re-applying SQL changes
- ChromaDB import name (`COLLECTION_NAME` vs `CHROMA_COLLECTION`) → fixed
- Links table column names (`source_entry_id` vs `source_id`) → fixed

### Session 4 (Option E — DS Tier 1/2 Expansion)
**Goal**: Expand DS wiki Tier 1/2 Primary layers to cover core science broadly, making DS the
universal vector anchor layer for all future RRB ingestions.

**Chunk 1** (scripts/insert_chunk1_bio_chem.py — 13 entries):
BIO1–BIO9 (Central Dogma, Hardy-Weinberg, Mendelian Segregation, Independent Assortment,
Michaelis-Menten, Metabolic Flux Balance, DNA Replication Fidelity, Population Growth/Logistic,
Natural Selection/Fitness), CHEM1–CHEM4 (Le Chatelier's, Arrhenius, Hess's Law, Henderson-Hasselbalch)

**Chunk 2** (scripts/insert_chunk2_math_info.py — 15 entries):
MATH1–MATH8 (Bayes' Theorem, CLT, LLN, Gödel Incompleteness, FTC, Prime Number Theorem,
Euler's Identity, Generalized Stokes' Theorem), INFO1–INFO5 (Shannon Entropy, Source Coding,
Noisy-Channel, Mutual Information/DPI, Kolmogorov Complexity), STAT1–STAT2 (Max Entropy, Ergodic)

**Chunk 3** (scripts/insert_chunk3_cs.py — 15 entries):
CS1–CS15 (Church-Turing, Halting Problem, Rice's Theorem, Cook-Levin/NP-completeness, Master
Theorem, Nyquist-Shannon, CAP Theorem, Amdahl's Law, Little's Law, No Free Lunch, Sort Lower
Bound Ω(n log n), FLP Impossibility, Perron-Frobenius, Byzantine Fault Tolerance, Time Hierarchy)

**Result**: 43 new reference_law entries, 156→199 total; 1261→1562 vectors; 87→174 tier-1.5 links.
Final snapshot: snap_20260310_090912. All 3 scripts use INSERT OR IGNORE (safe re-run).
New domains added: mathematics, computer science, information theory, mathematics · computer science,
computer science · mathematics, information · mathematics, information · physics, chemistry · biology.

---

### Session 3 (Generic Toolkit Design + Phase 1 Diagnostics)
**Generic Toolkit Design** (three new specification documents):
- GENERIC_TOOLKIT_SPEC.md (1,083 lines) — full domain-agnostic architecture
- IMPLEMENTATION_ROADMAP.md (425 lines) — Phase 1 plan with pseudocode
- PROJECT_OVERVIEW.md (340 lines) — navigation document

**Phase 1 Diagnostics** (src/analysis/ — fully implemented):
- HypothesisGenerator: finds surprising pairs (sim/baseline > threshold), generates research prompts
- CoverageAnalyzer: property coverage, network density, gap analysis, markdown reports
- 139 tests (31 + 56 unit + 52 integration) — **all passing**

**RRB Integration Analysis** (discussed, not yet coded):
- Current architecture not directly ready for RRBs
- Schema maps cleanly to RO-Crate, Frictionless Data, BagIt
- Two-pass approach designed: deterministic parser + LLM-guided mapping
- Three things needed: format parsers, LLM instruction package, MCP ingestion tools

---

## Diagnostic Tools: How to Use Them

### HypothesisGenerator
```python
# Run from src/ directory
from analysis import HypothesisGenerator

gen = HypothesisGenerator()  # uses config.py defaults

# Find surprising pairs
pairs = gen.find_surprising_pairs(
    sim_threshold=0.80,      # minimum cosine similarity
    surprise_threshold=1.15,  # minimum sim/type_baseline ratio
    max_pairs=100,
    include_linked=True,      # include already-linked pairs
)

# Get markdown report
print(gen.generate_markdown_report(pairs))

# Get compact stats dict
print(gen.get_stats())
```

```bash
# CLI
python3 analysis/hypothesis_generator.py --output markdown --sim-threshold 0.82 --max-pairs 50
python3 analysis/hypothesis_generator.py --output json --surprise-threshold 1.20 --no-linked
python3 analysis/hypothesis_generator.py --output stats
```

**Algorithm**: Loads embeddings from wiki_history.db (latest snapshot) → computes
entry-level centroids → N×N pairwise cosine similarity → filters by
sim_threshold AND surprise_factor = sim/baseline ≥ surprise_threshold →
generates 6 typed research prompts per pair.

### CoverageAnalyzer
```python
from analysis import CoverageAnalyzer

ca = CoverageAnalyzer()  # uses config.py defaults

# Full report
report = ca.compute_report()  # CoverageReport dataclass

# Markdown
print(ca.generate_markdown())

# Stats dict
print(ca.get_stats())
```

```bash
python3 analysis/coverage_analyzer.py --output markdown
python3 analysis/coverage_analyzer.py --output json
```

**Metrics**: entity type distribution, domain distribution, section counts,
property coverage % (with value distributions), 15-archetype breakdown,
d-sensitivity counts, network density, isolated entities, link type
distribution, confidence tier distribution, gap recommendations.

---

## Test Suite

```bash
# All 139 tests
python3 -m pytest tests/ -v

# Unit tests only (no DB needed)
python3 -m pytest tests/test_hypothesis_generator.py tests/test_coverage_analyzer.py -v

# Integration tests only (needs ds_wiki.db + wiki_history.db)
python3 -m pytest tests/test_integration.py -v
```

**Test architecture**:
- Unit tests use synthetic in-memory SQLite + numpy embeddings (no external files)
- Integration tests use real DS wiki data, verify specific discoveries (B5↔TD3, etc.)
- All tests are fully self-contained and deterministic

---

## Generic Toolkit: Design Status

The framework has been designed as a reusable platform for any research domain.

### Core Concept
```
Researcher's Knowledge Base (any format)
         ↓  [Transformer Input Translator]
Normalised SQLite (entities/sections/properties/links)
         ↓  [Taxonomy Application Engine]
Enriched SQLite + ChromaDB Vector Index
         ↓  [Diagnostic Toolkit]
Discoveries: surprising pairs, coverage gaps, hypothesis prompts
```

### Phases

| Phase | Status | Description |
|-------|--------|-------------|
| 0: Scaffolding | ✅ Complete | SQLite schema, ChromaDB, BGE embeddings, pairwise analysis, link validation |
| 1: Diagnostics | ✅ Complete | HypothesisGenerator + CoverageAnalyzer (this session) |
| 2a: Format Parsers | ❌ Not started | RO-Crate, Frictionless Data, CSV adapters |
| 2b: LLM Instruction Package | ❌ Not started | INGESTION_GUIDE.md, SCHEMA_REFERENCE.md |
| 2c: MCP Ingestion Tools | ❌ Not started | Expose parsers via MCP server |
| 3: Usability/Export | ❌ Not started | CLI, interactive HTML visualisation, markdown reports |
| 4: Packaging | ❌ Not started | PyPI package, examples, documentation |

### RRB Format Readiness

| Format | Schema Match | Parser | Status |
|--------|-------------|--------|--------|
| RO-Crate (ro-crate-metadata.json) | ✅ Excellent | ❌ Missing | Design complete |
| Frictionless Data (datapackage.json) | ✅ Good | ❌ Missing | Design complete |
| BagIt | ⚠️ Wrapper only | ❌ Missing | Need to unpack first |
| Flat CSV + YAML config | ✅ Designed | ❌ Missing | YAML spec written |
| Raw JSON array | ✅ Designed | ❌ Missing | YAML spec written |

**RO-Crate → Our Schema mapping** (confirmed clean match):
```
@graph[n]["@type"]      →  entries.entry_type
@graph[n]["name"]       →  entries.title
@graph[n]["description"]→  entries.description
@graph[n]["hasPart"]    →  links (link_type: "contains")
@graph[n]["author"]     →  links (link_type: "authored_by")
@graph[n]["keywords"]   →  entity_properties (concept_tags)
File entities           →  sections (embeddable content)
```

---

## Immediate Next Steps (choose one to start next session)

### ✅ Option E: COMPLETE — DS Tier 1/2 Expansion (43 new entries, 1562 vectors)
All three chunks executed and pushed. DS is now the universal vector anchor layer.

### Option A: LLM Instruction Package first (fastest to value)
Build `INGESTION_GUIDE.md` and `SCHEMA_REFERENCE.md` — makes the toolkit immediately
usable by any LLM (Claude Code, Cursor, Windsurf/Cascade) to guide project owners
through ingestion even before the parsers exist.

**Deliverables**: 2 documents, ~2 days, no code required.
**Value**: Any researcher can use the toolkit immediately with LLM assistance.

### Option B: RO-Crate Parser first (most common RRB format)
Build `src/ingestion/ro_crate_parser.py` — reads `ro-crate-metadata.json`,
extracts entities + relationships, maps to our schema, runs validator.

**Deliverables**: 1 Python module + tests, ~3 days.
**Value**: Can directly ingest RO-Crate bundles (Zenodo, OSF, institutional repos).

### Option C: Result Validator + Gap Analyzer (complete Phase 1)
Build the remaining two Phase 1 diagnostic tools (from IMPLEMENTATION_ROADMAP.md):
- ResultValidator: check research claims against KB for contradictions/support
- GapAnalyzer: identify under-covered domains with enrichment recommendations

**Deliverables**: 2 Python modules + unit tests + integration tests, ~1 week.
**Value**: Completes the Phase 1 diagnostic suite.

### Option D: Full ingestion pipeline
Build the complete ingestion stack at once:
- detector.py (format detection)
- ro_crate_parser.py
- frictionless_parser.py
- csv_parser.py
- validator.py
- INGESTION_GUIDE.md

**Deliverables**: 5 Python modules + 2 documents + tests, ~2 weeks.
**Value**: Complete Phase 2a+2b in one go.

### Option E: Expand DS Tier 1 & 2 Primary Layers — Core Science Knowledge Base ⭐ PROJECT IDEA
**Background**: The three confirmed RRB test cases (E. coli Core Metabolic Network, Periodic
Table, Complexity Zoo) will use DS Tier 1 & 2 as supplemental vector reference data —
meaning the DS knowledge base anchors cross-domain discovery. This only works well if
Tiers 1 & 2 are broad enough to cover fundamental science, not just the DS framework laws
currently ingested.

**The idea**: Expand the DS wiki Tier 1 & 2 Primary layers to include canonical entries for:
- **Physics**: Newton's laws, thermodynamic laws, Maxwell's equations, quantum postulates,
  relativity principles, statistical mechanics foundations, conservation laws (energy,
  momentum, charge, baryon number)
- **Biology**: Central dogma, Mendel's laws, Hardy-Weinberg equilibrium, metabolic
  principles (Michaelis-Menten, Krebs cycle laws), evolutionary mechanisms
- **Chemistry**: Periodic law, valence bond theory, reaction kinetics laws, Le Chatelier's
  principle, Hess's law, thermochemical laws
- **Computer Science**: Church-Turing thesis, Rice's theorem, CAP theorem, master theorem,
  Shannon's information theorems, fundamental complexity class containments
- **Mathematics**: Core theorems that appear across science (Euler's identity, Bayes'
  theorem, central limit theorem, Gödel incompleteness, Noether's theorem)

**Why this matters**: Each entry should follow the DS schema — entity type, mathematical
archetype, dimensional sensitivity, concept tags, cross-references. This transforms the DS
knowledge base from a DS-specific reference into a universal science anchor layer that
makes cross-domain vector discovery genuinely powerful across all future RRB ingestions.

**Scope estimate**: ~80-120 new entries, following existing DS wiki entry format.
**Prerequisite**: Should inform the RRB test cases — better to expand DS Tier 1/2 first
so the vector reference layer is rich when we run the three test ingestions.

**Deliverables**: New wiki entries (schema-compliant), re-sync to ChromaDB + wiki_history.db,
updated topology metrics. ~1-2 weeks of careful curation.

---

## Key Technical Decisions Made (do not revisit without reason)

1. **SQLite never modified** — all enrichment via INSERT OR IGNORE into existing tables
2. **ChromaDB rebuilt on each sync** — not incremental (fast enough at 1261 chunks)
3. **wiki_history.db append-only** — no deletions ever; embedding history preserved
4. **Embeddings from history DB, not ChromaDB** — HypothesisGenerator reads blobs from
   wiki_history.db (no model loading needed for analysis)
5. **Entry-level centroids** — average chunk embeddings per entry for pairwise analysis
6. **Three-tier link confidence** — 1 (canonical/NULL), 1.5 (discovered), 2 (validated)
7. **Surprise factor threshold 1.15** — calibrated on DS data; adjust per domain
8. **15 controlled archetypes** — fixed vocabulary; do not add new values without careful analysis
9. **Two-pass ingestion design** — deterministic code for standard fields, LLM for ambiguous

---

## Config Reference

```python
# src/config.py
SOURCE_DB  = ~/Library/Mobile Documents/.../ds_wiki.db  # read-only
HISTORY_DB = DS_Wiki_Transformation/data/wiki_history.db
CHROMA_DIR = DS_Wiki_Transformation/data/chroma_db/
CHROMA_COLLECTION = "ds_wiki"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
EMBED_DIM = 384
TOP_K_NEIGHBORS = 5
DRIFT_THRESHOLD = 0.05
TIER_THRESHOLDS = [(0.90, "1"), (0.85, "1.5"), (0.82, "2")]
```

---

## Running the Full Pipeline

```bash
# From DS_Wiki_Transformation/src/
python3 sync.py               # Full rebuild: extract → embed → snapshot → topology

# Run all tests
cd DS_Wiki_Transformation/
python3 -m pytest tests/ -v

# Run diagnostics
cd src/
python3 analysis/coverage_analyzer.py --output markdown > ../coverage_report.md
python3 analysis/hypothesis_generator.py --output markdown --max-pairs 20 > ../hypothesis_report.md
```

---

## Context Window / Session Management

**Claude Code auto-compacts** the conversation when context fills — older messages are
summarised, recent code stays in full. The MEMORY.md file persists across sessions.

**Good practice for this project:**
- Start a new chat thread every 3-4 major phases (keeps active context tight)
- Paste the text "Read MASTER_SUMMARY.md and continue" in the new thread
- Claude Code will read this file and be fully re-oriented within 2 responses
- The MEMORY.md at ~/.claude/projects/... also provides a lighter-weight auto-summary

**MEMORY.md location:**
```
/Users/iandarling/.claude/projects/-Users-iandarling-Projects-DS-Wiki-Transformation/memory/MEMORY.md
```
(This is the auto-memory that Claude Code updates automatically)

---

## Questions Open / Decisions Pending

1. **Next phase priority**: A (LLM instructions) vs B (RO-Crate parser) vs C (remaining diagnostics) vs D (full ingestion)?
2. **Publishing**: When to publish to PyPI? After Phase 3 (usability) or after Phase 2 (ingestion)?
3. **DS framework specifics**: Any remaining DS-specific enrichment before moving to generic toolkit?
4. **Tier 3 links**: 97 "couples to" candidates identified in vector analysis — never inserted. Still relevant?

---

## File Hashes / Version Anchors

**Last confirmed working state:**
```
Git commit: 4744f50  (Option E Chunk 3: Add 15 CS reference_law entries)
Branch: main
Remote: https://github.com/IanD25/ds-wiki-transformer.git
Tests: 139/139 passing (pytest 9.0.2, Python 3.13.12, Apple M4)
ChromaDB snapshot: snap_20260310_090912 (1,562 chunks)
DS wiki entries: 199 total (139 reference_law + 60 DS-native)
DS wiki links: 383 total (167 original + 174 tier-1.5 + 38 Tier 2 + 4 other)
Option E scripts: insert_chunk1_bio_chem.py, insert_chunk2_math_info.py, insert_chunk3_cs.py
```

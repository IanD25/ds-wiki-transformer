# DS Wiki Transformer

Semantic knowledge base for the Dimensional Scaling (DS) 2.x Wiki, expanded with
43 cross-domain reference laws spanning mathematics, CS, biology, chemistry, and
information theory. Exposes 199 entries, 16 conjectures, and 10 gates via a local
MCP server that any capable LLM can connect to.

**No hosting. No LLM backend. No cost beyond your existing Claude subscription.**

---

## Quick Start

```bash
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd DS_Wiki_Transformation
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Edit src/config.py — set SOURCE_DB to your ds_wiki.db path

# First run: downloads ~90MB BGE model, ~10s thereafter
python src/sync.py --trigger "initial"

# Start the MCP server
python src/mcp_server.py
```

Add to your MCP client config:

```json
{
  "mcpServers": {
    "ds-wiki": {
      "command": "/path/to/.venv/bin/python",
      "args": ["/path/to/DS_Wiki_Transformation/src/mcp_server.py"]
    }
  }
}
```

---

## Architecture

```
LAYER 1 — SOURCE OF TRUTH
  ds_wiki.db  (SQLite, read-only for queries, write-only via MCP tools)

LAYER 2 — VECTOR INDEX
  ChromaDB  (current semantic index, rebuilt on each sync)
  wiki_history.db  (append-only embedding snapshots, topology metrics)
  Model: BAAI/bge-small-en-v1.5  (384-dim, local, no API calls)

LAYER 3 — MCP SERVER
  src/mcp_server.py  (19 tools, FastMCP, stdio transport)
```

**Pipeline**: `sync.py` → `extractor.py` (reads ds_wiki.db) → `embedder.py`
(BGE-Small → ChromaDB + wiki_history.db snapshot) → MCP server serves queries.

---

## Data Model

### Entry

The core unit. Every entry has:

| Field | Type | Notes |
|-------|------|-------|
| `id` | TEXT (PK) | e.g. `"OmD"`, `"G1"`, `"Ax2"`, `"M6"`, `"CS1"`, `"BIO3"` |
| `title` | TEXT | Human-readable name |
| `filename` | TEXT | Slug (unused at runtime) |
| `entry_type` | TEXT | See controlled vocabulary below |
| `scale` | TEXT | quantum · molecular · cellular · organismal · population · cosmological · cross-scale |
| `domain` | TEXT | Free-form; common values listed below |
| `status` | TEXT | `established` · `contested` · `conjectured` |
| `confidence` | TEXT | `Tier 1` · `Tier 2` |
| `type_group` | TEXT | Single letter or short code: A B C D E F G H M Q T X Ax OmD |
| `authoring_status` | TEXT | nullable |

**Entry types**: `reference_law` · `law` · `method` · `instantiation` · `open question` ·
`constraint` · `axiom` · `parameter` · `theorem` · `mechanism`

**Common domains**: `physics` · `biology` · `chemistry` · `mathematics` ·
`computer science` · `information` · `earth sciences` · `networks` ·
`computer science · mathematics` · `information · mathematics` · `chemistry · biology`

### Sections

Each entry has multiple named sections (stored in the `sections` table).

**Standard sections for `reference_law` entries** (Option E pattern, 7 per entry):
1. `What It Claims` — plain English statement of the law
2. `Mathematical Form` — equations and formal statement
3. `Constraint Category` — which DS constraint class this law belongs to
4. `DS Cross-References` — which DS entries, conjectures, or gates this law informs
5. `Mathematical Archetype` — which of the 22 structural archetypes applies
6. `What The Math Says` — prose translation of the equations
7. `Concept Tags` — 5–10 semantic anchor phrases

**DS-native entry sections** vary; common ones include:
`What It Claims` · `Formula` · `Where It Applies` · `Why It Matters` ·
`Open Questions` · `References` · `Notes`

### Properties (`entry_properties` table)

Four standard properties on every entry. The `table_name` field groups them:

| table_name | property_name | Example value |
|---|---|---|
| `DS Facets` | `mathematical_archetype` | `conservation-law` |
| `DS Facets` | `dimensional_sensitivity` | `D-sensitive` · `D-invariant` |
| `DS Facets` | `Constraint Category` | `In` (Informatic) |
| `entries` | `concept_tags` | `entropy, information loss, irreversibility` |

**Constraint Category codes**:
- `Ge` — Geometric
- `Th` — Thermodynamic
- `Di` — Dynamical
- `In` — Informatic
- `Co` — Coordination

**Mathematical archetypes** (22 values currently in DB):
`conservation-law` · `thermodynamic-bound` · `equilibrium-condition` · `dimensional-scaling` ·
`statistical-distribution` · `geometric-ratio` · `power-law-scaling` · `gradient-flux-transport` ·
`symmetry-conservation` · `variational-principle` · `coupled-field-equations` ·
`inverse-square-geometric` · `exponential-decay` · `wave-equation` · `diffusion-equation` ·
`threshold-transition` · `sigmoid-saturation` · `linear-proportionality` ·
`logarithmic-growth` · `optimization-principle` · `oscillatory` · `recursive-self-similarity`

### Links

Typed directed relationships between entries (`links` table).

**Link types**:
- `tests` — source provides evidence for/against target
- `implements` — source is the mathematical method used by target
- `generalizes` — target is a special case of source
- `derives from` — source is logically derived from target
- `analogous to` — same mathematical structure, different domain
- `couples to` — source and target share a state variable
- `constrains` — source sets a boundary condition on target
- `predicts for` — source generates a testable claim about target
- `tensions with` — source and target offer competing explanations

**Confidence tiers** (objective — derived from cosine similarity):
- `1` (NULL) — canonical/original (≥ 0.90 or hand-authored)
- `1.5` — strong semantic bond (0.85–0.89)
- `2` — hand-validated explicit link (0.82–0.84)

### Conjectures and Gates

**16 conjectures** (P1–P16): DS-specific theoretical claims awaiting empirical support.
Each has: `conjecture_id`, `title`, `claim`, `gate`, `status`, `evidence`, `priority`.

**10 gates** (G1–G10): validation milestones that gate DS theory development.
Each has: `gate_id`, `title`, `claim`, `priority`, `blocking_entries`, `notes`.

---

## Current Data State

| Metric | Value |
|--------|-------|
| Total entries | 199 (139 reference_law + 60 DS-native) |
| Sections | 1,550 |
| Total links | 383 (167 original + 174 tier-1.5 + 38 tier-2 + 4 other) |
| Property rows | 786 |
| ChromaDB chunks | 1,562 (one per section) |
| Embedding dim | 384 (BGE-Small) |
| Snapshots | 7 (snap_20260309_233846 → snap_20260310_090912) |
| Conjectures | 16 (P1–P16) |
| Gates | 10 (G1–G10) |
| Archetypes | 22 distinct values |
| Top archetype | conservation-law (28 entries) |

**Entry ID prefixes**:
- DS-native: `A`, `B`, `C`, `CM`, `D`, `E`, `F`, `G`, `H`, `M`, `Q`, `T`, `X`, `Ax`, `OmD`, `ES`, `OP`, `TD`, `GV`, `EM`, `QM`, `RD`
- Option E reference laws: `BIO`, `CHEM`, `MATH`, `INFO`, `STAT`, `CS`

---

## MCP Tools — Full Reference

### Search & Retrieval

#### `search_semantic(query, n=5, entry_type=None, domain=None, status=None, type_group=None)`

Natural language vector search. Embeds the query with BGE-Small and returns the
nearest chunks by cosine similarity.

```python
# Returns list of:
{
  "chunk_id":     "G1_What_It_Claims",
  "entry_id":     "G1",
  "section_name": "What It Claims",
  "score":        0.847,          # cosine similarity (0–1, higher = more similar)
  "snippet":      "...",          # first 300 chars of section content
  "metadata":     { ... }         # entry_type, domain, status, type_group, etc.
}
```

Filters are ANDed and use ChromaDB `$eq` matching (exact). Use `search_structured`
for LIKE-style substring matching.

---

#### `search_structured(entry_type=None, scale=None, domain=None, status=None, type_group=None)`

Exact-match SQL filter on the `entries` table. No embeddings involved.
All params optional; returns every entry if none are given.

```python
# Returns list of:
{ "id", "title", "entry_type", "scale", "domain", "status", "confidence", "type_group" }
```

---

#### `get_entry(entry_id)`

Full entry retrieval: metadata + all sections + explicit connections + references + properties.

```python
# Returns:
{
  "entry":       { id, title, entry_type, scale, domain, status, confidence, type_group },
  "sections":    [ { "name": "What It Claims", "content": "..." }, ... ],
  "connections": [ { "link_type", "target_id", "target_label", "description" }, ... ],
  "references":  [ "citation string", ... ],
  "properties":  {
    "DS Facets": [ {"property": "mathematical_archetype", "value": "conservation-law"}, ... ],
    "entries":   [ {"property": "concept_tags", "value": "..."} ]
  }
}
```

---

#### `get_similar(entry_id, n=5)`

Finds entries most semantically similar to a given entry. Averages all chunk
embeddings of the entry into a single centroid vector, then queries ChromaDB.

```python
# Returns list of:
{ "entry_id", "chunk_id", "section_name", "score", "entry_type", "type_group", "status" }
```

Useful for: cross-domain discovery, finding analogues, identifying concept clusters.

---

#### `get_connections(entry_id)`

Returns both explicit (hand-authored) and semantic (vector-derived) connections.

```python
# Returns:
{
  "entry_id":             "G1",
  "explicit_connections": [ { "link_type", "target_id", "target_label", "description" } ],
  "semantic_neighbors":   [ ... ]   # same shape as get_similar output
}
```

---

#### `get_conjectures(gate=None)`

All 16 DS conjectures (P1–P16), optionally filtered by gate ID.

```python
# Returns list of conjecture dicts with all fields.
# Example: get_conjectures(gate="G1") returns conjectures linked to gate G1.
```

---

#### `get_gates()`

All 10 DS validation gates (G1–G10) with claim, priority, and blocking entries.
No parameters.

---

#### `get_all_links()`

Complete typed link graph — all 383 relationships between entries.

```python
# Returns list of:
{ "link_type", "source_id", "source_label", "target_id", "target_label",
  "description", "confidence_tier" }
```

---

### Vector History & Topology

#### `list_snapshots()`

All sync snapshots, newest first. Each snapshot is a full semantic record.

```python
# Returns list of:
{ "snapshot_id", "created_at", "trigger", "chunk_count", "notes" }
# Example snapshot_id: "snap_20260310_090912"
```

---

#### `get_drift_report(snapshot_id=None)`

Semantic change report comparing a snapshot to its predecessor.
Defaults to latest vs previous.

```python
# Returns:
{
  "mean_drift":       0.023,
  "top_drifted":      [ { "chunk_id", "drift" }, ... ],   # 10 most-moved chunks
  "new_chunks":       [ "chunk_id", ... ],
  "changed_chunks":   [ "chunk_id", ... ],
  "converging_pairs": [ { "chunk_a", "chunk_b", "sim_delta" }, ... ],
  "isolated_chunks":  [ { "chunk_id", "centroid_distance" }, ... ]
}
```

---

#### `get_entry_trajectory(entry_id)`

How an entry has moved through semantic space across all snapshots.
Returns per-chunk: centroid distance, top-5 neighbours, drift from previous snapshot.

Useful for: *"Is conjecture P3 converging toward established entries over time?"*

---

#### `get_neighborhood_history(chunk_id)`

How the top-5 nearest neighbours of a chunk have changed across all snapshots.
Includes Jaccard distance measuring stability of the neighbourhood set.

```python
# chunk_id examples: "G1_What_It_Claims", "M6_Formula", "conj_P3", "gate_G1"
```

---

#### `get_isolated_chunks(snapshot_id=None)`

Chunks that sit far from the corpus centroid — semantic outliers.
Threshold: centroid_distance > mean + 2*stdev.

```python
# Returns list of:
{ "chunk_id", "entry_id", "centroid_distance", "z_score" }
```

---

#### `compare_snapshots(snap_a, snap_b)`

Full semantic diff between two snapshots. Shows added/removed chunks and
per-chunk drift for changed content.

---

#### `get_cluster_evolution()`

Per snapshot: top-10 most similar chunk pairs. Reveals stable clusters and
newly forming tight relationships across the history of the knowledge base.

---

### Write Operations

All write operations auto-backup `ds_wiki.db` before modifying it and trigger
a full resync afterward. The DB is never left in a partially-written state.

#### `update_section(entry_id, section_name, new_content)`

Updates one section's content. Validates entry+section exist before writing.

```python
# Returns:
{ "success": True, "snapshot_id": "snap_...", "backup_path": "...", "message": "..." }
# On failure:
{ "success": False, "message": "Section 'X' not found in entry 'Y'. Use get_entry(...)." }
```

---

#### `trigger_sync(notes="")`

Manual full resync after direct DB changes made outside the MCP server.

```python
# Returns:
{ "snapshot_id": "snap_...", "chunk_count": 1562, "message": "..." }
```

---

#### `add_link(source_id, target_id, link_type, description, source_label="", target_label="", confidence_tier="", similarity_score=0.0)`

Add a single typed link to the link graph. Validates `link_type` against the
9-value controlled vocabulary before writing.

`confidence_tier` is resolved in order: explicit `confidence_tier` arg →
auto-computed from `similarity_score` (if > 0) → `None`.

```python
# Returns:
{ "success": True, "link_id": 384, "confidence_tier": "1.5",
  "backup_path": "...", "snapshot_id": "snap_...", "message": "..." }
```

---

#### `add_links_batch(links)`

Add multiple links in one backup + one resync. More efficient than calling
`add_link` repeatedly.

```python
# Each dict in `links` must have: source_id, target_id, link_type, description
# Optionally: source_label, target_label, confidence_tier, similarity_score

# Returns:
{ "success_count": 5, "failed": [], "snapshot_id": "snap_...", "backup_path": "..." }
```

---

## Typical LLM Workflows

**Explore a concept**
```
1. search_semantic("entropy and information loss", n=10)
2. get_entry("INFO1")          # Shannon Entropy
3. get_connections("INFO1")    # explicit + semantic neighbours
4. get_similar("INFO1", n=8)   # find analogues across domains
```

**Cross-domain discovery**
```
1. search_semantic("conservation under symmetry transformation")
2. get_similar("MATH8", n=10)  # Stokes' Theorem — find cross-domain analogues
3. search_structured(entry_type="law", domain="physics")
```

**Check DS theory status**
```
1. get_conjectures()                    # all 16 conjectures
2. get_gates()                          # all 10 validation gates
3. get_entry_trajectory("conj_P3")      # is P3 converging toward established entries?
4. get_connections("G1")               # what blocks gate G1?
```

**Semantic evolution analysis**
```
1. list_snapshots()                           # see sync history
2. get_drift_report()                         # what changed most in last sync?
3. compare_snapshots("snap_A", "snap_B")      # full diff between two states
4. get_cluster_evolution()                    # which pairs have always been close?
```

**Add a new validated link**
```
add_link(
    source_id="CS1",           # Church-Turing Thesis
    target_id="MATH4",         # Gödel Incompleteness
    link_type="analogous to",
    description="Both establish fundamental limits on what formal systems can compute/prove.",
    similarity_score=0.87
)
```

---

## Running the Pipeline

```bash
# Full resync (from project root)
python src/sync.py

# With metadata
python src/sync.py --trigger "add:CS16" --notes "Added CS16 entry"

# Run tests (139 tests, ~0.4s)
python -m pytest tests/ -v

# Run diagnostics
cd src/
python analysis/coverage_analyzer.py --output markdown > ../coverage_report.md
python analysis/hypothesis_generator.py --output markdown --max-pairs 20 > ../hypothesis_report.md
```

---

## Key Files

```
DS_Wiki_Transformation/
├── src/
│   ├── config.py            — paths, model name, tier thresholds, score_to_tier()
│   ├── extractor.py         — ds_wiki.db → 1562 Chunk objects
│   ├── embedder.py          — BGE-Small → ChromaDB + wiki_history.db snapshots
│   ├── topology.py          — read-only queries on embedding history
│   ├── sync.py              — orchestrator: backup → extract → embed → archive
│   ├── mcp_server.py        — 19 MCP tools (FastMCP, stdio)
│   └── analysis/
│       ├── hypothesis_generator.py  — pairwise similarity → surprising pair prompts
│       └── coverage_analyzer.py     — entity/domain/property/network metrics
│
├── scripts/                 — one-time enrichment scripts (all committed, safe to re-run)
│   ├── insert_reference_laws.py     — original 96 reference laws
│   ├── insert_chunk1_bio_chem.py    — Option E: 13 biology + chemistry entries
│   ├── insert_chunk2_math_info.py   — Option E: 15 math + info theory entries
│   ├── insert_chunk3_cs.py          — Option E: 15 CS theory entries
│   ├── add_phase1_taxonomy.py       — mathematical archetypes + D-sensitivity
│   ├── add_phase2_math_prose.py     — "What The Math Says" prose sections
│   ├── add_phase3_concept_tags.py   — concept tag properties + sections
│   └── add_tier2_links.py           — 38 hand-validated explicit links
│
├── tests/
│   ├── test_coverage_analyzer.py    — 56 unit tests (synthetic in-memory SQLite)
│   ├── test_hypothesis_generator.py — 31 unit tests
│   └── test_integration.py          — 52 integration tests (live ds_wiki.db)
│
├── MASTER_SUMMARY.md         — comprehensive re-entry document (read first in new sessions)
├── SPEC.md                   — DS-specific architecture spec
├── GENERIC_TOOLKIT_SPEC.md   — domain-agnostic toolkit architecture (1,083 lines)
└── IMPLEMENTATION_ROADMAP.md — Phase 1–4 implementation plan
```

---

## Requirements

- Python 3.11+
- `ds_wiki.db` — DS wiki SQLite database
- ~200MB disk (BGE model ~90MB + ChromaDB)
- Apple Silicon (MPS) or CPU; no GPU required

```
sentence-transformers>=3.0.0
chromadb>=0.5.0
fastmcp>=2.0.0
numpy>=2.0.0
```

# DS Wiki Transformer — Specification v2.0

**Project Owner:** Ian Darling (Finglas Media)
**Date:** March 9, 2026
**Status:** Approved for Implementation
**Executing Agent:** Claude (Opus 4.6)

---

## 0. Purpose & Design Philosophy

Transform the DS 2.x Wiki (SQLite source) into a live, semantically-indexed knowledge base
that any capable LLM (Claude, Copilot, Cursor, etc.) can connect to via MCP, query with
natural language, and help update — while maintaining a complete, immutable historical
record of how the semantic landscape of the knowledge has evolved over time.

**Core principles:**
- The original `ds_wiki.db` is the source of truth. It is never deleted, never schema-altered.
- Every write operation is preceded by a timestamped backup.
- All history is additive. Nothing is ever overwritten or removed.
- The LLM backend is Claude (or whichever model connects). No local LLM is run.
- Cost: $0 infrastructure. Everything runs locally on the M4 Mac.

---

## 1. What Gets Built

```
Five deliverables:

1. src/config.py              — Paths, constants, shared settings
2. src/extractor.py           — Reads ds_wiki.db → structured chunk list
3. src/embedder.py            — Embeds chunks → ChromaDB + records history
4. src/topology.py            — Computes & queries vector history metrics
5. src/mcp_server.py          — MCP server: exposes all tools to Claude
6. src/sync.py                — Orchestrator: runs extract → embed → archive
7. wiki_history.db            — New SQLite DB for snapshots + embedding history
8. chroma_db/                 — Persistent ChromaDB (current semantic index)
9. backups/                   — Timestamped copies of ds_wiki.db (pre-write)
```

---

## 2. Architecture

```
ds_wiki.db  (SOURCE OF TRUTH — read/write, never schema-altered)
     │
     │  src/extractor.py
     ▼
chunks: List[Chunk]           (in memory, not persisted as JSON)
     │
     │  src/embedder.py  (BGE-Small-EN-v1.5, 384-dim, via sentence-transformers)
     ├──────────────────────────────────────────────┐
     ▼                                              ▼
chroma_db/                              wiki_history.db
(current semantic index,                (immutable history:
 rebuilt on each sync)                   snapshots + embedding
                                         vectors + topology metrics)
     │                    │
     └────────────────────┘
                 │
          src/mcp_server.py
                 │
         ┌───────┴────────┐
    Claude Code       Any MCP-capable LLM
    (local)           (via GitHub repo + local run)
```

---

## 3. File & Directory Structure

```
DS_Wiki_Transformation/
├── SPEC.md                          ← this file
├── requirements.txt
├── .env.example                     ← DB_PATH and other config vars
├── src/
│   ├── config.py
│   ├── extractor.py
│   ├── embedder.py
│   ├── topology.py
│   ├── mcp_server.py
│   └── sync.py
├── data/
│   ├── chroma_db/                   ← ChromaDB persistent store
│   └── wiki_history.db              ← history database (created on first sync)
├── backups/
│   └── backup_YYYYMMDD_HHMMSS/
│       └── ds_wiki.db               ← copy of source before each write
└── README.md
```

**Source DB location (iCloud, do not move):**
```
/Users/iandarling/Library/Mobile Documents/com~apple~CloudDocs/
  Primary Work Outputs/wiki build/ds-wiki-repo/ds_wiki.db
```

---

## 4. Data Models

### 4.1 Chunk (in-memory, not persisted as JSON)

Every embeddable unit of wiki content is a Chunk:

```python
@dataclass
class Chunk:
    chunk_id: str        # unique: e.g. "A1_Formula", "conj_P3", "gate_G1"
    entry_id: str        # parent entry ID or "conj", "gate", "bridge"
    chunk_type: str      # "section" | "conjecture" | "gate" | "bridge"
    title: str           # entry title (for context in embedding)
    section_name: str    # section name or chunk subtype
    embed_text: str      # the text actually sent to the embedding model
    metadata: dict       # stored in ChromaDB alongside the vector
```

**`embed_text` construction by chunk_type:**

| Type | embed_text |
|------|-----------|
| `section` | `"{title}\n[{section_name}]\n{content}"` |
| `conjecture` | `"Conjecture {id}: {title}\nClaim: {claim}\nWould confirm: {would_confirm}\nWould kill: {would_kill}\nCritical gaps: {critical_gaps}"` |
| `gate` | `"Gate {id}\nClaim: {claim}\nPriority: {priority}\nBlocking: {blocking}"` |
| `bridge` | `"[Bridge: {section_name}]\n{content}"` |

**`metadata` fields stored in ChromaDB:**

| Field | Source | Notes |
|---|---|---|
| `entry_id` | entries.id | |
| `chunk_type` | derived | |
| `section_name` | sections.section_name | |
| `entry_type` | entries.entry_type | theorem, law, constraint, etc. |
| `scale` | entries.scale | |
| `domain` | entries.domain | |
| `status` | entries.status | established / contested / conjectured |
| `confidence` | entries.confidence | Tier 1 / Tier 2 † / Tier 3 ‡_p |
| `type_group` | entries.type_group | A, B, C, …, H, Q, X |

### 4.2 wiki_history.db Schema (new, separate from ds_wiki.db)

Three tables, all append-only:

```sql
CREATE TABLE wiki_snapshots (
    snapshot_id   TEXT PRIMARY KEY,   -- 'snap_20260309_143022'
    created_at    TEXT NOT NULL,       -- ISO 8601 UTC
    trigger       TEXT NOT NULL,       -- 'initial' | 'manual' | 'update:A1' | 'add:H6'
    chunk_count   INTEGER NOT NULL,    -- number of chunks embedded
    notes         TEXT                 -- optional human note
);

CREATE TABLE chunk_embedding_history (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id         TEXT NOT NULL REFERENCES wiki_snapshots(snapshot_id),
    chunk_id            TEXT NOT NULL,   -- e.g. 'A1_Formula'
    entry_id            TEXT NOT NULL,
    content_hash        TEXT NOT NULL,   -- SHA256(embed_text) — change detection
    embedding           BLOB NOT NULL,   -- numpy float32 array as raw bytes
    top5_neighbors      TEXT NOT NULL,   -- JSON: [{"id": "M6_Key_Connections", "score": 0.91}, ...]
    centroid_distance   REAL NOT NULL,   -- cosine distance from corpus centroid
    UNIQUE(snapshot_id, chunk_id)
);

CREATE TABLE topology_metrics (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id    TEXT NOT NULL REFERENCES wiki_snapshots(snapshot_id),
    metric_name    TEXT NOT NULL,
    metric_value   TEXT NOT NULL,   -- JSON-encoded value
    UNIQUE(snapshot_id, metric_name)
);

CREATE INDEX idx_ceh_entry    ON chunk_embedding_history(entry_id);
CREATE INDEX idx_ceh_snapshot ON chunk_embedding_history(snapshot_id);
CREATE INDEX idx_ceh_chunk    ON chunk_embedding_history(chunk_id);
```

**Topology metrics stored per snapshot:**

| metric_name | metric_value | Description |
|---|---|---|
| `corpus_centroid` | `[f32, f32, ...]` 384-dim JSON array | Mean embedding of all chunks |
| `chunk_count` | integer | Total chunks in snapshot |
| `mean_centroid_distance` | float | Average distance of all chunks from centroid |
| `max_drift_chunk` | `{"chunk_id": ..., "drift": float}` | Chunk that moved most vs previous snapshot |
| `mean_drift` | float | Mean cosine drift across all chunks vs previous |
| `new_chunks` | `["chunk_id", ...]` | Chunks present in this snapshot but not previous |
| `changed_chunks` | `["chunk_id", ...]` | Chunks where content_hash changed |
| `neighborhood_instability` | `{"chunk_id": jaccard_distance, ...}` | Top 10 most-changed neighborhoods |
| `isolated_chunks` | `["chunk_id", ...]` | Chunks with centroid_distance > mean + 2*stdev |
| `converging_pairs` | `[{"a": id, "b": id, "delta": float}, ...]` | Top 5 pairs that moved closer |

---

## 5. Script Specifications

### 5.1 `src/config.py`

Single source of configuration. All other scripts import from here.

```python
# All paths, model names, constants
SOURCE_DB   = Path("~/Library/Mobile Documents/com~apple~CloudDocs/
                    Primary Work Outputs/wiki build/ds-wiki-repo/ds_wiki.db").expanduser()
PROJECT_DIR = Path("~/Projects/DS_Wiki_Transformation").expanduser()
HISTORY_DB  = PROJECT_DIR / "data" / "wiki_history.db"
CHROMA_DIR  = PROJECT_DIR / "data" / "chroma_db"
BACKUP_DIR  = PROJECT_DIR / "backups"

EMBED_MODEL      = "BAAI/bge-small-en-v1.5"
EMBED_DIM        = 384
CHROMA_COLLECTION = "ds_wiki"
TOP_K_NEIGHBORS  = 5     # stored in history per chunk
DEFAULT_SEARCH_K = 5     # default n_results for semantic search
DRIFT_THRESHOLD  = 0.05  # cosine distance — flag as "changed" if above this
```

### 5.2 `src/extractor.py`

**Function:** `extract_chunks(db_path: Path) -> list[Chunk]`

**Logic:**
1. Connect to `ds_wiki.db` (read-only).
2. For each entry in `entries`: query its `sections`, build one Chunk per section.
   - `chunk_id` = `f"{entry_id}_{section_name.replace(' ', '_').replace('/', '_')}"`
   - `embed_text` = `f"{title}\n[{section_name}]\n{content}"`
   - `metadata` = all entry facets + section_name + chunk_type="section"
3. For each row in `conjectures`: build one Chunk.
   - `chunk_id` = `f"conj_{id}"`
   - `embed_text` = constructed from claim + would_confirm + would_kill + critical_gaps
4. For each row in `gates`: build one Chunk.
   - `chunk_id` = `f"gate_{id}"`
5. For each row in `bridge_content`: build one Chunk.
   - `chunk_id` = `f"bridge_{section_name.replace(' ', '_')}"`
6. Return full list. Log count by type.

**No writes. Pure read.**

### 5.3 `src/embedder.py`

**Function:** `embed_and_store(chunks: list[Chunk], trigger: str, notes: str = "") -> str`

Returns `snapshot_id`.

**Logic:**
1. Load `SentenceTransformer(EMBED_MODEL)` — downloads on first run, cached after.
2. Extract `embed_texts = [c.embed_text for c in chunks]`.
3. Call `model.encode(embed_texts, batch_size=32, show_progress_bar=True, normalize_embeddings=True)`.
   - `normalize_embeddings=True` means all vectors are unit-length → cosine similarity = dot product.
4. **ChromaDB update:**
   - Open/create persistent ChromaDB client at `CHROMA_DIR`.
   - Delete and recreate collection `CHROMA_COLLECTION` (full rebuild on each sync).
   - Add all chunks: `collection.add(ids, embeddings, documents, metadatas)`.
5. **History write:**
   - Compute corpus centroid: `np.mean(embeddings, axis=0)` (already normalized — re-normalize).
   - For each chunk, compute `top5_neighbors` (cosine similarity, exclude self) and `centroid_distance`.
   - Generate `snapshot_id = f"snap_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"`.
   - Insert into `wiki_snapshots`.
   - Insert all rows into `chunk_embedding_history`.
   - Compute and insert all topology metrics into `topology_metrics`.
6. Return `snapshot_id`.

**Topology metric computation:**
- Load previous snapshot (most recent before current) from `wiki_history.db`.
- For each chunk in current snapshot:
  - If chunk existed in previous: drift = `1 - cosine_sim(current_embedding, previous_embedding)`.
  - If chunk is new: mark as new_chunk.
  - Neighborhood instability = Jaccard distance between top-5 neighbor sets.
- Aggregate: mean_drift, max_drift, converging_pairs (pairs where drift was negative = moved closer).

### 5.4 `src/topology.py`

**Query functions (read-only, used by MCP server):**

```python
def get_entry_trajectory(entry_id: str) -> list[dict]
    """
    Returns ordered list of snapshots with:
    - snapshot_id, created_at, trigger
    - chunks belonging to this entry in that snapshot
    - per-chunk: centroid_distance, top5_neighbors, content_hash
    - per-chunk vs previous: drift, neighborhood_change (jaccard)
    Shows how an entry has moved through semantic space over time.
    """

def get_semantic_drift_report(snapshot_id: str = None) -> dict
    """
    For a given snapshot (default: latest vs previous):
    - mean_drift across all chunks
    - top 10 most-drifted chunks with delta and direction
    - new chunks added
    - changed chunks (content_hash differs)
    - top 5 converging pairs
    """

def get_neighborhood_history(chunk_id: str) -> list[dict]
    """
    For a specific chunk, returns its top-5 neighbors at each snapshot.
    Reveals which entries have become more/less related over time.
    """

def get_isolated_chunks(snapshot_id: str = None) -> list[dict]
    """
    Returns chunks that sit far from the corpus centroid.
    These are the most "unique" or "isolated" ideas in the wiki.
    """

def get_cluster_evolution() -> list[dict]
    """
    For each snapshot, returns the top-5 neighbor pairs by similarity.
    Shows which pairs of ideas have consistently been close,
    and whether any new tight clusters have formed.
    """

def compare_snapshots(snap_a: str, snap_b: str) -> dict
    """
    Full diff between two snapshots:
    - Added chunks, removed chunks, changed chunks
    - Per-chunk drift
    - Topology metric deltas
    """

def list_snapshots() -> list[dict]
    """
    Returns all snapshots with id, created_at, trigger, chunk_count, notes.
    """
```

### 5.5 `src/sync.py`

**Orchestrator. Run this to perform a full sync.**

```python
def sync(trigger: str = "manual", notes: str = ""):
    """
    1. Backup ds_wiki.db to backups/backup_YYYYMMDD_HHMMSS/
    2. extract_chunks() from source DB
    3. embed_and_store(chunks, trigger, notes)
    4. Print summary: snapshot_id, chunk count, drift stats vs previous
    """

def sync_after_update(entry_id: str):
    """Convenience wrapper: sync(trigger=f'update:{entry_id}')"""

def sync_after_add(entry_id: str):
    """Convenience wrapper: sync(trigger=f'add:{entry_id}')"""
```

**CLI usage:**
```bash
python src/sync.py                      # manual full sync
python src/sync.py --trigger "add:H6"  # after adding an entry
```

### 5.6 `src/mcp_server.py`

Built with `fastmcp`. Exposes all tools to Claude (or any MCP client).

**Run:**
```bash
python src/mcp_server.py
# or via Claude Code: add to .claude/mcp_servers.json
```

---

## 6. MCP Tool Definitions

All tools are read-only except `update_section` and `trigger_sync`.

### 6.1 Search & Retrieval

```
search_semantic(query: str, n: int = 5, filter_type: str = None,
                filter_domain: str = None, filter_status: str = None)
→ list of {chunk_id, entry_id, title, section_name, content_snippet, score, metadata}

Semantic search across all chunks using ChromaDB.
Supports optional metadata filters (applied before vector search).
```

```
search_structured(entry_type: str = None, scale: str = None,
                  domain: str = None, status: str = None,
                  type_group: str = None)
→ list of matching entries with all facets

Exact-match filter query on SQLite entries table. No embedding involved.
```

```
get_entry(entry_id: str)
→ {entry metadata, sections: [{name, content}], connections: [...], references: [...], properties: [...]}

Full entry retrieval from SQLite.
```

```
get_similar(entry_id: str, n: int = 5)
→ list of {chunk_id, score, entry_id, title, section_name}

Find semantically similar chunks to all chunks of a given entry.
Aggregates scores across all chunks of the entry, returns top n unique entries.
```

```
get_connections(entry_id: str)
→ {explicit: [{link_type, target_id, target_label, description}],
   semantic_neighbors: [{entry_id, title, score}]}

Returns both explicit (from SQLite entry_connections) and
semantic (top-5 from ChromaDB) connections for an entry.
```

```
get_conjectures(gate: str = None)
→ list of conjecture records, optionally filtered by gate

Returns all P1-P16 with full fields. Gate filter e.g. "G1".
```

```
get_gates()
→ list of gate records with blocking entries
```

```
get_all_links()
→ full link graph from SQLite links table
```

### 6.2 History & Topology

```
get_entry_trajectory(entry_id: str)
→ list of {snapshot_id, created_at, trigger, chunks: [{chunk_id, centroid_distance,
           drift_from_previous, top5_neighbors, neighborhood_change}]}

Shows how an entry has moved through semantic space across all snapshots.
```

```
get_drift_report(snapshot_id: str = None)
→ {snapshot_id, created_at, mean_drift, top_drifted: [...],
   new_chunks: [...], changed_chunks: [...], converging_pairs: [...]}

Semantic change report. Defaults to latest vs previous snapshot.
```

```
get_neighborhood_history(chunk_id: str)
→ list of {snapshot_id, created_at, top5_neighbors, jaccard_change_from_previous}

How the nearest neighbors of a specific chunk have changed over time.
```

```
get_isolated_chunks(snapshot_id: str = None)
→ list of {chunk_id, entry_id, centroid_distance, z_score}

Chunks that are semantic outliers — furthest from the corpus centroid.
```

```
list_snapshots()
→ list of {snapshot_id, created_at, trigger, chunk_count, notes}
```

```
compare_snapshots(snap_a: str, snap_b: str)
→ {added, removed, changed, topology_deltas}
```

```
get_cluster_evolution()
→ Per snapshot: top-10 most similar chunk pairs. Shows stable vs shifting clusters.
```

### 6.3 Write Operations

```
update_section(entry_id: str, section_name: str, new_content: str)
→ {success: bool, backup_path: str, message: str}

1. Backs up ds_wiki.db to backups/backup_YYYYMMDD_HHMMSS/
2. Updates sections table in ds_wiki.db
3. Calls sync_after_update(entry_id) — reruns full embed cycle
4. Returns snapshot_id of new snapshot
```

```
trigger_sync(notes: str = "")
→ {snapshot_id: str, chunk_count: int, drift_summary: str}

Manually trigger a full resync (extract → embed → history record).
Use after making changes directly to ds_wiki.db.
```

---

## 7. Dependencies

```txt
# requirements.txt
sentence-transformers>=3.0.0
chromadb>=0.5.0
fastmcp>=2.0.0
numpy>=2.0.0
```

**sqlite3** — built into Python standard library, no install needed.

**Note on Python 3.13:** All packages above support Python 3.13 as of March 2026.
Use a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Embedding model download:** BGE-Small-EN-v1.5 downloads automatically on first
`embed_and_store()` run (~90MB, cached to `~/.cache/huggingface/`).

**Apple Silicon (M4) note:** `sentence-transformers` automatically uses MPS acceleration.
Full resync of 57 entries (~400 chunks) takes approximately 3–5 seconds.

---

## 8. Claude Code MCP Configuration

After running `src/mcp_server.py`, add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "ds-wiki": {
      "command": "python",
      "args": ["/Users/iandarling/Projects/DS_Wiki_Transformation/src/mcp_server.py"],
      "env": {}
    }
  }
}
```

Any other developer can clone the GitHub repo, run `pip install -r requirements.txt`,
point `SOURCE_DB` at their copy of `ds_wiki.db`, run `python src/sync.py`, and connect
the same MCP server to their own Claude Code instance.

---

## 9. Backup Policy

- Every `update_section()` call creates a backup **before** any write.
- `trigger_sync()` does NOT create a backup (read-only operation).
- Backups are full copies of `ds_wiki.db` only (ChromaDB is regenerable, history DB is append-only).
- Backup directory: `backups/backup_YYYYMMDD_HHMMSS/ds_wiki.db`
- Backups are never automatically deleted.

---

## 10. Execution Order

```
Step 1:  Create virtual environment + install requirements
Step 2:  Run src/sync.py (initial sync)
         → Creates data/wiki_history.db
         → Creates data/chroma_db/
         → Creates backups/backup_initial/
         → Records first snapshot snap_YYYYMMDD_HHMMSS
Step 3:  Verify: python src/topology.py --report (prints drift report)
Step 4:  Start MCP server: python src/mcp_server.py
Step 5:  Add MCP server to Claude Code settings
Step 6:  Test: ask Claude to search_semantic("emergent threshold behavior")
Step 7:  Commit repo to GitHub (excluding data/ and backups/ — add to .gitignore)
```

---

## 11. Error Handling

| Scenario | Handling |
|---|---|
| `ds_wiki.db` not accessible (iCloud sync delay) | Raise `SourceDBError` with path; do not proceed |
| ChromaDB collection missing | Recreate on next sync |
| Embedding model not cached | Downloads automatically; log progress |
| `update_section` — entry_id not found | Raise `ValueError` before any backup or write |
| History DB schema missing | Auto-created with `CREATE TABLE IF NOT EXISTS` on first use |
| Previous snapshot missing (first run) | Skip drift computation; store zeros for drift metrics |

---

## 12. What This Enables

**For the researcher (Ian):**
- Ask Claude: *"What entries are semantically close to G1 but not explicitly linked?"*
- Ask Claude: *"Show me how M6's semantic neighborhood has changed over the last 3 syncs."*
- Ask Claude: *"Which ideas are semantic outliers — things that don't cluster with anything?"*
- Ask Claude: *"Update entry A1's Formula section with this new derivation."* → auto-backup + auto-resync
- Ask Claude: *"What changed semantically when I added the H-series entries?"*

**For any connected LLM:**
- Full structured access to the DS wiki via MCP tools
- Semantic search over all 57 entries + conjectures + gates
- Read the full semantic history and topology evolution
- Write updates back to the source DB

**Vector history topology answers questions like:**
- "Which conjectures are drifting toward established entries?" (P-series convergence to A/B/C)
- "Are the H-series entries forming their own cluster or integrating with existing ones?"
- "Which entry has been most semantically stable since the wiki began?"
- "What was the semantic impact of adding the X-series instantiations?"

---

## 13. Out of Scope (v2.0)

- UMAP/t-SNE 2D visualization of vector trajectories (future: `src/visualize.py`)
- Scheduled automatic syncs (future: cron or launchd)
- Re-ranking with cross-encoder (future optimization)
- Sentence-aware chunking with overlap (current: section = chunk, natural unit for this DB)
- Public web interface (current: MCP + Claude Code CLI only)

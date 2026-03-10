# DS Wiki Transformer

Semantic knowledge base for the Dimensional Scaling (DS) 2.x Wiki.
Exposes 199 entries (139 reference_law + 60 DS-native), 16 conjectures, and 10 gates
via an MCP server that any capable LLM (Claude Code, Cursor, Copilot) can connect to locally.

**No hosting. No LLM backend. No cost beyond your existing Claude subscription.**

---

## What It Does

- **Semantic search** across all wiki content using BGE-Small embeddings (384-dim)
- **Structured queries** by entry type, scale, domain, status, or type group
- **Explicit graph** — typed connections between entries
- **Vector history** — every sync records a full semantic snapshot so you can
  track how ideas drift, cluster, and converge over time
- **Write-back** — update wiki sections through Claude; auto-backup + auto-resync

---

## Quick Start

```bash
# 1. Clone and set up
git clone <repo-url>
cd DS_Wiki_Transformation
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Point to your ds_wiki.db — edit src/config.py SOURCE_DB path

# 3. Run initial sync (downloads ~90MB model on first run, ~10s after)
python src/sync.py --trigger "initial"

# 4. Start the MCP server
python src/mcp_server.py
```

Then add to your MCP client config (Claude Code example):

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
ds_wiki.db  (source of truth — read/write, never schema-altered)
     │
     ├── src/extractor.py   →  1,562 chunks (sections, conjectures, gates, bridge)
     ├── src/embedder.py    →  ChromaDB (current index) + wiki_history.db (snapshots)
     ├── src/topology.py    →  semantic drift, trajectory, cluster evolution queries
     ├── src/sync.py        →  orchestrator (backup → extract → embed → archive)
     └── src/mcp_server.py  →  17 MCP tools exposed to any connected LLM
```

---

## MCP Tools

### Search & Retrieval
| Tool | Description |
|---|---|
| `search_semantic` | Natural language search, optional facet filters |
| `search_structured` | Exact-match filter by type/scale/domain/status |
| `get_entry` | Full entry — sections, connections, references, properties |
| `get_similar` | Semantically similar entries (vector-derived) |
| `get_connections` | Explicit graph + semantic neighbours for an entry |
| `get_conjectures` | All P1–P16, optionally filtered by gate |
| `get_gates` | All G1–G10 with priority and blocking |
| `get_all_links` | Full typed link graph |

### Vector History & Topology
| Tool | Description |
|---|---|
| `list_snapshots` | All sync snapshots with metadata |
| `get_drift_report` | Semantic change report between snapshots |
| `get_entry_trajectory` | How an entry has moved through semantic space over time |
| `get_neighborhood_history` | How a chunk's nearest neighbours have changed |
| `get_isolated_chunks` | Semantic outliers far from the corpus centroid |
| `compare_snapshots` | Full diff between two snapshots |
| `get_cluster_evolution` | Most similar chunk pairs per snapshot |

### Write Operations
| Tool | Description |
|---|---|
| `update_section` | Update a section — auto-backup + auto-resync |
| `trigger_sync` | Manual full resync after direct DB changes |

---

## Vector History

Every `sync` call records:
- Full embedding vector for each chunk (stored in `wiki_history.db`)
- Top-5 semantic neighbours per chunk
- Centroid distance per chunk
- Topology metrics: mean drift, converging pairs, isolated chunks, cluster top-pairs

This lets you ask questions like:
- *"Which conjectures are drifting toward established entries?"*
- *"What was the semantic impact of adding the H-series?"*
- *"Which ideas have been most semantically stable?"*
- *"Show G1's trajectory through semantic space across all syncs."*

---

## Resync After Updates

```bash
# After editing ds_wiki.db directly:
python src/sync.py --trigger "add:H6" --notes "Added H6 entry"

# Or through Claude via the MCP tool:
# trigger_sync(notes="Added H6 entry")
# update_section("G1", "What It Claims", "new content...")
```

---

## Requirements

- Python 3.11+
- Apple Silicon (MPS acceleration) or CPU
- `ds_wiki.db` — your DS wiki SQLite database
- ~200MB disk for models + ChromaDB

## Dependencies

```
sentence-transformers>=3.0.0
chromadb>=0.5.0
fastmcp>=2.0.0
numpy>=2.0.0
```

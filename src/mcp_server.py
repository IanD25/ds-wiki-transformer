"""
mcp_server.py — MCP server exposing the DS Wiki knowledge base to Claude (or any
MCP-capable LLM). Run via: python src/mcp_server.py

All query embeddings use BGE-Small-EN-v1.5 (same model as the stored vectors)
for consistent semantic similarity scores.
"""
import json
import sqlite3
import sys
from pathlib import Path

import chromadb
import numpy as np
from fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

# Ensure src/ is importable regardless of cwd
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import (
    CHROMA_COLLECTION, CHROMA_DIR, DEFAULT_SEARCH_K,
    EMBED_MODEL, HISTORY_DB, SOURCE_DB, score_to_tier,
)
import topology as topo

# ── Singletons (lazy-loaded on first tool call) ───────────────────────────────
_model:      SentenceTransformer | None = None
_collection: chromadb.Collection  | None = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def _get_collection() -> chromadb.Collection:
    global _collection
    if _collection is None:
        client      = chromadb.PersistentClient(path=str(CHROMA_DIR))
        _collection = client.get_collection(CHROMA_COLLECTION)
    return _collection


def _source_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{SOURCE_DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def _embed_query(text: str) -> list[float]:
    """Embed a query string with BGE-Small (same space as stored vectors)."""
    vec = _get_model().encode([text], normalize_embeddings=True)[0]
    return vec.tolist()


def _build_where(
    entry_type:  str | None,
    domain:      str | None,
    status:      str | None,
    type_group:  str | None,
) -> dict | None:
    """Build a ChromaDB metadata filter dict from optional facet filters."""
    clauses = []
    if entry_type: clauses.append({"entry_type":  {"$eq": entry_type}})
    if domain:     clauses.append({"domain":      {"$eq": domain}})
    if status:     clauses.append({"status":      {"$eq": status}})
    if type_group: clauses.append({"type_group":  {"$eq": type_group}})
    if not clauses:
        return None
    return {"$and": clauses} if len(clauses) > 1 else clauses[0]


# ── MCP Server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    "DS Wiki",
    instructions=(
        "Semantic knowledge base for the Dimensional Scaling (DS) 2.x Wiki. "
        "57 entries across theorems, laws, constraints, methods, axioms, open questions, "
        "and instantiations. 16 conjectures (P1-P16), 10 gates (G1-G10). "
        "Use search_semantic for concept queries, get_entry for full content, "
        "get_connections to explore the idea graph, and the trajectory/drift tools "
        "to understand how the knowledge base has evolved semantically over time."
    ),
)


# ══════════════════════════════════════════════════════════════════════════════
# SEARCH & RETRIEVAL
# ══════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def search_semantic(
    query: str,
    n: int = DEFAULT_SEARCH_K,
    entry_type:  str | None = None,
    domain:      str | None = None,
    status:      str | None = None,
    type_group:  str | None = None,
) -> list[dict]:
    """
    Semantic search across all wiki chunks using BGE-Small embeddings.

    Args:
        query:      Natural language query (e.g. "emergent threshold behavior")
        n:          Number of results to return (default 5)
        entry_type: Filter by type — theorem | law | constraint | mechanism |
                    parameter | axiom | method | open question | instantiation
        domain:     Filter by domain — geometry | biology | cosmology | networks |
                    physics | information
        status:     Filter by status — established | contested | conjectured
        type_group: Filter by group letter — A | B | C | D | E | F | G | H |
                    M | Q | T | X | Ax | OmD

    Returns list of {chunk_id, entry_id, title, section_name, score, snippet, metadata}.
    """
    query_emb = _embed_query(query)
    where     = _build_where(entry_type, domain, status, type_group)

    kwargs: dict = dict(query_embeddings=[query_emb], n_results=min(n, 50))
    if where:
        kwargs["where"] = where

    res = _get_collection().query(**kwargs, include=["documents", "metadatas", "distances"])

    results = []
    for cid, doc, meta, dist in zip(
        res["ids"][0], res["documents"][0],
        res["metadatas"][0], res["distances"][0],
    ):
        results.append({
            "chunk_id":    cid,
            "entry_id":    meta.get("entry_id", ""),
            "section_name": meta.get("section_name", ""),
            "score":       round(1.0 - float(dist), 3),
            "snippet":     doc[:300].strip(),
            "metadata":    meta,
        })
    return results


@mcp.tool()
def search_structured(
    entry_type:  str | None = None,
    scale:       str | None = None,
    domain:      str | None = None,
    status:      str | None = None,
    type_group:  str | None = None,
) -> list[dict]:
    """
    Exact-match filter query on the entries table. No embeddings involved.
    All parameters are optional — combine freely to filter the wiki.

    Args:
        entry_type:  theorem | law | constraint | mechanism | parameter |
                     axiom | method | open question | instantiation
        scale:       quantum | molecular | cellular | organismal | population |
                     cosmological | cross-scale
        domain:      geometry | biology | cosmology | networks | physics | information
        status:      established | contested | conjectured
        type_group:  A | B | C | D | E | F | G | H | M | Q | T | X | Ax | OmD

    Returns list of matching entries with all facets.
    """
    clauses, params = [], []
    for col, val in [
        ("entry_type", entry_type), ("scale", scale),
        ("domain", domain), ("status", status), ("type_group", type_group),
    ]:
        if val:
            clauses.append(f"LOWER({col}) LIKE LOWER(?)")
            params.append(f"%{val}%")

    where_sql = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    conn = _source_conn()
    rows = conn.execute(
        f"SELECT id, title, entry_type, scale, domain, status, confidence, type_group "
        f"FROM entries {where_sql} ORDER BY id",
        params,
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@mcp.tool()
def get_entry(entry_id: str) -> dict:
    """
    Full entry retrieval — metadata, all sections, connections, references,
    and property tables.

    Args:
        entry_id: Entry ID e.g. "A1", "G1", "Ax2", "OmD", "M6"
    """
    conn = _source_conn()

    entry = conn.execute(
        "SELECT * FROM entries WHERE id = ?", (entry_id,)
    ).fetchone()
    if not entry:
        conn.close()
        return {"error": f"Entry '{entry_id}' not found."}

    sections = conn.execute(
        "SELECT section_name, content FROM sections "
        "WHERE entry_id = ? ORDER BY section_order",
        (entry_id,),
    ).fetchall()

    connections = conn.execute(
        "SELECT link_type, target_id, target_label, description "
        "FROM entry_connections WHERE entry_id = ? ORDER BY connection_order",
        (entry_id,),
    ).fetchall()

    references = conn.execute(
        "SELECT citation FROM references_ WHERE entry_id = ? ORDER BY ref_order",
        (entry_id,),
    ).fetchall()

    properties = conn.execute(
        "SELECT table_name, property_name, property_value "
        "FROM entry_properties WHERE entry_id = ? ORDER BY prop_order",
        (entry_id,),
    ).fetchall()

    conn.close()

    # Group properties by table_name
    prop_tables: dict[str, list] = {}
    for p in properties:
        prop_tables.setdefault(p["table_name"], []).append({
            "property": p["property_name"],
            "value":    p["property_value"],
        })

    return {
        "entry":       dict(entry),
        "sections":    [{"name": s["section_name"], "content": s["content"]} for s in sections],
        "connections": [dict(c) for c in connections],
        "references":  [r["citation"] for r in references],
        "properties":  prop_tables,
    }


@mcp.tool()
def get_similar(entry_id: str, n: int = DEFAULT_SEARCH_K) -> list[dict]:
    """
    Find semantically similar entries to a given entry.
    Aggregates similarity scores across all chunks of the entry,
    returns top-n unique entries (excluding the query entry itself).

    Args:
        entry_id: e.g. "G1", "M6", "conj_P3", "gate_G1"
        n:        Number of similar entries to return (default 5)
    """
    col = _get_collection()

    # Get all chunks for this entry
    results = col.get(where={"entry_id": {"$eq": entry_id}}, include=["embeddings"])
    if not results["ids"]:
        return [{"error": f"No chunks found for entry '{entry_id}'"}]

    # Average the entry's chunk embeddings → single representative vector
    embs   = np.array(results["embeddings"], dtype=np.float32)
    avg    = embs.mean(axis=0)
    norm   = np.linalg.norm(avg)
    if norm > 0:
        avg /= norm

    res = col.query(
        query_embeddings=[avg.tolist()],
        n_results=min(n * 6, 100),   # over-fetch to allow dedup by entry
        include=["metadatas", "distances"],
    )

    seen:    set[str]  = {entry_id}
    entries: list[dict] = []
    for cid, meta, dist in zip(
        res["ids"][0], res["metadatas"][0], res["distances"][0]
    ):
        eid = meta.get("entry_id", "")
        if eid in seen:
            continue
        seen.add(eid)
        entries.append({
            "entry_id":    eid,
            "chunk_id":    cid,
            "section_name": meta.get("section_name", ""),
            "score":       round(1.0 - float(dist), 3),
            "entry_type":  meta.get("entry_type", ""),
            "type_group":  meta.get("type_group", ""),
            "status":      meta.get("status", ""),
        })
        if len(entries) >= n:
            break
    return entries


@mcp.tool()
def get_connections(entry_id: str) -> dict:
    """
    Returns both explicit (hand-authored) and semantic (vector-derived)
    connections for an entry.

    Args:
        entry_id: e.g. "A1", "G1", "M6"
    """
    conn = _source_conn()
    explicit = conn.execute(
        "SELECT link_type, target_id, target_label, description "
        "FROM entry_connections WHERE entry_id = ? ORDER BY connection_order",
        (entry_id,),
    ).fetchall()
    conn.close()

    semantic = get_similar(entry_id, n=5)

    return {
        "entry_id": entry_id,
        "explicit_connections": [dict(r) for r in explicit],
        "semantic_neighbors":   semantic,
    }


@mcp.tool()
def get_conjectures(gate: str | None = None) -> list[dict]:
    """
    All conjectures (P1-P16) with full fields, optionally filtered by gate.

    Args:
        gate: e.g. "G1" — returns only conjectures linked to that gate
    """
    conn = _source_conn()
    if gate:
        rows = conn.execute(
            "SELECT * FROM conjectures WHERE gate LIKE ? ORDER BY conjecture_order",
            (f"%{gate}%",),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM conjectures ORDER BY conjecture_order"
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@mcp.tool()
def get_gates() -> list[dict]:
    """All validation gates (G1-G10) with claim, priority, and blocking entries."""
    conn = _source_conn()
    rows = conn.execute("SELECT * FROM gates").fetchall()
    conn.close()
    return [dict(r) for r in rows]


@mcp.tool()
def get_all_links() -> list[dict]:
    """
    Full typed link graph — all explicit relationships between entries.
    Link types: generalizes, derives from, constrains, couples to, predicts for,
    tensions with, analogous to, tests, implements.
    """
    conn = _source_conn()
    rows = conn.execute(
        "SELECT link_type, source_id, source_label, target_id, target_label, description, confidence_tier "
        "FROM links ORDER BY link_order"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ══════════════════════════════════════════════════════════════════════════════
# VECTOR HISTORY & TOPOLOGY
# ══════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def list_snapshots() -> list[dict]:
    """
    All sync snapshots, newest first.
    Each snapshot is a complete semantic record of the wiki at that moment.
    Returns snapshot_id, created_at, trigger, chunk_count, notes.
    """
    return topo.list_snapshots()


@mcp.tool()
def get_drift_report(snapshot_id: str | None = None) -> dict:
    """
    Semantic change report comparing a snapshot to its predecessor.
    Defaults to latest snapshot vs the one before it.

    Shows:
    - mean_drift: average semantic movement across all chunks
    - top_drifted: the 10 chunks that moved most in semantic space
    - new_chunks: chunks added in this snapshot
    - changed_chunks: chunks whose content changed
    - converging_pairs: idea pairs that became more semantically similar
    - isolated_chunks: ideas that sit far from the corpus centroid

    Args:
        snapshot_id: optional — defaults to latest snapshot
    """
    return topo.get_drift_report(snapshot_id)


@mcp.tool()
def get_entry_trajectory(entry_id: str) -> list[dict]:
    """
    How an entry has moved through semantic space across all snapshots.
    For each snapshot, returns each chunk's centroid distance, top-5 neighbours,
    and semantic drift from the previous snapshot.

    Answers: "Has G1 been drifting toward established entries over time?"

    Args:
        entry_id: e.g. "G1", "M6", "Ax2"
    """
    return topo.get_entry_trajectory(entry_id)


@mcp.tool()
def get_neighborhood_history(chunk_id: str) -> list[dict]:
    """
    How the top-5 nearest neighbours of a specific chunk have changed
    across all snapshots. Jaccard distance measures how much the
    neighbour set changed between snapshots.

    Answers: "Which entries have become more/less related to M6 over time?"

    Args:
        chunk_id: e.g. "M6_Formula", "G1_What_It_Claims", "conj_P1"
    """
    return topo.get_neighborhood_history(chunk_id)


@mcp.tool()
def get_isolated_chunks(snapshot_id: str | None = None) -> list[dict]:
    """
    Chunks that sit far from the corpus centroid — semantic outliers.
    These are the most conceptually unique or isolated ideas in the wiki,
    measured as centroid_distance > mean + 2*stdev.

    Returns chunk_id, entry_id, centroid_distance, z_score.

    Args:
        snapshot_id: optional — defaults to latest snapshot
    """
    return topo.get_isolated_chunks(snapshot_id)


@mcp.tool()
def compare_snapshots(snap_a: str, snap_b: str) -> dict:
    """
    Full semantic diff between two snapshots.
    Shows added/removed chunks and per-chunk drift for changed content.

    Args:
        snap_a: earlier snapshot_id (from list_snapshots)
        snap_b: later snapshot_id
    """
    return topo.compare_snapshots(snap_a, snap_b)


@mcp.tool()
def get_cluster_evolution() -> list[dict]:
    """
    Per snapshot: the top-10 most similar chunk pairs.
    Reveals which idea pairs have consistently been close (stable clusters)
    and whether new tight relationships have formed over time.
    """
    return topo.get_cluster_evolution()


# ══════════════════════════════════════════════════════════════════════════════
# WRITE OPERATIONS
# ══════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def update_section(entry_id: str, section_name: str, new_content: str) -> dict:
    """
    Update the content of a specific section in ds_wiki.db.
    Automatically:
      1. Backs up ds_wiki.db before writing
      2. Writes the new content to the sections table
      3. Runs a full resync (re-embeds all chunks, records new snapshot)

    Args:
        entry_id:    e.g. "G1", "M6", "Ax2"
        section_name: exact section name e.g. "What It Claims", "Formula"
        new_content: the new markdown content for this section

    Returns: {success, snapshot_id, backup_path, message}
    """
    import shutil
    from datetime import datetime, timezone

    # Validate entry + section exist
    conn = sqlite3.connect(SOURCE_DB)
    row  = conn.execute(
        "SELECT id FROM sections WHERE entry_id=? AND section_name=?",
        (entry_id, section_name),
    ).fetchone()
    if not row:
        conn.close()
        return {
            "success": False,
            "message": f"Section '{section_name}' not found in entry '{entry_id}'. "
                       f"Use get_entry('{entry_id}') to see available sections.",
        }

    # Backup before write
    ts      = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    bdir    = Path(__file__).resolve().parent.parent / "backups" / f"backup_{ts}_update_{entry_id}"
    bdir.mkdir(parents=True, exist_ok=True)
    backup_path = bdir / "ds_wiki.db"
    shutil.copy2(SOURCE_DB, backup_path)

    # Write
    conn.execute(
        "UPDATE sections SET content=? WHERE entry_id=? AND section_name=?",
        (new_content, entry_id, section_name),
    )
    conn.commit()
    conn.close()

    # Resync
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from sync import sync_after_update
    snapshot_id = sync_after_update(
        entry_id, notes=f"Updated section '{section_name}' of {entry_id}"
    )

    return {
        "success":     True,
        "snapshot_id": snapshot_id,
        "backup_path": str(backup_path),
        "message":     f"Section '{section_name}' of '{entry_id}' updated. "
                       f"New snapshot: {snapshot_id}.",
    }


@mcp.tool()
def trigger_sync(notes: str = "") -> dict:
    """
    Manually trigger a full resync of the wiki.
    Use after making direct changes to ds_wiki.db outside of update_section.
    Backs up the DB, re-extracts all chunks, re-embeds, and records a new snapshot.

    Args:
        notes: optional note to attach to this snapshot

    Returns: {snapshot_id, chunk_count, message}
    """
    from sync import sync
    snapshot_id = sync(trigger="manual", notes=notes, backup=True)
    snaps       = topo.list_snapshots()
    chunk_count = snaps[0]["chunk_count"] if snaps else 0
    return {
        "snapshot_id": snapshot_id,
        "chunk_count": chunk_count,
        "message":     f"Sync complete. Snapshot {snapshot_id} recorded with {chunk_count} chunks.",
    }


@mcp.tool()
def add_link(
    source_id:       str,
    target_id:       str,
    link_type:       str,
    description:     str,
    source_label:    str = "",
    target_label:    str = "",
    confidence_tier: str = "",
    similarity_score: float = 0.0,
) -> dict:
    """
    Add a new typed link to the wiki link graph (links table in ds_wiki.db).
    Automatically backs up the DB before writing and triggers a full resync.

    Valid link_types:
        tests          — source provides evidence for/against target
        implements     — source is the mathematical method used by target
        generalizes    — target is a special case of source
        derives from   — source is logically derived from target
        analogous to   — same mathematical structure, different domain
        couples to     — source and target share a state variable
        constrains     — source sets a boundary condition on target
        predicts for   — source generates a testable claim about target
        tensions with  — source and target offer competing explanations

    Confidence tiers (objective — derived from cosine similarity, not subjective):
        "1"   ≥ 0.90  — definitionally certain (structural, high-signal)
        "1.5" 0.85–0.89 — strong semantic bond, not definitional (half-tier)
        "2"   0.82–0.84 — plausible transitional connection

    Args:
        source_id:        e.g. "T4", "H1", "Ax2", "conj_P1", "gate_G1"
        target_id:        e.g. "conj_P1", "X3", "Q1"
        link_type:        one of the valid types above
        description:      one sentence explaining the relationship in DS terms
        source_label:     display label (defaults to source_id if omitted)
        target_label:     display label (defaults to target_id if omitted)
        confidence_tier:  "1", "1.5", or "2" — auto-computed from similarity_score if omitted
        similarity_score: cosine similarity (0–1) — used to auto-compute tier if confidence_tier omitted

    Returns: {success, link_id, confidence_tier, backup_path, snapshot_id, message}
    """
    import shutil
    from datetime import datetime, timezone

    valid_types = {
        "tests", "implements", "generalizes", "derives from",
        "analogous to", "couples to", "constrains", "predicts for", "tensions with",
    }
    if link_type not in valid_types:
        return {
            "success": False,
            "message": f"Invalid link_type '{link_type}'. Must be one of: {sorted(valid_types)}",
        }

    # Resolve tier
    tier = confidence_tier if confidence_tier in ("1", "1.5", "2") \
        else (score_to_tier(similarity_score) if similarity_score > 0 else None)

    # Backup before write
    ts      = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    bdir    = Path(__file__).resolve().parent.parent / "backups" / f"backup_{ts}_addlink_{source_id}_{target_id}"
    bdir.mkdir(parents=True, exist_ok=True)
    backup_path = bdir / "ds_wiki.db"
    shutil.copy2(SOURCE_DB, backup_path)

    wconn     = sqlite3.connect(SOURCE_DB)
    max_order = wconn.execute("SELECT COALESCE(MAX(link_order), 0) FROM links").fetchone()[0]
    wconn.execute(
        "INSERT INTO links "
        "(link_type, source_id, source_label, target_id, target_label, description, link_order, confidence_tier) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (link_type, source_id, source_label or source_id,
         target_id, target_label or target_id, description, max_order + 1, tier),
    )
    link_id = wconn.execute("SELECT last_insert_rowid()").fetchone()[0]
    wconn.commit()
    wconn.close()

    from sync import sync
    snapshot_id = sync(
        trigger=f"add_link:{source_id}→{target_id}",
        notes=f"Added '{link_type}' T{tier} link: {source_id} → {target_id}",
        backup=False,
    )

    return {
        "success":         True,
        "link_id":         link_id,
        "confidence_tier": tier,
        "backup_path":     str(backup_path),
        "snapshot_id":     snapshot_id,
        "message":         f"Link added: {source_id} —[{link_type}]→ {target_id}  (T{tier}). Snapshot: {snapshot_id}.",
    }


@mcp.tool()
def add_links_batch(links: list[dict]) -> dict:
    """
    Add multiple links in a single operation with one backup and one resync.
    More efficient than calling add_link repeatedly.

    Each link dict must have:
        source_id, target_id, link_type, description
    Optionally: source_label, target_label

    Returns: {success_count, failed, snapshot_id, backup_path}
    """
    import shutil
    from datetime import datetime, timezone

    valid_types = {
        "tests", "implements", "generalizes", "derives from",
        "analogous to", "couples to", "constrains", "predicts for", "tensions with",
    }

    # Single backup for the whole batch
    ts      = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    bdir    = Path(__file__).resolve().parent.parent / "backups" / f"backup_{ts}_addlinks_batch"
    bdir.mkdir(parents=True, exist_ok=True)
    backup_path = bdir / "ds_wiki.db"
    shutil.copy2(SOURCE_DB, backup_path)

    wconn     = sqlite3.connect(SOURCE_DB)
    max_order = wconn.execute("SELECT COALESCE(MAX(link_order), 0) FROM links").fetchone()[0]

    success_count = 0
    failed        = []

    for i, lnk in enumerate(links):
        sid  = lnk.get("source_id", "")
        tid  = lnk.get("target_id", "")
        lt   = lnk.get("link_type", "")
        desc = lnk.get("description", "")

        if lt not in valid_types:
            failed.append({"link": lnk, "reason": f"Invalid link_type '{lt}'"})
            continue
        if not sid or not tid or not desc:
            failed.append({"link": lnk, "reason": "Missing source_id, target_id, or description"})
            continue

        try:
            # Resolve confidence tier
            tier = lnk.get("confidence_tier")
            if tier not in ("1", "1.5", "2"):
                score = lnk.get("similarity_score", 0.0)
                tier  = score_to_tier(score) if score > 0 else None

            wconn.execute(
                "INSERT INTO links "
                "(link_type, source_id, source_label, target_id, target_label, description, link_order, confidence_tier) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (lt, sid, lnk.get("source_label", sid), tid, lnk.get("target_label", tid),
                 desc, max_order + i + 1, tier),
            )
            success_count += 1
        except Exception as e:
            failed.append({"link": lnk, "reason": str(e)})

    wconn.commit()
    wconn.close()

    from sync import sync
    snapshot_id = sync(
        trigger=f"add_links_batch:{success_count}",
        notes=f"Batch added {success_count} links",
        backup=False,
    )

    return {
        "success_count": success_count,
        "failed":        failed,
        "snapshot_id":   snapshot_id,
        "backup_path":   str(backup_path),
        "message":       f"{success_count} links added. {len(failed)} failed. Snapshot: {snapshot_id}.",
    }


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)

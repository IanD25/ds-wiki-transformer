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
        "Semantic knowledge base for the Dimensional Scaling (DS) 2.x Wiki, "
        "expanded with 43 cross-domain reference_law entries spanning mathematics, "
        "computer science, biology, chemistry, and information theory. "
        "199 entries total (139 reference_law + 60 DS-native), 1562 indexed chunks, "
        "16 conjectures (P1-P16), 10 gates (G1-G10). "
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


# ══════════════════════════════════════════════════════════════════════════════
# LINK TRIAGE (classifier integration)
# ══════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_link_candidates(
    sim_threshold: float = 0.78,
    max_pairs:     int   = 60,
    entry_types:   list[str] | None = None,
) -> dict:
    """
    Generate unlinked entry pairs above a cosine similarity threshold,
    with full WIC + Mathematical Form content for each entry.

    Returns a triage prompt (paste to Claude) plus structured candidate list.
    Use insert_triage_results() to write approved classifications back to the DB.

    Args:
        sim_threshold: cosine similarity floor (default 0.78)
        max_pairs:     max candidate pairs to return (default 60)
        entry_types:   restrict to specific entry types, e.g. ["reference_law"]
                       (None = all types)

    Returns:
        {
          "candidate_count": int,
          "sim_threshold": float,
          "candidates": [ {pair, source_id, source, target_id, target, similarity}, ... ],
          "triage_prompt": "..."   # full prompt for Claude to classify
        }
    """
    from analysis.link_classifier import LinkClassifier

    lc = LinkClassifier()
    candidates = lc.get_candidates(
        sim_threshold=sim_threshold,
        max_pairs=max_pairs,
        entry_types=entry_types,
    )

    candidate_list = [
        {
            "pair":       i + 1,
            "source_id":  c.entry_a.entry_id,
            "source":     c.entry_a.title,
            "source_domain": c.entry_a.domain,
            "target_id":  c.entry_b.entry_id,
            "target":     c.entry_b.title,
            "target_domain": c.entry_b.domain,
            "similarity": c.similarity,
        }
        for i, c in enumerate(candidates)
    ]

    triage_prompt = lc.format_triage_prompt(candidates)

    return {
        "candidate_count": len(candidates),
        "sim_threshold":   sim_threshold,
        "candidates":      candidate_list,
        "triage_prompt":   triage_prompt,
    }


@mcp.tool()
def insert_triage_results(
    classifications_json: str,
    min_confidence:       float = 0.80,
    dry_run:              bool  = False,
) -> dict:
    """
    Insert LLM-classified link results into the knowledge graph.

    Takes the JSON array produced by the link classifier (each item must have:
    pair, source_id, source_label, target_id, target_label, has_link,
    link_type, confidence, description) and writes approved links to ds_wiki.db.

    Skips: has_link=false, confidence < min_confidence, already-existing pairs.
    Does NOT auto-sync — call trigger_sync() separately when ready.

    Args:
        classifications_json: JSON array of classification results
        min_confidence:       minimum confidence to insert (default 0.80)
        dry_run:              if True, print without writing (default False)

    Returns:
        {inserted, skipped_confidence, skipped_no_link, skipped_exists, links}
    """
    from analysis.link_classifier import LinkClassifier, ClassificationResult

    try:
        raw = json.loads(classifications_json)
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON: {e}"}

    if not isinstance(raw, list):
        raw = [raw]

    results = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        results.append(ClassificationResult(
            source_id=item.get("source_id", ""),
            source_label=item.get("source_label", item.get("source_id", "")),
            target_id=item.get("target_id", ""),
            target_label=item.get("target_label", item.get("target_id", "")),
            has_link=bool(item.get("has_link", False)),
            link_type=item.get("link_type"),
            confidence=float(item.get("confidence", 0.0)),
            description=item.get("description"),
            reasoning=item.get("reasoning"),
            similarity=float(item.get("similarity", 0.0)),
        ))

    lc = LinkClassifier()
    counts = lc.insert_results(results, min_confidence=min_confidence, dry_run=dry_run)

    return {
        **counts,
        "min_confidence": min_confidence,
        "dry_run":        dry_run,
        "message": (
            f"{'[DRY RUN] ' if dry_run else ''}"
            f"{counts['inserted']} links inserted. "
            f"{counts['skipped_no_link']} no-link, "
            f"{counts['skipped_confidence']} low-confidence, "
            f"{counts['skipped_exists']} already exist."
        ),
    }


# ── Claim validation ──────────────────────────────────────────────────────────

@mcp.tool()
def validate_claim(
    claim:          str,
    top_k:          int   = 15,
    high_threshold: float = 0.72,
    low_threshold:  float = 0.55,
) -> dict:
    """
    Validate a free-text research claim against the knowledge base.

    Embeds the claim with BGE, retrieves the top-k most similar KB chunks,
    deduplicates to entry level, and classifies each entry as supporting,
    contradicting (if it has a 'tensions with' link to another high-sim entry),
    or related.

    Returns a consistency_score (0–1), lists of supporting/contradicting/related
    entries, and a ready-to-read markdown report.

    Args:
        claim:          Natural-language claim to validate.
        top_k:          Number of KB chunks to retrieve (default 15).
        high_threshold: Cosine sim above which an entry is "directly relevant"
                        (default 0.72).
        low_threshold:  Cosine sim above which an entry is "related"
                        (default 0.55).

    Returns:
        {consistency_score, supporting_count, contradiction_count, related_count,
         supporting, contradictions, related, notes, markdown}
    """
    from analysis.result_validator import ResultValidator

    validator = ResultValidator(source_db=SOURCE_DB, chroma_dir=CHROMA_DIR)
    result    = validator.validate_claim(
        claim,
        top_k=top_k,
        high_threshold=high_threshold,
        low_threshold=low_threshold,
    )

    def _serialise(items):
        return [
            {
                "entry_id":    e.entry_id,
                "title":       e.title,
                "entry_type":  e.entry_type,
                "domain":      e.domain,
                "similarity":  round(e.similarity, 4),
                "link_type":   e.link_type,
                "linked_to":   e.linked_to,
                "linked_title": e.linked_title,
                "excerpt":     e.excerpt,
            }
            for e in items
        ]

    return {
        "consistency_score":    round(result.consistency_score, 4),
        "supporting_count":     len(result.supporting_evidence),
        "contradiction_count":  len(result.contradictions),
        "related_count":        len(result.related_entities),
        "supporting":           _serialise(result.supporting_evidence),
        "contradictions":       _serialise(result.contradictions),
        "related":              _serialise(result.related_entities),
        "notes":                result.notes,
        "markdown":             result.as_markdown(),
    }


# ── Gap analysis ──────────────────────────────────────────────────────────────

@mcp.tool()
def analyze_gaps(
    type_minimums_json: str = "{}",
) -> dict:
    """
    Identify knowledge-base gaps and return ranked enrichment priorities.

    Analyses the KB for:
    - Property coverage gaps per entity type (e.g. 'CS entries missing concept_tags')
    - Sparse taxonomy values (archetypes or d-sensitivity values with < 3% representation)
    - Entity type balance gaps (types below expected minimum counts)
    - Link gaps (isolated entries, entries with no tier-1 links, same-type-only links)

    Returns a full markdown report plus structured lists for each gap category.

    Args:
        type_minimums_json: Optional JSON object overriding expected minimum counts per
                            entity type, e.g. '{"open_question": 20, "method": 15}'.
                            Merged over built-in defaults. Pass '{}' to use defaults.

    Returns:
        {summary_stats, property_gaps, taxonomy_gaps, type_balance_gaps, link_gaps,
         enrichment_priorities, markdown}
    """
    from analysis.gap_analyzer import GapAnalyzer

    try:
        overrides = json.loads(type_minimums_json) if type_minimums_json.strip() != "{}" else {}
    except json.JSONDecodeError as e:
        return {"error": f"Invalid type_minimums_json: {e}"}

    ga     = GapAnalyzer(source_db=SOURCE_DB, type_minimums=overrides or None)
    report = ga.analyze()

    def _ser_prop(g):
        return {
            "entity_type": g.entity_type, "property_name": g.property_name,
            "total_of_type": g.total_of_type, "filled": g.filled,
            "missing_count": g.missing_count, "coverage_pct": g.coverage_pct,
            "missing_ids": g.missing_ids, "priority": g.priority,
        }

    def _ser_tax(g):
        return {
            "taxonomy_name": g.taxonomy_name, "value": g.value,
            "count": g.count, "pct_of_filled": g.pct_of_filled, "flag": g.flag,
        }

    def _ser_type(g):
        return {
            "entity_type": g.entity_type, "observed": g.observed,
            "expected_min": g.expected_min, "deficit": g.deficit,
            "suggestion": g.suggestion,
        }

    def _ser_link(g):
        return {
            "entry_id": g.entry_id, "title": g.title, "entity_type": g.entity_type,
            "total_links": g.total_links, "gap_type": g.gap_type, "detail": g.detail,
        }

    def _ser_pri(p):
        return {
            "rank": p.rank, "action": p.action, "target": p.target,
            "description": p.description, "impact_score": p.impact_score,
        }

    return {
        "summary_stats":         report.summary_stats,
        "property_gaps":         [_ser_prop(g) for g in report.property_gaps],
        "taxonomy_gaps":         [_ser_tax(g)  for g in report.taxonomy_gaps],
        "type_balance_gaps":     [_ser_type(g) for g in report.type_balance_gaps],
        "link_gaps":             [_ser_link(g) for g in report.link_gaps],
        "enrichment_priorities": [_ser_pri(p)  for p in report.enrichment_priorities],
        "markdown":              report.as_markdown(),
    }


# ── Visualization tools ───────────────────────────────────────────────────────

def _derive_viz_output_dir(bundle_db: str) -> Path:
    """
    Auto-derive visualization output directory from bundle_db path.
    data/rrp/zoo_classes/rrp_zoo_classes.db  →  data/viz/zoo_classes/
    """
    p = Path(bundle_db).resolve()
    bundle_name = p.parent.name
    output_dir  = p.parent.parent.parent / "viz" / bundle_name
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _serialize_viz_result(obj):
    """Recursively convert Path objects to str for JSON transport."""
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, dict):
        return {k: _serialize_viz_result(v) for k, v in obj.items()}
    return obj


@mcp.tool()
def visualize_bridges(
    bundle_db:     str,
    ds_wiki_db:    str | None = None,
    sim_threshold: float = 0.82,
) -> dict:
    """
    Generate a cross-universe bridge network visualization for an RRP bundle.
    Creates both a static PNG and an interactive self-contained HTML file.

    The network uses a deterministic two-column bipartite layout:
      Left  = DS Wiki entries (science universe) — squares, sized by bridge count
      Right = RRP entries (research universe) — circles, coloured by source type
      Edges = bridges, coloured by link type (analogous to / couples to)

    NOTE: Default threshold 0.82 keeps ~432 edges — the readable zone.
    Below 0.80 the graph becomes a hairball.

    Args:
        bundle_db:     Absolute path to the RRP bundle .db file.
        ds_wiki_db:    Path to ds_wiki.db (default: project SOURCE_DB).
        sim_threshold: Minimum cosine similarity for bridges (default 0.82).

    Returns:
        {"html": str, "png": str, "stats": {"rrp_nodes": int, "ds_nodes": int,
                                             "edges": int, "sim_threshold": float}}
    """
    from viz.bridge_network import BridgeNetwork
    result = BridgeNetwork(bundle_db, ds_wiki_db or SOURCE_DB).generate(
        output_dir    = _derive_viz_output_dir(bundle_db),
        sim_threshold = sim_threshold,
    )
    return _serialize_viz_result(result)


@mcp.tool()
def visualize_similarity_distribution(
    bundle_db:     str,
    sim_threshold: float = 0.75,
) -> dict:
    """
    Generate a histogram of cross-universe bridge similarity scores for an RRP bundle.

    Shows the distribution of cosine similarity across all stored bridges.
    Bars are stacked and coloured by confidence tier (tier 1.5 = warm red,
    tier 2 = steel blue). Annotates threshold lines at 0.75, 0.82, and 0.85.

    Args:
        bundle_db:     Absolute path to the RRP bundle .db file.
        sim_threshold: Minimum similarity to include (default 0.75 = all bridges).

    Returns:
        {"html": str, "png": str, "stats": {"total": int, "mean_sim": float, ...}}
    """
    from viz.similarity_hist import SimilarityHist
    result = SimilarityHist(bundle_db).generate(
        output_dir    = _derive_viz_output_dir(bundle_db),
        sim_threshold = sim_threshold,
    )
    return _serialize_viz_result(result)


@mcp.tool()
def visualize_domain_heatmap(
    bundle_db:     str,
    ds_wiki_db:    str | None = None,
    sim_threshold: float = 0.75,
) -> dict:
    """
    Generate a bridge-density heatmap for an RRP bundle.

    Rows = RRP source type (theorems, classes, conjectures, problems)
    Cols = DS Wiki type_group (RL, Q, X, H, M, T, B, F, E, Ax, Other)
    Cell = count of bridges at sim >= sim_threshold. Colour: YlOrRd.

    Highlights which RRP entry types connect to which DS Wiki knowledge clusters.

    Args:
        bundle_db:     Absolute path to the RRP bundle .db file.
        ds_wiki_db:    Path to ds_wiki.db (default: project SOURCE_DB).
        sim_threshold: Minimum similarity to include (default 0.75).

    Returns:
        {"html": str, "png": str, "stats": {"rows": int, "cols": int, "total_bridges": int}}
    """
    from viz.domain_heatmap import DomainHeatmap
    result = DomainHeatmap(bundle_db, ds_wiki_db or SOURCE_DB).generate(
        output_dir    = _derive_viz_output_dir(bundle_db),
        sim_threshold = sim_threshold,
    )
    return _serialize_viz_result(result)


@mcp.tool()
def visualize_all(
    bundle_db:  str,
    ds_wiki_db: str | None = None,
) -> dict:
    """
    Run all three cross-universe visualizations for an RRP bundle in one call.

    Generates six files in data/viz/{bundle_name}/:
      similarity_hist.{png,html}  — similarity distribution histogram
      domain_heatmap.{png,html}   — RRP source type × DS type_group density
      bridge_network.{png,html}   — bipartite bridge network

    Uses recommended defaults: network at sim ≥ 0.82, histogram+heatmap at sim ≥ 0.75.

    Args:
        bundle_db:  Absolute path to the RRP bundle .db file.
        ds_wiki_db: Path to ds_wiki.db (default: project SOURCE_DB).

    Returns:
        {
          "histogram": {"html": str, "png": str, "stats": dict},
          "heatmap":   {"html": str, "png": str, "stats": dict},
          "network":   {"html": str, "png": str, "stats": dict},
          "output_dir": str,
        }
    """
    from viz.viz_runner import run_all_viz
    result = run_all_viz(bundle_db, ds_wiki_db or SOURCE_DB)
    return _serialize_viz_result(result)


# ── Fisher Information Matrix tools ──────────────────────────────────────────

@mcp.tool()
def fisher_analyze_node(
    node_id:  str,
    mode:     str = "internal",
    rrp_db:   str | None = None,
    alpha:    float = 1.0,
) -> dict:
    """
    Run the Fisher Information Matrix pipeline on a single node and return its
    information-geometric regime (radial, isotropic, or noise-dominated).

    mode="internal":
        Analyzes the node within the DS Wiki graph (or within an RRP universe's
        own internal graph if rrp_db is provided).  Use this to diagnose whether
        a specific entry is a focused hub (radial) or a cross-domain bridge
        (isotropic) within its own knowledge base.

    mode="bridge":
        Analyzes the node within the full Option B bridge graph (RRP + DS Wiki
        combined, connected by cross-universe bridges).  Requires rrp_db.  Use
        this to see how a node integrates into the combined topology.

    Args:
        node_id: Entry ID to analyze.
                 For mode="internal" without rrp_db: a DS Wiki ID (e.g., "B5").
                 For mode="internal" with rrp_db: bare RRP ID (e.g., "rxn_PFK").
                 For mode="bridge": prefixed ID ("rrp::rxn_PFK" or "wiki::B5"),
                   or bare ID which will be tried with both prefixes.
        mode:    "internal" (default) or "bridge".
        rrp_db:  Absolute path to an RRP bundle .db file.
                 Required for mode="bridge"; optional for mode="internal".
        alpha:   Exponential kernel decay (default 1.0).

    Returns:
        {node_id, mode, regime, d_eff, pr, eta, center_degree,
         sv_profile, skipped, skip_reason}
    """
    from analysis.fisher_diagnostics import (
        build_wiki_graph, build_bridge_graph, analyze_node, KernelType,
    )

    kernel = KernelType.EXPONENTIAL

    if mode == "internal":
        db = Path(rrp_db) if rrp_db else SOURCE_DB
        G, _ = build_wiki_graph(db)
        result = analyze_node(G, node_id, kernel, alpha=alpha)

    elif mode == "bridge":
        if not rrp_db:
            return {"error": "rrp_db is required for mode='bridge'"}
        G, node_source = build_bridge_graph(Path(rrp_db), SOURCE_DB)
        # Try prefixed forms if bare ID not found
        nid = node_id
        if nid not in G:
            for prefix in ("rrp::", "wiki::"):
                if f"{prefix}{node_id}" in G:
                    nid = f"{prefix}{node_id}"
                    break
        result = analyze_node(G, nid, kernel, alpha=alpha)

    else:
        return {"error": f"Unknown mode '{mode}'. Use 'internal' or 'bridge'."}

    return {
        "node_id":       result.node_id,
        "mode":          mode,
        "regime":        result.regime.value,
        "d_eff":         result.d_eff,
        "pr":            round(result.pr, 4),
        "eta":           round(result.eta, 4),
        "center_degree": result.center_degree,
        "sv_profile":    [round(v, 4) for v in result.sv_profile[:8]],
        "skipped":       result.skipped,
        "skip_reason":   result.skip_reason,
    }


@mcp.tool()
def fisher_sweep_rrp(
    rrp_db: str,
    alpha:  float = 1.0,
    top_n:  int   = 10,
) -> dict:
    """
    Run the Tier-1 Fisher sweep on an RRP universe's internal graph.

    Answers: is this knowledge base internally consistent?  Returns regime
    distribution, top hubs by d_eff, and a TIER-1 VERDICT.

    Interpretation guide:
      - INTERNALLY CONSISTENT: ≥80% of analyzed nodes are non-noise
      - MARGINAL: 60–80% non-noise — some structural gaps
      - FRAGMENTED: <60% non-noise — graph is poorly connected or under-linked

    Top hubs with high d_eff are entries that sit at the intersection of many
    independent information pathways — metabolic crossroads, multi-constraint
    reactions, etc.  Isotropic nodes are genuine cross-domain entries.

    Args:
        rrp_db: Absolute path to the RRP bundle .db file.
        alpha:  Exponential kernel decay (default 1.0).
        top_n:  Number of top hubs to return (default 10).

    Returns:
        {graph_source, n_nodes, n_edges, n_analyzed, n_skipped,
         mean_d_eff, median_eta, regime_counts, top_hubs,
         tier1_verdict, internal_coherence, cross_domain_fraction}
    """
    from analysis.fisher_diagnostics import (
        build_wiki_graph, sweep_graph, KernelType,
    )

    rrp_path = Path(rrp_db)
    G, _     = build_wiki_graph(rrp_path)
    sweep    = sweep_graph(G, f"rrp_internal:{rrp_path.stem}", KernelType.EXPONENTIAL, alpha=alpha)

    n = sweep.n_analyzed
    noise_frac = sweep.regime_counts.get("noise_dominated", 0) / max(n, 1)
    coherence  = 1.0 - noise_frac
    iso_frac   = sweep.regime_counts.get("isotropic", 0) / max(n, 1)

    if coherence >= 0.80:
        verdict = "INTERNALLY CONSISTENT"
    elif coherence >= 0.60:
        verdict = "MARGINAL"
    else:
        verdict = "FRAGMENTED"

    hubs = [
        {
            "node_id":       r.node_id,
            "regime":        r.regime.value,
            "d_eff":         r.d_eff,
            "pr":            round(r.pr, 3),
            "eta":           round(r.eta, 3),
            "center_degree": r.center_degree,
        }
        for r in sweep.top_hubs(n=top_n)
    ]

    return {
        "graph_source":         sweep.graph_source,
        "n_nodes":              G.number_of_nodes(),
        "n_edges":              G.number_of_edges(),
        "n_analyzed":           sweep.n_analyzed,
        "n_skipped":            sweep.n_skipped,
        "mean_d_eff":           round(sweep.mean_d_eff, 3),
        "median_eta":           round(sweep.median_eta, 3),
        "regime_counts":        sweep.regime_counts,
        "top_hubs":             hubs,
        "tier1_verdict":        verdict,
        "internal_coherence":   round(coherence, 3),
        "cross_domain_fraction": round(iso_frac, 3),
    }


@mcp.tool()
def fisher_sweep_bridge(
    rrp_db:       str,
    min_sim:      float = 0.75,
    alpha:        float = 1.0,
    top_n:        int   = 10,
) -> dict:
    """
    Run the Tier-2 Fisher sweep on the full Option B bridge graph (RRP + DS Wiki).

    Answers: how well does this RRP universe integrate into the DS Wiki formal
    foundation?  Returns regime distribution for RRP nodes in the combined graph,
    the most-connected DS Wiki anchors, and a TIER-2 VERDICT.

    Interpretation guide:
      - WELL-INTEGRATED: ≥70% of RRP nodes analyzable in bridge graph + <30% noise
      - PARTIAL: ≥40% of RRP nodes bridged
      - ISOLATED: <40% of RRP nodes reach DS Wiki above min_sim threshold

    RRP nodes that are ISOTROPIC in the bridge graph instantiate multiple
    independent DS Wiki principles simultaneously — these are the richest
    cross-domain entries.  RADIAL nodes connect to DS Wiki at one focal point.

    Args:
        rrp_db:   Absolute path to the RRP bundle .db file.
        min_sim:  Minimum bridge similarity to include (default 0.75).
        alpha:    Exponential kernel decay (default 1.0).
        top_n:    Number of top hubs to return from each side (default 10).

    Returns:
        {graph_source, n_nodes, n_rrp, n_wiki, n_bridge_edges,
         rrp_regime_counts, rrp_mean_d_eff, top_rrp_hubs, top_wiki_anchors,
         tier2_verdict, bridge_fraction, cross_domain_fraction}
    """
    from analysis.fisher_diagnostics import (
        build_bridge_graph, sweep_graph, KernelType, RegimeType,
    )

    rrp_path = Path(rrp_db)
    G, node_source = build_bridge_graph(rrp_path, SOURCE_DB, min_bridge_similarity=min_sim)
    sweep = sweep_graph(G, f"bridge:{rrp_path.stem}", KernelType.EXPONENTIAL, alpha=alpha)

    # Partition results by universe
    rrp_results  = [r for nid, r in sweep.results.items()
                    if node_source.get(nid) == "rrp" and not r.skipped]
    wiki_results = [r for nid, r in sweep.results.items()
                    if node_source.get(nid) == "wiki" and not r.skipped]

    n_rrp_total = sum(1 for v in node_source.values() if v == "rrp")
    n           = len(rrp_results)
    bridge_frac = n / max(n_rrp_total, 1)
    iso_count   = sum(1 for r in rrp_results if r.regime == RegimeType.ISOTROPIC)
    noise_count = sum(1 for r in rrp_results if r.regime == RegimeType.NOISE_DOMINATED)
    rrp_mean_deff = sum(r.d_eff for r in rrp_results) / max(n, 1)

    if bridge_frac >= 0.70 and noise_count / max(n, 1) < 0.30:
        verdict = "WELL-INTEGRATED"
    elif bridge_frac >= 0.40:
        verdict = "PARTIAL"
    else:
        verdict = "ISOLATED"

    rrp_regime_counts: dict = {}
    for r in rrp_results:
        rrp_regime_counts[r.regime.value] = rrp_regime_counts.get(r.regime.value, 0) + 1

    def _hub_dict(r):
        return {
            "node_id":       r.node_id,
            "regime":        r.regime.value,
            "d_eff":         r.d_eff,
            "pr":            round(r.pr, 3),
            "eta":           round(r.eta, 3),
            "center_degree": r.center_degree,
        }

    top_rrp  = sorted(rrp_results,  key=lambda r: (r.d_eff, r.pr), reverse=True)[:top_n]
    top_wiki = sorted(wiki_results, key=lambda r: (r.d_eff, r.pr), reverse=True)[:top_n]

    n_bridge_edges = sum(
        1 for _, _, d in G.edges(data=True) if d.get("type") == "bridge"
    )

    return {
        "graph_source":          sweep.graph_source,
        "n_nodes":               G.number_of_nodes(),
        "n_rrp":                 n_rrp_total,
        "n_wiki":                sum(1 for v in node_source.values() if v == "wiki"),
        "n_bridge_edges":        n_bridge_edges,
        "min_sim":               min_sim,
        "rrp_regime_counts":     rrp_regime_counts,
        "rrp_mean_d_eff":        round(rrp_mean_deff, 3),
        "top_rrp_hubs":          [_hub_dict(r) for r in top_rrp],
        "top_wiki_anchors":      [_hub_dict(r) for r in top_wiki],
        "tier2_verdict":         verdict,
        "bridge_fraction":       round(bridge_frac, 3),
        "cross_domain_fraction": round(iso_count / max(n, 1), 3),
    }


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)

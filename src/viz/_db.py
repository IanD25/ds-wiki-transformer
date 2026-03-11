"""
_db.py — Shared database query layer for the viz package.

All SQL lives here so the three viz modules never touch SQLite directly.
"""

import sqlite3
from dataclasses import dataclass
from pathlib import Path


# ── Data classes ──────────────────────────────────────────────────────────────

@dataclass
class BridgeRow:
    rrp_entry_id:       str
    rrp_entry_title:    str
    ds_entry_id:        str
    ds_entry_title:     str      # WARNING: often stores raw ID, not real title
    similarity:         float
    proposed_link_type: str
    confidence_tier:    str
    rrp_source_type:    str      # from entries.source_type (theorems/classes/conjectures/problems)


@dataclass
class DSEntryMeta:
    entry_id:   str
    title:      str
    type_group: str
    domain:     str


# ── Loaders ───────────────────────────────────────────────────────────────────

def load_bridges(bundle_db: Path | str, sim_threshold: float = 0.75) -> list[BridgeRow]:
    """
    Load cross_universe_bridges joined with entries.source_type.
    Returns BridgeRow list filtered to similarity >= sim_threshold,
    sorted by similarity descending.

    NOTE: RRP entries table uses `source_type` ("theorems", "classes", etc.)
    not `entry_type` — aliased here as `rrp_source_type` to avoid confusion.
    """
    conn = sqlite3.connect(bundle_db)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT
            b.rrp_entry_id,
            b.rrp_entry_title,
            b.ds_entry_id,
            b.ds_entry_title,
            b.similarity,
            b.proposed_link_type,
            b.confidence_tier,
            COALESCE(e.source_type, 'unknown')  AS rrp_source_type
        FROM cross_universe_bridges b
        LEFT JOIN entries e ON b.rrp_entry_id = e.id
        WHERE b.similarity >= ?
        ORDER BY b.similarity DESC
        """,
        (sim_threshold,),
    ).fetchall()
    conn.close()
    return [
        BridgeRow(
            rrp_entry_id       = r["rrp_entry_id"],
            rrp_entry_title    = r["rrp_entry_title"] or r["rrp_entry_id"],
            ds_entry_id        = r["ds_entry_id"],
            ds_entry_title     = r["ds_entry_title"] or r["ds_entry_id"],
            similarity         = r["similarity"],
            proposed_link_type = r["proposed_link_type"] or "related",
            confidence_tier    = r["confidence_tier"] or "2",
            rrp_source_type    = r["rrp_source_type"],
        )
        for r in rows
    ]


def load_ds_entry_meta(
    ds_wiki_db: Path | str,
    entry_ids: list[str],
) -> dict[str, DSEntryMeta]:
    """
    Return {entry_id: DSEntryMeta} for the given DS Wiki entry IDs.
    Falls back gracefully when an ID is not found (returns a stub).

    Always use this instead of bridge.ds_entry_title — the bridge table
    stores the raw entry_id string in that column, not the human-readable title.
    """
    if not entry_ids:
        return {}

    conn = sqlite3.connect(ds_wiki_db)
    conn.row_factory = sqlite3.Row
    placeholders = ",".join("?" * len(entry_ids))
    rows = conn.execute(
        f"SELECT id, title, COALESCE(type_group,'?') as type_group, "
        f"COALESCE(domain,'?') as domain FROM entries WHERE id IN ({placeholders})",
        entry_ids,
    ).fetchall()
    conn.close()

    result = {
        r["id"]: DSEntryMeta(
            entry_id   = r["id"],
            title      = r["title"],
            type_group = r["type_group"],
            domain     = r["domain"],
        )
        for r in rows
    }

    # Stub out any IDs that weren't found
    for eid in entry_ids:
        if eid not in result:
            result[eid] = DSEntryMeta(
                entry_id   = eid,
                title      = eid,
                type_group = "?",
                domain     = "?",
            )

    return result


def load_bundle_name(bundle_db: Path | str) -> str:
    """Read package_name from rrp_meta. Falls back to db stem if not set."""
    conn = sqlite3.connect(bundle_db)
    row = conn.execute(
        "SELECT value FROM rrp_meta WHERE key='package_name'"
    ).fetchone()
    conn.close()
    return row[0] if row else Path(bundle_db).stem


def load_bridge_stats(bundle_db: Path | str) -> dict:
    """Summary counts for the full bridge table (unfiltered)."""
    conn = sqlite3.connect(bundle_db)
    conn.row_factory = sqlite3.Row
    total = conn.execute("SELECT COUNT(*) FROM cross_universe_bridges").fetchone()[0]
    tier_1_5 = conn.execute(
        "SELECT COUNT(*) FROM cross_universe_bridges WHERE similarity >= 0.85"
    ).fetchone()[0]
    mean_sim = conn.execute(
        "SELECT AVG(similarity) FROM cross_universe_bridges"
    ).fetchone()[0] or 0.0
    median_sim = conn.execute(
        """SELECT similarity FROM cross_universe_bridges
           ORDER BY similarity
           LIMIT 1 OFFSET (SELECT COUNT(*)/2 FROM cross_universe_bridges)"""
    ).fetchone()
    conn.close()
    return {
        "total":         total,
        "tier_1_5":      tier_1_5,
        "tier_2":        total - tier_1_5,
        "mean_sim":      round(mean_sim, 4),
        "median_sim":    round((median_sim[0] if median_sim else 0.0), 4),
    }

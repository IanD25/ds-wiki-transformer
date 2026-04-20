"""
snapshot_retention.py — Hysteresis policy for embedding snapshots.

Wiki content (entries, conjectures, falsifications) is never deleted — that rule
governs `ds_wiki.db`. Embedding snapshots in `wiki_history.db` are derivative
measurements, fully regenerable from `ds_wiki.db` via `python3 -m src.sync`. They
follow a retention policy so the DB stays under GitHub's 100MB file limit.

Default policy: keep the N most recent snapshots (by created_at).
"""
import sqlite3
from typing import Optional


DEFAULT_KEEP_N = 3


def prune_snapshots(
    conn: sqlite3.Connection,
    keep_n: int = DEFAULT_KEEP_N,
    vacuum: bool = True,
    verbose: bool = False,
) -> dict:
    """Delete all snapshots except the `keep_n` most recent (by created_at).

    Cascades to chunk_embedding_history and topology_metrics. Optionally VACUUMs
    to reclaim freed pages. Safe to call when the DB has fewer than keep_n
    snapshots — it's a no-op in that case.

    Returns counts: {snapshots_kept, snapshots_deleted, embedding_rows_deleted,
    metric_rows_deleted}.
    """
    if keep_n < 1:
        raise ValueError(f"keep_n must be >= 1, got {keep_n}")

    keepers = [
        r[0] for r in conn.execute(
            "SELECT snapshot_id FROM wiki_snapshots "
            "ORDER BY created_at DESC LIMIT ?",
            (keep_n,),
        ).fetchall()
    ]

    if not keepers:
        return {"snapshots_kept": 0, "snapshots_deleted": 0,
                "embedding_rows_deleted": 0, "metric_rows_deleted": 0}

    placeholders = ",".join("?" for _ in keepers)

    n_emb = conn.execute(
        f"DELETE FROM chunk_embedding_history WHERE snapshot_id NOT IN ({placeholders})",
        keepers,
    ).rowcount
    n_metric = conn.execute(
        f"DELETE FROM topology_metrics WHERE snapshot_id NOT IN ({placeholders})",
        keepers,
    ).rowcount
    n_snap = conn.execute(
        f"DELETE FROM wiki_snapshots WHERE snapshot_id NOT IN ({placeholders})",
        keepers,
    ).rowcount

    conn.commit()

    if vacuum and (n_emb or n_metric or n_snap):
        conn.execute("VACUUM")

    result = {
        "snapshots_kept": len(keepers),
        "snapshots_deleted": n_snap,
        "embedding_rows_deleted": n_emb,
        "metric_rows_deleted": n_metric,
    }

    if verbose:
        print(f"  retention: kept {result['snapshots_kept']} snapshots, "
              f"deleted {result['snapshots_deleted']} "
              f"({result['embedding_rows_deleted']} embedding rows, "
              f"{result['metric_rows_deleted']} metric rows)")

    return result

"""
cull_embedding_snapshots_2026_04_19.py — One-off migration to enforce N=3 retention.

Why: wiki_history.db hit 160MB in 2026-04-18 (chunk_embedding_history is 35257 rows
across 20 snapshots). Exceeds GitHub's 100MB file limit. Embedding snapshots are
derivative — fully regenerable via `python3 -m src.sync` — so culling does not
violate the no-deletions rule for wiki content.

Action: keep the 3 most recent snapshots, delete the rest, VACUUM.
Going forward, src/embedder.py calls prune_snapshots() at end of each sync.
"""
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))

from snapshot_retention import prune_snapshots, DEFAULT_KEEP_N  # noqa: E402

HISTORY_DB = ROOT / "data" / "wiki_history.db"


def file_size_mb(path: Path) -> float:
    return path.stat().st_size / 1024 / 1024


def main() -> None:
    if not HISTORY_DB.exists():
        print(f"ERROR: {HISTORY_DB} does not exist.")
        sys.exit(1)

    size_before = file_size_mb(HISTORY_DB)
    conn = sqlite3.connect(HISTORY_DB)

    snaps_before = conn.execute("SELECT COUNT(*) FROM wiki_snapshots").fetchone()[0]
    embeds_before = conn.execute("SELECT COUNT(*) FROM chunk_embedding_history").fetchone()[0]

    print(f"Before:  {size_before:.1f} MB  |  {snaps_before} snapshots  |  {embeds_before} embedding rows")
    print(f"Pruning to N={DEFAULT_KEEP_N} most recent snapshots...")

    result = prune_snapshots(conn, keep_n=DEFAULT_KEEP_N, vacuum=True, verbose=False)
    conn.close()

    size_after = file_size_mb(HISTORY_DB)
    snaps_after = result["snapshots_kept"]
    embeds_after = embeds_before - result["embedding_rows_deleted"]

    print(f"After:   {size_after:.1f} MB  |  {snaps_after} snapshots  |  {embeds_after} embedding rows")
    print()
    print(f"Reclaimed: {size_before - size_after:.1f} MB "
          f"({result['snapshots_deleted']} snapshots, "
          f"{result['embedding_rows_deleted']} embedding rows, "
          f"{result['metric_rows_deleted']} metric rows)")

    if size_after > 100:
        print(f"\nWARNING: {size_after:.1f} MB still exceeds GitHub's 100MB file limit.")
        sys.exit(2)
    else:
        print(f"\nOK: under 100MB limit ({100 - size_after:.1f} MB headroom).")


if __name__ == "__main__":
    main()

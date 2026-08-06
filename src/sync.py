"""
sync.py — Orchestrator: backup → extract → embed → record history.
Run directly as a script or import and call sync().
"""
import argparse
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import BACKUP_DIR, SOURCE_DB
from embedder import embed_and_store
from extractor import extract_chunks


def _backup_source(label: str = "") -> Path:
    """Copy ds_wiki.db to backups/ before any write operation."""
    ts       = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    tag      = f"_{label}" if label else ""
    dest_dir = BACKUP_DIR / f"backup_{ts}{tag}"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest     = dest_dir / "ds_wiki.db"
    shutil.copy2(SOURCE_DB, dest)
    print(f"Backup created: {dest}")
    return dest


def sync(
    trigger: str = "manual",
    notes: str = "",
    backup: bool = True,
    milestone: bool = False,
) -> str:
    """
    Full sync cycle:
      1. Backup ds_wiki.db
      2. Extract all chunks from source DB
      3. Embed + store in ChromaDB and wiki_history.db
    Returns snapshot_id.

    Set milestone=True to mark this snapshot permanent — it is prefixed with
    "milestone:" and exempted from retention pruning, so it accumulates into a
    longitudinal record of the embedding space over time. Reserve it for
    meaningful rebuilds (e.g. after a research pass), not routine syncs.
    """
    if milestone and not trigger.lower().startswith("milestone"):
        trigger = f"milestone:{trigger}"

    print(f"\n{'='*60}")
    print(f"DS Wiki Sync  |  trigger={trigger}")
    print(f"{'='*60}")

    if backup:
        _backup_source(label=trigger.replace(":", "_"))

    chunks      = extract_chunks()
    snapshot_id = embed_and_store(chunks, trigger=trigger, notes=notes)

    print(f"\n[OK] Sync complete -- snapshot: {snapshot_id}")
    return snapshot_id


def sync_after_update(entry_id: str, notes: str = "") -> str:
    return sync(trigger=f"update:{entry_id}", notes=notes)


def sync_after_add(entry_id: str, notes: str = "") -> str:
    return sync(trigger=f"add:{entry_id}", notes=notes)


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync DS Wiki → ChromaDB + history")
    parser.add_argument("--trigger", default="manual", help="Trigger label (default: manual)")
    parser.add_argument("--notes",   default="",       help="Optional note for this snapshot")
    parser.add_argument("--no-backup", action="store_true", help="Skip source backup")
    parser.add_argument("--milestone", action="store_true",
                        help="Mark this snapshot permanent (exempt from retention pruning)")
    args = parser.parse_args()

    snap = sync(
        trigger=args.trigger,
        notes=args.notes,
        backup=not args.no_backup,
        milestone=args.milestone,
    )
    print(f"\nSnapshot ID: {snap}")

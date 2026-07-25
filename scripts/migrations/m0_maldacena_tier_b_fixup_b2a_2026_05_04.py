"""
Tier B Fixup — Re-apply B2a after sequencing bug — 2026-05-04

The Tier B prose migration (m0_maldacena_tier_b_prose_2026_05_04.py) had
a bug for the case where two edits target the same column: it pre-computed
both expected_new values from the original, then UPDATE applied each in
sequence. The second UPDATE overwrote the first.

Result: B2b landed correctly (DESI σ-level update); B2a (Amendola 5σ
correction within phase1_results) was overwritten back to original.

This script is idempotent: it checks if B2a anchor substring is present
(meaning the original text survived), and if so applies the replacement.
If B2a is already applied, this script is a no-op.

Run: python3 scripts/migrations/m0_maldacena_tier_b_fixup_b2a_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")

FIND_TEXT = "- GW merger rates reject k = 3 at >5 sigma (Amendola 2024)."

REPLACE_TEXT = (
    "- GW merger rates currently in ~3σ tension with k = 3 (Amendola 2024 "
    "GWTC-3 2σ upper limits k<2.1; the 5σ rejection was the paper's "
    "FORECAST for ~250 additional events, not current data — corrected "
    "2026-05-04)."
)


def main() -> None:
    if not DS_WIKI_DB.exists():
        raise SystemExit(f"Cannot find {DS_WIKI_DB}; run from repo root")

    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()

    cur.execute("SELECT phase1_results FROM conjectures WHERE id='P17'")
    row = cur.fetchone()
    if row is None:
        raise SystemExit("P17 conjecture not found")
    current = row[0] or ""

    if FIND_TEXT not in current:
        if "~3σ tension with k = 3" in current:
            print("B2a appears already applied; nothing to do (idempotent).")
        else:
            print("B2a anchor substring not found AND replacement marker not found.")
            print("State unclear — investigate before re-running.")
        conn.close()
        return

    new = current.replace(FIND_TEXT, REPLACE_TEXT, 1)
    if new == current:
        raise SystemExit("Replacement was a no-op despite finding the substring; aborting")

    cur.execute("UPDATE conjectures SET phase1_results=? WHERE id='P17'", (new,))
    if cur.rowcount != 1:
        conn.rollback()
        conn.close()
        raise SystemExit(f"UPDATE affected {cur.rowcount} rows (expected 1); rolled back")

    conn.commit()
    conn.close()

    # Re-verify
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    cur.execute("SELECT phase1_results FROM conjectures WHERE id='P17'")
    after = (cur.fetchone() or [""])[0]
    conn.close()

    if FIND_TEXT in after:
        raise SystemExit("Original B2a anchor text still present after UPDATE; investigate")
    if "~3σ tension with k = 3" not in after:
        raise SystemExit("Replacement marker not present after UPDATE; investigate")

    print("B2a fixup complete. P17.phase1_results now contains both B2a and B2b corrections.")
    print(f"  +{len(REPLACE_TEXT) - len(FIND_TEXT)} chars net change.")


if __name__ == "__main__":
    main()

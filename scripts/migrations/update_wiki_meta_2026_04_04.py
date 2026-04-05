"""
Update wiki_meta total_entries row after 2026-04-04 insertions.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB


def update(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Count actual values
    n_entries = cur.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    n_links = cur.execute("SELECT COUNT(*) FROM links").fetchone()[0]
    n_conj = cur.execute("SELECT COUNT(*) FROM conjectures").fetchone()[0]
    n_gates = cur.execute("SELECT COUNT(*) FROM gates").fetchone()[0]
    n_sections = cur.execute("SELECT COUNT(*) FROM sections").fetchone()[0]

    # Count type groups
    n_groups = cur.execute("SELECT COUNT(DISTINCT type_group) FROM entries").fetchone()[0]

    new_meta = (
        f"{n_entries} entries ({n_groups} type groups), {n_links} links, "
        f"{n_conj} conjectures (P1-P{n_conj}), {n_gates} gates (G1-G{n_gates}), "
        f"{n_sections} sections. Last updated: 2026-04-04."
    )

    cur.execute(
        "UPDATE wiki_meta SET value = ? WHERE key = 'total_entries'",
        (new_meta,)
    )
    print(f"  wiki_meta updated: {new_meta}")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Updating wiki_meta in:\n  {SOURCE_DB}\n")
    update(SOURCE_DB)

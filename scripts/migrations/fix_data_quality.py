"""
Data quality fixes identified in the full wiki audit (2026-04-02):

1. Normalize entry_type: 'open_question' (BR01) → 'open question' (consistent with 7 others)
2. Update stale wiki_meta.total_entries (says 57, actual 273)
3. Normalize orphan link targets:
   - 'Gate G1' → 'G1', 'gate_G1' → 'G1' etc. (gates table uses G1-G11)
   - 'conj_P1' → 'P1' etc. (conjectures table uses P1-P22)
   - 'P21_conjecture' → 'P21'
   - Leave 'ΛCDM (external)' as-is (intentionally external reference)
   - Leave 'P3' as-is (valid conjecture reference)
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB


def run(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ------------------------------------------------------------------
    # 1. Normalize entry_type: open_question → open question
    # ------------------------------------------------------------------
    print("=== Fix 1: Normalize entry_type ===")
    cur.execute("UPDATE entries SET entry_type = 'open question' WHERE entry_type = 'open_question'")
    print(f"  Updated {cur.rowcount} entries (open_question → open question)")

    # ------------------------------------------------------------------
    # 2. Update stale wiki_meta.total_entries
    # ------------------------------------------------------------------
    print("\n=== Fix 2: Update wiki_meta ===")
    total = cur.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    conj_count = cur.execute("SELECT COUNT(*) FROM conjectures").fetchone()[0]
    gate_count = cur.execute("SELECT COUNT(*) FROM gates").fetchone()[0]
    link_count = cur.execute("SELECT COUNT(*) FROM links").fetchone()[0]
    section_count = cur.execute("SELECT COUNT(*) FROM sections").fetchone()[0]

    type_groups = cur.execute("SELECT COUNT(DISTINCT type_group) FROM entries").fetchone()[0]
    new_total = (
        f"{total} entries ({type_groups} type groups), {link_count} links, "
        f"{conj_count} conjectures (P1-P22), {gate_count} gates (G1-G11), "
        f"{section_count} sections. Last updated: 2026-04-02 (full wiki audit)."
    )
    cur.execute("UPDATE wiki_meta SET value = ? WHERE key = 'total_entries'", (new_total,))
    print(f"  Updated total_entries: {new_total}")

    # ------------------------------------------------------------------
    # 3. Normalize orphan link targets
    # ------------------------------------------------------------------
    print("\n=== Fix 3: Normalize orphan link targets ===")

    # 3a. Gate references: 'Gate G1' → 'G1', 'gate_G1' → 'G1'
    gate_fixes = 0
    for row in cur.execute("SELECT id, target_id FROM links WHERE target_id LIKE 'Gate G%' OR target_id LIKE 'gate_%'").fetchall():
        link_id, old_target = row
        # Extract gate number
        if old_target.startswith('Gate G'):
            new_target = old_target.replace('Gate ', '')  # 'Gate G1' → 'G1'
        elif old_target.startswith('gate_'):
            new_target = old_target.replace('gate_', '')  # 'gate_G1' → 'G1'
        else:
            continue

        # Handle 'Gate G5 (ext.)' → 'G5'
        if ' ' in new_target:
            new_target = new_target.split(' ')[0]

        cur.execute("UPDATE links SET target_id = ? WHERE id = ?", (new_target, link_id))
        gate_fixes += 1
    print(f"  Normalized {gate_fixes} gate link targets")

    # 3b. Conjecture references: 'conj_P1' → 'P1'
    conj_fixes = 0
    for row in cur.execute("SELECT id, target_id FROM links WHERE target_id LIKE 'conj_%'").fetchall():
        link_id, old_target = row
        new_target = old_target.replace('conj_', '')  # 'conj_P5' → 'P5'
        cur.execute("UPDATE links SET target_id = ? WHERE id = ?", (new_target, link_id))
        conj_fixes += 1
    print(f"  Normalized {conj_fixes} conjecture link targets")

    # 3c. P21_conjecture → P21
    cur.execute("UPDATE links SET target_id = 'P21' WHERE target_id = 'P21_conjecture'")
    print(f"  Normalized {cur.rowcount} P21_conjecture targets")

    # 3d. Leave 'ΛCDM (external)' and 'P3' as-is (intentional)
    print("  Left 'ΛCDM (external)' (2 links) and 'P3' (1 link) as-is")

    # ------------------------------------------------------------------
    # Verify
    # ------------------------------------------------------------------
    print("\n=== Verification ===")

    # Check entry_type
    ot_count = cur.execute("SELECT COUNT(*) FROM entries WHERE entry_type = 'open_question'").fetchone()[0]
    print(f"  open_question entries remaining: {ot_count} (should be 0)")

    # Check remaining orphans (excluding intentional ones)
    orphans = cur.execute('''
        SELECT DISTINCT l.target_id
        FROM links l
        LEFT JOIN entries e ON l.target_id = e.id
        LEFT JOIN conjectures c ON l.target_id = c.id
        LEFT JOIN gates g ON l.target_id = g.id
        WHERE e.id IS NULL AND c.id IS NULL AND g.id IS NULL
        AND l.target_id NOT LIKE 'ΛCDM%'
    ''').fetchall()
    print(f"  Remaining orphan targets (excl ΛCDM): {[r[0] for r in orphans]}")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Running data quality fixes on:\n  {SOURCE_DB}\n")
    run(SOURCE_DB)

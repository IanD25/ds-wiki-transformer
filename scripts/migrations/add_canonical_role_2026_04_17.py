"""
GSW Anchor Architecture — canonical_role refinement — 2026-04-17

Adds the `canonical_role` column to external_anchors, subdividing canonical
authorities into five roles (progenitor / axiomatic_foundation /
standard_textbook / living_reference / comprehensive_survey).

Why: a rich concept (Shannon entropy, General Relativity) has multiple
legitimately canonical sources playing DIFFERENT roles. Treating them all as
undifferentiated canonical_authority anchors loses information and gives the
prior-art gate no principled way to decide "which is THE canonical source."

The field is NULL for non-canonical_authority relationships.

CRITICAL CONSTRAINTS (per charter + CLAUDE.md):
- Never schema-alter ds_wiki.db
- All new tables/columns go in wiki_history.db
- CREATE TABLE IF NOT EXISTS / ALTER TABLE ADD COLUMN — safe to re-run via
  column-presence check
- Non-destructive: ALTER TABLE ADD COLUMN is always safe in SQLite

Run with: python3 scripts/migrations/add_canonical_role_2026_04_17.py
"""

import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")

VALID_CANONICAL_ROLES = (
    "progenitor",            # first publication establishing the concept
    "axiomatic_foundation",  # formal axiomatic characterization
    "standard_textbook",     # field-standard graduate textbook
    "living_reference",      # encyclopedic reference article
    "comprehensive_survey",  # well-cited synthesis / review
)


def column_exists(conn: sqlite3.Connection, table: str, column: str) -> bool:
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    return any(row[1] == column for row in cur.fetchall())


def apply_migration(conn: sqlite3.Connection) -> None:
    """Add canonical_role column if it doesn't already exist.

    Note: SQLite ALTER TABLE cannot add CHECK constraints to an existing column.
    We enforce the value-set via a CHECK at the table level by rebuilding the
    table ONLY if it contains no rows at migration time (safe case); otherwise
    we enforce via a trigger so existing data stays untouched.
    """
    if column_exists(conn, "external_anchors", "canonical_role"):
        print("  canonical_role column already present — no-op.")
        return

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM external_anchors")
    row_count = cur.fetchone()[0]

    roles_list = ", ".join(f"'{r}'" for r in VALID_CANONICAL_ROLES)

    if row_count == 0:
        # Safe to rebuild the table with proper CHECK constraint at column level
        print("  external_anchors has 0 rows — rebuilding table with CHECK constraint.")
        _rebuild_external_anchors_with_canonical_role(conn, roles_list)
    else:
        # Data exists — preserve it. Add column plus trigger-based validation.
        print(f"  external_anchors has {row_count} rows — adding column + validation trigger.")
        cur.execute(
            f"ALTER TABLE external_anchors ADD COLUMN canonical_role TEXT"
        )
        cur.executescript(f"""
        CREATE TRIGGER IF NOT EXISTS validate_canonical_role_insert
        BEFORE INSERT ON external_anchors
        FOR EACH ROW
        WHEN NEW.canonical_role IS NOT NULL
             AND NEW.canonical_role NOT IN ({roles_list})
        BEGIN
            SELECT RAISE(ABORT, 'invalid canonical_role value');
        END;

        CREATE TRIGGER IF NOT EXISTS validate_canonical_role_update
        BEFORE UPDATE OF canonical_role ON external_anchors
        FOR EACH ROW
        WHEN NEW.canonical_role IS NOT NULL
             AND NEW.canonical_role NOT IN ({roles_list})
        BEGIN
            SELECT RAISE(ABORT, 'invalid canonical_role value');
        END;

        CREATE TRIGGER IF NOT EXISTS require_canonical_role_for_authority_insert
        BEFORE INSERT ON external_anchors
        FOR EACH ROW
        WHEN NEW.relationship = 'canonical_authority'
             AND NEW.canonical_role IS NULL
        BEGIN
            SELECT RAISE(ABORT, 'canonical_role required when relationship=canonical_authority');
        END;

        CREATE TRIGGER IF NOT EXISTS require_canonical_role_for_authority_update
        BEFORE UPDATE ON external_anchors
        FOR EACH ROW
        WHEN NEW.relationship = 'canonical_authority'
             AND NEW.canonical_role IS NULL
        BEGIN
            SELECT RAISE(ABORT, 'canonical_role required when relationship=canonical_authority');
        END;
        """)

    conn.commit()


def _rebuild_external_anchors_with_canonical_role(
    conn: sqlite3.Connection, roles_list: str
) -> None:
    """Rebuild external_anchors with canonical_role as a proper column CHECK.

    Only invoked when table is empty. Preserves indexes.
    """
    # Repeat constraints from the original migration; keep in sync if changed.
    VALID_RELATIONSHIPS = (
        "canonical_authority", "specialization_of", "generalization_of",
        "reframing_of", "adjacent_concept", "cites", "cited_by",
        "contradicts", "null_hypothesis", "open_in_literature",
    )
    VALID_STABILITY_CLASSES = (
        "canonical", "active-literature", "preprint-evolving", "data-ref-periodic",
    )
    VALID_CONFIDENCE = ("high", "medium", "low")

    rel_check = ", ".join(f"'{r}'" for r in VALID_RELATIONSHIPS)
    stab_check = ", ".join(f"'{s}'" for s in VALID_STABILITY_CLASSES)
    conf_check = ", ".join(f"'{c}'" for c in VALID_CONFIDENCE)

    conn.executescript(f"""
    DROP TABLE IF EXISTS external_anchors;

    CREATE TABLE external_anchors (
        id                      INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_id                TEXT NOT NULL,
        source                  TEXT NOT NULL,
        identifier              TEXT NOT NULL,
        revision_id             TEXT,
        title                   TEXT,
        tier                    INTEGER NOT NULL CHECK(tier BETWEEN 1 AND 4),
        source_stability_class  TEXT NOT NULL CHECK(source_stability_class IN ({stab_check})),
        relationship            TEXT NOT NULL CHECK(relationship IN ({rel_check})),
        canonical_role          TEXT CHECK(canonical_role IS NULL OR canonical_role IN ({roles_list})),
        verified_date           DATE NOT NULL,
        verified_by_session     TEXT,
        confidence              TEXT NOT NULL CHECK(confidence IN ({conf_check})),
        notes                   TEXT,
        UNIQUE(entry_id, source, identifier, relationship),
        CHECK (
            (relationship = 'canonical_authority' AND canonical_role IS NOT NULL)
            OR (relationship != 'canonical_authority' AND canonical_role IS NULL)
        )
    );

    CREATE INDEX idx_ext_anchors_entry ON external_anchors(entry_id);
    CREATE INDEX idx_ext_anchors_source ON external_anchors(source);
    CREATE INDEX idx_ext_anchors_relationship ON external_anchors(relationship);
    CREATE INDEX idx_ext_anchors_verified ON external_anchors(verified_date);
    CREATE INDEX idx_ext_anchors_stability ON external_anchors(source_stability_class);
    CREATE INDEX idx_ext_anchors_canonical_role ON external_anchors(canonical_role);
    """)


def verify(conn: sqlite3.Connection) -> None:
    print("\nVerification:")
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(external_anchors)")
    cols = {row[1]: row for row in cur.fetchall()}
    assert "canonical_role" in cols, "canonical_role column missing"
    print("  [OK] canonical_role column present")

    # Positive test: valid canonical_authority + canonical_role should insert
    cur.execute(
        "INSERT INTO external_anchors "
        "(entry_id, source, identifier, tier, source_stability_class, "
        " relationship, canonical_role, verified_date, confidence) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        ("__ROLE_TEST__", "doi", "10.0/test", 1, "canonical",
         "canonical_authority", "progenitor", "2026-04-17", "high"),
    )

    # Negative test: canonical_authority without canonical_role must fail
    try:
        cur.execute(
            "INSERT INTO external_anchors "
            "(entry_id, source, identifier, tier, source_stability_class, "
            " relationship, verified_date, confidence) "
            "VALUES (?,?,?,?,?,?,?,?)",
            ("__ROLE_TEST2__", "doi", "10.0/test2", 1, "canonical",
             "canonical_authority", "2026-04-17", "high"),
        )
        raise AssertionError("canonical_authority without canonical_role was accepted!")
    except sqlite3.IntegrityError as e:
        print(f"  [OK] canonical_authority w/o canonical_role correctly rejected: {e}")

    # Negative test: invalid canonical_role value
    try:
        cur.execute(
            "INSERT INTO external_anchors "
            "(entry_id, source, identifier, tier, source_stability_class, "
            " relationship, canonical_role, verified_date, confidence) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            ("__ROLE_TEST3__", "doi", "10.0/test3", 1, "canonical",
             "canonical_authority", "NOT_A_REAL_ROLE", "2026-04-17", "high"),
        )
        raise AssertionError("invalid canonical_role was accepted!")
    except sqlite3.IntegrityError as e:
        print(f"  [OK] invalid canonical_role correctly rejected: {e}")

    # Negative test: non-canonical_authority with canonical_role must fail
    try:
        cur.execute(
            "INSERT INTO external_anchors "
            "(entry_id, source, identifier, tier, source_stability_class, "
            " relationship, canonical_role, verified_date, confidence) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            ("__ROLE_TEST4__", "doi", "10.0/test4", 1, "canonical",
             "adjacent_concept", "progenitor", "2026-04-17", "high"),
        )
        raise AssertionError("non-authority with canonical_role was accepted!")
    except sqlite3.IntegrityError as e:
        print(f"  [OK] adjacent_concept with canonical_role correctly rejected: {e}")

    conn.rollback()
    print("  [OK] all constraint tests rolled back; table state unchanged")


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        print(f"Applying canonical_role refinement to {WIKI_HISTORY_DB}...")
        apply_migration(conn)
        verify(conn)
        print("\nMigration complete. Safe to re-run.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

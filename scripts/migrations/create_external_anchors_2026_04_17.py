"""
GSW Anchor Architecture — Schema Migration — 2026-04-17

Creates three new tables in wiki_history.db to support the GSW (Greater Science
World) anchor architecture. See docs/GSW_ANCHOR_ARCHITECTURE.md for full design.

Tables created:
- external_anchors       : links entries to external canonical sources (Wikipedia,
                           arXiv, DOI, Scholarpedia, etc.) with typed relationships
- internal_constructions : first-class label for entries with no GSW equivalent —
                           flags them as project-internal with explicit scrutiny
                           rationale
- pending_anchor_reviews : review queue for anchor candidates whose relationship
                           does not fit any of the 10 locked types (orphan anchors
                           per §4.1 of the architecture doc)

CRITICAL CONSTRAINTS (per charter + CLAUDE.md):
- Never schema-alter ds_wiki.db (read-only source of truth)
- All new tables go in wiki_history.db
- CREATE TABLE IF NOT EXISTS / INSERT OR IGNORE throughout — safe to re-run
- Taxonomy frozen at 10 relationship types; new types require >= 2 orphan cases
- Age is not decay — canonical Tier 1 sources have no calendar staleness
  (verified_date is a historical record, not a decay clock)

Run with: python3 scripts/migrations/create_external_anchors_2026_04_17.py

Ships with ZERO data rows. Subsequent migrations populate anchors per entry.
"""

import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")

VALID_RELATIONSHIPS = (
    "canonical_authority",
    "specialization_of",
    "generalization_of",
    "reframing_of",
    "adjacent_concept",
    "cites",
    "cited_by",
    "contradicts",
    "null_hypothesis",
    "open_in_literature",
)

VALID_STABILITY_CLASSES = (
    "canonical",
    "active-literature",
    "preprint-evolving",
    "data-ref-periodic",
)

VALID_CONFIDENCE = ("high", "medium", "low")

VALID_SCRUTINY_LEVELS = (
    "owner-aware",
    "needs-review",
    "high-novelty-risk",
)

VALID_REVIEW_STATUS = (
    "pending_lit_review",
    "resolved_to_existing_relationship",
    "new_relationship_proposed",
    "discarded_not_valid",
)


def create_schema(conn: sqlite3.Connection) -> None:
    """Create the three GSW-anchor tables (idempotent)."""

    rel_check = ", ".join(f"'{r}'" for r in VALID_RELATIONSHIPS)
    stability_check = ", ".join(f"'{s}'" for s in VALID_STABILITY_CLASSES)
    confidence_check = ", ".join(f"'{c}'" for c in VALID_CONFIDENCE)
    scrutiny_check = ", ".join(f"'{s}'" for s in VALID_SCRUTINY_LEVELS)
    review_check = ", ".join(f"'{s}'" for s in VALID_REVIEW_STATUS)

    conn.executescript(f"""
    CREATE TABLE IF NOT EXISTS external_anchors (
        id                      INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_id                TEXT NOT NULL,
        source                  TEXT NOT NULL,
        identifier              TEXT NOT NULL,
        revision_id             TEXT,
        title                   TEXT,
        tier                    INTEGER NOT NULL CHECK(tier BETWEEN 1 AND 4),
        source_stability_class  TEXT NOT NULL CHECK(source_stability_class IN ({stability_check})),
        relationship            TEXT NOT NULL CHECK(relationship IN ({rel_check})),
        verified_date           DATE NOT NULL,
        verified_by_session     TEXT,
        confidence              TEXT NOT NULL CHECK(confidence IN ({confidence_check})),
        notes                   TEXT,
        UNIQUE(entry_id, source, identifier, relationship)
    );

    CREATE INDEX IF NOT EXISTS idx_ext_anchors_entry
        ON external_anchors(entry_id);
    CREATE INDEX IF NOT EXISTS idx_ext_anchors_source
        ON external_anchors(source);
    CREATE INDEX IF NOT EXISTS idx_ext_anchors_relationship
        ON external_anchors(relationship);
    CREATE INDEX IF NOT EXISTS idx_ext_anchors_verified
        ON external_anchors(verified_date);
    CREATE INDEX IF NOT EXISTS idx_ext_anchors_stability
        ON external_anchors(source_stability_class);

    CREATE TABLE IF NOT EXISTS internal_constructions (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_id            TEXT NOT NULL UNIQUE,
        reason              TEXT NOT NULL,
        searched_sources    TEXT NOT NULL,
        flagged_date        DATE NOT NULL,
        flagged_by_session  TEXT,
        scrutiny_level      TEXT NOT NULL CHECK(scrutiny_level IN ({scrutiny_check})),
        notes               TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_int_construct_entry
        ON internal_constructions(entry_id);
    CREATE INDEX IF NOT EXISTS idx_int_construct_scrutiny
        ON internal_constructions(scrutiny_level);

    CREATE TABLE IF NOT EXISTS pending_anchor_reviews (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_id            TEXT NOT NULL,
        proposed_source     TEXT NOT NULL,
        proposed_identifier TEXT NOT NULL,
        proposed_title      TEXT,
        reason_orphan       TEXT NOT NULL,
        gate_report_path    TEXT,
        flagged_date        DATE NOT NULL,
        flagged_by_session  TEXT,
        status              TEXT NOT NULL DEFAULT 'pending_lit_review'
                            CHECK(status IN ({review_check})),
        resolution_notes    TEXT,
        resolved_date       DATE
    );

    CREATE INDEX IF NOT EXISTS idx_pending_entry
        ON pending_anchor_reviews(entry_id);
    CREATE INDEX IF NOT EXISTS idx_pending_status
        ON pending_anchor_reviews(status);
    """)
    conn.commit()


def verify_schema(conn: sqlite3.Connection) -> dict:
    """Verify the three tables + all indexes exist and have expected shape."""
    results = {}
    cur = conn.cursor()

    expected_tables = {
        "external_anchors": [
            "id", "entry_id", "source", "identifier", "revision_id", "title",
            "tier", "source_stability_class", "relationship", "verified_date",
            "verified_by_session", "confidence", "notes",
        ],
        "internal_constructions": [
            "id", "entry_id", "reason", "searched_sources", "flagged_date",
            "flagged_by_session", "scrutiny_level", "notes",
        ],
        "pending_anchor_reviews": [
            "id", "entry_id", "proposed_source", "proposed_identifier",
            "proposed_title", "reason_orphan", "gate_report_path",
            "flagged_date", "flagged_by_session", "status", "resolution_notes",
            "resolved_date",
        ],
    }

    for table, expected_cols in expected_tables.items():
        cur.execute(f"PRAGMA table_info({table})")
        actual_cols = [row[1] for row in cur.fetchall()]
        missing = set(expected_cols) - set(actual_cols)
        extra = set(actual_cols) - set(expected_cols)
        results[table] = {
            "exists": len(actual_cols) > 0,
            "columns": actual_cols,
            "missing": sorted(missing),
            "extra": sorted(extra),
            "ok": len(actual_cols) > 0 and not missing,
        }

    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'idx_ext_anchors%' "
        "OR name LIKE 'idx_int_construct%' OR name LIKE 'idx_pending%'"
    )
    results["indexes"] = sorted(row[0] for row in cur.fetchall())

    return results


def test_roundtrip(conn: sqlite3.Connection) -> None:
    """Insert + rollback a sentinel row in each table to verify CHECK constraints."""
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO external_anchors "
        "(entry_id, source, identifier, tier, source_stability_class, "
        " relationship, verified_date, confidence, notes) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        ("__TEST__", "test-source", "test-id", 1, "canonical",
         "canonical_authority", "2026-04-17", "high", "rollback test"),
    )
    cur.execute(
        "INSERT INTO internal_constructions "
        "(entry_id, reason, searched_sources, flagged_date, scrutiny_level) "
        "VALUES (?,?,?,?,?)",
        ("__TEST__", "rollback test", "[]", "2026-04-17", "needs-review"),
    )
    cur.execute(
        "INSERT INTO pending_anchor_reviews "
        "(entry_id, proposed_source, proposed_identifier, reason_orphan, flagged_date) "
        "VALUES (?,?,?,?,?)",
        ("__TEST__", "test-source", "test-id", "rollback test", "2026-04-17"),
    )

    try:
        cur.execute(
            "INSERT INTO external_anchors "
            "(entry_id, source, identifier, tier, source_stability_class, "
            " relationship, verified_date, confidence) "
            "VALUES (?,?,?,?,?,?,?,?)",
            ("__TEST2__", "x", "y", 1, "canonical", "NOT_A_REAL_RELATION",
             "2026-04-17", "high"),
        )
        raise AssertionError("CHECK constraint on relationship did not fire!")
    except sqlite3.IntegrityError:
        pass

    try:
        cur.execute(
            "INSERT INTO external_anchors "
            "(entry_id, source, identifier, tier, source_stability_class, "
            " relationship, verified_date, confidence) "
            "VALUES (?,?,?,?,?,?,?,?)",
            ("__TEST3__", "x", "y", 7, "canonical", "cites",
             "2026-04-17", "high"),
        )
        raise AssertionError("CHECK constraint on tier did not fire!")
    except sqlite3.IntegrityError:
        pass

    conn.rollback()


def main() -> None:
    if not WIKI_HISTORY_DB.parent.exists():
        raise SystemExit(f"Expected dir {WIKI_HISTORY_DB.parent} does not exist.")

    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        print(f"Applying GSW-anchor schema to {WIKI_HISTORY_DB}...")
        create_schema(conn)

        results = verify_schema(conn)
        for table in ("external_anchors", "internal_constructions", "pending_anchor_reviews"):
            info = results[table]
            status = "OK" if info["ok"] else "FAIL"
            print(f"  [{status}] {table}  ({len(info['columns'])} cols)")
            if info["missing"]:
                print(f"         missing: {info['missing']}")
            if info["extra"]:
                print(f"         extra:   {info['extra']}")
        print(f"  indexes: {len(results['indexes'])} created")
        for idx in results["indexes"]:
            print(f"    - {idx}")

        print("\nRunning constraint round-trip test (rolled back)...")
        test_roundtrip(conn)
        print("  [OK] CHECK constraints fire on invalid relationship / tier")

        cur = conn.cursor()
        for t in ("external_anchors", "internal_constructions", "pending_anchor_reviews"):
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            n = cur.fetchone()[0]
            print(f"  {t}: {n} rows (expected 0 on fresh migration)")

        print("\nMigration complete. Safe to re-run.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

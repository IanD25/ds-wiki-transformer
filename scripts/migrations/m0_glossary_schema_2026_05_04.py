"""
Glossary infrastructure — schema additions — 2026-05-04

Adds the supporting schema for the defined-term glossary system:
  1. New link_type 'disambiguates from' in ds_wiki.db.link_type_definitions
  2. New table wiki_history.db.term_uses  (caches markup→term_slug references)
  3. New table wiki_history.db.glossary_meta (small status table)

This script does NOT add glossary entries themselves; that happens in the
companion seed migration m0_glossary_seed_2026_05_04.py.

Run: python3 scripts/migrations/m0_glossary_schema_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-glossary-infrastructure-2026-05-04"


def add_link_type() -> None:
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO link_type_definitions (link_type, meaning) VALUES (?, ?)",
        (
            "disambiguates from",
            "Source and Target share a name/symbol but refer to "
            "different mathematical objects. Used to mark "
            "vocabulary-overlap pairs that should NOT be treated as "
            "analogous. See M0 Maldacena deep-research pass 2026-05-04 "
            "and the glossary subsystem.",
        ),
    )
    inserted = cur.rowcount
    conn.commit()
    conn.close()
    print(f"link_type_definitions: inserted={inserted} (0 means already present)")


def create_term_uses_table() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS term_uses (
            id INTEGER PRIMARY KEY,
            entry_id TEXT NOT NULL,
            section_name TEXT,
            term_slug TEXT NOT NULL,
            occurrence_index INTEGER NOT NULL,
            surrounding_context TEXT,
            populated_date TEXT NOT NULL,
            populated_by_session TEXT,
            UNIQUE(entry_id, section_name, term_slug, occurrence_index)
        );
        CREATE INDEX IF NOT EXISTS idx_term_uses_entry ON term_uses(entry_id);
        CREATE INDEX IF NOT EXISTS idx_term_uses_term ON term_uses(term_slug);

        CREATE TABLE IF NOT EXISTS glossary_meta (
            key TEXT PRIMARY KEY,
            value TEXT,
            updated_date TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
    print("term_uses + glossary_meta tables created (or already present)")


def stamp_meta() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT OR REPLACE INTO glossary_meta (key, value, updated_date) VALUES (?, ?, ?)",
        ("schema_version", "1.0", TODAY),
    )
    cur.execute(
        "INSERT OR REPLACE INTO glossary_meta (key, value, updated_date) VALUES (?, ?, ?)",
        ("created_by_session", SESSION, TODAY),
    )
    cur.execute(
        "INSERT OR REPLACE INTO glossary_meta (key, value, updated_date) VALUES (?, ?, ?)",
        (
            "markup_convention",
            "[[g:slug]] or [[g:slug|display text]] for inline term references; "
            "slug = ds_wiki.db.entries.id minus 'gloss_' prefix",
            TODAY,
        ),
    )
    conn.commit()
    conn.close()
    print("glossary_meta seeded")


def main() -> None:
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")
    add_link_type()
    create_term_uses_table()
    stamp_meta()
    print(f"\nGlossary schema migration complete. Session: {SESSION}")


if __name__ == "__main__":
    main()

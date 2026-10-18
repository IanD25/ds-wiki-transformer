"""
Consistency pass, Phase 5 — separate scientific claims from process records
— 2026-10-18 (audit_ref gsw-consistency-pass-2026-10-18). Additive schema
change to wiki_history.db only (two read-only views). ds_wiki.db untouched.

WHY
---
confidence_calibration mixes scientific claims and process items under the
same labels (e.g. cca_terminology_rename and lambda_symbol_collision are both
"Established"). Raw row counts ("13 Established / 3 Falsified out of 82
records") were being quoted as if they described claims.

CLASSIFICATION (latest row per entity, by calibration_date then id)
  scientific: conjecture, cca_conjecture, entry, claim, chain,
              structural_observation, scientific_question, open_question
  process:    decision, terminology, literature_priority, pattern_observation
  Owner-approved per-entity overrides (2026-10-18):
    -> process:    lambda_symbol_collision (notation), endpoint_decision_revised
                   (tracks a decision), scaling_framework_root_diagnosis
                   (meta-diagnosis of the project's own framework)
    -> scientific: matrix_spectrum_reduces_to_critical_exponents (a tested
                   physics finding about 2D Ising)
  Entity types not listed fall into neither view; add them here when new
  types appear.

Dry run by default; --apply creates the views. Idempotent (DROP VIEW IF EXISTS
+ CREATE). Verifies that the two views partition the calibrated entities.
"""
import argparse
import sqlite3
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")

SCIENTIFIC_TYPES = ("conjecture", "cca_conjecture", "entry", "claim", "chain",
                    "structural_observation", "scientific_question", "open_question")
PROCESS_TYPES = ("decision", "terminology", "literature_priority", "pattern_observation")
FORCE_PROCESS = ("lambda_symbol_collision", "endpoint_decision_revised", "scaling_framework_root_diagnosis")
FORCE_SCIENTIFIC = ("matrix_spectrum_reduces_to_critical_exponents",)


def q(items):
    return ", ".join(f"'{x}'" for x in items)


CLASS_EXPR = f"""CASE
      WHEN entity_id IN ({q(FORCE_PROCESS)}) THEN 'process'
      WHEN entity_id IN ({q(FORCE_SCIENTIFIC)}) THEN 'scientific'
      WHEN entity_type IN ({q(SCIENTIFIC_TYPES)}) THEN 'scientific'
      WHEN entity_type IN ({q(PROCESS_TYPES)}) THEN 'process'
      ELSE 'unclassified' END"""


def view_sql(name, klass):
    return f"""CREATE VIEW {name} AS
WITH ranked AS (
  SELECT c.*, ROW_NUMBER() OVER (PARTITION BY entity_id
                                 ORDER BY calibration_date DESC, id DESC) AS rn
  FROM confidence_calibration c
), latest AS (
  SELECT id, entity_id, entity_type, confidence, calibration_date, audit_ref,
         short_status, rationale,
         {CLASS_EXPR} AS record_class
  FROM ranked WHERE rn = 1
)
SELECT id AS calibration_id, entity_id, entity_type, record_class, confidence,
       calibration_date, audit_ref, short_status, rationale
FROM latest WHERE record_class = '{klass}'"""


VIEWS = {
    "claim_status_latest": view_sql("claim_status_latest", "scientific"),
    "process_status_latest": view_sql("process_status_latest", "process"),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    for name, sql in VIEWS.items():
        print(f"--- {name} ---\n{sql}\n")
    if not a.apply:
        # validate the SQL against a temp copy of the schema without writing
        mem = sqlite3.connect(":memory:")
        mem.execute(conn.execute("SELECT sql FROM sqlite_master WHERE name='confidence_calibration'").fetchone()[0])
        for sql in VIEWS.values():
            mem.execute(sql)
        print("DRY RUN — SQL validated in memory; nothing written. Re-run with --apply.")
        return
    for name, sql in VIEWS.items():
        conn.execute(f"DROP VIEW IF EXISTS {name}")
        conn.execute(sql)
    conn.commit()
    n_ent = conn.execute("SELECT count(DISTINCT entity_id) FROM confidence_calibration").fetchone()[0]
    n_c = conn.execute("SELECT count(*) FROM claim_status_latest").fetchone()[0]
    n_p = conn.execute("SELECT count(*) FROM process_status_latest").fetchone()[0]
    overlap = conn.execute("SELECT count(*) FROM claim_status_latest WHERE entity_id IN (SELECT entity_id FROM process_status_latest)").fetchone()[0]
    conn.close()
    print(f"entities {n_ent} = claims {n_c} + process {n_p}; overlap {overlap}")
    if n_c + n_p != n_ent or overlap:
        raise SystemExit("Views do not partition the calibrated entities — investigate unclassified types")
    print("verified: views partition all calibrated entities")


if __name__ == "__main__":
    main()

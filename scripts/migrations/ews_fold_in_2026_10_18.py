"""
EWS / tipping-point fold-in — 2026-10-18 (audit_ref gsw-ews-fold-in-2026-10-18). Mode A.

Questions Raised Log item QR-006 (can information measures warn of tipping points earlier or
more reliably than critical slowing down?) sat on an almost empty patch of the wiki: no entries
for critical slowing down, tipping types or early-warning signals. This migration adds ten
reference_law entries (EWS1-EWS10) written from the sources, each with a canonical_authority
anchor, GSW domain tags, and links to existing entries (STAT3, STAT5, STAT6, X0_FIM_Regimes,
M3, NE05, IT05, INFO1, INFO4, MATH1, BIO16) and among themselves. No conjectures, no Q-entries,
no promotions, no calibration rows; X0's label is not touched.

Reading record for every source (full text / preprint / abstract / not read) is in each
anchor's notes and in docs/prior_art_reviews/EWS_FOLD_IN_2026_10.md.

Writes (ds_wiki.db): entries, sections (7-section reference_law template),
entry_properties (DS Facets + concept_tags), links.
Writes (wiki_history.db): external_anchors, entry_source_domains.

Dry run by default; --apply writes. Aborts if a planned (table, row, column)
target appears twice in the plan, if a link endpoint does not exist, or if an
entry exists in a state other than exactly as planned. Idempotent: an entry
already present with identical content is skipped; anchors/tags/links are
checked for presence before insert. Read-back verified after writing.
"""
import argparse
import sqlite3
import sys
from pathlib import Path

from ews_fold_in_data_2026_10_18 import ENTRIES, LINKS, ANCHORS, TAGS  # noqa: E402

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-ews-fold-in-2026-10-18"
D = "2026-10-18"

SECTION_NAMES = ["What It Claims", "Mathematical Form", "Constraint Category", "DS Cross-References",
                 "Mathematical Archetype", "What The Math Says", "Concept Tags"]
ALLOWED_LINK_TYPES = None  # loaded from link_type_definitions

def entry_label(conn, eid):
    if eid.startswith("P") and eid[1:].isdigit():
        if not conn.execute("SELECT 1 FROM conjectures WHERE id=?", (eid,)).fetchone():
            raise SystemExit(f"ABORT — conjecture {eid} not found")
        return f"[{eid}](conjectures/{eid.lower()}.md)"
    if eid.startswith("G") and eid[1:].isdigit():
        if not conn.execute("SELECT 1 FROM gates WHERE id=?", (eid,)).fetchone():
            raise SystemExit(f"ABORT — gate {eid} not found")
        return f"Gate {eid}"
    row = conn.execute("SELECT filename FROM entries WHERE id=?", (eid,)).fetchone()
    if row is None:
        planned = {e["id"]: e for e in ENTRIES}
        if eid not in planned:
            raise SystemExit(f"ABORT — link endpoint {eid} not found")
        return f"[{eid}](entries/{planned[eid]['filename']})"
    return f"[{eid}](entries/{row[0]})"


def check_plan():
    seen = set()
    def once(key):
        if key in seen:
            raise SystemExit(f"ABORT — duplicate planned target {key}")
        seen.add(key)
    for e in ENTRIES:
        once(("entries", e["id"]))
        if [s[0] for s in e["sections"]] != SECTION_NAMES:
            raise SystemExit(f"ABORT — {e['id']} sections do not follow the 7-section template")
        for name, _ in e["sections"]:
            once(("sections", e["id"], name))
        for tname, pname, _, _ in e["properties"]:
            once(("entry_properties", e["id"], tname, pname))
    for (src, tgt, lt, tier, desc) in LINKS:
        once(("links", src, tgt, lt))
    for a in ANCHORS:
        once(("external_anchors", a["entry_id"], a["source"], a["identifier"], a["relationship"]))
    for (eid, tag, primacy, conf, why) in TAGS:
        once(("entry_source_domains", eid, tag))
    new_ids = {e["id"] for e in ENTRIES}
    for eid in new_ids:
        if not any(a["entry_id"] == eid and a["relationship"] == "canonical_authority" for a in ANCHORS):
            raise SystemExit(f"ABORT — {eid} has no canonical_authority anchor")
        if not any(t[0] == eid and t[2] == "primary" for t in TAGS):
            raise SystemExit(f"ABORT — {eid} has no primary domain tag")


def entry_state(conn, e):
    """'absent', 'applied' (identical), or raise on partial/different."""
    row = conn.execute("SELECT title, filename, entry_type, scale, domain, status, confidence, type_group "
                       "FROM entries WHERE id=?", (e["id"],)).fetchone()
    if row is None:
        if conn.execute("SELECT 1 FROM sections WHERE entry_id=?", (e["id"],)).fetchone():
            raise SystemExit(f"ABORT — {e['id']} has sections but no entry row")
        return "absent"
    want = (e["title"], e["filename"], "reference_law", e["scale"], e["domain"], e["status"], e["confidence"], "RL")
    if tuple(row) != want:
        raise SystemExit(f"ABORT — {e['id']} exists with different metadata: {row}")
    secs = dict(conn.execute("SELECT section_name, content FROM sections WHERE entry_id=?", (e["id"],)).fetchall())
    if secs != dict(e["sections"]):
        raise SystemExit(f"ABORT — {e['id']} exists with different section content")
    return "applied"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    check_plan()
    conn = sqlite3.connect(DS_WIKI_DB)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    link_types = {r[0] for r in conn.execute("SELECT link_type FROM link_type_definitions")}
    tag_ids = dict(hc.execute("SELECT tag_path, id FROM source_domain_taxonomy WHERE superseded_by IS NULL"))

    plan_entries = [e for e in ENTRIES if entry_state(conn, e) == "absent"]
    plan_links = []
    for (src, tgt, lt, tier, desc) in LINKS:
        if lt not in link_types:
            raise SystemExit(f"ABORT — link type '{lt}' not in link_type_definitions")
        sl, tl = entry_label(conn, src), entry_label(conn, tgt)
        if not conn.execute("SELECT 1 FROM links WHERE source_id=? AND target_id=? AND link_type=?", (src, tgt, lt)).fetchone():
            plan_links.append((lt, src, sl, tgt, tl, desc, tier))
    plan_anchors = [x for x in ANCHORS if not hc.execute(
        "SELECT 1 FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND relationship=?",
        (x["entry_id"], x["source"], x["identifier"], x["relationship"])).fetchone()]
    plan_tags = []
    for (eid, tag, primacy, conf, why) in TAGS:
        if tag not in tag_ids:
            raise SystemExit(f"ABORT — unknown taxonomy tag {tag}")
        if not hc.execute("SELECT 1 FROM entry_source_domains WHERE entry_id=? AND tag_id=? AND review_status='current'",
                          (eid, tag_ids[tag])).fetchone():
            plan_tags.append((eid, tag_ids[tag], primacy, conf, why, tag))

    print(f"Plan: {len(plan_entries)}/{len(ENTRIES)} entries, {len(plan_links)}/{len(LINKS)} links, "
          f"{len(plan_anchors)}/{len(ANCHORS)} anchors, {len(plan_tags)}/{len(TAGS)} domain tags")
    for e in plan_entries:
        print(f"  + {e['id']:6s} {e['status']:11s} {e['confidence']:9s} {e['title']}")
    for l in plan_links:
        print(f"  link {l[1]} --{l[0]}--> {l[3]} (tier {l[6]})")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return

    try:
        for e in plan_entries:
            conn.execute("INSERT INTO entries (id, title, filename, entry_type, scale, domain, status, confidence, "
                         "type_group, authoring_status, formality_tier) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                         (e["id"], e["title"], e["filename"], "reference_law", e["scale"], e["domain"], e["status"],
                          e["confidence"], "RL", "", 2))
            for order, (name, content) in enumerate(e["sections"]):
                conn.execute("INSERT INTO sections (entry_id, section_name, section_order, content) VALUES (?,?,?,?)",
                             (e["id"], name, order, content))
            for tname, pname, pval, pord in e["properties"]:
                conn.execute("INSERT INTO entry_properties (entry_id, table_name, property_name, property_value, prop_order) "
                             "VALUES (?,?,?,?,?)", (e["id"], tname, pname, pval, pord))
        for (lt, src, sl, tgt, tl, desc, tier) in plan_links:
            conn.execute("INSERT INTO links (link_type, source_id, source_label, target_id, target_label, description, "
                         "link_order, confidence_tier) VALUES (?,?,?,?,?,?,0,?)", (lt, src, sl, tgt, tl, desc, tier))
        for x in plan_anchors:
            hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier,
                          source_stability_class, relationship, canonical_role, verified_date, verified_by_session,
                          confidence, notes) VALUES (?,?,?,NULL,?,?,?,?,?,?,?,?,?)""",
                       (x["entry_id"], x["source"], x["identifier"], x["title"], x["tier"], x["stability"],
                        x["relationship"], x.get("role"), D, AUDIT_REF, x["confidence"], x["notes"]))
        for (eid, tid, primacy, conf, why, _) in plan_tags:
            hc.execute("""INSERT INTO entry_source_domains (entry_id, tag_id, primacy, via_borrowing_id, assigned_date,
                          assigned_by_session, last_reviewed_date, last_reviewed_by_session, confidence, review_status,
                          rationale) VALUES (?,?,?,NULL,?,?,?,?,?,'current',?)""",
                       (eid, tid, primacy, D, AUDIT_REF, D, AUDIT_REF, conf, why))
        conn.commit(); hc.commit()
    except Exception:
        conn.rollback(); hc.rollback(); raise

    # Read-back verification
    bad = []
    for e in ENTRIES:
        if entry_state(conn, e) != "applied":
            bad.append(e["id"])
        n = conn.execute("SELECT COUNT(*) FROM entry_properties WHERE entry_id=?", (e["id"],)).fetchone()[0]
        if n != len(e["properties"]):
            bad.append(f"{e['id']} properties {n}")
    for (src, tgt, lt, tier, desc) in LINKS:
        if conn.execute("SELECT COUNT(*) FROM links WHERE source_id=? AND target_id=? AND link_type=?", (src, tgt, lt)).fetchone()[0] != 1:
            bad.append(f"link {src}->{tgt} {lt}")
    for x in ANCHORS:
        if hc.execute("SELECT COUNT(*) FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND relationship=?",
                      (x["entry_id"], x["source"], x["identifier"], x["relationship"])).fetchone()[0] != 1:
            bad.append(f"anchor {x['entry_id']} {x['identifier']}")
    for (eid, tag, primacy, conf, why) in TAGS:
        if hc.execute("SELECT COUNT(*) FROM entry_source_domains WHERE entry_id=? AND tag_id=? AND review_status='current'",
                      (eid, tag_ids[tag])).fetchone()[0] != 1:
            bad.append(f"tag {eid} {tag}")
    orphans = [r[0] for r in conn.execute(
        "SELECT id FROM entries WHERE type_group != 'GL'").fetchall()
        if not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id=?", (r[0],)).fetchone()
        and not hc.execute("SELECT 1 FROM internal_constructions WHERE entry_id=?", (r[0],)).fetchone()]
    if orphans:
        bad.append(f"orphans {orphans}")
    if bad:
        raise SystemExit(f"Post-write drift: {bad}")
    print("  verified (entries, properties, links, anchors, tags; 0 non-glossary orphans)")


if __name__ == "__main__":
    sys.exit(main())

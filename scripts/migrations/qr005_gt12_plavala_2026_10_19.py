"""
QR-005 gates follow-up — 2026-10-19 (audit_ref gsw-qr005-gates-2026-10-19). Mode A, owner-approved.

The QR-005 gate report (docs/prior_art_reviews/QR-005_GATES_2026_10_19.md §5) found that GT12
(gravitationally mediated entanglement) omits the indirect single-mass route of Plávala 2026
(PRD 113:085004), which the map had cited only for its timeline sentence. This adds a dated note
after GT12's "What It Claims" text (unchanged above it) and a `cites` anchor. No other writes.

Dry run by default; --apply writes. Idempotent: the note and anchor are checked for presence
first; a partial state aborts. Read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-qr005-gates-2026-10-19"
D = "2026-10-19"
CHECK = "No such experiment has been done."

NOTE = (
    f"\n\n> **ADDED {D} (`{AUDIT_REF}`).** An indirect route. Plávala 2026 (PRD 113:085004; arXiv:2508.03052 v4, full "
    "text read 2026-10-19) argues that today's matter-wave interferometers could establish gravity-mediated "
    "entanglement without the two-mass experiment. The steps: verify the Schrödinger equation for a *single* "
    "delocalised mass interacting gravitationally with an external mass; then entanglement between two delocalised "
    "masses follows, provided either (1) a ~20 g mass can be delocalised with negligible decoherence and the "
    "interaction is symmetric under exchanging the masses, or (2) the interaction depends only on the product m₁m₂ "
    "(related to the equivalence principle). Any non-entangling theory consistent with such a verification must break "
    "both assumptions. The argument also assumes a linear, positive time evolution, so it sets aside nonlinear dynamics "
    "such as Schrödinger–Newton (GT16), which he says can be ruled out separately. It has not been carried out as a decisive test, and the assumptions are open to "
    "dispute. Plávala himself says the main bottleneck is theory: what an observed entanglement would imply (see S3 "
    "of the QR-005 gates). *The text above is unchanged.*")

ANCHOR = dict(
    entry_id="GT12", source="doi", identifier="10.1103/87dc-qt73",
    title="Plávala 2026 - Existing experiments suffice to indirectly verify the quantum essence of gravity (PRD 113:085004; arXiv:2508.03052)",
    tier=1, stability="active-literature", relationship="cites", role=None, confidence="high",
    notes=("Indirect route to gravity-mediated entanglement via single-mass Schrödinger-equation verification, under "
           "one of two assumptions (20 g delocalisable with exchange symmetry; interaction depends only on m1m2). Read "
           "by this session 2026-10-19 (arXiv v4 full text: abstract, assumptions, conclusions). DOI verified on "
           "Crossref 2026-10-19 (published 2 Apr 2026). The QR-005 map cited only its timeline sentence."))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB); hc = sqlite3.connect(WIKI_HISTORY_DB)
    row = conn.execute("SELECT id, content FROM sections WHERE entry_id='GT12' AND section_name='What It Claims'").fetchone()
    if row is None:
        raise SystemExit("ABORT — GT12 What It Claims not found")
    sid, content = row
    note_done = NOTE in content
    if not note_done and AUDIT_REF in content:
        raise SystemExit("ABORT — partial state in GT12 What It Claims")
    if not note_done and CHECK not in content:
        raise SystemExit(f"ABORT — check string missing: {CHECK!r}")
    anc_done = hc.execute("SELECT 1 FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND relationship=?",
                          (ANCHOR["entry_id"], ANCHOR["source"], ANCHOR["identifier"], ANCHOR["relationship"])).fetchone()
    print(f"Plan: note {'already applied' if note_done else 'to add'}; anchor {'already present' if anc_done else 'to add'}")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    try:
        if not note_done:
            n = conn.execute("UPDATE sections SET content=? WHERE id=?", (content + NOTE, sid)).rowcount
            if n != 1: raise SystemExit(f"rowcount {n}")
        if not anc_done:
            x = ANCHOR
            hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier,
                          source_stability_class, relationship, canonical_role, verified_date, verified_by_session,
                          confidence, notes) VALUES (?,?,?,NULL,?,?,?,?,?,?,?,?,?)""",
                       (x["entry_id"], x["source"], x["identifier"], x["title"], x["tier"], x["stability"],
                        x["relationship"], x["role"], D, AUDIT_REF, x["confidence"], x["notes"]))
        conn.commit(); hc.commit()
    except BaseException:
        conn.rollback(); hc.rollback(); raise
    got = conn.execute("SELECT content FROM sections WHERE id=?", (sid,)).fetchone()[0]
    n_anc = hc.execute("SELECT COUNT(*) FROM external_anchors WHERE entry_id='GT12' AND identifier=?",
                       (ANCHOR["identifier"],)).fetchone()[0]
    if got.count(NOTE) != 1 or n_anc != 1:
        raise SystemExit(f"Post-write drift: note x{got.count(NOTE)}, anchor x{n_anc}")
    print("  verified: note present once; anchor present once")


if __name__ == "__main__":
    main()

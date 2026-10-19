"""
P5 anchor 100 DOI fix — 2026-10-19 (owner-approved). CLAUDE.md open item 13.

Anchor 100 (P5 → Transtrum et al. 2015) stores identifier 10.1063/1.4918623, which Crossref
resolves to Beechem, Yates & Graham, Rev. Sci. Instrum. 86:041101 (2015), an unrelated paper.
The correct DOI, 10.1063/1.4923066, resolves to Transtrum, Machta, Brown, Daniels, Myers & Sethna,
"Perspective: Sloppiness and emergent theories in physics, biology, and beyond", J. Chem. Phys.
143:010901 (both checked against Crossref 2026-10-19). The 2026-10-18 prior-art fold-in recorded the
error in the notes but left the identifier. This follows the QR-005 precedent for wrong anchors:
correct the identifier and record the original in the notes. No section text cites the wrong DOI.

Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DB = Path("data/wiki_history.db")
AID, EID = 100, "P5"
OLD, NEW = "10.1063/1.4918623", "10.1063/1.4923066"
AUDIT = "gsw-p5-anchor-doi-2026-10-19"
NOTE = (f" CORRECTION 2026-10-19 ({AUDIT}): identifier changed from {OLD} (Beechem, Yates & Graham, "
        f"Rev. Sci. Instrum. 86:041101, unrelated) to {NEW} (Transtrum et al. 2015, J. Chem. Phys. "
        f"143:010901); both checked against Crossref. Owner-approved.")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB)
    row = c.execute("SELECT entry_id, identifier, notes FROM external_anchors WHERE id=?", (AID,)).fetchone()
    if row is None or row[0] != EID:
        raise SystemExit(f"ABORT — unexpected row {row!r}")
    if AUDIT in (row[2] or ""):
        if row[1] != NEW:
            raise SystemExit(f"ABORT — note present but identifier is {row[1]!r}")
        print("  [anchor 100] OK — already applied"); return
    if row[1] != OLD:
        raise SystemExit(f"ABORT — identifier {row[1]!r}, expected {OLD!r}")
    if c.execute("SELECT 1 FROM external_anchors WHERE entry_id=? AND source='doi' AND identifier=? AND id<>?",
                 (EID, NEW, AID)).fetchone():
        raise SystemExit("ABORT — P5 already has an anchor with the correct DOI")
    print(f"  [anchor 100] plan — identifier {OLD} -> {NEW}; append note")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    n = c.execute("UPDATE external_anchors SET identifier=?, notes=? WHERE id=?",
                  (NEW, (row[2] or "") + NOTE, AID)).rowcount
    if n != 1:
        c.rollback(); raise SystemExit(f"rowcount {n}")
    c.commit()
    got = c.execute("SELECT identifier, notes FROM external_anchors WHERE id=?", (AID,)).fetchone()
    c.close()
    if got[0] != NEW or not got[1].endswith(NOTE):
        raise SystemExit("Post-write drift")
    print("  verified")


if __name__ == "__main__":
    main()

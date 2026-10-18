"""
STAT3 downgrade — 2026-10-18. Owner-approved follow-up to the CCA-1c λ₁ reduction test
(docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md).

STAT3 (Constrained Critical Attractor class) had no calibration before 2026-04-20; the
Phase E row raised it to Supported on the d_eff first-order discrimination alone. The
reduction test showed that discrimination is the Potts order-parameter jump read through
λ₁, and row 98 withdrew the strengthening with the label left for the owner. The owner
decided 2026-10-18: downgrade to Speculative.

Writes:
  1. wiki_history.db — one appended calibration row (STAT3 → Speculative).
  2. ds_wiki.db — a dated banner appended to STAT3 "What It Claims"; original text unchanged.

Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

WIKI = Path("data/ds_wiki.db")
HIST = Path("data/wiki_history.db")
AUDIT = "gsw-stat3-downgrade-2026-10-18"
DATE = "2026-10-18"
KEY = ("STAT3", "What It Claims")

SHORT = ("Speculative — descriptive classification; its only empirical support (Phase E d_eff "
         "discrimination) withdrawn as the order-parameter jump; 'novel framing' claim never gated, "
         "overlaps QR-002 and the SOC literature")
RATIONALE = (
    "Owner decision 2026-10-18, after the CCA-1c λ₁ reduction test. STAT3 had no calibration until the "
    "2026-04-20 Phase E row raised it to Supported on one basis: d_eff_CCA discriminating first-order from "
    "continuous Potts transitions. The reduction test (docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md) "
    "showed that discrimination is the Potts order-parameter discontinuity read through λ₁ ≈ N(q−1)⟨M²⟩; row 98 "
    "withdrew the strengthening and left the label to the owner. Remaining basis: none empirical. Further problems: "
    "(1) STAT3 is a definition — its own scope statement says membership predicts nothing — so Supported is the wrong "
    "kind of label; (2) internal tension: the class's point is that a constraint holds the system at criticality without "
    "tuning, yet ordinary critical stat mech, listed as 'the original and most general instance', reaches T_c only by "
    "tuning temperature; (3) members are weak — Riemann zeros rest on the conjectured Hilbert–Pólya operator, neural "
    "criticality is contested (the entry says so), BH horizons are conjectural; (4) the 'no prior literature unifies "
    "these systems' claim was never gated. 'No tuning needed' is the defining idea of self-organised criticality "
    "(Bak–Tang–Wiesenfeld 1987), and the living-systems half is QR-002's subject (Muñoz 2018; Mora & Bialek 2011) — "
    "QR-002's literature mapping doubles as STAT3's prior-art gate. (5) The 'FDS SV2/SV1' diagnostic in What The Math "
    "Says (1.000 continuous vs 0.374 Potts q=10) was not re-examined; whether it too reduces to the order parameter is "
    "untested. Pattern tags: post-hoc-feature-fit (five-feature checklist fitted to its listed members); support "
    "withdrawn by in-project test. Revertible by appending a later row."
)
SUFFIX = (
    "\n\n> **DOWNGRADED 2026-10-18 — Supported → Speculative (owner decision).** The only empirical support for this "
    "class, the 2026-04-20 Phase E finding that d_eff discriminates first-order Potts transitions, was shown on "
    "2026-10-18 to be the order-parameter jump read through the top eigenvalue λ₁ "
    "(`docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md`; CCA-1c is Retired — Folded). This entry is a "
    "classification, not a testable claim. Open issues: (1) ordinary critical stat mech is listed as the original "
    "instance, but it reaches criticality by tuning temperature, which sits uneasily with a class defined by the absence "
    "of tuning; (2) the \"Novel framing\" claim below has not been through the prior-art gate — \"no tuning needed\" is "
    "the defining idea of self-organised criticality (Bak–Tang–Wiesenfeld 1987), and the living-systems members are the "
    "subject of `docs/QUESTIONS_RAISED_LOG.md` QR-002, whose literature mapping is this entry's prior-art check; "
    "(3) the FDS SV2/SV1 diagnostic has not been checked for the same order-parameter reduction. Original text kept above."
)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    w = sqlite3.connect(WIKI); h = sqlite3.connect(HIST)

    cur = w.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", KEY).fetchone()[0]
    banner_done = cur.endswith(SUFFIX)
    if not banner_done and "Novel framing" not in cur:
        raise SystemExit("ABORT — expected STAT3 text not found")
    row = h.execute("SELECT confidence FROM confidence_calibration WHERE entity_id='STAT3' AND calibration_date=? "
                    "AND audit_ref=?", (DATE, AUDIT)).fetchone()
    if row and row[0] != "Speculative":
        raise SystemExit(f"ABORT — colliding row with confidence {row[0]}")
    print(f"  [STAT3 banner] {'OK — already applied' if banner_done else f'plan — append (+{len(SUFFIX)})'}")
    print(f"  [STAT3 calibration] {'OK — already applied' if row else 'plan — append Speculative row'}")
    if banner_done and row:
        return
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return

    if not banner_done:
        c = w.execute("UPDATE sections SET content=? WHERE entry_id=? AND section_name=?", (cur + SUFFIX, *KEY))
        if c.rowcount != 1:
            w.rollback(); raise SystemExit("rowcount")
        w.commit()
    if not row:
        h.execute("INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date, audit_ref, "
                  "short_status, rationale) VALUES ('STAT3','entry','Speculative',?,?,?,?)", (DATE, AUDIT, SHORT, RATIONALE))
        h.commit()

    ok1 = w.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", KEY).fetchone()[0].endswith(SUFFIX)
    ok2 = h.execute("SELECT confidence FROM claim_status_latest WHERE entity_id='STAT3'").fetchone()[0] == "Speculative"
    w.close(); h.close()
    if not (ok1 and ok2):
        raise SystemExit("Post-write drift")
    print("  verified (claim_status_latest: STAT3 = Speculative)")


if __name__ == "__main__":
    main()

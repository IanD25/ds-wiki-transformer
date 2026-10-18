r"""
CCA-1c λ₁ reduction test — 2026-10-18 (audit_ref gsw-cca1c-lambda1-reduction-2026-10-18). Mode B.

Report: docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md
Analysis: scripts/cca1c_lambda1_reduction.py → data/reports/cca1c_lambda1_reduction_2026_10/

Verdict (pre-registered rule, commit d00e5fe): REDUCES. tr χ = N(q−1) is fixed, so
1/d_eff = f₁² + (1−f₁)²/d_bulk exactly; f₁ = λ₁/Σλ ≈ ⟨M²⟩ carries ≥100% of the
first-order log-jump, and d_bulk (λ₁ removed) falls rather than jumps.

Writes:
- ds_wiki.db: gloss_phase_transition "Why this disambig exists" — dated qualifier inserted
  immediately after the Phase E sentence (single composed write; original text unchanged).
- calibration (append-only): CCA-1c Speculative → Retired (Folded); STAT3 label unchanged,
  correction to the Phase E "strengthened" rationale.

Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-cca1c-lambda1-reduction-2026-10-18"
D = "2026-10-18"
REPORT = "docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md"

SEC_ENTRY, SEC_NAME = "gloss_phase_transition", "Why this disambig exists"
ANCHOR_TEXT = "CCA experiments distinguish first-order from continuous via curve-shape signatures (Phase E 2026-04-20, Outcome C)."
QUALIFIER = (
    f" (Qualified {D}, `{AUDIT_REF}`: the participation-ratio part of that signature is the Potts order-parameter "
    "discontinuity read through the top eigenvalue of the correlation matrix, λ₁ ≈ N(q−1)⟨M²⟩ — a restatement of "
    f"textbook first-order behaviour, not a new signature; see `{REPORT}`.)"
)

CALIBRATIONS = [
    ("CCA-1c", "conjecture", "Retired", D, AUDIT_REF,
     "Folded: d_eff jump = Potts order-parameter discontinuity read through λ₁ = S(k=0) ≈ N(q−1)⟨M²⟩ (Wu 1982, RMP 54:235)",
     "λ₁ reduction test on the saved Phase E spectra (540 runs, no new MC), hypothesis and verdict rules pre-registered "
     "(commit d00e5fe) — " + REPORT + ". Identity: χ_ii = q−1, so Σλ = N(q−1) is fixed and 1/d_eff = f₁² + (1−f₁)²/d_bulk "
     "exactly (f₁ = λ₁/Σλ; d_bulk = participation ratio with λ₁ removed). Result, L=32, T/T_c 0.99→1.01: f₁ 0.64→0.17 (q=5), "
     "0.74→0.04 (q=7), 0.81→0.016 (q=10); f₁ = ⟨M²⟩ to <0.5% below T_c; d_full = 1/f₁² to <1% below T_c. Shapley share of "
     "Δln d_eff carried by f₁ = 1.00–1.05 in all 12 (q,L); d_bulk FALLS by 1.5–2.1× across T_c at every q including q=2, so "
     "with λ₁ removed there is no upward jump; D_bulk (≤4.6) < D_G (8.6–61) everywhere. Pre-registered verdict: REDUCES. "
     "Phase E's '9–400× beyond GTE' compares an order parameter with a non-order-parameter. The η_CCA part of outcome C "
     "(peak co-located with GTE, 9/9 first-order configs) is by Phase E's own account a re-expression of Brown 2022 (STAT6); "
     "a one-grid-step offset from the χ_mag peak is unresolved and no claim is made from it. Nothing distinctive to CCA "
     "remains, and the literature answers the question as CCA-1c did, so Folded (owner rule), not Falsified. Same-day "
     "init-state check: all q≥5 runs at 0.98–1.01 used half_half starts, so the jump is not a protocol switch. "
     "Pattern tags: restatement-in-new-vocabulary; answer-forced-by-definition. Supersedes the 2026-04-20 Phase E row's "
     "'positive discriminative evidence' reading. Revertible by appending a later row."),
    ("STAT3", "entry", "Supported", D, AUDIT_REF,
     "Correction, label unchanged: Phase E 'd_eff 9–400× beyond GTE' strengthening withdrawn — it is the order-parameter jump",
     "The 2026-04-20 Phase E row counted 'd_eff_CCA jump magnitudes exceed GTE by 9–400×' as strengthening STAT3 from "
     "descriptive-only to an empirically validated transition-order discriminator. The 2026-10-18 λ₁ reduction test "
     "(" + REPORT + ") shows that jump is the Potts order-parameter discontinuity read through λ₁ ≈ N(q−1)⟨M²⟩; the "
     "remaining spectrum does not jump. Any order-parameter measure discriminates first-order transitions this way, so "
     "this is not evidence for the CCA class framework. Strengthening withdrawn; whether Supported stands on STAT3's "
     "remaining basis is an owner decision, not made here."),
]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB)
    rows = conn.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (SEC_ENTRY, SEC_NAME)).fetchall()
    conn.close()
    if len(rows) != 1: raise SystemExit(f"[{SEC_ENTRY}] FAIL — {len(rows)} matching sections")
    cur_v = rows[0][0]
    if ANCHOR_TEXT + QUALIFIER in cur_v:
        new_v = None; print(f"  [{SEC_ENTRY}] OK — already applied")
    else:
        if cur_v.count(ANCHOR_TEXT) != 1: raise SystemExit(f"[{SEC_ENTRY}] FAIL — anchor count {cur_v.count(ANCHOR_TEXT)}")
        new_v = cur_v.replace(ANCHOR_TEXT, ANCHOR_TEXT + QUALIFIER, 1)
        print(f"  [{SEC_ENTRY}] plan — qualifier (+{len(QUALIFIER)} chars)")
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    cals = []
    for c in CALIBRATIONS:
        got = hc.execute("SELECT short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                         (c[0], c[3], c[4])).fetchone()
        if got is None:
            if not hc.execute("SELECT 1 FROM confidence_calibration WHERE entity_id=?", (c[0],)).fetchone():
                raise SystemExit(f"[cal {c[0]}] ABORT — no prior history")
            cals.append(c); print(f"  [cal {c[0]}] plan — {c[2]}: {c[5][:70]}")
        elif got[0] != c[5]:
            print(f"  [cal {c[0]}] COLLISION — slot held by a different row ({got[0][:60]!r}); NOT written")
        else:
            print(f"  [cal {c[0]}] OK — already present")
    hc.close()
    print(f"  {1 if new_v else 0} section write, {len(cals)} calibration rows")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    if new_v:
        conn = sqlite3.connect(DS_WIKI_DB)
        c = conn.execute("UPDATE sections SET content=? WHERE entry_id=? AND section_name=?", (new_v, SEC_ENTRY, SEC_NAME))
        if c.rowcount != 1: conn.rollback(); raise SystemExit("rowcount")
        conn.commit(); conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for c in cals:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date, audit_ref,
                      short_status, rationale) VALUES (?,?,?,?,?,?,?)""", c)
    hc.commit()
    bad = []
    if new_v:
        conn = sqlite3.connect(DS_WIKI_DB)
        if conn.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (SEC_ENTRY, SEC_NAME)).fetchone()[0] != new_v:
            bad.append(SEC_ENTRY)
        conn.close()
    for c in CALIBRATIONS:
        if hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                      (c[0], c[3], c[4])).fetchone() != (c[2], c[5]):
            bad.append(c[0])
    hc.close()
    if bad: raise SystemExit(f"Post-write drift: {bad}")
    print("  verified")


if __name__ == "__main__":
    main()

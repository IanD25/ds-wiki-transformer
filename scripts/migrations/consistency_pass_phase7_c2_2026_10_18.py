"""
Consistency pass, Phase 7 — podcast-origin error found in the wiki: C2's urban
"β = 1 ± 1/D_eff" — 2026-10-18 (audit_ref gsw-consistency-pass-2026-10-18).

The podcast's S2E1→S2E2 handoff gives P11 as "β = 1 ± 1/D_eff"; the same formula
sits in C2 (Urban Scaling) What's Conjectured, with "implied D_eff ≈ 8" (GDP,
β ≈ 1.126) and "≈ 4.8" (water pipes, β ≈ 0.79).

Problems (checked against Bettencourt 2013, Science 340:1438, full text):
- Bettencourt's theory already gives β = 1 + δ (socioeconomic) and 1 − δ
  (infrastructure) with δ = H/[D(D+H)] ≃ 1/6 for D = 2, H = 1 — predictions
  7/6 and 5/6. "1 ± 1/D_eff" re-expresses that form with a free D_eff.
- Each "implied D_eff" is obtained by inverting the formula on a single
  exponent — one parameter per data point, zero predictive content — the same
  operation retired from C1 on 2026-07-25.
- 4.8 for a physical pipe network embedded in two dimensions is not a
  geometric possibility if D_eff is a network dimension.
- It contradicts P11, which states the D/(D+1) form (bounded ≤ 1).

Writes: dated banner appended to C2 What's Conjectured (original kept);
anchor reframing_of Bettencourt 2013 on C2. No calibration row (C2 has no
calibration history; its entry label 'contested' is unchanged).
Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-consistency-pass-2026-10-18"
D = "2026-10-18"

SUFFIX = (
    f"\n\n> **CORRECTION {D} (`{AUDIT_REF}`).** The prediction \"β = 1 ± 1/D_eff\" and the implied D_eff values above do not stand. "
    "(1) **It restates Bettencourt 2013** (*Science* 340:1438): β = 1 + δ for socioeconomic outputs and 1 − δ for infrastructure, with "
    "δ = H/[D(D+H)] ≃ 1/6 for spatial dimension D = 2 and network fractal dimension H = 1 — predicted exponents 7/6 and 5/6. Writing δ as "
    "1/D_eff replaces a derived quantity with a free one. (2) **Each implied D_eff (≈ 8, ≈ 4.8) is obtained by inverting the formula on a "
    "single exponent** — one fitted parameter per data point, so no predictive content; this is the operation retired from C1 on 2026-07-25. "
    "(3) **4.8 is not a possible dimension for a pipe network embedded in two dimensions**, if D_eff is a network dimension. (4) **It "
    "contradicts P11**, which states the D/(D+1) form; that form is bounded above by 1 and cannot produce superlinear exponents at all. "
    "These values should not be used as evidence. Original text kept above per the no-deletions rule."
)

ANCHOR = ("C2", "doi", "10.1126/science.1235823",
          "Bettencourt 2013 - The origins of scaling in cities (Science 340:1438-1441)",
          1, "canonical", "reframing_of", "high",
          "C2's conjectured 'beta = 1 +/- 1/D_eff' re-expresses Bettencourt 2013's derived beta = 1 +/- delta, delta = H/[D(D+H)] ~ 1/6 "
          "(D = 2, H = 1; predictions 7/6 socioeconomic, 5/6 infrastructure) with a free D_eff. Verified against the full text 2026-10-18 "
          "(gsw-consistency-pass-2026-10-18). Pattern-tag: restatement-in-new-vocabulary.")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.execute("SELECT content FROM sections WHERE entry_id='C2' AND section_name=\"What's Conjectured\"").fetchone()[0]
    conn.close()
    need_text = not cur.endswith(SUFFIX)
    if need_text and "1 \\pm 1/D_{\\text{eff}}" not in cur:
        raise SystemExit("ABORT — expected formula not found in C2 What's Conjectured")
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    need_anchor = not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id='C2' AND identifier=? AND relationship=?",
                                 (ANCHOR[2], ANCHOR[6])).fetchone()
    hc.close()
    print(f"  C2 text: {'plan' if need_text else 'already applied'}; anchor: {'plan' if need_anchor else 'present'}")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    if need_text:
        conn = sqlite3.connect(DS_WIKI_DB)
        c = conn.execute("UPDATE sections SET content=? WHERE entry_id='C2' AND section_name=\"What's Conjectured\"", (cur + SUFFIX,))
        if c.rowcount != 1: conn.rollback(); raise SystemExit("rowcount")
        conn.commit(); conn.close()
    if need_anchor:
        hc = sqlite3.connect(WIKI_HISTORY_DB)
        (eid, src, ident, title, tier, stab, rel, conf, notes) = ANCHOR
        hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier, source_stability_class,
                      relationship, canonical_role, verified_date, verified_by_session, confidence, notes)
                      VALUES (?,?,?,NULL,?,?,?,?,NULL,?,?,?,?)""", (eid, src, ident, title, tier, stab, rel, D, AUDIT_REF, conf, notes))
        hc.commit(); hc.close()
    conn = sqlite3.connect(DS_WIKI_DB)
    ok = conn.execute("SELECT content FROM sections WHERE entry_id='C2' AND section_name=\"What's Conjectured\"").fetchone()[0].endswith(SUFFIX)
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    ok = ok and bool(hc.execute("SELECT 1 FROM external_anchors WHERE entry_id='C2' AND identifier=?", (ANCHOR[2],)).fetchone())
    hc.close()
    if not ok: raise SystemExit("Post-write drift")
    print("  verified")


if __name__ == "__main__":
    main()

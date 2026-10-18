"""
Prior-art fold-in, part 2 — close P2 (Folded), P8 and P11 (Falsified) — 2026-10-18
(audit_ref gsw-prior-art-fold-in-2026-10-18). Mode A. Owner decisions 2026-10-18.

Each of the three conjectures restates a literature result that is now a
reference_law entry (prior_art_fold_in_2026_10_18.py must be applied first):
  P2  -> BIO12  West, Brown & Enquist 1997 (a = D/(D+1))
  P8  -> STAT4  Gefen, Mandelbrot & Aharony 1980 (exponents on fractal lattices)
  P11 -> URB1   Bettencourt 2013 (urban exponents from D and H)

Writes, per conjecture:
  wiki_history.db  confidence_calibration: one append-only row —
                   P2: 'Retired', short_status 'Folded: answered by BIO12 (WBE 1997)'
                   P8, P11: 'Falsified', short_status 'Falsified by <source>: ...; phenomenon folded into <ID>'
                   (the literature they restated contradicts their specific form)
  ds_wiki.db       conjectures.three_state and conjecture_summary.status:
                   '<label> | was: <current value verbatim>'
                   conjectures.claim: dated banner prepended; the earlier banner and the
                   original claim are kept unchanged below it.

Safety: dry run by default; --apply writes. Before any write, the current claim,
three_state and status must match the SHA-256 fingerprints taken when this script
was written (2026-10-18) — otherwise someone else has edited them and the script
aborts. Applied markers are checked FIRST (banners quote the prior text, so a
find-string test alone would misfire on a re-run). Aborts on a UNIQUE collision in
confidence_calibration rather than skipping. Read-back verified.
"""
import argparse
import hashlib
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-prior-art-fold-in-2026-10-18"
D = "2026-10-18"
TAG = "[restatement-in-new-vocabulary]"
TAG_F = "[restatement-in-new-vocabulary; contradicted-by-restated-prior-art]"
MARK = f"> **CLOSED {D} (`{AUDIT_REF}`).**"

FOLDS = {
    "P2": dict(
        entry="BIO12", confidence="Retired", tag=TAG,
        fp=("5072c29f23f42d41", "26b1691cbf36fc6d", "86911a41affc3e55"),
        short="Folded: answered by BIO12 (WBE 1997, Science 276:122) — a = D/(D+1) is WBE's",
        banner=(
            f"{MARK} Closed as **Folded: answered by BIO12** — West, Brown & Enquist 1997, *Science* 276:122 "
            "(doi:10.1126/science.276.5309.122), now a reference entry. The form α = D_eff/(D_eff+1) is WBE's own: \"Because "
            "the fractal network must still fill the entire D-dimensional volume, our result generalizes to a = D/(D + 1)\" "
            "(p. 126; restated in WBE 1999, *Science* 284:1677). In WBE, D is the dimension of the space the network fills "
            "(three for organisms), not a measured property of the vascular tree. P2's only addition — reading D as an "
            "independently measured vascular D_eff — is an untested reinterpretation with no data path "
            f"{TAG}. WBE's own status is contested (finite-size corrections, no universal 3/4; see BIO12, C1). "
            "*The earlier status banner and the claim as originally stated follow, unchanged.*"),
        rationale=(
            "P2's alpha = D_eff/(D_eff+1) is West-Brown-Enquist's a = D/(D+1) (WBE 1997 p. 126; WBE 1999 Science 284:1677; both checked "
            "first-hand 2026-10-18). In WBE, D is the dimension of the volume the network fills (D = 3 for organisms: 'which explains the "
            "3 in the numerator'); P2 renames it D_eff and reads it as a measured vascular dimension. That reinterpretation is the only "
            "content not already in WBE, and it has no data (micro-CT gap, M0). The question P2 poses is answered in the literature, so the "
            "conjecture is retired as Folded, not Falsified. WBE itself is contested as the explanation of metabolic scaling (BIO12). "
            "Pattern tags: restatement-in-new-vocabulary; untestable-without-owner-data."),
    ),
    "P8": dict(
        entry="STAT4", confidence="Falsified", tag=TAG_F,
        fp=("d1b0a6247d87e01d", "a23574ac59ed9f30", "4d5e8e188a668d39"),
        short=("Falsified by Gefen–Mandelbrot–Aharony 1980: critical behaviour depends on topology as well as dimension; "
               "phenomenon folded into STAT4"),
        banner=(
            f"{MARK} Closed as **Falsified by Gefen–Mandelbrot–Aharony 1980** (*PRL* 45:855, doi:10.1103/PhysRevLett.45.855), "
            "the work this conjecture restated, now reference entry STAT4. The question — how critical exponents behave on "
            "substrates of non-integer dimension — was answered in 1980, and the answer contradicts P8: the critical "
            "properties vary with D \"but also with several topological factors: ramification, connectivity, lacunarity\". "
            "Same D, different exponents (Koch curve y = D; Sierpiński gasket y = 0); different D, same exponent (branching "
            "Koch curves, y = ln2/ln3). So exponents are not a function of D_eff alone, and 'uniquely predicted by Fisher "
            "Rank' adds no prediction. The gasket named in *would_confirm* is finitely ramified and has T_c = 0, so it has "
            f"no exponents to interpolate {TAG_F}. **Correction:** the M0 attribution to Janke, Johnston & Kenna 2004 of "
            "'FIM distinguishes transition order' is unsupported — that paper never discusses first-order versus continuous "
            "transitions (see IT10). The Phase 2 results below stay as recorded; their order-discrimination question belongs "
            "to CCA-1c, whose prior art is STAT6. *The earlier status banner and the claim as originally stated follow, unchanged.*"),
        rationale=(
            "P8 claims critical exponents interpolate continuously as a function of non-integer D_eff, uniquely predicted by Fisher Rank. "
            "Gefen-Mandelbrot-Aharony 1980 (full text, checked first-hand 2026-10-18), the result P8 restated, contradicts it: exponents and "
            "T_c depend on fractal dimension AND on ramification, connectivity and lacunarity; finitely ramified lattices (e.g. the Sierpinski "
            "gasket named in P8's would_confirm) have T_c = 0; the same D gives different exponents and different D the same exponent. Fisher "
            "Rank contributes no prediction. Phenomenon folded into STAT4. Correction recorded: Janke-Johnston-Kenna 2004 (IT10) never "
            "addresses first-order vs continuous transitions; the M0 short_status 'Rediscovery of JJK-style FIM-distinguishes-order' "
            "misattributes. Pattern tags: restatement-in-new-vocabulary; contradicted-by-restated-prior-art."),
    ),
    "P11": dict(
        entry="URB1", confidence="Falsified", tag=TAG_F,
        fp=("4c441909cd885820", "e47c934e6b073de4", "7487b876f172c843"),
        short=("Falsified by Bettencourt 2013: δ = H/[D(D+H)], not D/(D+1), which cannot exceed 1; "
               "phenomenon folded into URB1"),
        banner=(
            f"{MARK} Closed as **Falsified by Bettencourt 2013** (*Science* 340:1438, doi:10.1126/science.1235823), the "
            "theory this conjecture restated, now reference entry URB1. The question — do urban scaling exponents follow from "
            "the dimension of the city's networks? — is answered there, and the answer contradicts P11's form: socioeconomic "
            "rates scale as N^{1+δ} and infrastructure volume as N^{1−δ}, with δ = H/[D(D+H)] ≃ 1/6 for spatial dimension "
            "D = 2 and path dimension H = 1 (7/6 and 5/6). P11's D/(D+1) form cannot exceed 1, so it cannot express the "
            f"superlinear half (also noted 2026-07-25) {TAG_F}. The empirical regularity is Bettencourt et al. 2007; "
            "Bettencourt's exponents are themselves contested empirically (boundary definitions, fluctuation models; see URB1). "
            "*The earlier status banner and the claim as originally stated follow, unchanged.*"),
        rationale=(
            "P11 claims urban scaling exponents track network dimension via the same D/(D+1) form as metabolic scaling. Bettencourt 2013 "
            "(full text and SM, checked first-hand 2026-10-18), the theory P11 restated, derives the exponents from spatial dimension D and "
            "path fractal dimension H: beta = 1 + delta (7/6), network volume 1 - delta (5/6), land area D/(D+H) (2/3), delta = H/[D(D+H)]. "
            "P11's D/(D+1) form differs and is bounded <= 1 (gsw-scaling-corrections, 2026-07-25), so it cannot produce the superlinear "
            "exponents the theory explains and observation shows (GMP beta = 1.126 +/- 0.023). Phenomenon folded into URB1. Empirical "
            "regularity: Bettencourt et al. 2007 (already anchored). Pattern tags: restatement-in-new-vocabulary; "
            "contradicted-by-restated-prior-art; over-extension-beyond-formula-range."),
    ),
}


def h(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def label(f):
    return f"{f['short']} {f['tag']} ({AUDIT_REF})"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB); hc = sqlite3.connect(WIKI_HISTORY_DB)
    plan = []
    for pid, f in FOLDS.items():
        if not conn.execute("SELECT 1 FROM entries WHERE id=?", (f["entry"],)).fetchone():
            raise SystemExit(f"ABORT — {f['entry']} not in entries; apply prior_art_fold_in_2026_10_18.py first")
        claim, ts = conn.execute("SELECT claim, three_state FROM conjectures WHERE id=?", (pid,)).fetchone()
        st = conn.execute("SELECT status FROM conjecture_summary WHERE id=?", (pid,)).fetchone()[0]
        lab = label(f)
        # applied markers first
        done_claim = claim.startswith(MARK)
        done_ts = ts.startswith(lab + " | was: ")
        done_st = st.startswith(lab + " | was: ")
        row = hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                         (pid, D, AUDIT_REF)).fetchone()
        if row and row != (f["confidence"], f["short"]):
            raise SystemExit(f"ABORT — UNIQUE collision on ({pid}, {D}, {AUDIT_REF}) with a different row: {row}")
        done_cal = row is not None
        # unapplied fields must match the fingerprints taken at authoring time
        for done, cur, fp, name in ((done_claim, claim, f["fp"][0], "claim"), (done_ts, ts, f["fp"][1], "three_state"),
                                    (done_st, st, f["fp"][2], "summary status")):
            if not done and h(cur) != fp:
                raise SystemExit(f"ABORT — {pid} {name} changed since this script was written (fingerprint {h(cur)} != {fp})")
        plan.append((pid, f, claim, ts, st, lab, done_claim, done_ts, done_st, done_cal))
        print(f"  {pid}: claim {'applied' if done_claim else 'plan'}; three_state {'applied' if done_ts else 'plan'}; "
              f"summary {'applied' if done_st else 'plan'}; calibration {'present' if done_cal else 'plan'}")
        print(f"        -> {lab}")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    try:
        for (pid, f, claim, ts, st, lab, dc, dt, ds, dcal) in plan:
            if not dc:
                n = conn.execute("UPDATE conjectures SET claim=? WHERE id=?", (f["banner"] + "\n\n" + claim, pid)).rowcount
                if n != 1: raise RuntimeError(f"{pid} claim rowcount {n}")
            if not dt:
                n = conn.execute("UPDATE conjectures SET three_state=? WHERE id=?", (f"{lab} | was: {ts}", pid)).rowcount
                if n != 1: raise RuntimeError(f"{pid} three_state rowcount {n}")
            if not ds:
                n = conn.execute("UPDATE conjecture_summary SET status=? WHERE id=?", (f"{lab} | was: {st}", pid)).rowcount
                if n != 1: raise RuntimeError(f"{pid} summary rowcount {n}")
            if not dcal:
                hc.execute("INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date, audit_ref, "
                           "short_status, rationale) VALUES (?,?,?,?,?,?,?)",
                           (pid, "conjecture", f["confidence"], D, AUDIT_REF, f["short"], f["rationale"]))
        conn.commit(); hc.commit()
    except Exception:
        conn.rollback(); hc.rollback(); raise
    # read-back
    for (pid, f, claim, ts, st, lab, dc, dt, ds, _) in plan:
        c2, t2 = conn.execute("SELECT claim, three_state FROM conjectures WHERE id=?", (pid,)).fetchone()
        s2 = conn.execute("SELECT status FROM conjecture_summary WHERE id=?", (pid,)).fetchone()[0]
        ok = (c2.startswith(f["banner"] + "\n\n") and (dc or c2 == f["banner"] + "\n\n" + claim)
              and (dt or t2 == f"{lab} | was: {ts}") and (ds or s2 == f"{lab} | was: {st}")
              and t2.startswith(lab + " | was: ") and s2.startswith(lab + " | was: "))
        latest = hc.execute("SELECT confidence, audit_ref FROM claim_status_latest WHERE entity_id=?", (pid,)).fetchone()
        if not ok or latest != (f["confidence"], AUDIT_REF):
            raise SystemExit(f"Post-write drift on {pid}: text ok={ok}, latest={latest}")
    print("  verified (banners, labels, calibration rows; claim_status_latest shows Retired / Falsified as planned)")


if __name__ == "__main__":
    main()

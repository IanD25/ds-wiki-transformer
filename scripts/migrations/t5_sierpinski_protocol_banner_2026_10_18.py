"""
T5 protocol banner — 2026-10-18. Follow-up to the prior-art fold-in report
(docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md, §5 item 1), owner-approved.

T5 ("Critical Exponent–Dimension Sensitivity") plans to measure Ising critical
exponents on the Sierpiński gasket. The gasket is finitely ramified, so Ising on
it has T_c = 0 (ν = ∞; Gefen, Mandelbrot & Aharony 1980, Eq. 1): there is no
finite-temperature transition to measure. Infinitely ramified fractals (carpet,
Menger sponge) do order at T_c > 0, but there critical behaviour depends on
topology as well as dimension. A dated banner is appended to T5 "What It Does";
original text unchanged. No calibration row (T5 has no calibration history and
its label does not change).

Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DB = Path("data/ds_wiki.db")
KEY = ("T5", "What It Does")
SUFFIX = (
    "\n\n> **CORRECTION 2026-10-18 (follow-up to `docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md` §5).** "
    "This protocol is ill-posed as written for the Sierpiński gasket. The gasket is finitely ramified, so the Ising model on "
    "it has T_c = 0 (ν = ∞; Gefen, Mandelbrot & Aharony 1980 — see STAT4): there is no finite-temperature transition whose "
    "exponents could be measured. Infinitely ramified fractals such as the Sierpiński carpet and the Menger sponge do order at "
    "T_c > 0, but on them critical behaviour depends on topology (ramification, connectivity, lacunarity) as well as on "
    "dimension, so exponents are not a function of D_eff alone and cannot test a D_eff-only interpolation. P8, which this "
    "protocol tests, was closed as Falsified on 2026-10-18 for the same reason. Original text kept above."
)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DB)
    cur = conn.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", KEY).fetchone()[0]
    if cur.endswith(SUFFIX):
        print("  [T5] OK — already applied"); conn.close(); return
    if "Sierpinski gasket" not in cur:
        conn.close(); raise SystemExit("ABORT — expected protocol text not found")
    print(f"  [T5] plan — append banner (+{len(SUFFIX)})")
    if not a.apply:
        conn.close(); print("DRY RUN — nothing written. Re-run with --apply."); return
    c = conn.execute("UPDATE sections SET content=? WHERE entry_id=? AND section_name=?", (cur + SUFFIX, *KEY))
    if c.rowcount != 1:
        conn.rollback(); conn.close(); raise SystemExit("rowcount")
    conn.commit()
    ok = conn.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", KEY).fetchone()[0].endswith(SUFFIX)
    conn.close()
    if not ok: raise SystemExit("Post-write drift")
    print("  verified")


if __name__ == "__main__":
    main()

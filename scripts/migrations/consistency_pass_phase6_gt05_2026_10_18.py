"""
Consistency pass, Phase 6 — resolve the GT05 provenance orphan — 2026-10-18
(audit_ref gsw-consistency-pass-2026-10-18). Mode A: corrections only.

GT05 (Carney Spin Entropic Gravity) had neither an external anchor nor an
internal_construction flag — the only non-glossary orphan. Its cited source was
checked against the full text (arXiv:2502.17575 HTML, read 2026-10-18):

  Carney, Karydas, Scharnhorst, Singh & Taylor 2025, "On the Quantum Mechanics
  of Entropic Forces", Phys. Rev. X 15, 031038, doi:10.1103/y7sy-3by1
  (open access).

The source exists and is the right paper, but GT05 misdescribes it:
  - five authors, not "Carney" alone;
  - the force comes from extremising the FREE ENERGY of a thermalised bath of
    qubits or oscillators (local model: one qubit per site of a 3D lattice),
    NOT from entanglement entropy of a spin network;
  - the noise prediction is a zero-frequency force-noise coefficient S_FF(0)
    (Brownian momentum diffusion from a Lindblad evolution), not S_FF(ω) ∝ ω^-α;
  - the paper reports that existing atom-interferometer decoherence results
    already rule out the non-local model at λ = 0, and fifth-force tests
    exclude lattice spacings a ≳ 1 mm; minimum force noise for mg masses at mm
    separation is "nearly observable" with modern force sensors. No
    "within an order of magnitude" claim was found in the portion read.
The same entanglement misreading propagated to BR01 (ER = EPR cross-reference)
and to links GT05→GT02 and GT05→IT02.

Writes: canonical_authority anchor (progenitor) for GT05; correction banner
prepended to GT05 What It Claims; pointer notes appended to four other GT05
sections and to BR01 DS Cross-References; link descriptions corrected with the
previous text kept. No calibration row: GT05 and BR01's labels do not change
(BR01's latest row concerns ER = EPR, not Carney) and GT05 has no calibration
history.

Dry run by default; --apply writes. Duplicate-target abort; idempotent;
read-back verification.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-consistency-pass-2026-10-18"
D = "2026-10-18"
CITE = ("Carney, Karydas, Scharnhorst, Singh & Taylor 2025, \"On the Quantum Mechanics of Entropic Forces\", "
        "*Phys. Rev. X* 15, 031038 (doi:10.1103/y7sy-3by1; arXiv:2502.17575)")
PTR = (f"\n\n[Corrected {D}, {AUDIT_REF}: the source paper derives the force from the free energy of a thermal qubit/oscillator "
       "bath, not from entanglement entropy of a spin network, and predicts a zero-frequency force-noise level S_FF(0), not an "
       "ω^-α spectrum. See the correction banner in What It Claims.]")

# (label, table, key, column, prefix, suffix)
EDITS = [
    ("GT05.claims", "sections", {"entry_id": "GT05", "section_name": "What It Claims"}, "content",
     f"> **CORRECTION — added {D} (`{AUDIT_REF}`), checked against the full text.** Source: {CITE}. "
     "This entry misdescribes the paper in four ways. (1) It has five authors, not 'Carney' alone. (2) The force comes from "
     "extremising the **free energy of a thermalised bath of qubits or oscillators** — in the local model one qubit per site of a "
     "3D lattice, with frequencies set by the nearby masses — not from the **entanglement** entropy of a spin network; the paper "
     "does not attribute the force to entanglement. Newton's 1/r² law is recovered in the thermodynamic (many-qubit) limit, exactly "
     "for the non-local model and at separations much larger than the lattice spacing for the local one. (3) The noise prediction "
     "is a **zero-frequency force-noise coefficient S_FF(0)** — Brownian momentum diffusion from a Lindblad (open-system) evolution — "
     "not a power-law S_FF(ω) ∝ ω^-α. The models are distinguished from perturbative quantum gravity, which is unitary and noiseless, "
     "by force noise, decoherence of spatial superpositions, gravitationally-mediated-entanglement witnesses, anomalous heating of "
     "cryogenic masses, and fifth-force bounds. (4) Omitted: the authors report that **existing atom-interferometer decoherence results "
     "already rule out the non-local model at λ = 0**, and fifth-force tests exclude lattice spacings a ≳ 1 mm; the minimum force noise "
     "for mg-scale masses at mm separation is 'nearly observable' with modern force sensors. Statements below that follow from the "
     "entanglement reading — the ER = EPR connection (BR01) and the von Neumann / reduced-density-matrix reading (IT02) — are not "
     "supported by the paper. *Original text follows, unchanged.*\n\n",
     ""),
    ("GT05.math_form", "sections", {"entry_id": "GT05", "section_name": "Mathematical Form"}, "content", "", PTR),
    ("GT05.math_says", "sections", {"entry_id": "GT05", "section_name": "What The Math Says"}, "content", "", PTR),
    ("GT05.constraint", "sections", {"entry_id": "GT05", "section_name": "Constraint Category"}, "content", "", PTR),
    ("GT05.archetype", "sections", {"entry_id": "GT05", "section_name": "Mathematical Archetype"}, "content", "", PTR),
    ("GT05.xrefs", "sections", {"entry_id": "GT05", "section_name": "DS Cross-References"}, "content", "",
     PTR[:-1] + " The BR01 (ER = EPR) and IT02 (von Neumann entropy of a reduced density matrix) links rest on the entanglement reading and do not follow from the paper.]"),
    ("BR01.xrefs", "sections", {"entry_id": "BR01", "section_name": "DS Cross-References"}, "content", "",
     f"\n\n[Corrected {D}, {AUDIT_REF}: the GT05 cross-reference above (\"Carney's spin entanglement mediating gravity is a "
     "microscopic realisation of ER = EPR\") does not hold — Carney et al. 2025 derive the force from the free energy of a thermal "
     "qubit/oscillator bath, not from entanglement. See GT05.]"),
]

LINK_FIXES = [  # (source_id, target_id, corrected-prefix)
    ("GT05", "GT02",
     f"[Corrected {D}, {AUDIT_REF}] Carney et al. 2025 give microscopic models realising entropic gravity — the force comes from "
     "extremising the free energy of a thermal qubit/oscillator bath, not from entanglement entropy. Previously: \""),
    ("GT05", "IT02",
     f"[Corrected {D}, {AUDIT_REF}] Weak link: the entropy in Carney et al. 2025 is the thermal entropy of a qubit/oscillator "
     "bath in a free-energy extremisation, not the entanglement (reduced-density-matrix) entropy of a spin system. Previously: \""),
]

ANCHOR = ("GT05", "doi", "10.1103/y7sy-3by1", None,
          "Carney, Karydas, Scharnhorst, Singh, Taylor 2025 - On the Quantum Mechanics of Entropic Forces (PRX 15, 031038; arXiv:2502.17575)",
          1, "active-literature", "canonical_authority", "progenitor", "high",
          "Primary source for GT05, verified against the full text 2026-10-18 (gsw-consistency-pass-2026-10-18). Resolves GT05's orphan "
          "status (no anchor, no internal_construction). The citation is right but GT05 misdescribed the paper: the mechanism is "
          "free-energy extremisation of a thermal qubit/oscillator bath, not spin-network entanglement entropy; the noise prediction is "
          "S_FF(0), not an omega^-alpha spectrum; existing atom-interferometer decoherence results already exclude the non-local "
          "lambda = 0 model. Corrections recorded in GT05, BR01 and links GT05->GT02, GT05->IT02.")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    ops, seen = [], set()
    for label, table, key, col, prefix, suffix in EDITS:
        t = (table, tuple(sorted(key.items())), col)
        if t in seen: raise SystemExit(f"[{label}] ABORT — duplicate target {t}")
        seen.add(t)
        w = " AND ".join(f"{k}=?" for k in key)
        row = cur.execute(f"SELECT {col} FROM {table} WHERE {w}", tuple(key.values())).fetchone()
        if row is None: raise SystemExit(f"[{label}] ABORT — row not found")
        cv = row[0] or ""
        if (not prefix or cv.startswith(prefix)) and (not suffix or cv.endswith(suffix)):
            print(f"  [{label}] OK — already applied"); continue
        ops.append((label, table, key, col, prefix + cv + suffix)); print(f"  [{label}] plan")
    link_ops = []
    for s, tgt, pre in LINK_FIXES:
        rows = cur.execute("SELECT id, description FROM links WHERE source_id=? AND target_id=?", (s, tgt)).fetchall()
        if len(rows) != 1: raise SystemExit(f"[link {s}->{tgt}] ABORT — {len(rows)} rows")
        lid, desc = rows[0]
        if desc.startswith(pre): print(f"  [link {s}->{tgt}] OK — already applied"); continue
        if ("links", lid, "description") in seen: raise SystemExit("duplicate link target")
        seen.add(("links", lid, "description"))
        link_ops.append((lid, pre + desc + "\"")); print(f"  [link {s}->{tgt} id={lid}] plan")
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    need_anchor = not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id=? AND identifier=? AND relationship=?",
                                 (ANCHOR[0], ANCHOR[2], ANCHOR[7])).fetchone()
    hc.close()
    print(f"\n  {len(ops)} section writes, {len(link_ops)} link writes, anchor {'planned' if need_anchor else 'present'}")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return

    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    for label, table, key, col, new in ops:
        w = " AND ".join(f"{k}=?" for k in key)
        cur.execute(f"UPDATE {table} SET {col}=? WHERE {w}", (new, *key.values()))
        if cur.rowcount != 1: conn.rollback(); raise SystemExit(f"[{label}] rowcount {cur.rowcount}")
    for lid, new in link_ops:
        cur.execute("UPDATE links SET description=? WHERE id=?", (new, lid))
        if cur.rowcount != 1: conn.rollback(); raise SystemExit(f"[link {lid}] rowcount {cur.rowcount}")
    conn.commit()
    if need_anchor:
        hc = sqlite3.connect(WIKI_HISTORY_DB)
        (eid, src, ident, rev, title, tier, stab, rel, role, conf, notes) = ANCHOR
        hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier,
                      source_stability_class, relationship, canonical_role, verified_date, verified_by_session,
                      confidence, notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (eid, src, ident, rev, title, tier, stab, rel, role, D, AUDIT_REF, conf, notes))
        hc.commit(); hc.close()
    bad = []
    for label, table, key, col, new in ops:
        w = " AND ".join(f"{k}=?" for k in key)
        if cur.execute(f"SELECT {col} FROM {table} WHERE {w}", tuple(key.values())).fetchone()[0] != new: bad.append(label)
    for lid, new in link_ops:
        if cur.execute("SELECT description FROM links WHERE id=?", (lid,)).fetchone()[0] != new: bad.append(f"link{lid}")
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    if not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id='GT05' AND identifier=?", (ANCHOR[2],)).fetchone(): bad.append("anchor")
    hc.close()
    if bad: raise SystemExit(f"Post-write drift: {bad}")
    print("  verified")


if __name__ == "__main__":
    main()

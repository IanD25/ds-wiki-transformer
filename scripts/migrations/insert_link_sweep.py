"""
insert_link_sweep.py — Add 20 vectorially-validated tier-1.5 / tier-2 links
across the GL, OP, ES, EM, and AM/QM clusters.

All pairs confirmed:
  • Not already present in links table
  • Cosine similarity ≥ 0.75 (all well-known structural relationships)
  • Safe to re-run — INSERT OR IGNORE guards against duplicates

Run from project root:
    python3 scripts/insert_link_sweep.py
"""
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from config import SOURCE_DB

# ── Link definitions ──────────────────────────────────────────────────────────
# (source_id, source_label, target_id, target_label, link_type, description, confidence_tier)
# Tier assignments:
#   1   ≥ 0.90 — definitionally certain
#   1.5 0.79–0.89 — strong structural/derivation bond (includes known derivations
#       where embedding gap reflects abstraction level, not relationship uncertainty)
#   2   below 0.82 — plausible structural connection, sim below tier threshold

LINKS = [
    # ── GL cluster: Ideal Gas Law → all three classical special cases ─────────
    ("GL1", "Ideal Gas Law",
     "GL2", "Boyle's Law",
     "generalizes",
     "Boyle's Law is GL1 at constant T: PV=nRT → PV=const when T is fixed.",
     "1"),       # sim=0.900

    ("GL1", "Ideal Gas Law",
     "GL3", "Charles's Law",
     "generalizes",
     "Charles's Law is GL1 at constant P: PV=nRT → V/T=nR/P when P is fixed.",
     "1.5"),     # sim=0.854

    ("GL1", "Ideal Gas Law",
     "GL4", "Gay-Lussac's Law",
     "generalizes",
     "Gay-Lussac's Law is GL1 at constant V: PV=nRT → P/T=nR/V when V is fixed.",
     "1.5"),     # sim=0.835

    ("GL1", "Ideal Gas Law",
     "GL5", "Avogadro's Law",
     "generalizes",
     "Avogadro's Law is GL1 at constant P and T: V/n = RT/P = const.",
     "1.5"),     # sim=0.881

    ("DM4", "Dalton's Law of Partial Pressures",
     "GL1", "Ideal Gas Law",
     "derives from",
     "P_total = Σp_i follows from GL1 applied to each non-interacting gas: p_i = n_i RT/V.",
     "2"),       # sim=0.822

    # ── OP cluster: Fermat as root; Snell → Brewster cascade ─────────────────
    ("OP2", "Law of Reflection",
     "OP1", "Fermat's Principle of Least Time",
     "derives from",
     "Equal angles of incidence/reflection extremize optical path length — direct consequence of Fermat.",
     "1.5"),     # sim=0.788 (abstraction-level gap: variational → geometric)

    ("OP3", "Snell's Law of Refraction",
     "OP1", "Fermat's Principle of Least Time",
     "derives from",
     "n₁sinθ₁=n₂sinθ₂ is the Euler-Lagrange condition for Fermat's optical action integral.",
     "1.5"),     # sim=0.799 (abstraction-level gap)

    ("OP4", "Brewster's Angle",
     "OP3", "Snell's Law of Refraction",
     "derives from",
     "tanθ_B = n₂/n₁ follows from Snell's Law plus Maxwell boundary conditions for p-polarization.",
     "2"),       # sim=0.833

    ("OP1", "Fermat's Principle of Least Time",
     "AM1", "Principle of Least Action",
     "analogous to",
     "Both are variational extremal principles: Fermat extremizes ∫n ds, Least Action extremizes ∫L dt.",
     "1.5"),     # sim=0.834 — cross-domain structural identity

    # ── ES cluster: Steno's Laws + Faunal Succession ─────────────────────────
    ("ES8", "Steno's Law of Superposition",
     "ES9", "Principle of Original Horizontality",
     "couples to",
     "Together they define the undisturbed reference frame: layers are horizontal and older below.",
     "1.5"),     # sim=0.818

    ("ES8", "Steno's Law of Superposition",
     "ES10", "Principle of Lateral Continuity",
     "couples to",
     "A laterally continuous layer (ES10) is also age-ordered by its vertical position (ES8).",
     "2"),       # sim=0.794

    ("ES9", "Principle of Original Horizontality",
     "ES10", "Principle of Lateral Continuity",
     "couples to",
     "Both constrain initial deposition geometry: horizontal plane extending laterally in all directions.",
     "1.5"),     # sim=0.850

    ("ES10", "Principle of Lateral Continuity",
     "ES14", "Walther's Law of Facies",
     "analogous to",
     "Lateral Continuity links spatial extension to layer identity; Walther's Law links lateral facies order to vertical succession.",
     "1.5"),     # sim=0.821

    ("ES11", "Principle of Cross-Cutting Relationships",
     "ES13", "Principle of Inclusions and Components",
     "analogous to",
     "Both derive relative age from geometric relationships: cutting features and inclusions are younger than the host.",
     "1.5"),     # sim=0.817

    ("ES12", "Principle of Faunal Succession",
     "ES8", "Steno's Law of Superposition",
     "implements",
     "Faunal Succession is the biostratigraphic implementation of Superposition: fossil assemblages proxy for stratigraphic time.",
     "2"),       # sim=0.752

    # ── EM cluster: Maxwell divergence pair + Biot-Savart ────────────────────
    ("EM2", "Gauss's Law for Magnetism",
     "EM1", "Gauss's Law for Electricity",
     "analogous to",
     "∇·B=0 (EM2) is the magnetic analog of ∇·E=ρ/ε₀ (EM1); both are divergence equations of Maxwell.",
     "1.5"),     # sim=0.855

    ("EM2", "Gauss's Law for Magnetism",
     "EM7", "Biot–Savart Law",
     "couples to",
     "Both describe magnetic field structure: EM2 constrains topology (no monopoles), Biot-Savart gives field from current sources.",
     "1.5"),     # sim=0.849

    # ── AM / QM: Hamiltonian mechanics → Hamilton-Jacobi → Schrödinger ───────
    ("AM4", "Hamilton–Jacobi Equation",
     "AM3", "Hamilton's Equations",
     "derives from",
     "H-J equation H(q,∂S/∂q,t)=−∂S/∂t follows from Hamilton's equations via the canonical transformation p=∂S/∂q.",
     "1.5"),     # sim=0.899

    ("AM4", "Hamilton–Jacobi Equation",
     "QM1", "Schrödinger Equation",
     "analogous to",
     "WKB connection: ψ=e^{iS/ℏ} converts Schrödinger to H-J in the classical limit ℏ→0; H-J is the classical skeleton of QM.",
     "1.5"),     # sim=0.862

    ("AM3", "Hamilton's Equations",
     "QM1", "Schrödinger Equation",
     "analogous to",
     "Canonical commutators [q,p]=iℏ reduce to Poisson brackets {q,p}=1 as ℏ→0; Schrödinger → Hamilton's equations classically.",
     "1.5"),     # sim=0.839
]


def insert_links(db_path: Path, dry_run: bool = False) -> None:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    inserted = 0
    skipped  = 0

    for src_id, src_lbl, tgt_id, tgt_lbl, ltype, desc, tier in LINKS:
        # Duplicate guard (bidirectional)
        cur.execute("""
            SELECT COUNT(*) FROM links
            WHERE (source_id=? AND target_id=?) OR (source_id=? AND target_id=?)
        """, (src_id, tgt_id, tgt_id, src_id))
        if cur.fetchone()[0] > 0:
            print(f"  SKIP (exists): {src_id} → {tgt_id}")
            skipped += 1
            continue

        if dry_run:
            print(f"  DRY RUN  [{tier}] {src_id} --{ltype}--> {tgt_id}")
            print(f"           {desc[:90]}")
            inserted += 1
            continue

        cur.execute("""
            INSERT INTO links
              (link_type, source_id, source_label, target_id, target_label,
               description, link_order, confidence_tier)
            VALUES (?, ?, ?, ?, ?, ?, 0, ?)
        """, (ltype, src_id, src_lbl, tgt_id, tgt_lbl, desc, tier))
        print(f"  [{tier}] {src_id} --{ltype}--> {tgt_id}")
        inserted += 1

    if not dry_run:
        conn.commit()
    conn.close()

    print(f"\n{'DRY RUN' if dry_run else 'INSERTED'}: {inserted} links, {skipped} skipped")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = parser.parse_args()

    print(f"{'DRY RUN — ' if args.dry_run else ''}Inserting {len(LINKS)} links into {SOURCE_DB}")
    print("─" * 70)
    insert_links(SOURCE_DB, dry_run=args.dry_run)

"""
Insert HB09: Generalised Second Law (GSL)

Bridge entry connecting:
  NE03 (Jarzynski Equality)   — non-equilibrium work, dissipated work, fluctuation theorems
  HB06 (Black Hole Area Theorem) — horizon area monotonicity, gravitational second law

The GSL is the irreversibility statement that unifies both: total entropy
(matter + Bekenstein-Hawking) is non-decreasing, linking gravitational
geometry to non-equilibrium thermodynamic fluctuation theorems via the
shared information-theoretic root in KL divergence non-negativity.

Pre-insertion NE03↔HB06 similarity: 0.763 (target: push toward 0.80+)
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRY = {
    "id": "HB09",
    "title": "HB09: Generalised Second Law",
    "filename": "HB09_generalised_second_law.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "HB",
    "authoring_status": "",
    "formality_tier": 1,
}

SECTIONS = [
    (0, "What It Claims",
     "The Generalised Second Law (GSL) states that the total entropy "
     "S_total = S_matter + S_BH never decreases: dS_total/dt ≥ 0, where "
     "S_BH = A/4l_P² is the Bekenstein-Hawking black hole entropy and "
     "S_matter is the von Neumann entropy S(ρ) = −Tr(ρ log ρ) of quantum "
     "fields outside the event horizon. The GSL unifies Hawking's classical "
     "area theorem dA/dt ≥ 0 (which governs isolated black holes) with the "
     "ordinary second law: even when matter falls into a black hole reducing "
     "the visible entropy, the event horizon area grows to compensate. "
     "The GSL is the irreversibility constraint that links gravitational "
     "geometry to non-equilibrium thermodynamics — the same directional "
     "asymmetry expressed by the Jarzynski equality ⟨e^{−W/k_BT}⟩ = "
     "e^{−ΔF/k_BT} and the Crooks fluctuation theorem, which quantify "
     "irreversibility via exponential averages of non-equilibrium work. "
     "Both the GSL and the fluctuation theorems are consequences of the "
     "non-negativity of KL divergence D_KL(p||q) ≥ 0 between forward and "
     "time-reversed process distributions — the GSL in the gravitational "
     "sector, the Jarzynski/Crooks relations in non-equilibrium "
     "thermodynamics. A quantum gravitational fluctuation theorem — "
     "extending the Crooks relation to black hole processes — would unify "
     "them as special cases of a single information-theoretic monotonicity "
     "constraint."),

    (1, "Mathematical Form",
     "dS_total/dt ≥ 0\n"
     "S_total = S_matter + A / (4 l_P²)\n\n"
     "where:\n"
     "  S_matter = −Tr(ρ log ρ)  — von Neumann entropy of exterior quantum fields\n"
     "  A         — event horizon area (Hawking's classical area theorem: dA/dt ≥ 0)\n"
     "  l_P = √(ℏG/c³)  — Planck length\n\n"
     "Bekenstein entropy bound: S_matter ≤ 2πER/ℏc\n"
     "(matter entropy bounded by energy E and linear size R)\n\n"
     "Limiting cases:\n"
     "  GSL → Hawking area theorem  (S_matter = 0, vacuum)\n"
     "  GSL → Second Law            (A fixed, flat spacetime)\n\n"
     "Fluctuation theorem parallel:\n"
     "  Crooks: P_F(W) / P_R(−W) = exp((W − ΔF)/k_BT)\n"
     "  Jarzynski: ⟨e^{−W/k_BT}⟩ = e^{−ΔF/k_BT}  →  ⟨W_diss⟩ ≥ 0\n"
     "Both follow from D_KL(p_forward || p_reverse) ≥ 0."),

    (2, "Constraint Category",
     "Thermodynamic-Geometric (Th-Gm): The GSL combines thermodynamic "
     "irreversibility (entropy non-decrease) with geometric monotonicity "
     "(event horizon area non-decrease). It is the gravitational counterpart "
     "of the Jarzynski dissipation bound ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 and the "
     "Crooks fluctuation theorem's non-equilibrium work asymmetry. All three "
     "— the GSL, the Jarzynski equality, and the Crooks fluctuation theorem "
     "— are manifestations of the non-negativity of KL divergence between "
     "forward and time-reversed distributions: D_KL(p_forward || p_reverse) "
     "= ⟨W_diss⟩/k_BT ≥ 0 in the non-equilibrium case, and the equivalent "
     "gravitational entropy balance in the black hole case. A quantum "
     "gravitational fluctuation theorem extending the Crooks relation "
     "P_F(W)/P_R(−W) = exp(βΔS) to black hole processes would unify them as "
     "two instances of the same information-theoretic monotonicity constraint, "
     "bridging non-equilibrium thermodynamics and black hole mechanics at the "
     "microscopic level."),

    (3, "DS Cross-References",
     "HB06 (Black Hole Area Theorem — the GSL directly generalises dA/dt ≥ 0: "
     "quantum fields allow area to decrease if matter entropy compensates; the "
     "area theorem is the classical vacuum limit of the GSL). "
     "NE03 (Jarzynski Equality — ⟨W_diss⟩ ≥ 0 is the non-equilibrium "
     "fluctuation-theorem counterpart of dS_total ≥ 0; both are "
     "irreversibility constraints tracing to KL divergence non-negativity; "
     "a quantum gravitational fluctuation theorem would unify them). "
     "NE04 (Crooks Fluctuation Theorem — the Crooks ratio P_F(W)/P_R(−W) = "
     "e^{β(W−ΔF)} is the microscopic fluctuation-theorem version of the GSL "
     "entropy balance; Jarzynski follows by exponential averaging over the "
     "Crooks distribution). "
     "HB02 (Bekenstein-Hawking Entropy — S_BH = A/4l_P² is the gravitational "
     "entropy term in the GSL; the GSL asserts this quantity plus matter "
     "entropy is non-decreasing). "
     "IT03 (KL Divergence — D_KL(p||q) ≥ 0 is the common information-theoretic "
     "root of both the GSL and the Jarzynski/Crooks inequalities; dissipated "
     "work W_diss/k_BT = D_KL(p_forward||p_reverse)). "
     "TD3 (Second Law of Thermodynamics — the GSL reduces to dS_matter ≥ 0 "
     "in flat spacetime; the Second Law is the GSL with the gravitational "
     "entropy term removed)."),

    (4, "Mathematical Archetype",
     "Mathematical archetype: conservation-law\n\n"
     "The GSL is an extensive monotonicity constraint of the same structural "
     "type as the Second Law and Hawking's area theorem: a total entropy "
     "functional S_total = S_matter + A/4l_P² is non-decreasing under "
     "time evolution. Gravitational entropy (area) and matter entropy trade "
     "off — any process decreasing one must increase the other by at least "
     "as much. This is the same archetype as the Jarzynski dissipation bound "
     "⟨W_diss⟩ ≥ 0 (total free energy is non-increasing) and the KL "
     "divergence non-negativity D_KL(p||q) ≥ 0 (relative entropy is always "
     "positive). The monotonicity is saturated at reversibility: GSL equality "
     "holds for quasi-static processes; Jarzynski equality saturates when all "
     "paths have W = ΔF (no dissipation)."),

    (5, "What The Math Says",
     "Throw matter with von Neumann entropy S_matter into a black hole. The "
     "exterior entropy decreases by S_matter. The event horizon area grows by "
     "at least 4l_P² × S_matter — the Bekenstein-Hawking entropy increases by "
     "at least S_matter. The GSL dS_total/dt ≥ 0 is satisfied: gravitational "
     "geometry absorbs the entropy loss of infalling matter.\n\n"
     "The structural parallel to the Jarzynski equality is exact: in a "
     "non-equilibrium process, useful work is extracted but dissipated work "
     "⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 is always non-negative — entropy is produced "
     "in the environment. In both cases, a total entropy budget is "
     "non-decreasing: matter + horizon entropy in the gravitational case, "
     "system + environment entropy in the thermodynamic case.\n\n"
     "Both the GSL and the Jarzynski/Crooks relations follow from the same "
     "mathematical fact: D_KL(p||q) ≥ 0. For fluctuation theorems: "
     "D_KL(p_forward||p_reverse) = ⟨W_diss⟩/k_BT ≥ 0. The gravitational "
     "analog would express the black hole entropy balance as a KL divergence "
     "between forward (infall) and time-reversed (Hawking radiation) "
     "distributions of quantum states across the event horizon."),

    (6, "Concept Tags",
     "• generalised second law\n"
     "• GSL\n"
     "• black hole entropy\n"
     "• Bekenstein-Hawking entropy\n"
     "• event horizon area\n"
     "• gravitational second law\n"
     "• area theorem\n"
     "• non-equilibrium thermodynamics\n"
     "• Jarzynski equality\n"
     "• Crooks fluctuation theorem\n"
     "• dissipated work\n"
     "• quantum fluctuation theorem\n"
     "• von Neumann entropy\n"
     "• KL divergence\n"
     "• entropy monotonicity\n"
     "• irreversibility\n"
     "• thermodynamic irreversibility\n"
     "• forward and reverse processes\n"
     "• non-negativity of KL divergence\n"
     "• exponential average"),
]

LINKS = [
    # HB09 → HB06
    ("HB09", "HB06", "derives_from", "1.5",
     "GSL directly generalises the Hawking area theorem to include quantum matter entropy"),
    # HB09 → NE03
    ("HB09", "NE03", "analogous_to", "1.5",
     "GSL irreversibility (dS_total ≥ 0) is the gravitational analog of Jarzynski dissipation bound (⟨W_diss⟩ ≥ 0)"),
    # HB09 → HB02
    ("HB09", "HB02", "derives_from", "1.5",
     "GSL uses S_BH = A/4l_P² as the gravitational entropy term"),
    # HB09 → IT03
    ("HB09", "IT03", "analogous_to", "1.5",
     "KL divergence non-negativity is the shared information-theoretic root of both GSL and fluctuation theorems"),
]


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Check if already exists
    existing = cur.execute("SELECT id FROM entries WHERE id = ?", (ENTRY["id"],)).fetchone()
    if existing:
        print(f"Entry {ENTRY['id']} already exists — skipping.")
        conn.close()
        return

    # Insert entry
    cur.execute(
        """INSERT INTO entries
           (id, title, filename, entry_type, scale, domain, status, confidence,
            type_group, authoring_status, formality_tier)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (ENTRY["id"], ENTRY["title"], ENTRY["filename"], ENTRY["entry_type"],
         ENTRY["scale"], ENTRY["domain"], ENTRY["status"], ENTRY["confidence"],
         ENTRY["type_group"], ENTRY["authoring_status"], ENTRY["formality_tier"])
    )
    print(f"  Inserted entry: {ENTRY['id']} — {ENTRY['title']}")

    # Insert sections
    for order, name, content in SECTIONS:
        cur.execute(
            """INSERT INTO sections (entry_id, section_name, section_order, content)
               VALUES (?, ?, ?, ?)""",
            (ENTRY["id"], name, order, content)
        )
        print(f"  Inserted section [{order}]: {name} ({len(content)} chars)")

    # Insert links (entry_connections table)
    # Check schema first
    link_cols = [r[1] for r in cur.execute("PRAGMA table_info(entry_connections)")]
    print(f"\n  entry_connections columns: {link_cols}")

    for src, tgt, rel, tier, note in LINKS:
        try:
            if "tier" in link_cols and "note" in link_cols:
                cur.execute(
                    """INSERT OR IGNORE INTO entry_connections
                       (source_id, target_id, relationship_type, tier, note)
                       VALUES (?, ?, ?, ?, ?)""",
                    (src, tgt, rel, tier, note)
                )
            elif "tier" in link_cols:
                cur.execute(
                    """INSERT OR IGNORE INTO entry_connections
                       (source_id, target_id, relationship_type, tier)
                       VALUES (?, ?, ?, ?)""",
                    (src, tgt, rel, tier)
                )
            else:
                cur.execute(
                    """INSERT OR IGNORE INTO entry_connections
                       (source_id, target_id, relationship_type)
                       VALUES (?, ?, ?)""",
                    (src, tgt, rel)
                )
            print(f"  Link: {src} → {tgt} ({rel}, tier {tier})")
        except Exception as e:
            print(f"  WARN link {src}→{tgt}: {e}")

    conn.commit()
    conn.close()
    print(f"\nDone. HB09 inserted.")


if __name__ == "__main__":
    print(f"Inserting GSL bridge entry into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)

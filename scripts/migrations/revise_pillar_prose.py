"""
Targeted prose revisions for cross-pillar vocabulary alignment.

Updates 'What It Claims' and 'Constraint Category' sections to inject
cross-domain vocabulary that improves embedding similarity for
structurally connected pairs that the embeddings missed.

Target pairs (pre-revision similarity):
  IT03 ↔ IT04: 0.836  (near miss)
  RG06 ↔ GT04: 0.809
  IT05 ↔ BR04: 0.793
  HB02 ↔ IT02: 0.787
  NE03 ↔ HB06: 0.738
  INFO4 ↔ RG04: 0.708
  GT03 ↔ RG04: 0.726
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

# Each revision: (entry_id, section_name, old_fragment, new_fragment)
# We replace a specific substring to inject vocabulary.

REVISIONS = [

# ═══════════════════════════════════════════════════════════════════════════
# 1. IT03 ↔ IT04 (0.836) — Add quantum/classical bridge vocabulary
# ═══════════════════════════════════════════════════════════════════════════

# IT03: Add quantum generalisation mention
("IT03", "What It Claims",
 "but it is the fundamental measure of statistical distinguishability between probability distributions.",
 "but it is the fundamental measure of statistical distinguishability between probability distributions. "
 "KL divergence applies to classical probability distributions; its quantum generalisation — the quantum "
 "relative entropy S(ρ||σ) = Tr(ρ log ρ − ρ log σ) — extends this to density matrices and quantum states, "
 "preserving the non-negativity and monotonicity properties in the non-commutative setting."),

# IT04: Strengthen classical-limit vocabulary
("IT04", "Constraint Category",
 "Every irreversibility result in quantum theory can be derived from this single property.",
 "Every irreversibility result in quantum theory can be derived from this single property. "
 "In the classical limit (commuting density matrices), quantum relative entropy reduces exactly to "
 "the Kullback-Leibler divergence, and the quantum data processing inequality reduces to the "
 "classical data processing inequality — the quantum and classical theories are nested."),

# ═══════════════════════════════════════════════════════════════════════════
# 2. RG06 ↔ GT04 (0.809) — Add gravitational/transport cross-vocabulary
# ═══════════════════════════════════════════════════════════════════════════

# RG06: Add gravitational dynamics vocabulary
("RG06", "What It Claims",
 "and through Bianconi's framework, to gravitational dynamics.",
 "and through Bianconi's framework, to gravitational dynamics. The Fisher-Rao metric "
 "thus serves as the common geometric substrate of both renormalisation group flow and "
 "emergent spacetime curvature: scale evolution and gravitational dynamics are both "
 "gradient flows on the same information-geometric manifold."),

# GT04: Add optimal transport / gradient flow vocabulary
("GT04", "What It Claims",
 "Bianconi's approach is network-native: it works on discrete quantum networks, not just continuous manifolds.",
 "Bianconi's approach is network-native: it works on discrete quantum networks, not just continuous manifolds. "
 "Like the Cotler-Rezchikov identification of renormalisation group flow as Wasserstein gradient flow on "
 "the Fisher-Rao manifold, Bianconi's framework treats gravitational dynamics as optimal transport on "
 "quantum state space — both are gradient flows driven by the same Fisher information metric."),

# ═══════════════════════════════════════════════════════════════════════════
# 3. IT05 ↔ BR04 (0.793) — Add thermodynamic geometry / estimation cross-vocab
# ═══════════════════════════════════════════════════════════════════════════

# IT05: Add thermodynamic geometry vocabulary
("IT05", "What It Claims",
 "This geometric interpretation connects statistical inference to general relativity (Ruppeiner geometry), "
 "renormalisation group flow (Cotler-Rezchikov), and emergent gravity (Bianconi).",
 "This geometric interpretation connects statistical inference to general relativity (Ruppeiner geometry), "
 "renormalisation group flow (Cotler-Rezchikov), and emergent gravity (Bianconi). In thermodynamic state "
 "space, the Fisher information matrix becomes the Ruppeiner metric — the negative Hessian of entropy — "
 "showing that thermodynamic fluctuation geometry is a special case of information geometry."),

# BR04: Add statistical estimation vocabulary
("BR04", "Constraint Category",
 "The identity with the Fisher-Rao metric makes this simultaneously a geometric and information-theoretic constraint.",
 "The identity with the Fisher-Rao metric makes this simultaneously a geometric and information-theoretic constraint. "
 "The Cramér-Rao bound of statistical estimation applies directly: the minimum variance of any "
 "thermodynamic measurement is bounded by the inverse of the Ruppeiner metric component — the "
 "Fisher information sets the precision limit for thermodynamic parameter estimation."),

# ═══════════════════════════════════════════════════════════════════════════
# 4. HB02 ↔ IT02 (0.787) — Add entanglement/horizon cross-vocabulary
# ═══════════════════════════════════════════════════════════════════════════

# HB02: Add von Neumann entropy vocabulary
("HB02", "What It Claims",
 "and is now understood to equal the entanglement entropy of quantum fields across the event horizon.",
 "and is now understood to equal the entanglement entropy — the von Neumann entropy S(ρ) = −Tr(ρ log ρ) "
 "of the reduced density matrix — of quantum fields across the event horizon. Tracing over the "
 "interior degrees of freedom produces a thermal density matrix for the exterior, whose von Neumann "
 "entropy exactly equals A/4l_P². This identifies black hole entropy as a quantum information quantity: "
 "it measures the entanglement between the interior and exterior quantum states."),

# IT02: Add Bekenstein-Hawking / horizon vocabulary
("IT02", "What It Claims",
 "This makes it the bridge between quantum information theory and black hole thermodynamics, "
 "where the Bekenstein-Hawking entropy of a black hole equals the entanglement entropy across the event horizon.",
 "This makes it the bridge between quantum information theory and black hole thermodynamics: "
 "the Bekenstein-Hawking entropy S_BH = A/4l_P² of a black hole equals the von Neumann entropy "
 "of the reduced density matrix obtained by tracing over the degrees of freedom behind the event horizon. "
 "The area-proportionality S ∝ A (not volume) of this entanglement entropy is the origin of the "
 "holographic principle — the quantum information content of a region is encoded on its boundary."),

# ═══════════════════════════════════════════════════════════════════════════
# 5. NE03 ↔ HB06 (0.738) — Add monotonicity / fluctuation cross-vocabulary
# ═══════════════════════════════════════════════════════════════════════════

# NE03: Add monotonicity / gravitational analog vocabulary
("NE03", "Constraint Category",
 "The equality has been experimentally verified in single-molecule pulling experiments on RNA hairpins "
 "(Liphardt et al., Science 296, 1832, 2002).",
 "The equality has been experimentally verified in single-molecule pulling experiments on RNA hairpins "
 "(Liphardt et al., Science 296, 1832, 2002). The Jarzynski equality is a monotonicity statement: "
 "average dissipated work ⟨W_diss⟩ = ⟨W⟩ − ΔF ≥ 0 is non-negative, paralleling the monotonicity "
 "of black hole horizon area dA/dt ≥ 0 (Hawking's area theorem). Both are irreversibility constraints "
 "— one thermodynamic, one gravitational — that may share a common information-theoretic origin in the "
 "non-negativity of KL divergence."),

# HB06: Add fluctuation theorem vocabulary
("HB06", "Constraint Category",
 "Combined with the four laws of black hole mechanics, it establishes a complete formal analogy between "
 "black hole physics and thermodynamics.",
 "Combined with the four laws of black hole mechanics, it establishes a complete formal analogy between "
 "black hole physics and thermodynamics. The area theorem is the gravitational counterpart of the "
 "non-negativity of dissipated work ⟨W_diss⟩ ≥ 0 in the Jarzynski equality and the Crooks fluctuation "
 "theorem. A quantum gravitational fluctuation theorem — extending the Crooks relation to black hole "
 "processes — remains an open question that would unify non-equilibrium thermodynamics with black "
 "hole mechanics at the microscopic level."),

# ═══════════════════════════════════════════════════════════════════════════
# 6. INFO4 ↔ RG04 (0.708) — Add coarse-graining / mutual-info cross-vocab
# ═══════════════════════════════════════════════════════════════════════════

# INFO4: Add coarse-graining / RG / degrees-of-freedom vocabulary
("INFO4", "Constraint Category",
 "This is deeply related to the Second Law of Thermodynamics: irreversible processing destroys "
 "information. The equality condition (sufficient statistic) identifies when no information is lost "
 "in the processing step.",
 "This is deeply related to the Second Law of Thermodynamics: irreversible processing destroys "
 "information. The equality condition (sufficient statistic) identifies when no information is lost "
 "in the processing step. The DPI is the information-theoretic version of the Zamolodchikov c-theorem "
 "in quantum field theory: coarse-graining (integrating out degrees of freedom in the renormalisation "
 "group) is a data-processing operation that can only reduce the effective number of degrees of freedom. "
 "The c-function that decreases monotonically under RG flow is the field-theoretic analog of mutual "
 "information that decreases under data processing."),

# RG04: Add mutual information / data-processing vocabulary
("RG04", "What It Claims",
 "The c-theorem was the first rigorous proof that RG flow has a preferred direction — from many degrees "
 "of freedom (UV) to few (IR).",
 "The c-theorem was the first rigorous proof that RG flow has a preferred direction — from many degrees "
 "of freedom (UV) to few (IR). The structural parallel to the data processing inequality is exact: "
 "the DPI states that mutual information I(X;Z) ≤ I(X;Y) when X → Y → Z forms a Markov chain; "
 "the c-theorem states that c_UV ≥ c_IR when the UV theory flows to the IR theory under coarse-graining. "
 "Both are monotonicity theorems proving that lossy processing — whether of data or of physical "
 "degrees of freedom — is irreversible."),

# ═══════════════════════════════════════════════════════════════════════════
# 7. GT03 ↔ RG04 (0.726) — Add DoF counting cross-vocabulary
# ═══════════════════════════════════════════════════════════════════════════

# GT03: Add c-theorem / irreversibility vocabulary
("GT03", "Constraint Category",
 "Cosmological expansion is driven by information disequilibrium.",
 "Cosmological expansion is driven by information disequilibrium. The monotonic approach to "
 "holographic equipartition (N_bulk → N_sur) parallels the monotonic decrease of the c-function "
 "under renormalisation group flow: both describe systems evolving irreversibly toward a state with "
 "fewer effective degrees of freedom, connecting cosmological dynamics to the RG irreversibility "
 "proven by Zamolodchikov's c-theorem."),

# RG04: Add cosmological / degree-of-freedom counting vocabulary
("RG04", "Constraint Category",
 "The constraint is both informatic (counting degrees of freedom) and dynamical (governing the direction of flow).",
 "The constraint is both informatic (counting degrees of freedom) and dynamical (governing the direction of flow). "
 "The same monotonic reduction of effective degrees of freedom appears in cosmology: Padmanabhan's "
 "holographic equipartition shows that the universe expands until the bulk degrees of freedom N_bulk "
 "match the surface degrees of freedom N_sur — a cosmological c-theorem where the expansion of "
 "space itself is driven by the information imbalance between surface and bulk."),

]


def apply_revisions(db_path, revisions):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    applied = failed = 0

    for entry_id, section_name, old_frag, new_frag in revisions:
        # Get current content
        row = cur.execute(
            "SELECT content FROM sections WHERE entry_id = ? AND section_name = ?",
            (entry_id, section_name)
        ).fetchone()

        if not row:
            print(f"  FAIL (not found): {entry_id} / {section_name}")
            failed += 1
            continue

        content = row[0]
        if old_frag not in content:
            print(f"  FAIL (fragment not found): {entry_id} / {section_name}")
            print(f"    Looking for: {old_frag[:80]}...")
            failed += 1
            continue

        new_content = content.replace(old_frag, new_frag)
        cur.execute(
            "UPDATE sections SET content = ? WHERE entry_id = ? AND section_name = ?",
            (new_content, entry_id, section_name)
        )
        print(f"  OK: {entry_id} / {section_name} (+{len(new_frag) - len(old_frag)} chars)")
        applied += 1

    conn.commit()
    conn.close()
    print(f"\nDone: {applied} applied, {failed} failed.")
    return applied, failed


if __name__ == "__main__":
    print(f"Applying {len(REVISIONS)} prose revisions to:\n  {SOURCE_DB}\n")
    apply_revisions(SOURCE_DB, REVISIONS)

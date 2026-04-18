"""
Insert INFO1 Shannon Entropy — GSW anchors — 2026-04-18

Applies the 8 anchors drafted in docs/prior_art_reviews/INFO1_Shannon_Entropy.md.
First real content insertion into external_anchors.

Covers 4 of 5 canonical roles:
- progenitor           : Shannon 1948 Parts I and II (DOI)
- axiomatic_foundation : Khinchin 1957 (ISBN)
- standard_textbook    : Cover & Thomas 2006 (ISBN)
- living_reference     : Wikipedia + MathWorld + Scholarpedia (3 anchors)

Plus 1 adjacent_concept anchor: nLab (categorical framing).

The comprehensive_survey role is legitimately empty for mature information theory
— textbooks serve that purpose.

Run: python3 scripts/migrations/insert_info1_anchors_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-info1-smoke-test-2026-04-18"
ENTRY_ID = "INFO1"


# Anchor rows from the smoke-test report
# Tuple: (source, identifier, revision_id, title, tier, stability_class,
#         relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ----- progenitor -----
    ("doi", "10.1002/j.1538-7305.1948.tb01338.x", None,
     "A Mathematical Theory of Communication (Part I)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Shannon's original paper. Bell System Technical Journal, vol. 27, "
     "no. 3, pp. 379-423, July 1948. H = -Sum p log p introduced in §6 "
     "(entropy axioms). ~51,000 citations. Verified via CrossRef API "
     "2026-04-17."),

    ("doi", "10.1002/j.1538-7305.1948.tb00917.x", None,
     "A Mathematical Theory of Communication (Part II)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Continuation of the primary paper: continuous case and channel "
     "capacity. BSTJ vol. 27, no. 4, pp. 623-656, October 1948. Frequently "
     "treated as part of the same work. Verified via CrossRef API "
     "2026-04-17."),

    # ----- axiomatic_foundation -----
    ("isbn", "978-0486604343", None,
     "Mathematical Foundations of Information Theory",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Khinchin 1957 (Dover English edition; Russian original 1953). "
     "Axiomatic derivation of Shannon entropy independent of Shannon's "
     "communication-theoretic motivation. ISBN-verified; not fetched. "
     "Known canonical axiomatization reference."),

    # ----- standard_textbook -----
    ("isbn", "978-0471241959", None,
     "Elements of Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Cover & Thomas, 2nd ed., Wiley 2006. Standard graduate-level textbook. "
     "Shannon entropy defined in Ch. 2. ISBN-verified; not fetched."),

    # ----- living_reference -----
    ("wikipedia", "https://en.wikipedia.org/wiki/Entropy_(information_theory)",
     "1348256973",
     "Entropy (information theory)",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-17. Standard definition "
     "H = -Sum p log p; two axiomatic characterizations (information-function "
     "+ Aczel-Forte-Ng); downstream concept links (differential entropy, "
     "conditional/joint entropy, mutual information, relative entropy, "
     "Renyi, Hartley). Revision pinned; 180d calendar refresh per §7 of "
     "GSW_ANCHOR_ARCHITECTURE.md."),

    ("mathworld", "https://mathworld.wolfram.com/Entropy.html", None,
     "Entropy (Wolfram MathWorld)",
     2, "canonical", "canonical_authority", "living_reference", "high",
     "Wolfram MathWorld's entropy article. Verified via WebFetch 2026-04-17: "
     "treats Shannon entropy with standard formula; cites Shannon 1948 with "
     "full BSTJ details (vol. 27, pp. 379-423 and 623-656). Complements "
     "Wikipedia; different editorial voice."),

    ("scholarpedia", "http://www.scholarpedia.org/article/Entropy", None,
     "Entropy (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Peer-reviewed Scholarpedia article covering Shannon + Kolmogorov-Sinai "
     "entropy. Confirmed to exist via WebSearch 2026-04-17; direct WebFetch "
     "timed out x2 (site is flaky). Confidence medium pending re-fetch of "
     "full content to verify specific treatment of Shannon entropy. "
     "Trigger: re-fetch on next session to upgrade confidence=high."),

    # ----- adjacent_concept (NOT canonical_authority) -----
    ("nlab", "https://ncatlab.org/nlab/show/entropy", None,
     "entropy (nLab)",
     2, "canonical", "adjacent_concept", None, "high",
     "nLab treats entropy categorically/operadically (Baez 'entropy as "
     "functor', Li 'entropy as universal natural transformation', "
     "Baudot-Bennequin 'homological nature of entropy'). Shannon entropy "
     "is a special case within that framing. Verified via WebFetch "
     "2026-04-17. Not canonical_authority — different mathematical framing "
     "of the concept. canonical_role is NULL per architecture §4.2."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        # Sanity check: INFO1 must have domain tags (from chunks 1-5)
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM entry_source_domains "
            "WHERE entry_id=? AND review_status='current'", (ENTRY_ID,),
        )
        n_tags = cur.fetchone()[0]
        if n_tags == 0:
            raise RuntimeError(
                f"{ENTRY_ID} has no domain tags; run retag migrations first."
            )
        print(f"INFO1 currently has {n_tags} domain-tag rows. Proceeding.")

        # Insert anchors
        rows_inserted = 0
        skipped = 0
        for a in ANCHORS:
            (source, identifier, revision_id, title, tier, stability,
             relationship, canonical_role, confidence, notes) = a
            res = conn.execute(
                "INSERT OR IGNORE INTO external_anchors "
                "(entry_id, source, identifier, revision_id, title, tier, "
                " source_stability_class, relationship, canonical_role, "
                " verified_date, verified_by_session, confidence, notes) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (ENTRY_ID, source, identifier, revision_id, title, tier,
                 stability, relationship, canonical_role,
                 TODAY, SESSION, confidence, notes),
            )
            if res.rowcount > 0:
                rows_inserted += 1
            else:
                skipped += 1

        conn.commit()

        print(f"\nInserted: {rows_inserted} new anchors")
        print(f"Skipped (already existed): {skipped}")

        # Verification report
        print(f"\nAll current anchors for {ENTRY_ID}:")
        for row in conn.execute("""
            SELECT source, identifier, tier, relationship, canonical_role,
                   confidence
            FROM external_anchors
            WHERE entry_id = ?
            ORDER BY
                CASE relationship WHEN 'canonical_authority' THEN 1 ELSE 2 END,
                CASE canonical_role
                    WHEN 'progenitor'           THEN 1
                    WHEN 'axiomatic_foundation' THEN 2
                    WHEN 'standard_textbook'    THEN 3
                    WHEN 'living_reference'     THEN 4
                    WHEN 'comprehensive_survey' THEN 5
                    ELSE 6 END,
                tier, source
        """, (ENTRY_ID,)):
            role = row[4] if row[4] else "—"
            print(f"  [tier {row[2]}] {row[3]:20} / {role:22} / "
                  f"{row[0]:15} ({row[5]:6}) {row[1][:60]}")

        # Canonicity slot coverage
        print(f"\nCanonical-role slot coverage for {ENTRY_ID}:")
        for role in ("progenitor", "axiomatic_foundation", "standard_textbook",
                     "living_reference", "comprehensive_survey"):
            cur.execute(
                "SELECT COUNT(*) FROM external_anchors "
                "WHERE entry_id=? AND canonical_role=?",
                (ENTRY_ID, role),
            )
            n = cur.fetchone()[0]
            status = "✓" if n > 0 else "empty"
            print(f"  {role:24} {n} anchors  [{status}]")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

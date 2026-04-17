"""
Phase 2: Cross-Pillar Similarity Analysis

Computes entry-level centroid embeddings for all new pillar entries,
builds a full cross-domain similarity matrix, and surfaces the top
link candidates.

Output:
  - Top cross-pillar pairs above threshold
  - Pillar-to-pillar density matrix
  - Priority target check (spec-predicted pairs)
  - Gap analysis
"""

import sqlite3
import json
import csv
import numpy as np
from pathlib import Path

# -- config --
DB_PATH = Path("data/ds_wiki.db")
CHROMA_PATH = Path("data/chroma_db")

NEW_PREFIXES = {"IT", "HB", "GT", "RG", "NE", "BR"}
ALL_PILLARS = {"IT", "HB", "GT", "RG", "NE", "BR"}
# Also include existing entries that the new pillars link to
BRIDGE_EXISTING = {"INFO", "STAT", "GV", "TD", "CM", "EM", "RD", "B5", "M6"}

SAME_DOMAIN_THRESH = 0.80
CROSS_DOMAIN_THRESH = 0.85
HIGH_SIM_THRESH = 0.90

OUTPUT_DIR = Path("data/reports/pillar_analysis")


def get_entry_prefix(entry_id):
    """Extract pillar prefix from entry ID."""
    for pfx in sorted(ALL_PILLARS, key=len, reverse=True):
        if entry_id.startswith(pfx):
            return pfx
    # For existing entries, map to broader categories
    if entry_id.startswith("INFO") or entry_id.startswith("STAT"):
        return "IT_existing"
    if entry_id.startswith("TD"):
        return "NE_related"
    if entry_id.startswith("GV"):
        return "GT_existing"
    return "other"


def compute_entry_centroids(db_path, chroma_path):
    """Compute centroid embedding for each entry from its chunk embeddings."""
    import chromadb

    client = chromadb.PersistentClient(path=str(chroma_path))
    collection = client.get_collection("ds_wiki")

    # Get all entries
    conn = sqlite3.connect(db_path)
    entries = conn.execute("SELECT id, title, domain FROM entries ORDER BY id").fetchall()
    conn.close()

    centroids = {}
    metadata = {}

    for entry_id, title, domain in entries:
        # Get all chunks for this entry
        results = collection.get(
            where={"entry_id": entry_id},
            include=["embeddings"]
        )

        if results["embeddings"] is not None and len(results["embeddings"]) > 0:
            embs = np.array(results["embeddings"])
            centroid = embs.mean(axis=0)
            centroid = centroid / np.linalg.norm(centroid)  # L2 normalise
            centroids[entry_id] = centroid
            metadata[entry_id] = {"title": title, "domain": domain}

    return centroids, metadata


def compute_similarity_matrix(centroids, metadata):
    """Full pairwise cosine similarity between all entries."""
    ids = sorted(centroids.keys())
    n = len(ids)
    sim_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            sim = np.dot(centroids[ids[i]], centroids[ids[j]])
            sim_matrix[i, j] = sim
            sim_matrix[j, i] = sim

    return ids, sim_matrix


def find_cross_pillar_candidates(ids, sim_matrix, metadata):
    """Surface cross-pillar link candidates above threshold."""
    candidates = []
    n = len(ids)

    for i in range(n):
        pfx_i = get_entry_prefix(ids[i])
        for j in range(i + 1, n):
            pfx_j = get_entry_prefix(ids[j])
            sim = sim_matrix[i, j]

            # Skip same-entry
            if ids[i] == ids[j]:
                continue

            # Determine if cross-domain
            is_cross = pfx_i != pfx_j

            if is_cross and sim >= CROSS_DOMAIN_THRESH:
                candidates.append({
                    "id_a": ids[i],
                    "title_a": metadata[ids[i]]["title"],
                    "prefix_a": pfx_i,
                    "id_b": ids[j],
                    "title_b": metadata[ids[j]]["title"],
                    "prefix_b": pfx_j,
                    "similarity": float(sim),
                    "level": "HIGH" if sim >= HIGH_SIM_THRESH else "CROSS",
                })
            elif not is_cross and sim >= SAME_DOMAIN_THRESH:
                candidates.append({
                    "id_a": ids[i],
                    "title_a": metadata[ids[i]]["title"],
                    "prefix_a": pfx_i,
                    "id_b": ids[j],
                    "title_b": metadata[ids[j]]["title"],
                    "prefix_b": pfx_j,
                    "similarity": float(sim),
                    "level": "SAME",
                })

    candidates.sort(key=lambda x: x["similarity"], reverse=True)
    return candidates


def check_priority_targets(centroids, metadata):
    """Check the spec-predicted priority pairs."""
    targets = [
        ("INFO4", "RG04", "analogous_to", "Both: quantity decreases under coarse-graining"),
        ("INFO4", "HB06", "analogous_to", "Both: irreversibility/monotonicity of information loss"),
        ("NE03", "HB06", "analogous_to", "Both: irreversibility statements connecting micro↔macro"),
        ("RG06", "GT04", "analogous_to", "Both: information-geometric object → physics"),
        ("GT03", "RG04", "analogous_to", "Both: DoF count decreases monotonically under a flow"),
        ("IT05", "BR04", "derives_from", "Ruppeiner metric IS Fisher-Rao on Gibbs distributions"),
        ("IT03", "IT04", "generalizes", "QRE generalises KL to quantum"),
        ("HB02", "IT02", "analogous_to", "Both: entropy of quantum system; BH = entanglement entropy"),
    ]

    results = []
    for id_a, id_b, expected_type, reason in targets:
        if id_a in centroids and id_b in centroids:
            sim = float(np.dot(centroids[id_a], centroids[id_b]))
            flagged = sim >= CROSS_DOMAIN_THRESH
            results.append({
                "id_a": id_a,
                "id_b": id_b,
                "title_a": metadata.get(id_a, {}).get("title", "?"),
                "title_b": metadata.get(id_b, {}).get("title", "?"),
                "expected_type": expected_type,
                "reason": reason,
                "similarity": sim,
                "flagged": flagged,
            })
        else:
            results.append({
                "id_a": id_a,
                "id_b": id_b,
                "title_a": "NOT FOUND",
                "title_b": "NOT FOUND",
                "expected_type": expected_type,
                "reason": reason,
                "similarity": -1,
                "flagged": False,
            })

    return results


def compute_pillar_density(candidates):
    """Compute pillar-to-pillar link density matrix."""
    pillars = sorted(ALL_PILLARS)
    matrix = {p1: {p2: 0 for p2 in pillars} for p1 in pillars}

    for c in candidates:
        p1 = c["prefix_a"] if c["prefix_a"] in ALL_PILLARS else None
        p2 = c["prefix_b"] if c["prefix_b"] in ALL_PILLARS else None
        if p1 and p2 and p1 != p2:
            matrix[p1][p2] += 1
            matrix[p2][p1] += 1

    return pillars, matrix


def filter_new_pillar_candidates(candidates):
    """Filter candidates to only those involving at least one new pillar entry."""
    new_cands = []
    for c in candidates:
        a_new = any(c["id_a"].startswith(p) for p in NEW_PREFIXES)
        b_new = any(c["id_b"].startswith(p) for p in NEW_PREFIXES)
        if a_new or b_new:
            new_cands.append(c)
    return new_cands


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Computing entry centroids from ChromaDB embeddings...")
    centroids, metadata = compute_entry_centroids(DB_PATH, CHROMA_PATH)
    print(f"  {len(centroids)} entries with embeddings")

    # Filter to new pillar entries for focused analysis
    new_ids = [eid for eid in centroids if any(eid.startswith(p) for p in NEW_PREFIXES)]
    print(f"  {len(new_ids)} new pillar entries")

    print("\nComputing full similarity matrix...")
    ids, sim_matrix = compute_similarity_matrix(centroids, metadata)
    print(f"  {len(ids)}×{len(ids)} matrix computed")

    print("\nFinding cross-pillar link candidates...")
    all_candidates = find_cross_pillar_candidates(ids, sim_matrix, metadata)
    new_candidates = filter_new_pillar_candidates(all_candidates)
    print(f"  {len(new_candidates)} candidates involving new pillar entries")

    # Top 30 cross-pillar candidates
    cross_cands = [c for c in new_candidates if c["level"] in ("CROSS", "HIGH")]
    print(f"  {len(cross_cands)} cross-domain candidates (≥{CROSS_DOMAIN_THRESH})")

    print("\n" + "=" * 80)
    print("TOP 30 CROSS-PILLAR LINK CANDIDATES")
    print("=" * 80)
    for i, c in enumerate(cross_cands[:30]):
        marker = "***" if c["level"] == "HIGH" else "   "
        print(f"{marker} {i+1:2d}. {c['id_a']:8s} ↔ {c['id_b']:8s}  sim={c['similarity']:.4f}  "
              f"| {c['title_a'][:35]:35s} ↔ {c['title_b'][:35]:35s}")

    # Check priority targets
    print("\n" + "=" * 80)
    print("PRIORITY TARGET PAIRS (spec-predicted)")
    print("=" * 80)
    priority_results = check_priority_targets(centroids, metadata)
    for r in priority_results:
        status = "✓ FLAGGED" if r["flagged"] else "✗ MISSED"
        print(f"  {status}  {r['id_a']:8s} ↔ {r['id_b']:8s}  sim={r['similarity']:.4f}  "
              f"({r['reason'][:60]})")

    # Pillar density matrix
    pillars, density = compute_pillar_density(cross_cands)
    print("\n" + "=" * 80)
    print("PILLAR-TO-PILLAR CROSS-DOMAIN LINK DENSITY (candidates ≥ 0.85)")
    print("=" * 80)
    header = "      " + "  ".join(f"{p:>4s}" for p in pillars)
    print(header)
    for p1 in pillars:
        row = f"{p1:4s}  " + "  ".join(f"{density[p1][p2]:4d}" for p2 in pillars)
        print(row)

    # Identify gaps
    print("\n" + "=" * 80)
    print("STRUCTURAL GAPS (zero cross-domain candidates between pillar pairs)")
    print("=" * 80)
    gaps = []
    for i, p1 in enumerate(pillars):
        for j, p2 in enumerate(pillars):
            if j > i and density[p1][p2] == 0:
                gaps.append((p1, p2))
                print(f"  GAP: {p1} ↔ {p2}")
    if not gaps:
        print("  No gaps — all pillar pairs have at least one cross-domain candidate.")

    # Save outputs
    # 1. Full candidate list as CSV
    csv_path = OUTPUT_DIR / "cross_pillar_similarity_candidates.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id_a", "title_a", "prefix_a",
                                                "id_b", "title_b", "prefix_b",
                                                "similarity", "level"])
        writer.writeheader()
        for c in new_candidates:
            writer.writerow(c)
    print(f"\nSaved: {csv_path} ({len(new_candidates)} rows)")

    # 2. Priority target results
    priority_path = OUTPUT_DIR / "priority_target_results.json"
    with open(priority_path, "w") as f:
        json.dump(priority_results, f, indent=2)
    print(f"Saved: {priority_path}")

    # 3. Summary stats
    stats = {
        "total_entries": len(centroids),
        "new_pillar_entries": len(new_ids),
        "total_candidates": len(new_candidates),
        "cross_domain_candidates": len(cross_cands),
        "high_sim_candidates": len([c for c in cross_cands if c["level"] == "HIGH"]),
        "priority_flagged": sum(1 for r in priority_results if r["flagged"]),
        "priority_missed": sum(1 for r in priority_results if not r["flagged"]),
        "structural_gaps": gaps,
        "pillar_density": {f"{p1}-{p2}": density[p1][p2] for p1 in pillars for p2 in pillars if p1 < p2},
    }
    stats_path = OUTPUT_DIR / "analysis_stats.json"
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Saved: {stats_path}")

    return stats


if __name__ == "__main__":
    main()

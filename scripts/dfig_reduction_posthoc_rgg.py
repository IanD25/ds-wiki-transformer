#!/usr/bin/env python3
"""POST-HOC (not pre-registered) diagnostic for the DFIG reduction test, §2.3.

H-RGG failed: on periodic random geometric graphs the "+1" survives centring.
This asks what the (d+1)-th eigenvector of the centred matrix C = F − μμᵀ is.
For each sampled vertex v and neighbour w_j, x_j = minimum-image displacement.
  - "translation fit": fraction of the top-d eigenvectors' span lying in the span
    of the d coordinate vectors (x_j)_a  (1 = the top d modes are the d displacement directions);
  - |cos| of the (d+1)-th eigenvector with the all-neighbours-in-phase vector 1/√k
    (the "radial" combination Σ_j s_j, the sector λ_A occupies on a torus);
  - |corr| of the (d+1)-th eigenvector with |x_j| (neighbour's Euclidean distance from v)
    and with deg(w_j).
Seeds 0–2, σ = 2, 50 vertices per seed, same graphs as the main script.
Writes data/reports/dfig_reduction_2026_10/posthoc_rgg.csv and prints a summary.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial import cKDTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dfig_reduction_2026_10_19 import OUT, fim, gap_rank, neighbours  # noqa: E402


def rgg_with_points(n, d, r, seed):
    rng = np.random.default_rng(seed)          # same stream as periodic_rgg()
    pts = rng.uniform(0, 1, size=(n, d))
    pairs = np.array(sorted(cKDTree(pts, boxsize=1.0).query_pairs(r)))
    A = csr_matrix((np.ones(2 * len(pairs)),
                    (np.r_[pairs[:, 0], pairs[:, 1]], np.r_[pairs[:, 1], pairs[:, 0]])), shape=(n, n))
    _, lab = connected_components(A, directed=False)
    keep = np.where(lab == np.argmax(np.bincount(lab)))[0]
    return A[keep][:, keep].tocsr(), pts[keep]


def main():
    rows = []
    for d, r in ((2, 0.03), (3, 0.09)):
        for seed in (0, 1, 2):
            A, pts = rgg_with_points(5000, d, r, seed)
            verts = np.random.default_rng(100 + seed).choice(A.shape[0], size=50, replace=False)
            deg = np.diff(A.indptr)
            for v in verts:
                F, S, p = fim(A, int(v), 2.0)
                mu = S @ p
                C = F - np.outer(mu, mu)
                ev, U = np.linalg.eigh(C)
                o = np.argsort(ev)[::-1]
                ev, U = ev[o], U[:, o]
                nb = neighbours(A, int(v))
                x = pts[nb] - pts[v]
                x -= np.round(x)                       # minimum image
                Q, _ = np.linalg.qr(x)                 # k×d orthonormal basis of displacement span
                top = U[:, :d]
                fit = float(np.linalg.norm(Q.T @ top) ** 2 / d)
                e1 = U[:, d]
                rad = np.linalg.norm(x, axis=1)
                c_rad = float(abs(np.corrcoef(e1, rad)[0, 1]))
                c_deg = float(abs(np.corrcoef(e1, deg[nb])[0, 1])) if np.std(deg[nb]) > 0 else np.nan
                c_uni = float(abs(e1.sum()) / np.sqrt(len(e1)))
                rows.append(dict(d=d, seed=seed, vertex=int(v), k=len(nb), rank_c=gap_rank(ev),
                                 translation_fit=fit, cos_e_dp1_uniform=c_uni, corr_e_dp1_radius=c_rad, corr_e_dp1_degree=c_deg))
    with (OUT / "posthoc_rgg.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for d in (2, 3):
        sel = [r for r in rows if r["d"] == d]
        cen = [r for r in sel if r["rank_c"] == d + 1]
        print(f"d={d}: n={len(sel)}, rank_c=d+1 at {len(cen)}")
        for lab, ss in (("all", sel), ("rank_c=d+1", cen)):
            print(f"  [{lab}] median translation_fit={np.median([r['translation_fit'] for r in ss]):.3f}"
                  f"  median |cos(e_d+1, 1/sqrt k)|={np.median([r['cos_e_dp1_uniform'] for r in ss]):.3f}"
                  f" (frac>=0.8: {np.mean([r['cos_e_dp1_uniform'] >= 0.8 for r in ss]):.2f})"
                  f"  median |corr(e_d+1, |x_j|)|={np.median([r['corr_e_dp1_radius'] for r in ss]):.3f}"
                  f"  frac>=0.8: {np.mean([r['corr_e_dp1_radius'] >= 0.8 for r in ss]):.2f}"
                  f"  median |corr(e_d+1, deg)|={np.nanmedian([r['corr_e_dp1_degree'] for r in ss]):.3f}")


if __name__ == "__main__":
    main()

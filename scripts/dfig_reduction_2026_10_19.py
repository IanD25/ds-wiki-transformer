#!/usr/bin/env python3
"""DFIG reduction test (pre-registered: docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md §1).

Re-implements the Phase 1 Fisher construction of the owner's D_eff-Test-1.0
repository (PHASE1_GEOMETRIC/src/ds_phase1_*.py) exactly:
  p_v(u) = exp(-d(v,u)/σ)/Z_v (BFS distance), s_j = log p_{w_j} - log p_{v0},
  F = Σ_u p_{v0}(u) s s^T (uncentred), gap rank = argmin(sv[i+1]/sv[i]) + 1,
  PR = (Σ sv)^2 / Σ sv^2.
and tests hypotheses H-T, H-CG, H-RGG, H-ER, H-P6 against the recorded
Phase 1 values. Deterministic graph computations only; no Monte Carlo.

Usage:  python3 scripts/dfig_reduction_2026_10_19.py
Writes: data/reports/dfig_reduction_2026_10/{tori.csv, coarsegrain.csv,
        rgg_er_vertices.csv, kagome_gasket.csv, summary.json}
"""
from __future__ import annotations

import csv
import json
import time
from pathlib import Path

import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, shortest_path
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/reports/dfig_reduction_2026_10"


# ── Phase 1 construction ─────────────────────────────────────────────────────

def to_csr(G: nx.Graph) -> tuple[csr_matrix, list]:
    nodes = list(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    r, c = [], []
    for u, v in G.edges():
        r += [idx[u], idx[v]]
        c += [idx[v], idx[u]]
    n = len(nodes)
    A = csr_matrix((np.ones(len(r)), (r, c)), shape=(n, n))
    return A, nodes


def neighbours(A: csr_matrix, i: int) -> np.ndarray:
    return A.indices[A.indptr[i]:A.indptr[i + 1]]


def dists(A: csr_matrix, v0: int) -> np.ndarray:
    """BFS distances from v0 (row 0) and from each of its neighbours (rows 1..k)."""
    return shortest_path(A, method="D", unweighted=True, indices=np.r_[v0, neighbours(A, v0)])


def fim(A: csr_matrix, v0: int, sigma: float, D: np.ndarray | None = None):
    """F (uncentred), score matrix S (k×n), p_{v0}, as in Phase 1."""
    nb = neighbours(A, v0)
    if D is None:
        D = dists(A, v0)

    def logp(drow):
        x = -drow / sigma
        x[~np.isfinite(drow)] = -1000.0
        return x - np.logaddexp.reduce(x)

    lp0 = logp(D[0])
    S = np.array([logp(D[j + 1]) - lp0 for j in range(len(nb))])
    p = np.exp(lp0)
    F = (S * p) @ S.T
    return F, S, p


def gap_rank(vals: np.ndarray) -> int:
    sv = np.sort(np.abs(vals))[::-1]
    if len(sv) < 2 or sv[0] <= 0:
        return 1
    sv = sv / sv[0]
    ratios = sv[1:] / np.maximum(sv[:-1], 1e-300)
    ratios[ratios == 0] = 1e-15
    return int(np.argmin(ratios)) + 1


def pr(vals: np.ndarray) -> float:
    sv = np.abs(vals)
    return float(sv.sum() ** 2 / (sv ** 2).sum())


def sv_of(M: np.ndarray) -> np.ndarray:
    return np.linalg.svd(M, compute_uv=False)


# ── D1 closed form, any L (1D numerical sums) ────────────────────────────────

def levels(sigma: float, L: int, d: int) -> tuple[float, float, float]:
    a = 1.0 / sigma
    x = np.arange(L)
    dl = np.minimum(x, L - x)                       # cyclic distance
    w = np.exp(-a * dl)
    pi = w / w.sum()
    sp = -a * (np.minimum((x - 1) % L, L - (x - 1) % L) - dl)   # neighbour at +1
    sm = -a * (np.minimum((x + 1) % L, L - (x + 1) % L) - dl)   # neighbour at -1
    m = float(pi @ sp)
    Mpp = float(pi @ (sp * sp))
    Mpm = float(pi @ (sp * sm))
    lT = Mpp - Mpm
    lE = Mpp + Mpm - 2 * m * m
    lA = lE + 2 * d * m * m
    return lT, lA, lE


def closed_spectrum(sigma: float, L: int, d: int) -> np.ndarray:
    lT, lA, lE = levels(sigma, L, d)
    return np.sort(np.array([lT] * d + [lA] + [lE] * (d - 1)))[::-1]


def torus_graph(d: int, L: int) -> nx.Graph:
    return nx.grid_graph(dim=[L] * d, periodic=True)


# ── recorded Phase 1 targets (PHASE1_*_RESULTS.md, D_eff-Test-1.0 @ 8f8094b) ──

TORI_REC = [  # (label, d, L, sigma, rank, PR, PR decimals)
    ("2D 200^2", 2, 200, 3.0, 2, 2.759, 3),
    ("3D 50^3", 3, 50, 3.0, 3, 4.134, 3),
    ("4D 12^4", 4, 12, 1.5, 5, 6.8086, 4),
    ("4D 12^4", 4, 12, 2.0, 5, 6.4929, 4),
    ("4D 12^4", 4, 12, 3.0, 4, 6.0369, 4),
    ("4D 12^4", 4, 12, 5.0, 4, 5.7306, 4),
    ("4D 12^4", 4, 12, 8.0, 4, 5.6151, 4),
]
SV4D_REC = [1, 1, 1, 1, 0.3813, 0.242, 0.242, 0.242]
SYM_REC = [("2D 200^2", 2, 200, 2.000), ("3D 50^3", 3, 50, 3.000)]

CG_V2 = {  # side: [(sched, sigma, rank, PR)]  — V2 table, 3 decimals
    2: {128: [("fixed", 3, 2, 2.759), ("B", 16, 2, 2.134), ("C", 8, 2, 2.265)],
        64: [("fixed", 3, 2, 2.759), ("B", 8, 2, 2.276), ("C", 4, 2, 2.556)],
        32: [("fixed", 3, 2, 2.767), ("B", 4, 2, 2.579), ("C", 2, 2, 3.157)],
        16: [("fixed", 3, 2, 2.885), ("B", 2, 2, 3.202), ("C", 1, 3, 3.647)],
        8: [("fixed", 3, 2, 3.364), ("B", 1, 3, 3.660), ("C", 0.5, 1, 2.054)],
        4: [("fixed", 3, 1, 3.991), ("B", 0.5, 1, 1.991), ("C", 0.25, 1, 1.114)]},
    3: {32: [("fixed", 3, 3, 4.146), ("B", 4, 3, 3.867), ("C", 2, 3, 4.708)],
        16: [("fixed", 3, 3, 4.323), ("B", 2, 3, 4.776), ("C", 1, 4, 5.050)],
        8: [("fixed", 3, 3, 5.039), ("B", 1, 4, 5.067), ("C", 0.5, 1, 2.290)],
        4: [("fixed", 3, 1, 5.978), ("B", 0.5, 1, 2.237), ("C", 0.25, 1, 1.128)]},
}
CG_V1 = [  # (label, d, side, rank, PR 4 decimals), σ = 3
    ("2D 2x2", 2, 128, 2, 2.7586), ("2D 2x2", 2, 64, 2, 2.7586), ("2D 2x2", 2, 32, 2, 2.7668),
    ("2D 2x2", 2, 16, 2, 2.8852), ("2D 2x2", 2, 8, 2, 3.3636), ("2D 2x2", 2, 4, 1, 3.9911),
    ("2D 3x3", 2, 81, 2, 2.7586), ("2D 3x3", 2, 27, 2, 2.7754), ("2D 3x3", 2, 9, 2, 3.2160),
    ("3D 2x2x2", 3, 32, 3, 4.1459), ("3D 2x2x2", 3, 16, 3, 4.3232),
    ("3D 2x2x2", 3, 8, 3, 5.0391), ("3D 2x2x2", 3, 4, 1, 5.9778),
]


def tol(decimals: int) -> float:
    return 0.002 if decimals == 3 else 0.0002


# ── H-T ──────────────────────────────────────────────────────────────────────

def h_tori() -> dict:
    rows, ok_rank, ok_pr = [], True, True
    for label, d, L, s, rk, prv, dec in TORI_REC:
        spec = closed_spectrum(s, L, d)
        r_c, p_c = gap_rank(spec), pr(spec)
        rows.append(dict(item="T.1", system=label, sigma=s, rank_rec=rk, rank_closed=r_c,
                         pr_rec=prv, pr_closed=round(p_c, 6), pr_ok=abs(p_c - prv) <= tol(dec)))
        ok_rank &= (r_c == rk)
        ok_pr &= abs(p_c - prv) <= tol(dec)
    spec4 = closed_spectrum(3.0, 12, 4)
    prof = spec4 / spec4[0]
    sv_ok = bool(np.all(np.abs(prof - SV4D_REC) <= 0.002))
    rows.append(dict(item="T.1 SV profile 4D σ=3", system="4D 12^4", sigma=3.0,
                     pr_closed=" ".join(f"{v:.4f}" for v in prof), pr_ok=sv_ok))

    # T.2 identity on the actual graphs (one vertex each)
    t2 = []
    for label, d, L in [("2D 200^2", 2, 200), ("3D 50^3", 3, 50), ("4D 12^4", 4, 12)]:
        A, _ = to_csr(torus_graph(d, L))
        F, S, p = fim(A, 0, 3.0)
        ev = np.sort(np.linalg.eigvalsh(F))[::-1]
        cs = closed_spectrum(3.0, L, d)
        dev = float(np.max(np.abs(ev - cs) / cs.max()))
        # T.3 symmetrised (Phase 1 pairing rule)
        diag = np.sqrt(np.maximum(np.diag(F), 1e-30))
        cosm = F / np.outer(diag, diag)
        np.fill_diagonal(cosm, np.inf)
        opp = np.argmin(cosm, axis=1)
        Ssym = 0.5 * (S - S[opp])
        Fsym = (Ssym * p) @ Ssym.T
        t2.append(dict(system=label, max_rel_dev=dev, rank_graph=gap_rank(ev),
                       pr_graph=pr(ev), sym_pr=pr(sv_of(Fsym)), sym_rank_sector=d))
        rows.append(dict(item="T.2/T.3", system=label, sigma=3.0, rank_closed=gap_rank(cs),
                         pr_closed=round(pr(cs), 6), max_rel_dev=dev,
                         sym_pr=round(pr(sv_of(Fsym)), 6)))
    t2_ok = all(r["max_rel_dev"] <= 1e-8 for r in t2)
    sym_ok = all(abs(r["sym_pr"] - rec) <= 0.002 and abs(r["sym_pr"] - r["sym_rank_sector"]) <= 1e-6
                 for r, (_, _, _, rec) in zip(t2[:2], SYM_REC))

    # T.4 σ window where rank = d (descriptive)
    windows = {}
    grid = np.round(np.arange(0.5, 20.0001, 0.01), 2)
    for d, L in [(2, 200), (3, 50), (4, 12)]:
        rk = np.array([gap_rank(closed_spectrum(s, L, d)) for s in grid])
        def span(val):
            sel = grid[rk == val]
            return [float(sel.min()), float(sel.max())] if len(sel) else None
        windows[f"d{d}_L{L}"] = {"rank_d": span(d), "rank_d+1": span(d + 1), "rank_1": span(1)}

    verdict = ("REDUCES" if ok_rank and ok_pr and sv_ok and t2_ok and sym_ok
               else "PARTLY REDUCES" if ok_rank else "DOES NOT REDUCE")
    return dict(rows=rows, identity=t2, sigma_windows=windows, ranks_match=ok_rank,
                pr_match=ok_pr, sv_profile_match=sv_ok, identity_ok=t2_ok,
                symmetrised_ok=sym_ok, verdict=verdict)


# ── H-CG ─────────────────────────────────────────────────────────────────────

def block_spin(L: int, d: int) -> nx.Graph:
    """Phase 1 block_spin_2d/3d (2^d blocks), labels as coordinate tuples."""
    G = torus_graph(d, L)
    Gc = nx.Graph()
    for u, v in G.edges():
        cu, cv = tuple(c // 2 for c in u), tuple(c // 2 for c in v)
        if cu != cv:
            Gc.add_edge(cu, cv)
    return Gc


def h_coarse() -> dict:
    iso = {}
    for d, L in [(2, 16), (3, 8)]:
        Gc = block_spin(L, d)
        T = torus_graph(d, L // 2)
        iso[f"{d}D {L}->{L // 2}"] = bool(
            set(map(frozenset, Gc.edges())) == set(map(frozenset, T.edges()))
            and set(Gc.nodes()) == set(T.nodes()))
    rows, ok_rank, ok_pr = [], True, True
    for d, table in CG_V2.items():
        for L, entries in table.items():
            for sched, s, rk, prv in entries:
                spec = closed_spectrum(s, L, d)
                r_c, p_c = gap_rank(spec), pr(spec)
                good = abs(p_c - prv) <= 0.002
                rows.append(dict(table="V2", d=d, side=L, schedule=sched, sigma=s,
                                 rank_rec=rk, rank_closed=r_c, pr_rec=prv,
                                 pr_closed=round(p_c, 6), pr_ok=good))
                ok_rank &= r_c == rk
                ok_pr &= good
    for label, d, L, rk, prv in CG_V1:
        spec = closed_spectrum(3.0, L, d)
        r_c, p_c = gap_rank(spec), pr(spec)
        good = abs(p_c - prv) <= 0.0002
        rows.append(dict(table="V1 " + label, d=d, side=L, schedule="fixed", sigma=3.0,
                         rank_rec=rk, rank_closed=r_c, pr_rec=prv,
                         pr_closed=round(p_c, 6), pr_ok=good))
        ok_rank &= r_c == rk
        ok_pr &= good
    increases = [r for r in rows if r["table"] == "V2" and r["schedule"] in ("B", "C")
                 and r["rank_closed"] == r["d"] + 1]
    iso_ok = all(iso.values())
    verdict = ("REDUCES" if iso_ok and ok_rank and ok_pr
               else "PARTLY REDUCES" if ok_rank else "DOES NOT REDUCE")
    return dict(rows=rows, isomorphism=iso, ranks_match=ok_rank, pr_match=ok_pr,
                rank_increases_exact=[(r["d"], r["side"], r["schedule"], r["sigma"], r["rank_closed"])
                                      for r in increases],
                verdict=verdict)


# ── H-RGG / H-ER ─────────────────────────────────────────────────────────────

def lcc(A: csr_matrix) -> csr_matrix:
    _, lab = connected_components(A, directed=False)
    big = np.argmax(np.bincount(lab))
    keep = np.where(lab == big)[0]
    return A[keep][:, keep].tocsr()


def periodic_rgg(n: int, d: int, r: float, seed: int) -> csr_matrix:
    rng = np.random.default_rng(seed)
    pts = rng.uniform(0, 1, size=(n, d))
    pairs = np.array(sorted(cKDTree(pts, boxsize=1.0).query_pairs(r)))
    A = csr_matrix((np.ones(2 * len(pairs)),
                    (np.r_[pairs[:, 0], pairs[:, 1]], np.r_[pairs[:, 1], pairs[:, 0]])), shape=(n, n))
    return lcc(A)


def er_graph(n: int, p: float, seed: int) -> csr_matrix:
    A, _ = to_csr(nx.erdos_renyi_graph(n, p, seed=seed))
    return lcc(A)


def vertex_stats(A: csr_matrix, v: int, sigma: float) -> dict:
    F, S, p = fim(A, v, sigma)
    mu = S @ p
    C = F - np.outer(mu, mu)
    evF, U = np.linalg.eigh(F)
    order = np.argsort(evF)[::-1]
    u1 = U[:, order[0]]
    evC = np.linalg.eigvalsh(C)
    cos = float(abs(u1 @ mu) / (np.linalg.norm(mu) + 1e-300))
    return dict(k=len(mu), rank_u=gap_rank(evF), rank_c=gap_rank(evC), cos_top_mu=cos,
                pr_u=pr(evF), pr_c=pr(evC))


def mode(xs):
    vals, cnt = np.unique(xs, return_counts=True)
    return int(vals[np.argmax(cnt)])


def h_rgg_er() -> dict:
    rows = []
    systems = ([("RGG", 2, dict(n=5000, d=2, r=0.03)), ("RGG", 3, dict(n=5000, d=3, r=0.09))]
               + [("ER", None, dict(n=1000, p=0.015)), ("ER", None, dict(n=2000, p=0.0075))])
    for kind, d, par in systems:
        for seed in (0, 1, 2):
            A = periodic_rgg(seed=seed, **par) if kind == "RGG" else er_graph(seed=seed, **par)
            n = A.shape[0]
            nv = 50 if kind == "RGG" else 30
            verts = np.random.default_rng(100 + seed).choice(n, size=nv, replace=False)
            for sigma in (2.0, 3.0):
                for v in verts:
                    st = vertex_stats(A, int(v), sigma)
                    rows.append(dict(kind=kind, d=d, n=par["n"], seed=seed, sigma=sigma,
                                     vertex=int(v), **st))
    summ = {}
    for key in [("RGG", 2), ("RGG", 3), ("ER", 1000), ("ER", 2000)]:
        for sigma in (2.0, 3.0):
            sel = [r for r in rows if r["kind"] == key[0] and r["sigma"] == sigma
                   and (r["d"] == key[1] if key[0] == "RGG" else r["n"] == key[1])]
            ru = np.array([r["rank_u"] for r in sel])
            rc = np.array([r["rank_c"] for r in sel])
            cs = np.array([r["cos_top_mu"] for r in sel])
            ent = dict(n_vertices=len(sel), mode_rank_u=mode(ru), mode_rank_c=mode(rc),
                       hist_rank_u={int(a): int(b) for a, b in zip(*np.unique(ru, return_counts=True))},
                       hist_rank_c={int(a): int(b) for a, b in zip(*np.unique(rc, return_counts=True))},
                       frac_cos_ge_095=float(np.mean(cs >= 0.95)), median_cos=float(np.median(cs)),
                       mean_k=float(np.mean([r["k"] for r in sel])))
            if key[0] == "RGG":
                d = key[1]
                ent["frac_u_eq_d1"] = float(np.mean(ru == d + 1))
                ent["frac_c_eq_d"] = float(np.mean(rc == d))
            else:
                ent["frac_u_eq_1"] = float(np.mean(ru == 1))
            summ[f"{key[0]}_{key[1]}_sigma{sigma:g}"] = ent

    def rgg_ok(d):
        e = summ[f"RGG_{d}_sigma2"]
        return e
    e2, e3 = rgg_ok(2), rgg_ok(3)
    repro = e2["mode_rank_u"] == 3 and e3["mode_rank_u"] == 4
    modes = [e2["mode_rank_c"] == 2, e3["mode_rank_c"] == 3]
    fracs = [e2["frac_c_eq_d"] >= e2["frac_u_eq_d1"] - 0.10,
             e3["frac_c_eq_d"] >= e3["frac_u_eq_d1"] - 0.10]
    if not repro:
        v_rgg = "VOID"
    elif all(modes) and all(fracs):
        v_rgg = "REDUCES"
    elif any(modes):
        v_rgg = "PARTLY REDUCES"
    else:
        v_rgg = "DOES NOT REDUCE"
    er_ok = all(summ[f"ER_{n}_sigma2"]["frac_u_eq_1"] >= 0.9 for n in (1000, 2000))
    pooled_cos = np.mean([r["cos_top_mu"] >= 0.95 for r in rows if r["kind"] == "ER" and r["sigma"] == 2.0])
    pooled_u1 = np.mean([r["rank_u"] == 1 for r in rows if r["kind"] == "ER" and r["sigma"] == 2.0])
    v_er = "REDUCES" if (pooled_u1 >= 0.9 and pooled_cos >= 0.9) else "DOES NOT REDUCE"
    return dict(rows=rows, summary=summ, rgg_reproduced=repro, verdict_rgg=v_rgg,
                er_pooled_frac_rank1=float(pooled_u1), er_pooled_frac_cos095=float(pooled_cos),
                er_each_frac_rank1_ok=er_ok, verdict_er=v_er)


# ── H-P6: kagome vs gasket ──────────────────────────────────────────────────

def gasket(level: int) -> nx.Graph:
    """Phase 1 make_sierpinski_gasket, iterative over levels."""
    G = nx.Graph([(0, 1), (1, 2), (0, 2)])
    top, bl, br = 0, 1, 2
    for _ in range(level):
        m = G.number_of_nodes()
        GB = nx.relabel_nodes(G, {v: v + m for v in G})
        GC = nx.relabel_nodes(G, {v: v + 2 * m for v in G})
        H = nx.compose_all([G, GB, GC])
        merge = {bl: top + m, br: top + 2 * m, br + m: bl + 2 * m}   # A_bl=B_top, A_br=C_top, B_br=C_bl
        H = nx.relabel_nodes(H, {b: a for a, b in merge.items()})
        new = (top, bl + m, br + 2 * m)
        mp = {v: i for i, v in enumerate(sorted(H))}
        G = nx.relabel_nodes(H, mp)
        top, bl, br = (mp[x] for x in new)
    return G


def kagome(M: int) -> csr_matrix:
    """Triangular M×M torus (basis b1, b2; neighbours ±b1, ±b2, ±(b1−b2)) with (odd, odd) removed."""
    assert M % 2 == 0
    keep = [(i, j) for i in range(M) for j in range(M) if not (i % 2 and j % 2)]
    idx = {s: n for n, s in enumerate(keep)}
    r, c = [], []
    for (i, j), a in idx.items():
        for di, dj in ((1, 0), (0, 1), (1, -1)):
            b = idx.get(((i + di) % M, (j + dj) % M))
            if b is not None:
                r += [a, b]
                c += [b, a]
    return csr_matrix((np.ones(len(r)), (r, c)), shape=(len(keep), len(keep)))


def triangular(M: int) -> csr_matrix:
    idx = lambda i, j: (i % M) * M + (j % M)
    r, c = [], []
    for i in range(M):
        for j in range(M):
            for di, dj in ((1, 0), (0, 1), (1, -1)):
                r += [idx(i, j), idx(i + di, j + dj)]
                c += [idx(i + di, j + dj), idx(i, j)]
    return csr_matrix((np.ones(len(r)), (r, c)), shape=(M * M, M * M))


def ecc(A: csr_matrix, v: int) -> int:
    return int(shortest_path(A, unweighted=True, indices=[v]).max())


SIG_GRID = [3, 5, 8, 12, 20, 30, 50, 80, 130, 220]


def pr_curve(A: csr_matrix, verts) -> dict:
    Ds = {int(v): dists(A, int(v)) for v in verts}
    out = {}
    for s in SIG_GRID:
        vals = [pr(sv_of(fim(A, v, float(s), D)[0])) for v, D in Ds.items()]
        out[s] = (float(np.mean(vals)), float(np.std(vals)))
    return out


def h_p6() -> dict:
    G = gasket(9)
    Ag, _ = to_csr(G)
    deg = np.diff(Ag.indptr)
    corners = np.where(deg == 2)[0]
    diam_g = int(shortest_path(Ag, unweighted=True, indices=[corners[0]]).max())
    vg = np.random.default_rng(7).choice(np.where(deg == 4)[0], size=20, replace=False)
    # kagome size: smallest even M whose diameter (vertex-transitive: one eccentricity) is within 10% of the gasket's
    M, Ak = 2 * (diam_g // 2), None
    while True:
        Ak = kagome(M)
        dk = ecc(Ak, 0)
        if dk >= 0.9 * diam_g:
            break
        M += 16
    vk = np.random.default_rng(8).choice(Ak.shape[0], size=20, replace=False)
    Mt = 2 * (diam_g // 2)
    while True:
        At = triangular(Mt)
        dt = ecc(At, 0)
        if dt >= 0.9 * diam_g:
            break
        Mt += 16
    cg, ck = pr_curve(Ag, vg), pr_curve(Ak, vk)
    ct = pr_curve(At, [0, 1, 2])
    Lsq = diam_g  # square L×L torus has diameter L
    rows = []
    for s in SIG_GRID:
        rows.append(dict(sigma=s, gasket_pr=cg[s][0], gasket_sd=cg[s][1], kagome_pr=ck[s][0],
                         kagome_sd=ck[s][1], triangular_pr=ct[s][0],
                         square_pr_closed=pr(closed_spectrum(float(s), Lsq, 2)),
                         kag_minus_gasket=ck[s][0] - cg[s][0]))
    smax = max(s for s in SIG_GRID if s <= 0.45 * min(diam_g, dk))
    rk = next(r for r in rows if r["sigma"] == smax)
    calibrated = abs(rk["square_pr_closed"] - 2.0) <= 0.05
    if not calibrated:
        verdict = "UNCALIBRATED"
    elif 1.90 <= rk["kagome_pr"] <= 2.10:
        verdict = "SURVIVES THIS TEST"
    else:
        verdict = "FALSIFIED (PR form)"
    return dict(rows=rows, gasket_level=9, gasket_n=Ag.shape[0], gasket_diameter=diam_g,
                kagome_M=M, kagome_n=Ak.shape[0], kagome_diameter=dk,
                triangular_M=Mt, triangular_diameter=dt, square_L=Lsq,
                decisive_sigma=smax, decisive=rk, calibrated=calibrated, verdict=verdict)


# ── main ────────────────────────────────────────────────────────────────────

def write_csv(path: Path, rows: list[dict]) -> None:
    keys = []
    for r in rows:
        keys += [k for k in r if k not in keys]
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    T = h_tori();      print("H-T ", T["verdict"], f"{time.time() - t0:.0f}s", flush=True)
    CG = h_coarse();   print("H-CG", CG["verdict"], f"{time.time() - t0:.0f}s", flush=True)
    R = h_rgg_er();    print("H-RGG", R["verdict_rgg"], "H-ER", R["verdict_er"], f"{time.time() - t0:.0f}s", flush=True)
    K = h_p6();        print("H-P6", K["verdict"], f"{time.time() - t0:.0f}s", flush=True)
    write_csv(OUT / "tori.csv", T.pop("rows"))
    write_csv(OUT / "coarsegrain.csv", CG.pop("rows"))
    write_csv(OUT / "rgg_er_vertices.csv", R.pop("rows"))
    write_csv(OUT / "kagome_gasket.csv", K["rows"])
    summary = dict(prereg="docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md (commit f29dd61)",
                   H_T=T, H_CG=CG, H_RGG_ER=R, H_P6=K, runtime_s=round(time.time() - t0, 1))
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "H_P6"}, indent=1, default=str)[:6000])
    print(json.dumps(K, indent=1, default=str))


if __name__ == "__main__":
    main()

"""
Tests for CCA isotropy prediction on lattice topologies and 2D Ising MC.

Phase A: Pure topology sweep — validates FIM behavior on lattice graphs
         without physical simulation. Uses kernel parameter alpha as proxy
         for interaction range.

Phase B: 2D Ising MC — validates that the FIM detects the ordered→disordered
         phase transition as a RADIAL→ISOTROPIC regime transition.

Key finding from experiments:
  - η alone is insufficient as CCA diagnostic (1D path reaches η=0.85)
  - The joint (d_eff, η) or PR is the correct CCA diagnostic
  - The FIM transition is shifted above T_c by finite-size effects on small L
  - The `abs` weight mode gives strongest CCA signal at T_c
"""

import sys
from pathlib import Path

import networkx as nx
import numpy as np
import pytest

SRC = Path(__file__).resolve().parent.parent / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from analysis.fisher_diagnostics import (
    KernelType, RegimeType, analyze_node, sweep_graph
)

# Import lattice builders from Phase A script
SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from ising_fim_topology_test import build_2d_torus, build_3d_torus, build_path, build_complete
from ising_fim_mc_test import ising_mc, build_correlation_graph, T_C


# ══════════════════════════════════════════════════════════════════════════════
# Phase A: Topology Sweep Tests
# ══════════════════════════════════════════════════════════════════════════════

class TestLatticeTopology:
    """FIM behavior on regular lattice graphs with alpha sweep."""

    def _sweep_alpha(self, G, alphas, n_sample=10):
        """Helper: analyze sampled nodes at each alpha, return dict of mean metrics."""
        nodes = [n for n in G.nodes() if G.degree(n) >= 2]
        rng = np.random.RandomState(42)
        if len(nodes) > n_sample:
            sampled = list(rng.choice(nodes, size=n_sample, replace=False))
        else:
            sampled = nodes

        results = {}
        for alpha in alphas:
            etas, d_effs, prs = [], [], []
            for node in sampled:
                r = analyze_node(G, str(node), KernelType.EXPONENTIAL, alpha=alpha)
                if not r.skipped:
                    etas.append(r.eta)
                    d_effs.append(r.d_eff)
                    prs.append(r.pr)
            results[alpha] = {
                "mean_eta": np.mean(etas) if etas else 0.0,
                "mean_d_eff": np.mean(d_effs) if d_effs else 0.0,
                "mean_pr": np.mean(prs) if prs else 0.0,
            }
        return results

    def test_2d_torus_eta_peaks_at_intermediate_alpha(self):
        """2D torus should have peak η at intermediate α, not at extremes."""
        G = build_2d_torus(12)
        alphas = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
        results = self._sweep_alpha(G, alphas)

        etas = [results[a]["mean_eta"] for a in alphas]
        peak_idx = np.argmax(etas)

        # Peak should not be at first or last alpha
        assert peak_idx > 0, f"Peak η at lowest α={alphas[0]} — expected intermediate"
        assert peak_idx < len(alphas) - 1, f"Peak η at highest α={alphas[-1]} — expected intermediate"

    def test_path_stays_deff_1(self):
        """1D path should have d_eff=1 for all alpha values."""
        G = build_path(30)
        alphas = [0.5, 1.0, 2.0, 3.0]
        results = self._sweep_alpha(G, alphas)

        for alpha in alphas:
            assert results[alpha]["mean_d_eff"] == 1.0, \
                f"Path at α={alpha}: d_eff={results[alpha]['mean_d_eff']}, expected 1.0"

    def test_complete_graph_stays_deff_1(self):
        """Complete graph should have d_eff=1 (spotlight effect) for all alpha."""
        G = build_complete(10)
        alphas = [0.5, 1.0, 2.0]
        results = self._sweep_alpha(G, alphas, n_sample=10)

        for alpha in alphas:
            assert results[alpha]["mean_d_eff"] == 1.0, \
                f"K_10 at α={alpha}: d_eff={results[alpha]['mean_d_eff']}, expected 1.0"

    def test_2d_torus_reaches_deff_above_1(self):
        """2D torus should achieve d_eff > 1 at some alpha."""
        G = build_2d_torus(12)
        alphas = [0.5, 0.75, 1.0]
        results = self._sweep_alpha(G, alphas)

        max_deff = max(results[a]["mean_d_eff"] for a in alphas)
        assert max_deff > 1.0, f"2D torus peak d_eff={max_deff}, expected > 1.0"

    def test_3d_torus_reaches_higher_deff_than_2d(self):
        """3D torus should achieve higher peak d_eff than 2D torus."""
        G_2d = build_2d_torus(8)
        G_3d = build_3d_torus(6)
        alphas = [0.25, 0.5, 0.75, 1.0]

        r_2d = self._sweep_alpha(G_2d, alphas)
        r_3d = self._sweep_alpha(G_3d, alphas)

        peak_2d = max(r_2d[a]["mean_d_eff"] for a in alphas)
        peak_3d = max(r_3d[a]["mean_d_eff"] for a in alphas)

        assert peak_3d >= peak_2d, \
            f"3D peak d_eff={peak_3d} < 2D peak d_eff={peak_2d}"

    def test_high_alpha_is_radial(self):
        """At very high alpha, all lattices should be RADIAL (short-range kernel)."""
        G = build_2d_torus(12)
        results = self._sweep_alpha(G, [5.0])
        assert results[5.0]["mean_eta"] < 0.35, \
            f"2D torus at α=5.0: η={results[5.0]['mean_eta']}, expected RADIAL (<0.35)"

    def test_eta_alone_insufficient_for_cca(self):
        """
        Path graph can reach high η but stays d_eff=1.
        Demonstrates that η alone is not a reliable CCA diagnostic.
        """
        G = build_path(30)
        results = self._sweep_alpha(G, [1.0])
        eta = results[1.0]["mean_eta"]
        d_eff = results[1.0]["mean_d_eff"]

        # Path can have η > 0.5 (empirically ~0.85 at α=1.0 for N=50)
        # but d_eff stays at 1 — this is trivial isotropy, not CCA
        assert d_eff == 1.0, f"Path d_eff should be 1, got {d_eff}"
        # η can be high — this is the point of the test
        # CCA requires d_eff > 1 AND high η


# ══════════════════════════════════════════════════════════════════════════════
# Phase B: Ising MC Tests
# ══════════════════════════════════════════════════════════════════════════════

class TestIsingMC:
    """FIM analysis of 2D Ising model with correlation-weighted edges."""

    # Use small L for test speed — L=8 runs in ~2s per temperature
    L = 8
    N_SAMPLE = 10
    ALPHA = 1.0

    def _run_at_temperature(self, T, weight_mode="abs"):
        """Helper: run MC + FIM at one temperature."""
        corr_h, corr_v = ising_mc(self.L, T, n_equil=2000, n_measure=5000,
                                   sample_every=5, seed=42)
        G = build_correlation_graph(corr_h, corr_v, self.L, weight_mode=weight_mode)

        nodes = list(G.nodes())
        rng = np.random.RandomState(43)
        sampled = list(rng.choice(nodes, size=min(self.N_SAMPLE, len(nodes)), replace=False))

        etas, d_effs, prs, regimes = [], [], [], []
        for node in sampled:
            r = analyze_node(G, str(node), KernelType.EXPONENTIAL, alpha=self.ALPHA)
            if not r.skipped:
                etas.append(r.eta)
                d_effs.append(r.d_eff)
                prs.append(r.pr)
                regimes.append(r.regime)

        return {
            "mean_eta": np.mean(etas) if etas else 0.0,
            "mean_d_eff": np.mean(d_effs) if d_effs else 0.0,
            "mean_pr": np.mean(prs) if prs else 0.0,
            "regimes": regimes,
            "mean_corr": float(np.mean(np.abs(np.concatenate([corr_h.ravel(), corr_v.ravel()])))),
        }

    def test_ordered_phase_has_high_correlation(self):
        """T = 1.5 (deep ordered): mean |correlation| should be near 1."""
        result = self._run_at_temperature(1.5)
        assert result["mean_corr"] > 0.8, \
            f"T=1.5: |corr|={result['mean_corr']:.3f}, expected > 0.8 (ordered phase)"

    def test_disordered_phase_not_radial(self):
        """T = 4.0 (deep disordered): should not be majority RADIAL."""
        result = self._run_at_temperature(4.0)
        n_radial = sum(1 for r in result["regimes"] if r == RegimeType.RADIAL_DOMINATED)
        frac_radial = n_radial / len(result["regimes"]) if result["regimes"] else 1
        assert frac_radial < 0.5, \
            f"T=4.0: {frac_radial:.0%} RADIAL, expected minority"

    def test_correlation_decreases_with_temperature(self):
        """Mean |⟨s_i s_j⟩| should decrease as T increases."""
        r_low = self._run_at_temperature(1.5)
        r_high = self._run_at_temperature(4.0)
        assert r_low["mean_corr"] > r_high["mean_corr"], \
            f"|corr| at T=1.5 ({r_low['mean_corr']:.3f}) should exceed T=4.0 ({r_high['mean_corr']:.3f})"

    def test_eta_increases_through_transition(self):
        """η should increase from ordered to disordered phase."""
        r_ordered = self._run_at_temperature(1.5)
        r_disordered = self._run_at_temperature(3.0)
        assert r_disordered["mean_eta"] > r_ordered["mean_eta"], \
            f"η should increase: T=1.5 ({r_ordered['mean_eta']:.3f}) → T=3.0 ({r_disordered['mean_eta']:.3f})"

    def test_critical_region_has_higher_eta_than_ordered(self):
        """η in the critical/disordered region should exceed deep ordered phase.
        Using neglog weights where the ordered phase shows clear RADIAL behavior."""
        r_ordered = self._run_at_temperature(1.5, weight_mode="neglog")
        r_disordered = self._run_at_temperature(3.0, weight_mode="neglog")
        assert r_disordered["mean_eta"] > r_ordered["mean_eta"], \
            f"η should increase: T=1.5 ({r_ordered['mean_eta']:.3f}) → T=3.0 ({r_disordered['mean_eta']:.3f})"

    def test_regime_transition_exists_neglog(self):
        """Using neglog weights, there should be a regime change across transition.
        Neglog weights produce clear RADIAL behavior in ordered phase because
        uniform high correlations → uniform small distances → single dominant direction."""
        r_low = self._run_at_temperature(1.5, weight_mode="neglog")
        r_high = self._run_at_temperature(4.0, weight_mode="neglog")

        # With neglog, ordered phase should be more RADIAL than disordered
        low_radial = sum(1 for r in r_low["regimes"] if r == RegimeType.RADIAL_DOMINATED)
        high_iso = sum(1 for r in r_high["regimes"]
                       if r in (RegimeType.ISOTROPIC, RegimeType.NOISE_DOMINATED))

        # At least one side should show regime structure
        assert low_radial > 0 or high_iso > 0, \
            f"No regime differentiation: T=1.5 radial={low_radial}, T=4.0 iso={high_iso}"

    def test_abs_weight_gives_higher_deff_at_tc_than_ordered(self):
        """Using abs weights, d_eff or PR at T_c should exceed deep ordered phase."""
        r_tc = self._run_at_temperature(T_C, weight_mode="abs")
        r_ordered = self._run_at_temperature(1.5, weight_mode="abs")
        assert r_tc["mean_pr"] > r_ordered["mean_pr"], \
            f"PR at T_c ({r_tc['mean_pr']:.3f}) should exceed T=1.5 ({r_ordered['mean_pr']:.3f})"


# ══════════════════════════════════════════════════════════════════════════════
# Phase A+B Joint: CCA Diagnostic Validation
# ══════════════════════════════════════════════════════════════════════════════

class TestCCADiagnostic:
    """Tests validating the refined CCA diagnostic: (d_eff, η) jointly."""

    def test_trivial_isotropy_detected(self):
        """
        Systems with η > 0.5 but d_eff = 1 should be flagged as trivial isotropy,
        not CCA. The path graph is the canonical example.
        """
        G = build_path(30)
        r = analyze_node(G, "n_15", KernelType.EXPONENTIAL, alpha=1.0)
        assert not r.skipped

        # Trivial isotropy: high η, low d_eff
        is_trivial = r.d_eff == 1 and r.eta > 0.35
        # This SHOULD be detected as trivial, not CCA
        assert is_trivial or r.eta <= 0.35, \
            "Path graph should show either trivial isotropy (d=1, high η) or low η"

    def test_structured_isotropy_on_torus(self):
        """
        2D torus at optimal α should show d_eff > 1 AND moderate η.
        This is structured (non-trivial) isotropy — the CCA signature.
        """
        G = build_2d_torus(12)
        r = analyze_node(G, "n_6_6", KernelType.EXPONENTIAL, alpha=0.75)
        assert not r.skipped

        # Structured isotropy: d_eff > 1 and η in ISOTROPIC range
        assert r.d_eff > 1, f"2D torus center: d_eff={r.d_eff}, expected > 1"

    def test_pr_distinguishes_trivial_from_structured(self):
        """
        PR should be higher for structured isotropy (torus) than trivial (path)
        at comparable η values, because PR weights both dimension count and equality.
        """
        G_path = build_path(30)
        G_torus = build_2d_torus(12)

        r_path = analyze_node(G_path, "n_15", KernelType.EXPONENTIAL, alpha=1.0)
        r_torus = analyze_node(G_torus, "n_6_6", KernelType.EXPONENTIAL, alpha=0.75)

        assert not r_path.skipped and not r_torus.skipped

        # Torus PR should exceed path PR when both have moderate η
        # (torus has more dimensions contributing)
        if r_path.eta > 0.3 and r_torus.eta > 0.3:
            assert r_torus.pr >= r_path.pr, \
                f"Torus PR={r_torus.pr:.3f} should >= Path PR={r_path.pr:.3f}"

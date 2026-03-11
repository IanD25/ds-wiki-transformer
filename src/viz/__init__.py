"""
viz/ — Cross-universe bridge visualization package.

Generates static PNG (matplotlib) and interactive HTML (plotly) outputs
from RRP bundle cross_universe_bridges data.

Usage:
    from viz import BridgeNetwork, SimilarityHist, DomainHeatmap, run_all_viz

    # Individual generators
    BridgeNetwork(bundle_db, ds_wiki_db).generate(output_dir)
    SimilarityHist(bundle_db).generate(output_dir)
    DomainHeatmap(bundle_db, ds_wiki_db).generate(output_dir)

    # All at once
    run_all_viz("data/rrp/zoo_classes/rrp_zoo_classes.db")
"""

def __getattr__(name):
    """Lazy-load submodules so partial installs don't block each other."""
    if name == "BridgeNetwork":
        from .bridge_network import BridgeNetwork
        return BridgeNetwork
    if name == "SimilarityHist":
        from .similarity_hist import SimilarityHist
        return SimilarityHist
    if name == "DomainHeatmap":
        from .domain_heatmap import DomainHeatmap
        return DomainHeatmap
    if name == "run_all_viz":
        from .viz_runner import run_all_viz
        return run_all_viz
    raise AttributeError(f"module 'viz' has no attribute {name!r}")

__all__ = ["BridgeNetwork", "SimilarityHist", "DomainHeatmap", "run_all_viz"]

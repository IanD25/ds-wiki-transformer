#!/usr/bin/env python3
"""
viz_network.py — Generate cross-universe bridge network for an RRP bundle.

Bipartite graph: DS Wiki entries (left) ↔ RRP entries (right).
Default threshold 0.82 keeps ~432 edges — the readable zone.
Below 0.80 the graph becomes a hairball; use viz_heatmap.py to explore the full set.

Usage:
    python scripts/viz_network.py data/rrp/zoo_classes/rrp_zoo_classes.db
    python scripts/viz_network.py data/rrp/zoo_classes/rrp_zoo_classes.db --threshold 0.85
    python scripts/viz_network.py data/rrp/zoo_classes/rrp_zoo_classes.db --ds data/ds_wiki.db
"""

import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from viz.bridge_network import BridgeNetwork
from viz.viz_runner     import _derive_output_dir

try:
    from config import SOURCE_DB
    _default_ds = str(SOURCE_DB)
except ImportError:
    _default_ds = "data/ds_wiki.db"


def main():
    parser = argparse.ArgumentParser(
        description="Cross-universe bridge network visualization for an RRP bundle."
    )
    parser.add_argument("bundle_db", help="Path to RRP bundle .db file")
    parser.add_argument("--ds",  default=_default_ds,
                        help=f"Path to ds_wiki.db (default: {_default_ds})")
    parser.add_argument("--threshold", type=float, default=0.82,
                        help="Minimum similarity (default: 0.82). Below 0.80 → hairball.")
    parser.add_argument("--out", default=None,
                        help="Output directory (default: data/viz/{bundle_name}/)")
    args = parser.parse_args()

    output_dir = Path(args.out) if args.out else _derive_output_dir(args.bundle_db)

    print(f"Bridge Network Visualization")
    print(f"  Bundle   : {args.bundle_db}")
    print(f"  DS Wiki  : {args.ds}")
    print(f"  Threshold: sim >= {args.threshold}")
    print(f"  Output   : {output_dir}")

    result = BridgeNetwork(args.bundle_db, args.ds).generate(
        output_dir    = output_dir,
        sim_threshold = args.threshold,
    )

    print(f"\n  PNG  : {result['png']}")
    print(f"  HTML : {result['html']}")
    print(f"  Stats: {result['stats']}")


if __name__ == "__main__":
    main()

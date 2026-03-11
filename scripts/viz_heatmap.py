#!/usr/bin/env python3
"""
viz_heatmap.py — Generate bridge-density heatmap for an RRP bundle.

Rows = RRP source type (theorems/classes/conjectures/problems)
Cols = DS Wiki type_group (RL, Q, X, H, M, T, B, F, E, Ax, Other)

Usage:
    python scripts/viz_heatmap.py data/rrp/zoo_classes/rrp_zoo_classes.db
    python scripts/viz_heatmap.py data/rrp/zoo_classes/rrp_zoo_classes.db --ds data/ds_wiki.db
    python scripts/viz_heatmap.py data/rrp/zoo_classes/rrp_zoo_classes.db --threshold 0.80
"""

import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from viz.domain_heatmap import DomainHeatmap
from viz.viz_runner     import _derive_output_dir

try:
    from config import SOURCE_DB
    _default_ds = str(SOURCE_DB)
except ImportError:
    _default_ds = "data/ds_wiki.db"


def main():
    parser = argparse.ArgumentParser(
        description="Bridge-density heatmap for an RRP bundle."
    )
    parser.add_argument("bundle_db", help="Path to RRP bundle .db file")
    parser.add_argument("--ds",  default=_default_ds,
                        help=f"Path to ds_wiki.db (default: {_default_ds})")
    parser.add_argument("--threshold", type=float, default=0.75,
                        help="Minimum similarity to include (default: 0.75)")
    parser.add_argument("--out", default=None,
                        help="Output directory (default: data/viz/{bundle_name}/)")
    args = parser.parse_args()

    output_dir = Path(args.out) if args.out else _derive_output_dir(args.bundle_db)

    print(f"Domain Heatmap")
    print(f"  Bundle   : {args.bundle_db}")
    print(f"  DS Wiki  : {args.ds}")
    print(f"  Threshold: sim >= {args.threshold}")
    print(f"  Output   : {output_dir}")

    result = DomainHeatmap(args.bundle_db, args.ds).generate(
        output_dir    = output_dir,
        sim_threshold = args.threshold,
    )

    print(f"\n  PNG  : {result['png']}")
    print(f"  HTML : {result['html']}")
    print(f"  Stats: {result['stats']}")


if __name__ == "__main__":
    main()

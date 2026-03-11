#!/usr/bin/env python3
"""
viz_hist.py — Generate similarity distribution histogram for an RRP bundle.

Usage:
    python scripts/viz_hist.py data/rrp/zoo_classes/rrp_zoo_classes.db
    python scripts/viz_hist.py data/rrp/zoo_classes/rrp_zoo_classes.db --threshold 0.80
    python scripts/viz_hist.py data/rrp/zoo_classes/rrp_zoo_classes.db --out data/viz/custom/
"""

import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from viz.similarity_hist import SimilarityHist
from viz.viz_runner      import _derive_output_dir


def main():
    parser = argparse.ArgumentParser(
        description="Similarity distribution histogram for an RRP bundle."
    )
    parser.add_argument("bundle_db", help="Path to RRP bundle .db file")
    parser.add_argument("--threshold", type=float, default=0.75,
                        help="Minimum similarity to include (default: 0.75)")
    parser.add_argument("--out", default=None,
                        help="Output directory (default: data/viz/{bundle_name}/)")
    args = parser.parse_args()

    output_dir = Path(args.out) if args.out else _derive_output_dir(args.bundle_db)

    print(f"Similarity Distribution Histogram")
    print(f"  Bundle   : {args.bundle_db}")
    print(f"  Threshold: sim >= {args.threshold}")
    print(f"  Output   : {output_dir}")

    result = SimilarityHist(args.bundle_db).generate(
        output_dir    = output_dir,
        sim_threshold = args.threshold,
    )

    print(f"\n  PNG  : {result['png']}")
    print(f"  HTML : {result['html']}")
    print(f"  Stats: {result['stats']}")


if __name__ == "__main__":
    main()

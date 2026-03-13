"""
run_spt.py — CLI for the Semantic Position Test (SPT)

STATUS: PROTOTYPE — see src/analysis/semantic_position_test.py for known limitations.
        Not part of the active pipeline. Parked pending resolution of the SEO
        contamination problem in the α score calculation.

Compares three pre-built RRP variant databases (neutral / supportive / critical)
to compute per-entry α scores. No API calls — the skew lives in the intake prompt
that created each database.

Usage:
    python scripts/run_spt.py \
        --neutral    data/rrp/opera/rrp_opera.db \
        --supportive data/rrp/opera/rrp_opera_S.db \
        --critical   data/rrp/opera/rrp_opera_C.db \
        [--chroma    data/chroma_db] \
        [--output    data/reports/opera/spt_result.json]

See src/analysis/semantic_position_test.py for the intake prompt variants
(SPT_SYSTEM_NEUTRAL / SPT_SYSTEM_SUPPORTIVE / SPT_SYSTEM_CRITICAL) to embed
in your LLM parser when generating the three database variants.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from analysis.semantic_position_test import run_spt, print_spt_report, save_spt_json


def main():
    parser = argparse.ArgumentParser(
        description="Run Semantic Position Test across three RRP variant databases."
    )
    parser.add_argument("--neutral",    required=True, help="RRP built with neutral intake prompt")
    parser.add_argument("--supportive", required=True, help="RRP built with supportive intake prompt")
    parser.add_argument("--critical",   required=True, help="RRP built with critical intake prompt")
    parser.add_argument("--chroma",     default="data/chroma_db", help="ChromaDB directory")
    parser.add_argument("--output",     default=None, help="JSON output path (optional)")
    args = parser.parse_args()

    for path_str, label in [
        (args.neutral, "--neutral"),
        (args.supportive, "--supportive"),
        (args.critical, "--critical"),
    ]:
        if not Path(path_str).exists():
            print(f"ERROR: {label} database not found: {path_str}")
            sys.exit(1)

    result = run_spt(
        db_neutral=args.neutral,
        db_supportive=args.supportive,
        db_critical=args.critical,
        chroma_dir=args.chroma,
    )

    print_spt_report(result)

    output_path = args.output or (
        Path("data/reports") / Path(args.neutral).stem.replace("rrp_", "") / "spt_result.json"
    )
    save_spt_json(result, output_path)


if __name__ == "__main__":
    main()

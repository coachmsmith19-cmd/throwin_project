"""
master_pipeline.py

Main entrypoint for running throw-in analysis.

Usage:
    python master_pipeline.py --analyze
    python master_pipeline.py --animate
    python master_pipeline.py --report
    python master_pipeline.py --all
"""

import argparse
from throwin_analysis import scoring, animation, reporting, pipeline

def run_analysis():
    print("🔍 Running throw-in scoring pipeline...")
    pipeline.run_full_analysis()

def run_animations():
    print("🎞️ Generating animations...")
    animation.generate_all()

def run_reporting():
    print("📝 Generating summaries and reports...")
    reporting.create_all_summaries()

def main():
    parser = argparse.ArgumentParser(description="Throw-In Analysis CLI")
    parser.add_argument('--analyze', action='store_true', help='Run analysis and scoring')
    parser.add_argument('--animate', action='store_true', help='Generate animations')
    parser.add_argument('--report', action='store_true', help='Generate text summaries')
    parser.add_argument('--all', action='store_true', help='Run full pipeline (all steps)')

    args = parser.parse_args()

    if args.all:
        run_analysis()
        run_animations()
        run_reporting()
    else:
        if args.analyze:
            run_analysis()
        if args.animate:
            run_animations()
        if args.report:
            run_reporting()

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()

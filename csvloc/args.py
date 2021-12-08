from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import List


def parse_args(args: List[str]) -> Namespace:
    parser = ArgumentParser(
        description="Merge multiple localizable CSV files into a single CSV file.",
    )
    parser.add_argument(
        "files", nargs="+", type=Path, metavar="FILE", help="a path to a CSV file"
    )
    return parser.parse_args(args)

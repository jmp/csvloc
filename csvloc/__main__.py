from sys import argv, stdout

from .args import parse_args
from .reader import read_csv
from .writer import write_csv


def main() -> None:
    args = parse_args(argv[1:])
    values = {}
    for in_file in args.files:
        with in_file.open() as f:
            read_csv(f, values)
    write_csv(stdout, values)


if __name__ == "__main__":
    main()

# csvloc

[![build](https://github.com/jmp/csvloc/actions/workflows/build.yml/badge.svg)](https://github.com/jmp/csvloc/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/jmp/csvloc/branch/master/graph/badge.svg?token=MEIHEJBWN9)](https://codecov.io/gh/jmp/csvloc)

Merge localizable strings/translations spread across several
CSV files into a single CSV file, for use with tools like
[strgen][strgen]

## Installation

    poetry install

## Usage

Imagine you have two CSV files for English and Finnish,
containing string identifiers and the corresponding translations:

1. `en-US.csv`:
   ```
   id,en-US
   someId,Some translation
   anotherId,Another translation
   ```
2. `fi-FI.csv`:
   ```
   id,fi-FI
   someId,Joku käännös
   anotherId,Toinen käännös
   ```

Running `csvloc en-US.csv fi-FI.csv` will produce a single
CSV file with all the translations merged:

    id,en-US,fi-FI
    someId,Some translation,Joku käännös
    anotherId,Another translation,Toinen käännös

[strgen]: https://github.com/daisuke-t-jp/strgen

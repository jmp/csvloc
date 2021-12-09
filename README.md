# csvloc

[![build](https://github.com/jmp/csvloc/actions/workflows/build.yml/badge.svg)](https://github.com/jmp/csvloc/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/jmp/csvloc/branch/master/graph/badge.svg?token=MEIHEJBWN9)](https://codecov.io/gh/jmp/csvloc)

Merge localizable strings/translations spread across several
CSV files into a single CSV file.

It can be used in combination with tools like [strgen][strgen] to
share translations between Android and iOS mobile apps. The CSV files
containing the translations can be kept in their own files and
managed with a system like [Weblate][weblate]. Once translated,
the files can be merged with `csvloc` and then ran through `strgen`
to create native translations for Android and iOS.

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
[weblate]: https://weblate.org/
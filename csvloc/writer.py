from csv import DictWriter
from typing import Collection, TextIO

from .types import TranslationDict


def write_csv(f: TextIO, values: TranslationDict) -> None:
    field_names = _find_field_names(values)
    writer = DictWriter(f, field_names)
    writer.writeheader()
    writer.writerows({"id": key, **value} for key, value in values.items())


def _find_field_names(values: TranslationDict) -> Collection[str]:
    field_names = {"id": ""}
    for value in values.values():
        field_names.update(value)
    return field_names.keys()

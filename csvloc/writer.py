from csv import DictWriter
from typing import Collection, TextIO

from .types import TranslationDict


def write_csv(f: TextIO, values: TranslationDict) -> None:
    field_names = _find_field_names(values)
    writer = DictWriter(f, field_names)
    writer.writeheader()
    for translation_id, values in values.items():
        writer.writerow({"id": translation_id, **values})


def _find_field_names(values: TranslationDict) -> Collection[str]:
    field_names = {"id": None}
    for value in values.values():
        for field_name in value.keys():
            field_names[field_name] = None
    return field_names.keys()

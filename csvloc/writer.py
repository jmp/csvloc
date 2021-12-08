from csv import DictWriter
from typing import Dict, List, TextIO

from .types import TranslationDict


def write_csv(f: TextIO, values: TranslationDict) -> None:
    field_names = _find_field_names(values)
    writer = DictWriter(f, field_names)
    writer.writeheader()
    for translation_id, values in values.items():
        writer.writerow({"id": translation_id, **values})


def _find_field_names(values: Dict[str, Dict[str, str]]) -> List[str]:
    field_names = ["id"]
    for value in values.values():
        for field_name in value.keys():
            if field_name in field_names:
                continue
            field_names.append(field_name)
    return field_names

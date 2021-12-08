from csv import DictReader
from typing import TextIO

from .types import TranslationDict


def read_csv(f: TextIO, values: TranslationDict) -> None:
    reader = DictReader(f)
    language_code = reader.fieldnames[1]
    for row in reader:
        translation_id = row["id"]
        translation = row[language_code]
        translations = values.get(translation_id, {})
        translations[language_code] = translation
        values[translation_id] = translations

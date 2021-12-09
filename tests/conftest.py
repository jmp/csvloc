from pathlib import Path

from pytest import fixture


@fixture
def fixtures_path() -> Path:
    return Path(__file__).parent / "fixtures"

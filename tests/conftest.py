from pathlib import Path

from pytest import fixture


@fixture
def fixtures_path() -> Path:
    return Path(__file__).parent / "fixtures"


@fixture
def tmp_file(tmp_path: Path) -> Path:
    return tmp_path / "tmp"

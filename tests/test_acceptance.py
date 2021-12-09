from pathlib import Path
from subprocess import DEVNULL, run

from pytest import CaptureFixture


def test_runs_successfully_when_invoked_via_module() -> None:
    result = run(["python", "-m", "csvloc", "-h"], stdout=DEVNULL, stderr=DEVNULL)
    assert result.returncode == 0


def test_usage_is_printed_to_stderr_when_no_arguments_are_given(
    capfd: CaptureFixture,
) -> None:
    result = run("csvloc")
    stderr = capfd.readouterr().err
    assert result.returncode != 0
    assert stderr.startswith("usage:")


def test_usage_is_printed_to_stdout_when_help_argument_is_given(
    capfd: CaptureFixture,
) -> None:
    result = run(["csvloc", "-h"])
    stdout = capfd.readouterr().out
    assert result.returncode == 0
    assert stdout.startswith("usage:")


def test_single_csv_file_is_copied_to_new_csv(
    fixtures_path: Path,
    capfd: CaptureFixture,
) -> None:
    expected_path = fixtures_path / "single.csv"
    result = run(["csvloc", fixtures_path / "en-US.csv"])
    stdout = capfd.readouterr().out.replace("\r\n", "\n")
    assert result.returncode == 0
    assert stdout == expected_path.read_text()


def test_multiple_csv_files_are_merged_into_single_csv(
    fixtures_path: Path,
    capfd: CaptureFixture,
) -> None:
    expected_path = fixtures_path / "multiple.csv"
    result = run(["csvloc", fixtures_path / "en-US.csv", fixtures_path / "fi-FI.csv"])
    stdout = capfd.readouterr().out.replace("\r\n", "\n")
    assert result.returncode == 0
    assert stdout == expected_path.read_text()

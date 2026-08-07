
import json
from datetime import datetime
from pathlib import Path

from src.formatter import format_system_info


BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def _generate_filename(extension: str) -> Path:
    """
    Generate a timestamped report filename.
    """

    if extension not in {"txt", "json"}:
        raise ValueError(
            f"Unsupported report format: {extension}"
        )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    return (
        REPORTS_DIR
        / f"system_report_{timestamp}.{extension}"
    )


def save_txt(data: dict) -> Path:
    """
    Save system information as a TXT report.
    """

    if not isinstance(data, dict):
        raise ValueError(
            "System information must be a dictionary."
        )

    REPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_path = _generate_filename("txt")

    try:
        report_path.write_text(
            format_system_info(data),
            encoding="utf-8",
        )

    except PermissionError as error:
        raise PermissionError(
            f"Permission denied while saving: {report_path}"
        ) from error

    except OSError as error:
        raise OSError(
            f"Unable to save TXT report: {error}"
        ) from error

    return report_path


def save_json(data: dict) -> Path:
    """
    Save system information as a JSON report.
    """

    if not isinstance(data, dict):
        raise ValueError(
            "System information must be a dictionary."
        )

    REPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_path = _generate_filename("json")

    try:
        report_path.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    except PermissionError as error:
        raise PermissionError(
            f"Permission denied while saving: {report_path}"
        ) from error

    except OSError as error:
        raise OSError(
            f"Unable to save JSON report: {error}"
        ) from error

    return report_path

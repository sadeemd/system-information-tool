import json
from datetime import datetime
from pathlib import Path

from src.formatter import format_system_info

# Reports directory
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def _generate_filename(extension: str) -> Path:
    """
    Generate a timestamped report filename.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return REPORTS_DIR / f"system_report_{timestamp}.{extension}"


def save_txt(data: dict) -> Path:
    """
    Save system information as a TXT report.
    """
    report_path = _generate_filename("txt")

    report_path.write_text(
        format_system_info(data),
        encoding="utf-8",
    )

    return report_path


def save_json(data: dict) -> Path:
    """
    Save system information as a JSON report.
    """
    report_path = _generate_filename("json")

    report_path.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8",
    )

    return report_path
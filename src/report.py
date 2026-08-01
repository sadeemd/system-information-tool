import json
from datetime import datetime
from pathlib import Path


def save_txt(data: dict) -> Path:
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = datetime.now().strftime("Report_%Y-%m-%d_%H-%M.txt")
    report_path = reports_dir / filename

    text = "\n".join(
        f"{key:18}: {value}"
        for key, value in data.items()
    )

    report_path.write_text(text, encoding="utf-8")

    return report_path


def save_json(data: dict) -> Path:
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = datetime.now().strftime("Report_%Y-%m-%d_%H-%M.json")
    report_path = reports_dir / filename

    report_path.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8",
    )

    return report_path
import argparse

from src.logger import setup_logger
from src.report import save_json, save_txt
from src.system_info import get_system_info

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="System Information Tool"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Save report as JSON",
    )

    args = parser.parse_args()

    logger.info("Application started")

    info = get_system_info()

    print("=" * 55)
    print("SYSTEM INFORMATION TOOL")
    print("=" * 55)

    for key, value in info.items():
        print(f"{key:18}: {value}")

    txt_report = save_txt(info)

    logger.info("TXT report saved: %s", txt_report)

    print(f"\nTXT Report: {txt_report}")

    if args.json:
        json_report = save_json(info)
        logger.info("JSON report saved: %s", json_report)
        print(f"JSON Report: {json_report}")

    logger.info("Application finished")


if __name__ == "__main__":
    main()
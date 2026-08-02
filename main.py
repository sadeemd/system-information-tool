
from src.formatter import format_system_info
from src.logger import setup_logger
from src.report import save_json, save_txt
from src.system_info import get_system_info

# Configure logger
logger = setup_logger()


def main():
    logger.info("Application Started")

    # Get system information
    info = get_system_info()

    print("=" * 60)
    print("SYSTEM INFORMATION TOOL".center(60))
    print("=" * 60)

    print(format_system_info(info))

    # Save TXT report
    txt_report = save_txt(info)
    logger.info("TXT report saved: %s", txt_report)

    # Save JSON report
    json_report = save_json(info)
    logger.info("JSON report saved: %s", json_report)

    print("\nReports Generated Successfully")
    print(f"TXT  : {txt_report}")
    print(f"JSON : {json_report}")

    logger.info("Application Closed")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Unexpected error occurred.")
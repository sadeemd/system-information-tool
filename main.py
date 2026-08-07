
from src.formatter import format_system_info
from src.logger import setup_logger
from src.report import save_json, save_txt
from src.system_info import get_system_info


logger = setup_logger()


def main():
    logger.info("Application started")

    try:
        info = get_system_info()
        logger.info("System information collected successfully")

        print("=" * 60)
        print("SYSTEM INFORMATION TOOL".center(60))
        print("=" * 60)

        print(format_system_info(info))

        txt_report = save_txt(info)
        logger.info("TXT report saved: %s", txt_report)

        json_report = save_json(info)
        logger.info("JSON report saved: %s", json_report)

        print("\nReports Generated Successfully")
        print(f"TXT  : {txt_report}")
        print(f"JSON : {json_report}")

        logger.info("Application completed successfully")

    except PermissionError as error:
        logger.error("Permission error: %s", error)
        print(f"Error: Permission denied - {error}")

    except OSError as error:
        logger.error("File system error: %s", error)
        print(f"Error: File system operation failed - {error}")

    except RuntimeError as error:
        logger.error("System information error: %s", error)
        print(f"Error: Unable to collect system information - {error}")

    except Exception:
        logger.exception("Unexpected error occurred")
        print("Error: An unexpected error occurred.")

    finally:
        logger.info("Application finished")


if __name__ == "__main__":
    main()

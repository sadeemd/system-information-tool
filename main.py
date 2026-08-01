import getpass
import logging
import platform
import socket
import uuid
from datetime import datetime
from pathlib import Path

import psutil

# Create logs directory
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=logs_dir / "system_information.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def get_computer_name() -> str:
    """Return the computer name."""
    return platform.node()


def get_username() -> str:
    """Return the current username."""
    return getpass.getuser()


def get_operating_system() -> str:
    """Return the operating system."""
    return platform.system()


def get_os_version() -> str:
    """Return the operating system version."""
    return platform.version()


def get_processor() -> str:
    """Return processor information."""
    return platform.processor()


def get_cpu_usage() -> float:
    """Return current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def get_ram_usage() -> str:
    """Return RAM usage information."""
    memory = psutil.virtual_memory()
    total = memory.total / (1024 ** 3)
    used = memory.used / (1024 ** 3)
    return f"{used:.2f} GB / {total:.2f} GB ({memory.percent}%)"


def get_disk_usage() -> str:
    """Return disk usage information."""
    disk = psutil.disk_usage("/")
    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    return f"{used:.2f} GB / {total:.2f} GB ({disk.percent}%)"


def get_ip_address() -> str:
    """Return local IP address."""
    return socket.gethostbyname(socket.gethostname())


def get_mac_address() -> str:
    """Return MAC address."""
    mac = uuid.getnode()
    return ":".join(f"{(mac >> ele) & 0xff:02X}" for ele in range(40, -1, -8))


def get_python_version() -> str:
    """Return installed Python version."""
    return platform.python_version()


def get_boot_time() -> str:
    """Return system boot time."""
    boot = datetime.fromtimestamp(psutil.boot_time())
    return boot.strftime("%Y-%m-%d %H:%M:%S")


def save_report(report: str) -> None:
    """Save report inside reports folder."""

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = datetime.now().strftime("Report_%Y-%m-%d_%H-%M.txt")
    report_path = reports_dir / filename

    report_path.write_text(report, encoding="utf-8")

    logging.info("Report saved: %s", report_path)

    print(f"\nReport saved successfully:")
    print(report_path)


def main() -> None:
    logging.info("Application started")

    report = f"""
==================================================
            SYSTEM INFORMATION TOOL
==================================================

Computer Name : {get_computer_name()}
Username      : {get_username()}
Operating Sys : {get_operating_system()}
OS Version    : {get_os_version()}
Processor     : {get_processor()}
CPU Usage     : {get_cpu_usage()}%
RAM           : {get_ram_usage()}
Disk Usage    : {get_disk_usage()}
IP Address    : {get_ip_address()}
MAC Address   : {get_mac_address()}
Python Version: {get_python_version()}
Boot Time     : {get_boot_time()}

Generated At  : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

    print(report)

    save_report(report)

    logging.info("Application finished")


if __name__ == "__main__":
    main()
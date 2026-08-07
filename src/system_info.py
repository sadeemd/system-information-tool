
import getpass
import platform
import socket
import uuid
from datetime import datetime

import psutil


def get_system_info() -> dict:
    """
    Collect system information.

    Raises:
        RuntimeError: If a critical system information operation fails.
    """

    try:
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        mac = uuid.getnode()

        mac_address = ":".join(
            f"{(mac >> ele) & 0xff:02X}"
            for ele in range(40, -1, -8)
        )

        boot = datetime.fromtimestamp(
            psutil.boot_time()
        )

    except (OSError, ValueError) as error:
        raise RuntimeError(
            f"Unable to collect system resources: {error}"
        ) from error

    # Battery Information
    try:
        battery = psutil.sensors_battery()

        if battery:
            battery_percent = f"{battery.percent}%"

            battery_status = (
                "Charging"
                if battery.power_plugged
                else "Not Charging"
            )

            if battery.secsleft in (
                psutil.POWER_TIME_UNLIMITED,
                psutil.POWER_TIME_UNKNOWN,
            ):
                battery_time = "Unknown"

            else:
                hours = battery.secsleft // 3600
                minutes = (
                    battery.secsleft % 3600
                ) // 60

                battery_time = (
                    f"{hours}h {minutes}m"
                )

        else:
            battery_percent = "Not Available"
            battery_status = "Not Available"
            battery_time = "Not Available"

    except Exception:
        battery_percent = "Not Available"
        battery_status = "Not Available"
        battery_time = "Not Available"

    # Network Information
    try:
        ip_address = socket.gethostbyname(
            socket.gethostname()
        )
    except socket.gaierror:
        ip_address = "Not Available"

    try:
        processor = platform.processor()
    except Exception:
        processor = "Not Available"

    try:
        username = getpass.getuser()
    except Exception:
        username = "Not Available"

    return {
        "General": {
            "Computer Name": platform.node(),
            "Username": username,
            "Generated At": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        },

        "Operating System": {
            "Operating System": platform.system(),
            "OS Version": platform.version(),
            "Boot Time": boot.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        },

        "Hardware": {
            "Processor": processor,
            "CPU Usage": (
                f"{psutil.cpu_percent(interval=1)}%"
            ),
            "RAM": (
                f"{memory.used / (1024**3):.2f} GB / "
                f"{memory.total / (1024**3):.2f} GB "
                f"({memory.percent}%)"
            ),
            "Disk Usage": (
                f"{disk.used / (1024**3):.2f} GB / "
                f"{disk.total / (1024**3):.2f} GB "
                f"({disk.percent}%)"
            ),
        },

        "Network": {
            "IP Address": ip_address,
            "MAC Address": mac_address,
        },

        "Battery": {
            "Battery Level": battery_percent,
            "Battery Status": battery_status,
            "Battery Time Left": battery_time,
        },

        "Software": {
            "Python Version": platform.python_version(),
        },
    }

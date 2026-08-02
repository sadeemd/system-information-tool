import getpass
import platform
import socket
import uuid
from datetime import datetime

import psutil


def get_system_info() -> dict:
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    mac = uuid.getnode()
    mac_address = ":".join(
        f"{(mac >> ele) & 0xff:02X}" for ele in range(40, -1, -8)
    )

    boot = datetime.fromtimestamp(psutil.boot_time())

    # Battery Information
    battery = psutil.sensors_battery()

    if battery:
        battery_percent = f"{battery.percent}%"
        battery_status = "Charging" if battery.power_plugged else "Not Charging"

        if battery.secsleft in (
            psutil.POWER_TIME_UNLIMITED,
            psutil.POWER_TIME_UNKNOWN,
        ):
            battery_time = "Unknown"
        else:
            hours = battery.secsleft // 3600
            minutes = (battery.secsleft % 3600) // 60
            battery_time = f"{hours}h {minutes}m"
    else:
        battery_percent = "Not Available"
        battery_status = "Not Available"
        battery_time = "Not Available"

    return {
        "General": {
            "Computer Name": platform.node(),
            "Username": getpass.getuser(),
            "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },

        "Operating System": {
            "Operating System": platform.system(),
            "OS Version": platform.version(),
            "Boot Time": boot.strftime("%Y-%m-%d %H:%M:%S"),
        },

        "Hardware": {
            "Processor": platform.processor(),
            "CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
            "RAM": f"{memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB ({memory.percent}%)",
            "Disk Usage": f"{disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB ({disk.percent}%)",
        },

        "Network": {
            "IP Address": socket.gethostbyname(socket.gethostname()),
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
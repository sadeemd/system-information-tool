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

    return {
        "Computer Name": platform.node(),
        "Username": getpass.getuser(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
        "RAM": f"{memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB ({memory.percent}%)",
        "Disk Usage": f"{disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB ({disk.percent}%)",
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "MAC Address": mac_address,
        "Python Version": platform.python_version(),
        "Boot Time": boot.strftime("%Y-%m-%d %H:%M:%S"),
        "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
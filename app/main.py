import requests as req
from secrets import token_urlsafe
import platform
import psutil

user_key = token_urlsafe(64)

system_info = platform.uname()

user_data = {
    "UserKey": user_key,
    "System": system_info.system,
    "NodeName": system_info.node,
    "Release": system_info.release,
    "Version": system_info.machine,
    "Processor": system_info.processor,
    "Physical Cores": psutil.cpu_count(False),
    "Logical Cores": psutil.cpu_count(),
    "Physical Memory Available": psutil.virtual_memory().total,
    "Total Disk Space": psutil.disk_usage('/').total,
}

#rint(user_data)
import requests as req
from secrets import token_hex
import platform
import psutil
import subprocess

# USER_KEY = token_hex(32)

# def gpu_info(info:str):
#     powershell_command = (
#     "Get-WmiObject Win32_VideoController | "
#     "Where-Object { $_.Name -notmatch 'Parsec' } | "
#     "Format-Table "
#     )

#     gpu = subprocess.run(["powershell", "-Command", powershell_command, info, "-HideTableHeaders"],capture_output=True,text=True)
#     return gpu.stdout.strip()

# system_info = platform.uname()

# user_data = {
#     "UserKey": USER_KEY,
#     "System": system_info.system,
#     "Node Name": system_info.node,
#     "Release": system_info.release,
#     "Version": system_info.machine,
#     "Processor": system_info.processor,
#     "Physical Cores": psutil.cpu_count(False),
#     "Logical Cores": psutil.cpu_count(),
#     "Physical Memory Available": psutil.virtual_memory().total,
#     "Total Disk Space": psutil.disk_usage('/').total,
#     "Gpu": gpu_info("Name"),
#     "Gpu Adapter Ram": gpu_info("AdapterRAM"),
#     "Gpu Driver Version": gpu_info("DriverVersion")
# }

# r = req.get("http://127.0.0.1:5000", headers={"Accept-Encoding": "gzip"})
# print(r)
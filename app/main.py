import requests as req
from secrets import token_urlsafe, SystemRandom
import platform
import GPUtil
import psutil

user_key = token_urlsafe(SystemRandom().getrandbits(7))

system_info = platform.uname()
print(system_info.processor)

user_data = {
    
}
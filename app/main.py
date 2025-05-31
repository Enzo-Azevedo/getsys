import requests as req
from secrets import token_urlsafe, SystemRandom

user_key = token_urlsafe(SystemRandom().getrandbits(9))
print(user_key)


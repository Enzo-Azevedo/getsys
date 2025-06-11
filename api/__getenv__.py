from dotenv import load_dotenv
from os import getenv

def return_env(enviroment_string:str):
    return getenv(enviroment_string)
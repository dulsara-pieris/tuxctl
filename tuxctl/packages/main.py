import requests
from utils.colours import *

base_url = "https://raw.githubusercontent.com/dulsara-pieris/tuxctl/Master/package_scripts/"

def find_package_file(target):
    
    package_url = f"{base_url}{target}.sh"
    
    try:
        response = requests.get(package_url, timeout=20)
        return response
    except requests.exceptions.Timeout:
        print(f"{RED}✗ Download timeout{RESET}")
        exit()


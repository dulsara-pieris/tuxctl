import requests
import os
import subprocess
from utils.colours import *

base_url = "https://raw.githubusercontent.com/dulsara-pieris/tuxctl/Master/package_scripts/"
tmp_package_dir = "/tmp/tuxctl/"

def find_package_file(target):
    
    package_url = f"{base_url}{target}.sh"
    
    try:
        response = requests.get(package_url, timeout=20)
        return response
    except requests.exceptions.Timeout:
        print(f"{RED}✗ Download timeout{RESET}")
        exit()

def install_package(target):
    os.makedirs(tmp_package_dir, exist_ok=True)
    package_file_path = f"{tmp_package_dir}{target}.sh"

    os.chmod(package_file_path, 0o755)
    subprocess.run([package_file_path])

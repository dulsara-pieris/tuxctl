import requests
import os
import subprocess
import shutil

from tuxctl.utils.colours import *

base_url = "https://raw.githubusercontent.com/dulsara-pieris/tuxctl/Master/package_scripts/"
tmp_package_dir = "/tmp/tuxctl/"

def find_package_file(target):
    package_url = f"{base_url}{target}.sh"

    try:
        response = requests.get(package_url, timeout=20)
        return response
    
    #So don't get hours trying to recive package
    except requests.exceptions.Timeout:
        print(f"{RED}✗ Download timeout{RESET}")
        exit()

def install_package(target, response):
    os.makedirs(tmp_package_dir, exist_ok=True)
    package_file_path = f"{tmp_package_dir}{target}.sh"

    #Check bash is there to run shell file
    if shutil.which("bash") is None:
        print(f"{RED}✗ Bash is a required package{RESET}")
        exit(1)
    
    #Writing to package shell file in tmp folder
    with open(package_file_path, "w") as file:
        file.write(response.text)

    print(f"{GREEN}✓{RESET} Download sucessfull")
    
    os.chmod(package_file_path, 0o755)
    
    process = subprocess.Popen(
        ["bash", package_file_path],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True
    )

    for line in process.stdout:
        print(line.strip())

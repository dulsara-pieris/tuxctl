import requests

base_url = "https://raw.githubusercontent.com/dulsara-pieris/tuxctl/Master/package_scripts/"

def find_package_file(target):
    
    package_url = f"{base_url}{target}.sh"
    response = requests.get(package_url)
    print(package_url)
    print(response.status_code)

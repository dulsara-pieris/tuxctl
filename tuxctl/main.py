#from checks.network import check_network_route
#from diagnose.network import diagnose_network

#network = check_network_route()
#network_problems = diagnose_network(network)

from packages.main import find_package_file
from packages.main import install_package

import sys
from utils.colours import *

if len(sys.argv) < 2:
    print("You might need help")
    print("""
    tuxctl - trouble shooting assistant
    Usage:
        tuxctl <command> <target>
          """)
    exit()

action = sys.argv[1]

if action in ["install", "remove"]:
    if len(sys.argv) < 3:
        print(f"{YELLOW}✗ Please Provide a package name{RESET}")
        exit()
    else:
        target = sys.argv[2]
        if action == "install":
            find_package_file(target)
            response = find_package_file(target)

            if response.status_code == 200:
                print(f"{GREEN}✓{RESET} Downloaded {target} Package")
                install_package(target)
            elif response.status_code == 404:
                print(f"{RED}✗ Package {target} not found{RESET}")
            else:
                print(f"{RED}✗ Server returned {response.status_code}{RESET}")

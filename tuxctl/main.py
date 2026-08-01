#from checks.network import check_network_route
#from diagnose.network import diagnose_network

#network = check_network_route()
#network_problems = diagnose_network(network)

from packages.main import find_package_file

import sys


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
        print("Please Provide a package name")
        exit()
    else:
        target = sys.argv[2]
        if action == "install":
            find_package_file(target)

from checks.network import check_network_route
from diagnose.network import diagnose_network

network = check_network_route()
network_problems = diagnose_network(network)
print(network_problems)

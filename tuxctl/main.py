from checks.network import check_network_route
from diagnose.network import diagnose_network

network = check_network_route()
problems = diagnose_network(network)

print(network)
print(problems)

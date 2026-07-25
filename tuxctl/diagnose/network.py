def diagnose_network(network):
    network_problems = []

    if not network:
        network_problems.append("Network info missing")
        return network_problems
    if not network.get("interface"):
        network_problems.append("no active interface")
    
    return network_problems


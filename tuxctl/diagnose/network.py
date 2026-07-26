def diagnose_network(network):
    network_problems = []

    if not network:
        network_problems.append("Network info missing")
        return network_problems

    if network.get("ping"):
        print("[OK] ping test passed")
        
        if network.get("dns"):
            print("[OK] No problems with diagnose connection")
    else:
        pass
    return network_problems

#    if not network.get("interface"):
#        network_problems.append("no active interface")
    


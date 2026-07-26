import subprocess
interfaces = []
network = {}

def check_ping():
    ping = subprocess.run(
        ["ping", "-c", "1" ,"1.1.1.1"],
        capture_output = True,
        text = True
    )

    return ping.returncode == 0

def check_dns():
    dns = subprocess.run(
        ["ping", "-c", "1", "google.com"],
        capture_output = True,
        text = True
    )
    
    return dns.returncode == 0


def check_network_interface():
    network_interfaces = subprocess.run(
        ["ip", "link"],
        capture_output = True,
        text = True
    )
    for line in network_interfaces.stdout.splitlines():
        if line and line[0].isdigit():
            #sorting the text out from ip link
            parts = line.split(":", 2)
        
            interface_name = parts[1].strip()

            print(interfaces)
            
            #sorting interface type
            if interface_name.startswith("wl"):
                internet_type = "WIFI"
            elif interface_name.startswith("en"):
                internet_type = "Ethernet"
            else:
                internet_type = "other"
           
            #Interface status
            interface_info = parts[2].strip()

            if "state UP" in interface_info:
                interface_status = "UP"
            else:
                interface_status = "DOWN" 
            
            interfaces.append({
                "name: ": interface_name,
                "type: ": internet_type,
                "status: ": interface_status 
            })
            
            return interfaces

def check_network_route():
    route = subprocess.run(
        ["ip", "route", "get", "1.1.1.1"],
        capture_output = True,
        text = True
    )

    ip_route_parts = route.stdout.split()

    if "via" not in ip_route_parts:
        network["gateway"] = None
        network["interface"] = None
        network["ip"] = None

    else:
        gateway = ip_route_parts[ip_route_parts.index("via") + 1]
        interface = ip_route_parts[ip_route_parts.index("dev") + 1]
        ip = ip_route_parts[ip_route_parts.index("src") + 1]

        network["gateway"] = gateway
        network["interface"] = interface
        network["ip"] = ip

    return network

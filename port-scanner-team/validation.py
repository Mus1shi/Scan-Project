import ipaddress
import re

def validate_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        print(f"That IP address is invalid: {ip_address}")

def validate_port_range(port_range):
    # Single port case validation
    if port_range.isdigit():
        port = int(port_range)
        if port <= 1 or port >= 65535:
            return True, (port, port)
        else:
            return False, f"{port_range} is out of range (1-65535)"

    # Port range case validation
    match = re.match(r'^(\d+)-(\d+)$', port_range)
    if match:
        start, end = int(match.group(1)), int(match.group(2))
        if 1 <= start <= end <= 65535:
            return True, (start, end)
        else:
            return False, f"Invalid port range: {port_range}"
    else:
        return False, f"Invalid port range format: {port_range} . Please use this format (port1-port2) ie: (3-554)"


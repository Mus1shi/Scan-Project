import ipaddress
import re
import validators
import socket
from urllib.parse import urlparse

def validate_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        print(f"That IP address is invalid: {ip_address}")
        return False

def validate_port_range(port_range):
    # Single port case validation
    if port_range.isdigit():
        port = int(port_range)
        if 1 <= port <= 65535:
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

def validate_url(url):
<<<<<<< HEAD
    if url.startswith(('http://', 'https://')):
        if validators.url(url):
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname
        else:
            print(f"Invalid URL format: {url}")
            return False, None
    else:
        # If not a full URL, treat as hostname and add http:// for validation purpose
        test_url = f"http://{url}"
        if validators.url(test_url):
            hostname = url
        else:
            # Try as plain hostname anyway
            hostname = url

    if hostname:
        try:
            ip_address = socket.gethostbyname(hostname)
            if validate_ip_address(ip_address):
                print(f"Successfully resolved {hostname} to {ip_address}")
                return True, ip_address
            else:
                return False, None
        except socket.gaierror:
            print(f"Couldn't resolve hostname: {hostname}")
            return False, None
        except Exception as e:
            print(f"Error resolving hostname: {e}")
            return False, None
    else:
        print(f"Couldn't extract hostname from: {url}")
        return False, None


=======
    # Ajouter https:// si absent
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    if validators.url(url):
        try:
            # Extraire le hostname (sans protocole ni chemin)
            hostname = url.split("//")[-1].split("/")[0]
            ip_address = socket.gethostbyname(hostname)
            validate_ip_address(ip_address)
            return True, ip_address
        except socket.gaierror:
            print(f"URL does not have a valid IP address: {url}")
            return False
    else:
        print(f"URL has a problem: {url}")
        return False
>>>>>>> dd494ac (🔧 Replaced log system with logging module + improved validation)

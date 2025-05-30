import socket
import logging
import validation

# Configuration du logger
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='[%(asctime)s] IP: %(ip)s, Port: %(port)s, Status: %(status)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("scanner")

def log_result(ip, port, status, verbose=False):
    message = f"Scan result"
    extra = {'ip': ip, 'port': port, 'status': status}
    logger.info(message, extra=extra)
    if verbose:
        print(f"[{ip}] Port {port} → {status}")

print(r"""______            _      _____ _                 _
|  _  \          | |    /  ___| |               | |
| | | |_   _  ___| | __ \ `--.| | ___  _   _ ___| |_ ___ _ __
| | | | | | |/ __| |/ /  `--. \ |/ _ \| | | / __| __/ _ \ '__|
| |/ /| |_| | (__|   <  /\__/ / | (_) | |_| \__ \ ||  __/ |
|___/  \__,_|\___|_|\_\ \____/|_|\___/ \__,_|___/\__\___|_|
""")

print("\n****************************************************************")
print("\n* Team Members:                                                 *")
print("\n* - Harold                                                     *")
print("\n* - Tommy                                                      *")
print("\n* - Patrick                                                    *")
print("\n* - Steve                                                      *")
print("\n****************************************************************")

def scan_website(webset):
    try:
        ip_address = socket.gethostbyname(webset)
        validation.validate_ip_address(ip_address)
        print(f"The IP address for {webset} is {ip_address}")
        return ip_address
    except socket.gaierror:
        print("❌ Could not resolve hostname.")
        return None

def find_port(ip_address):
    print(f"Scanning IP: {ip_address}")
    port_input = input("Enter the port you want to scan (ex: 21 or 20-80): ")
    valid, result = validation.validate_port_range(port_input)

    if not valid:
        print(f"❌ {result}")
        return

    start_port, end_port = result

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            status = "open" if result == 0 else "closed"
            log_result(ip_address, port, status, verbose=True)

def main():
    choice = input("Do you have a URL or an IP? ").strip().upper()
    ip = None

    if choice == "URL":
        url = input("Enter the website you want to scan: ").strip()
        valid, ip = validation.validate_url(url)
        if not valid:
            return
    elif choice == "IP":
        ip = input("Enter the IP address to scan: ").strip()
        try:
            validation.validate_ip_address(ip)
        except ValueError as e:
            print(f"❌ Invalid IP: {e}")
            return
    else:
        print("❌ Invalid choice. Please enter 'URL' or 'IP'.")
        return

    if ip:
        find_port(ip)

if __name__ == "__main__":
    main()

import socket  # Import socket module for network operations
import  validation  # Import custom validation module
import sys  # Import system module for system-specific operations

# ASCII art logo for Duck Slouster - This displays a fancy text-based logo
print(r"""______            _      _____ _                 _             
|  _  \          | |    /  ___| |               | |            
| | | |_   _  ___| | __ \ `--.| | ___  _   _ ___| |_ ___ _ __ 
| | | | | | |/ __| |/ /  `--. \ |/ _ \| | | / __| __/ _ \ '__|
| |/ /| |_| | (__|   <  /\__/ / | (_) | |_| \__ \ ||  __/ |   
|___/  \__,_|\___|_|\_\ \____/|_|\___/ \__,_|___/\__\___|_|   """)

# Display team member information in a formatted box
print("\n****************************************************************")
print("\n* Team Members:                                                 *")
print("\n* - Harold                                                     *")
print("\n* - Tommy                                                      *")
print("\n* - Patrick                                                    *")
print("\n* - Steve                                                      *")
print("\n****************************************************************")

 
def scan_website(website):
    """
    This function takes a website URL and converts it to an IP address
    Args:
        website (str): The website URL to scan
    Returns:
        str or None: Returns the IP address if valid, None if invalid
    """
    # Use validation module to check if URL is valid and get its IP address
    is_valid, ip_address = validation.validate_url(website)

    if is_valid:
        print(f"The IP address for {website} is: {ip_address}")
        return ip_address
    else:
        return None
    

def find_port(ip_address):
    """
    This function scans ports on a given IP address
    Args:
        ip_address (str): The IP address to scan
    """
    print(f"the scanning is for the IP {ip_address} ")
    print("enter the port you are looking for")

    try:
        # Get port range from user input
        port = input("enter the port you want to scan: ")
        # Validate the port range using validation module
        is_valid, result = validation.validate_port_range(port)
        start = 0
        end = 0
        if is_valid:
            # Extract start and end ports from validation result
            start, end = result
            print(f"Start port: {start}, End port: {end}")
        else:
            print(f"Error: {result}")
            return
            
        open_ports = [] # List to store ports that are found to be open
        
        # Loop through each port in the specified range
        for port in range(start, end + 1):
            # Create a new socket object for TCP connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Set timeout to 1 second

            # Try to connect to the port
            result = s.connect_ex((ip_address, port))
            if result == 0:  # If connection successful (port is open)
                print("Port {} is open".format(port))
                open_ports.append(port)
                # Log open ports to a file
                with open("open-ports.txt", "w") as log_file:
                    log_file.write(f"Port {port} is open on {ip_address}\n")
            else:  # If connection failed (port is closed)
                print("Port {} is closed".format(port))
            s.close()  # Close the socket connection
            
    # Handle various potential errors
    except KeyboardInterrupt:  # If user interrupts program (Ctrl+C)
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:  # If hostname resolution fails
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:  # If server doesn't respond
        print("\ Server not responding !!!!")
        sys.exit()


def main():
    """
    Main function that controls the program flow:
    1. Asks user if they have URL or IP
    2. Validates input
    3. Initiates port scanning if input is valid
    """
    # Ask user whether they have URL or IP
    url_or_ip = input("Do you have a URL or an IP? ").upper()
    ip = None
    
    if url_or_ip == "URL":
        # If URL provided, get website and convert to IP
        website = input("Enter the website you want to scan: ")
        ip = scan_website(website)
    elif url_or_ip == "IP":
        # If IP provided, validate the IP address
        user_ip = input("Enter the IP you want to scan: ")
        try:
            validation.validate_ip_address(user_ip)
            ip = user_ip
            print(f"✅ Using IP: {ip}")
        except Exception as e:
            print(f"❌ Invalid IP: {e}")
    else:
        print("❌ Please enter either 'URL' or 'IP'")
    
    # Proceed with port scanning only if we have a valid IP
    if ip:
        find_port(ip)
    else:
        print("❌ No valid IP to scan. Exiting...")

# Program entry point - only run main() if this file is run directly
if __name__ == "__main__":
    main()

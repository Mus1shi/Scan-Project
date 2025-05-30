import socket
import  validation
import sys

# ASCII art logo for Duck Slouster
# Art ASCII pour Duck Slouster
print(r"""______            _      _____ _                 _             
|  _  \          | |    /  ___| |               | |            
| | | |_   _  ___| | __ \ `--.| | ___  _   _ ___| |_ ___ _ __ 
| | | | | | |/ __| |/ /  `--. \ |/ _ \| | | / __| __/ _ \ '__|
| |/ /| |_| | (__|   <  /\__/ / | (_) | |_| \__ \ ||  __/ |   
|___/  \__,_|\___|_|\_\ \____/|_|\___/ \__,_|___/\__\___|_|   """)
print("\n****************************************************************")
print("\n* Team Members:                                                 *")
print("\n* - Harold                                                     *")
print("\n* - Tommy                                                      *")
print("\n* - Patrick                                                    *")
print("\n* - Steve                                                      *")
print("\n****************************************************************")

 
def scan_website(website):
    # Function to get IP address from website URL
    # Fonction pour obtenir l'adresse IP à partir de l'URL du site web
    is_valid, ip_address = validation.validate_url(website)

    if is_valid:
        print(f"The IP address for {website} is: {ip_address}")
        return ip_address
    else:
        return None
    

def find_port(ip_address):
    # Function to scan a specific port on the given IP address
    print(f"the scanning is for the IP {ip_address} ")
    print("enter the port you are looking for")

    try:
        port = input("enter the port you want to scan: ")
        is_valid, result = validation.validate_port_range(port)
        start = 0
        end = 0
        if is_valid:
            start, end = result
            print(f"Start port: {start}, End port: {end}")
        else:
            print(f"Error: {result}")
            return
        open_ports = [] #array to put open ports
        for port in range(start, end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((ip_address, port))
            if result == 0:
                print("Port {} is open".format(port))
                open_ports.append(port)
                with open("open-ports.txt", "w") as log_file:
                    log_file.write(f"Port {port} is open on {ip_address}\n")
            else:
                print("Port {} is closed".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()


def main():
    # Main function to handle user input and control program flow
    # Fonction principale pour gérer les entrées utilisateur et contrôler le flux du programme
    url_or_ip = input("Do you have a URL or an IP? ").upper()
    ip = None
    
    if url_or_ip == "URL":
        # Handle URL input and convert to IP
        # Gérer l'entrée URL et la convertir en IP
        website = input("Enter the website you want to scan: ")
        ip = scan_website(website)
    elif url_or_ip == "IP":
        # Handle direct IP input
        # Gérer l'entrée directe de l'IP
        user_ip = input("Enter the IP you want to scan: ")
        try:
            validation.validate_ip_address(user_ip)
            ip = user_ip
            print(f"✅ Using IP: {ip}")
        except Exception as e:
            print(f"❌ Invalid IP: {e}")
    else:
        print("❌ Please enter either 'URL' or 'IP'")
    
    # Only scan ports if we have a valid IP
    # Scanner les ports uniquement si nous avons une IP valide
    if ip:
        find_port(ip)
    else:
        print("❌ No valid IP to scan. Exiting...")

if __name__ == "__main__":
    main()
    
    



    




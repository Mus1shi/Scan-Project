import socket
import  validation
import nmap

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

 
def scan_website(webset):
    # Function to get IP address from website URL
    # Fonction pour obtenir l'adresse IP à partir de l'URL du site web
    try:
        ip_address = socket.gethostbyname(webset)
        validation.validate_ip_address(ip_address)
        print(f"The IP address for {webset} is {ip_address}")
        return ip_address
    except socket.gaierror:
        return "Could not resolve hostname" 
    

def find_port(ip_address):
    # Function to scan a specific port on the given IP address
    # Fonction pour scanner un port spécifique sur l'adresse IP donnée
    print(f"the scanning is for the IP {ip_address} ")
    print("enter the port you are looking for")

    try:
        port = input("enter the port you want to scan")
        validation.validate_port_range(port)
        nm = nmap.PortScanner()
        results = nm.scan(ip_address, str(port))
        if 'tcp' in results['scan'][ip_address]:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except ValueError:
        print("❌ Please enter a valid number for the port!")
    except Exception as e:
        print(f"❌ Error during scan: {e}")


def main():
    # Main function to handle user input and control program flow
    # Fonction principale pour gérer les entrées utilisateur et contrôler le flux du programme
    url_or_ip = input("Do you have a URL or an IP? ").upper()
    ip = None
    
    if url_or_ip == "URL":
        # Handle URL input and convert to IP
        # Gérer l'entrée URL et la convertir en IP
        website = input("Enter the website you want to scan: ")
        validation.validate_url(website)
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
    
    



    




import socket
import nmap
import validation      # Ton fichier Bloc 1
from log_output import log_result  # Ton fichier Bloc 3

# ✅ ASCII Art pour l'en-tête
print(r"""______            _      _____ _                 _             
|  _  \          | |    /  ___| |               | |            
| | | |_   _  ___| | __ \ `--.| | ___  _   _ ___| |_ ___ _ __ 
| | | | | | |/ __| |/ /  `--. \ |/ _ \| | | / __| __/ _ \ '__|
| |/ /| |_| | (__|   <  /\__/ / | (_) | |_| \__ \ ||  __/ |   
|___/  \__,_|\___|_|\_\ \____/|_|\___/ \__,_|___/\__\___|_|   """)
print("\n*************************************************************")
print("* 🔐 Projet Port Scanner — BeCode Cybersecurity 2025         *")
print("* Membres : Tommy, Harold, Patrick, Steve                   *")
print("*************************************************************\n")


# ✅ Fonction : scanner un site web (URL ➝ IP)
def scan_website(website):
    is_valid, ip_address = validation.validate_url(website)
    if is_valid:
        print(f"🌐 Adresse IP de {website} : {ip_address}")
        return ip_address
    else:
        print("❌ URL non valide ou introuvable.")
        return None


# ✅ Fonction : scanner un ou plusieurs ports sur une IP
def find_port(ip_address):
    print(f"\n🔍 Scan en cours pour l'adresse IP : {ip_address}")
    port_input = input("Entrez le port ou la plage de ports à scanner (ex: 22 ou 20-80) : ")

    is_valid, port_data = validation.validate_port_range(port_input)
    if not is_valid:
        print(f"❌ Erreur : {port_data}")  # port_data contient ici le message d’erreur
        return

    start_port, end_port = port_data
    nm = nmap.PortScanner()

    try:
        # ✅ Scan des ports
        port_range_str = f"{start_port}-{end_port}"
        results = nm.scan(ip_address, port_range_str)

        for port in range(start_port, end_port + 1):
            status = results['scan'][ip_address]['tcp'].get(port, {}).get('state', 'closed')
            log_result(ip_address, port, status)  # Appel du logger (Bloc 3)

    except Exception as e:
        print(f"❌ Erreur pendant le scan : {e}")


# ✅ Fonction principale : choix entre IP et URL
def main():
    choix = input("As-tu une URL ou une IP ? (Tape 'URL' ou 'IP') : ").strip().upper()
    ip = None

    if choix == "URL":
        website = input("Entre l'URL du site à scanner : ")
        ip = scan_website(website)

    elif choix == "IP":
        ip_input = input("Entre l'adresse IP à scanner : ").strip()
        if validation.validate_ip_address(ip_input):
            ip = ip_input
        else:
            print("❌ Adresse IP non valide.")

    else:
        print("❌ Merci d’indiquer 'URL' ou 'IP' uniquement.")
        return

    # ✅ Lancer le scan si IP valide
    if ip:
        find_port(ip)
    else:
        print("❌ Aucune adresse IP valide. Fin du programme.")


if __name__ == "__main__":
    main()

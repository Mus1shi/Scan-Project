import ipaddress  # Pour valider les adresses IP
import re         # Pour les expressions régulières (port ranges)
import validators # Pour vérifier la validité d'une URL
import socket     # Pour convertir une URL en IP

# ✅ Fonction pour valider une adresse IP (v4 ou v6)
def validate_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)  # Essaie de convertir l'entrée en IP
        return True
    except ValueError:
        print(f"❌ Adresse IP invalide : {ip_address}")
        return False

# ✅ Fonction pour valider un port ou une plage de ports
def validate_port_range(port_range):
    # ➤ Cas où l'utilisateur entre UN seul port (ex: "80")
    if port_range.isdigit():
        port = int(port_range)
        if 1 <= port <= 65535:
            return True, (port, port)
        else:
            return False, f"❌ Port hors limites (1–65535) : {port_range}"

    # ➤ Cas où l'utilisateur entre une PLAGE (ex: "20-80")
    match = re.match(r'^(\d+)-(\d+)$', port_range)
    if match:
        start, end = int(match.group(1)), int(match.group(2))
        if 1 <= start <= end <= 65535:
            return True, (start, end)
        else:
            return False, f"❌ Plage invalide : {port_range}"
    else:
        return False, f"❌ Format incorrect. Utilise par exemple : 3-554"

# ✅ Fonction pour valider une URL et la convertir en IP
def validate_url(url):
    if validators.url(url):  # Vérifie la structure de l'URL
        try:
            ip_address = socket.gethostbyname(url)  # Convertit URL ➝ IP
            if validate_ip_address(ip_address):
                return True, ip_address
            else:
                return False, None
        except socket.gaierror:
            print(f"❌ Impossible de résoudre l'URL : {url}")
            return False, None
    else:
        print(f"❌ URL invalide : {url}")
        return False, None

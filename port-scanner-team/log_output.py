import datetime
import os

def log_result(ip, port, status, verbose=False):
    """
    Fonction pour écrire les résultats du scan dans un fichier texte.
    
    Args:
        ip (str): L'adresse IP ciblée.
        port (int): Le port scanné.
        status (str): Le statut du port ("open", "closed", etc.).
        verbose (bool): Si True, affiche les logs dans le terminal en plus du fichier.
    """
    
    # Définir le nom du dossier de logs
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

    # Crée le nom de fichier avec date/heure
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{log_dir}/scan_log_{timestamp}.txt"

    # Préparer le message de log
    log_message = f"[{datetime.datetime.now()}] IP: {ip}, Port: {port}, Status: {status}\n"

    # Écrire dans le fichier
    with open(filename, "a") as file:
        file.write(log_message)

    # Afficher en console si verbose=True
    if verbose:
        print(log_message.strip())

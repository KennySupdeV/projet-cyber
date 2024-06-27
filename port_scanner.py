import socket
import os 
import library

def check_ports(host, start_port, end_port):
    message = ''
    open_ports = []
    closed_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        sock.close()
    return open_ports, closed_ports

# Adresse de l'hôte (localhost pour la machine locale)
host = 'localhost'
start_port = int(input("Entrez un port de départ : "))
end_port = int(input("Entrez un port de fin : "))
message = f"enregistrement depuis {start_port} jusqu à {end_port}"

print(f"Vérification des ports ouverts sur {host} de {start_port} à {end_port}...")

open_ports, closed_ports = check_ports(host, start_port, end_port)

print(f"Ports ouverts : {open_ports}")
print(f"Ports fermés : {closed_ports}")
message += f'\nPorts ouverts : {open_ports}\nPorts fermés : {closed_ports}'
library.create_rapport('port_scanner.txt', message )
library.open_rapport('port_scanner.txt')

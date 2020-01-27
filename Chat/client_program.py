import socket

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 8069

    client_socket.connect((host, port))

    print("Connected to server at " + str(host) + str(port))
    message = raw_input(" >> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print("Received from server: " + str(data))

        message = raw_input(" >> ")
        
    client_socket.close()

if __name__ == '__main__':
    client_program()
     
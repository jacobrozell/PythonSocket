import socket
import sys

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if sys.argv[1] is not None:
        arg1 = sys.argv[1]
        print("ARG1: " + str(arg1))
        host = str(arg1)
        port = 8080
    else:
        host = host.gethostname()
        port = 8080

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
     
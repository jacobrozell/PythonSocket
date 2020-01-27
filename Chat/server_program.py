import socket

def server_program():
    # Get Host Name

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 8069

    server_socket.bind((host, port))

    print(port)
    
    # configure how many client the server can listen
    server_socket.listen(2)

    print("Waiting for connections:  " + str(host) + str(port))

    conn, address = server_socket.accept()
    print("Connection from: ", address)
    while True:
        # receive data stream. It won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        message = raw_input(' >> ')
        conn.send(message.encode()) # send message to client

    conn.close() # close the connection

if __name__ == '__main__':
    server_program()

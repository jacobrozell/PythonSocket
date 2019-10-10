import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

print("Connected successfully!")

bytes_received = s.recv(1024)
message = bytes_received.decode()

print("Message received!\n")

print("Message is:\n\t" + message)

s.close()

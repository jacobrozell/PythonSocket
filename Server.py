import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("Socket binded to %s" % port)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    message = "Thank you for connecting"
    bytess = str.encode(message)
    c.send(bytess)

    c.close()

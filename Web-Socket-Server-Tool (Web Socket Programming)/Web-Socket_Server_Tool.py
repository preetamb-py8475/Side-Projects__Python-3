
import socket


"""
My Python Script : Web-Socket Server
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

s = socket.socket()
print()
print("Socket Successfully Created")

port = 25

s.bind(('', port))
print()
print("Socket bound to %s" % port)

s.listen(5)
print()
print("Socket is Listening")

while True:
    c, addr = s.accept()
    print()
    print('Got connection from', addr)

    print()
    c.send(b'Thank you for connecting')

    c.close()

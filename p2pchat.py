import socket
import os

host = ''
port = 1337

# set up socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((host,port))
listener.listen(1)
print("serving on port", port)
while True:
    x = 1 # eheh ok cool

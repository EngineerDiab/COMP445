import socket
import os

host = ''
port = 1337

# set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
print("serving on port", port)
while True:
    x = 1 # eheh ok cool

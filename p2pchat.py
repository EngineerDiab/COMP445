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
    x = 1


def build_message(user_message, user_name):
    return 'user: ' + user_name + '\nmessage: ' + user_message + '\n\n'


def sender(user_name, ip_address, port):
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    print("serving on port", port)
    while True:
        user_message = input()
        application_message = build_message(user_message, user_name)
        s.sendto(application_message, ip_address, port)


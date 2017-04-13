import socket
import os
import threading

def sender(username, ip, port):
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    print("serving on port", port)
    while True:
        user_message = input()
        application_message = build_message(user_message, username)
        s.sendto(application_message.encode('utf-8'), (ip, port))

def build_message(user_message, user_name):
    return 'user: ' + user_name + '\nmessage: ' + user_message + '\n\n'
        
def receiver(username, ip, socket):
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    print("serving on port", port)
    while True:
        appMsg = s.recv(4096)
        (username, userMsg) = parseMsg(appMsg)
        print(username, userMsg)

def parseMsg(appMsg):
    appMsg = appMsg.split('\n')
    username = appMsg[0]
    userMsg = appMsg[1]
    return (username, userMsg)

p2 = os.fork()
if p2 == 0:
    sender('bobby', 'localhost', 1337)
else:
    receiver('bobby', 'localhost', 1337)

while True:
    pass

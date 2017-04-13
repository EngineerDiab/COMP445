import socket
import os
import threading
from datetime import datetime

def sender(username, ip, port):
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
    print("sending on port", port)
    while True:
        user_message = input()
        application_message = build_message(user_message, username)
        s.sendto(application_message.encode('utf-8'), (ip, port))

def build_message(user_message, user_name):
    return 'user: ' + user_name + '\nmessage: ' + user_message + '\n\n'
        
def receiver(username, ip, port):
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))
    print("receiving on port", port)
    while True:
        appMsg = s.recv(4096)
        (username, userMsg) = parseMsg(appMsg)
        print(datetime.now(),' [', username,']: ', userMsg, sep='')

def parseMsg(appMsg):
    appMsg = appMsg.decode('utf-8')
    appMsg = appMsg.split('\n')
    username = appMsg[0].split(': ')[1]
    userMsg = appMsg[1].split(': ')
    userMsg = ''.join(userMsg[1:])
    return (username, userMsg)

p2 = os.fork()
if p2 == 0:
    receiver('bobby', '255.255.255.255', 1337)
else:
    sender('bobby', '255.255.255.255', 1337)


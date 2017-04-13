import socket
import os
import threading

def receiver(username, ip, port):
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip,port))
    print("serving on port", port)
    while True:
        appMsg = s.recv(1024)
        (username, userMsg) = parseMsg(appMsg)
        print(username, userMsg)

def parseMsg(appMsg):
    appMsg = appMsg.split('\n')
    username = appMsg[0]
    userMsg = appMsg[1]
    return (username, userMsg)

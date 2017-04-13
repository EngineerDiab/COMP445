import socket
import os
import threading
from datetime import datetime


def sender(username, ip, port):
    global userList
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    joinMsg = buildMsg(username, 'join', '')
    userList += [username]
    s.sendto(joinMsg.encode('utf-8'), (ip, port))
    running = True
    while running:
        userMsg = input()
        command = 'talk'
        if userMsg == '/leave':
            command = 'leave'
            running = False
        if userMsg == '/who':
            print('users:', userList)
        else:
            appMsg = buildMsg(username, command, userMsg)
            s.sendto(appMsg.encode('utf-8'), (ip, port))

def buildMsg(username, command, userMsg):
    return username + '\n' + command + '\n' + userMsg
        
def receiver(username, ip, port):
    global userList
    # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
    print("logged on to port", port)
    while True:
        appMsg = s.recv(4096)
        (user, command, userMsg) = parseMsg(appMsg)
        if command == 'talk':
            print(datetime.now(),' [', user,']: ', userMsg, sep='')
        if command == 'join':
            print(datetime.now(), user, 'joined!')
            print('potato')
            userList += [user]
            command == 'potato'
        if command == 'leave':
            print(datetime.now(), user, 'left...')
        if command == 'potato':
            userList += [user]

def parseMsg(appMsg):
    appMsg = appMsg.decode('utf-8')
    appMsg = appMsg.split('\n')
    username = appMsg[0]
    command = appMsg[1]
    userMsg = appMsg[2]
    return (username, command, userMsg)


userList = []
name = input('enter your name: ')
p2 = os.fork()
if p2 == 0:
    receiver(name, '', 1337)
else:
    sender(name, '<broadcast>', 1337)


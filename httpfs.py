import socket
import argparse
import os

host = ''
port = 8888
localPath = os.path.dirname(os.path.realpath(__file__))

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((host, port))
listener.listen(1)
print("serving HTTP on port", port)
while True:
    connection, address = listener.accept()
    request = connection.recv(1024).decode("utf-8")
    request = request.split('\r\n')
    getVsPostLine = request[0].split()
    getVsPost = getVsPostLine[0]
    path = getVsPostLine[1]
    separatorLine = request.index('')
    data = ''
    for line in request[separatorLine+1:]:
        data += line + "\n"
    response = ''

    # differentiate GET and POST
    if getVsPost == 'GET':
        if path == "/":
            fileList = os.listdir(localPath + path)
            for file in fileList:
                response += file + "\n"
        else:
            fileSpecific = open(localPath + path, 'r')
            response = fileSpecific.read()
            fileSpecific.close()
    elif getVsPost == 'POST':
        fileSpecific = open(localPath + path, 'w')
        fileSpecific.write(data)
        fileSpecific.close()
    
    connection.sendall(bytes(response, "utf-8"))
    connection.close()

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

    # differentiate GET and POST
    if getVsPost == 'GET':
        print("this is a GET request!")
        if path == "/":
            fileList = os.listdir(localPath + path)
            for file in fileList:
                print(file)
    elif getVsPost == 'POST':
        print("this is a POST request!")
    

    response = b"""\
            Hello, World!
            """
    connection.sendall(response)
    connection.close()

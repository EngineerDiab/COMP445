import socket
import argparse


host = ''
port = 8888
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
    elif getVsPost == 'POST':
        print("this is a POST request!")
    print("the path is", path)

    response = b"""\
            Hello, World!
            """
    connection.sendall(response)
    connection.close()

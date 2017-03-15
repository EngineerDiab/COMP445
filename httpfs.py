import socket
import argparse
from urllib.parse import urlparse


host = ''
port = 8888
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((host, port))
listener.listen(1)
print("serving HTTP on port ", port)
while True:
    connection, address = listener.accept()
    request = connection.recv(1024)
    print(request)

    response = """\
            HTTP/1.1 200 OK

            Hello, World!
            """
    connection.sendall(response)
    connection.close()

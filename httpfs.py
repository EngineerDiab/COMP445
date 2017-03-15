import socket
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='show verbose ouput',
        action='store_true')
parser.add_argument('-p', '--port', help='Specific port number to run server, default is 8888', type=int)
parser.add_argument('-d', '--directory', help='Specific local directory to read/write files, default is current directory', type=str)
args = parser.parse_args()

host = ''

port = 8888
if args.port is not None:
    port = args.port

localPath = os.path.dirname(os.path.realpath(__file__))
if args.directory is not None:
    localPath = args.directory

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

    if getVsPost == 'GET':
        if path == "/":
            fileList = os.listdir(localPath + path)
            for file in fileList:
                response += file + "\n"
        else:
            if os.path.exists(localPath+path):
                fileSpecific = open(localPath + path, 'r')
                response = fileSpecific.read()
                fileSpecific.close()
            else:
                response = '404'
    elif getVsPost == 'POST':
        fileSpecific = open(localPath + path, 'w')
        fileSpecific.write(data)
        fileSpecific.close()
    
    connection.sendall(bytes(response,"utf-8"))
    connection.close()

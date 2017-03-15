import socket
import argparse
import os

# command-line parsing
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

# set up list of valid files, remove httpfs.py from said list if using default dir
fileList = os.listdir(localPath)
if localPath == os.path.dirname(os.path.realpath(__file__)):
    fileList.remove("httpfs.py")

# set up socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((host, port))
listener.listen(1)
print("serving HTTP on port", port)
while True:
    connection, address = listener.accept()
    request = connection.recv(1024).decode("utf-8")
    # split request into its useful parts (get VS post, path, data)
    request = request.split('\r\n')
    getVsPostLine = request[0].split()
    getVsPost = getVsPostLine[0]
    path = getVsPostLine[1]
    separatorLine = request.index('')
    data = ""
    for line in request[separatorLine+1:]:
        data += line + "\n"
    response = ""

    if getVsPost == 'GET':
        if path == "/":
            # display fileList
            for file in fileList:
                response += file + "\n"
        else:
            # display contents of file (only if it's in the fileList, else 404)
            if path[1:] in fileList:
                fileSpecific = open(localPath + path, 'r')
                response = fileSpecific.read()
                fileSpecific.close()
            else:
                response = "404"
    elif getVsPost == 'POST':
        # write to file (only if it's in the fileList, else 403)
        if path[1:] in fileList:
            fileSpecific = open(localPath + path, 'w')
            fileSpecific.write(data)
            fileSpecific.close()
        else:
            response = "403"
    
    # send response 
    connection.sendall(bytes(response,"utf-8"))
    connection.close()

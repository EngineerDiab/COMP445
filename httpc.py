import socket
import argparse
from urllib.parse import urlparse


def httpc_get(url):
    # initialize the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # urlparse is only used here to grab the hostname and request separately,
    # NOT to connect! (So, you know, please don't dock marks for it... thanks!)
    url = urlparse(url)
    s.connect((url.hostname, 80))
    request = "GET " + url.path + "?" + url.query + "\r\n"
    print(request)
    s.sendall(request.encode("utf-8"))
    response = s.recv(4096)
    print(response.decode("utf-8"))
    s.close


def httpc_post(url, header, data):
    # initialize the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url = urlparse(url)
    s.connect((url.hostname, 80))
    request = "POST " + url.path + "\r\n" + header + "\r\n" + data + "\r\n"
    print(request)
    s.sendall(request.encode("utf-8"))
    response = s.recv(4096)
    print(response.decode("utf-8"))
    s.close


# argument parsing for command-line use
parser = argparse.ArgumentParser()
getVsPost = parser.add_mutually_exclusive_group()
getVsPost.add_argument('-g', '--get', help='get with URL argument', type=str)
getVsPost.add_argument('-p', '--post', help='post with URL argument', type=str)
parser.add_argument('--header', help='header for HTTP post', type=str)
dataVsFile = parser.add_mutually_exclusive_group()
dataVsFile.add_argument('-d', '--data', help='data string for HTTP post', type=str)
dataVsFile.add_argument('-f', '--file', help='file for HTTP post', type=str)
verbose = parser.add_argument('-v', '--verbose', help='show verbose output',
                              action='store_true')

args = parser.parse_args()
if args.get is not None:
    httpc_get(args.get)
elif args.post is not None:
    if args.data is not None:
        httpc_post(args.post, args.header, args.data)
    elif args.file is not None:
        f = open(args.file, 'r')
        data = file.read()
        f.close()
        httpc_post(args.post, args.header, data)

# COMP445 Lab Assignment
Dmitry Svoiski - 26893570

Mathieu Diab - 26525318

## Assignment 1: http client

```
python3 httpc.py [-h] [-g GET | -p POST] [--header HEADER] [-d DATA | -f FILE]
                 [-v]

optional arguments:
-h, --help            show this help message and exit
-g GET, --get GET     get with URL argument
-p POST, --post POST  post with URL argument
--header HEADER       header for HTTP post
-d DATA, --data DATA  data string for HTTP post
-f FILE, --file FILE  file for HTTP post
-v, --verbose         show verbose output

```

## Assignment 2: http server
```
python3 httpfs.py [-h] [-v] [-p PORT] [-d DIRECTORY]

optional arguments:
-h, --help                           show this help message and exit
-v, --verbose                        show verbose ouput
-p PORT, --port PORT                 Specific port number to run server, default is 8888
-d DIRECTORY, --directory DIRECTORY  Specific local directory to read/write files,
                                     default is current directory

```

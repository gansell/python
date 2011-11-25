# file: simple.py

from BaseHTTPServer import HTTPServer                   #1
from SimpleHTTPServer import SimpleHTTPRequestHandler   #2
from SocketServer import ThreadingMixIn                 #3


class ThreadingServer(ThreadingMixIn, HTTPServer):      #4
    pass
serveraddr = ('', 8080)                                 #5
server = ThreadingServer(serveraddr, SimpleHTTPRequestHandler)
server.serve_forever()                                  #6
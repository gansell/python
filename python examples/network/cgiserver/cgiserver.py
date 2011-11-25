# file: cgiserver.py

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler     #1
from SocketServer import ThreadingMixIn


class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass
serveraddr = ('', 8080)
server = ThreadingServer(serveraddr, CGIHTTPRequestHandler)
server.serve_forever()                              #1

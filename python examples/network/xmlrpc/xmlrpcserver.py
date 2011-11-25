# file: xmlrpcserver.py

from SimpleXMLRPCServer import SimpleXMLRPCServer, \
SimpleXMLRPCRequestHandler                          #1
from SocketServer import ThreadingMixIn             #2

import plain_pi                                     #3

def pi(n):                                          #4
    """
    Calculation of pi with Monte Carlo Simulation.

    n is the number of iterations.    
    """
    return plain_pi.piPlain(n)

class ThreadingServer(ThreadingMixIn,               #5
                      SimpleXMLRPCServer):
    pass

serveraddr = ('', 8888)                             #6
server = ThreadingServer(serveraddr,                #7
                         SimpleXMLRPCRequestHandler)
server.register_function(pi)                        #8
server.register_introspection_functions()           #9
server.serve_forever()                              #10
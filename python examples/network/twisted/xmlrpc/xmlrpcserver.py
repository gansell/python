# file: xmlrpcserver.py

from twisted.web import server, resource, xmlrpc    #1
from twisted.internet import reactor

import plain_pi                                     #2

class PiMaker(xmlrpc.XMLRPC):                       #3
    def xmlrpc_pi(self, n):                         #4
        return plain_pi.piPlain(n)
    xmlrpc_pi.signature = [['int'], ['double']]     #5
    xmlrpc_pi.help = 'Calculate pi with Monte ' \
                     'Carlo method.'                #6

pimaker = PiMaker()                                 #7
xmlrpc.addIntrospection(pimaker)                    #8
siteRoot = resource.Resource()                      #9
siteRoot.putChild('', pimaker)                      #10
reactor.listenTCP(8888, server.Site(siteRoot))      #11
reactor.run()
        
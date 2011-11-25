# file: soapserver.py

from twisted.web import server, resource, soap  #1
from twisted.internet import reactor

import plain_pi

class PiMaker(soap.SOAPPublisher):              #2
    def soap_pi(self, n):                       #3
        return plain_pi.piPlain(n)


siteRoot = resource.Resource()
siteRoot.putChild('', PiMaker())
reactor.listenTCP(8888, server.Site(siteRoot))
reactor.run()
        
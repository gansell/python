# file: pbserver.py

from twisted.spread import pb                       #1
from twisted.internet import reactor

import plain_pi

class PiMaker(pb.Root):                             #2
    def remote_pi(self, n):                         #3
        return plain_pi.piPlain(n)


reactor.listenTCP(8888, 
                  pb.PBServerFactory(PiMaker()))    #4
reactor.run()

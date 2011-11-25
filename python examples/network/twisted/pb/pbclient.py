# file: pbclient.py

from twisted.spread import pb                       #1
from twisted.internet import reactor

def gotObject(object):                              #2
    object.callRemote("pi",int(1e7)                 #3
                     ).addCallback(gotData)         #4

def gotData(pi):                                    #5
    print 'server sent pi:', pi
    reactor.stop()

def gotNoObject(reason):                            #6
    print "no object:",reason
    reactor.stop()

if __name__ == '__main__':
    factory = pb.PBClientFactory()                  #7
    reactor.connectTCP("localhost", 8888, factory)  #8
    factory.getRootObject().addCallbacks(           #9
                             gotObject, gotNoObject)
    reactor.run()

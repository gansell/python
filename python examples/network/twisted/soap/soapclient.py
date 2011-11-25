# file: soapclient.py

from twisted.web import soap                        #1
from twisted.internet import reactor

proxy = soap.Proxy('http://localhost:8888/')        #2

n = int(1e5)
d = proxy.callRemote('pi', n)                       #3

def showPi(pi):                                     #4
    print 'n: ', n
    print 'pi:', pi

def showError(failure):                             #5
    print 'Error:', failure.getErrorMessage()
    print failure.getTraceback()
    
d.addCallback(showPi).addErrback(showError)         #6

reactor.run()

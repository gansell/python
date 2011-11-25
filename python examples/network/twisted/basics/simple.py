# file: simple.py

from twisted.internet import reactor              #1

print "Twisted is running with reactor."
reactor.run()                                     #2
print 'Reactor stopped through external signal.'
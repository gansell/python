# file: simplecounter.py

from twisted.internet import reactor

counter = 0                                 #1

def showCounter():                          #2
    global counter                          #3
    counter += 1
    if counter == 1:
        print 'Called once.'
    elif counter == 2:
        print 'Called twice.'
    else:
        print 'Called %d times.' %counter

def stopReactor():                          #4
    print 'Stopping Twisted reactor with function.'
    reactor.stop()                          #5

for n in range(5):
    reactor.callLater(n, showCounter)       #6
    
reactor.callLater(n+1, stopReactor)         #7

print 'Reactor started running.'
reactor.run()                               #8
print 'Reactor stopped running.'
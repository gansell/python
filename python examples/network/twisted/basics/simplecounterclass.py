# file: simplecounterclass.py

from twisted.internet import reactor

class Counter:                                      #1
    def __init__(self, n=0):
        self.n = n

def showCounter(counter):                           #2
    counter.n += 1
    if counter.n == 1:
        print 'Called once.'
    elif counter.n == 2:
        print 'Called twice.'
    else:
        print 'Called %d times.' %counter.n

def stopReactor():                                  #3
    print 'Stopping Twisted reactor with function.'
    reactor.stop()                                  #4

counter = Counter()
for n in range(5):
    reactor.callLater(n, showCounter, counter)      #5
    
reactor.callLater(n+1, stopReactor)                 #6

print 'Reactor started running.'
reactor.run()                                       #7
print 'Reactor stopped running.'
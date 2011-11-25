# file: simpledefer.py

from twisted.internet import reactor, defer         #1

def giveData(seconds):                              #2
    data = [1, 2, 3]                                #3
    d = defer.Deferred()                            #4
    reactor.callLater(seconds, d.callback, data)    #5
    return d                                        #6

def showData(result):                               #7
    print 'data is:', result


d = giveData(2)                                     #8
d.addCallback(showData)                             #9

reactor.run()                                       #10

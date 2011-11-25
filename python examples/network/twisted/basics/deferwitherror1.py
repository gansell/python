# file: deferwitherror.py

from twisted.internet import reactor, defer


def produceData(seconds, limit, d):             #1
    data = [1, 2, 3]
    if seconds <= limit:                        #2
        d.callback(data)
    else:                                       #3
        d.errback(ValueError(
            'Only less then %s seconds are allowed.'
            %limit))
    
def giveData(seconds, limit=2):                 #4
    d = defer.Deferred()                        #5
    reactor.callLater(min(seconds, limit),      #6
                      produceData,
                      seconds, limit, d)
    return d                                    #7
    
def showData(result):
    print 'data is:', result
	
def modData(result):
	result[0] += 1
	result[1] += 1
	result[2] += 1
	return result
	
def newError(failure):
	print 'This would be a new error'
	return failure


def printError(failure):                        #8
    #failure.printTraceback()                    #9
    print 'Error:',  failure.getErrorMessage() #10
    reactor.stop()                              #11

    
d = giveData(1)                                 #12
d.addCallback(modData).addCallback(showData).addErrback(newError).addErrback(printError)  #13
# eqivalent to:
# d.addCallback(showData)
# d.addErrback(printError)

reactor.run()

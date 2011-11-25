import time
from twisted.internet import reactor

def every_second():
	print time.ctime()
	reactor.callLater(1, every_second)

reactor.callLater(1, every_second)
reactor.run()	


import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8888')
n = int(1e5)
print 'help on Pi:'
print s.system.methodHelp('pi')
print
print 'n: ',n
print 'pi:', s.pi(n)
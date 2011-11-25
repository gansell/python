# file: xmlrpclient.py

import xmlrpclib                                    #1

s = xmlrpclib.ServerProxy('http://localhost:8888/') #2

n = int(1e6)                                        #3
print 'Help on pi:' 
print s.system.methodHelp('pi')                     #4
print
print 'n: ', n
print 'pi:', s.pi(n)                                #5

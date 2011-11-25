# file: clusterServer.py

import sys
import Pyro.core
import Pyro.naming
import counter


class Counter(Pyro.core.ObjBase, counter.InsideCounter):
    pass

try:
    hostname = sys.argv[1]                              #1
except IndexError:
    print 'Please give hostname as command line argument.'
    print 'It will be used to register the calculator with the NS.'
    print 'Example: hostname:node1, object_name:counter_node1'
    
Pyro.core.initServer()
ns=Pyro.naming.NameServerLocator().getNS()
daemon=Pyro.core.Daemon()
daemon.useNameServer(ns)
uri=daemon.connect(Counter(),'counter_%s' %hostname)    #2

print 'Server with object counter_%s is ready.' %hostname
daemon.requestLoop()

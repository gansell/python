# file: server.py

import Pyro.core                                #1
import Pyro.naming                              #2
import pi                                       #3

class SimplePi(Pyro.core.ObjBase, pi.PiMaker):  #4
    pass                                        #5
#    def __init__(self):                        #6
#        Pyro.core.ObjBase.__init__(self)

Pyro.core.initServer()                          #7
ns=Pyro.naming.NameServerLocator().getNS(
'PYRO://127.0.0.1:9090/7f00000108cc13edbc69d1418b83b3aa')  #8
daemon=Pyro.core.Daemon()                       #9
daemon.useNameServer(ns)                        #10
uri=daemon.connect(SimplePi(), "pyropi")        #11

print "Server is ready."
daemon.requestLoop()                            #12

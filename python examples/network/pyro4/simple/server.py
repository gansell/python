# file: server.py

import Pyro4                                    #1
import pi                                       #2

daemon = Pyro4.Daemon()                         #3
ns = Pyro4.locateNS(st)                           #4
uri = daemon.register(pi.PiMaker())             #5
ns.register("pyropi", uri)                      #6

print "Server is ready."
daemon.requestLoop()                            #7

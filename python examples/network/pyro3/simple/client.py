# file: client.py

import Pyro.core                                  #1

Pyro.core.initClient()                            #2

picalculator = Pyro.core.getProxyForURI(          #3
                "PYRONAME://pyropi")

print '\npi calcualted through pyro:',
print picalculator.calcPi(int(1e5))               #4


# file: client.py

import Pyro4                                       #1


picalculator = Pyro4.Proxy("PYRONAME:pyropi")      #2

print '\npi calcualted through pyro:',
print picalculator.calc_pi(int(1e7))               #3


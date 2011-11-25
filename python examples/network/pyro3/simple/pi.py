# file: pi.py

import plain_pi                         #1

class PiMaker:                          #2
    
    def calcPi(self, n):                #3
        return plain_pi.pi_plain(n)
    
    def error(self, n):                 #4
        return int(n) / 0
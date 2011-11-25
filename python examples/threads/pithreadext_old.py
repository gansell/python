# file: pithreadprocess.py

import math 
import threading    
import os                                               #1
import sys

import count_ext

#sys.setcheckinterval(1)

class ThreadedPi(threading.Thread):                     #2
    
    def __init__(self, n):
        self.n = n
        threading.Thread.__init__(self)                 #3

    def countInside(self):
        self.count = count_ext.counter(self.n)
        
    def run(self):                                      #5
        self.countInside()


class PiMaker(object):                                  #6
    
    def __init__(self, numberOfIterations = 1000,       #7
                 numberOfThreads = 10):
        self.numberOfThreads = numberOfThreads
        self.numberOfIterations = numberOfIterations
        
    def calculatePi(self):
        piThreads = []                                  #8
        loops = [self.numberOfIterations] * self.numberOfThreads
        for n in loops:
            t = ThreadedPi(n)                           #9
            t.start()                                   #10
            piThreads.append(t)                         #11
        for t in piThreads:
            t.join()                                    #12
        nTotal = sum(loops)                             #13
        insideTotal = sum([x.count for x in piThreads]) #14
        print insideTotal, nTotal
        pi = 4.0 * insideTotal / nTotal                 #15
        self.nTotal = nTotal
        return pi
    
if __name__ == '__main__':                              #16
    import time
    n = int(1e8)
    threads = 2
    start = time.clock()
    p = PiMaker(n/threads, threads)
    print p.calculatePi()
    print 'Time with %d threads:' %threads, time.clock() - start
    start = time.clock()
    p = PiMaker(n, 1)
    print p.calculatePi()
    print 'Time with 1 threads:', time.clock() - start
    print math.pi
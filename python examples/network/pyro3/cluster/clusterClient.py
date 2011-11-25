# file: clusterClient.py

import Pyro.util
import Pyro.core
import threading                                    #1

class PiMaker(object):
    def __init__(self, n, nodes=['node1', 'node2']):#2
        self.n = n                                  #3
        self.nodes = nodes
        self.numberOfNodes = len(self.nodes)
        
    def connectToNodes(self):                       #4
        Pyro.core.initClient()                      #5
        self.pyroNodes = []                         #6
        for node in self.nodes:                     #7
            self.pyroNodes.append(
                   Pyro.core.getProxyForURI(
                   'PYRONAME://counter_%s' %node))
                
    def splitN(self):                               #8
        minNumber = self.n/len(self.nodes)
        self.partialNs = [minNumber]* self.numberOfNodes
        self.partialNs[-1] += self.n - \
                              self.numberOfNodes * minNumber
                
    def calcPi(self):                               #9
        self.connectToNodes()                       #10
        self.splitN()                               #11
        threads = []                                #12
        for pyroNode, partialN in zip(self.pyroNodes,
                                      self.partialNs):
            threads.append(CounterThread(pyroNode,  #13
                                         partialN))
        for thread in threads:
            thread.start()                          #14
        for thread in threads:
            thread.join()                           #15
        insideTotal = 0
        for thread in threads:
            insideTotal += thread.insideCount       #16
        return 4.0 * insideTotal / self.n           #17
    
class CounterThread(threading.Thread):              #18
    def __init__(self, remoteCounter, n):
        threading.Thread.__init__(self)             #19
        self.remoteCounter = remoteCounter          #20
        self.n = n                                  #21
        
    def run(self):                                  #22
        self.insideCount = \
             self.remoteCounter.countInside(self.n)

if __name__ == '__main__':
        piMaker = PiMaker(int(1e5))                 #23
        print 'pi through two servers:',
        print piMaker.calcPi()                      #24

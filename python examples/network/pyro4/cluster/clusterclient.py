# file: clusterclient.py


import threading                                    #1

import Pyro4 


class PiMaker(object):
    def __init__(self, n, nodes=['node1', 'node2']):#2
        self.n = n                                  #3
        self.nodes = nodes
        self.number_of_nodes = len(self.nodes)

    def connect_to_nodes(self):                       #4
        self.pyro_nodes = []                         #6
        for node in self.nodes:                     #7
            self.pyro_nodes.append(
                Pyro4.Proxy('PYRONAME:counter_%s' % node))

    def split_n(self):                               #8
        min_number = self.n / len(self.nodes)
        self.partial_ns = [min_number]* self.number_of_nodes
        self.partial_ns[-1] += self.n - \
                              self.number_of_nodes * min_number

    def calc_pi(self):                               #9
        self.connect_to_nodes()                       #10
        self.split_n()                               #11
        threads = []                                #12
        for pyro_node, partial_n in zip(self.pyro_nodes,
                                      self.partial_ns):
            threads.append(CounterThread(pyro_node,  #13
                                         partial_n))
        for thread in threads:
            thread.start()                          #14
        for thread in threads:
            thread.join()                           #15
        inside_total = 0
        for thread in threads:
            inside_total += thread.inside_count       #16
        return 4.0 * inside_total / self.n           #17


class CounterThread(threading.Thread):              #18
    def __init__(self, remote_counter, n):
        threading.Thread.__init__(self)             #19
        self.remote_counter = remote_counter          #20
        self.n = n                                  #21

    def run(self):                                  #22
        self.inside_count = \
             self.remote_counter.count_inside(self.n)


if __name__ == '__main__':
    
    def test():
        pi_maker = PiMaker(int(1e7))                 #23
        print 'pi through two servers:',
        print 'Pi is: ', pi_maker.calc_pi()                      #24

    test()        

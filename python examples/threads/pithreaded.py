# file: pithreaded.py

"""Use threads to calculate pi.
"""

import math
import random
import threading                                         #1


class ThreadedPi(threading.Thread):                      #2
    """The thread.
    """

    def __init__(self, n):
        self.n = n
        super(ThreadedPi, self).__init__()                #3a
        #threading.Thread.__init__(self)                  #3b

    def count_inside(self):
        """Count all hits inside the circle.
        """
        inside = 0
        for count in xrange(self.n):
            x = random.random()
            y = random.random()
            if math.sqrt(x * x + y * y) < 1:
                inside += 1
        self.count = inside                               #4

    def run(self):                                        #5
        """Start the thread.
        """
        self.count_inside()


class PiMaker(object):                                    #6
    """Use threads for calculation of pi.
    """

    def __init__(self, number_of_iterations=1000,         #7
                 number_of_threads=2):
        self.number_of_threads = number_of_threads
        self.number_of_iterations = number_of_iterations

    def calculate_pi(self, thread_class):
        """Start and join the threads.
        """
        pi_threads = []                                   #8
        loops = [self.number_of_iterations] * self.number_of_threads
        for n in loops:
            thread_inst = thread_class(n)                 #9
            thread_inst.start()                           #10
            pi_threads.append(thread_inst)                #11
        for thread_inst in pi_threads:
            thread_inst.join()                            #12
        n_total = sum(loops)                              #13
        inside_total = sum(x.count for x in pi_threads)   #14
        pi = 4.0 * inside_total / n_total                 #15
        self.n_total = n_total
        return pi

def main(threads=2, n=int(1e6), thread_class=ThreadedPi):
    """Test it.
    """
    import timeit
    start = timeit.default_timer()
    pi_maker = PiMaker(n / threads, threads)
    print 'pi:', pi_maker.calculate_pi(thread_class)
    duration = timeit.default_timer() - start
    print 'Time with %d threads:' % threads, duration
    start = timeit.default_timer()
    pi_maker = PiMaker(n, 1)
    print 'pi:', pi_maker.calculate_pi(thread_class)
    duration = timeit.default_timer() - start
    print 'Time with 1 thread:', duration
    print math.pi
        
if __name__ == '__main__':                                #16

    main()

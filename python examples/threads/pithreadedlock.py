# file: pithreadedlock.py


"""Use threads to calculate pi and lock a shared variable.
"""


import math
import random
import threading


class ThreadedPiLock(threading.Thread):
    """A thread that uses locking.
    """

    def __init__(self, n, lock, shared_inside_count):
        self.n = n
        self.lock = lock                                  #1
        self.shared_inside_count = shared_inside_count    #2
        super(ThreadedPiLock, self).__init__()

    def count_inside(self):
        """Count all hits inside the circle and incement shared
        variable.
        """
        for count in range(self.n):
            x = random.random()
            y = random.random()
            if  math.sqrt(x * x + y * y) < 1:
                self.lock.acquire()                       #3
                try:
                    self.shared_inside_count[0] += 1      #4
                finally:
                    self.lock.release()                   #5

    def run(self):
        """Start the thread.
        """
        self.count_inside()


class PiMaker(object):
    """Use threads with locking for calculation of pi.
    """

    def __init__(self, number_of_iterations=1000,
                 number_of_threads=2):
        self.number_of_threads = number_of_threads
        self.number_of_iterations = number_of_iterations
        self.shared_inside_count = [0]

    def calculate_pi(self):
        """Start and join the threads.
        """
        pi_threads = []
        loops = [self.number_of_iterations] * self.number_of_threads
        lock = threading.Lock()                             #6
        for n in loops:
            thread_inst = ThreadedPiLock(n, lock,           #7
                                         self.shared_inside_count)
            thread_inst.start()
            pi_threads.append(thread_inst)
        for thread_inst in pi_threads:
            thread_inst.join()
        n_total = sum(loops)
        pi = 4.0 * self.shared_inside_count[0] / n_total  #8
        return pi


def main(threads=2, n=int(1e6)):
    """Test it.
    """
    import timeit
    start = timeit.default_timer()
    pi_maker = PiMaker(n / threads, threads)
    print 'pi:', pi_maker.calculate_pi()
    duration = timeit.default_timer() - start
    print 'Time with %d threads:' % threads, duration
    start = timeit.default_timer()
    pi_maker = PiMaker(n, 1)
    print 'pi:', pi_maker.calculate_pi()
    duration = timeit.default_timer() - start
    print 'Time with 1 thread:', duration
    print math.pi

if __name__ == '__main__':

    main()

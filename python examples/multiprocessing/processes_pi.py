# file: process_pi.py

import math
try:
    from multiprocessing import Process, Queue                  #1
except ImportError:
    from processing import Process, Queue                       #2
import random
import time


def count_inside(n):                                            #3
    inside_count = 0
    for _ in xrange(n):
        x = random.random()
        y = random.random()
        d = math.sqrt(x*x + y*y)
        if d < 1:
            inside_count += 1
    return inside_count

def calc_pi(n):                                                 #4
    return 4 * count_inside(n) / float(n)

def count_inside_process(q, n):                                 #5
    q.put(count_inside(n))

def calc_pi_processes(n, process_count):                        #6
    min_n = n // process_count                                  #7
    counters = [min_n] * process_count                          #8
    reminder = n % process_count                                #9
    for m in xrange(reminder):                                  #10
        counters[m] += 1                                        #11
    processes = []                                              #12
    for counter in counters:                                    #13
        q = Queue()                                             #14
        p = Process(target=count_inside_process,
                    args=(q, counter))                          #15
        p.start()                                               #16
        processes.append((q, p))                                #17
    inside_count = sum(process[0].get() for process
                       in processes)                            #18
    for process in processes:                                   #19
        process[1].join()                                       #20
    return 4 * inside_count / float(n)                          #21

if __name__ == '__main__':
    import timeit

    process_count = 2                                           #22

    n = int(1e7)                                                #23

    print 'number of tries:. %2.0e' % n                          #24
    
    start = timeit.default_timer()                                        #25
    print 'pi:', calc_pi(n)
    no_time =  timeit.default_timer() - start
    print 'run time no processes:', no_time

    start = timeit.default_timer()                                        #26
    pi = calc_pi_processes(n, process_count)                    #27
    print 'pi', pi
    two_time = timeit.default_timer() - start
    print 'run time %d processes:' % process_count, two_time

    print 'ratio:', no_time/two_time                            #28
    print 'diff:', two_time - no_time

# file pool_pi.py

import math
try:
    from multiprocessing import Pool, cpu_count                 #1
except ImportError:
    from processing import Pool, cpuCount                       #2
    cpu_count = cpuCount
import random
import time


def count_inside(n):
    inside_count = 0
    for _ in xrange(n):
        #time.sleep(1e-5)
        x = random.random()
        y = random.random()
        d = math.sqrt(x*x + y*y)
        if d < 1:
            inside_count += 1
    return inside_count

def calc_pi(n):
    return 4 * count_inside(n) / float(n)

def calc_pi_workers(n, workers=None):                           #3
    if not workers:
        workers = cpu_count()                                    #4
    min_n = n // workers
    counters = [min_n] * workers
    reminder = n % workers
    for m in xrange(reminder):
        counters[m] += 1
    pool = Pool(processes=workers)                              #5
    results = [pool.apply_async(count_inside, (counter,))
                       for counter in counters]                 #6
    inside_count = sum(result.get() for result in results)      #7
    return 4 * inside_count / float(n)                          #8

if __name__ == '__main__':
    import time

    workers = 2

    n = int(1e7)

    print 'number of tries: %2.0e' % n
    start = time.clock()
    print 'pi:', calc_pi(n)
    no_time =  time.clock() - start
    print 'run time no workers:', no_time

    start = time.clock()
    pi = calc_pi_workers(n, workers)
    print 'pi', pi
    two_time = time.clock() - start
    print 'run time %d workers:' % workers, two_time
    print 'ratio:', no_time/two_time
    print 'diff:', two_time - no_time

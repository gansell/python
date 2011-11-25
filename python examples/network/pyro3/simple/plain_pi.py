# file: plain_pi.py

import random, math                                             #1


def piPlain(n):                                                #3
    """Pi with monte carlo.
    """
    count_inside = 0                                            #4
    for count in xrange(n):                                     #5
        x = random.random()                                     #6
        y = random.random()                                     #7
        d = math.sqrt(x * x + y * y)                                #8
        if d < 1:
            count_inside += 1                                   #9
    return 4.0 * count_inside / n                               #10



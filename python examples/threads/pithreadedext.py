# file: pithreaded.py

"""Use threads to calculate pi.
"""

import math
import random
import threading

import count_ext                                         #1
import pithreaded                                        #2


class ThreadedPiExt(threading.Thread):
    """The thread.
    """

    def __init__(self, n):
        self.n = n
        super(ThreadedPiExt, self).__init__()

    def count_inside(self):
        """Count all hits inside the circle.
        """
        self.count = count_ext.count(self.n)              #3

    def run(self):
        """Start the thread.
        """
        self.count_inside()



if __name__ == '__main__':

    pithreaded.main(2, int(1e8), ThreadedPiExt)           #4
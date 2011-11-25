# file: pithreadedsleep.py

import threading
import time

import pithreaded


class ThreadedPiSleep(threading.Thread):
    """Thread that just waits for while.
    """
    def __init__(self, n):
        self.n = n
        super(ThreadedPiSleep, self).__init__()
        self.count = 0

    def count_inside(self):
        """No counting, just wait.
        """
        time.sleep(2)                                     #1
        self.count += 1

    def run(self):
        """Start the thread.
        """
        self.count_inside()


if __name__ == '__main__':

    pithreaded.main(thread_class=ThreadedPiSleep)        #2

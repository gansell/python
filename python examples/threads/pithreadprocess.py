# file: pithreadprocess.py

# file: pithreadedsleep.py

import subprocess
import threading

import pithreaded


class ThreadedPiProcess(threading.Thread):
    """Thread that just waits for while.
    """
    def __init__(self, n):
        self.n = n
        super(ThreadedPiProcess, self).__init__()
        self.count = 0

    def count_inside(self):
        """No counting with eternal process.
        """
        pipe = subprocess.Popen(['count'],
                                shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        pipe.stdin.write('%d\n' % self.n)
        self.count = int(pipe.stdout.read())

    def run(self):
        """Start the thread.
        """
        self.count_inside()


if __name__ == '__main__':

    pithreaded.main(n=1e8, thread_class=ThreadedPiProcess)        #2

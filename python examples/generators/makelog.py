"""Creating a log files that is continuously updated.
"""

import random
import time


def log(file_name):
    """Write some random log data.
    """
    fobj = open(file_name, 'w')
    while True:
        value = random.randrange(0, 100)
        if value < 10:
            fobj.write('# comment\n')
        else:
            fobj.write('%d\n' % value)
        fobj.flush()
        time.sleep(2)

if __name__ == '__main__':

    def test():
        """Start logging.
        """
        import sys
        file_name = sys.argv[1]
        print 'logging to', file_name
        log(file_name)
    test()

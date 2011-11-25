"""Use generators to sum log file data on the fly.
"""

import sys
import time


def read_forever(fobj):
    """Read from a file as long as there are lines.
    Wait for the other process to write more lines.
    """
    while True:
        line = fobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def filter_comments(lines):
    """Filter out all lines starting with #.
    """
    for line in lines:
        if not line.strip().startswith('#'):
            yield line


def get_number(lines):
    """Read the number in the line and convert it to an integer.
    """
    for line in lines:
        yield int(line.split()[-1])


def show_sum():
    """Start all the generators and calculate the sum continuously.
    """
    lines = read_forever(open('log.txt'))
    filtered_lines = filter_comments(lines)
    numbers = get_number(filtered_lines)
    sum_ = 0
    try:
        for number in numbers:
            sum_ += number
            sys.stdout.write('sum: %d\r' % sum_)
            sys.stdout.flush()
    except KeyboardInterrupt:
        print 'sum:', sum_

if __name__ == '__main__':
    show_sum()

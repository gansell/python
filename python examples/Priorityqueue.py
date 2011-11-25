from Queue import PriorityQueue
import random
from threading import Thread
import time

THREADS = 1000

def do_work(priority, item, thread_counter):
    print 'working on item %d in worker %d with priority %d\n' % (item, thread_counter, priority)
    #wait = random.random()
    wait = 0.1
    time.sleep(wait)
    print 'waited %f seconds processing item %d\n' % (wait, item)


def worker(thread_counter, queue_obj):
    while(True):
        priority, item = queue_obj.get()
        do_work(priority, item, thread_counter)
        queue_obj.task_done()

def run(queue_obj):
    for item in range(1000):
        priority = random.choice([10, 20, 30, 40, 50])
        queue_obj.put((priority, item))
    for thread_counter in range(THREADS):
        thread = Thread(target=worker, args=(thread_counter, queue_obj))
        thread.daemon=(True)
        thread.start()
    queue_obj.join()


if __name__ == '__main__':
    print 'priority'
    print '==='
    run(PriorityQueue())

    
                    
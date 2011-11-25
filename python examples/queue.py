from Queue import Queue, LifoQueue
import random
from threading import Thread
import time

THREADS = 10

def do_work(item, thread_counter):
    print 'working on item %d in worker %d\n' % (item, thread_counter)
    #wait = random.random()
    wait = 2
    time.sleep(wait)
    print 'waited %f seconds processing item %d\n' % (wait, item)


def worker(thread_counter, queue_obj):
    while(True):
        item = queue_obj.get()
        do_work(item, thread_counter)
        queue_obj.task_done()

def run(queue_obj):
    for item in range(10):
        queue_obj.put(item)
    for thread_counter in range(THREADS):
        thread = Thread(target=worker, args=(thread_counter, queue_obj))
        thread.daemon=True
        thread.start()
    queue_obj.join()


if __name__ == '__main__':
    print 'fifo'
    print '==='
    run(Queue())
    print 'lifo'
    print '==='
    run(LifoQueue())
    
                    
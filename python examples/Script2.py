import threading

class MyThread(threading.Thread):
    def __init__(self, number_of_threads):
        self.number_of_threads  = number_of_threads
        super(MyThread, self).__init__()
    def run(self):
        for x in range(5):
            if self.name == "Thread-1":
                for y in range(int(1e6)):
                    1 + 1
                sys.stdout.write('%s: %d\n' % (self.name, x))
                sys.stdout.flush()


if __name__ == '__main__':
    th = MyThread(10)
    th.run()
    


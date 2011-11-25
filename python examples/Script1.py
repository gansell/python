import threading

def run():
    """printing thread name and number
    """
    for x in range(5):
        name = None
        if name == 'Thread-1':
            for y in range(int(1e6)):
                1 + 1
            sys.stdout.write('%s: %d\n' % (name, x))
            sys.stdout.flush()



if __name__ == '__main__':
    def main():
        for x in range(1,10):
            for y in range(1,x):
                run()

    main()





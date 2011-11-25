# file: clusterserver.py

import sys

import Pyro4

import counter


def main():
    try:
        hostname = sys.argv[1]                              #1
    except IndexError:
        print 'Please give hostname (e.g. `node1`) as command line argument.'
        print 'It will be used to register the calculator with the NS.'
        print 'Example: the hostname `node1` will result in an object'
        print 'name `counter_node1`'


    daemon=Pyro4.Daemon()
    ns=Pyro4.locateNS() 
    uri=daemon.register(counter.InsideCounter())
    ns.register('counter_%s' %hostname, uri)

    print 'Server with object counter_%s is ready.' %hostname
    daemon.requestLoop()                            #12


if __name__ == '__main__':
    main()




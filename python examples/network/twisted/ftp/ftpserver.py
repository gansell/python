# file: ftpserver.py

from twisted.cred.portal    import Portal               #1
from twisted.protocols.ftp  import FTPRealm             #2
from twisted.cred.checkers  import AllowAnonymousAccess #3
from twisted.cred.checkers  import FilePasswordDB       #4
from twisted.protocols.ftp  import FTPFactory           #5

p = Portal(FTPRealm('data'),                            #6
           (AllowAnonymousAccess(),                     #7
            FilePasswordDB("password.dat")))            #8

from twisted.internet import reactor
reactor.listenTCP(21, FTPFactory(p))                    #9
reactor.run()

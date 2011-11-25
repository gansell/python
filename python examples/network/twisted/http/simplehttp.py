# file: simplehttp.py

from twisted.web import http                        #1

class SimpleRequestHandler(http.Request):           #2
    pages = {                                       #3
        '/': '<h1>Twisted served page</h1>' \
               'This is served by twisted.',
        '/sub': '<h1>Sub page</h1>'\
                'This page is in a sub dircetory.',
        }
    
    def process(self):                              #4
        self.setHeader('Content-Type', 'text/html') #5
        if self.pages.has_key(self.path):           #6
            self.write(self.pages[self.path])
        else:                                       #7
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>404 Page not Found"
                       "</h1>Sorry, no page %s."
                       %self.path)
        self.finish()                               #8

class SimpleHttp(http.HTTPChannel):                 #9
    requestFactory = SimpleRequestHandler

class SimpleHttpFactory(http.HTTPFactory):          #10
    protocol = SimpleHttp

if __name__ == "__main__":
    from twisted.internet import reactor
    reactor.listenTCP(8080, SimpleHttpFactory())    #11
    reactor.run()                                   #12

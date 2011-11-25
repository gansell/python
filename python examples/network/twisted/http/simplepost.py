# file: simplepost.py

import math
import timeit

from twisted.web import http

import plain_pi                                     #1

def renderEntryPage(request):                       #2
    request.write("""
    <html>
    <head>
      <title>Pi with Twisted</title>
    </head>
    <body>
    <h1>Twisted-based Calculation of pi with
        the Monte Carlo Method</h1>
      <form action='calcpi' method='post'>
        <pre>
            Number of iterations: <input type="int"
                 name="n" maxlength="10" size="10"\>
            <input type="submit" value="Calculate"\>
        </pre>
    </body>
    </html>
    """)
    request.finish()

def handlePiPost(request):                          #3
    n = int(float(request.args['n'][0]))            #4
    start = timeit.default_timer()
    pi = plain_pi.piPlain(n)                        #5
    duration = timeit.default_timer() - start 
    request.write('''
        <html>
        <head><title>Pi with Twisted</title></head>
        <body>
        <h1>
        Twisted - Result of Monte Carlo Calculation of Pi
        </h1>
        <table>
        <tr>
        <td>Number of iterations</td>
        <td>%d</td>
        </tr>
        <tr>
        <td>Pi by Monte Carlo Method</td>
        <td>%15.12f </td>
        </tr>
        <tr>
        <td>Exact pi</td>
        <td>%15.12f </td>
        </tr>
        <td>Calculation time</td>
        <td>%15.3f seconds</td>
        </tr>
        </table>
        </body>
        </html>
    ''' %(n, pi, math.pi, duration))                #6
    request.finish()

class FunctionHandledRequest(http.Request):         #7
    pageHandlers = {                                #8
        '/': renderEntryPage,
        '/calcpi': handlePiPost,
        }
    
    def process(self):                              #9
        self.setHeader('Content-Type', 'text/html')
        if self.pageHandlers.has_key(self.path):    #10
            handler = self.pageHandlers[self.path]
            handler(self)                           #11
        else:                                       #12
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such page.")
            self.finish()

class PiHttp(http.HTTPChannel):
    requestFactory = FunctionHandledRequest

class PiHttpFactory(http.HTTPFactory):
    protocol = PiHttp

if __name__ == "__main__":
    from twisted.internet import reactor
    reactor.listenTCP(8080, PiHttpFactory())
    reactor.run()

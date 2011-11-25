# file: nonblocking_post.py

# Dynamic Twisted imports not recognized.
# pylint: disable-msg=E1101

"""
Example for a non-blocking HTTP server with Twisted.

Two things are important:
1. The render method of a page returns `server.NOT_DONE_YET` to
   signal that it will deliver its content later.
2. We use the decorator `@defer.inlineCallbacks` to make
   using deferreds easier.
"""


import math
import time

from twisted.internet import defer, threads
from twisted.web import resource, server

import plain_pi


class EntryPage(resource.Resource):
    """Start page with form for inputing calculation values.
    """

    def render(self, request):
        """Render the page.
        """
        return """
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
        """


class PiPost(resource.Resource):
    """Page showing the calculation results.
    """

    def render(self, request):
        """Render asynchronously using `server.NOT_DONE_YET`.
        """
        self._calculatePi(request).addCallback(self._gotResult, request)
        return server.NOT_DONE_YET

    @staticmethod
    @defer.inlineCallbacks
    def _calculatePi(request):
        """Generator to calculate pi.

        We use the decorator `@defer.inlineCallbacks to write
        this method sequentially but still use a deferred.
        With suspend `piPlan` to a thread to make it nonblocking.
        """
        iterations = int(float(request.args['n'][0]))
        start = time.time()
        calc_pi = yield threads.deferToThread(plain_pi.piPlain, iterations)
        duration = time.time() - start
        defer.returnValue({'iterations': iterations,
                           'pi': calc_pi,
                           'duration': duration,
                           'math_pi': math.pi})

    @staticmethod
    def _gotResult(result, request):
        """Render the result page.

        This staticmethod, i.e. function inside a class without
        access to `self` is added as a callback.
        """
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
            <td>%(iterations)d</td>
            </tr>
            <tr>
            <td>Pi by Monte Carlo Method</td>
            <td>%(pi)15.12f </td>
            </tr>
            <tr>
            <td>Exact pi</td>
            <td>%(math_pi)15.12f </td>
            </tr>
            <td>Calculation time</td>
            <td>%(duration)15.3f seconds</td>
            </tr>
            </table>
            </body>
            </html>
        ''' % result)             #6
        request.finish()


def main():
    """Setup and start the server.
    """
    from twisted.internet import reactor
    root = resource.Resource()
    root.putChild('', EntryPage())
    root.putChild('calcpi', PiPost())
    site = server.Site(root)
    reactor.listenTCP(8080, site)
    reactor.run()


if __name__ == "__main__":
    main()

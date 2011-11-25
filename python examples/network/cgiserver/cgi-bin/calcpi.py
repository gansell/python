#!/usr/bin/env python

import math
import cgi                                  #1
import cgitb                                #2
import timeit
import plain_pi                             #3
import pithreaded

cgitb.enable()                              #4

form = cgi.FieldStorage()                   #5
n = int(float(form.getvalue('n')))          #6
parallel = form.getvalue('parallel')        #6a
if parallel:
    parallel = 'yes'
else:
    parallel = 'no'
                                            #7
template = '''                              

<html>
<head><title>CGI with Python</title></head>
<body>
<h1>
Result of Monte Carlo Calculation of Pi
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
</tr>
<td>Calculation parallel</td>
<td>%s</td>
</tr>
</table>
</body>
</html>
'''


start = timeit.default_timer()

if parallel == 'no':
    pi = plain_pi.piPlain(n)                    #8
else:
    pi_maker = pithreaded.PiMaker(n, 2)
    pi = pi_maker.calculate_pi(pithreaded.ThreadedPi)
	
duration = timeit.default_timer() - start

print template %(n, pi, math.pi, duration, parallel)  #9

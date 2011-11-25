# file: counter.py

import random
import math

class InsideCounter:                    #1
    def countInside(self, n):
        insideCount = 0
        for count in range(n):
            x = random.random()
            y = random.random()
            d = math.sqrt(x*x + y*y)
            if d < 1:
                insideCount += 1
        return insideCount              #2

# file: counter.py

import random
import math

class InsideCounter:                    #1

    def count_inside(self, n):
        inside_count = 0
        for count in range(n):
            x = random.random()
            y = random.random()
            d = math.sqrt(x * x + y *y )
            if d < 1:
                inside_count += 1
        return inside_count              #2

from math import *
from cmath import *
AB = int(input())
BC = int(input())
result = round(degrees(phase(complex(BC / 2, AB / 2 ))))
print(result)

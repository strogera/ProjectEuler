from collections import defaultdict
from math import sqrt

allPerims = defaultdict(int)
for a in range(2, 999):
    for b in range(1, a):
        c = sqrt(a*a - b*b)
        perim = int(a + b + c)
        if c.is_integer() and perim <=1000 and a*a == b*b + c*c:
            allPerims[perim] += 1
print(max([(allPerims[k], k) for k in allPerims])[1])
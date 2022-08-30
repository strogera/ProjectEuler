from math import sqrt
from math import ceil


def getNumberOfFactors(x: int):
    if x == 1:
        return 1
    count = 0
    end = ceil(sqrt(x))
    for d in range(1, end):
        if x % d == 0:
            count += 2
    if (end * end == x):
        count += 1
    return count


def getTriangleNumberGenerator():
    triangleNum = 0
    step = 0
    while(True):
        triangleNum += step
        step += 1
        yield triangleNum


for triangleNum in getTriangleNumberGenerator():
    if (getNumberOfFactors(triangleNum) > 500):
        print(triangleNum) 
        break

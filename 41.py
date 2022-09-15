from math import sqrt
from itertools import permutations

def isPrime(n) -> bool:
    if n <= 1:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

for l in range(9, 1, -1):
    for comb in permutations([x for x in range(l, 0, -1)]):
        x = int(''.join([str(x) for x in comb]))
        if isPrime(x):
            print(x)
            exit()
from math import sqrt
from itertools import permutations


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    i = 2
    while i <= int(sqrt(n)) + 1:
        if n % i == 0:
            return False
        i += 1
    return True


fourDigitPrimes = []

for n in range(1000, 10000):
    if isPrime(n):
        fourDigitPrimes.append(n)

for prime in fourDigitPrimes:
    candidates = set()
    for p in permutations(str(prime), 4):
        currNum = int(''.join(p))
        if str(currNum)[0] != 0 and currNum in fourDigitPrimes:
            candidates.add(currNum)
    candidates = list(candidates)
    if len(candidates) >= 3:
        for i in range(len(candidates)):
            dList = []
            for j in range(len(candidates)):
                if i == j:
                    continue
                if abs(candidates[i] - candidates[j]) == 3330:
                    dList.append((candidates[i], candidates[j]))
            for d1 in dList:
                for d2 in dList:
                    if d1 == d2:
                        continue
                    if 1487 not in d1 and 1487 not in d2:
                        if d1[0] in d2 or d1[1] in d2:
                            print(''.join(
                                str(x)
                                for x in sorted(set(list(d1) + list(d2)))))
                            exit()
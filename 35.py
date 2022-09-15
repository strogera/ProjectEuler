from math import sqrt


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


seenPrime = set()
seenNotPrime = set()
res = []
for x in range(2, 1000000):
    allPrime = True
    for r in range(len(str(x))):
        rot = str(x)[r:] + str(x)[:r]
        if rot in seenNotPrime:
            allPrime = False
            break
        if rot not in seenPrime:
            if isPrime(int(rot)):
                seenPrime.add(int(rot))
            else:
                allPrime = False
                seenNotPrime.add(rot)
                break
    if allPrime:
        res.append(x)
print(len(res))

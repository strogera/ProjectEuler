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
res = set()
x = 10
while len(res) < 11:
    x += 1
    allPrime = True
    for curNum in [int(str(x)[i:]) for i in range(len(str(x)))] + [int(str(x)[: -i]) for i in range(1, len(str(x)))]:
        if curNum in seenNotPrime:
            allPrime = False
            seenNotPrime.add(curNum)
            break
        if curNum in seenPrime or isPrime(curNum):
            seenPrime.add(curNum)
        else:
            allPrime = False
            seenNotPrime.add(curNum)
            break
    if allPrime:
        res.add(x)
print(sum(res))



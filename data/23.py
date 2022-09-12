from math import sqrt

def getDivisors(n):
    i = 1
    divisors = []
    while i <= sqrt(n):
        if n % i == 0:
            divisors.append(i)
            if i != 1 and n // i != i:
                divisors.append(n // i)
        i += 1
    return divisors


def isAbuntantNum(n):
    return n < sum(getDivisors(n))

abuntantNums = set()

upperLimit = 28123
for n in range(1, upperLimit):
    if isAbuntantNum(n):
        abuntantNums.add(n)

abuntantSums = set()
for a in abuntantNums:
    for b in abuntantNums:
        if a + b < upperLimit:
            abuntantSums.add(a + b)

print(sum(x for x in range(upperLimit)) - sum(abuntantSums))

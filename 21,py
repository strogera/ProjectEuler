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


def sumOfDivisors(n):
    return sum(getDivisors(n))

sumOfDivisorsDict = {}
amicableNumbers = set()
for x in range(1, 10001):
    curSum = sumOfDivisors(x)
    if curSum != x and curSum in sumOfDivisorsDict and sumOfDivisorsDict[curSum] == x:
        amicableNumbers.add(x)
        amicableNumbers.add(curSum)
    sumOfDivisorsDict[x] = curSum
        
print(sum((sumOfDivisorsDict[x] for x in amicableNumbers)))
from math import sqrt


def isPrime(n):
    if (n <= 0):
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


maxConsecutivePrimes = 0
maxConsecutivePrimesCoefficients = (0, 0)
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        countConsecutivePrimes = 0
        for n in range(79):
            if isPrime(n * n + a * n + b):
                countConsecutivePrimes += 1
            else:
                break
        if maxConsecutivePrimes < countConsecutivePrimes:
            maxConsecutivePrimes = countConsecutivePrimes
            maxConsecutivePrimesCoefficients = (a, b)

print(maxConsecutivePrimesCoefficients[0] *
      maxConsecutivePrimesCoefficients[1])

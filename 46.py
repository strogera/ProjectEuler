from math import sqrt


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


primes = []
x = 1
while x := x + 2:
    if isPrime(x):
        primes.append(x)
    else:
        if not any(p + 2 * (d**2) == x for p in reversed(primes) for d in range(1, int((x - p) / 2) + 1)):
            print(x)
            break
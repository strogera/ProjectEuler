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


primes = set()

for n in range(1000000):
    if isPrime(n):
        primes.add(n)

sol = 0
maxLength = 0
primesList = sorted(primes)
for i, p in enumerate(primesList):
    summ = p
    count  = 1
    for j in range(i + 1, len(primesList)):
        summ +=  primesList[j]
        count += 1
        if summ >= 1000000:
            break
        if summ in primes and count > maxLength:
            sol = summ
            maxLength = count

print(sol)


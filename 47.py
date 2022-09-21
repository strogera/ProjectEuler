from collections import defaultdict

primes = []
cache = defaultdict(list)


def uniquePrimeFactors(n):
    for p in primes:
        if n % p == 0:
            return list(set(cache[n // p] + [p]))
    primes.append(n)
    return [1]


n = 1
while True:
    n += 1
    cache[n] = uniquePrimeFactors(n)
    if (len(cache[n]), len(cache[n - 1]), len(cache[n - 2]), len(cache[n - 3])) == (4, 4, 4, 4):
        print(n - 3)
        break
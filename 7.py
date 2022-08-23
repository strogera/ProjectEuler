from math import sqrt

x = 5
countPrime = 2
while (True):
    isPrime = True
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            isPrime = False
            break
    if isPrime:
        countPrime += 1
    if countPrime == 10001:
        break
    x = x + 2
print(x)
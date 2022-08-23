from math import sqrt

x = 5
summ = 5
while (True):
    isPrime = True
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            isPrime = False
            break
    if isPrime:
        summ += x
    if x == 1999999:
        break
    x = x + 2
print(summ)
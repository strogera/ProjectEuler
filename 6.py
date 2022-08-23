x = 1
summ1 = 0
summ2 = 0
while x <= 100:
    summ1 += x**2
    summ2 += x
    x += 1
print((summ2**2) - summ1)

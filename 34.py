from math import factorial

res = []
for x in range(1000000):
    summ = 0
    i = 0
    xStr = str(x)
    while summ <= x and i < len(xStr):
        summ += factorial(int(xStr[i]))
        i += 1
    if i > 1 and i == len(xStr) and summ == x:
        res.append(x)
print(sum(res))
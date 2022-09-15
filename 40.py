from math import prod

start = 1
end = 11
curMaxD = 0
res = {1: -1, 10: -1, 100: -1, 1000: -1, 10000: -1, 100000: -1, 1000000: -1}
while curMaxD <= 1000000:
    num = ''.join([str(x) for x in range(start, end)])
    start += 10
    end += 10
    curMaxD += len(num)
    for d in res:
        if curMaxD > d and res[d] == -1:
            res[d] = int(num[d - curMaxD - 1])
print(prod(res.values()))

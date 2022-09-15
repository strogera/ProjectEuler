coins = [1, 2, 5, 10, 20, 50, 100, 200]

sums = [0, 1] + [0] * 201
for coin in coins:
    for i in range(201):
        if (i + coin < len(sums)):
            sums[i + coin] += sums[i]
print(sums[201])

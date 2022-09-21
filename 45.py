def triangle(n):
    return int(n * (n + 1) / 2)


def pentagonal(n):
    return int((n * (3 * n - 1)) / 2)


def hexagonal(n):
    return int(n * (2 * n - 1))


triangleNums = set()
pentagonalNums = set()
hexagonalNums = set()

for n in range(2, 100000):
    triangleNums.add(triangle(n))
    pentagonalNums.add(pentagonal(n))
    hexagonalNums.add(hexagonal(n))

for num in triangleNums.intersection(pentagonalNums):
    if num != 40755 and num in hexagonalNums:
        print(num)
        exit()
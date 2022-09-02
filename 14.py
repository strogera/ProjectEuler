
chainLengthCache = {}
def chainLength(n: int):
    count = 1
    origN = n
    while n > 1:
        if n in chainLengthCache:
            curLength = count + chainLengthCache[n] - 1
            chainLengthCache[origN] = curLength
            return curLength
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1
    chainLengthCache[origN] = count
    return count


print(max(((chainLength(n), n) for n in range(1, 1000000)))[1])
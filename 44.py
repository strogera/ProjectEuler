pentagonalNumbers = set()


def pentagonalNumber(n):
    pen = (n * (3 * n - 1)) / 2
    return pen


for i in range(1, 10000):
    pentagonalNumbers.add(pentagonalNumber(i))

pentList = list(sorted(pentagonalNumbers))
minDist = 9999999
for k in range(1, len(pentList)):
    for j in range(k + 1, len(pentList)):
        d = abs(pentList[k] - pentList[j])
        if d >= minDist:
            break
        if d in pentagonalNumbers and (pentList[k] +
                                       pentList[j]) in pentagonalNumbers:
            minDist = min(minDist, int(d))
            break
print(minDist)

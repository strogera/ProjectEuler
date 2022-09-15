def sumOfWord(word):
    return sum([ord(c) - ord('A') + 1 for c in word])


def isTrianbleNumber(x):
    n = 1
    tn = lambda n: (n * (n + 1)) / 2
    while tn(n) < x:
        n += 1
    return tn(n) == x


with open("./data/p042_words.txt", "r") as inputFile:
    count = 0
    for word in inputFile.read().split(','):
        if (isTrianbleNumber(sumOfWord(word.replace('"', '')))):
            count += 1
    print(count)
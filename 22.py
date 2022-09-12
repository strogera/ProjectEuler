with open("./data/p022_names.txt", "r") as inputFile:
    nameList = sorted(list(map(lambda k: k[1:-1], inputFile.read().strip().split(','))))
    total = 0
    for i, name in enumerate(nameList):
        total += sum(((ord('A') - ord(c) - 1) * (-1) for c in name)) * (i + 1)
    print(total)
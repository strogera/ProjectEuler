from itertools import permutations

def generatorPandigitalProducts():
    seen = set()
    for l in range(2,6):
        for perm in permutations(range(1, 10), l):
            permStr = ''.join([str(x) for x in list(perm)])
            for i in range(1, len(permStr) - 1):
                a = int(permStr[:i])
                b = int(permStr[i:])
                if (a, b) not in seen:
                    seen.add((a, b))
                    seen.add((b, a))
                    allStr = str(a) + str(b) + str(a*b)
                    if ''.join(sorted(x for x in allStr)) == "123456789" :
                        yield a*b

print(sum(set(x for x in generatorPandigitalProducts())))



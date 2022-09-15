import fractions

productOfFraction = fractions.Fraction(1, 1)
for x in range(10, 100):
    for y in range(10, 100):
        if x == y or x % 10 == 0 or y % 10 == 0:
            continue
        common = set(str(x)).intersection(set(str(y)))
        if len(common) == 1:
            commonDigit = common.pop()
            newFraction = fractions.Fraction(
                int(str(x).replace(commonDigit, '', 1)),
                int(str(y).replace(commonDigit, '', 1)))
            if fractions.Fraction(x, y) == newFraction and newFraction < 1:
                productOfFraction *= newFraction
print(productOfFraction.denominator)
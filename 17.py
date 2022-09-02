numLengthTo9 = {
    0: 0,
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine")
}

numLength10to19 = {
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen")
}

extra10s = [
    0,
    len("ten"),
    len("twenty"),
    len("thirty"),
    len("forty"),
    len("fifty"),
    len("sixty"),
    len("seventy"),
    len("eighty"),
    len("ninety")
]


def sumOfLetters(n: int):
    if n >= 1000:
        return len("onethousand")
    if 1 <= n < 10:
        return numLengthTo9[n]
    if 10 <= n < 20:
        return numLength10to19[n]
    if n < 100:
        return extra10s[n // 10] + numLengthTo9[n % 10]
    if n >= 100:
        return numLengthTo9[int(str(n)[0])] + len("hundred") + (
            len("and") + sumOfLetters(n % 100) if n % 100 != 0 else 0)


summ = sum(numLengthTo9.values()) + sum(numLength10to19.values())
for n in range(20, 1001):
    summ += sumOfLetters(n)
print(summ)
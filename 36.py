def isPalindromic(x: str) -> bool:
    if len(x) == 1:
        return True
    if len(x) == 2:
        return x[0] == x[1]

    if x[0] == x[-1]:
        return isPalindromic(x[1:-1])
    return False

res = []
for x in range(1, 1000000):
    if isPalindromic(str(x)) and isPalindromic(str(bin(x)[2:])):
        res.append(x)
print(sum(res))
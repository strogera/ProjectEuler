cache = {}
def factorial(n):
    if n == 1:
        return 1
    else:
        if n - 1 in cache:
            cache[n] = n * cache[n-1]
            return n * cache[n-1]
        return n * factorial(n-1)

print(sum(int(digit) for digit in str(factorial(100))))

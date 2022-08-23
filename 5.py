x = 2520
while any((x % i != 0 for i in range(20, 1, -1))):
    x += 20
print(x)
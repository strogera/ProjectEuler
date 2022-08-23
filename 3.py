from math import sqrt

num = 600851475143
num2 = num
div = 0
for i in range(3, int(sqrt(num)), 2):
    while (num2 % i == 0):
        num2 = num2 / i
        div = i
print(div)

def canBeWrittenAsPowersOfFifth(n):
    return sum([pow(int(x), 5) for x in str(n)]) == n


nums = []
for x in range(2, 1000000):
    if (canBeWrittenAsPowersOfFifth(x)):
        nums.append(x)

print(sum(nums))

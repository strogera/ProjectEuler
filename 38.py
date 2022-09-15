def isPandigital(nums: list) -> bool:
    return ''.join(sorted(''.join([str(x) for x in nums]))) == "123456789"


maxNum = 0
for x in range(10000):
    nums = []
    numsJoined = ''
    y = 1
    while len(numsJoined) < 9:
        nums.append(x * y)
        numsJoined = ''.join([str(x) for x in nums])
        if isPandigital(nums):
            maxNum = max(maxNum, int(numsJoined))
            break
        y += 1
print(maxNum)
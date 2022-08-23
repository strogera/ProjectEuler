nums = set()
count = 3
while count < 1000:
    if count % 3 == 0 or count % 5 == 0:
        nums.add(count)
    count += 1
print(sum(nums))
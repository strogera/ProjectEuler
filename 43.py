from itertools import permutations

nums = []
primes = [2, 3, 5, 7, 11, 13, 17]
for comb in permutations([x for x in range(10)]):
    if comb[0] == 0:
        continue
    if all(
        (comb[1 + i] * 100 + comb[2 + i] * 10 + comb[3 + i]) % primes[i] == 0
            for i in range(7)):
        nums.append(int(''.join(str(x) for x in comb)))

print(sum(nums))
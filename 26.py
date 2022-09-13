import decimal

def getLengthOfRecurringCycle(decimals: str) -> int:
    maxRecurringCycle = 0
    start = 0
    while start < len(decimals):
        jump = 0
        for end in range(start + 1, len(decimals)):
            if (end + (end - start) < len(decimals)
                    and decimals[start:end] == decimals[end:end + (end - start)]):
                jump = end + (end - start)
                maxRecurringCycle = max(maxRecurringCycle, end - start)
                break
        start += 1 + jump
    return maxRecurringCycle


maxRecurringCycle = (0, 0)
decimal.getcontext().prec = 2000
for x in range(1, 1000):
    fraction = decimal.Decimal(1) / decimal.Decimal(x)
    maxRecurringCycle = max(maxRecurringCycle, (getLengthOfRecurringCycle(
        (fraction.to_eng_string() + '.').split(".")[1]), x))
print(maxRecurringCycle[1])
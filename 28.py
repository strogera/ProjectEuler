def generateGrid(length: int) -> list:
    grid = [[0 for _ in range(length)] for _ in range(length)]
    x = 0
    y = length 
    num = length * length
    yLimit = 0
    xLimit = 0
    while num >= 1:
        y = length - yLimit - 1
        x = xLimit
        while y >= yLimit:
            grid[x][y] = num
            num -= 1
            if num <= 0:
                return grid
            y -= 1
        y = yLimit
        x = xLimit + 1
        while x < length - xLimit:
            grid[x][y] = num
            num -= 1
            if num <= 0:
                return grid
            x += 1
        xLimit += 1
        x = length - xLimit
        y = yLimit + 1
        while y < length - yLimit:
            grid[x][y] = num
            num -= 1
            if num <= 0:
                return grid
            y += 1
        yLimit += 1
        y = length - yLimit
        x -= 1
        while x >= xLimit:
            grid[x][y] = num
            num -= 1
            if num <= 0:
                return grid
            x -= 1

length = 1001
grid = generateGrid(length)
summ = 0
for x in range(length):
    summ += grid[x][x]
    summ += grid[x][length - x - 1]
print(summ - 1) # -1 for double counting 1 which is always the case since it's at the center

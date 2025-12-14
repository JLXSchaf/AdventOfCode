file = open("day4input.txt", "r")
grid = [line.strip() for line in file]

def checkPosition(x,y,grid):

    if (x>=0 and x<len(grid)) and (y>=0 and y<len(grid[0])):
        if grid[x][y] == "@":
            return 1
        return 0
    return 0


def checkAdjucants(x,y,grid):
    found = 0
    found = found + checkPosition(x-1,y-1,grid)
    found = found + checkPosition(x-1,y,grid)
    found = found + checkPosition(x-1,y+1,grid)
    found = found + checkPosition(x+1,y-1,grid)
    found = found + checkPosition(x+1,y,grid)
    found = found + checkPosition(x+1,y+1,grid)
    found = found + checkPosition(x,y-1,grid)
    found = found + checkPosition(x,y+1,grid)
    return found

def searchGrid(grid):
    found = 0
    cacheGrid = grid.copy()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            position = grid[x][y]

            if position == "@" and checkAdjucants(x,y,grid)<4:
                cacheGrid[x] = cacheGrid[x][:y]+"X"+cacheGrid[x][y+1:]
                found += 1
    return cacheGrid, found

part1 = 0
part2 = 0
newGrid = grid.copy()

while True:
    round = 0
    cacheFound = 0
    newGrid, cacheFound = searchGrid(newGrid)
    #newGrid, cacheFound = cacheMethodResults[0], cacheMethodResults[1]
    if cacheFound == 0:
        break
    if round == 0:
        part1 += cacheFound
    part2 += cacheFound
print(part1)
print(part2)

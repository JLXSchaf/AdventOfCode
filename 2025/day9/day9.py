
def getInput():
    #input aufbereiten
    file = open(r"day9\day9input.txt", "r")

    cacheArray = []
    for line in file:
        cache = line.strip()
        redTileposition = cache.split(",")
        cacheArray.append([int(redTileposition[0]), int(redTileposition[1])])
    return cacheArray

def measureRectangle(firstTile, secondTile):

    point1 = abs(firstTile[0]-secondTile[0])+1
    point2 = abs(firstTile[1]-secondTile[1])+1
    return point1 * point2

redTilesPositions = getInput()
allDistances = []
for ind1 in range(len(redTilesPositions)):
    firstTile = redTilesPositions[ind1]
    for ind2 in range(ind1, len(redTilesPositions)):
        secondTile = redTilesPositions[ind2]
        allDistances.append([measureRectangle(firstTile, secondTile), firstTile, secondTile])

allDistances.sort()
[print(i) for i in allDistances]

# 11,-1 - 2,-5......11,-7 - 2,-3
#-0123456789123|0123456789123
#0.............|.............
#1..OOOOOOOOOO.|.............
#2..OOOOOOOOOO.|.............
#3..OOOOOOOOOO.|..OOOOOOOOO..
#4..OOOOOOOOOO.|..OOOOOOOOO..
#5..OOOOOOOOOO.|..OOOOOOOOO..
#6.............|..OOOOOOOOO..
#7.........#.#.|..OOOOOOOOO..
#8.............|..............
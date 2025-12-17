#fix input
file = open("day7\day7input.txt", "r")
map = [line.strip() for line in file]
part2map = [[i for i in line.strip()] for line in map.copy()]
#met hoden
def printBeamsOnMap(map, breakerPositions, beamPositions, ind):
    newMap = map.copy()
    #get Beam positions
    if len(breakerPositions) > 0:

        for breakerPosition in breakerPositions:
            if breakerPosition in beamPositions:
                beamPositions.remove(breakerPosition)
            beamPositions = beamPositions | findBeamPositions(len(map[0]), breakerPosition)

    #change Map
    for beamPosition in beamPositions:
        newMap[ind] = newMap[ind][:beamPosition]+"|"+newMap[ind][beamPosition+1:]

    return newMap, beamPositions

def findBeamPositions(outerBoundary, position):
    boundaries = [0, outerBoundary]
    partBeamPositions = set()
    if position-1 >= boundaries[0]:
        partBeamPositions.add(position-1)
    if position+1 <= boundaries[1]:
        partBeamPositions.add(position+1)
    return partBeamPositions

def OutOfBounds(part2map, position):
    return position[1] < 0 or position[1] >= len(part2map[0])

def LeftOf(position):
    return [position[0], position[1]-1]

def RightOf(position):
    return [position[0], position[1]+1]

def Below(position):
    return [position[0]+1, position[1]]


#variables setup
beamPositions = {map[0].index("S")}
breaker = "^"
part1 = 0
part2 = 0

#prepare Map
for ind in range(1,len(map)):

    if breaker in map[ind]:
        breakerPositions = [i for i in range(len(map[ind])) if breaker in map[ind][i]]
    else:
        breakerPositions = []

    cache = printBeamsOnMap(map, breakerPositions, beamPositions, ind)
    map, beamPositions = cache[0], cache[1]

#part1
for y in range(1,len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "^" and map[y-1][x] == "|":
            part1 += 1

print(part1)
usual = ["^",".","S"]

def fickMeinGehirn(part2map, punkt):
    if OutOfBounds(part2map, punkt):
        return 0

    if punkt[0] == len(part2map)-1:
        part2map[punkt[0]][punkt[1]] = 1
        return 1

    valueAtPunkt = part2map[punkt[0]][punkt[1]]

    #schonmal besucht
    if valueAtPunkt not in usual:
        return valueAtPunkt

    if valueAtPunkt == breaker:
        value = fickMeinGehirn(part2map, LeftOf(punkt)) + fickMeinGehirn(part2map, RightOf(punkt))
    else:
        value = fickMeinGehirn(part2map, Below(punkt))

    part2map[punkt[0]][punkt[1]] = value
    return value

part2 = fickMeinGehirn(part2map, [0, part2map[0].index("S")])
print(part2)


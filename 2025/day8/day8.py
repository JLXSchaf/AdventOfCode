import math

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getPosition(self):
        return self.x, self.y, self.z

    def getX(self):
        return self.x

    def getY(self):
        return self.Y

    def getZ(self):
        return self.Z

def measureDistance(firstBox, secondBox):
    #distance = sqrt((p1-q1)**2+(px-qx)**2....)
    firstBoxCoord = firstBox.getPosition()
    secondBoxCoord = secondBox.getPosition()
    point1 = (firstBoxCoord[0]-secondBoxCoord[0])**2
    point2 = (firstBoxCoord[1]-secondBoxCoord[1])**2
    point3 = (firstBoxCoord[2]-secondBoxCoord[2])**2
    return math.sqrt(point1+point2+point3)

def getAllDistances(CollectionOfJunctionBoxes):
    cacheList = []
    for firstBoxInd in range(len(CollectionOfJunctionBoxes)):
        firstBox = CollectionOfJunctionBoxes[firstBoxInd]
        for secondBoxInd in range(firstBoxInd+1, len(CollectionOfJunctionBoxes)):
            secondBox = CollectionOfJunctionBoxes[secondBoxInd]

            currentDistance = measureDistance(firstBox, secondBox)
            cacheList.append([currentDistance, firstBox, secondBox])
    return cacheList

def findJunctionBoxInCiruits(CollectionOfJunctionBoxes, junctionBox):
    for ind in range(len(CollectionOfJunctionBoxes)):
        if junctionBox in CollectionOfJunctionBoxes[ind]:
            return ind
    return 0

def findIndex(circuits, box):
    for ind in range(len(circuits)):
        if box in circuits[ind]:
            return ind

def addCircuit(circuits, currentShortestConnection):
    firstBox = currentShortestConnection[1]
    firstBoxInd = findIndex(circuits, firstBox)

    secondBox = currentShortestConnection[2]
    secondBoxInd = findIndex(circuits, secondBox)

    if firstBoxInd == secondBoxInd:
        circuits.sort(key = len, reverse=True)
        return circuits


    circuits[firstBoxInd] += circuits[secondBoxInd]
    circuits.pop(secondBoxInd)
    circuits.sort(key = len, reverse = True)

    #part2 only
    if len(circuits) == 1:
        print(firstBox.getX() * secondBox.getX())

    return circuits

def part1Count(circuits):
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

#input aufbereiten
file = open(r"day8\day8input.txt", "r")
CollectionOfJunctionBoxes = []
for line in file:
    cache = line.strip()
    box = cache.split(",")
    CollectionOfJunctionBoxes.append(JunctionBox(int(box[0]),int(box[1]),int(box[2])))

#Variablen Setup
circuits = [[i] for i in CollectionOfJunctionBoxes.copy()]
distances = []
part2bool = True

countOfConnections = 0
limitOfConnections = 1000
while countOfConnections < limitOfConnections:
    currentDistancesOfAllConnections = getAllDistances(CollectionOfJunctionBoxes)
    currentDistancesOfAllConnections.sort(key = lambda x: x[0])

    circuits = addCircuit(circuits, currentDistancesOfAllConnections[countOfConnections])

    countOfConnections += 1

    if len(circuits) == 1:
        break

    if part2bool:
        if countOfConnections == limitOfConnections:
            limitOfConnections = 100000000


print(part1Count(circuits))
#12824*23560
#[print(i[0], i[1].getPosition(), i[2].getPosition()) for i in currentDistancesOfAllConnections]
#[print(i.getPosition()) for i in CollectionOfJunctionBoxes]
#[print([print(x) for x in i]) for i in circuits]

file = open("day5input.txt", "r")
fileCache = [line.strip() for line in file]

def getRightInput(fileCache):
    counter = 0
    freshRangesList = list()
    foodID = list()
    while True:
        if fileCache[counter] == "":
            counter += 1
            break
        freshRangesList.append(fileCache[counter])
        counter+= 1
    while counter < len(fileCache):
        foodID.append(int(fileCache[counter]))
        counter += 1
    return freshRangesList, foodID

def getFreshIDs(freshRangesList):
    freshIDs = list()
    for freshRange in freshRangesList:
        freshRangeBeginning, freshRangeEnding = freshRange.split("-")
        freshIDs.append([int(freshRangeBeginning), int(freshRangeEnding)])
    return freshIDs

freshRangesList, foodIDs = getRightInput(fileCache)
freshIntRangesList = getFreshIDs(freshRangesList)
part1 = 0
part2 = 0
finalFreshRanges = freshIntRangesList.copy()

#part1
for foodId in foodIDs:
    for freshRange in freshIntRangesList:
        if freshRange[0] <= foodId:
            if freshRange[1] >= foodId:
                part1 += 1
                break
print(part1)

def myKeyFunc(e):
    return e[0]
counter=0
#part2
while True:
    newFreshRanges = list()
    finalFreshRanges.sort(key=myKeyFunc)
    finished = True
    for finalFreshRangeInd in range(len(finalFreshRanges)):
        if len(newFreshRanges)==0:
            newFreshRanges.append(finalFreshRanges[finalFreshRangeInd])
            continue
#[23847884851515, 26063777298581]

        changed = False
        currentFreshRange = finalFreshRanges[finalFreshRangeInd]
        for lookingForNewFreshRangesInd in range(len(newFreshRanges)):
            testingFreshRange = newFreshRanges[lookingForNewFreshRangesInd]
            #looking if smaller number is in range        bigger number is in range
            if (testingFreshRange[0] <= currentFreshRange[0] and testingFreshRange[1] >= currentFreshRange[0]) \
            or (testingFreshRange[0] <= currentFreshRange[1] and testingFreshRange[1] >= currentFreshRange[1]):
                changed = True
                finished = False

                #lower smaller number
                if testingFreshRange[0] > currentFreshRange[0]:
                    newFreshRanges[lookingForNewFreshRangesInd][0] = currentFreshRange[0]

                #higher bigger number
                if testingFreshRange[1] < currentFreshRange[1]:
                    newFreshRanges[lookingForNewFreshRangesInd][1] = currentFreshRange[1]


        if not changed:
            newFreshRanges.append(currentFreshRange)
    counter += 1
    finalFreshRanges = newFreshRanges.copy()
    if finished:
        break
print(sum([i[1]+1-i[0] for i in finalFreshRanges]))

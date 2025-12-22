from textwrap import wrap

def polishInput():
    #input aufbereiten
    file = open(r"day10\day10testinput.txt", "r")

    #design
    #ind light dia  button wiring schem  joltage requirements
    #[.#.]          (x,x)(x)               {3}
    # . = off, # = on

    indicatorLights, buttonSchematics, joltageReqs = [],[],[]

    for line in file:
        cache = line.strip().split()
        indicatorLights.append(wrap(cache[0].strip("[]"),1))
        joltageReqs.append(cache[-1].strip("{}").split(","))
        buttonSchematics.append(ArrOfStrArrToIntArr([i.strip("()").split(",") for i in cache[1:-1]]))

    return indicatorLights, buttonSchematics, joltageReqs

def ArrOfStrArrToIntArr(array):
    newArr = []

    for arr in array:
        cache = []
        for str in arr:
            cache.append(int(str))
        newArr.append(cache)
    return newArr

def changeLights(currentLights, buttonCombo):
    lights = [".","#"]
    for ind in buttonCombo:
        currentLights[ind] = lights[(lights.index(currentLights[ind])+1)%2]
    return currentLights
cache = polishInput()
indicatorLights, buttonSchematics, joltageReqs = cache[0], cache[1], cache[2]
#array of chars,  Array of Arrays of Int Arrays, cleaned int array


def recursiveFunction(currentLights, finishedLights, buttonCombos, buttonCombosPressed):

    if currentLights == finishedLights:
        print(currentLights, finishedLights,)
        return 0

    for buttonCombo in buttonCombos:
        if buttonCombo in buttonCombosPressed:
            continue
        buttonCombosPressed.append(buttonCombo)
        currentLights = changeLights(currentLights, buttonCombo)
        return 1 + recursiveFunction(currentLights, finishedLights, buttonCombos, buttonCombosPressed)

    if len(buttonCombosPressed) == len(buttonCombos):
        return 0

part1 = 0
for ind in range(len(indicatorLights)):
    defaultLights = ["." for _ in range(len(indicatorLights[ind]))]
    part1 += recursiveFunction(defaultLights, indicatorLights[ind], buttonSchematics[ind], buttonCombosPressed=[])
    print(part1)

#print(indicatorLights, buttonSchematics, joltageReqs)
print(part1)
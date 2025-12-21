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
        indicatorLights.append(cache[0].strip("[]"))
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

cache = polishInput()
indicatorLights, buttonSchematics, joltageReqs = cache[0], cache[1], cache[2]
#cleaned no br,  Array of Arrays of Int Arrays, cleaned int array
print(indicatorLights, buttonSchematics, joltageReqs)
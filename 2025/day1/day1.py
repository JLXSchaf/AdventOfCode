def rotations(start, direction, movements):
    cache4 = 0
    current = start
    if direction == "R":
        for _ in range(int(movements)):
            current += 1
            if current == 100:
                current = 0
                cache4 += 1
    else:
        for _ in range(int(movements)):
            current -= 1
            if current==0:
                cache4 += 1
            if current == -1:
                current = 99

    return current, cache4

file = open("day1input.txt", "r")
part1 = 0
part2 = 0
numbers = list(range(100))
currPosition = 50

for line in file:
    stripLine = line.strip()
    currDirection, currNumber = stripLine[0], stripLine[1:]

    cache = rotations(currPosition, currDirection, currNumber)
    currPosition, cache1 = cache[0],cache[1]
    if currPosition==0:
        part1 += 1
    part2 += cache1
file.close()

print(part1)
print(part2)



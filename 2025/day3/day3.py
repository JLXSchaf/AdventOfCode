def part2work(currentline):
    currentVoltage = currentline[:12]

    for ind in range(12,len(currentline)):
        testcurrent = currentVoltage+currentline[ind]
        changed = False

        for testind in range(len(testcurrent)-1):
            if testcurrent[testind] < testcurrent[testind+1]:
                currentVoltage = testcurrent[:testind]+testcurrent[testind+1:]
                changed = True
                break

        if changed==False:
            currentVoltage = testcurrent[:12]

    return int(currentVoltage)

file = open("day3input.txt", "r")
part1 = 0
part2 = 0

for line in file:
    testline = line.strip()
    highestVoltage = 0

    intLine = [int(i) for i in testline]
    firstDigit = max(intLine[:-1])
    firstDigitIndex = intLine.index(firstDigit)
    secondDigit = max(intLine[firstDigitIndex+1:])
    part1 += (firstDigit*10+secondDigit)
    part2 += part2work(testline)

print(part1)
print(part2)

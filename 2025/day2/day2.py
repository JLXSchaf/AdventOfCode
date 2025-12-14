file = open("day2input.txt", "r")
ranges = []
part1 = 0
part2 = 0
for line in file:
    ranges = line.strip().split(",")

#prep for usage
for specificRange in ranges:
    startNumber, lastNumber = specificRange.split("-")

    #selection Process begins
    for number in range(int(startNumber),int(lastNumber)+1):
        test = str(number)

        #part1
        if len(test)%2==0 and test.startswith(test[int(len(test)/2):]):
                part1 += number
                part2 += number
                continue

        #part2
        a = b = 0
        for inde in range(1,int(len(test)/2)+1):
            sequence = test[:inde]
            startOfTestSequence = inde
            endOfTestSequence = startOfTestSequence+inde
            #print(testSequence, test)
            counter = 0
            while sequence == test[startOfTestSequence:endOfTestSequence]:
                counter += 1
                if endOfTestSequence == len(test):
                    part2 += number
                    print("FOUND::::::", sequence, test)
                    break

                startOfTestSequence += inde
                endOfTestSequence += inde
print(part1)
print(part2)

class Mathproblem:
    def __init__(self, a, b, c, d, sign):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sign = sign

    def solve1(self):
        #print(self.a,self.b,self.c, self.d, self.sign, "=", eval(self.a+self.sign+self.b+self.sign+self.c+self.sign+self.d))
        return eval(self.a+self.sign+self.b+self.sign+self.c+self.sign+self.d)



    def solve2(self):
                    # D  C   B  A
        newNumbers = ["","","",""]

        for ind in range(4):
            if len(self.a)-1 >= ind:
                newNumbers[ind] = newNumbers[ind] + self.a[-ind-1]
            if len(self.b)-1 >= ind:
                newNumbers[ind] = newNumbers[ind] + self.b[-ind-1]
            if len(self.c)-1 >= ind:
                newNumbers[ind] = newNumbers[ind] + self.c[-ind-1]
            if len(self.d)-1 >= ind:
                newNumbers[ind] = newNumbers[ind] + self.d[-ind-1]

        if newNumbers[2] == "":
            return eval(clear(newNumbers[1])+self.sign+clear(newNumbers[0]))
        if newNumbers[3] == "":
            return eval(clear(newNumbers[2])+self.sign+clear(newNumbers[1])+self.sign+clear(newNumbers[0]))
        return eval(clear(newNumbers[3])+self.sign+clear(newNumbers[2])+self.sign+clear(newNumbers[1])+self.sign+clear(newNumbers[0]))

#clear leading zeros
def clear(number):
    if number=="":
        return number
    return str(int(number))


file = open("day6input.txt", "r")
fileCache = [line.strip().split() for line in file]

mathproblems = []
for ind in range(len(fileCache[0])):
    mathproblems.append(Mathproblem(\
                                    fileCache[0][ind],\
                                    fileCache[1][ind],\
                                    fileCache[2][ind],\
                                    fileCache[3][ind],\
                                    fileCache[4][ind]))

part1 = 0
part2 = 0

for problem in mathproblems:
    part1 += problem.solve1()
    part2 += problem.solve2()

print(part1)
print(part2)

c = -1
file2 = open("day6input.txt", "r")
fileLines = [line for line in file2]
sign = ""
numbers = []
newPart2 = 0

while c < len(fileLines[0])-2:
    c += 1
    #char everyline
    chars = [fileLines[0][c],fileLines[1][c],fileLines[2][c],fileLines[3][c],fileLines[4][c]]
    if chars[4] != " ":
        sign = chars[4]
    if sum([1 if chars[i] != " " else 0 for i in range(len(chars))]) == 0:
        #hier rechnung
        result =  0 if sign == "+" else 1
        for number in numbers:
            result = eval(str(result)+sign+str(number))

        newPart2 += result
        #reset
        numbers = []
        continue

    numbers.append(int(chars[0]+chars[1]+chars[2]+chars[3]))

result =  0 if sign == "+" else 1
for number in numbers:
    result = eval(str(result)+sign+str(number))
newPart2 += result
print(newPart2)
#11532799891761
#11601712780573
# Mein Fehler ist, dass ich dachte die whitespaces sind egal aber das sind sie laut der Lösung nicht

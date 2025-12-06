import re

def part1():
    with open('main.in','r') as file:
        raw = file.read().splitlines()

    dataset = []
    operations = []
    patternStr = "\\b\\d+\\b"
    for i,line in enumerate(raw):
        
        if i != len(raw)-1:
            x = re.findall(patternStr,line)
            dataset.append(x)
        else:
            patternStr = "(?:[+]|[*])+"
            x = re.findall(patternStr,line)
            operations = x
        
    total = 0
    for i,x in enumerate(operations):
        temp = -1
        for j in range(len(dataset)):
            if temp == -1:
                temp = int(dataset[j][i])
            elif x == "*":
                temp *= int(dataset[j][i])
            elif x == "+":
                temp += int(dataset[j][i])
        total += temp
    return total
    



def part2():
    with open('main.in','r') as file:
        raw = file.read().splitlines()

    dataset = []
    operations = []
    patternStr = "\\b\\d+\\b"

    operationLengths = []

    spaces = 0
    index = 0
    for letter in raw[len(raw)-1]:
        if letter == ' ':
            spaces += 1
            continue

        operations.append(letter)
        if (index != 0):
            operationLengths.append(spaces)
            spaces = 0
        
        index += 1
    
    operationLengths.append(spaces+1)




    for i,line in enumerate(raw):
        
        if i != len(raw)-1:
            # x = re.findall(patternStr,line)
            x = []
            # dataset.append(x)
            idx = 0
            for length in operationLengths:
                curBuild = ''
                for i in range(length):
                    if line[idx] == ' ':
                        curBuild += '0'
                    else:
                        curBuild += line[idx]
                    idx += 1
                idx+=1
                x.append(curBuild)
            dataset.append(x)
                
        else:
            patternStr = "(?:[+]|[*])+"
            x = re.findall(patternStr,line)
            operations = x



    mathGroups = []
    total = 0
    for i,x in enumerate(operations):
        temp = []
        for j in range(len(dataset)):
            temp.append(dataset[j][i])
        mathGroups.append(temp)
    


    for i, opList in enumerate(mathGroups):
        maxLen = operationLengths[i]
        temp = 0
        for j in range(maxLen):
            curBuild = ''
            for num in opList:
                if num[j] != "0":
                    curBuild += num[j]

            curBuild = int(curBuild)
            if (temp == 0):
                temp = int(curBuild)
            elif operations[i] == "*":
                temp *= int(curBuild)
            elif operations[i] == "+":
                temp += int(curBuild)
        total += temp
    
    return total



if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())
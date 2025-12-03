import re



with open("2025/inputs/02.txt","r") as f:
    inputStr = f.read().strip().split(',')

def part1():

    def checkInvalid(val:str)->bool:
        if (len(val) % 2 == 1):return False
        firstHalf = val[:len(val)//2]
        secondHalf = val[len(val)//2:]
        if (firstHalf==secondHalf): return True
        return False
    
    total = 0
    for rang in inputStr:
        val1, val2 = rang.split("-")

        for i in range(int(val1),int(val2)+1):
            if checkInvalid(str(i)):
                total += i
    
    return total


def part2():
    def checkInvalid(val:str)-> bool:
        patternStr = ""
        for i,letter in enumerate(val):
            patternStr += letter
            
            x = re.findall(patternStr,val)
            length = len(x)*(i+1)

            if (length == len(val) and len(x) > 1): 
                return True
            if i == (len(val)//2): return False
    
    total = 0
    for rang in inputStr:
        val1, val2 = rang.split("-")

        for i in range(int(val1),int(val2)+1):
            if checkInvalid(str(i)):
                total += i


    return total
    
import re



with open("main.in","r") as f:
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
    
    print(total)


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


    print(total)
    

if __name__ == "__main__":
    print("Part 1 answer: ",end="")
    part1()
    print("Part 2 answer: ",end="")
    part2()
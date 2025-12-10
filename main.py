import re, math
from grid import *
from functools import cache

found:bool = False
def part1():
    global found
    class Machine:
        buttons:tuple[tuple[int]]
        indicatorLength:int
        finalIndicators:list[bool] # true for on, false for off
        currentIndicators:list[bool]
        def __init__(self,finalIndicators,buttons):
            self.buttons = buttons
            self.finalIndicators = finalIndicators
            self.indicatorLength = len(finalIndicators)
            self.currentIndicators = [False for x in range(self.indicatorLength)]
    
    with open('main.in','r') as file:
        raw = file.read().splitlines()

    machines:list[Machine] = []
    
    for line in raw:
        finalPatternRaw = re.findall("\\[([.#]+)\\]",line)[0]
        buttonsRaw = re.findall("\\((\\d(?:,\\d)*)\\)",line)
        finalPattern = [True if x == "#" else False for x in finalPatternRaw]
        buttons = tuple([tuple([int(x) for x in btn.split(',')]) for btn in buttonsRaw])
        machine = Machine(finalPattern,buttons)
        machines.append(machine)

    # this may be  a recursion/dp day

    # start by applying all which will get the last one correct, then shorten the list for each of those and move on to the next


    def doCount(currentIndicators:list[bool],finalIndicator:list[bool],buttons:tuple[tuple[int]],prevButtonIdx=-1):
        global found

        if currentIndicators == finalIndicator:
            found = True
            return 1
    

        if found:
            return 1e15
        
        smallest = 1e15
        for i,button in enumerate(buttons):
            if prevButtonIdx == i:continue
            print(button)
            newIndicators = currentIndicators.copy()
            for x in button: # invert
                newIndicators[x] = False if newIndicators[x] else True

            count = doCount(newIndicators, finalIndicator,buttons,i) + 1
            if count < smallest:
                smallest = count
        count = doCount(currentIndicators, finalIndicator,buttons,i)
        if count < smallest:
            smallest = count
        print("")
        return smallest
    

    total = 0
    for machine in machines: # the idea is here the implenmentation is not
        found = False
        machine = machines[0]
        x = doCount(machine.currentIndicators,machine.finalIndicators,machine.buttons)
        print(x)
        total += x
        break
    
    return total
                
            
        



def part2():

    with open('main.in','r') as file:
        raw = file.read().splitlines()

    
    ...






if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


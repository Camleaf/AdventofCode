import re, math
from grid import *
from functools import cache
from collections import deque

found:bool = False
def part1():
    global found
    class Machine:
        buttons:list[tuple[int]]
        indicatorLength:int
        finalIndicators:list[bool] # true for on, false for off
        currentIndicators:list[bool]
        count:int
        def __init__(self,finalIndicators,buttons,currentIndicators, count=0):
            self.buttons = buttons
            self.finalIndicators = finalIndicators
            self.indicatorLength = len(finalIndicators)
            self.currentIndicators = currentIndicators
            self.count = count
    
    with open('2025/inputs/10.txt','r') as file:
        raw = file.read().splitlines()

    machines:list[Machine] = []
    
    for line in raw:
        finalPatternRaw = re.findall("\\[([.#]+)\\]",line)[0]
        buttonsRaw = re.findall("\\((\\d(?:,\\d)*)\\)",line)
        finalPattern = [True if x == "#" else False for x in finalPatternRaw]
        buttons = list([tuple([int(x) for x in btn.split(',')]) for btn in buttonsRaw])
        machine = Machine(finalPattern,buttons,[False for x in finalPatternRaw])
        machines.append(machine)

    # this may be  a recursion/dp day


    total = 0

    def bfs(startMachine:Machine):

        q = deque([])
        q.append(startMachine)
        
        lowest = 12371928
        while q:
            machine:Machine = q.popleft()

            for i,button in enumerate(machine.buttons):
                newIndic = [x for x in machine.currentIndicators]
                for x  in button:
                    newIndic[x] = False if newIndic[x] else True
                
                if newIndic == machine.finalIndicators:
                    return machine.count + 1
                newButtons = [x for x in machine.buttons]
                newButtons.remove(button)
                newMach = Machine(machine.finalIndicators,newButtons,newIndic,machine.count+1)

                q.append(newMach)
        return lowest
        
    for machine in machines:
        total += bfs(machine)
    return total
                
            
        



def part2():

    with open('2025/inputs/10.txt','r') as file:
        raw = file.read().splitlines()

    
    return "unfinished"






if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


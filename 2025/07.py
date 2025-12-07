import re
from grid import *

def part1():
    with open('main.in','r') as file:
        raw = file.read()
    

    grid = Grid(raw)
    splitters = []
    start = 0
    width = len(grid._grid[0])
    height = len(grid._grid)

    for y,line in enumerate(grid._grid):
        splitters.append([])
        for x,val in enumerate(line):
            if val.val == "S": # shoul dbe one of these
                start = x
            if val.val == "^":
                splitters[y].append(x)
    
    beams = set()
    beams.add(start)
    splitTotal = 0
    for y,splitterLine in enumerate(splitters):

        newBeams = set()
        for beamX in beams:
            if beamX in splitterLine:
                splitTotal += 1
                if (beamX-1 != 0):
                    newBeams.add(beamX-1)
                if (beamX+1 != width):
                    newBeams.add(beamX+1)
                continue
            # if not in line keep going
            newBeams.add(beamX)
        beams = newBeams

    return splitTotal
    
    

    


def part2():
    with open('main.in','r') as file:
        raw = file.read()
    


    grid = Grid(raw)
    splitters = []
    start = 0
    width = len(grid._grid[0])
    height = len(grid._grid)

    for y,line in enumerate(grid._grid):
        splitters.append([])
        for x,val in enumerate(line):
            if val.val == "S": # shoul dbe one of these
                start = x
            if val.val == "^":
                splitters[y].append(x)
    
    def getIdentical(beamQuery,beams):
        newBeams = set()
        thisBeam = [beamQuery[0],beamQuery[1]]

        for beam in beams:
            if beam[0] == beamQuery[0]:
                thisBeam[1]+=beam[1]
            else:
                newBeams.add(beam)
            

        newBeams.add(tuple(x for x in thisBeam))
        return newBeams
                

    beams = set()
    beams.add((start,1)) # x, timelines
    splitTotal = 0
    for y,splitterLine in enumerate(splitters):

        newBeams = set() #i need to check if equal by xpos
        for beam in beams:
            beamX = beam[0]
            timelines = beam[1]
            if beamX in splitterLine:
                splitTotal += 1
                if not (beamX-1 < 0):
                    testBeam = (beamX-1,timelines)
                    newBeams = getIdentical(testBeam,newBeams)

                if (beamX+1 != width):
                    testBeam = (beamX+1, timelines)
                    newBeams = getIdentical(testBeam,newBeams)
                continue
            # if not in line keep going
            testBeam = (beamX, timelines)
            newBeams = getIdentical(testBeam,newBeams)
        beams = newBeams
    total = 0

    for beam in beams:
        total += beam[1]
    return total



if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())
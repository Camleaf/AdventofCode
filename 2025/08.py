import re, math
from grid import *

# This code probably contains some really unecessary data structures
class Junction:
    x:int
    y:int
    z:int
    ID:int
    def __init__(self,x1,y1,z1,ID):
        self.x,self.y,self.z,self.ID = x1,y1,z1,ID
    def __str__(self):
        return f"{self.ID}"
    def __repr(self):
        return f"Junction: {self.ID}"

class Path:
    junkFrom:Junction
    junkTo:Junction
    dist:int
    def __init__(self, junkFrom, junkTo,dist):
        self.junkFrom=junkFrom
        self.junkTo=junkTo
        self.dist=dist

    def __repr__(self):
        return f"{self.dist} | from: {self.junkFrom} to: {self.junkTo}\n"

def part1():
    with open('2025/inputs/08.txt','r') as file:
        raw = file.read().splitlines()
    

    junctions = []
    paths:list[Path] = []
    for i,line in enumerate(raw):
        x,y,z = list(map(int,line.split(',')))
        junk = Junction(x,y,z,i)

        for tempJunk in junctions:
            x1,y1,z1 = junk.x,junk.y,junk.z
            x2,y2,z2 = tempJunk.x, tempJunk.y, tempJunk.z

            dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
            path = Path(junk,tempJunk,dist)

            paths.append(path)

        
        junctions.append(junk)


    circuits = []

    idx = 0
    for path in sorted(paths,key=lambda x: x.dist): #what happens if two circuits become linked

        foundCircuits = []
        for cindex,circuit in enumerate(circuits):
            if path.junkFrom in circuit and path.junkTo in circuit:
                break
            elif path.junkFrom in circuit or path.junkTo in circuit:
                foundCircuits.append(cindex)
                
                
        
        if len(foundCircuits)==0:
            newCirc = set()
            newCirc.add(path.junkFrom)
            newCirc.add(path.junkTo)
            circuits.append(newCirc)
        elif len(foundCircuits) == 1:
            cindex = foundCircuits[0]
            circuits[cindex].add(path.junkFrom)
            circuits[cindex].add(path.junkTo)
        else:
            newCircuits = []
            mergedCircuit = set()
            for j,circuit in enumerate(circuits):
                if j not in foundCircuits:
                    newCircuits.append(circuit)
                    continue
                #otherwise
                for tempJunk in circuit:
                    mergedCircuit.add(tempJunk)
            newCircuits.append(mergedCircuit)
            circuits = newCircuits


        idx+=1
        if idx==1000: #11 for test, 1000 for real
            break
    

    total = 0
    idx = 0
    for circuit in sorted(circuits,key=lambda x: len(x),reverse=True):
        # print(len(circuit))
        if total == 0:
            total = len(circuit)
        else:
            total *= len(circuit)
        idx+=1
        if idx==3:
            break
    return total




    

    


def part2():
    # to solve this, check when circuit[0] == junctions to find last el
    #

    with open('2025/inputs/08.txt','r') as file:
        raw = file.read().splitlines()
    

    junctions:list[Junction] = []
    paths:list[Path] = []
    for i,line in enumerate(raw):
        x,y,z = list(map(int,line.split(',')))
        junk = Junction(x,y,z,i)
        junctions.append(junk)
        for tempJunk in junctions:
            x1,y1,z1 = junk.x,junk.y,junk.z
            x2,y2,z2 = tempJunk.x, tempJunk.y, tempJunk.z

            dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
            path = Path(junk,tempJunk,dist)
            paths.append(path)


    circuits = [set([junk]) for junk in junctions]
    lastOne = None

    for path in sorted(paths,key=lambda x: x.dist): #what happens if two circuits become linked

        foundCircuits = []
        bothIn = False
        for cindex,circuit in enumerate(circuits):
            if path.junkFrom in circuit and path.junkTo in circuit:
                bothIn = True
                break
            elif path.junkFrom in circuit or path.junkTo in circuit:
                foundCircuits.append(cindex)
        if bothIn:
            continue
                
        
        if len(foundCircuits)==0:
            newCirc:set[Junction] = set()
            newCirc.add(path.junkFrom)
            newCirc.add(path.junkTo)
            circuits.append(newCirc)
  
        elif len(foundCircuits) == 1:
            cindex = foundCircuits[0]
            circuits[cindex].add(path.junkFrom)
            circuits[cindex].add(path.junkTo)

        else:
            newCircuits = []
            mergedCircuit = set()
            for j,circuit in enumerate(circuits):
                if j not in foundCircuits:
                    newCircuits.append(circuit)
                    continue
                #otherwise
                for tempJunk in circuit:
                    mergedCircuit.add(tempJunk)
            newCircuits.append(mergedCircuit)
            mergedCircuit.add(path.junkFrom)
            mergedCircuit.add(path.junkTo)
            circuits = newCircuits
        if (len(circuits) == 1):
            lastOne = path
            break
        

    idx = 0
    if lastOne is None: return -1
    return lastOne.junkFrom.x * lastOne.junkTo.x
    



if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


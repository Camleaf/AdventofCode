

def part1():
    with open('main.in','r') as file:
        dataset = file.read().splitlines()
    

    ranges = []
    index = 0 # current way thru dataset
    for line in dataset: # parse ranges. Ranges are inclusive
        index+=1
        if line == '': break
        ranges.append(tuple(map(int,line.split('-'))))
    
    total = 0
    for line in dataset[index:]:
        fresh = False
        for range in ranges:
            if range[0] <= int(line) <= range[1]:
                fresh = True
                break
        if fresh:
            total += 1
    return total


def part2():
    with open('main.in','r') as file:
        dataset = file.read().splitlines()
    

    def inRange(x,iterRange) -> bool:
        if (iterRange[0]<=x<iterRange[1]):
            return True
        return False


    ranges = []
    index = 0 # current way thru dataset
    for line in dataset: # parse ranges. Ranges are inclusive
        index+=1
        if line == '': break
        x = list(map(int,line.split('-')))
        x[1]+=1
        ranges.append(x)

    total = 0
    lrange = tuple((0,0))

    for ran in sorted(ranges,key=lambda r :r[0]):
        
        if inRange(ran[0],lrange):
            if not inRange(ran[1],lrange):
                total += ran[1] - lrange[1]
                lrange = tuple((lrange[0],ran[1]))
        else:
            
            total += ran[1]-ran[0]
            lrange=ran
    

    return total



if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())
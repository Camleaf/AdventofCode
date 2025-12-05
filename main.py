

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


from collections import defaultdict
def part2():
    with open('main.in','r') as file:
        dataset = file.read().splitlines()
    

    ranges = []
    index = 0 # current way thru dataset
    for line in dataset: # parse ranges. Ranges are inclusive
        index+=1
        if line == '': break
        ranges.append(tuple(map(int,line.split('-'))))

    total = 0
    for i,range in enumerate(ranges):
        temptotal = range[1] - range[0]+1 # need to figure out how to union these ranges
        for j,range2 in enumerate(ranges):

            if i <= j: #only checks overlap if the current cehck is after
                continue
            
            if (range[0] >= range2[0] and range[1] <= range2[1]):
                temptotal = 0
                break

            if (range2[0]<=range[0]<=range2[1]<=range[1]):
                temptotal-=(range2[1]-range[0])
                temptotal-=1

            if (range[0]<=range2[0]<=range[1]<=range2[1]):
                temptotal-=(range[1]-range2[0])
                temptotal-=1
            print(range,range2)
            

            
            # cases:
            # r1 r2 e1 e2
            # r2 r1 e2 e1
            # r2 r1 e1 e2
        print(temptotal)
        total += temptotal
    return total



if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())
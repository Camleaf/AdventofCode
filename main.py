

def part1():
    dataset = open("main.in","r").read().split('\n')

    total = 0

    for line in dataset:
        mp = list(map(int,list(line)))
        biggest = max(mp[:len(mp)-1]) # it can't be the last one
        index = mp.index(biggest)
        second_biggest = max(mp[index+1:])
        total += int(str(biggest)+str(second_biggest))
        
    print(total)







def part2():
    dataset = open("main.in","r").read().split('\n')

    total = 0

    for line in dataset:
        mp = list(map(int,list(line)))
        # make an algorithm that does the same thing as above but for 12 numbers
        out = ""
        rang = len(mp)-11
        startDex = 0
        for i in range(12): # it makes a moving window
            biggest = max(mp[startDex:rang])
            startDex = mp[startDex:rang].index(biggest)+1+startDex
            rang += 1
            out += str(biggest)
        total += int(out)

    print(total)


if __name__ == "__main__":
    import time
    startTime = time.time()
    print("Part 1 answer: ",end="")
    part1()
    part1Time = time.time()
    print(f"Part 2 answer: ")
    part2()
    part2Time = time.time()
    print("\n")
    print("Part 1 time:",str(round(1000*(part1Time-startTime),4)) + "ms")
    print("Part 2 time:",str(round(1000*(part2Time-startTime),4)) + "ms")
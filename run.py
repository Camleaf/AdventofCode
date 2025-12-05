



import os, time
from types import ModuleType
import importlib

if __name__ == "__main__":
    day:str = str(input("Enter Day:\n >"))

    if (len(day) == 0 or not day.isnumeric()):
        print("Day not acceptable format")
        exit()

    if not (0<int(day)<=12):
        print("Day not in acceptable range")
        exit()

    if (len(day) == 1):
        day = "0" + day
    

    dayImport:ModuleType = importlib.import_module(f"2025.{day}")

    part1 = getattr(dayImport,"part1")
    part2 = getattr(dayImport,"part2")

    

    print("Part 1 answer: ",end="")
    startTime = time.time()
    p1 = part1()
    part1Time = time.time() - startTime
    print(p1)




    print("Part 1 answer: ",end="")
    startTime = time.time()
    p2 = part2()
    part2Time = time.time()-startTime
    print(p2)


    print("\nPart 1 time:",str(round(1000*(part1Time),4)) + "ms")
    print("Part 2 time:",str(round(1000*(part2Time),4)) + "ms")


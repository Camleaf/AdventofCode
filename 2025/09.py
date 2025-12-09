import re, math
from grid import *


class Point:
    x:int
    y:int
    grouped:int
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.grouped = x + y
        
def part1():
    with open('main.in','r') as file:
        raw = file.read().splitlines()
    
    points:list[Point] = []
    for line in raw:
        x,y = list(map(int,line.split(',')))
        points.append(Point(x,y))

    points = sorted(points,key=lambda x: x.grouped)

    biggest = 0
    for i, point in enumerate(points):
        for j, point2 in enumerate(points[::-1]):
            if point == point2:
                continue
            test = (abs(point2.x-point.x)+1) * (abs(point2.y-point.y)+1)
            if test > biggest:
                biggest = test
    
    return biggest








    

    


def part2():
    with open('main.in','r') as file:
        raw = file.read().splitlines()
    



if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


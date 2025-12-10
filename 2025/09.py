import re, math
from grid import *
from typing import Self
from shapely import LineString, Polygon


class Point:
    x:int
    y:int
    grouped:int
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.grouped = x + y

def part1():
    with open('2025/inputs/09.txt','r') as file:
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

    



class Line:
    start:Point
    end:Point
    vertical:bool

    def __init__(self,start,end):
        self.start = start
        self.end = end
        if start.x == end.x:
            self.vertical = True
        else:
            self.vertical = False
    def getCoord(self):
        return ((self.start.x,self.start.y),(self.end.x,self.end.y))


    def intersects(self,line:Self): #continue this intersection func
        slf = LineString(self.getCoord())
        ln = LineString(line.getCoord())
        return slf.intersects(ln)
            

def part2():

    with open('2025/inputs/09.txt','r') as file:
        raw = file.read().splitlines()

    points:list[Point] = []
    polyPoints = []
    for line in raw:
        x,y = list(map(int,line.split(',')))
        points.append(Point(x,y))
        polyPoints.append((x,y))


    polygon = Polygon(polyPoints)
    points = sorted(points,key=lambda x: x.grouped)
    
    
    biggest = 0
    for i, point in enumerate(points):
        for j, point2 in enumerate(points[::-1]): # i definitely can optimize this, as it likely repeats stuff a lot
            if point == point2:
                continue
            
            rect = Polygon([[point.x,point.y],[point.x,point2.y],[point2.x,point2.y],[point2.x,point.y]])
            
            if polygon.contains(rect):

                test = (abs(point2.x-point.x)+1) * (abs(point2.y-point.y)+1)

                
                if test > biggest:
                    biggest = test
    
    return biggest






if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


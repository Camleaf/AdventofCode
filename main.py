import re, math
from grid import *
from typing import Self



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

    def intersects(self,line:Self): #continue this intersection func
        if line.vertical:
            if self.vertical:
                if self.start.x == line.start.x and (
                    line.start.y < self.start.y < line.end.y
                    or line.start.y < self.end.y < line.end.y
                    or line.end.y > self.end.y > line.start.y
                    or line.start.y > self.start.y > line.end.y
                    ):
                    return True
                else: return False

        else:
            ...
            

def part2():

    with open('main.in','r') as file:
        raw = file.read().splitlines()

    maxX = 0
    maxY = 0
    minX = 1e14
    minY = 1e14
    points:list[Point] = []
    for line in raw:
        x,y = list(map(int,line.split(',')))
        points.append(Point(x,y))
        if x < minX: minX = x
        if x > maxX: maxX = x
        if y < minY: minY = y
        if y > maxY: maxY = y

    # since points not sorted yet it is in shape of polygon
    lines:list[Line] = [] #could split into vert/horiz lines if I need the optimization
    for i in range(len(points)):
        if (i+1 != len(points)):
            lines.append(Line(points[i], points[i+1]))
        else:
            lines.append(Line(points[i], points[0]))

    
    points = sorted(points,key=lambda x: x.grouped)
    

    def pointsInsidePoly(polyLines:list[Line],point:Point,point2:Point):
        points = [point,Point(point.x,point2.y),point2,Point(point2.x,point.y)]
        rectLines = [Line(points[0],points[1]),Line(points[1],points[2]),Line(points[2],points[3]),Line(points[3],points[0])]
        for pt in points:
            testLines = [
                Line(pt,Point(maxX,pt.y)), Line(Point(minX,pt.y),pt),Line(pt,Point(pt.x,maxY)),Line(Point(pt.x,minY),pt)
            ]
            for testLine in testLines:
                for line in polyLines:
                    if testLine.intersects(line):
                        ...



        for direction in CLOCKWISE_DIRS:
            ...
        return True

    biggest = 0
    for i, point in enumerate(points):
        for j, point2 in enumerate(points[::-1]): # i definitely can optimize this, as it likely repeats stuff a lot
            if point == point2:
                continue
            if not (pointsInsidePoly(polygon,point,point2)):
                continue

            test = (abs(point2.x-point.x)+1) * (abs(point2.y-point.y)+1)

            
            if test > biggest:
                biggest = test
    
    return biggest






if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


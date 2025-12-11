import re, math
from grid import *
from collections import deque
from typing import Self


def part1():
    
    with open('2025/inputs/11.txt','r') as file:
        raw = file.read().splitlines()
        
    graph = {}

    for line in raw:
        line = line.split(':')
        start = line[0]
        nodes = line[1].strip().split(" ")
        graph[start] = nodes


    # do bfs
    startNode = "you"
    endNode = "out"

    q = deque([startNode])
    paths = 0
    while q:
        curNode = q.popleft()
        for node in graph[curNode]:
            if node == endNode:
                paths += 1
                continue
            q.append(node)
    return paths
        
cache = {}

def part2():

    with open('2025/inputs/11.txt','r') as file:
        raw = file.read().splitlines()
        
    graph = {}

    for line in raw:
        line = line.split(':')
        start = line[0]
        nodes = line[1].strip().split(" ")
        graph[start] = nodes
        
    startName = "svr"
    endName = "out"
    

    def dfs(curNode:str,foundDac:bool=False,foundFft:bool=False):
        global cache
        if curNode == endName and foundDac and foundFft:
            return 1
        elif curNode == endName: # if not founddac and foundfft
            return 0
        
        if (k:=cache.get(hash((curNode,foundDac,foundFft)),-1)) != -1:
            return k
        
        total = 0
        for nodeName in graph[curNode]:
            tempfoundDac = foundDac
            tempfoundFft = foundFft
            if nodeName == "dac":
                tempfoundDac = True
            if nodeName == "fft":
                tempfoundFft = True

            total += dfs(nodeName,tempfoundDac,tempfoundFft)
        cache[hash((curNode,foundDac,foundFft))] = total
        return total
    
    return dfs(startName) 






if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())


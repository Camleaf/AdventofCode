from grid import *


def part1():

    def check_eight(row:int,col:int,grid:Grid) -> bool:
        
        if (grid.get_node_val(row,col)!="@"):
            return
        check = 0
        for (y,x) in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)):
            if not (0 <= row + y < len(grid._grid) and 0<=col+x<len(grid._grid[0])): continue
            if (grid.get_node_val(row+y,col+x)=="@"):
                check+=1
            if (check >= 4):
                return False
        return True


    with open("main.in","r") as file:
        grid = Grid(file.read())
    
    total = 0

    for i, row in enumerate(grid._grid):
        for j, el in enumerate(row):
            if check_eight(i,j,grid):
                total += 1

    return total


def part2():
    def check_eight(row:int,col:int,grid:Grid) -> bool:
            
        if (grid.get_node_val(row,col)!="@"):
            return
        check = 0
        for (y,x) in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)):
            if not (0 <= row + y < len(grid._grid) and 0<=col+x<len(grid._grid[0])): continue
            if (grid.get_node_val(row+y,col+x)=="@"):
                check+=1
            if (check >= 4):
                return False
        return True
    

    with open("main.in","r") as file:
        grid = Grid(file.read())
        
    

    iterList = [] # for faster iterations over the specific item we want
    for i, row in enumerate(grid._grid):
        for j, el in enumerate(row):
            if grid.get_node_val(i,j) == "@":
                iterList.append((i,j))
    

    total = 0
    picked = 1
    while picked != 0:
        picked = 0
        newIterList = [x for x  in iterList.copy()]
        for (i,j) in iterList:
            if (check_eight(i,j,grid)):
                grid.set_node_val(i,j,".")
                newIterList.remove((i,j))
                picked += 1
                total += 1
        iterList = [x for x in newIterList]
    return total
                


if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())
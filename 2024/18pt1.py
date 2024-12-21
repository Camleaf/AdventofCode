#some bfs should work. Kind of scared for the
#part 2 tho
from grid import Grid, CLOCKWISE_DIRS
from collections import deque
with open("main.in","r") as file:
    raw = file.read().split("\n")
    walls = [list(reversed(list(map(int,x.split(','))))) for x in raw]

width = 71
height = 71
grid_str = '.'*width +'\n'
grid_str *= height
bytes_falling = 1024

grid = Grid(grid_str)
i = 0
nodes = grid.nodes_indicies()
for row,col in walls:
    if i == bytes_falling: break
    grid.set_node_val(row,col,"#")
    i+=1
grid.print()

def is_valid(row,col,grid,visited):
    return grid.get_node_val(row,col) != "#" and not visited.get((row,col),False)

#run bfs
def bfs(grid):
    queue = deque()
    queue.append((0,0,0))
    end_node = (height-1,width-1)
    visited = {
        
    }
    visited[(queue[0][0],queue[0][1])] = True
    end_distance = -1
    
    while queue:
        row,col,dist = queue.popleft()
        
        if (row,col) == end_node:
            end_distance = dist
            break
        
        for vector in CLOCKWISE_DIRS:
            next_dist = dist+1
            next_row = row + vector[0]
            next_col = col + vector[1]
            if not grid.in_bounds(next_row,next_col): continue
            if is_valid(
                next_row,
                next_col,
                grid,visited)and grid.get_node_val(
                    next_row,
                    next_col) != "#":
                visited[(next_row,next_col)] = True
                queue.append((next_row,next_col,next_dist))
    return end_distance
print(bfs(grid))
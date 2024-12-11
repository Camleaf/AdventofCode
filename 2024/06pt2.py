raw = open("Main.in","r").read().split('\n')
grid = [list(line) for line in raw]
from copy import deepcopy

start = []
for i,row in enumerate(grid):
    if "^" in grid[i]:
        start = [i,grid[i].index("^")]
print(start)
directions = {
    0:(-1,0),
    1:(0,1),
    2:(1,0),
    3:(0,-1)
}

def find_wall(grid,coords,directions,cur_dir,new_block):
    global corner_list, positions
    y,x = coords
    vector_y,vector_x = directions[cur_dir]
    while True:
        x += vector_x
        y += vector_y
        if x >= len(grid[0]) or x < 0 or y >= len(grid) or y < 0: return [False]
        if grid[y][x] == "#":
            if [y-vector_y,x-vector_x] not in corner_list[y][x]:
                    corner_list[y][x].append([y-vector_y,x-vector_x])
            else:
                positions += 1
                return [False]
            return [True,[y-vector_y,x-vector_x]]

raw = open("6pt2external.txt","r").read().split('\n')
pos_list = [list(map(int,raw[i].split(' '))) for i in range(len(raw))]
coords = start
positions = 0
for i in range(len(pos_list)):
    corner_list = [[[] for _ in grid[0]] for _ in grid]
    ny,nx = pos_list[i]
    if grid[ny][nx] == "#" or grid[ny][nx] == "^":
        continue
    test_grid = deepcopy(grid)
    test_grid[ny][nx] = "#"
    new_block = [ny,nx]
    cur_dir = 0
    coords = start
    while True:
        raw = find_wall(test_grid,coords,directions,cur_dir,new_block)
        if not raw[0]: break
        coords = [x for x in raw[1]]
        cur_dir += 1
        if cur_dir == 4:
            cur_dir = 0
print(positions)

raw = open("Main.in","r").read().split('\n')
grid = [list(line) for line in raw]
#find ^

start = []
for i,row in enumerate(grid):
    if "^" in grid[i]:
        start = [i,grid[i].index("^")]
        grid[start[0]][start[1]] = "X"
print(start)
directions = {
    0:(-1,0),
    1:(0,1),
    2:(1,0),
    3:(0,-1)
}

###
###
###
cur_dir = 0
x_list = []
def find_wall(grid,coords,directions,cur_dir):
    print(coords)
    global x_list
    y,x = coords
    vector_y,vector_x = directions[cur_dir]
    while True:
        x += vector_x
        y += vector_y
        if x >= len(grid[0]) or x < 0 or y >= len(grid) or y < 0: return [False]
        if grid[y][x] == "#":
            return [True,[y-vector_y,x-vector_x]]
        if [y,x] not in x_list:
            x_list.append([y,x])
            grid[y][x] = "X"

coords = start
while True:
    raw = find_wall(grid,coords,directions,cur_dir)
    if not raw[0]: break
    coords = [x for x in raw[1]]
    cur_dir += 1
    if cur_dir == 4:
        cur_dir = 0
print(len(x_list) + 1) #+1 for starting spot

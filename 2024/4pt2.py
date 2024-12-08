grid = open("Main.in","r").read().split('\n')
gridx = len(grid[0])
gridy = len(grid)

cases = [
    ["MM","SS"],
    ["SS","MM"],
    ["SM","SM"],
    ["MS","MS"]
]

seen_list = []
def explore(grid,x,y,cases)
    case_build = ['','']
    for vector_y,vector_x in ((-1,-1),(-1,1),(1,-1),(1,1)):
        if vector_y + y >= gridy or vector_y + y < 0 or vector_x + x >= gridx or vector_x + x < 0: return False
    case_build[0] += grid[y-1][x-1]
    case_build[0] += grid[y-1][x+1]
    case_build[1] += grid[y+1][x-1]
    case_build[1] += grid[y+1][x+1]
    if case_build in cases:
        return True
    else:
        return False

        
xmas = 0
for y in range(gridy):
    for x in range(gridx):
        letter = grid[y][x]
        if letter != "A": continue
        xmas_found = explore(grid,x,y,cases)
        if xmas_found: xmas += 1
print(xmas)

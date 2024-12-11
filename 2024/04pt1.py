grid = open("Main.in","r").read().split('\n')
string = "MAS"
gridx = len(grid[0])
gridy = len(grid)

seen_list = []
def explore(grid,x,y,vector_x,vector_y,string,seen_list):
    xmas_loc = [y,x]
    for i,letter in enumerate(string):
        j = i+1
        if y+(vector_y*j) >= gridy or y+(vector_y*j) < 0 or x+(vector_x*j) >= gridy or x+(vector_x*j) < 0: return -1
        if grid[y+(vector_y*j)][x+(vector_x*j)] != letter:
            return -1
        xmas_loc.append([y+(vector_y*j),x+(vector_x*j)])
    for loc in seen_list:
        found = 0
        for pos in xmas_loc:
            if pos in loc:
                found += 1
        if found == 4:
            return -1
    return xmas_loc


xmas = 0
for y in range(gridy):
    for x in range(gridx): 
        letter = grid[y][x]
        if letter != "X": continue
        
        #search

        for vector_y,vector_x in ((1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
            if vector_y + y >= gridy or vector_y + y < 0 or vector_x + x >= gridx or vector_x + x < 0:
                continue
            xmas_found = explore(grid,x,y,vector_x,vector_y,string,seen_list)
            if xmas_found == -1:
                continue
            seen_list.append(xmas_found)
            xmas += 1
print(xmas)

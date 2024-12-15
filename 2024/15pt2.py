#same as part one just will need to add a few more cases to my function, and refine input. honestly doesnt seem that bad( famous last words  ik)
#parse input
with open("main.in","r") as file: #ned to acocunt for more lines of instructions
    raw = file.read().split('\n')
    grid = []
    instr = ''
    r = 0
    for i,line in enumerate(raw):
        if len(line)==0: 
            r = 1
            continue
        if r == 0:grid.append([x for x in line])
        else: instr += line

#find robot
robot = [-1,-1]
boxes = []
instr = list(instr)
for i,line in enumerate(grid):
    for j, element in enumerate(line):
        if element == "@":
            robot = [i,j]
        elif element == "O":
            boxes.append([i,j])

#define movement (y,x) reminder up and left is negative
movement = {
    "^": (-1,0),
    ">": (0,1),
    "<": (0,-1),
    "v": (1,0)
}
width = len(grid[0])
height = len(grid)
#recursive check to see if boxes can be moved, and then sends data back up chain to move them
def push(test_y,test_x,vector):
    global boxes, robot
    check = 0
    if test_y >= height-1 or test_y == 0 or test_x == width-1 or test_x == 0 or grid[test_y][test_x]=="#": return False
    elif [test_y,test_x] in boxes:
        check = push(test_y+vector[0],test_x+vector[1],vector)
        if check:
            boxes[boxes.index([test_y,test_x])] = [test_y+vector[0],test_x+vector[1]]
            return True
        else:
            return False
    else:
        return True

#run the push function for each instructions, then move robot
for i,element in enumerate(instr):
    vector = movement[element]
    test_y = vector[0] + robot[0]
    test_x = vector[1] + robot[1]
    if test_y >= height-1 or test_y == 0 or test_x == width-1 or test_x == 0: continue
    check = push(test_y,test_x,vector)
    if check:
        robot = [test_y,test_x]

#find total gps coords

total = 0
for y,x in boxes:
    total += y*100 + x
print(total)


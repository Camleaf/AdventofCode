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
walls = []
empty = []
instr = list(instr)
for i,line in enumerate(grid):
    for j, element in enumerate(line):
        if element == "@":
            robot = [i,j]
        elif element == "O":
            boxes.append([i,j])
        elif element =="#":
            walls.append([i,j])
        elif element == ".":
            empty.append([i,j])

#double everything's sizes
width = len(grid[0]) * 2
height = len(grid)
robot[1] *= 2
left_boxes = []
right_boxes = []
i = 0
for y,x in boxes:
    boxes[i] = [[y,x*2],[y,(x*2)+1]]
    left_boxes.append([y,x*2])
    right_boxes.append([y,(x*2)+1])
    i+=1
tempwalls = []
i = 0
for y,x in walls:
    walls[i] = [y,x*2]
    tempwalls.append([y,(x*2)+1])
    i+=1
walls += tempwalls
tempty = []
i = 0
for y,x in empty:
    empty[i] = [y,x*2]
    tempty.append([y,(x*2)+1])
    i+=1
empty += tempty

#define movement (y,x) reminder up and left is negative
movement = {
    "^": (-1,0),
    ">": (0,1),
    "<": (0,-1),
    "v": (1,0)
}
#recursive check to see if boxes can be moved, and then sends data back up chain to move them
def pushx(test_y,test_x,xvector): #pushes for x_vector
    global boxes, robot,update
    check = 0
    if xvector == 1:
        if [test_y,test_x] in walls: return False
        elif [[test_y,test_x],[test_y,test_x+xvector]] in boxes:
            
            check = pushx(test_y,test_x+(xvector*2),xvector)
            if check:
                update.append(f'update_x_1({xvector},{test_y},{test_x})')
                return True
            else:
                return False
        else:
            return True
    else:
        if [test_y,test_x] in walls: return False
        elif [[test_y,test_x+xvector],[test_y,test_x]] in boxes:
            
            check = pushx(test_y,test_x+(xvector*2),xvector)
            if check:
                update.append(f'update_x_2({xvector},{test_y},{test_x})')
                return True
            else:
                return False
        else:
            return True

def pushy(test_y,test_x,yvector):
    global boxes, robot,update
    if [test_y,test_x] in walls: return False
    elif [test_y,test_x] in empty:
        return True
    elif [test_y,test_x] in left_boxes:
        left = [test_y,test_x]
        right = [test_y,test_x+1]
    elif [test_y,test_x] in right_boxes:
        left = [test_y,test_x-1]
        right = [test_y,test_x]
    print(test_y,test_x)
    check = [pushy(left[0]+yvector,left[1],yvector),pushy(right[0]+yvector,right[1],yvector)]
    print(test_y,test_x)
    print([left,right])
    print(boxes)
    for element in check:
        if not element: return False
    update.append(f'update_y({left},{right},{yvector})')
    return True

#eval functions to delay handling until I know all boxes can move
def update_y(left,right,yvector):
    global boxes, left_boxes,right_boxes,empty
    boxes[boxes.index([left,right])] = [[left[0]+yvector,left[1]],[right[0]+yvector,right[1]]]
    left_boxes[left_boxes.index(left)] = [left[0]+yvector,left[1]]
    right_boxes[right_boxes.index(right)] = [right[0]+yvector,right[1]]
    empty.remove([left[0]+yvector,left[1]])
    empty.remove([right[0]+yvector,right[1]])
    empty.append(left)
    empty.append(right)

def update_x_1(xvector,test_y,test_x):
    global boxes, left_boxes,right_boxes,empty
    boxes[boxes.index([[test_y,test_x],[test_y,test_x+xvector]])] = [[test_y,test_x+xvector],[test_y,test_x+(2*xvector)]]
    right_boxes[right_boxes.index([test_y,test_x+xvector])] = [test_y,test_x+(2*xvector)]
    left_boxes[left_boxes.index([test_y,test_x])] = [test_y,test_x+xvector]
    if [test_y,test_x+(2*xvector)] in empty:
        empty.remove([test_y,test_x+(2*xvector)])
        empty.append([test_y,test_x])
def update_x_2(xvector,test_y,test_x):
    global boxes, left_boxes,right_boxes,empty
    boxes[boxes.index([[test_y,test_x+xvector],[test_y,test_x]])] = [[test_y,test_x+(2*xvector)],[test_y,test_x+xvector]]
    left_boxes[left_boxes.index([test_y,test_x+xvector])] = [test_y,test_x+(2*xvector)]
    right_boxes[right_boxes.index([test_y,test_x])] = [test_y,test_x+xvector]
    if [test_y,test_x+(2*xvector)] in empty:
        empty.remove([test_y,test_x+(2*xvector)])
        empty.append([test_y,test_x])

#run the push function for each instructions, then move robot
print(robot)
for i,element in enumerate(instr): #how do i fix the updating parable
    vector = movement[element]
    test_y = vector[0] + robot[0]
    test_x = vector[1] + robot[1]
    if [test_y,test_x] in walls: continue
    update = []
    if vector[0] == 0:
        check = pushx(test_y,test_x,vector[1]) #fixed x function
        print(check)
        if check:
            for instr in update:
                eval(instr)
            empty.append(robot)
            robot = [test_y,test_x]
            empty.append(robot)
    else:
        if [test_y,test_x] in empty: #so something is missing because my score is 200 too high
            robot = [test_y,test_x]
            continue
        if [test_y,test_x] in left_boxes:
            left = [test_y,test_x]
            right = [test_y,test_x+1]
        elif [test_y,test_x] in right_boxes:
            left = [test_y,test_x-1]
            right = [test_y,test_x]
        print("1")
        check = []
        check.append(pushy(left[0],left[1],vector[0]))
        print("2")
        check.append(pushy(right[0],right[1],vector[0]))
        if all(check):
            for instr in update:
                eval(instr)
            empty.append(robot)
            robot = [test_y,test_x]
            empty.append(robot)
            
#find total gps coords
print(boxes)
total = 0
for box in boxes:
    y = box[0][0]
    x = box[0][1]
    total += y*100 + x
print(total)


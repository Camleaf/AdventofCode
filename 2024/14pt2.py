import re
import math
with open("main.in","r") as file:
    dataset = file.read()
    pattern = 'p\=([-+]?\d{1,3})\,([-+]?\d{1,3}) v\=([-+]?\d{1,3})\,([-+]?\d{1,3})'
    groups = [list(map(int,x)) for x in re.findall(pattern,dataset)]
width = 101  
height = 103
lowest = 10000000000000
lowest_seconds = -1
seconds = 10000
for seconds_passed in range(seconds):
    quadrant = [0,0,0,0]
    for i,group in enumerate(groups):
        posx,posy,vectx,vecty = group
        posx = ((vectx * seconds_passed) + posx) % width + 1 
        posy = ((vecty * seconds_passed) + posy) % height + 1
        if group[1] == math.ceil(height / 2) or group[0] == math.ceil(width/2):
            continue
        posx /= width
        posy /= height
        if posx < 0.5 and posy < 0.5: quadrant[0] += 1
        elif posx < 0.5 and posy > 0.5: quadrant[1] += 1
        elif posx > 0.5 and posy > 0.5: quadrant[2] += 1
        elif posx > 0.5 and posy < 0.5: quadrant[3] += 1
    test_score = quadrant[0]*quadrant[1]*quadrant[2]*quadrant[3]
    if test_score < lowest:
        lowest_seconds = seconds_passed
        lowest = test_score
    #now find where it is in the grid
print(lowest_seconds)
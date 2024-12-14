import re
import math
with open("main.in","r") as file:
    dataset = file.read()
    pattern = 'p\=([-+]?\d{1,3})\,([-+]?\d{1,3}) v\=([-+]?\d{1,3})\,([-+]?\d{1,3})'
    groups = [list(map(int,x)) for x in re.findall(pattern,dataset)]
print(groups)
width = 101  
height = 103

seconds = 100
quadrant = [0,0,0,0]
for i,group in enumerate(groups):
    posx,posy,vectx,vecty = group
    final_posx = (vectx * seconds) + posx
    final_posy = (vecty * seconds) + posy
    final_posx = final_posx % width + 1
    final_posy = final_posy % height + 1
    #now find where it is in the grid
    if final_posy == math.ceil(height / 2) or final_posx == math.ceil(width/2):
        print("Hello")
        continue
    final_posx /= width
    final_posy /= height
    if final_posx < 0.5 and final_posy < 0.5: quadrant[0] += 1
    elif final_posx < 0.5 and final_posy > 0.5: quadrant[1] += 1
    elif final_posx > 0.5 and final_posy > 0.5: quadrant[2] += 1
    elif final_posx > 0.5 and final_posy < 0.5: quadrant[3] += 1
print(quadrant)
print(quadrant[0]*quadrant[1]*quadrant[2]*quadrant[3])
220971520
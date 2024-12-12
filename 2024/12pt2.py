#bfs searh but with more con
from collections import deque
with open("main.in","r") as file:
    dataset = file.read().split('\n')
    dataset = [list(line) for line in dataset]


dist_list = [[False]*len(dataset[0]) for i in range(len(dataset))]

def bfs(dataset,Sy,Sx,cur_type):
  global dist_list
  #define sx,sy, ex, and ey
  Ey=-1
  Ex=-1
  height = len(dataset)
  base = len(dataset[0])
      
  q = deque()

  q.append([Sy,Sx])
  dist_list[Sy][Sx] = True
  cur_ground = []
  cur_ground.append([Sy,Sx])
  perimeter = 0
  while q: #find sides
        curry,currx = q.popleft()
        default_perimeter_add = 4
        for y,x in ((curry+y,currx+n) for y,n in ((-1,0),(1,0),(0,-1),(0,1))):
            if y < 0 or x < 0 or y >= height or x >= base:
                continue
            if not dist_list[y][x] and dataset[y][x] == cur_type:
                dist_list[y][x] = True
                cur_ground.append([y,x])
                q.append([y,x])
            if dataset[y][x] == cur_type: 
                default_perimeter_add -= 1
        perimeter += default_perimeter_add
  return [cur_ground,len(cur_ground)]

def rotate_side_fill(orig_grounds,grounds,sides,rotations):
    #[y-1,x] [y,x-1]
    #[y-1,x-1] [y,x-1]
    
    #[y+1,x] [y,x + 1]
    #[y+1,x+1] [y,x+1]
    
    #[y,x-1] [y+1,x]
    #[y+1,x,-1] [y+1,x]
    
    #[y,x+1] [y-1,x]
    #[y-1,x+1]  [y-1,x]
    for y,x in grounds:
        #do a case test
        #case 1
        if [y-1,x] not in grounds and [y,x-1] not in grounds:
            sides += 1
        elif [y-1,x-1] in grounds and [y,x-1] not in ground:
            sides += 1
        #case2 
        if [y+1,x] not in grounds and [y,x+1] not in grounds:
            sides += 1
        elif [y+1,x+1] in grounds and [y,x+1] not in ground:
            sides += 1
        #case 3
        if [y,x-1] not in grounds and [y+1,x] not in grounds:
            sides += 1
        elif [y+1,x-1] in grounds and [y+1,x] not in ground:
            sides += 1
        #case 4
        if [y,x+1] not in grounds and [y-1,x] not in grounds:
            sides += 1
        elif [y-1,x+1] in grounds and [y-1,x] not in ground:
            sides += 1
    #now rotate stuff
    return sides



price = 0
for i, line in enumerate(dataset):
    for j, element in enumerate(line):
        if dist_list[i][j]: continue
        ground,area = bfs(dataset,i,j,element)
        edges = rotate_side_fill(ground,ground,0,0)
        price += edges * area
print(price)

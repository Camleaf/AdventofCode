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
  while q:
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
  return [perimeter,len(cur_ground)]


price = 0
for i, line in enumerate(dataset):
    for j, element in enumerate(line):
        if dist_list[i][j]: continue
        raw = bfs(dataset,i,j,element)
        price += raw[0] * raw[1]
print(price)

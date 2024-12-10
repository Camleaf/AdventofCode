from collections import deque
dataset = open("main.in","r").read().split("\n")
dataset = [list(map(int,line)) for line in dataset]
def bfs(dataset,Sy,Sx):
  height = len(dataset)
  base = len(dataset[0])
      
  q = deque()

  dist_list = [[-1]*len(dataset[0]) for i in range(len(dataset))]
  q.append([Sy,Sx])
  dist_list[Sy][Sx] = 0
  end_node = 9
  trailhead_endings = 0
  while q:
      curry,currx = q.popleft()
      cur_dist = dist_list[curry][currx]
      for y,x in ((curry+y,currx+n) for y,n in ((-1,0),(1,0),(0,-1),(0,1))):
        if y < 0 or x < 0 or y >= height or x >= base:
          continue
        if dist_list[y][x] == -1 and dataset[y][x] - dataset[curry][currx] == 1:
              if dataset[y][x] == end_node:
                trailhead_endings += 1
              dist_list[y][x] = cur_dist+1
              q.append([y,x])
  return trailhead_endings


starts_list = []
for i, line in enumerate(dataset):
    for j, element in enumerate(line):
        if element == 0:
            starts_list.append([i,j])
 
trailhead_total = 0 
for start in starts_list:
    trailhead_total += bfs(dataset,start[0], start[1])

print(trailhead_total)

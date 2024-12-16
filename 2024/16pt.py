#handle input
import sys
sys.setrecursionlimit(30000000)




with open("main.in","r") as file:
    dataset = file.read().split('\n')
    dataset = [list(x) for x in dataset]

#create adj list for dijkstra's algorithm
#order elements 1 to width*height, right to left.
#will need to make a function which accounts for this
#just make adj list for now, during algorithm will compare 
#length of each turn
#build adj list as we turn



#run recursive alg

start = [len(dataset)-2,1]
#this algorithm bad
lowest_cost_list = [[1e13 for _ in range(len(dataset[0]))]for _ in range(len(dataset))]
width = len(dataset[0])
height = len(dataset)
lowest_end = 1e13
dirs = ((-1,0),(1,0),(0,1),(0,-1))
end = [1,width-2]
best_track = []
# def run_tracker(posy,posx,vector,cost_list,travel_cost):
#     global lowest_cost_list,lowest_end,dirs,end,width,height, best_track
#     cost = int(cost_list[posy-vector[0]][posx-vector[1]] if cost_list[posy-vector[0]][posx-vector[1]] != "||" else 0) + travel_cost
#     if [posy,posx] == end:
#         if cost < lowest_end:
#             lowest_end = cost
#             best_track = cost_list
#             return
#     if dataset[posy][posx] == "#": return
#     if cost_list[posy][posx] != '||' and cost_list[posy][posx] < cost: return
#     cost_list[posy][posx] = cost
#     for new_vector in dirs:
#         if new_vector == vector: continue
#         if not dataset[posy + new_vector[0]][posx + new_vector[1]] == "#":run_tracker(posy+new_vector[0],posx+new_vector[1],new_vector,cost_list,1001)
#     if cost-lowest_cost_list[posy][posx] > 1000: return
#     elif cost-lowest_cost_list[posy][posx] < 0:lowest_cost_list[posy][posx] = cost

#     run_tracker(posy+vector[0],posx+vector[1],vector,cost_list,1)
    # for y,x in ((node[0]+n,node[1]+m) for n,m in ((-1,0),(1,0),(0,1),(0,-1))):
trackers = []
for vector in ((0,-1,1),(-1,0,1001)):
    trackers.append([start[0]+vector[0],start[1]+vector[1],(vector[0],vector[1]),[['||' for _ in range(len(dataset[0]))]for _ in range(len(dataset))],vector[2]])
while trackers:
    tracker = trackers.pop(0)
    posy,posx,vector,cost_list,travel_cost = tracker
    cost = int(cost_list[posy-vector[0]][posx-vector[1]] if cost_list[posy-vector[0]][posx-vector[1]] != "||" else 0) + travel_cost
    if cost > lowest_end:continue
    if [posy,posx] == end:
        if cost< lowest_end:
            lowest_end = cost
            best_track = cost_list
            print(lowest_end)
            continue
    if dataset[posy][posx] == "#":
        continue
    if cost_list[posy][posx] != '||': 
        continue     
    cost_list[posy][posx] = cost
    for new_vector in dirs:
        if new_vector == vector: continue
        if not dataset[posy + new_vector[0]][posx + new_vector[1]] == "#":
            trackers.append([posy+new_vector[0],posx+new_vector[1],new_vector,[[y for y in x] for x in cost_list],1001])
    if cost-lowest_cost_list[posy][posx] > 100:
        continue
    elif cost-lowest_cost_list[posy][posx] < 0:lowest_cost_list[posy][posx] = cost
    trackers.append([posy+vector[0],posx+vector[1],vector,[[y for y in x] for x in cost_list],1])
print(*best_track,sep="\n")
print(lowest_end)

#had to deal with inheritance issues
#tried answers
#75402
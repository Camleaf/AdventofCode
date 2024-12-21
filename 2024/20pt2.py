from grid import Grid, CLOCKWISE_DIRS
from collections import deque
with open("main.in","r") as file:
    raw = file.read()
    grid = Grid(raw)

for row, col in grid.nodes_indicies():
    cur_val = grid.get_node_val(row, col)
    if cur_val == "S":
        start = (row, col)
    elif cur_val == "E":
        end = (row,col)
height = len(grid._grid)
width = len(grid._grid[0])
def is_valid(row,col,grid,cheats,history):
    valid_checks = []
    valid_checks.append(grid.get_node_val(row,col) != "#"or cheats > 0)
    valid_checks.append((row,col) not in history)
    return all(valid_checks)


def find_possible(grid,row,col):
    #assume that row,col is a wall
    #this function will fail as seperated walls exist
    for y,x in grid.nodes_indicies():
        if abs(y-row) + abs(x-col) <= 20: 
            if grid.get_node_val(y,x) == ".":
                yield (y,x)


def bfs(grid,end,starting_arrangement,track_cache):
    queue = deque()
    queue.append(starting_arrangement)
    end_scores = []
    finished_paths = []
    cheat_entries = []
    while queue:
        row,col,dist,cheats,history = queue.popleft()

        if (row,col) == end:
            if history in finished_paths: continue
            end_scores.append(dist)
            finished_paths.append(history)
            continue
        elif cheats == 0:
            if (row,col) in track_cache.keys():
                end_scores.append(dist+track_cache[row,col])
                continue
        for vector in CLOCKWISE_DIRS:
            next_dist = dist+1
            next_row = row + vector[0]
            next_col = col + vector[1]
            new_cheats = cheats
            if not grid.in_bounds(next_row,next_col): continue
            if is_valid(
                next_row,
                next_col,
                grid,cheats,history):
                if grid.get_node_val(next_row,next_col) == "#":
                    if new_cheats == 1:
                        if (next_row,next_col) in cheat_entries: continue
                        cheat_entries.append((next_row,next_col))
                        possible = find_possible(grid,next_row,next_col)
                        for next_row,next_col in possible:
                            queue.append((next_row,next_col,next_dist,new_cheats,[x for x in history] + [(next_row,next_col)]))
                        new_cheats -= 1
                        continue
                queue.append((next_row,next_col,next_dist,new_cheats,[x for x in history] + [(next_row,next_col)]))
    
    return [end_scores,finished_paths]
no_cheat_start = (start[0],start[1],0,0,[(start[0],start[1])])
starting_arrangement = (start[0],start[1],0,1,[(start[0],start[1])])

track_distance_raw = bfs(grid,end,no_cheat_start,{})
track_distance = min(track_distance_raw[0])
track = track_distance_raw[1][track_distance_raw[0].index(min(track_distance_raw[0]))]
track_cache = {

}
for i, coord in enumerate(track):
    track_cache[coord] = track_distance-i
cheat_distances_raw = bfs(grid,end,starting_arrangement,track_cache)
cheat_distances = []
for x in cheat_distances_raw[0]:
    if x >= track_distance: continue
    cheat_length = track_distance - x
    if cheat_length >= 50:
        cheat_distances.append(x)
print(len(cheat_distances))

#can instead use dijkstra and build a distance map with stuff but like later when i have more time
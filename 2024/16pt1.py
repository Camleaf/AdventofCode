from collections import deque

from grid import CLOCKWISE_DIRS,COUNTERCLOCKWISE_DIRS,Grid

with open("main.in","r") as file:
    raw = file.read()
    grid = Grid(raw)
    grid.print()

for row, col in grid.nodes_indicies():
    if grid.get_node_val(row, col) == "S":
        start = (row, col)

dir = 1
lowest = float("inf")

lowest_cost = {}
queue = deque(())
queue.append((start[0],start[1],dir,0))
def is_valid(row,col,grid):
    return grid.get_node_val(row,col) != "#"
while queue:
    cur_y, cur_x, cur_dir, cur_score = queue.popleft()
    lowest_cost[(cur_y, cur_x, cur_dir)] = min(cur_score,lowest_cost.get((cur_y, cur_x, cur_dir), float("inf")))
    if grid.get_node_val(cur_y,cur_x) == "E":
        lowest = min(lowest,cur_score)
    
    y_straight = cur_y + CLOCKWISE_DIRS[cur_dir][0]
    x_straight = cur_x + CLOCKWISE_DIRS[cur_dir][1]
    next_score_straight = cur_score + 1
    if is_valid(y_straight,x_straight,grid) and next_score_straight < lowest_cost.get((y_straight, x_straight, cur_dir), float("inf")):
        lowest_cost[(y_straight, x_straight, cur_dir)] = next_score_straight
        queue.append((y_straight, x_straight, cur_dir, next_score_straight))

    for turn_indicator in ((cur_dir +1) % 4,(cur_dir -1) % 4):
        y_turn = cur_y + CLOCKWISE_DIRS[turn_indicator][0]
        x_turn = cur_x + CLOCKWISE_DIRS[turn_indicator][1]
        next_score_turn = cur_score + 1001
        if is_valid(y_turn,x_turn,grid) and next_score_turn < lowest_cost.get((y_turn,x_turn, turn_indicator), float("inf")):
            lowest_cost[(y_turn,x_turn, turn_indicator)] = next_score_turn
            queue.append((y_turn,x_turn, turn_indicator, next_score_turn))
print(lowest)
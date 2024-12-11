grid = open("Main.in","r").read().split('\n')
grid = [list(line)for line in grid]
node_types = {

}
orig_types = {

}
elements = []
for y, line in enumerate(grid):
    for x,element in enumerate(line):
        if element == ".": continue
        if element not in node_types:
            node_types[element] = []
            orig_types[element] = []
            elements.append(element)
        node_types[element].append([y,x])
        orig_types[element].append([y,x])
antinodes = []
for i,element in enumerate(elements):
    if len(orig_types[element]) == 1: continue
    length = len(node_types[element])
    for j in range(length):
        cur_node = node_types[element].pop(0)
        for k in range(len(node_types[element])):
            anti_tests = []
            cur_y,cur_x = cur_node
            test_y,test_x = node_types[element][k]
            d_v= [cur_y-test_y,cur_x-test_x]
            offset = [0,0]
            while [cur_y + offset[0],cur_x + offset[1]] == [test_y,test_x] or [cur_y + offset[0],cur_x + offset[1]] == [cur_y,cur_x]:
                offset[0] += d_v[0]
                offset[1] += d_v[1]
            anti_tests.append([cur_y + offset[0],cur_x + offset[1]])
            offset = [0,0]
            while [cur_y - offset[0],cur_x - offset[1]] == [test_y,test_x] or [cur_y - offset[0],cur_x - offset[1]] == [cur_y,cur_x]:
                offset[0] += d_v[0]
                offset[1] += d_v[1]
            anti_tests.append([cur_y - offset[0],cur_x - offset[1]])
            for test in anti_tests:
                if test in antinodes: continue
                if test[0] < 0 or test[0] >= len(grid) or test[1] < 0 or test[1] >= len(grid[0]): continue
                antinodes.append(test)
                grid[test[0]][test[1]] = "#"
                    

print(len(antinodes))

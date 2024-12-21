#maybe just bfs solve
#make a dict of how patterns branch out then use that as adj
#store substrings based on the next letter they could 
#possibly have
from collections import deque
with open("main.in","r") as file:
    raw = file.read().split('\n')
    towels = raw[0].split(', ')
    designs = raw[2:]
print(len(designs))


total = 0
for i, design in enumerate(designs):
    #do a lot of bfs i guess
    print(i)
    tried_designs = []
    queue = deque()
    for new_towel in towels:
        queue.append(('',new_towel))
    while queue:
        test_design, towel = queue.popleft()
        new_design = test_design + towel
        if len(new_design) > len(design): continue
        # print(new_design,''.join(design[:len(new_design)]))
        if new_design != ''.join(design[:len(new_design)]):
            continue
        if new_design in tried_designs: continue
        tried_designs.append(new_design)
        if new_design == design: 
            total+=1
            break
            
        for new_towel in towels:
            queue.append((new_design,new_towel))
print(total)  
    #(test_design, cur_towel)
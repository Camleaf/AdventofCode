#maybe just bfs solve
#make a dict of how patterns branch out then use that as adj
#store substrings based on the next letter they could 
#possibly have
from functools import cache
from collections import deque
with open("main.in","r") as file:
    raw = file.read().split('\n')
    towels = set(raw[0].split(', '))
    designs = raw[2:]
print(len(designs))

@cache
def is_valid(pattern):    
    if not pattern:
        return 1
    
    count = 0
    for i in range(1, len(pattern) + 1):
        prefix = pattern[0:i]
        suffix = pattern[i:]
        
        if prefix in towels:
            count += is_valid(suffix)       
    
    return count

count = 0
for design in designs:
    count += is_valid(design)
print(count)
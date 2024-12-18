#unfinihsed
import re
import math
from collections import deque
with open('main.in','r') as file:
    raw = file.read().split('\n')
    program_raw = raw[-1]
    raw = ''.join(raw)
    pattern = 'Register A: (\d{1,20})Register B: (\d{1,20})Register C: (\d{1,20})'
    registers_raw = [int(x) for x in re.findall(pattern,raw)[0]]
    program_raw = list(program_raw[9:])
    PROGRAM = [int(program_raw[i*2]) for i in range(len(program_raw)//2+1)]

reg_a = registers_raw[0]
reg_b = registers_raw[1]
reg_c = registers_raw[2]
def part_1(reg_a,reg_b,reg_c,PROGRAM):
    out = []
    instruction_pointer = 0
    while instruction_pointer < len(PROGRAM):
        opcode = PROGRAM[instruction_pointer]
        combo = PROGRAM[instruction_pointer+1]
        instruction_pointer += 2
        literal = combo
        match combo:
            case 4: combo = reg_a
            case 5: combo = reg_b
            case 6: combo = reg_c
        match opcode:
            case 0: reg_a = reg_a>>combo
            case 1: reg_b = reg_b^literal
            case 2: reg_b = combo%8
            case 3: instruction_pointer = literal if reg_a != 0 else instruction_pointer
            case 4: reg_b = reg_b^reg_c 
            case 5: out.append(combo%8)
            case 6: reg_b = reg_a>>combo
            case 7: reg_c = reg_a>>combo
    return out

part_1(reg_a,reg_b,reg_c,PROGRAM)
#part 2
#do some kind of cursed bfs. during testing it looks like bsf left 3 works to get a rough estimate of the area of the next element in the key
queue = deque()
queue.append([len(PROGRAM),3])
length = len(PROGRAM)
end_queue = ()
while queue:
    i, num = queue.popleft()
    if i < 0: continue
    for j in range(8):
        new_num = (num << 3) + j
        new_program = part_1(new_num,0,0,PROGRAM)
        check_program = PROGRAM[i:]
        if new_program == check_program:
            if i == 0:
                end_queue.append(num)
            queue.append((i-1,num))
print(min(end_queue))
import re
import math
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
output = ",".join(map(str, out))
print(output)


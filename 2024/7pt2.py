from itertools import product
dataset = open("Main.in","r").read().split('\n')

total = 0
incr = {
    0:"*",
    1:"+",
    2:"||"
}
for i,line in enumerate(dataset):
    left_side, right_side = line.split(': ')
    left_side = int(left_side)
    right_side = [int(x) for x in right_side.split(' ')]
    #make like binary increment
    length = len(right_side)-1
    lists = []
    lists = list(product([0,1,2], repeat=length))

    for j, listed in enumerate(lists):
        cur = 0
        for i,num in enumerate(listed):
            operation = incr[num]
            if i == 0:
                if operation == "*":
                    cur += right_side[i] * right_side[i+1]
                elif operation == "||":
                    cur += int(str(right_side[i])+str(right_side[i+1]))
                else:
                    cur += right_side[i] + right_side[i+1]
            else:
                if operation == "*":
                    cur *= right_side[i+1]
                elif operation == "||":
                    cur = int(str(cur)+str(right_side[i+1]))
                else:
                    cur += right_side[i+1]
        if cur == left_side:
            total += left_side
            break
print(total)

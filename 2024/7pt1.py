import itertools
dataset = open("Main.in","r").read().split('\n')

total = 0
incr = {
    0:"*",
    1:"+"
}
for i,line in enumerate(dataset):
    left_side, right_side = line.split(': ')
    left_side = int(left_side)
    right_side = [int(x) for x in right_side.split(' ')]
    #make like binary increment
    length = len(right_side)-1
    lists = []
    for i in range(0, 2**length):
        lists.append([*map(int, '{:0{n}b}'.format(i, n=length))])
    for j, list in enumerate(lists):
        cur = 0
        for i,num in enumerate(list):
            operation = incr[num]
            if i == 0:
                if operation == "*":
                    cur += right_side[i] * right_side[i+1]
                else:
                    cur += right_side[i] + right_side[i+1]
            else:
                if operation == "*":
                    cur *= right_side[i+1]
                else:
                    cur += right_side[i+1]
        if cur == left_side:
            total += left_side
            break
print(total)

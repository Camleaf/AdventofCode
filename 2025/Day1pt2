# Open files
dataset = open("main.in","r").read().split('\n')

point = 50
total = 0
for line in dataset:
    dir = line[0]
    num = int(line[1:])
    if (num > 99):
        total += num//100

    num %= 100

    prevPoint = point

    if dir == "R":
        if (point + num >= 100): total += 1
        point += num
        point %= 100
        

    else:
        x = False
        if (point - num <= 0 and point != 0): 
            x = True
            total += 1
        point -= num
        if point < 0:
            point = 100 + point


print(total)
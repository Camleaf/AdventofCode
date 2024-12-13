import re
import numbers
with open("main.in","r") as file:
    dataset = file.read()
    pattern = 'Button A: X\+(\d\d)\, Y\+(\d\d)\nButton B: X\+(\d\d)\, Y\+(\d\d)\nPrize: X\=(\d{3,20})\, Y\=(\d{3,20})'
    
    groups = re.findall(pattern,dataset)
price = 0
for group in groups:
    ax,ay,bx,by,tx,ty = list(map(int,group))
    cur_x,cur_y = 0,0
    r = 0
    for i in range(1,101):
        cur_x += ax
        cur_y += ay
        if (tx-cur_x) // bx == (ty-cur_y) // by:
            test = (tx-cur_x) /bx + (ty-cur_y)/by
            if not test.is_integer():
                continue
            r = (tx-cur_x)//bx
            break
    if r != 0:
        price += r + i*3

print(price)
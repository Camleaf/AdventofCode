import re
import math
with open("main.in","r") as file:
    dataset = file.read()
    pattern = 'Button A: X\+(\d\d)\, Y\+(\d\d)\nButton B: X\+(\d\d)\, Y\+(\d\d)\nPrize: X\=(\d{3,20})\, Y\=(\d{3,20})'
    groups = re.findall(pattern,dataset)
#use like a div feature
price = 0
for group in groups:
    a,c,b,d,e,f = list(map(int,group))
    e += 10000000000000
    f += 10000000000000
    #find a way to run this and divide it
    #cramer's law. Sadly first one i had to use the internet for for ideas
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    a = x
    b = y
    r = a*3+b
    if not r.is_integer():
        continue
    price += r

print(int(price))
# ax + bx = tx
# ay + by = ty

# aA + bB = e
# cA + dB = f
#
#(xval1)A + (xval2)B = Tx
#(yval1)A + (yval2)B = Ty
#
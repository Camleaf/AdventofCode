raw = open("main.txt","r").readline()
numbers = "0123456789"
cur_progress = 0
progress = "mul("
cur_num = []
numbers_found = False
num1 = 0
num2 = 0
comma_found = False
final = 0
for letter in raw:
    if cur_progress < 4:
        needed = progress[cur_progress]
        if letter == needed:
            cur_progress+=1
        else:
            cur_progress = 0
    else:
        if letter in numbers:
            cur_num.append(letter)
            numbers_found = True
            continue
        elif letter == ",":
            if numbers_found == True and comma_found == False:
                num1 = int(''.join(cur_num))
                cur_num = []
                comma_found = True
                numbers_found = False
                continue
        elif letter == ")":
            if comma_found == True and numbers_found == True:
                num2 = int(''.join(cur_num))
                final += num1*num2
                num1=0
                num2=0
                cur_progress=0
                comma_found = False
                numbers_found = False
                cur_num = []
                continue
        else:
            num1=0
            num2=0
            cur_progress=0
            comma_found = False
            numbers_found = False
            cur_num = []
            continue
print(final)

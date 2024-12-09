data = list(map(int,list(open("main.in","r").read())))
file_spaces = []
file_id = 0
for i, size in enumerate(data):
    if i % 2 == 0: #remake this to create blocks where 10 is still one block
     for i in range(size):
        file_spaces.append(str(file_id))
     file_id += 1
    else:
        for i in range(size):
            file_spaces.append(".")
space_list = []
for i,element in enumerate(file_spaces): 
    if element == ".": space_list.append(i)
space_list = sorted(space_list)
test_file_spaces = list(reversed([x for x in file_spaces]))
print(''.join(file_spaces))
for i,element in enumerate(test_file_spaces):
    if element == ".": continue
    if len(space_list) == 0: break
    if space_list[0] > len(file_spaces)-i-1:
        break
    file_spaces[len(file_spaces)-i-1] = "."
    file_spaces[space_list.pop(0)] = element
checksum = 0
for i, element in enumerate(list(file_spaces)):
    if element == ".": 
        continue
    checksum += i*int(element)
print(checksum)

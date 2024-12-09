data = list(map(int,list(open("main.in","r").read())))
file_groups = {}
empty_groups = {}
file_id = 0
adjust = 0


for i, size in enumerate(data):
    if size == 0: 
        adjust += 1
        continue
    if i % 2 == 0:
     file_groups[file_id] = [i-adjust,size]
     file_id += 1
    else:
        if size not in empty_groups.keys():
            empty_groups[size] = []
        empty_groups[size].append(i-adjust)

for element in list(reversed(file_groups.keys())):
    #search for suitable candidate
    location = file_groups[element][0]
    size = file_groups[element][1]
    leftmost,leftsize = len(file_groups.keys()) * 2 + 1,0

    for empty_size in empty_groups.keys():
        if empty_size < size: continue
        for empty_loc in empty_groups[empty_size]:
            if empty_loc < leftmost and empty_loc < location:
                leftmost = empty_loc
                leftsize = empty_size
    if leftsize == 0:
        continue
    file_groups[element][0] = leftmost
    remainder = leftsize - size
    empty_groups[leftsize].remove(leftmost)


    #edge cases
    #check case 1: more empty to either side of new rightmost empty
        
    new_loc_list = []
    loc_adjust = 0
    use_function = False
    for empty_size in empty_groups.keys():
        if location + 1 in empty_groups[empty_size]:
            empty_groups[empty_size].remove(location+1) #this test input contains a failure on this function, when element 5 moves
            new_loc_list.append(empty_size)
            use_function = True
        if location - 1 in empty_groups[empty_size]:
            empty_groups[empty_size].remove(location-1)
            new_loc_list.append(empty_size)
            loc_adjust += 1
            use_function = True
        if len(new_loc_list) == 2: break
    
    new_size = sum(new_loc_list) + size
    new_location = location - loc_adjust

    if size not in empty_groups.keys():
        empty_groups[size] = []
    
    if new_size not in empty_groups.keys():
        empty_groups[new_size] = []
    
    if loc_adjust == 0 and use_function is False:
        empty_groups[size].append(location)
    else:
        empty_groups[new_size].append(new_location+1)

    if remainder == 0: pass 
    else:
        #check case 2: more empty to right of leftmost new empty
        #only check if remainder isn't zero
        for element in file_groups.keys(): #id expansion for files. Add right location adjust
            if file_groups[element][0] > leftmost:
                file_groups[element][0] += 1
            if file_groups[element][0] > location - loc_adjust:
                file_groups[element][0] -= len(new_loc_list)
        
        if remainder not in empty_groups.keys():
            empty_groups[remainder] = []
        
        applied = 0 
        for empty_size in empty_groups.keys(): 
            if leftmost+1 in empty_groups[empty_size]:
                empty_groups[empty_size].remove(leftmost+1)
                if empty_size + remainder not in empty_groups.keys():  #this not running sometimes can cause issues
                    empty_groups[empty_size + remainder] = []
                empty_groups[empty_size + remainder].append(leftmost+1)
                applied = 1
                break
        
        if applied == 0:
            empty_groups[remainder].append(leftmost+1)
            for empty_size in empty_groups.keys(): #id expansion for empties
                for i in range(len(empty_groups[empty_size])):
                    if empty_groups[empty_size][i] > leftmost+1:
                        empty_groups[empty_size][i] += 1
                    if empty_groups[empty_size][i] > location - loc_adjust:
                        empty_groups[empty_size][i] -= len(new_loc_list)


#put string back together

#make list of unordered files
unordered_files = []
for element in file_groups.keys():
    unordered_files.append([str(element),file_groups[element][0],file_groups[element][1]])

#make list of unordered empties
unordered_empties = []
for empty_size in empty_groups.keys():
    for id_addr in empty_groups[empty_size]:
        unordered_empties.append(['.',id_addr,empty_size])

#join them and order them with lambda sort
ordered_files_empties = sorted(unordered_files + unordered_empties,key=lambda x: x[1])

#lay out each element, instead of grouping them

ordered_list = []
for i, element in enumerate(ordered_files_empties):
    for j in range(element[2]):
        ordered_list.append(element[0])

checksum, count = 0,0
for i,element in enumerate(ordered_list):
    if element == ".":
        count += 1
        continue
    checksum += int(element)*count
    count+=1
    
print(checksum)

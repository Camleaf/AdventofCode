raw = open("Main.in","r").read().split('\n')
dataset = [list(map(int,raw[i].split('   '))) for i in range(len(raw))]
left_list,right_list = [dataset[i][0] for i in range(len(dataset))],sorted([dataset[i][1] for i in range(len(dataset))])

similarity = 0
compute_index = {}
for check_num in left_list:
    if check_num not in compute_index.keys():
        compute_index[check_num] = 0
        compute = 0
        for test in right_list:
            if test > check_num:
                break
            if test == check_num:
                compute += 1
        compute *= check_num
        compute_index[check_num] = compute
        similarity += compute
    else:
        similarity += compute_index[check_num]
print(similarity)

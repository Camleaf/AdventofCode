raw = open("Main.in","r").read().split('\n')
dataset = [list(map(int,raw[i].split('   '))) for i in range(len(raw))]
left_list,right_list = sorted([dataset[i][0] for i in range(len(dataset))]),sorted([dataset[i][1] for i in range(len(dataset))])

dist = 0

for i in range(len(left_list)):
    dist += abs(left_list[i]-right_list[i])
print(dist)

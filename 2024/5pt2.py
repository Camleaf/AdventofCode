raw = open("main.txt").read().split("\n")
ordering_list = []
layer_list = []
for line in raw:
    if "|" in line:
        ordering_list.append(line)
    else:
        if line != '':
            layer_list.append(line)

order_dict = {} #element: elements that are after it it
for i,order in enumerate(ordering_list):
    after,before = list(map(int,order.split('|')))
    if before not in order_dict:
        order_dict[before] = []
    if after not in order_dict:
        order_dict[after] = []
    order_dict[after].append(before)

inaccurate = []
for i, line in enumerate(layer_list):
    accurate = True
    elements = list(map(int,line.split(',')))
    orig = [x for x in elements]
    length = len(elements)
    for j in range(len(elements)):
        cur_element = elements.pop(0)
        for test in elements:
            if test in order_dict[cur_element]:
                continue
            else:
                accurate = False
    if accurate == False:
        inaccurate.append(orig)

total = 0
for i, elements in enumerate(inaccurate):
    orig = [x for x in elements]
    for i, element in enumerate(orig):
        r = 0
        for j, test in enumerate(elements):
            if test == element:
                continue
            if test in order_dict[element]:
                elements.remove(element)
                elements.insert(elements.index(test),element)
                r = 1
                break
        if r == 0:
            elements.remove(element)
            elements.insert(len(elements),element)
    length = len(elements)//2
    total += elements[length]
print(total)

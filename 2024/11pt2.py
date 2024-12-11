stones = list(map(int,open("main.in","r").read().split(' ')))

dcache = {}
cache = {}


for i in range(75):
    cache[i] = []
    dcache[i] = []


def recursivesolve(cur_stone,i):
    global cache
    if cur_stone in cache[i]:
        return dcache[i][cache[i].index(cur_stone)]
    new_stones = []
    total = 0
    if cur_stone == 0:
        new_stones.append(1)
    elif len(str(cur_stone)) % 2 == 0:
        l = len(str(cur_stone))
        cur_stone = list(str(cur_stone))
        stone_str = ''.join(cur_stone[:l//2])
        new_stones.append(int(stone_str))
        stone_str = ''.join(cur_stone[l//2:])
        new_stones.append(int(stone_str))
    else:
        stone = cur_stone * 2024
        new_stones.append(stone)
    if i == 74:
        return len(new_stones)
    for stone in new_stones:
        x = recursivesolve(stone,i+1)
        cache[i+1].append(stone)
        dcache[i+1].append(x)
        total += x
    return total

total = 0
for stone in stones:
    total += recursivesolve(stone,0)
print(total)hain in advance, then compute the length of the chains

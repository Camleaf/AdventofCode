stones = list(map(int,open("main.in","r").read().split(' ')))

for i in range(25):
    new_stones = []
    for j, cur_stone in enumerate(stones):
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
    stones = new_stones
print(len(stones))

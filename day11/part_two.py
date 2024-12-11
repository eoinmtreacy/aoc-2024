from typing import List

with open('day11.input', 'r') as file:
    input = [line.split() for line in file][0]

def transform(stone: str) -> List[str]:
    stones = []
    if stone == '0':
        stones.append('1')
    elif len(stone) % 2 == 0:
        left = str(int(stone) // 10 ** (len(stone) // 2))
        right = str(int(stone) % 10 ** (len(stone) // 2))
        stones.append(left)
        stones.append(right)
    else:
        stones.append(str(int(stone) * 2024))
    
    return stones

def dfs(stone, depth = 0, cache = dict()):
    if depth > 74:
        return 1
    if cache.get(stone) == None:
        cache[stone] = {}
    if cache.get(stone).get(depth) == None:
        result = sum([dfs(s, depth + 1, cache) for s in transform(stone)]) 
        cache[stone][depth] = result
    return cache.get(stone).get(depth)

print(sum([dfs(stone) for stone in input]))
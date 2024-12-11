from typing import List

with open('day11.sample', 'r') as file:
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

def dfs(stones: str, count: int) -> List[str]:
    global cache
    if count > 24:
        return stones
    else:
        result = []
        for stone in stones:
            inter = transform(stone)
            result += dfs(inter, count + 1)

        return result

result = []
cache: dict = {}

for i in input:
    result += dfs([i], 0)

print(len(result))




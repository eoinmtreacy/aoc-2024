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

result = []
cache: dict = {}

for i in input:
    print("working on stone", i)
    stones = []
    stones.append(i)
    for _ in range(75):
        intermediate = []
        for stone in stones:
            intermediate += transform(stone)
        stones = intermediate
    result += stones


print(len(result))



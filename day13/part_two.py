import re
from typing import List

with open('day13.sample', 'r') as file:
    input = [re.findall("[0-9]+", str(line)) for line in file]

def dot(m1: List[List[float]], m2: List[float]) -> List[float]:
    result = []
    for row in m1:
        inter = 0
        for i in range(len(row)):
            inter += row[i] * m2[i]     
        result.append(inter)
    return result

result = 0

i = 0
while i < len(input):

    if not input[i]:
        i += 1
        continue

    v1 = [int(char) for char in input[i]]
    i += 1
    v2 = [int(char) for char in input[i]]
    i += 1
    C = [int(char) for char in input[i]]
    i += 1

    M = [v1, v2] # vector 

    inverse_m = [ [(1 / (v1[0] * v2[1] - v1[1] * v2[0])) * c for c in v] for v in [[v2[1], -v1[1]], [-v2[0], v1[0]]]]
    print(dot(inverse_m, C))
    countA, countB = dot(inverse_m, C)
    print(countA, countB)

    break


print(result)

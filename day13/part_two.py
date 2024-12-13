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
        result.append(int(inter))
    return result

def gcd(a: int, b: int) -> int | None:
    n = 1
    while min(a,b) / n > 1:
        if max(a,b) % (min(a,b) / n) == 0:
            return  int(min(a, b) / n)
        n += 1
    return 1


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

    if C[0] % gcd(v1[0], v2[0]) != 0 or C[1] % gcd(v1[1], v2[1]) != 0:
        continue
    
    print("something")
    M = [v1, v2] # vector 

    inverse_m = [ [(1 / (v1[0] * v2[1] - v1[1] * v2[0])) * c for c in v] for v in [[v2[1], -v1[1]], [-v2[0], v1[0]]]]
    countA, countB = dot(inverse_m, C)
    print(countA, countB)
    
    aX, aY = v1
    bX, bY = v2
    targetX, targetY = C

    currX = countA * aX + countB * bX
    currY = countA * aY + countB * bY

    print(gcd(aX, bX))

    # break


print(result)

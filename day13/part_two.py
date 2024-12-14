import re
from typing import List

with open('day13.input', 'r') as file:
    input = [re.findall("[0-9]+", str(line)) for line in file]

def dot(v1: List[List[int]], v2: List[List[int]]) -> List[int]:
    return [sum([v1[i][j] * v2[j]  for j in range(len(v1[i]))]) for i in range(len(v1))]

def solve_linear_eq(M: List[List[int]], v: List[int]):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    M[0][0], M[1][1] = M[1][1], M[0][0]
    M[0][1] *= -1
    M[1][0] *= -1
    return dot([[1 / det * each for each in col] for col in M], v)
    

result = 0

i = 0
while i < len(input):

    if not input[i]:
        i += 1
        continue

    v1 = aX, aY = [int(char) for char in input[i]]
    i += 1
    v2 = bX, bY = [int(char) for char in input[i]]
    i += 1
    C = targetX, targetY = [int(char) + 10000000000000 for char in input[i]]
    i += 1

    A, B = solve_linear_eq([[aX, bX], [aY, bY]], C)
    if round(A) * aX + round(B) * bX == targetX and round(A) * aY + round(B) * bY == targetY:
        result += 3 * round(A) + round(B)

print(result)

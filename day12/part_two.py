
from typing import List

with open('day12.input', 'r') as file:
    grid = [line.strip() for line in file]

ROWS = len(grid)
COLS = len(grid[0])

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
visitedPerim = [[False for _ in range(COLS)] for _ in range(ROWS)]

areas: List[tuple] = []

def dfsArea(r, c, plant) -> int:
    if (r > -1 and c > -1 and r < ROWS and c < COLS and not visited[r][c] and grid[r][c] == plant):
        visited[r][c] = True
        return 1 + sum([
            dfsArea(r + 1, c, plant), dfsArea(r, c + 1, plant),
            dfsArea(r - 1, c, plant), dfsArea(r, c - 1, plant) 
            ])
    else:
        return 0
    
def dfsPerim(r, c, fences: List[List[List[bool]]]):
    if visitedPerim[r][c]: 
        return 0 
    else:
        visitedPerim[r][c] = True
        result = 0
        for idx, d in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]): # up down left right
            dy, dx = d
            pR = r + dy
            pC = c + dx
            if (pR < 0 or pC < 0 or pR >= ROWS or pC >= COLS or grid[r][c] != grid[pR][pC]):
                result += 1
                fences[idx][r][c] = True
            else:
                result += dfsPerim(pR, pC, fences)
        return result
    
def fences_to_sides(fences: List[List[List[bool]]]):
    result = 0
    for row in fences[0]:
        i = 0
        while i < len(row):
            if row[i]:
                result += 1
                while i < len(row) and row[i]:
                    i += 1
                i -= 1
            i += 1
    top = result

    for row in fences[1]:
        i = 0
        while i < len(row):
            if row[i]:
                result += 1
                while i < len(row) and row[i]:
                    i += 1
                i -= 1
            i += 1

    for col in range(len(fences[2][0])):
        row = 0
        while row < len(fences[2]):
            if fences[2][row][col]:
                result += 1
                while row < len(fences[2]) and fences[2][row][col]:
                    row += 1
                row -= 1
            row += 1

    for col in range(len(fences[3][0])):
        row = 0
        while row < len(fences[3]):
            if fences[3][row][col]:
                result += 1
                while row < len(fences[3]) and fences[3][row][col]:
                    row += 1
                row -= 1
            row += 1
    return result
    
for r in range(ROWS):
    for c in range(COLS):
        if not visited[r][c]:
            area = dfsArea(r, c, grid[r][c])
            fences = [[[False for _ in range(ROWS)] for _ in range(COLS)] for _ in range(4)]
            perim = dfsPerim(r, c, fences)
            areas.append((
                area, fences_to_sides(fences), perim
            ))


print(sum([a * b for a, b, c in areas]))
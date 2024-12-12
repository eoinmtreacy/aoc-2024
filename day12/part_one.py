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
    
def dfsPerim(r, c):
    if visitedPerim[r][c]: 
        return 0 
    else:
        visitedPerim[r][c] = True
        result = 0
        for d in [(1,0), (0,1), (-1, 0), (0, -1)]:
            dx, dy = d
            pR = r + dx
            pC = c + dy
            if (pR < 0 or pC < 0 or pR >= ROWS or pC >= COLS or grid[r][c] != grid[pR][pC]):
                result += 1
            else:
                result += dfsPerim(pR, pC)
        return result
    

    
for r in range(ROWS):
    for c in range(COLS):
        if not visited[r][c]:
            area = dfsArea(r, c, grid[r][c])
            perim = dfsPerim(r, c)
            areas.append((
                area, perim
            ))

print(sum([a * b for a, b in areas]))
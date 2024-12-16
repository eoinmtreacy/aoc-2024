with open('day16.sample', 'r') as file:
    grid = [line.strip() for line in file]

ROWS: int = len(grid)
COLS: int = len(grid[0])

directions = ((0,1), (1,0), (0,-1), (-1,0)) # e s w n

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

def dfs(r, c, idx, carry = 0):
    # if r < 0 or c < 0 or r >= ROWS or c >= COLS: return float('inf')
    if grid[r][c] == '#': return float('inf')
    if visited[r][c]: return float('inf')
    if grid[r][c] == 'E': return carry

    visited[r][c] = True

    paths = []

    for i, cost in zip(range(idx - 1, idx + 3), [1001, 1, 1001, 2001]):
        dr, dc = directions[(i + 4) % 4]
        nr, nc = r + dr, c + dc
        paths.append(dfs(nr, nc, i, carry + cost))

    

    return min(paths)

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            result = dfs(r, c, 0)
            break

print(result)




with open('day10.input', 'r') as file:
    grid = [[int(char)  if char != '.' else float('inf') for char in line.split()[0]] for line in file]

result = 0

def dfs(r, c, prev):
    if (r > -1 and c > -1 and r < len(grid) and c < len(grid[0]) and grid[r][c] - prev == 1):
        if grid[r][c] == 9:
            return 1
        return sum([
            dfs(r + 1, c, grid[r][c]), dfs(r, c + 1, grid[r][c]),
            dfs(r - 1, c, grid[r][c]), dfs(r, c - 1, grid[r][c])
        ])
    else:
        return 0 
    
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            result += dfs(r, c, grid[r][c] - 1)

print(result)
with open('day10.input', 'r') as file:
    grid = [[int(char)  if char != '.' else float('inf') for char in line.split()[0]] for line in file]

result = 0

def dfs(r, c, prev, nines):
    if (r > -1 and c > -1 and r < len(grid) and c < len(grid[0]) and grid[r][c] - prev == 1):
        if grid[r][c] == 9:
            nines.add((r,c))
        else:
            dfs(r + 1, c, grid[r][c], nines) 
            dfs(r, c + 1, grid[r][c], nines)
            dfs(r - 1, c, grid[r][c], nines) 
            dfs(r, c - 1, grid[r][c], nines)
    else:
        return
    
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            newSet = set()
            dfs(r, c, grid[r][c] - 1, newSet)
            print(newSet)
            result += len(newSet)

print(result)
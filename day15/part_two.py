with open('day15.input', 'r') as file:
    input = file.read()
    grid, moves = input.split("\n\n")
    grid = [[c for c in line] for line in grid.split('\n')]
    print(len(moves.split()))
    moves = "".join(moves.split())
    print(len(moves))

ROWS: int = len(grid)
COLS: int = len(grid[0])

dir: dict = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == '@':
            r, c = i, j
            grid[i][j] = '.'
            break
        
for m in moves:
    dr, dc = dir[m]
    pr, pc = r + dr, c + dc

    if grid[pr][pc] == '#':
        continue

    elif grid[pr][pc] == '.':
        r += dr
        c += dc
        continue

    while grid[pr][pc] != '#' and grid[pr][pc] != '.':
        pr += dr
        pc += dc
    if grid[pr][pc] == '.':
        grid[pr][pc], grid[r + dr][c + dc] = grid[r + dr][c + dc], grid[pr][pc]
        r += dr
        c += dc

result = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'O':
            result += c + 100 * r

print(result)
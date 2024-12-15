with open('day15.sample3', 'r') as file:
    input = file.read()
    grid, moves = input.split("\n\n")

def converter(c):
    if c == '#': return '##'
    if c == '.': return '..'
    if c == 'O': return '[]'
    if c == '@': return '@.'

grid = [list("".join([converter(c) for c in line])) for line in grid.split('\n')]
moves = "".join(moves.split())

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
        print(grid[i][j], end="")
        if grid[i][j] == '@':
            r, c = i, j
            grid[i][j] = '.'
    print()
        
for m in moves:
    dr, dc = dir[m]
    pr, pc = r + dr, c + dc

    if grid[pr][pc] == '#':
        continue

    elif grid[pr][pc] == '.':
        r += dr
        c += dc
        continue

    # horizontal movement
    if dr == 0:
        while grid[pr][pc] != '#' and grid[pr][pc] != '.':
            pr += dr
            pc += dc
        
        if grid[pr][pc] == '.':
            if dc < 0: # pushing left
                grid[pr][pc : c] = grid[pr][pc + 1: c + 1]
            else:
                grid[pr][c + dc + 1 : pc + 1] = grid[pr][c + dc : pc]
                grid[pr][c + dc] = '.'
            r += dr
            c += dc
    # break

result = 0
for r in range(ROWS):
    for c in range(COLS):
        print(grid[r][c], end='')
        if grid[r][c] == 'O':
            result += c + 100 * r
    print()

print(result)
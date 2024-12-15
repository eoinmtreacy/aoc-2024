with open('day15.input', 'r') as file:
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
print()

for m in moves:
    dr, dc = dir[m]
    pr, pc = r + dr, c + dc


    if grid[pr][pc] == '#':
        continue

    if grid[pr][pc] == '.':
        r = pr
        c = pc
        continue
    
    def canMove(r, c, movers = []):
        if grid[r][c] == '#': return False
        if grid[r][c] == '.': return True

        movers.append((r,c, grid[r][c]))
        if dr != 0: # moving vertically 
            if grid[r][c] == ']':
                nr, nc = r, c - 1
            else:
                nr, nc = r, c + 1
            
            movers.append((nr, nc, grid[nr][nc]))

            return canMove(r + dr, c + dc, movers) and canMove(nr + dr, nc + dc, movers)
        else:
            return canMove(r + dr, c + dc, movers)
            
    c2m = []
    if canMove(pr, pc, c2m):
        for r, c, _ in c2m:
            grid[r][c] = '.'
        for r, c, symbol in c2m:
            grid[r + dr][c + dc] = symbol

        r = pr
        c = pc

result = 0
for r in range(ROWS):
    for c in range(COLS):
        print(grid[r][c], end='')
        if grid[r][c] == '[':
            result += c + 100 * r
    print()

print(result)
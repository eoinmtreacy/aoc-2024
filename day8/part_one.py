with open('day8.input', 'r') as file:
    grid = [list(line.strip()) for line in file]

map = {}
nodes = set()
result = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        el = grid[r][c]
        if el != '.':

            if map.get(el) == None:
                map[el] = [(r,c)]

            else:
                for coord in map[el]:
                    row, col = coord

                    if r == row:
                        diff = col - c
                        if c - diff > -1: nodes.add((r, c - diff))
                        if col + diff < len(grid[0]): nodes.add((r, c + diff))

                    elif c == col:
                        diff = row - r
                        if r - diff > -1: nodes.add((r - diff, c))
                        if row + diff < len(grid): nodes.add((r + diff, c))

                    elif c < col:
                        dR, dC = r - row, col - c
                        if c - dC > -1 and r + dR < len(grid): nodes.add((r + dR, c - dC))
                        if col + dC < len(grid[0]) and row - dR > -1: nodes.add((row - dR, col + dC))

                    elif c > col:
                        dR, dC = r - row, c - col
                        if c + dC < len(grid[0]) and r + dR < len(grid): nodes.add((r + dR, c + dC))
                        if col - dC > -1 and row - dR > -1: nodes.add((row - dR, col - dC))


                map[el].append((r,c))

print(len(nodes))
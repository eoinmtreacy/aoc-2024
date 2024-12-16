def main():
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
                    nodes.add((r,c))
                    for coord in map[el]:
                        row, col = coord
                        nodes.add((row, col))


                        if r == row:
                            diff = col - c
                            inc = diff
                            while (col - diff > -1 or c + diff < len(grid[0])):
                                if c - diff > -1: nodes.add((r, c - diff))
                                if col + diff < len(grid[0]): nodes.add((r, c + diff))
                                diff += inc


                        elif c == col:
                            diff = row - r
                            inc = diff
                            while (row - diff > -1 or r + diff < len(grid)):
                                if row - diff > -1: nodes.add((row - diff, c))
                                if row + diff < len(grid): nodes.add((row + diff, c))
                                diff += inc

                        elif c < col:
                            dR, dC = r - row, col - c
                            incR, incC = dR, dC
                            while ( ( c - dC > -1 and r + dR < len(grid) ) or ( col + dC < len(grid[0]) and row - dR > -1 ) ):
                                if c - dC > -1 and r + dR < len(grid): nodes.add((r + dR, c - dC))
                                if col + dC < len(grid[0]) and row - dR > -1: nodes.add((row - dR, col + dC))
                                dR += incR
                                dC += incC

                        elif c > col:
                            dR, dC = r - row, c - col
                            incR, incC = dR, dC
                            while ( (c + dC < len(grid[0]) and r + dR < len(grid)) or (col - dC > - 1 and row - dR > -1) ):
                                if c + dC < len(grid[0]) and r + dR < len(grid): nodes.add((r + dR, c + dC))
                                if col - dC > -1 and row - dR > -1: nodes.add((row - dR, col - dC))
                                dR += incR
                                dC += incC


                    map[el].append((r,c))

    print(len(nodes))

if __name__ == "__main__":
    main()
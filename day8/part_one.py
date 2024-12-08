with open('day7.sample', 'r') as file:
    grid = [list(line.strip()) for line in file]

# def genDiag(grid):
#     result = []

#     for r in range(len(grid)):
#         stash = r
#         c = 0
#         line = []
#         while r > -1 and c < len(grid[0]):
#             line.append(grid[r][c])
#             r -= 1
#             c += 1
#         result.append(line)
#         r = stash

#     for c in range(1, len(grid[0])):
#         stash = c 
#         r = len(grid) - 1
#         line = []
#         while r > 0 and c < len(grid[0]):
#             line.append(grid[r][c])
#             r -= 1
#             c += 1
#         result.append(line)
#         c = stash

#     return result

# verticals = []
# for c in range(len(grid)):
#     line = []
#     for r in range(len(grid)):
#         line.append(grid[r][c])
#     verticals.append(line)

# diagonals = []
# for line in genDiag(grid):
#     diagonals.append(line)

# revDi = []
# for line in genDiag(grid[::-1]):
#     revDi.append(line)

# for v in verticals: grid.append(v)
# for d in diagonals: grid.append(d)
# for r in revDi: grid.append(r)

# for idx, line in enumerate(grid):
#     print(idx, line)

# def countAntiNodes(line):
#     result = 0
#     map = {}
#     for idx, el in enumerate(line):
#         if el != '.':
#             if map.get(el) == None:
#                 map[el] = [idx]
#             else:
#                 rec = map[el][-1]
#                 print(el, rec, idx)
#                 map[el].append(idx)
#                 diff = idx - rec
#                 if rec - diff > -1:
#                     result += 1
#                 if idx + diff < len(line):
#                     result += 1
#     return result

# result = 0
# for idx, line in enumerate(grid):
#     inc = countAntiNodes(line)
#     if inc > 0: print(idx)
#     result += inc
map = {}
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
                        if c - diff > -1: result += 1
                        if col + diff < len(grid[0]): result += 1

                    elif c == col:
                        diff = row - r
                        if r - diff > -1: result += 1
                        if row + diff < len(grid): result += 1

                    elif c < col:
                        dR, dC = r - row, col - c
                        if c - dC > -1 and r + dR < len(grid): result += 1
                        if col + dC < len(grid[0]) and row - dR > -1: result += 1

                    elif c > col:
                        dR, dC = r - row, c - col
                        if c + dC < len(grid[0]) and r + dR < len(grid): result +=1
                        if col - dC > -1 and row - dR > -1: result += 1


                map[el].append((r,c))


[print(line) for line in grid]
print(map)
print(result)
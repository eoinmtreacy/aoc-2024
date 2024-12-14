import re
import numpy as np
with open('day13.input', 'r') as file:
    input = [line.strip().split() for line in file]

X = 101
Y = 103


temp = []
for line in input:
    left, right = line
    x, y = [int(char) for char in re.findall("[0-9]+", left)]
    dx, dy = right.split('=')[1].split(',')
    dx = int(dx)
    dy = int(dy)
    temp.append((x,y,dx,dy))

_x, _y, dx, dy = robots = np.array(temp).T

count = 1
best = float('inf')
# while True:
for count in range(8162):
    _x = (_x + dx) % X
    _x = np.where(_x > -1, _x, X + _x)

    _y = (_y + dy) % Y
    _y = np.where(_y > -1, _y, Y + _y)

    print(count)
    if count > 8157:
        grid = [[" " for _ in range(X)] for _ in range(Y)]
        for x, y in zip(_x, _y):
            grid[y][x] = '#'
        for y in range(Y):
            for x in range(X):
                print(grid[y][x], end="")
            print()


    # x_diff = _x[:, np.newaxis] - _x
    # y_diff = _y[:, np.newaxis] - _y
    # distances = np.sqrt(x_diff**2 + y_diff**2)

    # # Compute the average distance
    # avg = np.mean(distances)
    # if avg < best:
    #     print("New Best distance:", avg, "Count", count)
    # best = min(best, avg)
    # count += 1

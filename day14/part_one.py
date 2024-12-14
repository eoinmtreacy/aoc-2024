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

for _ in range(100):
    _x = (_x + dx) % X
    _x = np.where(_x > -1, _x, X + _x)

    _y = (_y + dy) % Y
    _y = np.where(_y > -1, _y, Y + _y)

nw, ne, sw, se = 0, 0, 0, 0

for x, y in zip(_x,_y):
    if x != X // 2 and y != Y // 2:
        if x < X / 2:
            if y < Y / 2:
                nw += 1
            else:
                sw += 1
        else:
            if y < Y / 2:
                ne += 1
            else:
                se += 1

result = 1
for q in [ne, nw, sw, se]: result *= q
print(result)
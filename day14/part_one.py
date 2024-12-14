import re
with open('day13.input', 'r') as file:
    input = [line.strip().split() for line in file]

X = 101
Y = 103

nw, ne, sw, se = 0, 0, 0, 0

pre = []
robots = []

for line in input:
    left, right = line
    x, y = [int(char) for char in re.findall("[0-9]+", left)]
    pre.append((x, y))
    dx, dy = right.split('=')[1].split(',')
    dx = int(dx)
    dy = int(dy)

    for _ in range(100):
        x = (x + dx) % X if (x + dx) % X > -1 else X + x
        y = (y + dy) % Y if (y + dy) % Y > -1 else Y + y

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

    print(x, y, dx, dy)

    robots.append((x,y))

print(sorted(robots, key=lambda x : (x[0], x[1])))
print(nw, ne, sw, se)
result = 1
for q in [ne, nw, sw, se]: result *= q
print(result)
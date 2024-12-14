import re 

with open('day13.input', 'r') as file:
    input = [re.findall("[0-9]+", str(line)) for line in file]

result = 0

i = 0
while i < len(input):

    if not input[i]:
        i += 1
        continue

    aX, aY = [int(char) for char in input[i]]
    i += 1
    bX, bY = [int(char) for char in input[i]]
    i += 1
    targetX, targetY = [int(char) for char in input[i]]
    i += 1

    countA = 0
    countB = min(targetX // bX, targetY // bY)

    currX, currY = bX * countB, bY * countB

    seen = set()
    while (currX != targetX or currY != targetY) and (-1 < countA < 101 and countB > -1):
        if currX > targetX or currY > targetY:
            currX -= bX
            currY -= bY
            countB -= 1
        else:
            currX += aX
            currY += aY
            countA += 1
        
        if (countA, countB) in seen:
            break
        seen.add((countA, countB))

    if currX == targetX and currY == targetY and (-1 < countA < 101 or countB > -1):
        result += countA * 3 + countB

print(result)

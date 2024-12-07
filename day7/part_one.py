from typing import List
# read grid 
# with open('day7.sample', 'r') as file:
#     grid = [list(line.strip()) for line in file]

# read lines

def getPerms(input: List[int]) -> set:
    perms = set()
    perms.add(input[0])
    for num in input[1:]:
        newPerms = set()
        for p in perms:
            newPerms.add(num * p)
            newPerms.add(num + p)
        perms = newPerms
    return perms

with open('day7.input', 'r') as file:
    lines = [line for line in file]

lines = [line.split(":") for line in lines]

targets, args = [int(line[0]) for line in lines], [[int(num) for num in line[1].split()] for line in lines]

result = 0 

for t, a in zip(targets, args):
    if t in getPerms(a):
        result += t

print(result)
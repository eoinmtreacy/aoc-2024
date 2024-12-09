with open('day9.input', 'r') as file:
    string = [line for line in file][0]

big = []

for a, b, idx in zip(range(0, len(string), 2), range(1, len(string) + 1, 2), range(len(string))):
    for _ in range(int(string[a])):
        big.append(idx)
    if b < len(string):
        for _ in range(int(string[b])):
            big.append('.')

left, right = 0, len(big) - 1
l, r = left, right

while (right > -1):
    while right == '.':
        r -= 1
    while r > -1 and big[right] == big[r]:
        r -= 1
    file = right - r

    left = 0
    while(left < right):
        while left < right and big[left] != '.':
            left += 1
        l = left

        while l < right and big[l] == '.':
            l += 1
        
        if l - left >= file:
            # move the file
            big[left : left + file], big[r + 1 : right + 1] = big[r + 1 : right + 1], big[left : left + file]
            break
        else:
            left = l

    right = r

print(sum([idx * int(num) if num != '.' else 0 for idx, num in enumerate(big)]))
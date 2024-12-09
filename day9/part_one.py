with open('day9.input', 'r') as file:
    string = [line for line in file][0]

big = []

for a, b, idx in zip(range(0, len(string), 2), range(1, len(string) + 1, 2), range(len(string))):
    for _ in range(int(string[a])):
        big.append(idx)
    if b < len(string):
        for _ in range(int(string[b])):
            big.append('.')

l, r = 0, len(big) - 1

while (l < r):
    if big[l] != '.': l += 1
    if big[r] == '.': r -= 1
    if big[l] == '.' and big[r] != '.':
        big[l], big[r] = big[r], big[l]


print(sum([idx * int(num) if num != '.' else 0 for idx, num in enumerate(big)]))
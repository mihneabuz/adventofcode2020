import sys
import numpy as np

map = []

for line in sys.stdin:
    map.append(list(line)[0 : -1])

map = np.array(map)
[height, width] = map.shape
print(map)

mult = [1, 3, 5, 7]
total = 1
for k in mult:
    nr = 0
    for i in range(height):
        j = (k * i) % width
        if (map[i, j] == '#'):
            nr += 1
    print(nr)
    total *= nr

nr = 0
for i in range(0, height, 2):
    j = int(i / 2) % width
    if (map[i, j] == '#'):
        nr += 1

print(nr)
total *= nr
print(map)
print(total)

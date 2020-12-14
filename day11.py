import numpy as np
import sys

l = []
sizex = 0
sizey = 0
directions = [(0, 1), (0, -1), (1, 0), (1, 1),
             (1, -1), (-1, 0), (-1, 1), (-1, -1)]

for line in sys.stdin:
    l.append(list(line)[:-1])

sizex = len(l)
sizey = len(l[0])

def valid_poz(i, j):
    if (i >= 0 and j >= 0 and i < sizex and j < sizey):
        return True
    return False

def count_adj(i, j):
    nr = 0
    for d in directions:
        x = i + d[0]
        y = j + d[1]
        if (valid_poz(x, y) and l[x][y] == '#'):
            nr += 1
    return nr

def count_vision(i, j):
    nr = 0
    for d in directions:
        x = i + d[0]
        y = j + d[1]
        while(valid_poz(x, y) and l[x][y] == '.'):
            x = x + d[0]
            y = y + d[1]
        if (valid_poz(x, y) and l[x][y] == '#'):
            nr += 1
    return nr


#print(np.array(l))
cpy = l.copy()

change = 1
while (change):
    change = 0
    next = [[0 for j in range(sizey)] for i in range(sizex)]
    for i in range(sizex):
        for j in range(sizey):
            if (l[i][j] == '.'):
                next[i][j] = '.'
            else:
                adj = count_adj(i, j)
                if (adj == 0 and l[i][j] == 'L'):
                    next[i][j] = '#'
                    change = 1
                elif (adj > 3 and l[i][j] == '#'):
                    next[i][j] = 'L'
                    change = 1
                else:
                    next[i][j] = l[i][j]
    l = next

#print(np.array(l))
nr = 0
for k in l:
    for i in k:
        if (i == '#'):
            nr += 1
print(nr)

l = cpy

change = 1
while(change):
    change = 0
    next = [[0 for j in range(sizey)] for i in range(sizex)]
    for i in range(sizex):
        for j in range(sizey):
            if (l[i][j] == '.'):
                next[i][j] = '.'
            else:
                adj = count_vision(i, j)
                if (adj == 0 and l[i][j] == 'L'):
                    next[i][j] = '#'
                    change = 1
                elif (adj > 4 and l[i][j] == '#'):
                    next[i][j] = 'L'
                    change = 1
                else:
                    next[i][j] = l[i][j]
    l = next

nr = 0
for k in l:
    for i in k:
        if (i == '#'):
            nr += 1
print(nr)

import sys
import numpy as np
from scipy.ndimage import convolve

#Tried using the symetry to calculate less buut
#I only got it to work for 3 dimensions :(

def Kernel(n):
    aux = np.ones(tuple(3 for i in range(n)))
    aux[tuple(1 for i in range(n))] = 0
    return aux

def step(dim, start, iter):
    ker = Kernel(dim)

    space = np.zeros((1, *(len(start) for i in range(dim - 1))))
    space[tuple(0 for i in range(dim - 2))] = start

    for i in range(iter):
        space = np.pad(space, 1)
        neighbors = convolve(space, ker)
        space = np.where((neighbors == 3) | ((space == 1) & (neighbors==2)), 1, 0)

    print(space[6].sum(), space[7 :].sum())
    return space.sum()

start = []

for line in sys.stdin:
    start.append([1 if x == '#' else 0 for x in list(line[: -1])])


print("One: ", step(3, start, 6))
print("Two: ", step(4, start, 6))

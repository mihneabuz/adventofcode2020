from numba import njit
import sys
import numpy as np

d = [0, 1, -1]
limit = 20
space = np.zeros([limit, limit, limit, limit])

l = []
for line in sys.stdin:
  l.append([1 if x == '#' else 0 for x in list(line[: -1])])
n = len(l)
print(np.array(l))

space[int((limit - n) / 2) : int((limit + n) / 2),
      int((limit - n) / 2) : int((limit + n) / 2),
      int(limit / 2 - 1),
      int(limit / 2 - 1)] = np.array(l)
@njit
def valid(limit, x, y, z, t) -> bool:
  if ((x > limit-1) or (y > limit-1) or (z > limit-1) or (t > limit-1)
      or x < 0 or y < 0 or z < 0 or t < 0):
    return False
  return True

@njit
def count_nei(space, limit, x, y, z, t) -> int:
  nei = 0
  d = (0, 1, -1)
  for i in d:
    for j in d:
      for k in d:
        for q in d:
          if not valid(limit, x + i, y + j, z + k, t + q):
            pass
          else:
            nei += space[x + i, y + j, z + k, t + q] == 1
  return nei - space[x, y, z, t]

@njit
def step(new_space, space, limit):
  for i in range(limit):
    print("   ", i)
    for j in range(limit):
      for k in range(limit):
        for q in range(limit):
          nei = count_nei(space, limit, i, j, k, q)
          if (space[i, j, k, q] == 1 and nei != 2 and nei != 3):
            new_space[i, j, k, q] = 0
          elif(space[i, j, k, q] == 0 and nei == 3):
            new_space[i, j, k, q] = 1
          else:
            new_space[i, j, k, q] = space[i, j, k, q]

for i in range(6):
  new_space = np.zeros([limit, limit, limit, limit])
  print("\n\nstep: ", i)
  step(new_space, space, limit)
  space = new_space

print(sum(sum(sum(sum(space)))))

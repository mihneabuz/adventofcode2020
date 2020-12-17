import sys
import numpy as np

d = [0, 1, -1]
limit = 20
space = np.zeros([limit, limit, limit])

l = []
for line in sys.stdin:
  l.append([1 if x == '#' else 0 for x in list(line[: -1])])
n = len(l)
print(np.array(l))

space[int((limit - n) / 2) : int((limit + n) / 2),
      int((limit - n) / 2) : int((limit + n) / 2),
      int(limit / 2 - 1)] = np.array(l)
print(space[:, :, int(limit / 2 - 1)], "\n")

def valid(limit, x, y, z):
  if ((x > limit-1) or (y > limit-1) or (z > limit-1) or x < 0 or y < 0 or z < 0):
    return False
  return True


def count_nei(space, limit, x, y, z):
  nei = 0
  for i in d:
    for j in d:
      for k in d:
        if not valid(limit, x + i, y + j, z + k):
          pass
        else:
          nei += space[x + i, y + j, z + k] == 1
  return nei - space[x, y, z]

def step(new_space, space, limit):
  for i in range(limit):
    for j in range(limit):
      for k in range(limit):
        nei = count_nei(space, limit, i, j, k)
        if (space[i, j, k] == 1 and nei != 2 and nei != 3):
          new_space[i, j, k] = 0
        elif(space[i, j, k] == 0 and nei == 3):
          new_space[i, j, k] = 1
        else:
          new_space[i, j, k] = space[i, j, k]

for i in range(6):
  new_space = np.zeros([limit, limit, limit])
  step(new_space, space, limit)
  space = new_space

print(new_space[:, :, int(limit / 2 - 1)-1], "\n")
print(new_space[:, :, int(limit / 2 - 1)], "\n")
print(new_space[:, :, int(limit / 2 - 1)+1], "\n")

print(sum(sum(sum(space))))

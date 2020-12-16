import time
import numpy as np
from numba import njit

input = "2,1,10,11,0,6"

nums = np.array([int(x) for x in input.split(",")])

begin = time.time()
@njit
def day15(nums, target):
    ap = np.full(target, -1)
    for i, val in enumerate(nums[: -1]):
        ap[val] = i
    last = nums[-1]
    for i in range(len(nums) - 1, target - 1):
        new = 0 if ap[last] == -1 else i - ap[last]
        ap[last] = i
        last = new
    return last

print(day15(nums, 2020))
print(day15(nums, 30000000))
print(time.time() - begin)

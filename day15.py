line = input()
numbers = [int(x) for x in line.split(",")]

d = {}
for i in range(len(numbers)):
    d.update({numbers[i]: (-1, i)})

i = len(numbers)
last = numbers[len(numbers) - 1]

# brute force just worked I guess xD
while(i < 30000000):
    ap = d[last]
    if (ap[0] == -1):
        new = 0
    else:
        new = ap[1] - ap[0]
    if (new not in d):
        d.update({new: (-1, i)})
    ap = d[new]
    d.update({new: (ap[1], i)})
    if (i + 1 == 2020):
        print(i+1, new)
    last = new
    i += 1

print(new)

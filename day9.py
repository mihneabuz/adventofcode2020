import sys

l = []
preamble = 25
numbers = []
key = 0

for i in sys.stdin:
    numbers.append(int(i))
    if (len(l) < preamble):
        l.append(int(i))
    else:
        x = int(i)
        found = False
        for previous in l:
            if (x - previous in l and 2 * i != x):
                found = True
        if (not found):
            key = x
        l = l[1 :]
        l.append(x)

print(key, "\n")

for i in range(len(numbers)):
    s = numbers[i]
    j = i + 1
    while(s < key):
        s += numbers[j]
        j += 1
    if (s == key):
        solution = numbers[i : j]
        break

#print(solution)
print(max(solution) + min(solution))

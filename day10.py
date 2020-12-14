import sys

l = []

for line in sys.stdin:
    l.append(int(line))

current = 0
no = 0
dif1 = 0
dif3 = 0

target = max(l)

while(current < target):
    next = []
    for adaptor in l:
        if(adaptor - current < 4 and adaptor - current > 0):
            next.append(adaptor)
    if (min(next) == current + 1):
        dif1 += 1
    if (min(next) == current + 3):
        dif3 += 1
    no += 1
    current = min(next)

dif3 += 1
assert (no == len(l))
print(dif1, dif3, dif1 * dif3)

####################################################
#################ASA NU!###########################
count = 0
sequence = []
def add_elem(l, sequence, target):
    if(len(sequence) > 0):
        x = sequence[-1]
    else:
        x = 0
    if (x == target):
        print(sequence)
        global count
        count += 1
    else:
        for i in l:
            if (i - x > 0 and i - x < 4):
                sequence.append(i)
                add_elem(l, sequence, target)
                sequence.pop()

#add_elem(l, sequence, target)
#print(count)
####################################################

v = [0 for i in range(target + 1)]
v[0] = 1
for i in l:
    v[i] = 1

combinations = [0 for i in range(target + 1)]
combinations[0] = 1
if (v[1]):
    combinations[1] = 1
if (v[2]):
    combinations[2] = 1 + combinations[1] * v[1]

for i in range(1, target + 1):
    if (v[i]):
        combinations[i] = combinations[i - 1] * v[i - 1] +\
                          combinations[i - 2] * v[i - 2] +\
                          combinations[i - 3] * v[i - 3]

print(combinations[target])

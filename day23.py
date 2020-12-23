input = "952438716"
#input = "389125467"
nocups = 1000000
nopicked = 3

initial_cups = [int(x) for x in input]
print(initial_cups)

cups = {initial_cups[i]: initial_cups[i+1] for i in range(len(initial_cups)-1)}
cups.update({initial_cups[-1]:max(initial_cups) + 1})
for i in range(max(cups) + 1, nocups):
    cups.update({i:i+1})
cups.update({nocups:initial_cups[0]})

def pick(cups, current):
    picked = []
    picked.append(cups[current])
    for i in range(nopicked - 1):
        picked.append(cups[picked[-1]])
    cups[current] = cups[picked[-1]]
    for i in picked:
        cups[i] = -1
    return picked

def findlower(cups, current):
    lower = current - 1;
    while(1):
        if (lower == 0):
            lower = nocups
        if (lower in cups and cups[lower] != -1):
            return lower
        lower -= 1

def insert(cups, key, picked):
    next = cups[key]
    cups[key] = picked[0]
    for i in range(nopicked - 1):
        cups[picked[i]] = picked[i + 1]
    cups[picked[2]] = next

current = initial_cups[0]
for i in range(10000000):
    picked = pick(cups, current)
    lower = findlower(cups, current)
    insert(cups, lower, picked)
    current = cups[current]

x1 = cups[1]
x2 = cups[x1]
print("final: ", x1, x2, x1 * x2)

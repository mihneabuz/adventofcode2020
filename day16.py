import sys

fields = []
names = []

for line in sys.stdin:
    if (line == "\n"):
        break
    name = line.split(":")[0]
    names.append(name)
    line = line[: -1].split(":")[1].split(" ")[1:]
    a = line[0].split("-")
    b = line[2].split("-")
    fields.append([int(x) for x in [*a, *b]])

nrf = len(fields)
sys.stdin.readline()
myticket = [int(x) for x in sys.stdin.readline().split(",")]
sys.stdin.readline()
sys.stdin.readline()

def tvalid(i, k):
    if ((i >= k[0] and i <= k[1]) or (i >= k[2] and i <= k[3])):
        return 1;
    return 0

#Part one
tickets = []
s = 0
for line in sys.stdin:
    nr = [int(x) for x in line[: -1].split(",")]
    valid = 1
    for i in nr:
        ok = 0
        for k in fields:
            ok = tvalid(i, k)
            if (ok):
                break
        if (not ok):
            s += i
            valid = 0
            break
    if (valid):
        tickets.append(nr)

print(s)

#Part two
l = [[0 for j in range(nrf)] for i in range(nrf)]

#made a bitmap of maching values and fields and sum it over all tickets
for ticket in tickets:
    for i, val in enumerate(ticket):
        for j, field in enumerate(fields):
            l[i][j] += tvalid(val, field)

matched = [-1 for i in range(nrf)]
nrtickets = len(tickets)

while(-1 in matched):
    for i in range(nrf):
        found = 0
        for j in range(nrf):
            if (l[i][j] == nrtickets and j not in matched):
                if (not found):
                    found = 1
                    match = j
                else:
                    found = 0
                    break
        if (found):
            matched[i] = match

for i, val in enumerate(myticket):
    print(names[matched[i]], ":", val)

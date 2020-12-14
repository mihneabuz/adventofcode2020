import sys

time = int(sys.stdin.readline())
line = sys.stdin.readline()[:-1]
buses = [int(i) for i in line.replace("x,", "").split(",")]

min = time
bustime = 0
minind = 0

for i in range(len(buses)):
    x = (int(time / buses[i] + 1) * buses[i])
    if (x - time < min):
        min = x - time
        minind = i
        bustime = x
    #print(x, min)

print(buses[minind] * (bustime - time), "\n")

line = line.split(',')

l = []

for i in range(len(line)):
    try:
        x = int(line[i])
        l.append((x, i))
    except:
        pass
print(l)

mul = l[0][0]
x = l[0][0]

for i in l[1:]:
    while((x + i[1]) % i[0] != 0):
        x += mul
    mul = mul * i[0]
print(x)

#for i in range(100):
#    print(i, 17 * i, (17 * i + 2) % 13)

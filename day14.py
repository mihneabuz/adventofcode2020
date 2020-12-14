import sys

# Part one
'''
m0 = 0
m1 = 0
mem = {}
for command in sys.stdin:
    command = command[:-1].split(" ")
    if (command[0] == "mask"):
        m0 = 0
        m1 = 0
        k = 0
        for i in reversed(list(command[2])):
            if (i == 'X'):
                m0 += 1 << k
            elif (i == '1'):
                m0 += 1 << k
                m1 += 1 << k
            k += 1
    else:
        location = int(command[0][4 : -1])
        value = (int(command[2]) & m0) | m1
        mem.update({location: value})

print(sum(mem.values()))
'''

# Part two

def generate_address(address, value, mask, i):
    #print(address, i)
    if (i == 36):
        global mem
        mem.update({address: value})
    else:
        if (mask[35 - i] == '0'):
            generate_address(address, value, mask, i + 1)
        elif (mask[35 - i] == '1'):
            address = address | (1 << i)
            generate_address(address, value, mask, i + 1)
        else:
            address = address | (1 << i)
            generate_address(address, value, mask, i + 1)
            address = address & (~(1 << i))
            generate_address(address, value, mask, i + 1)
    return 0

mask = []
mem = {}
for command in sys.stdin:
    command = command[:-1].split(" ")
    if (command[0] == "mask"):
        mask = list(command[2])
    else:
        value = int(command[2])
        address = int(command[0][4:-1])
        generate_address(address, value, mask, 0)
print(sum(mem.values()))

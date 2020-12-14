import sys

commands = []
for line in sys.stdin:
    line = line.split(" ")
    commands.append([line[0], int(line[1][ : -1]), False])


def check_loop(commands):
    accumulator = 0
    idx = 0
    loops = False

    while (idx < len(commands)):
    #    print(accumulator, idx)
        if(commands[idx][2]):
            loops = True
            break
        else:
            commands[idx][2] = True

        if (commands[idx][0] == "nop"):
            idx += 1
        elif (commands[idx][0] == "acc"):
            accumulator += commands[idx][1]
            idx += 1
        elif (commands[idx][0] == "jmp"):
            idx += commands[idx][1]

    for i in commands:
       i[2] = False

    if (loops):
        print("it looped!")
    print(accumulator)

check_loop(commands)
for command in commands:
    if (command[0] == "jmp"):
        command[0] = "nop"
        check_loop(commands)
        command[0] = "jmp"
    elif (command[0] == "nop" and command[1] != 0):
        command[0] = "jmp"
        check_loop(commands)
        command[0] = "nop"

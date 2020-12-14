import sys

test_string = list("FBFBBFFRLR")

maxim = 0
id_list = [0 for i in range(127 * 8 + 7)]

for line in sys.stdin:
    line = list(line)
    rowL = 0
    rowU = 127
    columnL = 0
    columnU = 7
    for char in line[0 : 7]:
        #print(char)
        if (char == "F"):
            rowU = int((rowU + rowL) / 2)
        elif (char == "B"):
            rowL = int((rowU + rowL) / 2) + 1
        #print(rowL, rowU)

    for char in line[7 :]:
        #print(char)
        if (char == "L"):
            columnU = int((columnU + columnL) / 2)
        elif (char == "R"):
            columnL = int((columnU + columnL) / 2) + 1
        #print(columnL, columnU)
    x = rowU * 8 + columnU
    id_list[x] = 1
    if (x > maxim):
        maxim = x

print(maxim)
for i in range(1, maxim):
    if (id_list[i] == 0 and id_list[i - 1] == 1 and id_list[i + 1] == 1):
        print(i)
        break

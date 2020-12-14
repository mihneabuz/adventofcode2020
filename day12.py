import numpy as np
import sys

input = []

#part one
poz = np.array([0, 0])
direction = np.array([0, 1])
R_rotation = np.array([[0, 1], [-1, 0]])
L_rotation = np.array([[0, -1], [1, 0]])
# Matrice de rotatie: [cos t, -sin t][sin t, cos t]

for command in sys.stdin:
    input.append(command)
    if (command[0] == 'F'):
        poz += direction * int(command[1:])
    elif (command[0] == 'R'):
        nr = int(int(command[1:]) / 90)
        direction = direction.dot(np.linalg.matrix_power(R_rotation, nr))
    elif (command[0] == 'L'):
        nr = int(int(command[1:]) / 90)
        direction = direction.dot(np.linalg.matrix_power(L_rotation, nr))
    elif (command[0] == 'N'):
        poz[0] += int(command[1:])
    elif (command[0] == 'S'):
        poz[0] -= int(command[1:])
    elif (command[0] == 'E'):
        poz[1] += int(command[1:])
    elif (command[0] == 'W'):
        poz[1] -= int(command[1:])

distance = sum(abs(poz))
print(distance)


#part two
ship_poz = np.array([0, 0])
wp_poz = np.array([1, 10])
R_rotation = np.array([[0, 1], [-1, 0]])
L_rotation = np.array([[0, -1], [1, 0]])

for command in input:
    print(command[:-1])
    if (command[0] == 'F'):
        ship_poz += wp_poz * int(command[1:])
    elif (command[0] == 'R'):
        nr = int(int(command[1:]) / 90)
        wp_poz = wp_poz.dot(np.linalg.matrix_power(R_rotation, nr))
    elif (command[0] == 'L'):
        nr = int(int(command[1:]) / 90)
        wp_poz = wp_poz.dot(np.linalg.matrix_power(L_rotation, nr))
    elif (command[0] == 'N'):
        wp_poz[0] += int(command[1:])
    elif (command[0] == 'S'):
        wp_poz[0] -= int(command[1:])
    elif (command[0] == 'E'):
        wp_poz[1] += int(command[1:])
    elif (command[0] == 'W'):
        wp_poz[1] -= int(command[1:])
    print(ship_poz, wp_poz, "\n")

distance = sum(abs(ship_poz))
print(distance)

from numba import njit

card = int(input())
door = int(input())

print(card, door)


@njit
def find(card, door):
    x = 1
    i = 0
    while (1):
        x = (x * 7) % 20201227
        i += 1
        if (x == card):
            subject = door
            loop = i
            return loop, subject
        if (x == door):
            subject = card
            loop = i
            return loop, subject


loop, subject = find(card, door)

@njit
def key(loop, subject):
    x = 1
    for _ in range(loop):
        x = (x * subject) % 20201227
    return x

print(key(loop, subject))

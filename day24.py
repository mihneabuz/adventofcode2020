import sys
from itertools import zip_longest

directions = {"ne":(1, 1),  "e":(2, 0),  "se":(1, -1),
              "nw":(-1, 1), "w":(-2, 0), "sw":(-1, -1)}
tiles = set()

for line in sys.stdin:
    i = 0
    tile = [0, 0]
    while (i < len(line) - 1):
        move = ""
        if (line[i] == 'e' or line[i] == 'w'):
            move = line[i]
            i += 1
        else:
            move = line[i:i+2]
            i += 2
        d = directions[move]
        tile[0] += d[0]
        tile[1] += d[1]
    tile = tuple(tile)
    if (tile not in tiles):
        tiles.add(tile)
    else:
        tiles.remove(tile)

print("Part one:", len(tiles))

def neighbours(tile):
    return zip_longest([], list(directions.values()), fillvalue=tile)

def step(tiles):
    whites = set()
    blacks = set()
    for tile in tiles:
        blacks.add(tile)
        whites = whites.union([(i[0][0] + i[1][0], i[0][1] + i[1][1])
                                for i in neighbours(tile)])
    new = set()
    for tile in blacks:
        nei = sum([1 if (i[0][0] + i[1][0], i[0][1] + i[1][1]) in blacks else 0
                   for i in neighbours(tile)])
        if (nei == 1):
            new.add(tile)
    for tile in whites:
        nei = sum([1 if (i[0][0] + i[1][0], i[0][1] + i[1][1]) in blacks else 0
                   for i in neighbours(tile)])
        if (nei == 2):
            new.add(tile)
    return new

for i in range(100):
    tiles = step(tiles)

print("Part two:", len(tiles))

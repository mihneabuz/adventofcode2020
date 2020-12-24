import sys
import math
import numpy as np

class Tile:

    def __init__(self, index, m):
        self.index = index
        self.map = m
        self.edges = [0] * 4
        self.edges[0] = hash_edge(m[0, :])
        self.edges[1] = hash_edge(m[:, 9])
        self.edges[2] = hash_edge(m[9, ::-1])
        self.edges[3] = hash_edge(m[::-1, 0])
        self.matches = 0
        self.next = []
        self.seen = 0

    def calc_matches(self, tiles):
        matches = [0] * 4
        for tile in tiles:
            if (self.index != tile.index):
                matcharr = np.array([1 if (i == j or i == flip_value(j)) else 0
                                     for i in self.edges for j in tile.edges])
                for i in range(4):
                    matches[i] += sum(matcharr[4 * i : 4 * i + 4])
                if (sum(matcharr) == 1):
                    self.next.append(tile)

        self.matches = matches

    def flipx(self):
        self.map = np.flip(self.map, axis=0)
        self.edges[0], self.edges[2] = self.edges[2], self.edges[0]
        for i in range(4):
            self.edges[i] = flip_value(self.edges[i])
        self.matches[0], self.matches[2] = self.matches[2], self.matches[0]
        return self

    def flipy(self):
        self.map = np.flip(self.map, axis=1)
        self.edges[1], self.edges[3] = self.edges[3], self.edges[1]
        for i in range(4):
            self.edges[i] = flip_value(self.edges[i])
        self.matches[1], self.matches[3] = self.matches[3], self.matches[1]
        return self

    def rotate(self, times):
        self.map = np.rot90(self.map, times, axes=(1, 0))
        for i in range(times):
            self.edges[0], self.edges[1:4] = self.edges[3], self.edges[0:3]
            self.matches[0], self.matches[1:4] = self.matches[3], self.matches[0:3]
        return self

    def orient_corner(self):
        while(self.matches[1] == 0 or self.matches[2] == 0):
            self.rotate(1)

def hash_edge(s) -> int:
    nr = 0
    for i in range(10):
        nr += 1 << i if s[i] else 0
    return nr

def flip_value(x) -> int:
    y = 0
    for i in range(10):
        if (x & 1 << i):
            y += 1 << (9 - i)
    return y

def get_corner(tiles):
    for tile in tiles:
        if (sum(tile.matches) == 2):
            tile.orient_corner()
            return tile

tiles = []
m = []
index = 0
for line in sys.stdin:
    if (line == '\n'):
        tiles.append(Tile(index, np.array(m)))
        m = []
    elif ("Tile" in line):
        index = int(line.split(" ")[1][:-2])
    else:
        m.append([1 if i == '#' else 0 for i in line[:-1]])

for tile in tiles:
    tile.calc_matches(tiles)

n = len(tiles)
l = int(math.sqrt(n))
print(n, l)

sorted = [get_corner(tiles)]
sorted[0].seen = 1

'''
tile.flipy()

print(tile.index)
print(tile.map)
print(tile.edges)
print(tile.matches)
'''
def print_tiles(tiles):
    for i, tile in enumerate(tiles):
        print(tile.index, end = " ")
        if ((i + 1) % l == 0):
            print()
    print("\n")

def recurse(sorted, poz):
    print_tiles(sorted)
    if (poz == n - 1):
        return sorted
    elif (poz < l):
        tomatch = sorted[poz - 1].edges[1]
        for tile in sorted[poz - 1].next:
            for i, edge in enumerate(tile.edges):
                if (tomatch == edge):
                    tile.rotate(3 - i)
                    sorted.append(tile)
                    recurse(sorted, poz + 1)
                    sorted.pop()
                if (tomatch == flip_value(edge)):
                    tile.rotate(3 - i)
                    tile.flipx()
                    sorted.append(tile)
                    recurse(sorted, poz + 1)
                    sorted.pop()
    else:
        tomatch = sorted[poz - l].edges[2]
        #print("->", sorted[poz - l].index, tomatch)
        for tile in sorted[poz - l].next:
            #print("-->", tile.index)
            for i, edge in enumerate(tile.edges):
                #print("---->", edge, flip_value(edge))
                if (tomatch == edge):
                    #print("noflip:", tile.edges, i)
                    tile.rotate(4 - i)
                    #print("ready:", tile.edges, i, flip_value(edge))
                    sorted.append(tile)
                    recurse(sorted, poz + 1)
                    sorted.pop()
                if (tomatch == flip_value(edge)):
                    #print("flip:", tile.edges, i, flip_value(edge))
                    tile.rotate(4 - i)
                    tile.flipy()
                    #print("ready:", tile.edges, i, flip_value(edge))
                    sorted.append(tile)
                    recurse(sorted, poz + 1)
                    sorted.pop()
recurse(sorted, 1)

'''
tile = tiles[3]
print(tile.index)
print(tile.map)
print(tile.edges)
print(tile.matches)

tile = tiles[0]
print(tile.index)
print(tile.map)
print(tile.edges)
print(tile.matches)

tile.flipy()
tile = tiles[0]
print(tile.index)
print(tile.map)
print(tile.edges)
print(tile.matches)
'''

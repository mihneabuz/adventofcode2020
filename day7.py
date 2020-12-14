import sys
from functools import lru_cache

test_code = {"lr": [1, "bw", 2, "my"], "do": [3, "bw", 4, "my"],
              "bw": [1, "sg"], "my": [2, "sg", 9, "fb"],
              "sg": [1, "dl", 2, "vp"], "dl": [3, "fb", 4, "db"],
              "vp": [5, "fb", 6, "db"], "fb": [], "db": []}

def test():
    for item in test_code:
        print(item, end = "")
        l = test_code[item]
        for i in range(0, len(l), 2):
            print(" ({} {}) ".format(l[i], l[i + 1]), end = "")
        print()


# Part I
color_code = {}
'''
for line in sys.stdin:
    bags = line[: -1].split("contain")
    inner = [string[3:] for string in
             bags[1][: - 1].replace("bags", "bag").split(",")]
    outer = bags[0][: -2]
    color_code.update({outer: inner})


l = ["shiny gold bag"]
i = 0
while (i < len(l)):
    color = l[i]
    for item in color_code:
        if (color in color_code[item] and item not in l):
            l.append(item)
    i += 1

print(len(l) - 1)
'''

# Part II
color_code = {}

@lru_cache(maxsize = 100)
def recursion(bag):
    if (len(color_code[bag]) == 0):
        return 0;
    else:
        s = 0
        for item in color_code[bag]:
            #print(item, color_code[bag][item], recursion(item))
            s += color_code[bag][item] * (recursion(item) + 1)
    return s

for line in sys.stdin:
    bags = line[: -1].split("contain")
    inner = bags[1][: - 1].replace("bags", "bag").split(",")
    if (inner[0] == " no other bag"):
        inner = {}
    else:
        inner = {string[3:] : int(string[1]) for string in inner}
    outer = bags[0][: -2]
    color_code.update({outer: inner})
    #print(outer, ":", inner)

start = "shiny gold bag"
print(recursion(start))

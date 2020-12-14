import sys

nr = 0

for line in sys.stdin:
    [rang, char, string] = line.split()
    string = list(string)
    char = char[0]
    rang = [int(i) for i in rang.split("-")]
    if (string[rang[0] - 1] == char and string[rang[1] - 1] != char or
        string[rang[0] - 1] != char and string[rang[1] - 1] == char):
        nr += 1

print(nr)

import sys

s = 0
nr = 0
ans = {chr(i) : 0 for i in range(ord('a'), ord('z') + 1)}
for line in sys.stdin:
    if (line == "\n"):
        s += sum([int(x / nr) for x in ans.values()])
        nr = 0
        ans = {chr(i) : 0 for i in range(ord('a'), ord('z') + 1)}
    else:
        nr += 1
        chars = list(line)[0 : -1]
        for c in chars:
            ans[c] += 1
print(s)
print(ans)

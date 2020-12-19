import sys
import re

rules = {}
words = []

for line in sys.stdin:
    if (line == '\n'):
        break
    line = line[: -1].split(": ")
    rules.update({int(line[0]): line[1]})

for line in sys.stdin:
    words.append(' ')
    words.append(line[: -1])
    words.append(' ')

words = "".join(words)

def gen_regex(rules, index, limit = 5):
    if (limit == 0):
        return ''

    rule = rules[index]

    if ('"' in rule):
       return rule[1]
    string = []

    if ('|' in rule):
        string.append('(')
        halves = rule.split('|')
        for i in halves[0].split():
            if (int(i) == index):
                limit -= 1
            string.append(gen_regex(rules, int(i), limit))
        string.append('|')
        for i in halves[1].split():
            if (int(i) == index):
                limit -= 1
            string.append(gen_regex(rules, int(i), limit))
        string.append(')')
    else:
        for i in rule.split():
            string.append(gen_regex(rules, int(i), limit))
    return "".join(string)

print(rules)
print(words)
regex = " " + gen_regex(rules, 0) + " "
print(regex)
print(len(re.findall(regex, words)))

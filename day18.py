import sys

index = 0
def read_eq(ops) -> list:
    l = []
    global index
    while(index < len(ops)):
        if (ops[index] == ")"):
            index += 1
            return l
        elif (ops[index] == "("):
            index += 1
            l.append(read_eq(ops))
        elif (ops[index] in ['+', '-', '*', '/']):
            l.append(ops[index])
            index += 1
        else:
            l.append(int(ops[index]))
            index += 1
    return l

def calculate(op1, op2, f):
    if (f == "+"):
        return op1 + op2
    if (f == "-"):
        return op1 - op2
    if (f == "*"):
        return op1 * op2
    if (f == "/"):
        return op1 / op2

def evaluate1(eq) -> int:
    if isinstance(eq, int):
        return eq

    op1 = 0
    op2 = 0
    f = ''

    if isinstance(eq[0], list):
        op1 = evaluate1(eq[0])
    else:
        op1 = eq[0]

    for item in eq[1:]:
        if isinstance(item, str):
            f = item
        else:
            op2 = evaluate1(item)
            op1 = calculate(op1, op2, f)
    return op1

def evaluate2(eq) -> int:
    if isinstance(eq, int):
        return eq

    op1 = 0
    op2 = 0
    f = ''
    rez = 0

    index = 0
    while (index < len(eq)):
        if isinstance(eq[index], str) and eq[index] in ['+', '-']:
            f = eq.pop(index)
            op1 = evaluate2(eq.pop(index - 1))
            op2 = evaluate2(eq[index - 1])
            rez = calculate(op1, op2, f)
            eq[index - 1] = rez
        elif isinstance(eq[index], list):
            eq[index] = evaluate2(eq[index])
        else:
            index += 1
    return evaluate1(eq)

s1 = 0
s2 = 0
for line in sys.stdin:
    eq = line[:-1].replace("(", "( ").replace(")", " )").split(" ")
    index = 0
    eq = read_eq(eq)
    s1 += evaluate1(eq)
    s2 += evaluate2(eq)

print(s1)
print(s2)

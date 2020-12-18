import sys

data = open(sys.argv[1]).readlines()

precedence = {
    '+': 3,
    '-': 2,
    '*': 2,
    '/': 3,
    '(': 0,
    ')': 9,
}

def shunting_yard(line):
    line = line.replace('(', ' ( ').replace(')', ' ) ')
    line = [x for x in line.strip().split(' ') if x]

    output = []
    operators = []
    for c in line:
        if (c in ['+','-','*','/']):
            while (operators):
                op = operators[-1]
                if (precedence[op] <= precedence[c]):
                    break
                if (op == '('):
                    break
                output.append(operators.pop())
            operators.append(c)
        elif (c == '('):
            operators.append(c)
        elif (c == ')'):
            while (operators):
                op = operators[-1]
                if (op == '('):
                    break
                output.append(operators.pop())
            if (operators and operators[-1] == '('):
                operators.pop()
        else: # Is number
            output.append(int(c))

    while (operators):
        output.append(operators.pop())
    return output

def calc(rpn):
    print(rpn)
    s = []
    while rpn:
        op = rpn.pop(0)
        if (isinstance(op, int)): 
            s.append(op)
        elif (op == '+'):
            s.append(s.pop() + s.pop())
        elif (op == '-'):
            s.append(s.pop() - s.pop())
        elif (op == '*'):
            s.append(s.pop() * s.pop())
        elif (op == '/'):
            s.append(s.pop() / s.pop())
    return s[-1]

total_sum = 0
for line in data:
    rpn = shunting_yard(line)
    v = calc(rpn)
    total_sum += v
    print(v)
print(total_sum)


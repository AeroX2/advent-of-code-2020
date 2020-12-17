import sys
import re

data = open(sys.argv[1]).readlines()
data = [x.strip() for x in data]


def new_mask(mask):
    one_mask = 0
    x_mask = 0
    for c in mask:
        if (c == '1'):
            one_mask |= 1
        if (c == 'X'):
            x_mask |= 1

        one_mask <<= 1
        x_mask <<= 1
    one_mask >>= 1
    x_mask >>= 1

    return (one_mask, x_mask)

mem = {}
for line in data:
    m = re.match(r'mask = (.+)', line)
    if (m):
        one_mask, x_mask = new_mask(m.group(1))

        continue

    m = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)

    addr = int(m.group(1))
    addr = (addr & ~one_mask) | one_mask
    addr = (addr & ~x_mask)

    val = int(m.group(2))

    x_length = len(bin(x_mask))-2
    x_count = bin(x_mask).count('1')
    for i in range(pow(2, x_count)):
        ni = i
        expand = 0

        for ii in range(x_length): 
            if ((x_mask >> ii) & 1):
                expand |= (ni & 1) << ii
                ni >>= 1

        mem[addr | expand] = val

print(sum(mem.values()))




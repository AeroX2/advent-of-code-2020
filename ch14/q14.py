import sys
import re

data = open(sys.argv[1]).readlines()
data = [x.strip() for x in data]


def new_mask(mask):
    and_mask = 0
    or_mask = 0
    for c in mask:
        if (c == '1' or c == '0'):
            and_mask |= 1
        if (c == '1'):
            or_mask |= 1

        and_mask <<= 1
        or_mask <<= 1
    and_mask >>= 1
    or_mask >>= 1

    return (and_mask, or_mask)

memory = {}
for line in data:
    m = re.match(r'mask = (.+)', line)
    if (m):
        and_mask, or_mask = new_mask(m.group(1))
        continue

    m = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)
    v = int(m.group(2))
    v = (v & ~and_mask) | (or_mask & and_mask)
    memory[m.group(1)] = v
    
print(sum(memory.values()))



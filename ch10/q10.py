import sys
from collections import Counter

data = open(sys.argv[1]).readlines()
data = [int(x) for x in data]
data = set(data)

max_joltage = max(data)
def charge(joltage_c, chain=[]):
    #print(len(chain))

    if (joltage_c >= max_joltage and
        joltage_c <= max_joltage+3 and
        len(chain) == len(data)):

        chain_o = [0]+chain[:-1], chain
        chain_o = [x[1]-x[0] for x in zip(*chain_o)]

        one = sum([x == 1 for x in chain_o])
        three = sum([x == 3 for x in chain_o]) + 1

        print(one * three)
        sys.exit()

    for i in range(1,4):
        joltage = joltage_c +i
        if (joltage not in data):
            continue
        if (charge(joltage, chain+[joltage])):
            break
    return False


charge(0)

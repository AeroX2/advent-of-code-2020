import sys
from collections import Counter

data = open(sys.argv[1]).readlines()
data = [int(x) for x in data]
data = set(data)

cache = {}
max_joltage = max(data)
def charge(joltage_c, chain=[]):
    if (joltage_c in cache):
        return cache[joltage_c]

    if (joltage_c >= max_joltage and
        joltage_c <= max_joltage+3):
        print(chain)
        return 1

    output = 0
    for i in range(1,4):
        joltage = joltage_c + i
        if (joltage not in data):
            continue
        output += charge(joltage, chain+[joltage])

    cache[joltage_c] = output
    return output

print(charge(0))

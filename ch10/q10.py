import sys
from collections import Counter

data = open(sys.argv[1]).readlines()
data = [int(x) for x in data]
data = set(data)

differences = Counter()
max_joltage = max(data)
def charge(joltage_c, chain=[]):
    print(chain)

    if (joltage_c > max_joltage and joltage_c <= max_joltage+3):
        return

    for i in range(1,4):
        joltage = joltage_c +i
        if (joltage not in data):
            continue
        differences[i] += 1
        charge(joltage, chain+[joltage])

charge(0)
print(differences)

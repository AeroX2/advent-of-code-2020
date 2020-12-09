import sys

data = open(sys.argv[1]).readlines()
data = [int(x) for x in data]

preamble_i = int(sys.argv[2])
preamble = data[:preamble_i]

def check(preamble, ex):
    for i,x in enumerate(preamble):
        for y in preamble[i:]:
            if (x + y == ex):
                return True
    return False

for x in data[preamble_i:]:
    if (not check(preamble, x)):
        print(x)
        break
    preamble = preamble[1:] + [x]

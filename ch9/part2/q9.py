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
        invalid_number = x
        break
    preamble = preamble[1:] + [x]

low = 0
high = 0
total = 0
while True:
    if (total == invalid_number):
        print(low, high)

        a = min(data[low:high])
        b = max(data[low:high])
        print(a,b)
        print(a+b)

        break

    while (total < invalid_number):
        total += data[high]
        high += 1

    while (total > invalid_number):
        total -= data[low]
        low += 1
        



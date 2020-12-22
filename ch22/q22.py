import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

p1 = [int(x) for x in data[0].split('\n')[1:]]
p2 = [int(x) for x in data[1].split('\n')[1:]]

while (len(p1) and len(p2)):
    p1c = p1.pop(0)
    p2c = p2.pop(0)

    if (p1c > p2c):
        p1.extend([p1c, p2c])
    elif (p2c > p1c):
        p2.extend([p2c, p1c])
    else:
        print('wtf')
        sys.exit()

winner = p1 if len(p1) > 0 else p2

print(winner)

total = 0
for i,card in enumerate(reversed(winner)):
    total += (i+1) * card
print(total)
    

import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

p1 = [int(x) for x in data[0].split('\n')[1:]]
p2 = [int(x) for x in data[1].split('\n')[1:]]

# Returns True if player 1 wins
def helper(p1, p2, depth=0):
    cache = set()
    while (len(p1) and len(p2)):
        s = (tuple(p1),tuple(p2))
        if (s in cache):
            return True
        cache.add(s)

        p1c = p1.pop(0)
        p2c = p2.pop(0)

        winner_p1 = p1c > p2c
        if (p1c <= len(p1) and p2c <= len(p2)):
            winner_p1 = helper(p1[:p1c], p2[:p2c], depth+1)

        if (winner_p1):
            p1.extend([p1c, p2c])
        else:
            p2.extend([p2c, p1c])

    return len(p1) > 0

helper(p1, p2)
winner = p1 if len(p1) > 0 else p2

total = 0
for i,card in enumerate(reversed(winner)):
    total += (i+1) * card
print(total)
    

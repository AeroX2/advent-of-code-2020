import sys

data = open(sys.argv[1]).readlines()

sled_ox = 3
#sled_oy = 1

sled_x = 0
#sled_y = 0

trees = 0
for line in data[1:]:
    line = line.strip()

    sled_x += sled_ox
    if (line[sled_x % len(line)] == '#'):
        trees += 1
print(trees)


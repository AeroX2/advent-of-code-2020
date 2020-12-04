import sys

data = open(sys.argv[1]).readlines()

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

slope_trees = []
for slope in slopes:
    sled_x = 0
    sled_ox = slope[0]
    trees = 0
    for linei in range(slope[1],len(data),slope[1]):
        line = data[linei].strip()

        sled_x += sled_ox
        if (line[sled_x % len(line)] == '#'):
            trees += 1
    slope_trees.append(trees)

print(slope_trees)
output = 1
for v in slope_trees:
    output *= v
print(output)

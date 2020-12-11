import sys
import copy

data = open(sys.argv[1]).read().strip().replace('\n','')
l = int(sys.argv[2])
data = [data[i:i+l] for i in range(0,len(data),l)]
data = [list(x) for x in data]

directions = [
    (0,1),
    (1,0),
    (-1,0),
    (0,-1),
    (-1,-1),
    (1,1),
    (1,-1),
    (-1,1),
]
def check(x,y,char):
    count = 0
    for direction in directions:
        dx = x
        dy = y

        while True:
            dx += direction[0]
            dy += direction[1]

            if (dx < 0 or dx >= len(data[0])):
                break
            if (dy < 0 or dy >= len(data)):
                break
        
            #print(dx,dy,len(data),len(data[0]),len(data[22]))
            if (data[dy][dx] == char):
                count += 1
                break
            elif (data[dy][dx] != '.'):
                break

    return count

while True:
    changed = False
    new_data = copy.deepcopy(data)
    for y,line in enumerate(data):
        for x,char in enumerate(line):
            if (char == 'L' and check(x,y,'#') == 0):
                new_data[y][x] = '#'
                changed = True
            elif (char == '#' and check(x,y,'#') >= 5):
                new_data[y][x] = 'L'
                changed = True
    data = new_data
    if (not changed):
        break

    for line in data:
        print(''.join(line))
    print()

count = 0
for y,line in enumerate(data):
    for x,char in enumerate(line):
        if (char == '#'):
            count += 1
print(count)


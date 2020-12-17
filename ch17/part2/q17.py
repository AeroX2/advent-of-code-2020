import sys

data = open(sys.argv[1]).read().strip()
data = [list(x) for x in data.split('\n')]

print(data)

cube = {}
for y,v in enumerate(data):
    h = len(v)//2
    for x,v2 in enumerate(v):
        cube[(x-h,y-h,0,0)] = v2
print(cube)

width = len(data[0])
height = width
depth = 0
hyper = 0
print('Dimensions')
print((width, height, depth, hyper))

def check_active(pos):
    active_count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    if (x == 0 and y == 0 and z == 0 and w == 0):
                        continue
                    new_pos = (pos[0]+x, pos[1]+y, pos[2]+z, pos[3]+w)
                    active_count += 1 if cube.get(new_pos, '.') == '#' else 0
    return active_count

for i in range(6):
    #for z in range(-depth,depth+1):
    #    print('z =',z)
    #    for y in range(-height,height+1):
    #        for x in range(-width,width+1):
    #            print(cube.get((x,y,z),'.'),end='')
    #        print()

    width += 1
    height += 1
    depth += 1
    hyper += 1

    modify_list = []
    for x in range(-width,width+1):
        for y in range(-height,height+1):
            for z in range(-depth,depth+1):
                for w in range(-hyper,hyper+1):
                    is_active = cube.get((x,y,z,w), '.') == '#'
                    active_count = check_active((x,y,z,w))
                    if (is_active and not (active_count == 2 or active_count == 3)):
                        modify_list.append((x,y,z,w,'.'))
                    elif (not is_active and (active_count == 3)):
                        modify_list.append((x,y,z,w,'#'))

    for x,y,z,w,v in modify_list:
        cube[(x,y,z,w)] = v

print(len([x for x in cube.values() if x == '#']))
 

import sys
from math import cos,sin,radians

data = open(sys.argv[1]).readlines()

ship_p = [0,0]
ship_w = [10,1]
ship_d = 0

for line in data:
    op = line[0]
    am = int(line[1:])

    if (op == 'N'):
        ship_w[1] += am
    elif (op == 'E'):
        ship_w[0] += am
    elif (op == 'S'):
        ship_w[1] -= am
    elif (op == 'W'):
        ship_w[0] -= am
    elif (op == 'L'):
        r = radians(am)
        ship_w = [ship_w[0] * cos(r) - ship_w[1] * sin(r),
                  ship_w[0] * sin(r) + ship_w[1] * cos(r)]
    elif (op == 'R'):
        r = -radians(am)
        ship_w = [ship_w[0] * cos(r) - ship_w[1] * sin(r),
                  ship_w[0] * sin(r) + ship_w[1] * cos(r)]
    elif (op == 'F'):
        ship_p = [ship_p[0] + ship_w[0] * am, ship_p[1] + ship_w[1] * am]
    print(ship_p, ship_w)

print(abs(ship_p[0]) + abs(ship_p[1]))






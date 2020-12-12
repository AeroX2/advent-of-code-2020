import sys

data = open(sys.argv[1]).readlines()

ship_p = [0,0]
ship_d = 0
for line in data:
    op = line[0]
    am = int(line[1:])

    if (op == 'N'):
        ship_p[1] += am
    elif (op == 'E'):
        ship_p[0] += am
    elif (op == 'S'):
        ship_p[1] -= am
    elif (op == 'W'):
        ship_p[0] -= am
    elif (op == 'L'):
        ship_d = (ship_d - am) % 360
    elif (op == 'R'):
        ship_d = (ship_d + am) % 360
    elif (op == 'F'):
        d = ship_d // 90

        if (d == 0):
            ship_p[0] += am
        elif (d == 1):
            ship_p[1] -= am
        elif (d == 2):
            ship_p[0] -= am
        elif (d == 3):
            ship_p[1] += am

print(abs(ship_p[0]) + abs(ship_p[1]))






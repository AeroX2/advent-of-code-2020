import sys

data = open(sys.argv[1]).readlines()

schedule = [x for x in data[1].split(',')]

for i,time in enumerate(schedule):
    if (time == 'x'):
        continue
    time = int(time)



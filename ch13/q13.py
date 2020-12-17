import sys

data = open(sys.argv[1]).readlines()

earliest = int(data[0])
schedule = [int(x) for x in data[1].split(',') if x != 'x']

min_bus = None
min_time = None
for time in schedule:
    closest_time = (((earliest // time) + 1) * time) - earliest

    if (min_time is None or closest_time < min_time):
        min_bus = time
        min_time = closest_time

print(min_bus, min_time)
print(min_time * min_bus)


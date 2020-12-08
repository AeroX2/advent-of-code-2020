import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

print(data)

flatten = lambda t: [item for sublist in t for item in sublist]

data = [x.split('\n') for x in data]

print(data)

data = [[set(x) for x in y] for y in data]

print(data)

data = [set.intersection(*y) for y in data]

print(data)

data = [len(y) for y in data]

print(data)
print(sum(data))


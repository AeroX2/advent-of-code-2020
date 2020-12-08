import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

print(data)

flatten = lambda t: [item for sublist in t for item in sublist]

data = [set(flatten(x.split('\n'))) for x in data]

print(data)

data = [len(x) for x in data]

print(data)
print(sum(data))



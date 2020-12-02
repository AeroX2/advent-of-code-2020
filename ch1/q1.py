
import sys

data = open(sys.argv[1]).readlines();
data = list(map(lambda x: int(x), data))

for i in data:
    for ii in data:
        if (i + ii == 2020):
            print(i, ii)
            print(i * ii)

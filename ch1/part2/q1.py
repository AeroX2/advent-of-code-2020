
import sys

data = open(sys.argv[1]).readlines();
data = list(map(lambda x: int(x), data))

for i in data:
    for ii in data:
        for iii in data:
            if (i + ii + iii == 2020):
                print(i, ii, iii)
                print(i * ii * iii)

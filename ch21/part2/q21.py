import re
import sys

data = open(sys.argv[1]).readlines()

all_ingredients = []
allegens = {}
for line in data:
    m = re.match(r'^(.+) \(contains (.+)\)$', line)
    ingredients = set(m.group(1).split(' '))
    all_ingredients.extend(ingredients)

    for allegen in m.group(2).split(', '):
        if (allegen in allegens):
            allegens[allegen].append(ingredients)
        else:
            allegens[allegen] = [ingredients]

valids = set()
for allegen in allegens:
    valid = allegens[allegen][0].intersection(*allegens[allegen])
    valids.update(valid)

for allegen in allegens:
    allegens[allegen] = valids.intersection(*allegens[allegen])
print(allegens)

while True:
    final_list = { allegen:allegens[allegen] for allegen in allegens if len(allegens[allegen]) == 1 }
    if (len(final_list) == len(allegens)):
        print(final_list)
        break

    for allegen in allegens:
        if (allegen not in final_list):
            allegens[allegen] = allegens[allegen].difference(*final_list.values())


print(','.join([[*final_list[x]][0] for x in sorted(final_list)]))


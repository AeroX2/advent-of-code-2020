import re
import sys

data = open(sys.argv[1]).readlines()

all_ingredients = []
allegens = {}
for line in data:
    m = re.match(r'^(.+) \(contains (.+)\)$', line)
    print(m.groups())
    ingredients = set(m.group(1).split(' '))
    all_ingredients.extend(ingredients)

    for allegen in m.group(2).split(', '):
        if (allegen in allegens):
            allegens[allegen].append(ingredients)
        else:
            allegens[allegen] = [ingredients]

invalids = set()
for allegen in allegens:
    invalid = allegens[allegen][0].intersection(*allegens[allegen])
    invalids.update(invalid)

total = 0
for ingredient in set(all_ingredients):
    if (ingredient not in invalids):
        total += all_ingredients.count(ingredient)
print(total)






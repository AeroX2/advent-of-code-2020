import re
import sys

data = open(sys.argv[1]).readlines()

class Bag:
    def __init__(self, name):
        self.name = name
        self.bags = []

    def __repr__(self):
        return "Name: %s, Bags: %s" % (self.name,self.bags)

    def __str__(self):
        return "Name: %s, Bags: %s" % (self.name,self.bags)

bags = {}
for line in data:
    match = re.match(r'(.+) bags contain ((no other bags)|(.+)).', line)

    bag_name = match.group(1)
    if (bag_name in bags):
        parent_bag = bags[bag_name]
    else:
        parent_bag = Bag(bag_name)
        bags[bag_name] = parent_bag


    if (match.group(2) == 'no other bags'):
        continue

    containing_bags = []
    for group in re.findall(r'([0-9]+) (.+?) bags?,? ?', match.group(2)):
        count = int(group[0])
        bag_name = group[1]
        containing_bags.append((bag_name, count))
    parent_bag.bags = containing_bags


def travel(parent):
    for bag in parent.bags:
        #print(bag)

        bag, count = bag
        if (bag == 'shiny gold'):
            return True

        if (travel(bags[bag])):
            return True
    return False

#print(bags)
#print(len(bags))
#print([travel(bags[bag]) for bag in bags])
print(sum([travel(bags[bag]) for bag in bags]))

#print(travel(bags['dark red']))


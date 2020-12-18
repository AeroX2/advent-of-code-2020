import sys
import re

data = open(sys.argv[1]).read().strip().split('\n\n')

fields_raw = data[0].split('\n')
your_ticket = data[1].split('\n')[1]
other_tickets = [map(int,x.split(',')) for x in data[2].split('\n')[1:]]

fields = []
for field in fields_raw:
    m = re.match(r'(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', field)
    l1 = int(m.group(2))
    h1 = int(m.group(3))
    l2 = int(m.group(4))
    h2 = int(m.group(5))

    fields.append((l1,h1,l2,h2))
print(fields)

def invalid_fields(ticket):
    return [v for v in ticket if not check_value(v)]

def check_value(x):
    for f in fields:
        l1,h1,l2,h2 = f
        if ((x>=l1 and x<=h1) or (x>=l2 and x<=h2)):
            return True
    return False

invalid_sum = 0
for ticket in other_tickets:
    invalid_sum += sum(invalid_fields(ticket))
print(invalid_sum)





import sys
import re

data = open(sys.argv[1]).read().strip().split('\n\n')

fields_raw = data[0].split('\n')
six_fields = [i for i,x in enumerate(fields_raw) if 'departure' in x]

your_ticket = [int(x) for x in data[1].split('\n')[1].split(',')]
other_tickets = [list(map(int,x.split(','))) for x in data[2].split('\n')[1:]]

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
    return [v for v in ticket if not any([check_value(f,v) for f in fields])]

def check_value(f,x):
    l1,h1,l2,h2 = f
    return ((x>=l1 and x<=h1) or (x>=l2 and x<=h2))

other_tickets = list(filter(lambda x: len(invalid_fields(x)) == 0, other_tickets))
print(len(other_tickets))

valid_columns = [[x for x in range(len(fields))] for _ in fields]
for ticket in other_tickets:
    for i,v in enumerate(ticket):
        invalid = []
        for fi,f in enumerate(valid_columns[i]):
            if (not check_value(fields[f], v)):
                invalid.append(fi)

        for x in invalid:
            del valid_columns[i][x]

while any([len(x) != 1 for x in valid_columns]):
    for i,vc in enumerate(valid_columns):
        if (len(vc) != 1):
            continue

        for ii,vc2 in enumerate(valid_columns[:i]+valid_columns[i+1:]):
            if (vc[0] in vc2):
                vc2.remove(vc[0])
    
print(valid_columns)
print(six_fields)
print(your_ticket)

mul_sum = 1
for i,v in enumerate(your_ticket):
    correct_column = valid_columns[i][0]
    if (correct_column in six_fields):
        mul_sum *= int(v)
print(mul_sum)





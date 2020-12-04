import re
import sys

data = open(sys.argv[1]).read().split('\n\n')
data = map(lambda x: re.split(r'[\n ]', x), data)

valid_parameters = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]


valid_passports = 0
for passport in data:
    valid = 0
    for field in passport:
        if (len(field) <= 0):
            continue
        print(field)
        parameter, value = field.split(':')

        if (parameter in valid_parameters):
            valid += 1
    if (valid >= 7):
        print(passport)
        valid_passports += 1
print(valid_passports)

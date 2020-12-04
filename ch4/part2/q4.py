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

def check_param_valid(parameter, value):
    try:
        if (parameter == 'byr'):
            vi = int(value)
            return len(value) == 4 and vi >= 1920 and vi <= 2002
        elif (parameter == 'iyr'):
            vi = int(value)
            return len(value) == 4 and vi >= 2010 and vi <= 2020
        elif (parameter == 'eyr'):
            vi = int(value)
            return len(value) == 4 and vi >= 2020 and vi <= 2030
        elif (parameter == 'hgt'):
            vi = int(value[:-2])
            type = value[-2:]
            if (type == 'cm'):
                return vi >= 150 and vi <= 193
            elif (type == 'in'):
                return vi >= 59 and vi <= 76
            else:
                return False
        elif (parameter == 'hcl'):
            return re.match(r'#[0-9a-f]{6}', value)
        elif (parameter == 'ecl'):
            return value in ['amb','blu','brn','gry','grn','hzl','oth']
        elif (parameter == 'pid'):
            int(value)
            return len(value) == 9
    except:
        return False



valid_passports = 0
for passport in data:
    valid = 0
    for field in passport:
        if (len(field) <= 0):
            continue
        print(field)
        parameter, value = field.split(':')

        if (parameter in valid_parameters 
            and check_param_valid(parameter, value)):
            valid += 1

    if (valid >= 7):
        print(passport)
        valid_passports += 1
print(valid_passports)

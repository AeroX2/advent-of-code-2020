import sys

data = open(sys.argv[1]).readlines()

valid = 0
for line in data:
    count, char, password = line.split(" ")
    char = char[0]
    
    low,high = count.split("-")
    low = int(low)
    high = int(high)

    pass_1 = password[low-1] == char
    pass_2 = password[high-1] == char
    if (pass_1 ^ pass_2 == True):
        valid += 1
print(valid)

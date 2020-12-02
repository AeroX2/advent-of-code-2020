import sys

data = open(sys.argv[1]).readlines()

valid = 0
for line in data:
    count, char, password = line.split(" ")
    char = char[0]
    
    low,high = count.split("-")
    low = int(low)
    high = int(high)

    pass_count = password.count(char) 
    if (pass_count >= low and pass_count <= high):
        valid += 1
print(valid)

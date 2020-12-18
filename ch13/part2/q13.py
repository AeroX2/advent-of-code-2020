import sys
from functools import reduce

#Borrowed from http://www.rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

data = open(sys.argv[1]).readlines()
schedule = [(i,int(x)) for i,x in enumerate(data[1].split(',')) if x != 'x']

n = [x[1] for x in schedule]
a = [x[1]-x[0] for x in schedule]
print(chinese_remainder(n, a))



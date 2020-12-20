import re
import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

rules_raw = data[0].split('\n')
lines_raw = data[1].split('\n')

rules = {}
for line in rules_raw:
    m = re.match('([0-9]+): (.+)', line)
    rules[m.group(1)] = m.group(2)

print(rules)
    
def helper(curr_rule):
    m = re.match(r'"([a-z])"', curr_rule)
    if (m):
        return m.group(1)

    m = re.match(r'(.+) \| (.+)', curr_rule)
    if (m):
        group1 = m.group(1).split(' ')
        group2 = m.group(2).split(' ')
        a = ''.join([helper(rules[x]) for x in group1])
        b = ''.join([helper(rules[x]) for x in group2])
        return '((%s)|(%s))' % (a,b)

    group = curr_rule.split(' ')
    a = ''.join([helper(rules[x]) for x in group])
    return a

single_rule = helper(rules['0'])
single_rule = '^'+single_rule+'$'

print(sum([1 for line in lines_raw if re.match(single_rule, line)]))


import re
import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

rules_raw = data[0].split('\n')
lines_raw = data[1].split('\n')

rules = {}
for line in rules_raw:
    m = re.match('([0-9]+): (.+)', line.strip())
    rules[m.group(1)] = m.group(2)

visited = {}
def helper(rule_name):
    curr_rule = rules[rule_name]

    m = re.match(r'"([a-z])"', curr_rule)
    if (m):
        return m.group(1)

    if (rule_name in visited):
        return visited[rule_name]
    #visited[rule_name] = '(?P<%s>)' % (chr(int(rule_name)+ord('a')),)

    m = re.match(r'(.+) \| (.+)', curr_rule)
    if (m):
        group1 = m.group(1).split(' ')
        group2 = m.group(2).split(' ')

        a = [helper(x) for x in group1]
        if (rule_name == '8'):
            return '(%s)+' % (a[0],)
        if (rule_name == '11'):
            return '(?P<a>(%s)(?&a)?(%s))' % (a[0],a[1])

        b = ''.join([helper(x) for x in group2])

        s = '(%s|%s)' % (''.join(a),b)
        visited[rule_name] = s
        return s

    group = curr_rule.split(' ')
    a = ''.join([helper(x) for x in group])
    visited[rule_name] = a
    return a

single_rule = helper('0')
single_rule = '^'+single_rule+'$'
print(single_rule)

import regex as reg
print(sum([1 for line in lines_raw if reg.match(single_rule, line)]))


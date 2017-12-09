#!/ubr/bin/env python3
#-*- coding: utf-8 -*-

with open('day9.input') as f:
    s = f.read()

m = [0, 0, 0]
res1, res2 = 0, 0
parse = lambda m: {
    '!': not m[0] and (1, 0, 0),
    '<': not sum(m[:2]) and (0, 1, 0),
    '>': not m[0] and m[1] and (0, -1, 0),
    '{': not sum(m[:2]) and (0, 0, 1),
    '}': not sum(m[:2]) and m[2] and (0, 0, -1),
}  
for c in s:
    p = parse(m).get(c) or (m[0] and -1 or 0, 0, 0)
    res1 += p[2] == -1 and m[2]
    res2 += m[1] and not p[1] and not p[0] and 1
    m = [mi + p[i] for i, mi in enumerate(m)]

print("Solutions: [{}] [{}]".format(res1, res2))


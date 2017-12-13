#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day13.input') as f:
    s = dict((int(n) for n in l.strip().split(': ')) for l in f.readlines())

run = lambda s, d: sum((i in s and (i + d) % ((s[i] - 1) * 2) == 0) and
                       ((i + d) * s[i]) for i in range(max(s.keys()) + 1))
r1, r2, c = run(s, 0), -1, 1
while c != 0:
    r2, c = r2 + 1, run(s, r2 + 1)

print("Solutions: [{}] [{}]".format(r1, r2))

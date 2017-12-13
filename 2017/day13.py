#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day13.input') as f:
    s = dict((int(n) for n in l.strip().split(': ')) for l in f.readlines())

def run(s, d):
    return sum((i in s and (i + d) % ((s[i] - 1) * 2) == 0) and
               ((i + d) * s[i]) for i in range(max(s.keys()) + 1))

r = [run(s, 0), (-1, -1)]
while r[1][1] != 0:
    r[1] = r[1][0] + 1, run(s, r[1][0] + 1)

print("Solutions: [{}] [{}]".format(*r))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

parse = re.compile(r"^([0-9]+): ([0-9]+)$")

s = {}
with open('day13.input') as f:
    for l in f.readlines():
        m = parse.match(l)
        s[int(m.group(1))] = int(m.group(2))

def run(s, d):
    return sum((i in s and (i + d) % ((s[i] - 1) * 2) == 0) and
               ((i + d) * s[i]) for i in range(max(s.keys()) + 1))

r = [run(s, 0), 0]
while True:
    if run(s, r[1]) == 0:
        break
    r[1] += 1

print("Solutions: [{}] [{}]".format(*r))

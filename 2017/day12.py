#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

parse = re.compile(r"^([0-9]+) <-> (.*)$")

s = {}
with open('day12.input') as f:
    for l in f.readlines():
        m = parse.match(l)
        s[int(m.group(1))] = [
            int(e) for e in m.group(2).split(', ')]

def walk(s, prog, count, bp):
    bp.add(prog)
    for p in set(s[prog]) - bp:
        bp.update(walk(s, p, count, bp))
    return bp

groups = []
for p in s.keys():
    if p not in [e for g in groups for e in g]:
        groups.append(walk(s, p, 0, set()))

print("Solutions: [{}] [{}]".format(len(groups[0]), len(groups)))

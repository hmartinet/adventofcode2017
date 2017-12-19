#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

parse = re.compile(r"^([0-9]+) <-> (.*)$")


def walk(s, prog, group):
    group |= {prog}
    for p in s[prog] - group:
        group |= walk(s, p, group)
    return group


def solve(din):
    s = {}
    for l in din.readlines():
        m = parse.match(l)
        s[int(m.group(1))] = {
            int(e) for e in m.group(2).split(', ')}

    groups, keys = [], set()
    for p in filter(lambda k: k not in keys, s.keys()):
        groups.append(walk(s, p, set()))
        keys |= groups[-1]

    return len(groups[0]), len(groups)

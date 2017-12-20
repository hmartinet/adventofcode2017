#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from recordclass import recordclass

Part = recordclass('Attrs', 'p v a')
V = recordclass('Vector', 'x y z')
parser = re.compile(r'p=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, '
                    r'v=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, '
                    r'a=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)')


def tick(parts):
    c = None
    for i, p in enumerate(parts):
        p.v.x += p.a.x
        p.v.y += p.a.y
        p.v.z += p.a.z
        p.p.x += p.v.x
        p.p.y += p.v.y
        p.p.z += p.v.z
        print((p, abs(p.p.x) + abs(p.p.y) + abs(p.p.z)))
        if not c or abs(p.p.x) + abs(p.p.y) + abs(p.p.z) < c[1]:
            c = i, abs(p.p.x) + abs(p.p.y) + abs(p.p.z)
    return c


def solve(din):
    parts = []
    for l in din.readlines():
        g = parser.match(l).groups()
        parts.append(Part(
            V(*[int(v) for v in g[0:3]]),
            V(*[int(v) for v in g[3:6]]),
            V(*[int(v) for v in g[6:9]])))

    c = None
    for i, p in enumerate(parts):
        print((p, abs(p.p.x) + abs(p.p.y) + abs(p.p.z)))
        if not c or abs(p.p.x) + abs(p.p.y) + abs(p.p.z) < c[1]:
            c = i, abs(p.p.x) + abs(p.p.y) + abs(p.p.z)
    for _ in range(4):
        print('-')
        cl = tick(parts)
        if not c or cl[1] < c[1]:
            c = cl

    return c, 1

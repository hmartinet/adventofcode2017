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


def add(v1, v2):
    return V(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


def sub(v1, v2):
    return V(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)


def divide(v1, v2):
    if v1.x / v2.x == v1.y / v2.y == v1.z / v2.z:
        return v1.x / v2.x
    else:
        raise


def collide(p1, p2):
    return divide(sub(p2.p, p1.p), add(p1.v, p2.v))


def solve(din):
    parts = []
    for l in din.readlines():
        g = parser.match(l).groups()
        parts.append(Part(
            V(*[int(v) for v in g[0:3]]),
            V(*[int(v) for v in g[3:6]]),
            V(*[int(v) for v in g[6:9]])))

    collisions = {}
    for i, p1 in enumerate(parts):
        for p2 in parts[i + 1:]:
            try:
                n = collide(p1, p2)
                collisions[n] = collisions.get(n, []) + [(p1, p2)]
            except Exception:
                pass

    sparts = parts[:]
    for n in sorted(collisions.keys()):
        for pair in collisions[n]:
            if pair[0] in sparts and pair[1] in sparts:
                print(pair)
                sparts.remove(pair[0])
                sparts.remove(pair[1])

    return 1, len(sparts)

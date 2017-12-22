#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from recordclass import recordclass
from math import sqrt
import itertools as it

Part = recordclass('Attrs', 'p v a')
V = recordclass('Vector', 'x y z')
Eq = recordclass('Equation', 'a b c')
parser = re.compile(r'p=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, '
                    r'v=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, '
                    r'a=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)')


def equation(p1, p2, d):
    a = .5 * (p1.a[d] - p2.a[d])
    return Eq(a, p1.v[d] - p2.v[d] + a, p1.p[d] - p2.p[d])


def eq(f1, f2):
    return abs(f1 - f2) < 0.00001


def rnd(f):
    return round(f, 5)


def collide(p1, p2):
    r = []
    for d in range(3):
        if eq(p1.a[d], p2.a[d]):
            if eq(p1.v[d], p2.v[d]):
                if not eq(p1.p[d], p2.p[d]):
                    return None
            else:
                r.append({rnd((p1.p[d] - p2.p[d]) / (p1.v[d] - p2.v[d]))})
            continue
        e = equation(p1, p2, d)
        delta = e.b ** 2 - 4 * e.a * e.c
        if delta < 0:
            return None
        sd = sqrt(delta)
        r.append({rnd((-e.b + sd) / (2 * e.a)), rnd((-e.b - sd) / (2 * e.a))})

    n = tuple(filter(lambda x: x >= 0, set.intersection(*r)))
    return min(n) if n else None


def solve(din):
    parts = []
    for l in din.readlines():
        g = parser.match(l).groups()
        parts.append(Part(
            V(*[int(v) for v in g[0:3]]),
            V(*[int(v) for v in g[3:6]]),
            V(*[int(v) for v in g[6:9]])))

    collisions = {}
    for p1, p2 in it.combinations(parts, 2):
        n = collide(p1, p2)
        if n is not None:
            collisions[n] = collisions.get(n, []) + [(repr(p1), repr(p2))]

    print(sorted(collisions.keys()))

    sparts = set(repr(p) for p in parts)
    for n in sorted(collisions.keys()):
        tr = set()
        for pair in collisions[n]:
            if len(sparts & set(pair)) == 2:
                tr |= set(pair)
        sparts -= tr

    return 1, len(sparts)

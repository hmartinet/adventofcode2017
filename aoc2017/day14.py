#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
from collections import namedtuple
from aoclib import knot

Point = namedtuple('Point', 'x y')

with open('input/day14') as f:
    inpt = f.read().strip()


def adjoin(p1, p2):
    return (-1 <= p1.x - p2.x <= 1 and p1.y == p2.y or
            p1.x == p2.x and -1 <= p1.y - p2.y <= 1)


def adjoins(pts, p):
    return any(adjoin(pi, p) for pi in pts)


def regions(data):
    regions = []
    pts = [Point(x, y)
           for y, row in enumerate(data)
           for x, value in enumerate(row) if value == '1']
    for p in pts:
        adjr = [r for r in regions if adjoins(r, p)]
        if adjr:
            adjr[0].add(p)
            if len(adjr) > 1:
                regions[:] = [r for r in regions if r not in adjr]
                regions.append(reduce(set.union, adjr))
        else:
            regions.append(set([p]))
    return regions


data = [knot.bstr("{}-{}".format(inpt, i), 128) for i in range(128)]

print("Solutions: [{}] [{}]".format(
    sum(int(b) for h in data for b in h),
    len(regions(data))))

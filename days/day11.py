#!/usr/bin/env python3
# -*- coding: utf-8 -*-

coord = {'n': (2, 0), 'ne': (1, -1), 'se': (-1, -1),
         's': (-2, 0), 'sw': (-1, 1), 'nw': (1, 1)}


def distance(c):
    x, y = tuple(abs(c[i]) for i in range(2))
    return y + max(0, (x - y) // 2)


def solve(din):
    path = din.read().strip().split(',')
    md = 0
    c = 0, 0
    for step in path:
        c = tuple(c[i] + coord[step][i] for i in range(2))
        md = max(md, distance(c))

    return distance(c), md

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
from copy import deepcopy

V = namedtuple('Vector', 'x y')


def rules(state, dr, mode):
    l, r, b = V(dr.y, -dr.x), V(-dr.y, dr.x), V(-dr.x, -dr.y)
    return ({'.': (l, '#'), '#': (r, '.')},
            {'.': (l, 'W'), '#': (r, 'F'), 'F': (b, '.'), 'W': (dr, '#')}
            )[mode][state]


def solve_for(grid, iters, mode):
    g = deepcopy(grid)
    cur = V(len(g) // 2, len(g[0]) // 2)
    dr = V(0, -1)
    count = 0

    for _ in range(iters):
        state = g[cur.y][cur.x]

        dr, g[cur.y][cur.x] = rules(state, dr, mode)
        count += g[cur.y][cur.x] == '#'
        cur = V(cur.x + dr.x, cur.y + dr.y)

        if cur.y == -1:
            g.insert(0, ['.'] * len(g[0]))
            cur = V(cur.x, cur.y + 1)
        elif cur.y == len(g):
            g.append(['.'] * len(g[0]))
        elif cur.x == -1:
            g = [['.'] + l for l in g]
            cur = V(cur.x + 1, cur.y)
        elif cur.x == len(g[0]):
            g = [l + ['.'] for l in g]

    return count


def parse(din):
    return [list(l.strip()) for l in din.readlines()]


def solve(din):
    grid = parse(din)
    return solve_for(grid, 10000, 0), solve_for(grid, 10000000, 1)

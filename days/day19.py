#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

V = namedtuple('Vector', 'x y')
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def solve(din):
    level = list(din)
    r = ['', 0]

    def get(v):
        return level[v.x][v.y]

    def add(v, d):
        return V(v.x + d.x, v.y + d.y)

    for i, c in enumerate(level[0]):
        if c == '|':
            cr, dr, dc = V(0, i), V(1, 0), '|'
            break

    while True:
        if get(cr) not in ('|', '-'):
            if get(cr) == '+' and not get(add(cr, dr)) in letters + [dc]:
                left, right = V(-dr.y, dr.x), V(dr.y, -dr.x)
                turn = letters + ['|' if dc == '-' else '-']
                dr = left if get(add(cr, left)) in turn else right
                dc = '|' if dc == '-' else '-'
            elif get(cr) in letters:
                r[0] += get(cr)
            else:
                break
        cr = add(cr, dr)
        r[1] += 1

    return r

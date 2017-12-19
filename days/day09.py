#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parser(m):
    return {'!': not m[0] and (1, 0, 0),
            '<': not sum(m[:2]) and (0, 1, 0),
            '>': not m[0] and m[1] and (0, -1, 0),
            '{': not sum(m[:2]) and (0, 0, 1),
            '}': not sum(m[:2]) and m[2] and (0, 0, -1)}


def solve(din):
    m = 0, 0, 0
    res = 0, 0

    for c in din.read():
        p = parser(m).get(c) or (m[0] and -1 or 0, 0, 0)
        res = (res[0] + (p[2] == -1 and m[2]),
               res[1] + (m[1] and not p[1] and not p[0] and 1))
        m = tuple([m[i] + p[i] for i in range(3)])

    return res

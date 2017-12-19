#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def run(s, d):
    return sum((i + d) % (2 * (r - 1)) == 0 and (i + d) * r for i, r in s)


def solve(din):
    s = [tuple(int(n) for n in l.strip().split(': ')) for l in din.readlines()]
    r1, r2, c = run(s, 0), 0, 1
    while c != 0:
        r2, c = r2 + 1, run(s, r2)

    return r1, r2 - 1

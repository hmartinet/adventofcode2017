#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def nsum(s, x, y):
    return sum([s.get((x + dx, y + dy), 0)
                for dx in (0, 1, -1)
                for dy in (0, 1, -1)])


def spiral(limit):
    if limit == 1:
        return 0, 0
    s = {(0, 0): 1}
    n, x, y, i = 1, 0, 0, 0
    r1, r2 = 1, 0
    while True:
        for _ in range(i // 2 + 1):
            n += 1
            x += d[i % 4][0]
            y += d[i % 4][1]
            r1 = n == limit and abs(x) + abs(y)
            if not r2:
                s[x, y] = nsum(s, x, y)
                r2 = s[x, y] >= limit and s[x, y]
            if r1 and r2:
                return r1, r2
        i += 1


def solve(din):
    return spiral(int(din.read()))

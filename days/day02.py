# -*- coding: utf-8 -*-

import re


def solve(din):
    s = [[int(d) for d in re.split('\W+', l.strip())] for l in din.readlines()]

    r1, r2 = sum([max(d) - min(d) for d in s]), 0
    for l in s:
        for i in range(len(l)):
            for j in range(len(l) - i - 1):
                c = l[i], l[i + j + 1]
                x, y = max(c), min(c)
                r2 += x % y == 0 and x // y

    return r1, r2

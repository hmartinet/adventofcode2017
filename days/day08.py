#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

parser = re.compile(r'^(.*) (inc|dec) (-?[0-9]+) if ([a-z]*) (.*)$')


def solve(din):
    reg, m = {}, -sys.maxsize

    for l in din.readlines():
        r, dr, val, src, cond = parser.match(l).groups()
        if eval("{} {}".format(reg.get(src, 0), cond)):
            reg[r] = reg.get(r, 0) + int(val) * (dr == 'inc' and 1 or -1)
            m = max(m, reg[r])

    return max(list(reg.values())), m

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoclib import knot

with open('input/day10') as f:
    inpt = f.read().strip()

h1 = knot.knot([int(n) for n in inpt.split(',')], 1, [])
h2 = knot.knot([ord(i) for i in inpt])

print("Solutions: [{}] [{}]".format(h1[0] * h1[1], knot.hstr(h2)))

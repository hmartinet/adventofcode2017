#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common import knot


def solve(din):
    lengths = din.read().strip()

    h1 = knot.knot([int(n) for n in lengths.split(',')], 1, [])
    h2 = knot.knot([ord(i) for i in lengths])

    return h1[0] * h1[1], knot.hstr(h2)


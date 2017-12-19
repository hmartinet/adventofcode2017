#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve(din):
    ps = [l.strip().split(' ') for l in din.readlines()]

    return (len([1 for p in ps if len(p) == len(set(p))]),
            len([1 for s in [[''.join(sorted(c)) for c in p] for p in ps]
                if len(s) == len(set(s))]))

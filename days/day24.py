#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def run(components, side0, mode):
    strengths = [(0, 1)]
    for i, c in enumerate(components):
        if side0 in c:
            subset = components[0:i] + components[i + 1:]
            s, l = run(subset, c[c[0] == side0], mode)
            strengths.append((s + sum(c), l + 1))
    return max(strengths, key=lambda e: mode == 0 and e or e[::-1])


def solve(din):
    components = [tuple([int(n) for n in c.strip().split('/')])
                  for c in din.readlines()]
    return tuple(run(components, 0, m)[0] for m in (0, 1))

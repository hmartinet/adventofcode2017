#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('input/day05') as f:
    s = [int(d.strip()) for d in f.readlines()]


def execute(s, increment):
    m, size = s.copy(), len(s)
    cursor, step = 0, 0
    while True:
        step += 1
        current = cursor
        cursor += m[current]
        m[current] += increment(m[current])
        if cursor < 0 or cursor >= size:
            return step


print("Solutions: [{}] [{}]".format(
    execute(s, lambda v: 1),
    execute(s, lambda v: v >= 3 and -1 or 1)))

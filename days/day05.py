#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


def solve(din):
    s = [int(d.strip()) for d in din.readlines()]
    return (execute(s, lambda v: 1),
            execute(s, lambda v: v >= 3 and -1 or 1))

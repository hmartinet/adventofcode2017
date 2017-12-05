#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day5.input') as f:
    s = [int(d.strip()) for d in f.readlines()]

def execute(m, increment):
    cursor, step = 0, 0
    while True:
        step += 1
        current = cursor
        cursor += m[current]
        m[current] += increment(m[current])
        if cursor >= len(m) or cursor < 0:
            return step

print("Solutions: [{}] [{}]".format(
    execute(list(s), lambda v: 1),
    execute(list(s), lambda v: v >= 3 and -1 or 1)))

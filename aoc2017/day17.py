#!/usr/bin/env python3
# -*- coding: utf-8 -*-

steps = 335

buf = [0]
cur = 0
for i in range(2017):
    cur = ((cur + steps) % len(buf)) + 1
    buf.insert(cur, i + 1)
r1 = buf[cur+1]

lbuf = 1
pos1 = None
cur = 0
for i in range(50000000):
    cur = ((cur + steps) % lbuf) + 1
    if cur == 1:
        pos1 = i + 1
    lbuf += 1
r2 = pos1

print("Solutions: [{}] [{}]".format(r1, r2))

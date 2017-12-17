#!/usr/bin/env python3
# -*- coding: utf-8 -*-

steps = 335

buf = [0]
cur = 0
for i in range(1, 2018):
    cur = ((cur + steps) % len(buf)) + 1
    buf.insert(cur, i)
r1 = buf[cur+1]

r2 = None
cur = 0
for lbuf in range(1, 50000000):
    cur = ((cur + steps) % lbuf) + 1
    if cur == 1:
        r2 = lbuf

print("Solutions: [{}] [{}]".format(r1, r2))

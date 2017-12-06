#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day6.input') as f:
    mem = [int(n.strip()) for n in f.read().split('\t')]

def execute(mem):
    hist, m = [], mem.copy()
    while True:
        hist.append(m.copy())
        i, v = max(enumerate(m), key=lambda m: m[1])
        m[i] = 0
        for r in range(v):
            m[(i + r + 1) % len(m)] += 1
        if m in hist:
            return len(hist), len(hist) - hist.index(m)

print("Solutions: [{}] [{}]".format(*execute(mem)))

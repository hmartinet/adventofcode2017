#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day6.input') as f:
    mem = [int(n.strip()) for n in f.read().split('\t')]

def execute(mem):
    step = 0
    m = mem[:]
    hist = {str(m): step}
    while True:
        p = max(enumerate(m), key=lambda m: m[1])
        l = len(m)
        m[p[0]] = 0
        m = [v + p[1] // l + (((i-p[0]-1) % l) < p[1] % l and 1) 
             for i, v in tuple(enumerate(m))]
        strm = str(m)
        if strm in hist:
            return len(hist), len(hist) - hist[strm]
        step += 1
        hist[strm] = step

print("Solutions: [{}] [{}]".format(*execute(mem)))

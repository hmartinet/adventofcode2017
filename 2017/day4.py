#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('day4.input') as f:
    ps = [l.strip().split(' ') for l in f.readlines()]

r = (len([1 for p in ps if len(p) == len(set(p))]),
     len([1 for s in [[''.join(sorted(c)) for c in p] for p in ps]
          if len(s) == len(set(s))]))

print("Solutions: [{}] [{}]".format(*r))

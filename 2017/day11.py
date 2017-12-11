#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import numpy

coord = {'n': (2, 0), 'ne': (1, -1), 'se': (-1, -1), 
         's': (-2, 0), 'sw': (-1, 1), 'nw': (1, 1)}

with open('day11.input') as f:
    path = f.read().strip().split(',')

def distance(pos):
    pos = numpy.abs(pos)
    x, y = pos[...,0], pos[...,1]
    return y + numpy.maximum(0, (x - y) // 2)

md = 0
c = 0, 0
for step in path:
   c =  c[0] + coord[step][0], c[1] + coord[step][1]
   md = max(md, distance(c))

print("Solutions: [{}] [{}]".format(distance(c), md))

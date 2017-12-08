#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
import sys

parser = re.compile(r'^(.*) (inc|dec) (-?[0-9]+) if ([a-z]*) (.*)$')

reg = {}
m = -sys.maxsize

with open('day8.input') as f:
    for l in f.readlines():
        r, dr, val, src, cond = parser.match(l).groups()
        if eval("{} {}".format(reg.get(src, 0), cond)):
            reg[r] = reg.get(r, 0) + int(val) * (dr == 'inc' and 1 or -1)
            m = max(m, reg[r])
            
print("Solutions: [{}] [{}]".format(max(list(reg.values())), m))
        

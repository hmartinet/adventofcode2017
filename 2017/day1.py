#!/usr/bin/env python3
#-*- coding: utf-8 -*-

c = [int(d) for d in input("Captcha: ")]

r1, r2 = 0, 0
h = len(c) // 2
for i in range(len(c)):
    r1 += c[i-1] == c[i] and c[i-1]
    e = c[(i+h) % len(c)]
    r2 += c[i] == e and e
 
print((r1, r2))

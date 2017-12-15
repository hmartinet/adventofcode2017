#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Generator():
    
    def __init__(self, *args):
        self.f1, self.f2, self.val, self.mod = args

    def next(self):
        self.val = (self.val * self.f1) % self.f2
        if self.val % self.mod != 0:
            self.next()

    def bin16(self):
        return '{:032b}'.format(self.val)[16:]


def resolve(g1, g2, iters):
    i, count = 0, 0
    while i < iters:
        g1.next()
        g2.next()
        count += g1.bin16() == g2.bin16()
        i += 1
    return count

r1 = resolve(Generator(16807, 2147483647, 116, 1),
             Generator(48271, 2147483647, 299, 1),
             40000000)
r2 = resolve(Generator(16807, 2147483647, 116, 4),
             Generator(48271, 2147483647, 299, 8),
             5000000)

print("Solutions: [{}] [{}]".format(r1, r2))

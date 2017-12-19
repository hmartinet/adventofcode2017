#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Generator():

    def __init__(self, *args):
        self.f1, self.f2, self.val, self.mod = args

    def next(self):
        self.val = (self.val * self.f1) % self.f2
        if self.val % self.mod != 0:
            self.next()
        return self.val


def resolve(g1, g2, iters):
    return sum(g1.next() & 0xFFFF == g2.next() & 0xFFFF for _ in range(iters))


def solve(din):
    a, b = tuple(int(l.split(' ')[-1]) for l in din.readlines())
    r1 = resolve(Generator(16807, 2147483647, a, 1),
                 Generator(48271, 2147483647, b, 1),
                 40000000)
    r2 = resolve(Generator(16807, 2147483647, a, 4),
                 Generator(48271, 2147483647, b, 8),
                 5000000)
    return r1, r2

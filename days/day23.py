#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def run1(prog):
    reg = dict.fromkeys('abcdefghpr', 0)
    code = []

    def cmp(line):
        code.append(compile(line, '<string>', 'exec'))

    funcs = {'set': "{x} = {y}",
             'sub': "{x} -= {y}",
             'mul': "\n".join(("{x} *= {y}", "r += 1")),
             'jnz': "p += ({y} - 1) if {x} != 0 else 0"}
    for i, l in enumerate(prog):
        cmd, x, y = l.strip().split()
        cmp(funcs[cmd].format(x=x, y=y))
    while 0 <= reg['p'] < len(code):
        exec(code[reg['p']], reg)
        reg['p'] += 1
    return reg['r']


def run2(prog):
    h = 0
    b = int(prog[0].strip().split()[-1]) * 100 + 100000
    c = b + 17000

    while True:
        f, d = 1, 2,
        while True:
            f = b % d and f
            d += 1
            if d != b:
                continue
            h += f == 0 or 0
            if b == c:
                return h
            b += 17
            break


def solve(din):
    prog = list(din)
    return run1(prog), run2(prog)

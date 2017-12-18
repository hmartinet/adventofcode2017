#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from multiprocessing import pool, Queue


prog = list(sys.stdin)


def run(pid, mqs):

    def val(v):
        return int(v) if v.lstrip("-").isdigit() else regs[v]

    regs = {}
    ptr, res = 0, 0

    while 0 <= ptr < len(prog) - 1:
        cmd, x, y, *_ = prog[ptr].split() + [0]
        if cmd == 'snd':
            res = mqs and (res + 1) or val(x)
            if mqs:
                mqs[0 if pid else 1].put(val(x))
        elif cmd == 'set':
            regs[x] = val(y)
        elif cmd == 'add':
            regs[x] = regs.get(x, pid) + val(y)
        elif cmd == 'mul':
            regs[x] = regs.get(x, pid) * val(y)
        elif cmd == 'mod':
            regs[x] = regs.get(x, pid) % val(y)
        elif cmd == 'rcv':
            regs[x] = mqs[pid].get() if mqs else res
            if not mqs and regs[x]:
                return regs[x]
        elif cmd == 'jgz' and val(x) > 0:
            ptr += val(y)
            continue
        ptr += 1

    return res


tp, *mqs = pool.ThreadPool(processes=2), Queue(), Queue()
p0, p1 = tp.apply_async(run, (0, mqs)), tp.apply_async(run, (1, mqs))

print("Solutions: [{}] [{}]".format(run(0, None), p1.get()))

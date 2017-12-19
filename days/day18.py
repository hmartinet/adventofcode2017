#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import pool, Queue


def run(pid, prog, mqs):

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


def solve(din):
    prog = list(din)
    tp, *mqs = pool.ThreadPool(processes=2), Queue(), Queue()
    tp.apply_async(run, (0, prog, mqs))
    p1 = tp.apply_async(run, (1, prog, mqs))

    return run(0, prog, None), p1.get()

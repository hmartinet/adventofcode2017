#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve_for(din, *iters):
    rules = {s: d.split('/') for s, d in [l.strip().split(' => ')
             for l in din.readlines()]}
    img = ['.#.', '..#', '###']

    def flat(m):
        return '/'.join(m)

    def tiles(m):
        t, d = [], 2 if len(m) % 2 == 0 else 3
        for l in range(len(m) // d):
            t += [[]]
            for r in range(len(m) // d):
                t[-1].append([s[d * r:][:d] for s in m[d * l:][:d]])
        return t

    def detiles(t):
        m = []
        for itl, tl in enumerate(t):
            m += ["" for _ in range(len(tl[0]))]
            for tile in tl:
                for il, l in enumerate(tile):
                    m[len(tile) * itl + il] += l
        return m

    def isos(m):
        r1 = [''.join(s) for s in zip(*m[::-1])]
        r2 = [''.join(s) for s in zip(*r1[::-1])]
        r3 = [''.join(s) for s in zip(*r2[::-1])]
        return [m[:], r1, r2, r3, m[::-1], r1[::-1], r2[::-1], r3[::-1]]

    def transform(img):
        ts = tiles(img)
        for tile in sum(ts, []):
            for iso in isos(tile):
                key = flat(iso)
                if key in rules:
                    tile[:] = rules[key]
                    break
        return detiles(ts)

    r = []
    for _ in range(max(iters)):
        img = transform(img)
        r.append(sum([l.count('#') for l in img]))

    return tuple(r[i - 1] for i in iters)


def solve(din):
    return solve_for(din, 5, 18)

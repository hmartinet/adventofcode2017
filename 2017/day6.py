#!/ubr/bin/env python3
#-*- coding: utf-8 -*-

with open('day6.input') as f:
    b = [int(n.strip()) for n in f.read().split('\t')]

h = [b.copy()]
step = 0
while True:
    step += 1
    m = max(b)
    i = b.index(m)
    b[i] = 0
    for r in range(m):
        i = (i + 1) % len(b)
        b[i] += 1

    if b in h:
        break
    h.append(b.copy())

print("Solutions: [{}] [{}]".format(
    step, len(h) - h.index(b)))

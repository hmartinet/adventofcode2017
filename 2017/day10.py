#!/ubr/bin/env python3
#-*- coding: utf-8 -*-

with open('day10.input') as f:
    inpt = f.read().strip()

def hash(data, rnd=64, ext=[17, 31, 73, 47, 23]):
    lengths = data[:]
    lengths.extend(ext)
    h = list(range(256))
    cr, skip = 0, 0
    for r in range(rnd):
        for l in lengths:
            sl = [h[(cr+i)%256] for i in range(l)][::-1]
            for i in range(l):
                h[(cr+i)%256] = sl[i]
            cr, skip = (cr+l+skip)%256, skip+1
    return h

def hex(data):
    res = 16 * [0]
    for i in range(16):
        for j in range(16):
            res[i] ^= data[16*i+j]
    return ''.join(['{:02x}'.format(n) for n in res])

h1 = hash([int(n) for n in inpt.split(',')], 1, [])
h2 = hash([ord(i) for i in inpt])

print("Solutions: [{}] [{}]".format(h1[0]*h1[1], hex(h2)))

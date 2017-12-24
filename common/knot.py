# -*- coding: utf-8 -*-


def knot(data, rnd=64, ext=[17, 31, 73, 47, 23], base=256):
    lengths = data[:]
    lengths.extend(ext)
    h = list(range(base))
    cr, skip = 0, 0
    for _ in range(rnd):
        for l in lengths:
            sub = [h[(cr + i) % base] for i in range(l)][::-1]
            for i in range(l):
                h[(cr + i) % base] = sub[i]
            cr, skip = (cr + l + skip) % base, skip + 1
    return h


def hstr(data):
    res = 16 * [0]
    for i in range(16):
        for j in range(16):
            res[i] ^= data[16 * i + j]
    return ''.join(['{:02x}'.format(n) for n in res])


def bstr(s, l):
    return bin(int(hstr(knot([ord(i) for i in s])), 16))[2:].rjust(l, '0')

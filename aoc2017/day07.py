#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

re_line = re.compile(r'^(.*) \(([0-9]*)\)( -> )?(.*)?$')


def parseinput():
    res = {}
    with open('input/day07') as f:
        for l in f.readlines():
            n, w, _, cstr = re_line.match(l).groups()
            res[n] = int(w), cstr and cstr.split(', ') or []
    return res, next(iter(set(res.keys()) -
                          set(sum([v[1] for v in res.values()], []))))


class Node():
    def __init__(self, data, name, parent):
        self.name = name
        self.weight = data[name][0]
        self.parent = parent
        self.children = {child: Node(data, child, self)
                         for child in data[name][1]}

    def deep_weight(self):
        return self.weight + sum(
            [n.deep_weight() for n in self.children.values()])

    def find_unbalanced(self):
        weights = [n.deep_weight() for n in self.children.values()]
        for _, n in self.children.items():
            if weights.count(n.deep_weight()) == 1:
                return n.find_unbalanced()
        return self


data, root_name = parseinput()
root = Node(data, root_name, None)

enode = root.find_unbalanced()
cnode = enode.parent.children[[n for n in enode.parent.children.keys()
                               if n != enode.name][0]]

print("Solutions: [{}] [{}]".format(
    root.name,
    enode.weight + cnode.deep_weight() - enode.deep_weight()))

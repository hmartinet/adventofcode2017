#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import operator
from functools import reduce
from pprint import pprint

weights = {}
inputs = {}
with open('day7.input') as f:
    for l in f.readlines():
        e = [s.strip() for s in l.split(' ')]
        weights[e[0]] = int(e[1][1:-1])
        if len(e) > 3:
            inputs[e[0]] = ''.join(e[3:]).split(',')
        else:
            inputs[e[0]] = []

def findroot():
    childs = {ck: k for k, v in inputs.items() for ck in v}
    for node in weights.keys():
        if node not in childs:
            return node

def buildtree(tree, node):
    return {child: buildtree({}, child) for child in inputs[node]}
            
def weight(node, tree):
    return sum(weight(*i) for i in tree.items()) + weights[node]  

def findpath(tree):
    wm = {k: weight(k, v) for k, v in tree.items()}
    for n in wm.keys():
        if list(wm.values()).count(wm[n]) == 1:
            return [n] + findpath(tree[n])
    return []
    
def main():
    root = findroot()
    tree = buildtree({}, root)

    path = findpath(tree)
    enode = path[-1]
    etree = reduce(operator.getitem, path[:-1], tree)
    cnode = [n for n in etree.keys() if n != enode][0]

    print("Solutions: [{}] [{}]".format(
        root, 
        weights[enode] + 
        weight(cnode, etree[cnode]) - weight(enode, etree[enode])))

main()


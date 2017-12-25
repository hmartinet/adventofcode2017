#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse(din):
    machine = {}
    state, value = None, None
    for l in din .readlines():
        lw = l.strip().split()
        if not lw:
            continue
        elif lw[0] == 'Begin':
            machine['start'] = lw[-1][:-1]
        elif lw[0] == 'Perform':
            machine['steps'] = int(lw[-2])
        elif lw[0] == 'In':
            state = lw[-1][:-1]
            machine[state] = []
        elif lw[0] == 'If':
            value = len(machine[state])
            machine[state].append([])
        elif lw[1] == 'Write':
            machine[state][value].append(int(lw[-1][:-1]))
        elif lw[1] == 'Move':
            machine[state][value].append(lw[-1][:-1] == 'right' and 1 or -1)
        elif lw[1] == 'Continue':
            machine[state][value].append(lw[-1][:-1])
    return machine


def run(machine):
    cr = 0
    tape = {}
    state = machine[machine['start']]
    for _ in range(machine['steps']):
        val = tape.get(cr, 0)
        tape[cr] = state[val][0]
        cr += state[val][1]
        state = machine[state[val][2]]
    return tape


def solve(din):
    return sum(run(parse(din)).values()), '*' * 50

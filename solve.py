#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import days
# import profile

day = sys.argv[1]
print("### Run Advent Of Code - Day {} ###\n".format(day))

day = getattr(days, "day{}".format(day))
# res = (None, None)
# profile.run('res = day.solve(sys.stdin)')
res = day.solve(sys.stdin)
print("Solutions: [{}] [{}]".format(*res))

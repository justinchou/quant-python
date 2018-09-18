# -*- coding: UTF-8 -*-

import random

rand = [random.normalvariate(0, 1) for i in range(0, 20)]

minNum = min(rand)
maxNum = max(rand)
total = sum(rand)
print("Serial Min %s Max %s, Total %s" % (minNum, maxNum, total))

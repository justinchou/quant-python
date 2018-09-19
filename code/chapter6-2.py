# -*- coding: UTF-8 -*-

import random

for item in [random.normalvariate(0, 1) for i in range(0, 5)]:
    print("Big" if item > 0 else "Small", item)


# -*- coding: UTF-8 -*-


def getPositiveReturnDays(lst):
    if type(lst) not in (tuple, list):
        return ("Invlaid List Input")

    isPositive = lambda ipt: 1 if ipt > 0 else 0

    return sum(map(isPositive, lst))


v = getPositiveReturnDays([1.2, 2, -1, 0, -1.4, 1.05, 0.8])
print(v)

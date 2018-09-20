# -*- coding: UTF-8 -*-


def absList(*lst):
    if type(lst) is not tuple:
        return ("Invlaid List Input")

    return (map(abs, lst))


v = absList(1, -1, 2, -3)
print(type(v))

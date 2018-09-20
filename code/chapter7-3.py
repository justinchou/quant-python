# -*- coding: UTF-8 -*-

sumType = {int, float, bool, complex}


def sum2(*argv):
    if (type(argv) is not tuple or len(argv) == 0):
        return 0

    print(argv)
    sumVal = 0

    for i in argv:
        if (type(i) in sumType):
            sumVal += i

    return sumVal


v=sum2(1, 2, 3, "12", {12}, [12], (12,), True, 1+2j, 3.14)
print(v)

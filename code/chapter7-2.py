# -*- coding: UTF-8 -*-


def sum_list(l1, l2):
    if (len(l1) != len(l2)):
        return "Invalid Length~"

    sumLen = [l1[i]+l2[i] for i in range(len(l1))]
    return sumLen


print(sum_list([1, 2, 3], [2, 3, 4]))

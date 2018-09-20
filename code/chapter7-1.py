# -*- coding: UTF-8 -*-

x = [1, 2, 3]


def func(x):
    x[0], x[-1] = x[-1], x[0]
    return x


y = func(x)

# True
print(y is x)

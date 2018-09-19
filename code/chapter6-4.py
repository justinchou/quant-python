# -*- coding: UTF-8 -*-

a = (-1, 0, 1, 2, 39)
b = (1, 4)

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            print("Interact %s" % (a[i]))

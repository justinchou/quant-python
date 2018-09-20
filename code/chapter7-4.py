# -*- coding: UTF-8 -*-

import time


def fibo(n):
    if n in (0, 1):
        return 1

    return fibo(n-1) + fibo(n-2)


start = time.clock()
v = fibo(30)
print("Fibo 30 => %s" % (time.clock() - start))
print(v)


betterFiboList = []


def subFibo(n):
    if n < len(betterFiboList):
        return betterFiboList[n]

    if n in (0, 1):
        betterFiboList.append(1)
        return 1

    fiboN = subFibo(n-1) + subFibo(n-2)
    betterFiboList.append(fiboN)

    return fiboN


def betterFibo(n):
    for i in range(n):
        subFibo(i)

    return subFibo(n)


start = time.clock()
v = betterFibo(300)
print("BetterFibo 300 => %s" % (time.clock() - start))
print(v)

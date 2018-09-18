# -*- coding: UTF-8 -*-

print("==========", 5)

s = "abc"

t = (s,)
print(t)

l = [s]
print(l)

st = set(s)
print(st)


print("==========", 6)

d2num = {"A": ord("A"), "b": ord("b"), "\n": ord("\n")}
print(d2num)

num2d = {"65": chr(65), 98: chr(98), 10: chr(10)}
print(num2d)

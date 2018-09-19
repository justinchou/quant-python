# -*- coding: UTF-8 -*-

v = 14

if type(v) != int:
    print("Error: Only Support Integer!")
elif v % 2 == 0:
    print(0)
elif v % 2 == 1:
    print(v)
    

v = 12
print(type(v))
v = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(type(v))
v = 12.5
print(type(v))
v = 12 + 5j
print(type(v))
v = True
print(type(v))


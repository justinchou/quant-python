# -*- coding: UTF-8 -*-

# [1,2,3]
a = [1,2,3]
print(a)

# [1,2,3]
b = a
print(b)

# True
print(id(a) == id(b))

b[0] = 3

# [3,2,3]
print(b)

# [3,2,3]
print(a)

# True
print(id(a) == id(b))
# -*- coding: UTF-8 -*-

# 7
v = 3+4
print(v)

# 13.6
v = 3.4*4
print(v)

# 0
v = 3//4
print(v)

# True
v = id(['a', 3, True, 'asd'][1]) == id(3)
print(v)

# False
v = (3 == 4 in [1, "334", 3+4j, 4 in [1, 2, 3]])
print(v)

# True
v = ((3 == 4*4.5 % 2 is 0) in [3, 4, "Tom", "c" in "comic"])
print(v)

# -*- coding: UTF-8 -*-

# is 即为比较两个变量的 id

# 首先说基础类型, is 和 == 相同, 因为基础类型底层是不可变的唯一地址

s1 = "abc"
s2 = "abc"
print(s1 == s2, s1 is s2)

# 然后是扩展类型, 扩展类型中, 虽然内部的基础类型地址相同, 但是在外部又构建了不同的结构地址

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1[0] == l2[0], l1[0] is l2[0])
print(l1 == l2, l1 is not l2)

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1[0] == t2[0], t1[0] is t2[0])
print(t1 == t2, t1 is not t2)

d1 = {"a": 1, 2: 3}
d2 = {"a": 1, 2: 3}
print(d1["a"] == d2["a"], d1["a"] is d2["a"])
print(d1 == d2, d1 is not d2)

st1 = {"a", 1, 2, 3}
st2 = {"a", 1, 2, 3}
print(st1 == st2, st1 is not st2)

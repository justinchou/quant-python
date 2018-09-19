# 量化投资-以 Python 为工具

## Anaconda

安装好后要检查环境变量(/anaconda/bin:$HOME/.anaconda/bin)

## Python 编程小技巧

```
# -*- coding: UTF-8 -*-
# 上面注释允许本文件以 UTF8 编码.
```

空行有时必须, 用于标记循环语句结束.
使用 \ 能将两行以一行执行(和 shell 相同)

字符串可以是 " ... ", ' ... ', """ ... """

缩进表示结构丛属关系

## Python 基础类型

1. 数值: int long(2.x) float bool complex
2. 字符串: string
3. 容器: list set dict tuple

type() 查看某变量类型
判断变量是否是某种类型: type(x) is int, type(x) == int, isinstance(x, int) 
=> 区别在于判断B继承A时,  isinstance(B(), A) 真, type(B()) is A 假; 基础类型判断没有问题.

bool() 查看对象的布尔值
id() 查看变量的内存地址

ord("char") => num, chr(num) => char

dir() 查看系统变量, dir(**builtin**) 查看内置模块和系统关键字

1. int/long 2.x 整数 2^-31~2^31, 超出后末尾自动加 `L`; 3.x 整数只受内存大小限制.
2. float 值都是近似值, 无法进行金融计算.
3. bool 首字母要大些呢, True/1, False/0/""/''/[]/()/{}/None
4. complex(x,y) 即为 x+yj, 虚数单位用 j/J 表示.
5. string ""/''/""" ... """, 可以使用下标 s[id] 访问某个字符(但类型也是只有一个字符的字符串).
6. list [...] 类似非强类型数组, 使用下标 l[id] 访问/赋值, 元素可改变(增加l.append(i)/删除/更改数据-值/类型)

所有数值型, 字符串都是不可变对象.
赋值只是将其指向另一个地址, 原数据还在, 重新赋值还指向原地址.

```python
x = 1
id(x)   // 值 aaa
x = x+1
id(x)   // 值变了
x = x-1
id(x)   // 值又变为 aaa
```

7. tuple 元组 (v1,), 类似列表 list 可以存储不同类型数据, 类似 string 元素不可变. 为避免与括号歧义, 一个元素的元组末尾要有逗号.大项目可以有效防止误操作.
8. dict 字典 {key: val}, 通过 dict[key] 访问值.
9. set 集合 {key1, key2} 或 set([key1, key2]), 集合无序, 存储不可变对象, 无重复元素. 不能索引存取. 使用字符串创建必须使用 set("str"), 创建空集合必须使用 set().

值类型只能通过下标访问, 不能通过下标赋值.

## Spyder

Spyder 中将代码使用 `#%%` 分块, 可以以块为单位执行.

执行之后, 会有 Variable Explorer 显示脚本执行过程中的所有变量及值列表.

设定当前工作路径的功能, 协助切换路径, 方便引入文件.

## Python 运算符

数值(布尔,虚数)类型: + - * / \*\*幂 //整除 %模
字符串类型: +链接 *重复 %s 格式化, "str"\*n, "hello %s" %("justin")

赋值运算: = += -= \*= /= \*\*= //= %=

比较运算: == != > < >= <=, True == 1 成立, 但是 True == 2 不成立

逻辑运算: and or not 都是惰性运算, 返回惰性值

身份运算: is 和 is not, 比较的是内存地址. is 相当于用于判断 id(a) == id(b), is not 反之.

成员运算: in 和 not in, 支持 list[], tuple(), set{}和字符串

1. \*\*
2. - / // %
3. - -
4. > > = < <=
5. == !=
6. = += -= \*= /= \*\*= //= %=
7. is, is not
8. in, not in
9. and, or, not

内置算数函数

sum(iter, init=0), pow(x, y, z=None), divmod(x, y) => (x//y, x%y)
abs(x), all(iter) => bool, any(iter) => bool, max(...), min(...), round(x, n)

## 语句

**赋值**

1. x = 5
2. y = [1,2]
3. a = b = c = 5
4. a, b, c = 1,2,3
5. += -= *= /= **= //= %=

**条件: cond 无括号**

if cond:
  statement
elif:
  statement
else:
  statement

**三元运算符**

v1 if cond else v2 
相当于 cond ? v1 : v2

**循环**

for, while, 嵌套 => break退出循环, continue退出本次循环继续下一次, pass当前逻辑未写

遍历序列: 

for 循环 `for i in list:` 直接遍历的是值, 而非其他语言的 index
如果遍历 index, 需要使用 `for id in range(len(list)):`

for i in list/tuple/str:
  statement

for i in range(len(list/tuple/str)):
  if cond:
    statement

如果循环处理某个序列值, 生成新序列, 可以简化成单条语句

[statement for i in list/tuple/str]

[statement for i in range(len(list/tuple/str)) if cond]

嵌套循环

for i in x:
  for j in y:
    [i, j]

[[i, j] for i in x for j in y]

while cond:
  statement

## 函数

## 面向对象

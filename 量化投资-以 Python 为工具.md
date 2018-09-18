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

1. 数值: int long float bool complex
2. 字符串: string
3. 容器: list set dict tuple

type() 查看某变量类型
bool() 查看对象的布尔值
id() 查看变量的内存地址

ord("char") => num, chr(num) => char

dir() 查看系统变量, dir(__buildin__) 查看内置模块和系统关键字

1. int/long 2.x 整数 2^-31~2^31, 超出后末尾自动加 `L`; 3.x 整数只受内存大小限制.
2. float 值都是近似值, 无法进行金融计算.
3. bool 首字母要大些呢, True/1, False/0/""/''/[]/()/{}/None 
4. complex(x,y) 即为 x+yj, 虚数单位用 j/J 表示.
5. string ""/''/""" ... """, 可以使用下标 s[id] 访问某个字符(但类型也是只有一个字符的字符串).
6. list [...] 类似非强类型数组, 使用下标 l[id] 访问/赋值, 元素可改变(增加/删除/更改数据-值/类型)

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

## Python 运算符 TODO

## 语句

## 函数

## 面向对象




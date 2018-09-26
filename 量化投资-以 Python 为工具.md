# 量化投资-以 Python 为工具

## Anaconda

安装好后要检查环境变量(/anaconda/bin:$HOME/.anaconda/bin)

## Python 编程小技巧

```python
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
=> 区别在于判断 B 继承 A 时, isinstance(B(), A) 真, type(B()) is A 假; 基础类型判断没有问题.

bool() 查看对象的布尔值
id() 查看变量的内存地址

ord("char") => num, chr(num) => char

dir() 查看系统变量, dir(**builtin**) 查看内置模块和系统关键字

1. int/long 2.x 整数 2^-31~2^31, 超出后末尾自动加 `L`; 3.x 整数只受内存大小限制.
2. float 值都是近似值, 无法进行金融计算.
3. bool 首字母要大些呢, True/1, False/0/""/''/[]/()/{}/None
4. complex(x,y) 即为 x+yj, 虚数单位用 j/J 表示.
5. string ""/''/""" ... """, 可以使用下标 s[id] 访问某个字符(但类型也是只有一个字符的字符串).
6. list [...] 类似非强类型数组, 使用下标 l[id] 访问/赋值, 元素可改变(增加 l.append(i)/删除/更改数据-值/类型)

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

数值(布尔,虚数)类型: `+` `-` `*` `/` `**`幂 `//`整除 `%`模
字符串类型: +链接 \*重复 %s 格式化, "str"\*n, "hello %s" %("justin")

赋值运算: `=` `+=` `-=` `*=` `/=` `**=` `//=` `%=`

比较运算: `==` `!=` `>` `<` `>=` `<=`, True == 1 成立, 但是 True == 2 不成立

逻辑运算: and or not 都是惰性运算, 返回惰性值

身份运算: is 和 is not, 比较的是内存地址. is 相当于用于判断 id(a) == id(b), is not 反之.

成员运算: in 和 not in, 支持 list[], tuple(), set{}和字符串

1. `**`
2. `-` `/` `//` `%`
3. `+` `-`
4. `>` `>=` `<` `<=`
5. `==` `!=`
6. `=` `+=` `-=` `*=` `/=` `**=` `//=` `%=`
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
5. += -= \*= /= \*\*= //= %=

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

for, while, 嵌套 => break 退出循环, continue 退出本次循环继续下一次, pass 当前逻辑未写

遍历序列:

for 循环 `for i in list:` 直接遍历的是值, 而非其他语言的 index
如果遍历 index, 需要使用 `for id in range(len(list)):`

```python
for i in list/tuple/str:
  statement

for i in range(len(list/tuple/str)):
  if cond:
    statement
```

如果循环处理某个序列值, 生成新序列, 可以简化成单条语句

```python
[statement for i in list/tuple/str]

[statement for i in range(len(list/tuple/str)) if cond]
```

嵌套循环

```python
for i in x:
  for j in y:
    [i, j]

[[i, j] for i in x for j in y]
```

```python
while cond:
  statement
```

## 函数

```python
def func(arg1, ..., argN=1):
  expression
  return None
```

return 是 return None 的简写, 函数可以没有 return 语句.
空函数体要使用 `pass`

超过一个返回值, 使用 tuple 实现: `return x,y,z`

传参可以直接按顺序传, 也可以 `func(argN=1, ..., arg1=n)`

不可变对象传参值传递, 可变对象传参引用传递

可选参数:

1. 参数打包后以[]/()/{}传参.
2. \*tpl 表示 tuple, \*\*dct 表示 dict.

匿名函数:
lambda arg1...: expression

作用域: 模块内函数外, 则全局可访问(函数内访问是只读, 加 global 变可写); 函数内, 函数局部可访问.

## 面向对象

```python
class ClassName(baseObject 默认 object):
  """
  一般的类注释
  """

  def __init__(self, id, price):
    """
    初始化方法, 必须传入股票的 id 和价格
    """
    # public
    self.id = id
    # private
    self.__price = price

  def debug(self):
    print("%s price is %s" %(self.id, self.__price))

  def getPrice(self):
    return(self.__price)

obj1 = ClassName(1, 12.5)
obj2 = ClassName(2, 8.0)

obj1.debug()

```

继承的初始化和覆盖

```python
# 继承
class Parent(object):
  def __init__(self, argv1):
    self.argv1 = argv1

  def foo(self):
    pass


class Child(Parent):
  def __init__(self, argv1, argv2):
    Parent.__init__(self, argv1)
    # 或者
    super(Child, self).__init__(argv1)
    
    self.argv2 = argv2

  def foo(self):
    super(Child, self).foo()

```

属性可以动态产生, 所以同一个类产生的对象, 不一定有相同的属性,
但是必要的属性, 可以使用 `__init__` 方法添加, 必须在创建对象时传入.

封装: 增加 private 概念, 使得有些内容只能内部访问, 要增加部分方法予以暴露.
继承: 增加复用性, 抽象性(父类是多个子类的共性), 子类覆盖父类的方法称重写.

## 标准库与数据操作

### 模块

模块即为函数集合的文件, 文件名作为全局的变量(`__name__`)可以被其他模块导入

```python
# package file PriceAnalysis.py
# 导入全部
import PriceAnalysis
PriceAnalysis.OpenPrice()

# 别名
import PriceAnalysis as prcAnsys
prcAnsys.OpenPrice()

# 导入某个方法
from PriceAnalysis import OpenPrice
OpenPrice()
```

搜索路径为 `os.getcwd()` -> `sys.path`

### 包

**包** 文件夹必须有 `__init__.py` 文件, 但内容可以为空, 用以标记文件夹是否为包.

```python
import mainPkg.subPkg.className
mainPkg.subPkg.className.funcName()

from mainPkg.subPkg import className
className.funcName()

from mainPkg.subPkg.className import funcName
funcName()
```

定义 `__init__.py` 支持 `import *`

```python
__all__ = [file1, file2...]
```

### 内置模块

数学模块: math(float), cmath(int, float, complex)
时间日期: calendar(获取, 显示), time(计算, 除了, 格式化), datetime.datetime

calendar.isleap(2016)

time.time(): timestamp
time.struct_time((tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)): struct_time
time.localtime(timestamp): strct_time
time.asctime(structTime): str
time.ctime(timestamp): str
time.strptime(YmdStr, YmdTemplate): struct_time 用时间格式模板(例如"%Y-%m-%d")解析时间字符串("2018-09-21")
time.strftime(YmdTemplate, structTime): str 将 struct 对象格式化成指定时间模板

`Y/y-m/b/B-d H/I-M-S a/A/w/W/U` 年月日 时分秒 星期

datetime.now(): datetime
计算时间差, 返回 datetime.delta 类型, 可与 datetime 类型直接加减运算.
str(dateTime): str
dateTime.strftime(YmdTemplate): str
dateTime.strptime(YmdStr, YmdTemplate): datetime

### 内置数据类型操作

#### 序列 list, tuple, range + str

x (not) in s 是否在其中
ns = `+` 链接, s * n 重复
s[i] 取元素
s[i,j,k] 切片, 不包括 j,  步长k默认1
len(), min(), max()
s.index(x, i, j) 索引值, 起点i默认0, 终点j默认 len() - 1
s.count(x) 统计

1. 创建 list([..]) | [..]

s.append(x), s.extend([..]/(..))
s.insert(i, x)
x = s.pop(i) 第i个元素默认删最右端
s.remove(x) 删左边第一次出现, 不存在报错, 所以先count统计判断
s.sort() s.reverse() 升降序

2. 创建 tuple((..)) | 逗号 | (..)

列表->元组 tuple(list)
字符串->元组 tuple(str)

值不可变, 无个性化方法

3. 创建 range(start, end, step)

值不可变, 经常与 for 联合使用.

无法直接查看其中枚举值, 只能将其转换成 tuple/list 查看

range->列表: list(range)
range->元组: tuple(range)

不可以使用 `*` 进行重复

4. 创建 str() | "",'',""" .. """

s.split(spliter): list 默认空格分割
str.join(iter): str 组合

s.islower/isupper/istitle()
s.lower/upper/title/capitalize/swapcase()
词频统计, 最好先全部转换成小写, 避免首字母大写造成的问题.

s.find/rfind/index/rindex(x) 不存在 find返回-1, index报错
s.startswith/endswith(ns/tpl) 是否以 str, str元组开头
s.strip/rstrip(rem) 删掉两端/末尾 rem 字符, 默认空白字符

#### 字典

创建 {}, dict({}), dict(k=v,...), dict((k,v),...), dict(zip([keyList], [valueList]))

dic.items(): [(key, value), ...]
dic.keys(): [key, ...]
dic.values(): [value, ...]
可以进行 for in 循环.

查 dic[key], dic.get(key)
改 dic[key] = val, dic.update(key=value)
增 dic[nkey] = val
删 del dic[key]
清空 dic.clear() 删除所有 key, 返回空字典{}
复制 ndic = dic.copy()
合并 ndic = dict(dic1, **dic2)


#### 集合

无序, 不重复, 不能索引. 列表转集合可以去重.

创建可变集合 set() 或 {}
创建不可变集合 frozenset()

可变集合 st.add(v), st.remove(v)
元素个数 len(st)
遍历 for v in st:

`∩` 交 union `|`, `∪` 并 interaction `&`, `-` 差 difference `-`, 对称差 symmetric_difference `^` (`∪`并-`∩`交)
子集 issubset `<=`, 父集 issuperset `>=`, 无关 isdisjoint
































## 使用函数库 Numpy 和 Pandas

### Numpy

用于创建一维数组和二维矩阵(以及多维), 并对其进行运算

```python
import numpy as np
arr1 = np.array(range(12)) # 初始化数组
arr1.shape # 获取结构
arrn.dtype # 可以查看数组item类型

# 一维 <=> 二维
arr1.shape = 3,4 # 更改结构
arr2 = arr1.reshape(4,3) # 拷贝新结构, 原结构不变
arr3 = arr1.reshape(2,3,4)
## 上面的 arr1 和 arr2 值共用内存地址, 相当于同一个指针, 只不过结构部分不一致

# 初始化
arr4 = np.arange(0,6,2) # start stop step => int64数列(不含末尾值)
arr5 = np.linspace(0,6,7) # start stop amount dtype=int?舍尾 => float64数列(包含末尾值)
arr6 = np.zeros((2,3)) # 初始化占位符, 默认浮点型
arr7 = np.ones((2,3), dtype=int/np.int16)

# 切片
arr[start:stop=start:step=1] # 切片, 负数从右向左, 切片与原数组共享内存(list并不是共享内存)

# 二维
arr[start:stop:step, start:stop:step] # 二位数组切片 [x横, y竖]
arr[[a,b,c],[α,β,γ]]

# 运算
参数(arr1, num/arr2, target), 每个元素都加 num, 或者数组 arr2 对应元素相加.
target = np.zeros((a,b), dtype=np.int16)

1. np.add()  `+`
2. np.substract()  `-`
3. np.multipl()  `*`
4. np.devide()  `/`
5. np.mod()  `%`
6. np.remainder()  `%`
7. np.power()  `**`
8. np.square()
9. >/>= ... 数组中每一个元素都参与判断, 得出布尔结果
0. cos()/sin() ... 数组中每个值都计算
```

### Pandas

#### Series 序列

value 和 index(可重复数据标记), value 本质上还是列表/numpy.array.

```python
import pandas as pd

sr = pd.Series()
sr = pd.Series(lst/np.arr, index=lst) # index 默认从 0 增长
sr = pd.Series(dict)

sr.value  # 值列表
sr.index  # 索引列表
sr[idx] = val # 增加元素

sr.head(n=5)
sr.tail(n=5)
sr.take([idx lst])

# idx 为数字下标序号, index 为
sr[idx/index] 获取单元素
sr[[idx/index, ...]] 依据
sr[start:stop] 使用 idx 不包含 stop, 使用 index 包含 stop.

# 时序
pd.Series(lst/arr, index=pd.to_datetime(date_str_list))
pd.Series(lst/arr, index=[datetime(..), ..])
# 时序索引优化
ts["Ymd"] / tm["Y-m-d"] / tm["m/d/Y"]
ts["Ym":"Ym"] / ts["Ym"]
ts.truncate(after="Ymd") 去掉该日期之后的
# +滞后, -前移操作(数组值移动几个位置)
ts.shift(±n)
# 重新取样, 例如将日数据转换成月数据
ts.resample("M/MS", how="first/mean...")
```

#### DataFrame 就是类似 mysql 的数据表

```python
# 随机数据
df = pd.DataFrame(np.random.randn(m,n), index=pd.to_datetime(list), columns=list)

# 读取 csv/txt, header=0 表示首行是头, names各列变量名(有 header 时省略)
df = pd.read_csv("filename", sep=",", header=None)
df = pd.read_table("filename", sep="\t", header=None, names=None)
# 读取 mysql 数据表
import MySQLdb
conn = MySQLdb.connect(host="", port=3306, user="", passwd="", db="")
df = pd.read_sql("select * from ...", conn)
conn.close()

# 控制台显示
df  df.head(n)  df.tail(n)
df.columns  df.index  df.values 二维数组
df.describe() 描述性统计

# 按行切片 => 列不能切片
df[idxStart:idxStop]
# 取某些列
df[["A","C"]]
# 满足条件
df[df["A"]>0]
# 行列共同操作
df.loc[row行-date类型, column列-标签] 使用 name "A", "B", "C"..
df.iloc[row行-idx类型, column列-索引], 使用 idx 0,1,2..
df.ix[row 行, column列] 自动判断标签/索引

# 转置
df.T
df.sort(axis=0/1, columns=None, ascending=True) 默认 axis=0 按照index日期排序, axis=1 排序列的左右顺序(貌似用处不大); 以某一列进行排序要指定 columns.
df.rank(axis=0/1, ascending=True) 返回轴上排名表

# 增加一列, 列数据是 list 列表, 列索引是以 Ymd 开始的 n 天, 一般 n 就是 list 数据长度
col = pd.Series(list, index=pd.date_range("YmdStartDate", periods=n))
df["E"] = col

# 合并
pd.concat([df, sr]) - join
df.append() - multi-insert
pd.concat([df, df], join="inner")

# 删除
df.drop(dates[1:3]) 删除行(返回新表)
df.drop("A", axis=1) 删除列(返回新表)
del df["A"] 删除列(作用于原表)

# 替换 - 取到位置直接赋值
df.loc[:, "A"] = np.arange(0, len(df)) 整列
df.loc[dates[1], "B"] = 0 替换指定位置
df.loc[1, 1] = 0 替换指定位置

# 重置索引返回新表 - 老表没有的数据新表为 NaN
df.reindex(pd.date_range("Ymd", periods=n), column=list)

# 运算 - Series 的 index 与 DateFrame 的 column 对应. 无法预算值为 NaN
Series: [1,2,3], index=list("ABC")
DataFrame:
.. A  B  C
d1 .. .. ..
d2 .. .. ..
# 运算 - DataFrame 与 DataFrame 则按行列对应计算, 无法计算值为 NaN
# 缺失值可以在使用运算函数的时候, 指定默认值

# 应用函数
df.apply(func, axis=0)
df.apply(max, axis=0)
df.apply(lambda x: x.max() - x.min(), axis=1)
```

#### 数据规整化

**判断缺失值** df.isnull() / df.notnull()

DataFrame 对象判断 NaN / None 时返回一个 True|False 的 DataFrame 对象.

df.A[df.A.notnull()] 选出有数值的数据

**填充缺失数据** df.fillna(...)

**删除缺失值** df.dropna(...)

**判断重复行/删除** df.duplicated([columeName]), df.drop_duplicates([columnName]) 默认不传列名, 匹配所有列

## Matplotlib 绘图

@TODO 绘图部分











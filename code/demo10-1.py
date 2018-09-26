# -*- coding: utf-8 -*-

import numpy as np

# 初始化数组
arr1 = np.array(range(12))
# 获取结构
arr1.shape
# 更改结构
arr1.shape = 3,4
# 拷贝新结构, 原结构不变
arr2 = arr1.reshape(4,3)
## 上面的 arr1 和 arr2 值共用内存地址, 相当于同一个指针, 只不过结构部分不一致

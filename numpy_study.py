# -*- coding: utf-8 -*-
#numpy的核心是构建多维数组
import numpy as np
array1 = np.array(range(6))

print(array1)

print(array1.shape)
#输出为(6,)表明array1为一维数组

#将数组改为二维结构（二行三列）
array1.shape=2,3
print(array1)

array2 = array1.reshape(3,2)
print(array2)
print(array2.shape)

print(array1.shape)


array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array3)
print(array3.shape)

# 根据起始值、结束值和步长生成一维数组
array4 = np.arange(13,1,-1)
print(array4)

array4.shape=2,2,3
print(array4)

array5 = array4.reshape(3,2,2)
print(array5)

# 根据起始值，结束值以及样本数生成序列
array6 = np.linspace(1,12,12)
print(array6)
print(array6.dtype)

# 还可以指定linespace的数据类型
array7 = np.linspace(1,12,12,dtype=int)
print(array7)



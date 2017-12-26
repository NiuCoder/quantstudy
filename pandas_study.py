# -*- coding: utf-8 -*-
#pandas的核心是序列，其实就是包含index的一维数组，可以看做是横纵坐标值
import pandas as pd
import numpy as np
from datetime import datetime

#创建空的Series
S1=pd.Series()
print(S1)

#同时指定index和values
S2=pd.Series([1,3,5,7,9],\
             index=['a','b','c','d','e'])
print(S2)

print(S2.values)
print(S2.index)

#增加新的元素
S2['f']=11
print(S2)

#Series和字典dict很像，可以将字典转换为Series
S3 = pd.Series({'a':1,'b':3,'c':5,'d':7})
print(S3)

#仅指定values属性的取值
S4 = pd.Series([1,3,-5,7])
print(S4)

S5 = pd.Series([0,np.NAN,2,4,6,8,True,10,12])
#默认取前五个
print(S5.head())
#默认取最后五个
print(S5.tail())
#取指定索引
print(S5.take([2,4,0]))

#时间序列
dates=['2016-01-01','2016-01-02','2016-01-03']
ts=pd.Series([1,2,3],index=pd.to_datetime(dates))
print(ts)
print(ts.index)

#滞后或超前操作
price = pd.Series([20.34,20.56,21.01,20.65,21.34],\
                  index=pd.to_datetime(['2016-01-01','2016-01-02',\
                                        '2016-01-03','2016-01-04',\
                                        '2016-01-05']))
rate = (price-price.shift(1))/price.shift(1)
print(rate)
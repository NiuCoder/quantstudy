# -*- coding: utf-8 -*-
#随机变量
import numpy as np
import pandas as pd
import os
os.chdir('D:\\pythonworkspace\\quantstudy\\quantbook\\014')

#生成100个随机数，指定可能取值以及相应的概率
RandomNumber = np.random.choice([1,2,3,4,5],size=100,
                                replace=True,p=[0.1,0.1,0.3,0.3,0.2])
print(RandomNumber)
print(pd.Series(RandomNumber).value_counts())

#以2014年沪深300指数的日收益率序列为例，说明如何用python估计概率分布
HSRet300 = pd.read_csv('return300.csv')
#查看其结构
print(HSRet300.head(n=2))

import matplotlib.pyplot as plt
from scipy import stats

#根据样本计算概率密度，
density = stats.kde.gaussian_kde(HSRet300.iloc[:,1])
bins = np.arange(-5,5,0.02) #设定分割区间

plt.subplot(211)
plt.plot(bins,density(bins))
plt.title('沪深300收益率序列的概率密度曲线图')

plt.subplot(212)
plt.plot(bins,density(bins).cumsum())
plt.title('沪深300收益率序列的累积分布函数图')

#生成二项分布随机数，感觉不是二项分布啊？？
np.random.binomial(100,0.5,20)

#求100次试验，有20次正面朝上的概率
print(stats.binom.pmf(20,100,0.5))
print(stats.binom.pmf(50,100,0.5))

#求解100次试验，小于20次的概率
dd = stats.binom.pmf(np.arange(0,21,1),100,0.5)
print(dd.sum())

#也可以用binom类的cdf函数求解
print(stats.binom.cdf(20,100,0.5))

ret = HSRet300.iloc[:,1]
#估算沪深300上涨的概率p
p=len(ret[ret>0])/len(ret)
print(p)
#估算10个交易日中，有6个交易日中上涨的概率
prob=stats.binom.pmf(6,10,p)
print(prob)

#生成5个标准正态分布随机数
Norm=np.random.normal(size=5)
print(Norm)
#求生成的正态分布随机数的密度值
print(stats.norm.pdf(Norm))
#求正态分布随机数的累积密度值
print(stats.norm.cdf(Norm))

#沪深300收益率序列的均值和方差
HS300_RetMean=ret.mean()
HS300_RetVariance=ret.var()
#查询累积密度值为0.05的分位数
print(stats.norm.ppf(0.05,HS300_RetMean,HS300_RetVariance**0.5))

#上证综指和深证综指的日收益率相关性
TRD_Index = pd.read_table('TRD_Index.txt',sep='\t')
SHindex = TRD_Index[TRD_Index.Indexcd==1]
SHindex.head(3)

SZindex = TRD_Index[TRD_Index.Indexcd==399106]
SZindex.head(3)

plt.scatter(SHindex.Retindex,SZindex.Retindex)
plt.title('上证综指与深证成指收益率的散点图')
plt.xlabel('上证综指收益率')
plt.ylabel('深证成指收益率')

#收益率相关系数
SZindex.index=SHindex.index
SZindex.Retindex.corr(SHindex.Retindex)

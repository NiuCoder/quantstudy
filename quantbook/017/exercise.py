# -*- coding: utf-8 -*-
import os
os.chdir('D:\\pythonworkspace\\quantstudy\\quantbook\\017')

import pandas as pd
TRD_Index = pd.read_table('TRD_Index.txt',sep='\t')
SHindex = TRD_Index[TRD_Index.Indexcd==1]
SZindex = TRD_Index[TRD_Index.Indexcd==399106]
SHRet=SHindex.Retindex
SZRet=SZindex.Retindex
SZRet.index=SHRet.index

#构造上证综指与深证成指收益率的回归模型
import statsmodels.api as sm
model=sm.OLS(SHRet,sm.add_constant(SZRet)).fit()
#查看回归模型结果
print(model.summary())

import matplotlib.pyplot as plt
plt.scatter(model.fittedvalues,model.resid)
plt.xlabel('拟合值')
plt.ylabel('残差')

import scipy.stats as stats
sm.qqplot(model.resid_pearson,stats.norm,line='45')

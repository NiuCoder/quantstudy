# -*- coding: utf-8 -*-
import os
os.chdir('D:\\pythonworkspace\\quantstudy\\quantbook\\016')

import pandas as pd
import statsmodels.stats.anova as anova
from statsmodels.formula.api import ols

year_return = pd.read_csv('TRD_Year.csv',encoding='gbk')
year_return.head()

#接着进行方差分析
model = ols('Return ~ C(Industry)',data=year_return.dropna()).fit()
table1 = anova.anova_lm(model)
print(table1)
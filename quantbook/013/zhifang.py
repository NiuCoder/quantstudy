# -*- coding: utf-8 -*-
#显示直方图
import os
os.chdir('D:\\pythonworkspace\\quantstudy\\quantbook\\013')
import pandas as pd
returns = pd.read_csv('retdata.csv')

gsyh = returns.gsyh

import matplotlib.pyplot as plt
plt.hist(gsyh)


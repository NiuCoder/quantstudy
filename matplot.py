# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#构建表格数据，假定为某股票每天的开盘收盘最高最低价以及成交量
#数据是伪造的，忽略最终划出的结果
df = pd.DataFrame(2+np.random.rand(366,4),
                  index=pd.date_range('20160101',periods=366),
                  columns=['Open','High','Low','Close'])
s1 = pd.Series(np.random.randint(4000000,8000000,366),
               index=pd.date_range('20160101',periods=366))
df['Volume'] = s1
print(df)

Close = df.Close

plt.plot(Close['2016'])


plt.plot([1,1,0,0,-1,0,1,1,-1])
plt.ylim(-1.5,1.5)
plt.xticks(range(9),\
    ['2015-02-01','2015-02-02',\
    '2015-02-03','2015-02-04',\
    '2015-02-05','2015-02-06',\
    '2015-02-07','2015-02-08',\
    '2015-02-09'],rotation=45)
plt.title('中国银行2016年收盘价曲线')
plt.xlabel('日期')
plt.ylabel('收盘价')

#增加背景grid，只增加横向的，如果双方向的用both
plt.grid(True,axis='y')

#可以在画图的时候指定线条类型
plt.plot([1,1,0,0,-1,0,1,1,-1],label='收盘价',linestyle='solid')
plt.plot([0,0,1,1,0,0,-1,-1,1],label='开盘价',ls='-')
#显示图例
plt.legend()

#柱状图
plt.bar([2,3,4,5],[1,2,3,4])
#饼状图
plt.pie([2,3,4,5],labels=('(2,3]','(3,4]','(4,5]','(5,6]'),\
        colors=('b','g','r','c'),shadow=False)


# -*- coding: utf-8 -*-
#dataframe是共享同一个index的Series集合，可以看成表格

import numpy as np
import pandas as pa
import pymysql

dates = ['2016-01-01','2016-01-02','2016-01-03',
         '2016-01-04','2016-01-05','2016-01-06']

dates = pa.to_datetime(dates)

print(dates)

# 跟Series相比多了一个columns，指定不同列的列名，将Series从一维扩展成多维
df = pa.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

#从文件读取数据，不指定列名
df2 = pa.read_table('data.txt',sep='\t',header=None,names=None)
print(df2)

#从文件读取数据，指定列名
df3 = pa.read_table('data.txt',sep='\t',names=list('ABCDE'))
print(df3)

#从数据库读取数据
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                       passwd='',db='mystudy')
cur = conn.cursor()
#cur.execute("SELECT * FROM user")
#for r in cur.fetchall():
#    print(r)
#conn.close()

#从数据库读到dataframe中
df4 = pa.read_sql('select * from user limit 10;',con=conn)
conn.close()
print(df4)
print(df4.head(4))
print(df4.columns)
print(df4.index)
print(df4.values)
print(df4.describe())

print(df4['name'])

#提取一行或者几行
print(df[1:3]) #提取前两行
print(df['A']) #提取单独一列
print(df[['A','C']]) #提取AC两列
print(df.loc[:,'A']) #提取A列
print(df.loc[dates[0:2],'A':'C']) #提取前两行的A到C列
print(df.loc[dates[0],'A']) #提取特定的标量


#DataFrame的操作
print(df)
print(df.T)  #转置
print(df.sort_index(axis=1,ascending=False)) #按照列名排序
print(df.sort_values(by='C',ascending=False)) #按照某一列的值降序排列
print(df.rank(axis=0))  #排名函数

#增加行或列
s1 = pa.Series([1,2,3,4,5],index=pa.date_range('20160102',periods=5))
print(s1)
#新增一列
df['E']=s1
print(df)
df1 = pa.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]},\
                    index=pa.date_range('20160110',periods=3))
print(df1)
#合并操作--纵向
df.append(df1)
print(df)

#删除操作
print(df.drop(dates[1:3]))
#删除某列
print(df.drop('A',axis=1))

#变动原DataFrame
#del df['A']
#print(df)

#替换操作
#df.loc[dates[2],'C']=0   #标签索引替换
#df.iloc[0,4] = 0         #位置索引替换
#df.loc[:,'B'] = np.arange(0,len(df)) #整列替换

#映射
print(df.apply(max,axis=0))
f = lambda x:x.max()-x.min()
print(df.apply(f,axis=1))

#可以对dataframe中的缺失值NaN进行填充（替换）
df5 = pa.DataFrame(np.random.randn(5,4),
                   index=list('abcde'),
                   columns=list('ABCD'))
df5.ix['c','A']=np.nan
df5.ix['c':'d','C']=np.nan
print(df5)

#指定数值填充空缺值
df5.fillna(0)
#前一个观测值填充，列方向
df5.fillna(method='ffill')
#后一个观测值填充，列方向
df5.fillna(method='bfill')
#后一个观测值填充，行方向
df5.fillna(method='backfill',axis=1)

#缺失值的选择删除
df5.dropna(axis=0) #行方向有缺失值就删除
df5.dropna(axis=1,thresh=3) #列方向多于3个缺失值删除

#删除重复数据
df6=pa.DataFrame({'c1':['apple']*3+['banana']*3+['apple'],
                  'c2':['a','a',3,3,'b','b','a']})
df6.drop_duplicates()




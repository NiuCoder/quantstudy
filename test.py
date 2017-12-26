# -*- coding: utf-8 -*-

import numpy as np
import pandas as pa

df = pa.DataFrame({'id':['a','b','c','d','e','f']})
print(df)

s1 = pa.Series(['Alice','Bob','Charlie','David','Esther','Fanny'])
print(s1)

s2 = pa.Series(['34','36','30','29','32','36'])
print(s2)
df['name']=s1
df['age']=s2
print(df)

df2 = pa.DataFrame({'id':['g']},index=['6'])
s3 = pa.Series(['John'],index=['6'])
s4 = pa.Series(['19'],index=['6'])
df2['name']=s3
df2['age']=s4
print(df2)
df3 = df.append(df2)
print(df3)

#重置索引
new_index = df3['age']
df4 = df.reindex(columns=new_index)

print(df4)
print(df4.drop(2))
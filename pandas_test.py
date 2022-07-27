import numpy as np
import pandas as pd
x=pd.Series([3,2,5,7])
print(x)
print(type(x))
print(x.index)
print(x.values)

x=pd.Series([1,3,4,7,3], index=['a','b','c','d','e'])
print(x)
print(x.index)

x.index={'가','나','다','라','마']
x

data={'kim':80,'lee':75, 'park':90, 'choi':65}
s1=pd.Series(data)
s1


s1.name='Seri'
s1.index.name='Names'
s1

s1['kim':'park']

s2=pd.Series([10,20,79,66,90])
s2[1:3]

s1[['kim','park']]

names=['민준','현우','서연','동현','지현']
years=[2013, 2012, 2014, 2015, 2013]
points=[1.5, 1.7, 3.6, 2.4, 2.9]
data={'name':names, 'year':years, 'point':points}

df=pd.DataFrame(data)
df

data=[['민준','현우','서연','동현','지현'],[2013, 2012, 2014, 2015, 2013],[1.5, 1.7, 3.6, 2.4, 2.9]]
df1=pd.DataFrame(data).transpose()
df1.columns=['name','year','point']
df1
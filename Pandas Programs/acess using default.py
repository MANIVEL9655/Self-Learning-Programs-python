import pandas as pd

s=pd.Series(data= ['a',10,20,'c','d'],index=['b','c','d','e','a'])
print(s)
print(s['b'])
print(s[1])
print(s['a'])
print(s['e'])
print(s[4])
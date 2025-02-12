import numpy as np
import pandas as pd
d={'Name':pd.Series(['Tom','Lily',"King",'Michel','Roshan','Karukuty',"Lee","Sambath","Krish","Valli","Naidu"]),
   'Age':pd.Series([12,34,56,78,90,15,45,66,77,33,18]),
   'Ratings':pd.Series([12,34,55,3,4,2,5,6,0,45,32,1])}
df=pd.DataFrame(d)
print(df.count())
print(df.sum())
print(df.mean())
print(df.median())
print(df.std())
print(df.max())
print(df.min())
print(df.avg())
print(df.cumsum())
print(df.cummax())
print(df.cumprod())
print(df.cummin())
print(df.abs())
print(df)
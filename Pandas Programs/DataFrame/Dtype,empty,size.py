import numpy as np
import pandas as pd
d={'Name':pd.Series(['Tom','Lily','Charu','Michel','Roshan','Kannan','Karukuty']),
   'Age':pd.Series([12,34,56,78,90,15]),
   'Marks':pd.Series([56,34,56,78,99,100])}
df=pd.DataFrame(d)
print(df)
print("==================================================")
print(df.dtypes)
print("==================================================")
print(df.empty)
print("==================================================")
print(df.ndim)
print("==================================================")
print(df.values)
print("==================================================")
print(df.head())
print("==================================================")

print(df.tail())
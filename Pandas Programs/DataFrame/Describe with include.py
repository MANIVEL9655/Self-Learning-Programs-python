import numpy as np
import pandas as pd
d={'Name':pd.Series(['Tom','Lily',"King",'Michel','Roshan','Kannan','Karukuty',"Lee","Sambath","Krish","Valli","Naidu"]),
   'Age':pd.Series([12,34,56,78,90,15,45,66,77,44,33,18]),
   'Ratings':pd.Series([12,34,55,3,4,2,5,6,0,45,32,1])}
df=pd.DataFrame(d)
print(df)
print("3333333333333333333333333333333333333333333")
print(df.describe(include='object'))
print("==============================================")
print(df.describe(include='number'))
print("==============================================")
print(df.describe(include='all'))
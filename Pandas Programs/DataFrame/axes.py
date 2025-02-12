import numpy as np
import pandas as pd
d={'Name':pd.Series(['Tom','Lily','Charu','Michel','Roshan','Kannan','Karukuty']),
   'Age':pd.Series([12,34,56,78,90,15]),
   'Marks':pd.Series([56,34,56,78,99,100])}
df=pd.DataFrame(d,dtype=object)
print(df)
print("Axes of the matrix")
print(df.axes)
print(type(df))
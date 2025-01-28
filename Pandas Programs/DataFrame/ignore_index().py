import pandas as pd
from isapi.samples.redirector_with_filter import proxy

df1=pd.DataFrame([[1,2],[3,4]],columns=['a','b'],index=["Row1","Row2"])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
print(df1)
print("==============================")
print(df2)
print("===========================")
df=df1._append(df2,ignore_index=True)
print(df)
print("===============================")

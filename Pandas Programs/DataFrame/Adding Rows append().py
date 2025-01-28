import pandas as pd
df1=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
print(df1)
print("===========================")
df=df1._append(df2)
print(df)
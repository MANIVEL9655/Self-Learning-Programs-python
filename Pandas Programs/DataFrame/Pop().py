from operator import index

import pandas as pd
data={'One':pd.Series([1,2,3],index=["Row1","Row2","Row3"]),"Two":pd.Series(
    [1,2,3,4],["Row1","Row2","Row3","Row4"])}
df=pd.DataFrame(data=data)
print("=================================")
print("Addomg n columns by passing series")
df['Three']=pd.Series([10,20,30],index=["Row1","Row2","Row3"])
print(df)
print("==========================")
df['Total']=df['One']+ df['Three']
print(df)
print("===============================")
print(df.pop("One"))

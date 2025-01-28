from operator import index

import pandas as pd
data={'Name':pd.Series(['Kamal','Vishnu','Selva','Rajesh','Yogie'],index=["Row1","Row2","Row3","Row4","Row5"]),"Age":pd.Series(
    [10,20,30,40,50],["Row1","Row2","Row3","Row4","Row5"]
)}
df=pd.DataFrame(data=data,copy=True,columns=["Name","Age"])
df['Marks']=pd.Series([23.4,55.6,56,66,90],index=["Row1","Row2","Row3","Row4","Row5"])
print(df)
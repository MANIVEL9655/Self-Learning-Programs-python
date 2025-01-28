from operator import index

import pandas as pd
data={'Name':pd.Series(sorted(['Kamal','Vishnu','Selva','Rajesh','Yogie']),index=["Row1","Row2","Row3","Row4","Row5"]),"Age":pd.Series(
    [10,20,30,40,50],["Row1","Row2","Row3","Row4","Row5"]
)}
df=pd.DataFrame(data=data,copy=True,columns=["Name","Age"])
df['Marks']=pd.Series(sorted([3.4,55.6,5,66,90]),index=sorted(["Row1","Row2","Row3","Row4","Row5"]))
print(df)